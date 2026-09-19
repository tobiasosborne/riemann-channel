# Lane L12: lab book shards 01 to 04g

## Coverage

| file | lines | read fully? | ideas found |
| --- | --- | --- | --- |
| report/sections/01_conventions_notation.tex | 128 | yes | 2 (L12-001, L12-002) |
| report/sections/02_definitions.tex | 180 | yes | 4 (L12-003 .. L12-006) |
| report/sections/02b_definitions_arithmetic.tex | 279 | yes | 8 (L12-007 .. L12-014) |
| report/sections/02c_definitions_phantasm.tex | 114 | yes | 6 (L12-015 .. L12-020) |
| report/sections/02d_definitions_complexes.tex | 151 | yes | 5 (L12-021 .. L12-025) |
| report/sections/02e_definitions_symmetry.tex | 62 | yes | 3 (L12-026 .. L12-028) |
| report/sections/02f_definitions_graded_cmps.tex | 72 | yes | 1 (L12-029) |
| report/sections/02g_definitions_ring_norm_tensor.tex | 86 | yes | 4 (L12-030 .. L12-033) |
| report/sections/02h_definitions_graded_ramanujan.tex | 156 | yes | 8 (L12-034 .. L12-041) |
| report/sections/03_what_rh_has_become.tex | 298 | yes | 10 (L12-042 .. L12-051) |
| report/sections/03b_graded_permutation.tex | 307 | yes | 11 (L12-052 .. L12-062) |
| report/sections/03c_graded_ramanujan.tex | 250 | yes | 10 (L12-063 .. L12-072) |
| report/sections/03d_graded_ramanujan_continuum.tex | 202 | yes | 11 (L12-073 .. L12-083) |
| report/sections/03e_selberg_letters.tex | 229 | yes | 9 (L12-084 .. L12-092) |
| report/sections/03f_selberg_letters_finite.tex | 165 | yes | 8 (L12-093 .. L12-100) |
| report/sections/04_riemann_channel.tex | 319 | yes | 8 (L12-101 .. L12-108) |
| report/sections/04b_phantasm_forced.tex | 292 | yes | 8 (L12-109 .. L12-116) |
| report/sections/04c_phantasm_channels.tex | 265 | yes | 11 (L12-117 .. L12-127) |
| report/sections/04d_bc_symmetry_generators.tex | 236 | yes | 10 (L12-128 .. L12-137) |
| report/sections/04e_cmps_parity_overlap.tex | 246 | yes | 2 (L12-138, L12-139) |
| report/sections/04f_cmps_twisted_supertrace.tex | 222 | yes | 5 (L12-140 .. L12-144) |
| report/sections/04g_phase_side_lindbladian.tex | 189 | yes | 9 (L12-145 .. L12-153) |

Note on 02c/02d: those two files were read in one concatenated pass; 02d's own line numbering runs 1-151
and its definitions appear at concatenated lines 115-265. Line citations below for 02d name the definition
label as well as the line, so they can be located either way.

Cross-check against `db/claims.tsv`: every claim row whose shard column is one of these files and whose
status is `open`, `conjectured`, `assumed` or `sketched` appears below. The `open` conjectures
`conj:phantasm-both-halves` and `conj:galois-graded-bond` are registered in shard 10 (outside this lane)
but are *raised* inside my files and are entered here (L12-125, L12-127).

## Ideas and leads

### L12-001 One critical modulus sqrt(q) shared by three unrelated roles of the size parameter
- Source: report/sections/01_conventions_notation.tex:27-31
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (recorded as a convention)
- Content: The single letter q plays three roles that never co-occur: the field size for Artin-Schreier curves, the LPS prime for the Weil-LPS channels, and D-1 for a channel with D Kraus operators. The note observes that "in every role the critical modulus is sqrt(q)". That is stated as bookkeeping, but it asserts that three unrelated families of examples have the same critical circle.
- Lead: none stated. If the coincidence were made a theorem (one construction specialising to all three), it would be the "mechanism" the book repeatedly says is missing.
- Related: L12-005, L12-063, L12-072.

### L12-002 Reading the notes' two-value "established / not established" as sketched versus open
- Source: report/sections/01_conventions_notation.tex:63-68
- Raised by: orchestrator (Claude)
- Status at last mention: settled convention
- Content: The prior-art verdict vocabulary (SAME / RELATED / NOT) is confined to the prior-art section and read as provenance, while the notes' "established / not established" is mapped onto sketched/numerical versus open. This is the rule by which every earlier informal claim in the notebook acquired a status.
- Lead: none stated.
- Related: -

### L12-003 A "small matrix" exists exactly when the zeta function is rational
- Source: report/sections/02_definitions.tex:39-47; report/sections/03_what_rh_has_become.tex:50-71
- Raised by: orchestrator (Claude), from the founding session with TJO
- Status at last mention: registered as sketched (obs:rh-small-matrix)
- Content: For a shift or permutation with fixed-point counts fix(l), a small matrix is any M with Tr M^l = fix(l) for all l. It exists exactly when the zeta function is rational, and its eigenvalues are new numbers, not those of the permutation matrix. RH then becomes: every subleading eigenvalue has modulus the square root of the leading one.
- Lead: for the primes the zeta is not rational, so the small matrix must become a semigroup in continuous length; the whole side-B programme is the search for that semigroup with extra structure.
- Related: L12-045, L12-048.

### L12-004 The one identity read as a bosonic partition function and a gas of rings
- Source: report/sections/02_definitions.tex:30-37; report/sections/03_what_rh_has_become.tex:19-39
- Raised by: orchestrator (Claude), founding session
- Status at last mention: registered as sketched (obs:one-identity)
- Content: 1/det(1-uM) is simultaneously a product over eigenvectors (one bosonic mode each, Boltzmann factor lambda_i u) and exp(sum_l Tr M^l u^l / l) (a sum over closed walks carrying the 1/l of a ring's rotation symmetry). "One object, two descriptions: a gas of modes and a gas of rings." For a permutation the ring side collapses to an Euler product over cycles, and the primes will be the cycles.
- Lead: the tension between the two sides is declared "the whole subject"; the concrete step is to find which state has the primes as its rings.
- Related: L12-052, L12-109.

### L12-005 The RH analogue for an MPS: one correlation length equal to 2/entropy
- Source: report/sections/02_definitions.tex:49-58, 147-153; report/sections/03_what_rh_has_become.tex:121-141
- Raised by: TJO (founding session), written up by the orchestrator
- Status at last mention: registered as sketched (obs:rh-mps-correlation-length)
- Content: In canonical form the subleading transfer eigenvalues are exp(-1/xi_k + i phi_k). Translating the graph statement (leading growth q, subleading modulus sqrt q) gives xi_k = 2/log q = 2/S for every k. So RH for an MPS says all correlation lengths are equal and equal to twice the inverse entropy rate; the phases are unconstrained and there may be infinitely many.
- Lead: build the state; the phases gamma_n are then free data and only the moduli are pinned. Every later construction is tested against this shape.
- Related: L12-003, L12-046, L12-049.

### L12-006 The quantum Ihara zeta is the Artin-Ihara L-function of a bouquet twisted by Ad(U)
- Source: report/sections/02_definitions.tex:104-111, 170-180
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definition, used throughout
- Content: For a mixed-unitary channel with E_i = Ad(U_i) and U_{ibar} = U_i^dagger, the quantum Ihara zeta det(1-uT)^{-1} of the quantum Hashimoto operator is exactly the Artin-Ihara L-function of the bouquet (free fundamental group, one operator per loop) twisted by the holonomy Ad o U.
- Lead: this bridge lets graph L-function technology (Bass formula, Artin factorisation) apply to channels; the Artin factorisation is later used in L12-071.
- Related: L12-065, L12-071.

### L12-007 The Riemann channel as a CP semigroup, and the loose use of the name
- Source: report/sections/02b_definitions_arithmetic.tex:31-38; report/sections/04_riemann_channel.tex:83-88
- Raised by: orchestrator (Claude), founding session
- Status at last mention: registered as a definition; the CP lift is called "immediate and uninformative"
- Content: The Riemann channel is rho -> Z_t^* rho Z_t on B(K_S), a single-Kraus CP semigroup whose modes are the zeros and whose distributional trace is the prime measure. The name is also used loosely for the whole side-A/side-B package.
- Lead: find a non-trivial Kraus decomposition; that is conj:stinespring-jump-form (L12-105).
- Related: L12-105, L12-117.

### L12-008 Weil positivity as a Bochner statement on the dilation group
- Source: report/sections/02b_definitions_arithmetic.tex:77-83; report/sections/03_what_rh_has_become.tex:246-252
- Raised by: a classical criterion (Weil), imported
- Status at last mention: registered as a definition; used as the positivity face of RH
- Content: RH holds iff F_weil(u) = sum over zeros of exp((rho-1/2)u) is positive definite on the dilation group, iff its spectral measure is a positive measure, which by Bochner is the same as all its atoms being real.
- Lead: "Proving it would mean exhibiting that state, or a Stinespring form of Z_t with the prime dilations as Kraus operators, in a way that makes the positivity manifest."
- Related: L12-012, L12-051, L12-105.

### L12-009 The Hecke relation: Weil-LPS channels for different q commute
- Source: report/sections/02b_definitions_arithmetic.tex:114-120
- Raised by: orchestrator (Claude), from LPS/Hecke theory
- Status at last mention: registered as a definition; the associated conj:weil-lps-hecke is open (shard 05, outside this lane)
- Content: The LPS Cayley adjacency operators satisfy A_q^2 - q = A_{q^2} and A_{q1}A_{q2} = A_{q1q2}: the tree relations "two steps without backtracking" and multiplicativity. Consequently the Weil-LPS channels for different q commute.
- Lead: a commuting family of quantum expanders indexed by primes is exactly the shape of a Hecke algebra acting on one bond; if the relation holds at the channel level, one gets an arithmetic rigidity source for channels.
- Related: L12-070, L12-001.

### L12-010 Dwork's operator as a second, p-adic side-B transfer for exponential sums
- Source: report/sections/02b_definitions_arithmetic.tex:141-147
- Raised by: orchestrator (Claude), from Dwork's method
- Status at last mention: registered as a definition; not developed inside my shards
- Content: Dwork's operator is decimation composed with multiplication by the splitting function on p-adic power series; the exponential sums are its traces and the curve L-function its Fredholm determinant. It is an alternative side-B operator for the same counts as the Artin-Schreier transfer matrix.
- Lead: none stated inside my shards. The relation between the p-adic and the complex transfer operator for the same curve is never compared here.
- Related: L12-019, L12-115.

### L12-011 Slicing, big monodromy and "the sign" as the Deligne-style route to rigidity
- Source: report/sections/02b_definitions_arithmetic.tex:149-160; report/sections/03_what_rh_has_become.tex:237-244, 269-273
- Raised by: orchestrator (Claude), from Deligne/Katz vocabulary
- Status at last mention: raised as the vocabulary of the wanted mechanism; never instantiated
- Content: "Slicing" writes the middle block of a variety as the interesting block of a base curve with coefficients from hyperplane sections; "big monodromy" says the only invariants of even tensor powers are the pairwise contractions; "the sign" is the minus with which the interesting block enters the count. The book states that being Ramanujan is never a consequence of structure, that in every known case it comes from arithmetic input of Deligne's type, and that "some arithmetic rigidity has to enter, playing the role that weights play for curves."
- Lead: import a big-monodromy / weight argument into the channel setting. No instance is constructed anywhere in my files; this is the largest standing gap.
- Related: L12-050, L12-072, L12-116.

### L12-012 The rescaled trace sequence, the Weil form and the mode-pairing form
- Source: report/sections/02b_definitions_arithmetic.tex:233-258
- Raised by: orchestrator (Claude) with the Weil-positivity lane
- Status at last mention: registered as definitions, feeding the (out-of-lane) Weil-window shards
- Content: For an operator X, a designated trivial set and a critical radius r, the rescaled trace sequence is nu_l = r^{-l}(Tr X^l minus the trivial part), extended by conjugation. The Weil form is the Toeplitz form built from nu; the mode-pairing form pairs each retained mode lambda with its reflection r^2/conj(lambda) in the critical circle. Positive definiteness of the Toeplitz form is the finite-dimensional Weil criterion.
- Lead: prove that positivity of the Weil form forces the retained spectrum onto the critical circle in a setting where the letters supply the form. (The windowed version continues in shard 08g, outside this lane.)
- Related: L12-008, L12-013, L12-097.

### L12-013 The continuous rescaled trace and reflection in a vertical line
- Source: report/sections/02b_definitions_arithmetic.tex:269-278
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definition
- Content: The generator analogue of L12-012: F(t) = e^{-a t}(Tr e^{tL} minus the trivial part), reflection R_a(lambda) = 2a - conj(lambda) in the line Re = a, positive definiteness in the Bochner sense on real times.
- Lead: this is the object one would need to control for a Lindbladian Phantasm; nothing in my files tests it against an actual generator.
- Related: L12-012, L12-078.

### L12-014 Adjoint pairing versus inverse pairing of Kraus letters
- Source: report/sections/02b_definitions_arithmetic.tex:260-267; report/sections/03f_selberg_letters_finite.tex:54-61, 87-89
- Raised by: orchestrator (Claude); sharpened by the codex prover (ledger L36)
- Status at last mention: settled distinction; the Hashimoto-lift theorem holds in the inverse-paired setting only
- Content: A family E_i = Ad(B_i) is adjoint-paired if B_{ibar} = B_i^dagger and inverse-paired if B_{ibar} = B_i^{-1}. The Kraus families of the quantum Hashimoto construction are adjoint-paired; cor:qihara-unitary needs inverse pairing. The prover notes that thm:hashimoto-lift-metric "is not a theorem for arbitrary Hermitian CP channels without such a lift."
- Lead: extend the letter-derived metric to adjoint-paired but non-invertible letters, i.e. to genuinely dissipative channels. Stated as a gap, not attempted.
- Related: L12-097, L12-099.

### L12-015 Supertrace distribution and net multiplicity as the only observable data
- Source: report/sections/02c_definitions_phantasm.tex:14-25; report/sections/04b_phantasm_forced.tex:73-86
- Raised by: orchestrator (Claude); proved by the codex prover
- Status at last mention: proved (thm:supertrace-rigidity)
- Content: A graded spectral datum is a multiset of (lambda, parity) pairs; its supertrace distribution is the signed exponential sum and its net multiplicity is m(+) - m(-). Two data with the same supertrace have the same net multiplicity everywhere: ring norms see the net graded spectrum and nothing else, "not Jordan blocks, not the Hilbert-space geometry, not the operator domain."
- Lead: any construction matching the prime measure is pinned only up to cancelling pairs, so extra structure (positivity, a Kraus realisation, a metric) is exactly what must be added to get more.
- Related: L12-110, L12-144.

### L12-016 The distributional trace of Z_t is a definition by fiat, not a trace theorem
- Source: report/sections/02c_definitions_phantasm.tex:27-34; report/sections/04b_phantasm_forced.tex:281-289
- Raised by: orchestrator (Claude), flagged by the Opus reviewer
- Status at last mention: recorded as a scope limitation
- Content: Tr_d Z_t := sum over zeros of exp(-conj(rho)t/2) is declared to be a distribution on (0, infinity); "this is a definition by fiat, not an application of a trace theorem to Z_t". Z_t is not trace class for t > 0.
- Lead: supply an actual trace-class or regularised-determinant statement; until then every "trace" identity in the Riemann channel is formal.
- Related: L12-078, L12-112.

### L12-017 The Riemann graded bond with an archimedean ladder in the odd part
- Source: report/sections/02c_definitions_phantasm.tex:36-42; report/sections/04b_phantasm_forced.tex:255-270
- Raised by: orchestrator (Claude); proved conditionally by the codex prover
- Status at last mention: registered as proved-conditional (prop:riemann-graded-generator)
- Content: The bond is an even line plus (K_S plus l^2(N)) odd; the generator is 0 on the even line, B on K_S, and diag(-(k+1/2)) on the ladder. Its supertrace is exactly twice the positive-time prime measure. "The odd K_S part is the Riemann channel; the missing even fixed line is the pole; the ladder is the archimedean place."
- Lead: realise this spectral datum as an actual doubled-bond cMPS transfer generator. Never supplied; explicitly listed as missing.
- Related: L12-078, L12-112, L12-143.

### L12-018 The prime-chain detailed-balance Lindbladian
- Source: report/sections/02c_definitions_phantasm.tex:55-66; report/sections/04c_phantasm_channels.tex:142-160
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, negative (real spectrum, no zeros)
- Content: Forward jumps mu_p (n -> pn) at rate r_p and reverse jumps at rate r_p p^beta give a multiplicative birth-death process with Gibbs fixed point N^{-beta}/zeta(beta). Its spectrum is a real union of M/M/1 bands and their Minkowski sums, containing no zero of zeta.
- Lead: dead as a source of zeros; kept as the side-A half of the Phantasm.
- Related: L12-121, L12-125, L12-149.

### L12-019 The Artin-Schreier ring form, radical and radical sign
- Source: report/sections/02c_definitions_phantasm.tex:78-91
- Raised by: orchestrator (Claude)
- Status at last mention: registered as definitions feeding the (out-of-lane) shard 06b
- Content: For g(x) = sum a_j x^{1+q^j}, the ring form Q(x) = x^t P_g(C) x with C the cyclic shift; the trace form with the Gram matrix of a normal basis; the radical ker P_g(C); its sign det(C restricted to the radical); and a period parameter h read off from the order of vanishing of z^J P_g(z) at z = -1.
- Lead: the sign and the period parameter are the combinatorial data controlling the exponential sum: a purely ring-theoretic (shift-on-a-cycle) description of curve counts. Not developed further here.
- Related: L12-010, L12-020, L12-115.

### L12-020 The Artin-Schreier super-transfer matrix and its symplectic/Weil structure
- Source: report/sections/02c_definitions_phantasm.tex:93-114; report/sections/04c_phantasm_channels.tex:223-233
- Raised by: orchestrator (Claude)
- Status at last mention: registered as definitions; the even/odd split by additive character is called an analogy, not a theorem
- Content: The super-transfer has even part (the de Bruijn adjacency matrix of memory J, plus the point at infinity) and odd part the sum over nontrivial additive characters of the Frobenius blocks; the point count is its supertrace. The transfer unitary conjugates centred Weyl operators by a symplectic map in Sp(2J, F_q), so it is a Weil implementer up to scalar.
- Lead: "a graded channel of circle type with a group-theoretic mechanism (odd block sqrt(q) times a unitary because of a representation, as in Artin-Schreier by Parseval)" is exactly the item listed as NOT understood in obs:graded-ramanujan-status.
- Related: L12-072, L12-115, L12-126.

### L12-021 Two competing higher-dimensional non-backtracking flows
- Source: report/sections/02d_definitions_complexes.tex, def:ordered-geodesic-flow and def:pointed-opposition-flow (concatenated lines 132-168)
- Raised by: orchestrator (Claude)
- Status at last mention: both registered; the fork is left open inside my shards
- Content: The ordered-cell flow drops the oldest vertex, appends a new one, and forbids the step a (k+1)-cell would short-cut; for d=1 it is exactly the Hashimoto operator. The pointed opposition flow instead uses opposition in the spherical link of a building and weights steps by u^{lambda_0}, an *algebraic* length. "Opposition is strictly stronger than the non-cell condition."
- Lead: decide which is the right higher-dimensional side B - intrinsic-for-any-complex versus building-specific with lengths. The continuation is shards 08d/08f, outside this lane.
- Related: L12-022, L12-025.

### L12-022 The graded geodesic determinant: grade a complex by cell dimension
- Source: report/sections/02d_definitions_complexes.tex, def:graded-geodesic-determinant (concatenated lines 170-192)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definition
- Content: Give the degree-k space parity k+1, insert the sign s_k = (-1)^{k+1} once per successor arrow, and define the total zeta as a superdeterminant over the whole graded space: odd k (edges) in the denominator, even k (chambers) in the numerator. The same grading trick as the Phantasm's, but with cell dimension as the parity.
- Lead: a complex's own dimension supplies a grading for free, so zeros of a complex's total zeta are structural rather than imposed. The connection back to the Phantasm's bond parity is never drawn in my files.
- Related: L12-021, L12-092, L12-140.

### L12-023 A Kraus connection on the 1-skeleton: twisting with no flatness or positivity assumed
- Source: report/sections/02d_definitions_complexes.tex, def:kraus-connection (concatenated lines 220-234)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definition; scope deliberately maximal
- Content: Assign an arbitrary endomorphism to each directed edge; it is a Kraus connection when the fibre is M_n and each E_e is completely positive. Flat means E_{yx} = E_{xy}^{-1} and E_{yz}E_{xy} = E_{xz} on every 2-cell; pure gauge means E = F_y F_x^{-1}. "No positivity, invertibility, pairing or flatness is assumed unless said."
- Lead: the interesting cases are the non-flat ones (curvature of a Kraus connection), which are defined but never explored inside my shards.
- Related: L12-024, L12-006.

### L12-024 The voltage quotient and its Artin block, distinguished from the connection on the cover
- Source: report/sections/02d_definitions_complexes.tex, def:voltage-quotient (concatenated lines 236-249)
- Raised by: orchestrator (Claude)
- Status at last mention: registered, with the explicit warning "This is not the same object as the connection ... on the full cover"
- Content: A free group action lets each transition be labelled by a voltage h in G; a unitary rho of G replaces the arrow by rho(h^{-1}), and the Artin determinant is the product over rho of det(I - s_k T_{k,rho})^{a_rho}.
- Lead: compare the two twisting notions (voltage/Artin block versus arbitrary Kraus connection) and find when they agree. Flagged as distinct, not compared.
- Related: L12-023, L12-071.

### L12-025 The exceptional space can be strictly larger than the fixed space on a partite complex
- Source: report/sections/02d_definitions_complexes.tex, def:ramanujan-quantum-expander-a2 (concatenated lines 251-265)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definitional subtlety
- Content: For a type-A-tilde graded quantum expander one must remove not just the common fixed space but the sum E_R of type-character subrepresentations excluded by the Ramanujan-complex convention. "Only when E_R = F_R is this the fixed-point-complement condition; on a partite complex E_R can be strictly larger."
- Lead: characterise when the collapse E_R = F_R happens - essentially conj:vertex-collapse-characterisation, registered in shard 08f outside this lane.
- Related: L12-021.

### L12-026 Matrix extensions of the finite BC phase marginal: the off-diagonal entries are free data
- Source: report/sections/02e_definitions_symmetry.tex:12-23; report/sections/04d_bc_symmetry_generators.tex:25-43, 60-74
- Raised by: TJO's specification, formalised by the codex prover / orchestrator
- Status at last mention: registered as sketched (prop:bc-symmetry-state-extension)
- Content: The BC state restricted to the phase algebra fixes only the diagonal of a density on l^2(F_p). Off-diagonal entries are additional data. Weil invariance picks out a unique extension aI + (r-a)Par, positive iff r <= 2/(p+1); full Weyl invariance forces I/p. "This does not specify a representation of the full BC algebra."
- Lead: the free off-diagonal data is where any coherence carrying the zeros would have to live; the covariance requirements are what kill it.
- Related: L12-129, L12-133.

### L12-027 Three distinct local arithmetic covariances, deliberately kept apart
- Source: report/sections/02e_definitions_symmetry.tex:25-38
- Raised by: orchestrator (Claude)
- Status at last mention: registered; used to prove the collapse L12-133
- Content: Galois-torus covariance (commuting with Ad(U_a)), linear symplectic covariance (commuting with Ad(Weil(g))), and Weyl-translation covariance (commuting with all Ad(W_v)). The note is explicit: "Weyl-translation covariance is an extra condition, not a consequence of carrying Weyl operators."
- Lead: this separation is what makes the cone dimensions informative: the first two allow large cones, adding the third collapses them.
- Related: L12-132, L12-133.

### L12-028 The conditional Choi matrix as the exact finite feasibility object
- Source: report/sections/02e_definitions_symmetry.tex:52-62; report/sections/04d_bc_symmetry_generators.tex:86-116
- Raised by: codex prover / orchestrator
- Status at last mention: registered as sketched (thm:bc-covariant-gks-cone)
- Content: Q C_L Q >= 0 with Q = I - |b><b| characterises exactly the GKLS generators; combined with Hermiticity preservation, trace annihilation, stationarity and covariance it turns "does a Riemann Lindbladian with these symmetries exist?" into a concrete positive-semidefinite cone question in finite dimension.
- Lead: the finite inverse problem is now computable; the missing input is the representation connecting the BC algebra to the scattering bond (L12-136).
- Related: L12-132, L12-136.

### L12-029 cMPS rings defined with no supercommutation regularity and no normalisation of Q
- Source: report/sections/02f_definitions_graded_cmps.tex, def:cmps-ring-vector (concatenated lines 96-114)
- Raised by: orchestrator (Claude, opus-5 lane)
- Status at last mention: deliberate scope choice
- Content: The boson-fermion cMPS ring vector is defined for arbitrary constant Q, R_a and boundary matrix B, with no regularity (supercommutation) condition and no normalisation of Q, so the overlap theorem applies to every such datum.
- Lead: the price is that Tcm_eta need not generate a positive semigroup (04e:242-246); a regularity condition may be needed before any Lindbladian reading.
- Related: L12-138, L12-139.

### L12-030 The ring zeta of a graded lattice tensor as 1/sdet, poles even and zeros odd
- Source: report/sections/02g_definitions_ring_norm_tensor.tex, def:graded-lattice-tensor (concatenated lines 150-171); report/sections/04f_cmps_twisted_supertrace.tex:138-155
- Raised by: orchestrator (Claude)
- Status at last mention: proved for finite bonds (thm:cmps-sdet, sketched-conditional)
- Content: The P-closed ring norm is str E^n = sum over words of |Tr(P A_{s1}...A_{sn})|^2, an unconditional identity by Kronecker multiplicativity; the ring zeta is 1/sdet(1-uE) = det(odd)/det(even). Net spectrum means after cancelling common even and odd eigenvalues; zero eigenvalues and nilpotent blocks are invisible to all positive powers.
- Lead: this is the engine of the whole "zeros from a grading" programme; everything later asks which gradings give which divisors.
- Related: L12-015, L12-140, L12-144.

### L12-031 The lifted Frobenius as a toral endomorphism, and the Hodge ket bond C^{1|1}
- Source: report/sections/02g_definitions_ring_norm_tensor.tex, def:lifted-frobenius-torus and def:elliptic-norm-tensor (concatenated lines 173-193)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as definitions feeding the genus-one result (shards 06d/06e, out of lane)
- Content: For an ordinary elliptic curve, Deuring lifting gives a lattice in C on which Frobenius acts by multiplication; its integral matrix induces a toral endomorphism of R^2/Z^2, and the Hodge ket bond is C + C dz = C^{1|1} with P = (-1)^deg, whose double is the full cohomology of the torus graded by total form degree. The elliptic norm tensor is all-even with A_s = a_s diag(1, pi) and P-closed ring vector (1 - pi^n) phi^{tensor n}.
- Lead: the arithmetic of the curve becomes a two-dimensional bond with a form-degree grading; the same form-degree grading is later identified on the Selberg side.
- Related: L12-032, L12-084, L12-115.

### L12-032 The genus-two bond C^{1|2} and the nine-letter tensor
- Source: report/sections/02g_definitions_ring_norm_tensor.tex, def:genus-two-bond and def:nine-letter-tensor (concatenated lines 195-219)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as definitions; the existence theorem and conj:three-letter-universal live in shard 06f, out of lane
- Content: For a genus-two curve with simple ordinary Jacobian and CM type Phi the bond is C + H^{1,0} = C^{1|2} with D = diag(pi_1, pi_2). An explicit nine-letter tensor realises the counts when q+1 >= 4 sqrt q, using five even letters built from a positive square root of w1_4 - b_0 b_0^* and four odd letters of weight sqrt h.
- Lead: whether three letters suffice universally is registered open elsewhere; the condition q+1 >= 4 sqrt q is a genuine constraint excluding small q.
- Related: L12-031, L12-030.

### L12-033 Even gauge freedom fixes every ring norm
- Source: report/sections/02g_definitions_ring_norm_tensor.tex, def:graded-lattice-tensor (concatenated lines 166-168)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a definition
- Content: A_s -> G A_s G^{-1} with G even and invertible conjugates the doubled transfer by G tensor conj(G) and fixes every ring norm. So the tensor is only ever determined up to even gauge.
- Lead: the gauge orbit is the right object to classify; together with Kraus uniqueness (L12-056) it says the physical datum is a channel plus a grading, not a tensor.
- Related: L12-056, L12-058.

### L12-034 The graded divisor as the object on which RH, FE, Ramanujan and Hilbert-Polya are stated
- Source: report/sections/02h_definitions_graded_ramanujan.tex:19-95
- Raised by: TJO's question of 2026-09-15, answered by the orchestrator; corrected repeatedly by the codex prover (ledger L28, L31-L33, L36, L41)
- Status at last mention: registered as the book's working definition
- Content: nu(lambda) = m_even - m_odd; nu > 0 are poles, nu < 0 zeros, nu = 0 invisible. (RH) is one-sided square-root cancellation on the retained divisor; (FE) is nu_ret(q/lambda) = nu_ret(lambda), with a stronger operator form (an even similarity J with J E J^{-1} = q E^{-1} that also matches Jordan data); (Ram) is two-sided, every retained point on the critical circle; (HP) is a Gdb-even positive form G with E^dagger G E = q G, a statement about the retained operators and not about the divisor alone. "(RH), (FE) and mixing are independent in general."
- Lead: state and check all four conditions on every example, and never conflate them.
- Related: L12-035, L12-036, L12-066.

### L12-035 The trivial divisor must be *signed*, with parities recorded not assumed
- Source: report/sections/02h_definitions_graded_ramanujan.tex:32-40
- Raised by: the codex prover (ledger L31, L41)
- Status at last mention: correction applied
- Content: The trivial divisor comprises q (even, simple), its period images zeta q (whose parities can be odd and so are recorded), the value 1 as the designated H^0 partner, the FE partners of these, and, in arithmetic cases, the archimedean or topological ladder. Accidental eigenvalues at a trivial value are retained with their own multiplicity. The prover's correction: "a value set of even modes is not the accurate object."
- Lead: any claim "the divisor is Ramanujan" must first name the signed trivial divisor; several earlier drafts did not.
- Related: L12-034, L12-084.

### L12-036 For a generator, the second reference rate must be supplied as extra data
- Source: report/sections/02h_definitions_graded_ramanujan.tex:41-46
- Raised by: the codex prover (ledger L36)
- Status at last mention: recorded as a structural requirement
- Content: In the channel normalisation the fixed point's rate is omega_0 = 0 and the critical line is the midpoint of (omega_0, omega_1). But a trace-preserving spectral bound alone gives 0 and does not determine omega_1: amplitude damping has centre -gamma/2 with spectral bound 0. So the critical line is not read off the channel; it is input.
- Lead: for the Riemann case the pair is (0, -1/2) and the centre -1/4; for any new example one must say where omega_1 comes from. An unresolved source of arbitrariness.
- Related: L12-078, L12-094.

### L12-037 Parity-twisted unitality and the P-mode, which is structural but not trivial
- Source: report/sections/02h_definitions_graded_ramanujan.tex:49-58; report/sections/03c_graded_ramanujan.tex:49-68
- Raised by: orchestrator (Claude); proved by the codex prover (D2)
- Status at last mention: registered as sketched (prop:p-mode)
- Content: A graded channel is parity-twisted unital with twisted eigenvalue lambda_P when sum_s eps_s K_s K_s^dagger = lambda_P; then P itself is an even eigenvector, and for a representation channel lambda_P is the sign character on the walk element. For the elliptic tensor lambda_P is the H^0 pole; for the Pauli letters it is -2, inside the Hastings band, and its Ihara-Bass quadratic contributes a pole pair on the critical circle; for all letters odd it is -q-1, the period image of the fixed point.
- Lead: the *balance condition* |w_even - w_odd| <= lambda_H is imposed on any unitary-letter Ramanujan candidate unless the P-mode is declared trivial. A concrete design constraint on the letters.
- Related: L12-063, L12-069.

### L12-038 Graded quantum expanders: the odd gap is not a single-step contraction bound
- Source: report/sections/02h_definitions_graded_ramanujan.tex:97-112
- Raised by: orchestrator (Claude), sharpened by the prover
- Status at last mention: registered as a definition
- Content: A graded quantum expander bounds even and odd eigenvalues separately. The odd gap bounds the asymptotic decay of parity coherences "with possible Jordan factors; it is not a single-step contraction bound". Also: the letter degree D is data, since repeated letters change the Hastings benchmark without changing the channel; the all-odd examples have the even mode P at -1 and are period two, not mixing.
- Lead: benchmarks against lambda_H are meaningful only once the letter multiset is fixed; repeating letters is a cheap way to fake Ramanujan-ness.
- Related: L12-067, L12-069.

### L12-039 The graded Hashimoto operator and the balanced grading
- Source: report/sections/02h_definitions_graded_ramanujan.tex:114-124
- Raised by: orchestrator (Claude)
- Status at last mention: registered; the (1-u^2) factors cancel exactly when D_+ = D_-
- Content: For unitary homogeneous letters closed under adjoint, the quantum Hashimoto operator commutes with Gdb, so the graded quantum Ihara zeta is det(1-uT_1)/det(1-uT_0), the ring zeta of the periodic non-backtracking rings, with str T^n = sum over cyclically non-backtracking words of |Tr(P U_w)|^2.
- Lead: balanced gradings are the clean case; unbalanced ones carry a (1-u^2) power of exponent (D-2)(D_+ - D_-)^2/2.
- Related: L12-065, L12-030.

### L12-040 Index-two (Clifford) gradings as the recipe for making a representation channel graded
- Source: report/sections/02h_definitions_graded_ramanujan.tex:126-140; report/sections/03c_graded_ramanujan.tex:149-179
- Raised by: orchestrator (Claude)
- Status at last mention: registered; the mechanism theorem is thm:graded-harrow (sketched)
- Content: Take G with an index-two subgroup G_0 and sign character eps. If an irreducible pi restricts reducibly, put P = +1 on pi_+ and -1 on pi_-, so P pi(g) P = eps(g) pi(g): elements of G_0 are even letters and elements of the odd coset are odd letters. Examples: PGL_2(F_p) over PSL_2(F_p) with eps the Legendre symbol of the determinant, and the Pauli group (not its abelian quotient, whose two-dimensional representation is projective; ledger L09) with G_0 = <iI, Z>.
- Lead: this is the only mechanism the book has for producing graded quantum expanders; look for other index-two pairs. The archimedean case is L12-081.
- Related: L12-068, L12-081.

### L12-041 Graded CP transfer versus graded spectral transfer
- Source: report/sections/02h_definitions_graded_ramanujan.tex:88-95, 142-156
- Raised by: the codex prover lane ("Definitions: verdict")
- Status at last mention: recorded as a permanent distinction; the missing Kraus realisations are a central open item
- Content: A graded CP transfer has a supplied Kraus realisation; a graded spectral transfer is only a graded operator with a divisor. The Artin-Schreier super-transfer, the Riemann graded generator, and the Selberg stable transverse complex are all of the second kind, and "only the divisor statements apply to them".
- Lead: supply a doubled-bond Kraus realisation for any one of the three. Listed as not understood in obs:graded-ramanujan-status and obstructed by the dimension count of L12-082.
- Related: L12-082, L12-089, L12-143.

### L12-042 The pairing comes from a symmetry, the hypothesis from a bound
- Source: report/sections/03_what_rh_has_become.tex:110-119
- Raised by: orchestrator (Claude), founding session
- Status at last mention: the book's standing slogan
- Content: For a graph, mu mu' = q is a functional equation pairing eigenvalues symmetrically about sqrt(q) on a log scale; RH is the extra statement that each pair is degenerate in modulus, which happens exactly when it is a conjugate pair. For the primes the pairing is the functional equation, and RH is again the extra degeneracy.
- Lead: separate every candidate mechanism into the part giving the pairing (cheap) and the part giving the bound (hard). This drives the later (FE)/(RH)/(Ram) split.
- Related: L12-034, L12-043, L12-048.

### L12-043 Self-adjointness is not enough: the prism counterexample
- Source: report/sections/03_what_rh_has_become.tex:113-117
- Raised by: orchestrator (Claude)
- Status at last mention: settled negative, used repeatedly
- Content: The adjacency matrix is symmetric for every graph, so eigenvalues are real and the pairing holds, but the bound can fail; C_16 x K_2 is symmetric and fails it.
- Lead: this is the standing refutation of naive Hilbert-Polya ("find a self-adjoint operator"), and the reason the book keeps asking for an extra bound.
- Related: L12-042, L12-049, L12-134.

### L12-044 The bound is geometric: no eigenvalue outside the spectrum of the universal cover
- Source: report/sections/03_what_rh_has_become.tex:116-119
- Raised by: orchestrator (Claude)
- Status at last mention: standing reading; realised in the continuum as temperedness
- Content: [-2 sqrt q, 2 sqrt q] is the spectrum of the infinite tree covering the graph, so RH says the graph has no eigenvalue outside the spectrum of its universal cover. "The word is tempered."
- Lead: the continuum analogue is proved (Ramanujan = temperedness of the tensor square, L12-079); the arithmetic Riemann analogue of a "universal cover" is never identified.
- Related: L12-079.

### L12-045 The two-shift table: the RH analogue holds for one shift and fails for another
- Source: report/sections/03_what_rh_has_become.tex:73-85
- Raised by: orchestrator (Claude), founding session
- Status at last mention: recorded example
- Content: A 4-symbol cyclic rule has small-matrix eigenvalues 2, 1+i, 1-i, 0 and satisfies the RH analogue; the golden-mean shift has phi, -1/phi and fails it. "The RH analogue is here a property some systems have and others do not."
- Lead: classify which shifts satisfy it. Not attempted, but it is the cleanest elementary testbed in the book.
- Related: L12-003.

### L12-046 The hierarchy primitivity / spectral gap / Ramanujan and its arithmetic counterparts
- Source: report/sections/03_what_rh_has_become.tex:143-166
- Raised by: orchestrator (Claude)
- Status at last mention: recorded table
- Content: A unique peripheral eigenvalue = primitivity = zeta(1+it) non-zero = PNT; all others inside a smaller circle = spectral gap = the zero-free region; all others on one circle of radius exp(-1/xi) with xi = 2/S = Ramanujan = RH.
- Lead: this dictionary makes "prove a uniform decay rate" the operational target, and it says that intermediate results (gap improvements) have arithmetic meaning too.
- Related: L12-005.

### L12-047 The minus sign forces a graded, not plainly bosonic, bond
- Source: report/sections/03_what_rh_has_become.tex:198-205
- Raised by: orchestrator (Claude), founding session
- Status at last mention: later proved as a no-go (thm:no-ungraded-trace)
- Content: In the explicit-formula trace identity the zeros enter with a minus sign relative to the leading term, "the same minus sign that marks the fermionic H^1 block in the elliptic-curve case and the absorption spectrum in Connes's language". The total measure stays positive because the von Mangoldt weights are nonnegative, but the subleading sector contributes negatively, "so whatever state this is, its bond space is graded, not plainly bosonic".
- Lead: became thm:no-ungraded-trace and cor:curve-counts-graded.
- Related: L12-113, L12-114, L12-116.

### L12-048 The explicit formula as a semigroup trace with the pole as entropy 1
- Source: report/sections/03_what_rh_has_become.tex:168-196
- Raised by: orchestrator (Claude), founding session
- Status at last mention: registered as sketched (obs:rh-flow-pairing)
- Content: Differentiating the Riemann-von Mangoldt formula in the ring length gives sum_n Lambda(n) delta(l - log n) = e^l - sum_rho e^{rho l} - (e^{-2l} + e^{-4l} + ...), which is Tr exp(l L) for a generator with eigenvalues 1 (the pole, entropy 1), every zero, and the trivial zeros. The functional equation makes the normalised rates pair as (1-sigma, sigma), "exactly as mu mu' = q paired the graph eigenvalues around sqrt q".
- Lead: the semigroup exists as a spectral datum; the programme is to realise it as an actual transfer operator of a state.
- Related: L12-017, L12-112.

### L12-049 The Hilbert-Polya operator is the "adjacency" partner of the flow generator
- Source: report/sections/03_what_rh_has_become.tex:254-267; report/sections/02b_definitions_arithmetic.tex:70-75
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (obs:hilbert-polya-hermitian)
- Content: Write the subleading generator as L = -1/2 + iH; RH says exactly that H is Hermitian. "L is to H what the Hashimoto edge operator is to the adjacency matrix of a graph." The Hermitian object carries the symmetric combination rho(1-rho), real iff Re rho = 1/2. For graphs the Hermitian object is given and reality is a theorem; for the primes it is the conjecture. The definition also records that H "is not the entanglement Hamiltonian of any state".
- Lead: find the arithmetic analogue of the compression T -> A (the Ihara-Bass step). This is exactly what prop:selberg-ladder-ihara later does on the Selberg side.
- Related: L12-088, L12-097, L12-051.

### L12-050 Being Ramanujan is never a consequence of the structure
- Source: report/sections/03_what_rh_has_become.tex:237-244
- Raised by: orchestrator (Claude)
- Status at last mention: the book's standing warning
- Content: For graphs side B exists, the trace identity holds, and the small matrix is symmetric for *every* graph, yet most graphs fail the bound. In every known case the bound comes from arithmetic input of Deligne's type. For Selberg's surfaces the same statement is open in general.
- Lead: "the Kraus structure alone will not do it, and some arithmetic rigidity has to enter, playing the role that weights play for curves."
- Related: L12-011, L12-086, L12-116.

### L12-051 Erratum: -log T is not the entanglement Hamiltonian (dead route)
- Source: report/sections/03_what_rh_has_become.tex:275-284
- Raised by: orchestrator (Claude), correcting the founding session
- Status at last mention: declared wrong; listed among the dead routes
- Content: The entanglement Hamiltonian of an MPS is -log of a reduced density matrix built from the *fixed points* of T alone, is Hermitian by construction, and does not see the subleading spectrum. The operator whose spectrum contains the zeros is the transfer generator, non-Hermitian in general, whose eigenvalue phases are the oscillation frequencies of the ring norms.
- Lead: none; the route is listed among the dead ones. The correct relation is obs:hilbert-polya-hermitian.
- Related: L12-049, L12-122.

### L12-052 The graded permutation toy: a permutation, its gas, and whether boundary conditions induce zeros
- Source: report/sections/03b_graded_permutation.tex:12-20
- Raised by: TJO (2026-09-14, night)
- Status at last mention: answered; the whole shard is the answer
- Content: TJO's question: start from pi = (12)(345); the naive MPS has bond dimension five; the gas of rings should be l^2 of the naturals and zeta the partition function of two oscillators with energies 2 and 3, so there should be an isomorphism. Then grade the second cycle odd and ask whether the right boundary conditions induce zeros; and what principle fixes the number of physical letters, since one letter and five letters both have a reason to be.
- Lead: both sub-questions were answered (L12-053, L12-058); the answers set the design rules for the Riemann cMPS.
- Related: L12-053, L12-058, L12-061.

### L12-053 Three separate knobs: the grading, the parity insertion, the holonomy
- Source: report/sections/03b_graded_permutation.tex:105-137
- Raised by: orchestrator (Claude), answering TJO
- Status at last mention: registered as sketched (thm:permutation-induced-zeros)
- Content: (ii) The grading alone does nothing: the untwisted closure gives the ungraded zeta for every grading. (i) The parity insertion produces the numerator, so odd cycles' eigenvalues become zeros. (i again) The holonomy places the zeros: h = -1 on the 3-cycle moves them from the primitive cube roots to exp(+-i pi/3), and a zero and a pole cancel exactly when an even and an odd cycle share a root. On the gas side an odd cycle is a fermionic prime contributing 1 - h_c u^{l_c}, and the graded zeta is a Witten index with fugacity, an indefinite overlap rather than a norm. "grade a sector odd is only half a specification."
- Lead: any Phantasm construction must specify all three knobs.
- Related: L12-054, L12-062.

### L12-054 The Moebius function is a fermion parity
- Source: report/sections/03b_graded_permutation.tex:139-153
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (cor:moebius-fermion-parity); *corrected* in shard 04g
- Content: Grading every cycle odd gives det(1-uP) = 1/zeta_pi. Arithmetically, grading every prime odd gives prod_p (1 - p^{-s}) = 1/zeta(s) = sum_n mu(n) n^{-s}: the squarefree gas with mu(n) = (-1)^{#primes} as its fermion parity.
- Lead: the tempting "zeros on Re s = 0" reading is false and was corrected: each finite factor vanishes there, but that says nothing about the continued product, whose poles inside the strip are exactly the zeros of zeta with their orders.
- Related: L12-152, L12-147.

### L12-055 The prime-side creation operators are the Bost-Connes isometries, not oscillator a-daggers
- Source: report/sections/03b_graded_permutation.tex:94-101
- Raised by: orchestrator (Claude)
- Status at last mention: recorded reading
- Content: The gas is the Fock space of one oscillator per cycle, but on the prime side the creation operators are the shifts |a> -> |a+1>, i.e. the BC isometries: the Hilbert space and the Hamiltonian are oscillator-like, but the algebra is Toeplitz. Also noted: in the toy the length operator is degenerate (2^3 and 3^2 have the same length) whereas log 2 and log 3 are incommensurable.
- Lead: the distinction matters for any Riemann Lindbladian with "creation" jumps; it recurs in the phase-side guess.
- Related: L12-145, L12-018.

### L12-056 Ring norms see the letters only through the transfer channel; Kraus rank is the floor
- Source: report/sections/03b_graded_permutation.tex:157-174
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (prop:letters-transfer-invariance)
- Content: For any graded lattice tensor, |Psi_B|^2 = Tr[(B tensor conj B) E^n] depends on the letters only through E; an isometry on the letter index leaves E fixed, and conversely two families with the same E are so related after padding by zero letters. The minimal number of letters is the Kraus rank of the transfer channel, and Tr[Gdb E^n] is the Ramond amplitude of the *one-letter* MPS with matrix E on the doubled bond graded by Gdb.
- Lead: the letter count is not determined by the zeta; the canonical minimal choice is the Kraus rank.
- Related: L12-058, L12-033.

### L12-057 Sector-separating letters kill the odd sector, hence the zeros
- Source: report/sections/03b_graded_permutation.tex:176-189
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (lem:sector-separating-letters)
- Content: If every letter is supported in a single parity sector, E vanishes on the Gdb-odd doubled subspace, so twisted and untwisted ring norms coincide and the ring zeta has no zeros.
- Lead: a hard design constraint: letters that record the bond parity destroy the zeros. This is the "from above" half of the physical-dimension principle.
- Related: L12-058, L12-064.

### L12-058 What fixes the physical dimension: Kraus rank from below, coarser-than-the-grading from above
- Source: report/sections/03b_graded_permutation.tex:191-216, 243-260
- Raised by: TJO's question; answered by the orchestrator
- Status at last mention: registered as sketched (obs:physical-dimension-principle)
- Content: The zeta never chooses the physical dimension. From below it is the Kraus rank. From above, once a grading is in play, the letters must be coarser than the grading. One and five letters for a permutation are *two different channels* - Ad(P) and the dephased permutation - agreeing only on the diagonal sector where the count lives; the physical dimension measures the which-path information the environment records per step (in Lindblad language, the number of jump channels). The letter ladder for (12)(345) at n=6 is 5, 13, 1. "The one letter per prime choice, natural on the gas side, is the worst one when the grading is by prime."
- Lead: choose the letters transverse to the grading. Directly constrains the Riemann cMPS ansatz, and is exactly what the phase-side guess violated.
- Related: L12-056, L12-057, L12-148.

### L12-059 Weighted letters let several letters coexist with the sign
- Source: report/sections/03b_graded_permutation.tex:213-216
- Raised by: orchestrator (Claude)
- Status at last mention: raised, used in the genus-one construction
- Content: For 0/1 letters the two parity sectors interfere only if they emit literally the same word, which forces one letter; weighted letters diag(a_s, c a_s) emit the same word with amplitudes differing by c^n, so several letters coexist with the sign. "The weights (sqrt q, phases) buy that freedom."
- Lead: weights are not decoration; they are what makes multi-letter graded tensors possible at all.
- Related: L12-032, L12-062.

### L12-060 A parity-measuring jump shifts the whole odd spectrum uniformly, and 2 gamma = 1/4
- Source: report/sections/03b_graded_permutation.tex:218-241
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (prop:parity-jump-uniform-shift)
- Content: Partial dephasing by P multiplies the odd doubled subspace by 1-2p and fixes the even one. For a graded Lindbladian, adding the jump sqrt(gamma) P adds exactly gamma(Gdb - 1): every even-odd coherence eigenvalue shifts by -2 gamma, every even one is unchanged. For a finite abelian character grading the group-average jumps add -gamma on every cross-character coherence and 0 within a sector; the full average as a single-step channel is the character measurement and annihilates those coherences. Hence a uniform-rate odd spectrum is preserved and translated, and "2 gamma = 1/4 is the e^{-t/4} of the Riemann normalisation."
- Lead: this is the letter-level carrier of the *rate* half of the Ramanujan statement; the frequencies must come from elsewhere.
- Related: L12-061, L12-067, L12-151.

### L12-061 The Riemann cMPS ansatz: prime jumps + Galois dephasing at 2 gamma = 1/4 + an even-odd Hamiltonian
- Source: report/sections/03b_graded_permutation.tex:262-289
- Raised by: TJO asked (2026-09-14) which jump operators; the ansatz is the orchestrator's answer
- Status at last mention: raised as "a reading and not a theorem", unreviewed; the named test venue is the finite covariant cones of shard 04d
- Content: (a) The ring norms see the jumps only through the Lindbladian, so the question is about Tcm, not about unravellings. (b) Galois jumps are diagonal in the character grading; their dissipator is character dephasing, setting one uniform rate on every trivial-nontrivial coherence and leaving the pole sector alone; as a full average per step it is a character measurement and removes the zeros. (c) Prime jumps act on every character sector and carry the lengths: they are the record, and the prime comb is their emission record; alone they give a Gibbs fixed point with real spectrum and no zeros. The grading must be transverse to the primes. (d) Neither family supplies the frequencies gamma_n; those need a Hamiltonian, or a non-normal even-odd coupling, on the coherences between the pole sector and the nontrivial-character sectors: "the Hilbert-Polya half remains". (e) The ansatz shape: prime jumps with weights (record, lengths, Gibbs fixed point) + Galois dephasing at 2 gamma = 1/4 (rate) + an even-odd Hamiltonian part (frequencies), with RH the statement that the dissipation on the even-odd coherences is pure dephasing, i.e. uniform.
- Lead: test (e) in the finite covariant cones of sec:bc-symmetry-generators. Partly done there and partly refuted (L12-134), and refuted on the phase side (L12-148).
- Related: L12-134, L12-148, L12-060, L12-074.

### L12-062 The critical-line separation needs weights sqrt(q) on the odd cycle
- Source: report/sections/03b_graded_permutation.tex:134-137
- Raised by: orchestrator (Claude)
- Status at last mention: raised, developed in the ring-norm shards
- Content: Every eigenvalue of a permutation has modulus one, so the pole circle and the zero circle coincide. Separating them (a critical circle of radius sqrt q strictly inside a pole circle of radius q) requires weights sqrt(q) on the odd cycle.
- Lead: the arithmetic weight is what makes the two circles different; a purely combinatorial model can never see the critical line.
- Related: L12-053, L12-059, L12-031.

### L12-063 Graded Weil-Hodge inequality: the odd trace is dominated by the even one
- Source: report/sections/03c_graded_ramanujan.tex:32-47
- Raised by: orchestrator (Claude); proved by the codex prover (D1)
- Status at last mention: registered as sketched (prop:graded-weil-hodge)
- Content: Both closures are ring norms hence nonnegative, so |Tr E_1^n| <= Tr E_0^n and spec-rad(E_1) <= spec-rad(E_0) = q. Equal radii do not force a common eigenvalue (ledger L01: the single even letter P on C^{1|1} has even spectrum {1,1}, odd {-1,-1}). A Perron eigenmatrix averages to an even one, so the radius is attained evenly, although positive operators need not be even (L02). "This is the finite shadow of the Hodge index inequality."
- Lead: positivity of both closures is a free inequality every graded transfer channel satisfies, and it is the only unconditional constraint on the odd sector.
- Related: L12-084, L12-012.

### L12-064 No zeros without a grading; zeros with a unique fixed point require *odd* letters
- Source: report/sections/03c_graded_ramanujan.tex:72-89; report/sections/03c:12-29
- Raised by: TJO's suspicion (2026-09-15) that all known quantum expanders are ungraded; confirmed and proved by the prover (D14)
- Status at last mention: registered as sketched (prop:no-ungraded-zeros)
- Content: (i) With P = 1 the two closures coincide and the ring zeta has only poles; every quantum expander in sight (Hastings, Harrow, the Weil-LPS channels, the complexes) is such. (ii) If every letter is even the bond splits and both 1_+ and 1_- are fixed: no unique fixed point. So zeros with a unique fixed point require letters that anticommute with P. (iii) No nonzero positive operator is odd; odd fixed operators exist only when the stationary state is not unique.
- Lead: TJO's suspicion is confirmed about the literature and about the book up to sec:zeta-conditions; the search must be for odd letters.
- Related: L12-040, L12-057, L12-141.

### L12-065 Graded quantum Ihara-Bass holds sector by sector
- Source: report/sections/03c_graded_ramanujan.tex:91-108
- Raised by: orchestrator (Claude); proved by the prover (D3)
- Status at last mention: registered as sketched (thm:graded-qihara-bass)
- Content: det(1 - u T_k) = (1-u^2)^{n_k(D-2)/2} det(1 - u Sigma_k + (D-1)u^2) for k = 0, 1, since Gdb tensor 1 commutes with T, with Sigma tensor 1, and with the reversal. The graded quantum Ihara zeta is then a ratio of Ihara quadratics over odd and even adjacency eigenvalues, the (1-u^2) factors cancelling exactly for a balanced grading.
- Lead: the whole graph toolkit now applies to graded channels; this is what turns a band bound into a circle statement.
- Related: L12-066, L12-039.

### L12-066 Band if and only if circle, but only for the *net* divisor, and the converse fails
- Source: report/sections/03c_graded_ramanujan.tex:110-130
- Raised by: orchestrator (Claude); corrected and proved by the prover (D4)
- Status at last mention: registered as sketched (cor:graded-band-circle)
- Content: A bound on both entire sectors implies the divisor statement; the converse is false without a no-cancellation hypothesis. The prover's counterexample: a primitive degree-14 channel with even {14, 10} and odd {10, 6} has the mode 10 outside the band, cancelled, and reduced zeta (1 - 6u + 13u^2)/((1-u)(1-13u)).
- Lead: "Ramanujan on the divisor" and "Ramanujan sector by sector" are genuinely different properties; every claim must say which.
- Related: L12-070, L12-099, L12-034.

### L12-067 There is no odd-sector Alon-Boppana bound (refuted)
- Source: report/sections/03c_graded_ramanujan.tex:132-145
- Raised by: orchestrator (Claude) as a drafted claim; refuted by the prover (D5)
- Status at last mention: pursued, negative
- Content: The drafted odd-sector analogue of Hastings' lower bound is false. The degree-four channel (1/4)(2 Ad 1 + 2 Ad P) on C^{m|m} has zero odd part for every m, and there are primitive degree-sixteen families with zero odd radius and unbounded m. Hastings' argument needs every word trace |Tr U_w|^2 >= 0; on the odd sector word traces can be negative. The even letter P is exactly the parity jump, which shifts the whole odd spectrum.
- Lead: "Ramanujan for the odd sector is an upper bound (the band), not an optimality statement." So one cannot argue by extremality on the odd side.
- Related: L12-060, L12-038.

### L12-068 Graded Harrow expanders: index-two gradings of Harrow channels are graded Ramanujan
- Source: report/sections/03c_graded_ramanujan.tex:149-179
- Raised by: orchestrator (Claude); corrected and proved by the prover (D6, ledger L06-L09, L37)
- Status at last mention: registered as sketched (thm:graded-harrow)
- Content: Gdb = Ad(P) is a G-intertwiner; the trivial representation occurs once (the fixed point) and the sign representation once (spanned by P), both even; every other constituent is bounded by the second eigenvalue of the Cayley graph. So if Cay(G,S) is Ramanujan the graded channel is a graded Ramanujan quantum expander whose odd Hashimoto sector carries zeros on |u| = q^{-1/2}. The character formulas show only words with product in G_0 contribute to either ring norm.
- Lead: the first mechanism for graded Ramanujan channels; instantiated for the Pauli group and for PGL_2(F_p) with LPS generators in the odd coset.
- Related: L12-040, L12-069, L12-070.

### L12-069 A qubit with Pauli letters counts the points of an elliptic curve over F_5
- Source: report/sections/03c_graded_ramanujan.tex:181-192, 220-249
- Raised by: orchestrator (Claude); corrected and proved by the prover (D13, ledger L25-L27)
- Status at last mention: registered as sketched (prop:qubit-graded-zeta)
- Content: V = C^{1|1}, P = Z, letters X, X, Y, Y, Z, Z (each twice so the reversal is fixed-point-free), D = 6, q = 5. The graded quantum Ihara zeta is (1 + 2u + 5u^2)/((1-u)(1-5u)), the zeta of the elliptic curves y^2 = x^3 + 4x + b over F_5 (8 points, a_5 = -2): the periodic non-backtracking ring norms of a qubit with Pauli letters count the points of an elliptic curve. Caveat: the direct, non-lifted transfer has its zero at -2, off the circle - "the curve appears only after the non-backtracking lift". Counts 8, 32, 104, 640, 3208, 15392.
- Lead: the numerator is in general not integral (a Ramanujan example with N_P(1) = 16/3), need not be a Weil polynomial, and an integral Weil numerator need not be a curve numerator ((1-3u)^4 over F_9 would give -2 points). So "which graded channels give curves" is open.
- Related: L12-037, L12-030, L12-072.

### L12-070 Graded Weil-LPS: Hecke-eigenvalue zeros, and the extremal eigenvalue is in the odd sector
- Source: report/sections/03c_graded_ramanujan.tex:196-217
- Raised by: orchestrator (Claude); audited and corrected by the prover (finite/harrow_audit.py)
- Status at last mention: numerical (num:graded-ramanujan(c))
- Content: G = PGL_2(F_p), pi the principal series with chi of order 4, S the q+1 LPS quaternions with (q/p) = -1, all in the odd coset; (p; q) = (5; 13) and (13; 5). Both sectors lie in the band. The sectors *share* eigenvalues and only the net divisor survives: for (5; 13) there are 16 cancelled pairs and the reduced zeta has numerator degree 4 with no nontrivial poles; for (13; 5) both degrees are 144 with 140 nontrivial pole factors on the circle. "In the (13;5) case the extremal Hecke eigenvalue 4.2497 lives in the odd sector."
- Lead: the orchestrator's first printout claimed numerator degrees 36 and 196; the prover's audit corrected it. That the extremal Hecke eigenvalue sits on the odd (zero) side is a small, unexploited observation.
- Related: L12-066, L12-068, L12-009.

### L12-071 The Artin factorisation of a graded expander into L-functions of constituents
- Source: report/sections/03c_graded_ramanujan.tex:164-169
- Raised by: orchestrator (Claude); proved by the prover as part of D6
- Status at last mention: registered inside thm:graded-harrow(v)
- Content: With a_{k,sigma} the multiplicity of constituent sigma in sector k, the graded quantum Ihara zeta factors as prod_sigma det(1 - u T_sigma)^{a_{1,sigma} - a_{0,sigma}}, where T_sigma is built from the *individual* letters sigma(s) and the reversal, not from the averaged matrix sigma(W_S). "The L-functions of the graded expander are the sigma-factors, with net sign by sector."
- Lead: this is the structural reason different representations give different zeros; it is the finite analogue of the character-sector grading.
- Related: L12-024, L12-126, L12-006.

### L12-072 Two mechanisms for graded Ramanujan: band type and circle type
- Source: report/sections/03c_graded_ramanujan.tex:193-195; report/sections/03d_graded_ramanujan_continuum.tex:182-201
- Raised by: orchestrator (Claude)
- Status at last mention: one mechanism understood, the other declared not understood
- Content: Mechanism one (band): a Hermitian graded channel whose sector adjacency eigenvalues lie in the band, lifted onto the circle by the non-backtracking construction. Mechanism two (circle): the odd block is directly sqrt(q) times a unitary, as for the 06h elliptic tensor (E_1^dagger E_1 = 5) and for Artin-Schreier by Parseval, with the P-mode as H^0 by parity-twisted unitality. Also listed as not understood: a Kraus (doubled-bond) realisation of the Artin-Schreier, Riemann and Selberg graded spectral transfers.
- Lead: "Not understood: a graded channel of circle type with a group-theoretic mechanism." The Riemann case is said to need the second mechanism in the continuum, on regular data.
- Related: L12-020, L12-041, L12-082, L12-097.

### L12-073 Exactness of the divisor definition under the continuum limit, with an aliasing caveat
- Source: report/sections/03d_graded_ramanujan_continuum.tex:19-37
- Raised by: orchestrator (Claude); corrected and proved by the prover (D7, ledger L10)
- Status at last mention: registered as sketched-conditional (prop:graded-continuum-exact)
- Content: The lattice divisor is the push-forward of the generator divisor under exp(eps lambda); a line statement is eps-independent, and (RH), (FE), (Ram) are eps-independent for eps small enough that no two divisor points alias and none aliases a trivial mode. At eps = 1 a CP example whose rates all alias to e has a lattice divisor that cancels completely while the continuum supertrace does not vanish between samples.
- Lead: always check aliasing before reading a lattice divisor as a continuum one.
- Related: L12-088.

### L12-074 Graded Chernoff: the grading lives in the jumps; there is no Hamiltonian odd letter
- Source: report/sections/03d_graded_ramanujan_continuum.tex:39-62
- Raised by: orchestrator (Claude); corrected and proved by the prover (D8, ledger L11-L12, L38)
- Status at last mention: registered as sketched (prop:graded-chernoff)
- Content: Parity-covariant CPTP maps close to the identity converge to a GKSL generator with [H, P] = 0 and homogeneous jumps; the no-event part Q is even. Odd letters satisfy sum over odd a of |K_a|_HS^2 = O(eps), so they are collectively of order sqrt(eps) and can never be a drift letter close to the identity (PAP = -A with A = 1+B forces |B| >= 1). "In the continuum, parity-changing dynamics is dissipative and there is no Hamiltonian odd letter."
- Lead: "This is why obs:jump-operator-guidance needed an even-odd Hamiltonian on the *doubled* bond rather than an odd letter." A hard structural constraint on any continuum Phantasm.
- Related: L12-061, L12-075, L12-092.

### L12-075 Individual odd-letter limits need a choice of Kraus gauge
- Source: report/sections/03d_graded_ramanujan_continuum.tex:50-52 (ledger L12), 46-48 (L38)
- Raised by: the codex prover
- Status at last mention: recorded caveat
- Content: The collective sqrt(eps) estimate is gauge-free, but individual limits K_a/sqrt(eps) -> R_a require a choice of Kraus gauge; and the canonical homogeneous presentation is reached "by a canonical change of noise basis, not necessarily by an even unitary remix alone".
- Lead: a small but real obstruction to identifying "the" odd jump operators of a continuum limit.
- Related: L12-074, L12-056.

### L12-076 Jump Lindbladians: the Ramanujan band is affine in the rates
- Source: report/sections/03d_graded_ramanujan_continuum.tex:64-76
- Raised by: orchestrator (Claude); proved by the prover (D9)
- Status at last mention: registered as sketched (prop:jump-lindbladian-band)
- Content: For Tcm = sum_s g_s (Ad U_s - 1) with homogeneous unitaries closed under adjoint, exp(t Tcm) = exp(-gamma t) exp(gamma t Phi), so spec Tcm = gamma(spec Phi - 1) sector by sector, and the graded Ramanujan band for equal rates is [-gamma(1+lambda_H), -gamma(1-lambda_H)] on both sectors; the non-backtracking lift exists because the words are discrete.
- Lead: gives an explicit continuum family of graded Ramanujan generators; none of them has an infinite critical-line divisor, which is why L12-083 is asked.
- Related: L12-083.

### L12-077 The relative resonance divisor: what "divisor" means when there is no trace
- Source: report/sections/03d_graded_ramanujan_continuum.tex:78-98
- Raised by: orchestrator (Claude); made precise by the prover (D10, ledger L13-L14)
- Status at last mention: registered as sketched-conditional (obs:divisor-regular-data)
- Content: Given specified regular spaces, a meromorphic continuation of the resolvent between them beyond Re z = omega/2, and finite-rank Riesz projections at its poles, the divisor is the signed count of algebraic multiplicities of those projections, sector by sector. The order of a scalar correlation pole does not measure multiplicity, and a general non-normal generator has no scalar spectral measure, so with continuous spectrum one retains vector-dependent spectral measures or supplies a spectral theorem with weights.
- Lead: this is the definition under which any infinite-dimensional Phantasm statement must be made.
- Related: L12-078, L12-089, L12-144.

### L12-078 The norm of Z(t) is 1 for all t, so no L^2 statement on K_S sees the rate 1/4
- Source: report/sections/03d_graded_ramanujan_continuum.tex:89-97
- Raised by: two readers, 2026-09-14, unreviewed
- Status at last mention: recorded as a decisive obstruction
- Content: For the compressed Riemann semigroup |Z(t)| = 1 for all t, so the divisor is deliberately *not* the L^2 spectrum of Tcm; (HP) must be stated on a weighted or anisotropic space with domain and norm-equivalence qualifications, as resonances are for Anosov flows. For the Riemann graded generator the reference rates are 0 and -1/2, the archimedean ladder must be designated trivial, and the regular nontrivial modes have centre -1/4 iff RH. The realisation of that generator as a doubled-bond cMPS is not supplied.
- Lead: build the weighted/anisotropic space on the Riemann side. Not done; the analytic counterpart of the modular-surface obstacle.
- Related: L12-093, L12-036, L12-077.

### L12-079 Continuous Harrow: "Ramanujan" is temperedness of the tensor square
- Source: report/sections/03d_graded_ramanujan_continuum.tex:102-126
- Raised by: orchestrator (Claude); proved by the prover (D11)
- Status at last mention: registered as sketched (obs:continuous-harrow-tempered)
- Content: Letters exp(+- sqrt(eps) X_j) give the representation Lindbladian; with Tcm_* = (1/2)(B_H^2 + B_E^2) = 2 Cas + (1/2) B_W^2, the equally averaged two-generator walk has threshold 1/4 and Tcm_* itself threshold 1/2 (ledger L15). For an irreducible tempered pi of SL_2(R), pi tensor conj pi is tempered (Fell absorption) and on the K-invariant sector spec(-Tcm_*) lies in [1/2, infinity), with exact rate 2s(1-s) + m^2/2; the bound is sharp for every discrete series, there is no HS fixed vector, and for PSL_2(R) the type-zero bound is *equivalent* to temperedness. "This is the precise diffusion meaning of continuous Ramanujan."
- Lead: it is *not* a flow-divisor line theorem - principal constituents have exponents -1/2 +- ir while discrete series are tempered with faster exponents -n/2, and the two coexist (ledger L16-L18). The discrete zeros appear only on a lattice quotient.
- Related: L12-044, L12-080, L12-081.

### L12-080 The complementary-series tensor square and Selberg's 3/16 (unverified, from memory)
- Source: report/sections/03d_graded_ramanujan_continuum.tex:121-125
- Raised by: the codex prover's report, citing H-repka from memory
- Status at last mention: raised, explicitly "not to be cited until byte-checked"
- Content: The tensor square of a complementary series pi_s is reported to contain a complementary series iff s > 3/4. If so, the Lindbladian of pi_s would be Ramanujan for 1/2 < s <= 3/4 although pi_s is not tempered, the threshold being Selberg's 3/16 = (3/4)(1/4).
- Lead: byte-check Repka's decomposition. If true, "Ramanujan for the Lindbladian" is strictly weaker than temperedness and coincides exactly with the Selberg constant - a striking and unexploited coincidence.
- Related: L12-079, L12-086.

### L12-081 Graded continuous Harrow: the PGL_2(R) reflection grading puts the ladder odd and the geodesics even
- Source: report/sections/03d_graded_ramanujan_continuum.tex:128-154
- Raised by: orchestrator (Claude); decomposed exactly by the prover (D12, ledger L19-L24)
- Status at last mention: registered as sketched (obs:graded-continuous-harrow); the assignment is the *opposite* of the Riemann one
- Content: For PGL_2(R) over PSL_2(R) the index-two graded genuine irreducibles are the discrete series pairs with k >= 2 *even* (odd k needs a covering group or a projective bond, L19), swapped by the reflection diag(-1,1); the odd letter is the reflection, a jump at rate gamma. The even sector is purely principal series; the odd sector is purely discrete with leading exponents -n/2 - "an arithmetic ladder at and beyond the functional-equation partner, positionally the Gamma-factor ladder, carrying no critical-line modes". P is a bounded eigenoperator but not Hilbert-Schmidt, so supplies no HS divisor point (L21); the regular even and odd hyperbolic contributions cancel in the supertrace because the two discrete-series characters agree there (L22-L23). For k=1 (projective) the exponents match the Gamma_C and Gamma_R pole lists positionally.
- Lead: a clean negative for the reflection grading as the Selberg/Riemann grading; but the positional match of the odd ladder with the Gamma-factor pole list is an unexploited coincidence.
- Related: L12-084, L12-017, L12-040.

### L12-082 A doubled bond has more even than odd dimensions; a cohomological grading may not
- Source: report/sections/03d_graded_ramanujan_continuum.tex:190-192
- Raised by: orchestrator (Claude)
- Status at last mention: recorded as an obstruction to Kraus realisation
- Content: A doubled bond has n_0 - n_1 = (D_+ - D_-)^2 >= 0, so the even sector is always at least as big as the odd one; a cohomological grading, where the interesting block is the odd one, may have the opposite inequality.
- Lead: a dimension-counting obstruction to realising the Artin-Schreier, Riemann or Selberg graded spectral transfers as doubled-bond CP transfers. Stated in one line and never pushed to a theorem.
- Related: L12-041, L12-089.

### L12-083 Wanted: a continuum example with an infinite discrete critical-line divisor, other than Riemann and Selberg
- Source: report/sections/03d_graded_ramanujan_continuum.tex:192-193
- Raised by: orchestrator (Claude)
- Status at last mention: listed as not understood
- Content: Every continuum example the book has is either finite-divisor (jump Lindbladians, graded Harrow) or one of the two arithmetic objects. No third example with an infinite discrete divisor on a critical line is known here.
- Lead: find one. It would separate "graded Ramanujan in the continuum" from "arithmetic accident".
- Related: L12-076, L12-072.

### L12-084 The Selberg zeta is the ring zeta of the *stable* two-term transverse complex
- Source: report/sections/03e_selberg_letters.tex:102-142; report/sections/02h_definitions_graded_ramanujan.tex:142-156
- Raised by: TJO's question (2026-09-16: "exhibit an infinite-object zeta as a graded transfer whose odd-block unitarity is derived from the letters rather than read off the zeros"); drafted by the orchestrator, corrected and proved by the codex prover (D2, ledger L02-L09), reviewed by an Opus refuter
- Status at last mention: registered as proved-conditional (thm:selberg-two-term-ring-zeta)
- Content: With even generator -X and odd generator -X+1, connected by f -> (U_+ f) eta_+, the flat supertrace is (1 - e^t)F and the ring zeta is exactly Z_Selberg = D_tower(s-1)/D_tower(s). The retained divisor is entirely odd; both constant roots are zeros, not a Perron pole and partner; reference pair (1, 0), critical line Re s = 1/2. Closed geodesics are fermionic because dim E_s = 1: det(1 - P_gamma) = -|det(1 - P_gamma)|. The table also gives the function flow (even and all-odd) and the full transverse forms.
- Lead: the choice of *which* complex is decisive; only the stable one has the right divisor.
- Related: L12-085, L12-022, L12-031, L12-100.

### L12-085 (FE) and (Ram) fail for the Ruelle zeta even under coercivity
- Source: report/sections/03e_selberg_letters.tex:126-129
- Raised by: the codex prover, correcting the draft
- Status at last mention: pursued, negative
- Content: For the Ruelle zeta the retained divisor is -S + S(.+1) - the even band is the odd band shifted by -1 - so (FE) and (Ram) fail even under Selberg's 1/4; the all-odd tower likewise fails unless restricted to its first band.
- Lead: dead for the Ruelle zeta as a graded Ramanujan object, and a warning that "an alternating product of determinants" is not automatically a good graded transfer.
- Related: L12-084.

### L12-086 Selberg's 1/4 is the one extra bound, and it is not derived from the letters
- Source: report/sections/03e_selberg_letters.tex:67-73, 152-157; report/sections/03f_selberg_letters_finite.tex:112-126
- Raised by: orchestrator / codex prover
- Status at last mention: registered as assumed (asm:selberg-coercivity)
- Content: The coercivity |H f|^2 + |E f|^2 >= |f|^2 on right-K-invariant f orthogonal to 1 is equivalent to Laplacian >= 1/4 on 1-perp. "A surface-dependent property, not derived from the letters; it is the Selberg-side analogue of the Ramanujan bound." The labelled-input theorem makes [BOUND] exactly equivalent to (RH) and (Ram), with (FE) holding without it.
- Lead: the separation "letters give reality + FE + a positive form; one coercivity bound gives RH" is the template the Riemann side is supposed to imitate.
- Related: L12-050, L12-098, L12-093.

### L12-087 The threshold is a Jordan obstruction: exact 1/4 admits no positive unitarising form
- Source: report/sections/03e_selberg_letters.tex:173-178; report/sections/03f_selberg_letters_finite.tex:76-80, 160-164
- Raised by: the codex prover (D3, ledger L10-L16)
- Status at last mention: proved-conditional
- Content: At lambda = -1/2 the eigenstate space has dimension d_{1/4} while the algebraic multiplicity is 2 d_{1/4}; a positive G with A^{*G} + A = -1 forces semisimplicity, so the full algebraic block at Laplace eigenvalue exactly 1/4 admits no positive unitarising form. Divisor (RH)/(FE)/(Ram) are unaffected; operator (HP) needs in addition that 1/4 is not in the spectrum. The finite mirror: at a = +- 2 sqrt q the companion matrix has a size-two Jordan block.
- Lead: the manifest Hilbert-Polya form is strictly stronger than RH, failing precisely at the extremal point. Any Hilbert-Polya programme must decide what to do at the threshold.
- Related: L12-097, L12-099.

### L12-088 Operator-level continuous Ihara-Bass: a *quadratic* intertwining plus a horocyclic ladder
- Source: report/sections/03e_selberg_letters.tex:187-205
- Raised by: orchestrator (Claude); proved by the prover (D4, ledger L18-L19)
- Status at last mention: registered as proved-conditional (prop:selberg-ladder-ihara)
- Content: On ker U_-, pi_*(A^2 + A) = -Lap pi_* with A = -X: one Laplace eigenvalue has two flow roots, exactly as one adjacency eigenvalue has two edge eigenvalues. The ladder coefficient U_- U_+^m v = m(2z - m + 1) U_+^{m-1} v gives the decomposition off an exceptional set. Sampling at time t_s turns the two roots into mu_+ mu_- = e^{-t_s} and mu_+ + mu_- = 2 e^{-t_s/2} cos(t_s sqrt(lambda - 1/4)), "a cosine functional calculus of Lap, not -2 Lap, with aliasing".
- Lead: "a literal compression of the whole tower to one Laplacian determinant is still not supplied" (ledger L19). That is the remaining piece of the continuous Ihara-Bass.
- Related: L12-049, L12-073, L12-097.

### L12-089 No doubled-bond CP realisation of the Selberg flow: the flat supertraces are negative
- Source: report/sections/03e_selberg_letters.tex:207-228
- Raised by: the codex prover (D5, ledger L20-L25)
- Status at last mention: registered as sketched-conditional (prop:selberg-no-cp-realisation)
- Content: The stable complex and the full transverse generator are single-copy graded *spectral* transfers. They are not doubled transfers: the CP conjugation lives on a larger space with generator T tensor 1 + 1 tensor conj T, product grading and squared coefficient growth; multiplication operators are not Hilbert-Schmidt; and both flat supertraces -C and -C/(1 - e^{-t}) are *negative* distributions, hence cannot be cMPS ring norms, which are nonnegative.
- Lead: a hard no-go for realising Selberg as a cMPS. Since the sign is the whole obstruction, a different closure or a sign convention with its own meaning is the obvious next thing to try; nobody tries it here.
- Related: L12-041, L12-082, L12-143.

### L12-090 Adding diffusion to the Selberg drift destroys the first band; its fate is unknown
- Source: report/sections/03e_selberg_letters.tex:218-224 (ledger L25)
- Raised by: the codex prover
- Status at last mention: raised, not pursued
- Content: Adding the two dissipative jumps sqrt(kappa)H, sqrt(kappa)E to the drift gives L_kappa = -X + 2 kappa Cas + (kappa/2) W^2 on multiplication observables; it preserves neither the K-sector nor the first band, since the commutator of U_- with the two-jump generator is (2 lambda - 1) U_+ on first-band states. "So the Selberg divisor is a drift phenomenon and its fate under diffusion needs new analysis."
- Lead: work out what happens to the divisor at small kappa. This is the one place where the Selberg object and the Lindbladian (Phantasm) picture could be joined, and it is completely open.
- Related: L12-074, L12-076.

### L12-091 The Laplacian is a sum of squares of the letters ("reality from Haar")
- Source: report/sections/03e_selberg_letters.tex:87-100, 152-157
- Raised by: orchestrator (Claude); proved by the prover (D1, correcting the draft's direction, ledger L01)
- Status at last mention: proved-conditional (prop:selberg-letters-laplacian)
- Content: The left-invariant fields are skew-symmetric with respect to Haar measure (the group is unimodular by the brackets), so on right-K-invariant f, <f, Lap f> = (1/4)(|H f|^2 + |E f|^2). Hence the spectrum is nonnegative and every s with s(1-s) in the spectrum lies in the critical line union [0,1]. Applied to first-band states, this gives the reality of the retained odd divisor for free.
- Lead: the letters supply reality and the strip; only the 1/4 gap is extra. This is the template result of the whole lane.
- Related: L12-086, L12-098, L12-093.

### L12-092 The parity of the Selberg complex is a coefficient grading, not a physical parity-changing jump
- Source: report/sections/03e_selberg_letters.tex:222-224 (ledger L24)
- Raised by: the codex prover
- Status at last mention: recorded consistency note
- Content: prop:graded-chernoff (no Hamiltonian odd letter) is consistent with the Selberg complex because the parity there is a coefficient grading of the transverse factor, not a physical parity-changing jump.
- Lead: there are at least two kinds of grading in the book - physical bond parity and cohomological/coefficient parity - and results about one do not transfer to the other. Never systematised.
- Related: L12-074, L12-022.

### L12-093 The modular surface obstacle: Riemann zeros are Selberg zeros outside L^2 (H-CUSP-BRIDGE)
- Source: report/sections/03f_selberg_letters_finite.tex:26-50
- Raised by: orchestrator (Claude), corrected by the prover (ledger L28, L30, L31) and reviewed
- Status at last mention: "this item is exploratory and OPEN"
- Content: For PSL_2(Z) and a nontrivial zero rho of order m, the scattering determinant has a pole of order m at s_0 = rho/2 and the Selberg zeta a zero there, with no collision with the discrete spectrum. RH is the statement that *these* zeros lie on Re s = 1/4, not a 1/4 line for the whole divisor. The mechanism stops exactly here: a first-band state at lambda = s_0 - 1 would push forward to the leading Laurent coefficient of the Eisenstein series, whose constant term is not in L^2, so the Haar-transported form is unavailable and symmetry of the Laplacian says nothing about rho.
- Lead: "What is missing is a non-compact flow realisation with finite-rank resonant data at s_0 - 1 and a positive modal pairing at the correct centre" (the prover's H-CUSP-BRIDGE). This is the sharpest open problem in my files.
- Related: L12-094, L12-078, L12-086.

### L12-094 The centre mismatch: -3/4 (scattering sector) versus -1/4 (Riemann model)
- Source: report/sections/03f_selberg_letters_finite.tex:38-43 (ledger L30)
- Raised by: the codex prover, correcting the draft
- Status at last mention: recorded as an unresolved identification
- Content: The draft's e^{t/2} rescaling can never unitarise the scattering sector under *any* positive norm, since Re(lambda + 1/2) = Re s_0 - 1/2 < 0: the scattering subset has flow centre -3/4 under RH, while the Riemann model has centre -1/4 and belongs to -conj(rho)/2. "The two are related by affine substitutions and have not been identified."
- Lead: identify them, or explain why they cannot be. A concrete, small, decidable question.
- Related: L12-093, L12-017, L12-036.

### L12-095 Truncated Maass-Selberg positivity is not an RH criterion
- Source: report/sections/03f_selberg_letters_finite.tex:43-45 (ledger L31)
- Raised by: the codex prover
- Status at last mention: pursued, negative
- Content: The Maass-Selberg relation for the truncated Eisenstein series gives a strictly positive truncated norm throughout 0 < Re s_0 < 1/2, so truncated positivity holds whether or not RH does.
- Lead: dead; rules out one obvious positivity route on the modular surface.
- Related: L12-093, L12-008.

### L12-096 Selberg's 1/4 for the full modular group is a theorem, not open (correction)
- Source: report/sections/03f_selberg_letters_finite.tex:17-24, 45-46 (ledger L28)
- Raised by: the Opus refuter / prover, citing Booker-Lee-Strombergsson
- Status at last mention: corrected
- Content: The draft called Selberg's eigenvalue conjecture open for the full modular group; it is known (Theorem 1.1: true for Gamma_1(N) for N <= 880 and Gamma(N) for N <= 226).
- Lead: so the obstruction on the modular surface is *not* the eigenvalue bound; it is entirely the non-L^2 scattering sector.
- Related: L12-093.

### L12-097 The letter-derived metric G_C, positive exactly on the strict Ramanujan band
- Source: report/sections/03f_selberg_letters_finite.tex:54-90
- Raised by: orchestrator (Claude); proved by the prover (D7, nine steps, ledger L32, L35, L36)
- Status at last mention: registered as proved (thm:hashimoto-lift-metric)
- Content: With T = SR - J_0 and the companion model C = [[Sigma, q], [-1, 0]], the metric G_C = [[1, Sigma/2], [Sigma/2, q]] satisfies C^dagger G_C C = q G_C; it is positive definite iff the *strict* band |a| < 2 sqrt q holds for every retained eigenvalue, and then T/sqrt q is G_C-unitary on the whole algebraic band, with an explicit operator functional equation F_C, F_C^2 = 1, F_C C F_C = q C^{-1}. Reality of Sigma comes from the letters; the band bound is extra; "the reduced divisor sees only m_0(a) - m_1(a) and cannot certify sector positivity". The value +- sqrt q is *not* an exception (L32).
- Lead: this settles the "Hermitian channel plus lift" item of obs:graded-ramanujan-status in the inverse-paired setting; extending it to adjoint-paired non-invertible letters is open.
- Related: L12-012, L12-014, L12-087, L12-099.

### L12-098 Labelled inputs: exactly what the letters supply, and what is extra
- Source: report/sections/03f_selberg_letters_finite.tex:112-145
- Raised by: orchestrator / prover
- Status at last mention: registered as proved / proved-conditional (thm:letters-derived-selberg, thm:letters-derived-finite)
- Content: [HAAR]+[SL2] give Lap >= 0 as a sum of letter squares; adding [ANALYSIS] gives the first-band quadratic, reality, the branchwise form and the paired operator FE off the threshold; adding [TRACE] identifies the ring zeta with Z_Selberg and fixes the trivial multiplicities; [BOUND] is equivalent to (RH) and (Ram); with [ENDPOINT] it gives the positive manifest form. The finite counterpart needs no resonance or Poisson theorem.
- Lead: "A tensor-network Kraus realisation and norm equivalence with the anisotropic space are separate, unproved." That is the standing to-do.
- Related: L12-086, L12-089, L12-041.

### L12-099 Exact endpoint counterexamples with Jordan blocks
- Source: report/sections/03f_selberg_letters_finite.tex:160-164
- Raised by: the prover's numerics
- Status at last mention: numerical (num:selberg-letters)
- Content: K_3 box Q_3 is 5-regular and Ramanujan with eigenvalue -4 of multiplicity two, and its Hashimoto matrix has dim ker(T+2) = 2 but dim ker(T+2)^2 = 4. The ten-letter Pauli channel (I x4, X x4, Z x2, P = Z, D = 10, q = 9, even adjacency {10, 2}, odd {6, -2}) is sector-Ramanujan with an odd Hashimoto eigenvalue 3 of nullities 1, 2.
- Lead: explicit small objects where the manifest form fails while the divisor statement holds; a permanent test suite for any positivity claim.
- Related: L12-087, L12-097.

### L12-100 The K-type grading is *not* a flow grading (correction of an earlier proposal)
- Source: report/sections/03f_selberg_letters_finite.tex:92-108; report/sections/03d_graded_ramanujan_continuum.tex:168-174
- Raised by: the orchestrator originally proposed the K-type grading; refuted by the prover (D8, ledger L37-L40)
- Status at last mention: pursued, negative
- Content: With P_K = (-1)^{m/2} on K-type m: P_K H P_K = -H, P_K E P_K = -E, P_K W P_K = W, so the two-jump diffusion is even but the geodesic generator X = H/2 is *odd*; P_K does not commute with the flow. It is not the Hodge grading either. On a spherical principal-series constituent the graded heat trace is a positive theta sum (0.7300003... at t = 1 by Poisson summation), so nothing cancels.
- Lead: "The K-type parity survives only as a grading of the diffusion letters." Dead as a flow grading; the grading that yields Z_Selberg is the stable transverse complex.
- Related: L12-084, L12-081.

### L12-101 The innerness of the scattering symbol is not written out
- Source: report/sections/04_riemann_channel.tex:52-58, 297-305
- Raised by: orchestrator (Claude), founding session
- Status at last mention: registered as sketched (prop:scattering-inner), gap acknowledged
- Content: Unimodularity on the real line and analyticity in the lower half plane are argued; contractivity in the interior is the Phragmen-Lindelof step, "which the note does not write out (step 3 of HANDOFF.md)". The innerness numbers are a check at four points, not a proof.
- Lead: write out the Phragmen-Lindelof step, or cite Lax-Phillips with a local source.
- Related: L12-102.

### L12-102 The Adamyan-Arov identification is quoted without a local source
- Source: report/sections/04_riemann_channel.tex:60-66, 297-305
- Raised by: orchestrator (Claude)
- Status at last mention: acknowledged gap
- Content: The compressed semigroup on K_S is said to be unitarily equivalent to the Lax-Phillips semigroup of the modular surface with the cusp forms removed, by Adamyan-Arov; "the note states this without a written argument, and no local source exists for it here."
- Lead: obtain the source and byte-check it. Without it the entire Riemann-channel identification rests on an unverified claim. It is also listed under "Not established: the analytic realisation of the Lax-Phillips input".
- Related: L12-101, L12-117.

### L12-103 The two placements of the primes are different objects
- Source: report/sections/04_riemann_channel.tex:90-107
- Raised by: orchestrator (Claude)
- Status at last mention: recorded distinction
- Content: Placement one is a dilation-covariant Markov semigroup on L^2(R_+^x) in Holevo form with the von Mangoldt jump measure and symbol (zeta(sigma - i tau)/zeta(sigma))^t, a genuine Markov semigroup for sigma > 1 by Khinchin's compound-Poisson theorem; it has no zeros for sigma > 1 and at sigma = 1/2 is not a semigroup at all, the symbol being unbounded. Placement two is Z_t on K_S: the zeros as resonances, no jump structure, the primes entering only through the symbol. "The bridge between the two is the boundary phase."
- Lead: the jump structure and the zeros live at different values of sigma; the BC phase transition beta = 1 is exactly the finite- versus infinite-activity threshold of the jump measure.
- Related: L12-104, L12-105.

### L12-104 The bridge: Lax-Phillips = (Bost-Connes at beta = 1) + (Sz.-Nagy-Foias), at the level of boundary phases
- Source: report/sections/04_riemann_channel.tex:109-129, 297-305
- Raised by: orchestrator (Claude), founding session; called "the note's proposal"
- Status at last mention: registered as sketched (prop:phase-identity); explicitly "a statement about boundary phases, not about the operators"
- Content: For real tau, S(tau) = exp(-2i arg xi(1 + 2i tau)), and -arg zeta(1 + 2i tau) is exactly the imaginary part of the BC Levy exponent at the critical temperature. The real part of the critical Levy exponent diverges (sum 1/p is infinite) and "that divergence *is* the Bost-Connes phase transition"; the imaginary part converges conditionally at PNT strength. The proposal: take the BC process at beta = 1, discard the divergent real part, keep the phase, and use that unimodular function as the characteristic function of a contraction semigroup.
- Lead: upgrade the boundary-phase identity to an operator identity. Never done; the central unbuilt bridge of the founding session.
- Related: L12-103, L12-107, L12-153.

### L12-105 Conjecture: a Stinespring form of Z_t whose Kraus operators are the prime dilations
- Source: report/sections/04_riemann_channel.tex:307-319 (conj:stinespring-jump-form, status open)
- Raised by: orchestrator (Claude), founding session
- Status at last mention: registered as open
- Content: The single-Kraus lift exists trivially and says nothing; the Holevo-form covariant Lindbladian with the von Mangoldt jump measure lives on the full regular representation and is not the compressed object. Whether a jump-type generator on K_S reproduces Z_t is the open question the note isolates, and its physical index would be the Stinespring environment.
- Lead: "A negative answer with a reason is a result"; the route is listed among the dead ones in the open-problems shard.
- Related: L12-007, L12-008, L12-118.

### L12-106 The Bost-Connes phase operator is a matrix product operator over the prime chain
- Source: report/sections/04_riemann_channel.tex:245-265
- Raised by: orchestrator (Claude), from HANDOFF item 2
- Status at last mention: registered as sketched (prop:bc-mpo), numerically checked against Hurwitz zeta and Dirichlet L-values
- Content: e(a/b) is an MPO over the prime chain with bond space Z/b, the local transfer map being r -> p^k r, i.e. Shor's map at the site p. In the Dirichlet character basis the transfer eigenvalues are L(beta, conj chi)/zeta(beta). Extremal KMS states differ only by the boundary residue of the chain, and beta -> 1^+ kills every nontrivial character sector: "the symmetry breaking read as a boundary effect."
- Lead: "Shor's unitary is the level-N Galois symmetry of the system and a snapshot of the dilation flow" - a one-line remark never developed.
- Related: L12-126, L12-127, L12-107.

### L12-107 The bond-space mismatch: Z/b for the phase operators versus K_S for the semigroup
- Source: report/sections/04_riemann_channel.tex:292-295
- Raised by: orchestrator (Claude)
- Status at last mention: raised, no map offered
- Content: "The bond space of the phase operators is Z/b, finite and abelian, whereas that of the compressed semigroup is K_S, and the note offers no map between them."
- Lead: this is HANDOFF open item 0b' ("identify K_S with a Bost-Connes bond"), reported still unchanged after the phase-side campaign.
- Related: L12-104, L12-153, L12-127.

### L12-108 No identification with the parent repository's beta > 1 constructions is claimed
- Source: report/sections/04_riemann_channel.tex:302-305
- Raised by: orchestrator (Claude)
- Status at last mention: scope disclaimer
- Content: The parent repo's constructions sit above the phase transition; the object here is the beta = 1 phase compressed to a co-invariant subspace.
- Lead: none stated; it leaves open whether the two can be related by a limit, which is also where the normality obstruction (L12-120) bites.
- Related: L12-120.

### L12-109 The Phantasm specification: a cMPS in dilation time whose bond carries a Riemann Lindbladian
- Source: report/sections/04b_phantasm_forced.tex:13-27
- Raised by: TJO (HANDOFF.md, central priority of 2026-09-12)
- Status at last mention: the organising target; two complementary halves built, neither complete
- Content: The Phantasm is a continuous matrix product state whose one-dimensional space is dilation time, whose bond carries a Lindbladian with the pole of zeta at s = 1 as fixed point and the zeros as relaxation modes, and whose ring norm is the prime measure. Because cMPS ring norms are sums of squares while the zeros enter with a minus sign, the bond was expected to be Z_2-graded, the zeros odd, the pole even, and the ring norm a supertrace.
- Lead: shards 04b-04g are the attempt; conj:phantasm-both-halves is the residue.
- Related: L12-047, L12-125, L12-143.

### L12-110 The forced net spectrum, and the parity-flip analysis
- Source: report/sections/04b_phantasm_forced.tex:104-180
- Raised by: orchestrator / codex prover; part (i) strengthened by the Opus reviewer
- Status at last mention: finite flips proved-conditional; the unrestricted infinite case is open (obs:parity-infinite-open)
- Content: A graded datum with supertrace the prime comb has net multiplicity 1 at the pole, -m_rho at each zero, -1 at each trivial zero, 0 elsewhere. If the flipped zero set is finite, positivity forces the pole even and no zero flipped, while the trivial-zero parities may be anything, even infinitely many. With infinitely many flips: positivity alone still forces the pole even (monotone convergence of the cutoff pairings, no domination premise, no Landau input); the zeros need a domination premise. The draft's "a cosine is negative somewhere" was replaced by an argument on the whole leading-frequency sum.
- Lead: "whether positivity alone forces every parity is open here." The obstruction is that for infinite flipped sets the difference is only a distribution and can carry negative mass at the prime-power atoms.
- Related: L12-015, L12-111.

### L12-111 The ladder parity is free; all-even is impossible
- Source: report/sections/04b_phantasm_forced.tex:272-279
- Raised by: orchestrator / prover
- Status at last mention: proved-conditional (prop:ladder-parity-free)
- Content: With the ladder odd the supertrace is 2 P_prime + e^{-t/2}/(e^t - 1); with the ladder even it is 2 P_prime + twice that; both are positive, so positivity does not fix the ladder parity. Exact equality to 2 P_prime does force the net spectrum, and no all-even graded datum has the right supertrace.
- Lead: the archimedean place's parity is genuinely undetermined by the data at hand - a small gap any geometric realisation would settle.
- Related: L12-017, L12-081.

### L12-112 The even line as the pole = the residue of the Eisenstein series at s = 1, not constructed
- Source: report/sections/04b_phantasm_forced.tex:281-289
- Raised by: orchestrator (Claude)
- Status at last mention: raised, "an identification not constructed here"
- Content: RH is the statement that every odd K_S mode has real part -1/4; the even line represents the pole of zeta - the constant function on the modular surface, the residue of the Eisenstein series at s = 1. Also: Z_t is not trace class for t > 0, and the identity is a spectral identity, not a cMPS tensor whose Hilbert norm is the prime measure.
- Lead: construct the identification of the even line with the residual/constant mode of the modular surface. Small, concrete, never done.
- Related: L12-093, L12-016, L12-017.

### L12-113 The no-go: no ungraded trace-class realisation of a numerator
- Source: report/sections/04b_phantasm_forced.tex:192-214
- Raised by: orchestrator / prover
- Status at last mention: proved (thm:no-ungraded-trace)
- Content: If N_n = sum b_i^n - sum alpha_j^n with at least one alpha, no finite matrix and no trace-class operator has Tr E^n = N_n for all n: at u = 1/alpha_j the generating function has residue +m_j/alpha_j whereas an ordinary trace has residue -m_E/alpha_j with m_E >= 0, so "a numerator root needs a negative multiplicity". The companion criterion: a sequence is the supertrace sequence of a finite graded matrix iff the germ is a rational function with value 1 at 0.
- Lead: the grading is forced, not chosen.
- Related: L12-047, L12-114, L12-015.

### L12-114 Curves need the grading; graphs do not
- Source: report/sections/04b_phantasm_forced.tex:224-242
- Raised by: orchestrator / prover
- Status at last mention: proved-conditional (cor:curve-counts-graded)
- Content: For a curve of genus >= 1 the counts are not the trace sequence of any finite matrix or trace-class operator, hence not the ring norms of any translation-invariant bosonic MPS with a fixed local tensor. They *are* the supertrace sequence of diag(q, 1) even plus (Frobenius on H^1) odd, and the odd net spectrum is forced to be the Frobenius eigenvalues. Non-backtracking graph counts are ordinary trace sequences and the Ihara zeta has no finite zeros.
- Lead: this is the precise content of "the sign"; it forces every curve-type example to be graded.
- Related: L12-113, L12-031, L12-030.

### L12-115 The Artin-Schreier transfer matrix is a complex partition-function transfer, not a norm transfer
- Source: report/sections/04b_phantasm_forced.tex:236-242
- Raised by: the codex prover ("a point the prover insisted on")
- Status at last mention: recorded correction
- Content: The quadratic Artin-Schreier transfer matrix whose trace is an exponential sum is a complex partition-function transfer, not the norm transfer of a state: "the honest state, the uniform superposition over the points of the curve, has no fixed-tensor MPS with those norms."
- Lead: distinguish partition-function transfers from norm transfers everywhere; the ring-norm-tensor campaign (shards 06c-06f) is the attempt to build genuine norm transfers for curves.
- Related: L12-020, L12-032, L12-019.

### L12-116 Prior art: the grading is Deninger's, the sign is Connes's
- Source: report/sections/04b_phantasm_forced.tex:28-57
- Raised by: orchestrator (Claude), byte-cited
- Status at last mention: cited facts (cit:deninger-graded-lefschetz, cit:connes-absorption)
- Content: Deninger's conjectural picture already has H^0 = R with Theta = 0, H^1 infinite dimensional with spectrum the nontrivial zeros, H^2 = R with Theta = id, and the Lefschetz formula 1 - sum e^{t rho} + e^t. Connes: "the spectral interpretation of the zeros ... should be as an absorption spectrum rather than as an emission spectrum". "So the forced part of the Phantasm ... is Deninger's programme, and the sign is Connes's. What this book adds is the reading through ring norms and transfer operators."
- Lead: the novelty claim is deliberately narrow - the tensor-network reading, and the rigidity, no-go and realisation statements.
- Related: L12-047, L12-113.

### L12-117 What is and is not established for the Phantasm
- Source: report/sections/04c_phantasm_channels.tex:255-265
- Raised by: orchestrator (Claude)
- Status at last mention: status summary (obs:phantasm-established-scope)
- Content: Established: the forced graded net spectrum and its realisation by a graded contraction semigroup with one even fixed line; the no-go for ungraded trace-class realisations; a genuine absorbing-vacuum channel with the Riemann channel as its odd coherences; the normal-Gibbs classification and the prime-chain spectra. Not established: unrestricted infinite parity rigidity, the analytic realisation of the Lax-Phillips input, a cMPS whose Hilbert norm is the prime measure, and a stationary entangled bond with the critical arithmetic state.
- Lead: four named gaps, each a concrete target.
- Related: L12-110, L12-102, L12-125.

### L12-118 The vacuum-decay channel: the zeros as odd coherences
- Source: report/sections/04c_phantasm_channels.tex:52-95
- Raised by: orchestrator / prover
- Status at last mention: proved (thm:vacuum-decay-finite); the infinite version proved-conditional
- Content: For a contraction semigroup tending strongly to zero, the absorbing-vacuum channel on C plus H is CPTP with unique stationary density the pure vacuum, and its coherence blocks evolve exactly by Z_t. Spectrum = {0} plus spec(B) plus its conjugate plus all pair sums; coherences odd, populations even. For H = K_S each zero appears once as an odd coherence mode and once as its conjugate.
- Lead: "their formal trace |Tr_d Z_t|^2 is not a defined product of distributions; no pair-correlation statement follows." So the tempting "pair correlation of zeros from the population sector" does not work as stated.
- Related: L12-119, L12-142.

### L12-119 The vacuum is absorbing, so the SHW rebound picture fails inside K_S
- Source: report/sections/04c_phantasm_channels.tex:97-109
- Raised by: orchestrator / prover
- Status at last mention: proved, negative
- Content: The jump reinserts into the vacuum, but the renewal integral diverges linearly: the vacuum is absorbing, not a rebound state of finite holding time, so this model does not solve the renewal equation of the SHW picture with a rebound inside K_S. The canonical cMPS selected by the stationary bond density has a single nonzero Schmidt weight: its half-line entanglement is trivial. "This is the first half: side B without side A."
- Lead: conj:phantasm-both-halves explicitly says the rebound-state equation with a *mixed* rebound state is the finite-dimensional shadow - i.e. try a mixed rebound state.
- Related: L12-125, L12-118.

### L12-120 Normal KMS states exist only above the transition
- Source: report/sections/04c_phantasm_channels.tex:113-132
- Raised by: orchestrator / prover, on top of the cited BC KMS classification
- Status at last mention: proved (prop:normal-kms-gibbs)
- Content: For the dynamics Ad(N^{it}) on B(l^2(N)) a normal KMS_beta state exists iff beta > 1, and then it is the Gibbs density with entanglement spectrum beta log n + log zeta(beta); the thermofield double factorises over the prime sites with bond dimension one along the chain. "The unique critical KMS state of the Bost-Connes algebra is not a normal density in this representation."
- Lead: any critical (beta = 1) Phantasm must be non-normal, i.e. a type III object - exactly the hedge in conj:phantasm-both-halves.
- Related: L12-125, L12-121, L12-108.

### L12-121 Delocalisation at the transition
- Source: report/sections/04c_phantasm_channels.tex:162-174
- Raised by: orchestrator / prover
- Status at last mention: proved (cor:gibbs-delocalisation)
- Content: As beta decreases to 1 the Gibbs density has no trace-norm limit and its mass on every finite-rank projection tends to zero; for beta <= 1 the prime occupation process has no stationary probability on finite-support configurations. "This is the precise content available for the Bost-Connes transition; it is not a proof of ergodicity breaking of a Riemann Lindbladian."
- Lead: the honest statement of what the transition gives; the tempting "ergodicity breaking" reading is explicitly disclaimed.
- Related: L12-120, L12-018.

### L12-122 The entanglement Hamiltonian would be free and Hagedorn, not Cardy
- Source: report/sections/04c_phantasm_channels.tex:176-205
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (obs:gibbs-entanglement-hagedorn)
- Content: If the Phantasm's bond fixed point is the BC Gibbs density, its entanglement Hamiltonian is beta log N, free over the primes with single-particle levels log p; the entropy is finite above the transition, grows like log P (prime cutoff) or (1/2) log N (bond cutoff) at criticality, and like a power for beta < 1. The level density e^E is Hagedorn growth with beta_H = 1 (Julia's reading), not Cardy growth, "so the finite-entanglement scaling law of critical CFTs does not apply to this state". Constants fixed by the review: the prime-cutoff constant is exactly 0 (the two Mertens constants cancelling) and the bond-cutoff constant is -gamma_E/2.
- Lead: whatever the Phantasm is, it is not a critical CFT ground state; MPS/cMPS finite-entanglement scaling intuitions are inapplicable. "Gapped, critical, and not a cMPS at all."
- Related: L12-120, L12-121, L12-051.

### L12-123 Every prime-by-prime construction is blind to the zeros
- Source: report/sections/04c_phantasm_channels.tex:172-174
- Raised by: orchestrator (Claude), referring to obs:prime-by-prime-blind (registered outside this lane)
- Status at last mention: recorded principle
- Content: The prime-chain construction's spectrum is blind to the zeros "as every prime-by-prime construction is". "This is the second half: side A without side B."
- Lead: the zeros require something that couples the primes - which is what the character-sector grading and the even-odd Hamiltonian are meant to supply.
- Related: L12-018, L12-061, L12-126, L12-135.

### L12-124 The two halves are complementary
- Source: report/sections/04c_phantasm_channels.tex:209-221
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched (obs:complementary-halves)
- Content: The vacuum-decay channel has the zeros as odd relaxation modes (each zero twice, plus an even pair-sum sector) but a pure stationary state and trivial entanglement. The prime-chain Gibbs Lindbladian has the right stationary state, with entanglement spectrum proportional to the ring lengths 2 log n, but a real spectrum with no zeros. "No construction in this book has both, and the Phantasm would need both."
- Lead: build one with both.
- Related: L12-125, L12-118, L12-018.

### L12-125 Conjecture: a graded Lindbladian with the BC KMS state stationary and the zeros as odd relaxation modes
- Source: report/sections/04c_phantasm_channels.tex:220 (reference to conj:phantasm-both-halves; full statement read from db/claims.tsv)
- Raised by: orchestrator (Claude), replacing HANDOFF item 0b
- Status at last mention: registered as open (row in shard 10)
- Content: There is a Z_2-graded Lindbladian (or a type III generalisation at beta = 1) whose stationary state is the Bost-Connes KMS state, with entanglement Hamiltonian log N, and whose odd relaxation modes are the nontrivial zeros: the object having both halves. The rebound-state equation of the SHW renewal picture with a *mixed* rebound state is its finite-dimensional shadow; the vacuum rebound state is excluded.
- Lead: solve the finite-dimensional shadow first (mixed rebound state).
- Related: L12-119, L12-124, L12-109, L12-120.

### L12-126 The grading as trivial versus nontrivial Dirichlet characters
- Source: report/sections/04c_phantasm_channels.tex:223-240
- Raised by: orchestrator (Claude), by analogy with the Artin-Schreier super-transfer
- Status at last mention: registered as sketched-conditional (obs:character-sector-grading); "It is an analogy, not a theorem"
- Content: In the Artin-Schreier super-transfer the even block is the trivial additive-character sector (the de Bruijn count, the pole at u = 1/q) together with the point at infinity (the pole at u = 1, not a character sector), and the odd block is the sum over nontrivial characters carrying the zeros. By analogy a Galois-symmetric Riemann bond decomposed under Zhat^x would have the pole in the even sector (the trivial Dirichlet character being the only one with a pole) and the zeros of every L(s, chi) in the odd one. "The graded object would compute the zeta of the cover, the Dedekind zeta of the cyclotomic field at level N, not zeta alone." This is where Connes's trace formula lands (all L-functions with Grossencharakter).
- Lead: the finite-level test is conj:galois-graded-bond. Note the tension: it is consistent with the character-basis transfer eigenvalues of the BC MPO, which is nevertheless not that object.
- Related: L12-020, L12-127, L12-071, L12-106.

### L12-127 Conjecture: the Gamma_0(N) model space carries the L(s, chi) zeros organised by characters
- Source: report/sections/04c_phantasm_channels.tex:239 and report/sections/04d_bc_symmetry_generators.tex:229-230 (conj:galois-graded-bond; full statement read from db/claims.tsv)
- Raised by: orchestrator (Claude)
- Status at last mention: registered as open; "a computation, not yet done"
- Content: The model space of a congruence subgroup Gamma_0(N), whose scattering determinant involves the Dirichlet L-functions mod N, carries the zeros of L(s, chi) organised by the characters of (Z/N)^x, with the Shor map as the level-N Galois symmetry acting on the bond; the graded bond of the character-sector observation is realised at finite level.
- Lead: do the computation. It is explicitly a computation, not a theory problem, and it is the finite-level test of the character-sector grading. Still listed as open in the "what is still missing" paragraph of 04d.
- Related: L12-126, L12-106, L12-136.

### L12-128 Finite representations of the full BC algebra collapse all phases (but compressions are not excluded)
- Source: report/sections/04d_bc_symmetry_generators.tex:45-58
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (prop:bc-no-finite-phase-representation)
- Content: mu_n^* mu_n = I makes mu_n unitary in finite dimension, and the BC relation then forces e(1/n) = I for every n. "This excludes an exact finite representation; it does not exclude restrictions, CP compressions, or asymptotic models."
- Lead: look for CP compressions or asymptotic (large-N) models rather than exact finite representations. Stated in one sentence and not pursued.
- Related: L12-026, L12-136.

### L12-129 The unique Weil-invariant matrix extension, and Weil invariance of the diagonal exactly at beta = 1
- Source: report/sections/04d_bc_symmetry_generators.tex:25-43, 60-82
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (prop:bc-residue-state, prop:bc-symmetry-state-extension)
- Content: The residue probabilities are p^{-beta} at zero and (1 - p^{-beta})/(p-1) elsewhere, so at criticality the phase marginal is uniform at every level and the diagonal extension is I/p. The Weil-invariant operator space is span{I, Par} (the symplectic group is transitive on nonzero Weyl labels and the sum of the Weyl operators is p times parity), so the diagonal fixes the two coefficients; positivity holds iff r <= 2/(p+1). The diagonal extension is Galois invariant, and Weil invariant *iff* beta = 1.
- Lead: the critical temperature is singled out by a finite symplectic symmetry requirement - an unexploited coincidence.
- Related: L12-026, L12-133.

### L12-130 Above the transition, covariance can act on a family of extremal states instead of fixing one
- Source: report/sections/04d_bc_symmetry_generators.tex:79-82
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: The claim "a unique stationary density of a covariant semigroup is invariant under its symmetry group" has uniqueness as a premise; above the transition covariance can instead act on a family of stationary extremal states. "A single extremal state is generally not invariant."
- Lead: a covariant Lindbladian with a *family* of stationary states permuted by Galois is a different and unexplored ansatz - and it is exactly the shape of BC symmetry breaking.
- Related: L12-120, L12-106.

### L12-131 Every invariant faithful state admits an interior feasible generator
- Source: report/sections/04d_bc_symmetry_generators.tex:105-115
- Raised by: orchestrator / codex prover
- Status at last mention: part of thm:bc-covariant-gks-cone (sketched)
- Content: X -> sigma Tr X - X (the reset generator) is always feasible, with conditional Choi matrix Q(I tensor sigma)Q, strictly positive on the range of Q. So the cone is never empty and has nonempty interior.
- Lead: feasibility is free; only the *spectral* requirements bite. This is why the cone dimensions are the informative object.
- Related: L12-132, L12-137.

### L12-132 The four cone dimensions
- Source: report/sections/04d_bc_symmetry_generators.tex:117-141, 207-218
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (thm:bc-critical-cone-dimensions), 427 numerical checks
- Content: At the tracial state I/p the real span dimensions are (p-1)(p+1)^2 for the Galois torus, 2p-2 for the full linear Weil action, p+1 for Weyl translations plus Galois torus, and 1 for Weyl translations plus full Weil action; checked at p = 3, 5, 7 as (32,4,4,1), (144,8,6,1), (384,12,8,1). "The depolarizing generator is an interior point of the conditional Choi cone, so positivity does not reduce these dimensions." Also noted: orbit coefficients are not independent nonnegative rates in the first two rows.
- Lead: these numbers say precisely how much freedom the symmetry requirements leave.
- Related: L12-027, L12-133.

### L12-133 Extra Weyl covariance collapses the cone to the depolarizer and removes the zero-like modes
- Source: report/sections/04d_bc_symmetry_generators.tex:143-157
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (prop:bc-weyl-covariance-collapse)
- Content: All Weyl-covariant generators are sums over nonzero v of c_v (W_v X W_v^* - X) with c_v >= 0; Galois covariance makes the rates constant on the two punctured axes and the p-1 hyperbolae xy = b; in particular c_v = c_{-v}, so every Weyl eigenvalue is real and nonpositive. Full symplectic covariance makes all rates equal and gives exactly gamma(Dep - id). "This extra commuting symmetry removes the oscillatory zero-like modes in this model. It is not a consequence of merely requiring a symplectic representation or an adelic structure."
- Lead: do *not* impose Weyl-translation covariance on the Phantasm. A clear design ruling.
- Related: L12-027, L12-134.

### L12-134 A symplectic odd-sector counterexample: covariance permits unequal odd decay rates
- Source: report/sections/04d_bc_symmetry_generators.tex:161-182
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (prop:bc-symplectic-odd-counterexample)
- Content: With a a primitive root mod p and R_a(I) = 0, R_a(W_v) = W_{av}, the generator Dep - id + eps R_a with eps = 1/(4p^2) is CPTP with unique stationary state I/p and full Weil, Galois and parity covariance. At p = 7 its odd eigenvalues are -1 - eps and -1 + eps/2 +- i sqrt3 eps/2, each of multiplicity 8: the odd decay rates are *unequal*. "Thus the counterexample does not fit any input zero positions."
- Lead: full arithmetic covariance does not by itself force a uniform odd rate, so the Ramanujan property cannot be a consequence of symmetry alone in this finite model. Directly limits the ansatz of L12-061(e); the finite analogue of "self-adjointness is not enough".
- Related: L12-061, L12-133, L12-043.

### L12-135 Two-prime couplings invisible to the one-prime restrictions
- Source: report/sections/04d_bc_symmetry_generators.tex:184-205
- Raised by: orchestrator / codex prover
- Status at last mention: registered as sketched (prop:bc-compatible-prime-coupling)
- Content: For distinct p, q and 0 <= c <= min(a,b), a family L_c of CPTP generators has stationary state I/(pq), full local Weyl/Weil covariance, and one-prime restrictions independent of c with rates a and b, while the joint traceless rate is a + b - c. "This supplies compatible two-prime residue dynamics under CRT with a variable coupling; it is not an infinite adelic construction."
- Lead: a genuine hidden coupling parameter invisible to local data - the natural place for a global (adelic) constraint to enter. Never pushed past two primes.
- Related: L12-123, L12-136.

### L12-136 What is missing on the BC side: a representation or CP comparison map to the scattering bond
- Source: report/sections/04d_bc_symmetry_generators.tex:220-236
- Raised by: orchestrator (Claude)
- Status at last mention: listed as missing
- Content: "The missing input is a representation or CP comparison map connecting the full BC algebra, including its prime isometries, to the scattering bond, with compatible local Weil data. It must select the permitted commuting symmetries and constrain the generator blocks and the inter-prime couplings." Also unconstructed: prime-power levels, the real place, metaplectic compatibility, and the critical operator-algebra limit. "A chosen graded transfer spectrum alone does not identify a physical cMPS norm."
- Lead: five separately named construction tasks, none begun.
- Related: L12-107, L12-127, L12-128.

### L12-137 The reset test is not a no-go criterion for the full cone
- Source: report/sections/04d_bc_symmetry_generators.tex:233-236
- Raised by: orchestrator (Claude), correcting an earlier reading
- Status at last mention: correction recorded
- Content: The earlier reset test -(B sigma + sigma B^*) >= 0 is a criterion for a *fixed* finite no-event generator B and scalar reset, when its exit flux is positive. It is not a no-go criterion for the full cone, where B and all jumps may vary.
- Lead: an earlier apparent obstruction was overclaimed; the cone is genuinely larger than that test suggested.
- Related: L12-131, L12-132.

### L12-138 The cMPS overlap and fermion parity theorem, proved from the graded relations alone
- Source: report/sections/04e_cmps_parity_overlap.tex:12-34, 66-69, 193-246
- Raised by: TJO (2026-09-13) asked whether the supertrace reading had been proved and for a direct calculation of the expectation of (-1)^F
- Status at last mention: registered as sketched-conditional (thm:cmps-overlap-parity); no independent review
- Content: It had not been proved; the book contained only the graded contraction of lattice fermionic MPS and the graded cMPS matrix structure as citations. The theorem: for arbitrary data, the overlap with a parity insertion is Tr[(B tensor conj B') exp(L Tcm_eta)], a signed sum of squares, with no bond grading, regularity or normalisation assumed. The key checked step is that ordered creation vectors contract with *no* statistics sign, because the statistics factors ride only on terms that vanish. "What this section adds is a proof from (F1)-(F5) in which the absence of a statistics sign in the norm is a checked step, not a convention."
- Lead: the sign in the Phantasm cannot come from physical statistics.
- Related: L12-139, L12-140, L12-143.

### L12-139 Tcm_eta is in general not the generator of a positive semigroup
- Source: report/sections/04e_cmps_parity_overlap.tex:242-246
- Raised by: orchestrator (Claude, opus-5)
- Status at last mention: recorded caveat
- Content: The parity expectation is a ratio of two traces; the sign sits in the generator, every n-particle term is weighted by eta_a, and Tcm_eta is in general not the generator of a positive semigroup. "It is a trace, not a supertrace."
- Lead: this distinguishes the two candidate mechanisms for a minus sign - eta in the generator versus Gdb in the closure - and only the second is positivity-safe.
- Related: L12-140, L12-029.

### L12-140 The twisted ring norm is a supertrace, and the odd sector is an interference term
- Source: report/sections/04f_cmps_twisted_supertrace.tex:50-92
- Raised by: orchestrator (Claude, opus-5)
- Status at last mention: registered as sketched-conditional (thm:cmps-twisted-supertrace)
- Content: The untwisted norm is Tr exp(L Tcm) and the twisted one is str exp(L Tcm), the latter a manifestly nonnegative sum of squares of P-inserted amplitudes. The even trace is the sum of the two sector-closure norms and the odd trace is twice the real part of their overlap: "the minus sign of the supertrace is the minus sign in Psi_P = Psi_+ - Psi_-", i.e. the odd sector is the *interference* between the two parity-sector closures.
- Lead: positivity is automatic; the zeros are interference, not negative probability.
- Related: L12-030, L12-141, L12-142.

### L12-141 Physical fermions are not needed to have an odd sector
- Source: report/sections/04f_cmps_twisted_supertrace.tex:88-92
- Raised by: orchestrator (Claude)
- Status at last mention: recorded reading
- Content: If every species is bosonic and P commutes with Q and all R_a, the bond splits into two decoupled cMPS and str exp(L Tcm) = |Psi_+ - Psi_-|^2, the odd sector being their cross-transfer. "Fermionic R_a are what couple the two blocks."
- Lead: one could look for the Phantasm's grading among purely bosonic models with a split bond - though then the fixed point is not unique (prop:no-ungraded-zeros(ii)).
- Related: L12-064, L12-140.

### L12-142 The zeros would be relaxation rates on coherences between the two parity blocks
- Source: report/sections/04f_cmps_twisted_supertrace.tex:205-221
- Raised by: orchestrator (Claude)
- Status at last mention: registered as sketched-conditional (obs:cmps-supertrace-reading)
- Content: The grading is Gdb = P tensor conj P on the doubled bond, whose odd sector is the block-off-diagonal operators: "if zeros are to appear as the odd part of such a ring zeta, they are relaxation rates of Tcm on coherences between the two parity blocks, which agrees with the vacuum-decay picture".
- Lead: says exactly where in a Lindbladian the zeros must live; consistent with the vacuum-decay model.
- Related: L12-118, L12-061.

### L12-143 The HANDOFF sentence corrected: the sign is the bond parity of the closure, not the expectation of (-1)^F
- Source: report/sections/04e_cmps_parity_overlap.tex:21-29; report/sections/04f_cmps_twisted_supertrace.tex:16-48, 94-136, 205-221
- Raised by: orchestrator (Claude, opus-5), answering TJO
- Status at last mention: correction applied
- Content: With a bond grading the physical parity only conjugates the boundary matrix, so the expectation of (-1)^F is +-1 for a parity-homogeneous boundary and "carries no spectral information". The supertrace appears instead as the norm of the ring closed with the *bond* parity. The twisted ring is the periodic (Ramond) fermion ring and the untwisted one the antiperiodic (Neveu-Schwarz) ring - "the familiar exchange of a parity insertion in one direction with a boundary condition in the other".
- Lead: also flagged: "the supertrace over the bond itself in the graded realisation of sec:phantasm-forced is a different operator and its relation to a Tcm is not established". That is the remaining gap between the Riemann graded generator and any cMPS.
- Related: L12-017, L12-041, L12-140.

### L12-144 Nothing is established for an infinite-dimensional bond
- Source: report/sections/04f_cmps_twisted_supertrace.tex:219-221
- Raised by: orchestrator (Claude)
- Status at last mention: scope limitation
- Content: "Not established: anything for an infinite-dimensional bond (trace class, regularisation of the Laplace transforms), and any identification of Tcm with a Riemann Lindbladian."
- Lead: extend the supertrace/superdeterminant machinery to infinite bonds, presumably via the relative resonance divisor.
- Related: L12-077, L12-016, L12-030.

### L12-145 The phase-side Lindbladian guess (the "yolo" ansatz)
- Source: report/sections/04g_phase_side_lindbladian.tex:12-36
- Raised by: TJO (2026-09-14, night: "Can we yolo guess the right Lindblad given the circumstantial info we have found in this project so far?" and "dispatch two super smart codex astra xhighs"), guessed by the orchestrator, audited by two codex gpt-6-astra lanes
- Status at last mention: pursued, negative overall
- Content: Bond L^2(Zhat) tensor L^2(R_+^x); grading +1 on the vacuum Fourier mode and -1 on its complement; one prime jump V_p per prime at rate 1/p, tensored with the length shift T_{log p}; a Gamma-factor ladder and a dilation Hamiltonian on the archimedean line; Galois dephasing at rate 1/4 on vacuum-odd coherences; the physical cMPS along the archimedean coordinate with the primes as letters. Finite model: Ramanujan-sum shells and a prime cutoff.
- Lead: three structural premises all fail (L12-148, L12-149, L12-150); what survives is L12-146, L12-147, L12-151.
- Related: L12-061, L12-152.

### L12-146 What survives: exact prime-jump kinematics and the Ramanujan-shell formulas
- Source: report/sections/04g_phase_side_lindbladian.tex:40-60
- Raised by: the two codex lanes
- Status at last mention: registered as sketched (prop:phase-jumps-shells)
- Content: V_p is an isometry commuting with the other V_q and with the Galois unitaries; the Ramanujan-sum shells span the Galois-trivial sector and reduce every V_p and V_p^*; explicit shell matrix elements are given; the vacuum is *not* invariant. On a level coprime to p, sqrt(p) V_p^* restricted to that level is the Shor permutation r -> pr, while V_p itself leaves the level. For a Gauss vector and p not dividing b, V_p^* g_chi = p^{-1/2} conj chi(p) g_chi. The shell expectation tends to 0 as beta -> 1^+ for every b > 1.
- Lead: the Gauss-vector eigenrelation is a clean place where Dirichlet characters appear as jump eigenvectors - noted and not exploited.
- Related: L12-106, L12-126.

### L12-147 An exact reciprocal-zeta matrix element
- Source: report/sections/04g_phase_side_lindbladian.tex:62-84, 164-171
- Raised by: the codex lanes / orchestrator
- Status at last mention: registered as sketched (prop:phase-vacuum-generating-functions)
- Content: A(w) = sum n^{-w} V_n = prod_p (1 - p^{-w} V_p)^{-1} converges in operator norm for Re w > 1, its inverse is sum mu(n) n^{-w} V_n, and the vacuum matrix element of the inverse is exactly 1/zeta(w + 1/2). "An exact operator statement derived from the jumps, with zeta in the *denominator*, but of a specified sum over one copy of each integer, not a resolvent of the generator." The actual finite-cutoff generating functions are shifted partial zeta functions with zeta in the numerator, no pole in the strip at any cutoff uniformly in P, and no tested shell overlap has a zero there; word sums retain multinomial multiplicities despite commutation.
- Lead: this is the only place in my files where 1/zeta appears as an honest operator matrix element. The verdict calls it "an arithmetic evaluation, not a dynamical overlap"; whether it can be made dynamical is unexplored.
- Related: L12-054, L12-152.

### L12-148 The grading is not preserved: the vacuum leaks into shell p
- Source: report/sections/04g_phase_side_lindbladian.tex:104-119
- Raised by: the codex lanes
- Status at last mention: pursued, negative (prop:phase-grading-not-invariant)
- Content: The single-prime dissipator applied to the vacuum projector produces odd terms, so the Lindbladian does not commute with Gdb for any nonempty positive-rate prime set, and "no restriction to the even-odd coherences is defined". The vacuum-character coherence is not an eigenoperator (explicit mod-3, prime-2 counterexample; HS residual 0.61 at P = 47), and its self-projection coefficient has an extra 1/p against the drafted value. Vacuum coherences leak out of the odd block and retain a conserved lower bound sqrt(phi(b)/b) in trace norm.
- Lead: a grading by "vacuum versus its complement" is incompatible with prime jumps; the grading must be transverse to the primes, as L12-058 already warned.
- Related: L12-058, L12-061, L12-145.

### L12-149 No Gibbs fixed point, no normal semigroup at rates 1/p, no ring trace
- Source: report/sections/04g_phase_side_lindbladian.tex:121-141
- Raised by: the codex lanes
- Status at last mention: pursued, negative (prop:phase-no-gibbs-no-trace)
- Content: (i) Shell weights b^{-beta} are not stationary (exact 2x2 rational counterexample); population balance needs the down/up ratio p^beta, and even then the vacuum stay term creates coherences. "Resolving each edge into its own jump |pb><b| restores a Gibbs fixed point but changes the model." (ii) At rate 1/p the no-jump quadratic form is infinite and the finite-prime semigroups have no trace-norm limit at any positive time. (iii) "a prime cutoff is not a bond cutoff": even at finite prime cutoff the doubled-bond exponential is invertible, hence not compact, so the parity-inserted trace is not an ordinary trace. (iv) A single forward prime has Hilbert-Schmidt spectrum the full disc, not isolated real modes.
- Lead: the edge-resolved jump model (one jump per edge) is a named but unexplored alternative that *does* have a Gibbs fixed point.
- Related: L12-018, L12-145, L12-016.

### L12-150 A parity closure is not a quotient by Q^x
- Source: report/sections/04g_phase_side_lindbladian.tex:143-159
- Raised by: the codex lanes
- Status at last mention: pursued, negative (prop:parity-closure-not-quotient)
- Content: Multiplication by a rational is unitary on L^2(adeles) by the product formula and acts as the identity on functions of classes in the quotient; the periods log p come from the stabiliser and the norm-kernel quotient R_+/p^Z. Closing a ring with the parity only changes the boundary functional and imposes none of this (explicit 2x2 counterexample). "The identification of the guess's ring norm with an adelic periodic-orbit trace needs a quotient, an intertwiner and a regularised trace, none of which the guess supplies; Connes' 1999 paper proves local and finite-place cutoff trace formulas and does not supply them either."
- Lead: three named missing objects for any adelic reading of a ring norm.
- Related: L12-136, L12-126.

### L12-151 Galois dephasing produces a frequency only for inversion-asymmetric rates
- Source: report/sections/04g_phase_side_lindbladian.tex:86-100, 169-172
- Raised by: the codex lanes, correcting the orchestrator's earlier claim in shard 03b
- Status at last mention: registered as sketched (prop:galois-dephasing-rates); correction applied
- Content: For a finite abelian group of character-diagonal unitaries with rates lambda_a, the dissipator acts on a cross-character coherence as a scalar: zero within a sector; for uniform rates it is -gamma and real; for rates symmetric under inversion it is real; for asymmetric rates it acquires an imaginary part, i.e. a frequency.
- Lead: asymmetric Galois rates are a *source of frequencies* from a purely dissipative term - the only mechanism in my files that gets a frequency without a Hamiltonian. Not pursued.
- Related: L12-060, L12-061.

### L12-152 Verdict on the guess, and the two corrections it forces
- Source: report/sections/04g_phase_side_lindbladian.tex:161-177
- Raised by: orchestrator (Claude), after the two lanes
- Status at last mention: registered as sketched (obs:phase-side-verdict)
- Content: "The phase-side prime jumps reproduce side A: their vacuum generating functions are the Euler product, shifted, and nothing else." The guess supplies neither the pole at 1 nor the critical-line modes, and its three structural premises fail. Two earlier claims of the graded-permutation shard are corrected: Galois-diagonal jumps produce no frequency only for inversion-symmetric rates; and "fermionic primes give zeros on Re s = 0" is a statement about each finite factor, not about the continued product.
- Lead: "the negative rules out the Ramanujan-sum sector with prime jumps alone as that identification."
- Related: L12-054, L12-151, L12-153.

### L12-153 Open item 0b' (identify K_S with a Bost-Connes bond) is unchanged
- Source: report/sections/04g_phase_side_lindbladian.tex:174-177
- Raised by: orchestrator (Claude)
- Status at last mention: still open
- Content: After the whole phase-side campaign the HANDOFF open item "identify K_S with a Bost-Connes bond" is unchanged; only one candidate identification (the Ramanujan-sum sector with prime jumps) has been ruled out.
- Lead: the item remains the central unsolved identification of the Bost-Connes reframe.
- Related: L12-107, L12-104, L12-125.

## Small but possibly consequential

1. **L12-151** (asymmetric Galois dephasing rates give a frequency) - the only mechanism anywhere in these shards that produces an oscillation frequency from a purely dissipative term, mentioned once and never used, although the book repeatedly says "neither family supplies the frequencies gamma_n".
2. **L12-080** (complementary-series tensor square threshold s > 3/4 giving exactly Selberg's 3/16) - if byte-checked, "Ramanujan for the Lindbladian" would be strictly weaker than temperedness and would land exactly on the Selberg constant; currently tagged "not to be cited".
3. **L12-070** (the extremal Hecke eigenvalue 4.2497 in the (13;5) case lives in the *odd* sector) - one sentence of numerics suggesting the hardest eigenvalue is systematically on the zero side; no follow-up.
4. **L12-082** (a doubled bond forces n_0 - n_1 = (D_+ - D_-)^2 >= 0) - a one-line dimension count that may be a genuine obstruction theorem against ever realising a cohomological grading as a doubled-bond CP transfer.
5. **L12-149(i)** (resolving each edge into its own jump restores a Gibbs fixed point but changes the model) - a named alternative model with the right fixed point, dismissed in half a sentence.
6. **L12-129** (the diagonal BC residue extension is Weil invariant *iff* beta = 1) - the critical temperature is singled out by a finite symplectic symmetry requirement; an unexploited coincidence.
7. **L12-135** (two-prime couplings invisible to one-prime restrictions) - a hidden global parameter that local arithmetic data cannot see; the natural slot for an adelic constraint, never pushed past two primes.
8. **L12-106 / L12-130** (Shor's unitary as "the level-N Galois symmetry and a snapshot of the dilation flow", and covariance acting on a *family* of extremal states) - two one-line remarks that between them describe an unexplored ansatz in which Galois permutes stationary states rather than fixing one.

## Dead routes recorded

- **-log T as the entanglement Hamiltonian.** Wrong: the entanglement Hamiltonian is built from the fixed points alone, is Hermitian by construction, and does not see the subleading spectrum. report/sections/03_what_rh_has_become.tex:275-284.
- **Self-adjointness as a route to the bound.** The adjacency matrix is symmetric for every graph and most graphs fail the Ramanujan bound; the prism C_16 x K_2 is the explicit counterexample. report/sections/03_what_rh_has_become.tex:113-117.
- **The odd-sector Alon-Boppana bound.** Refuted by the prover (D5): degree-four and degree-sixteen families with zero odd spectral radius and unbounded bond dimension. report/sections/03c_graded_ramanujan.tex:132-145.
- **"Band bound iff divisor statement" without a no-cancellation hypothesis.** The converse is false; explicit degree-14 counterexample. report/sections/03c_graded_ramanujan.tex:118-121.
- **The direct (non-lifted) qubit transfer as a curve zeta.** Its zero at -2 is off the circle; the curve appears only after the non-backtracking lift. report/sections/03c_graded_ramanujan.tex:187-189.
- **The K-type grading as the Selberg flow grading.** P_K anticommutes with the geodesic generator, so it is not a flow grading, and the graded heat trace is a strictly positive theta sum: nothing cancels. report/sections/03f_selberg_letters_finite.tex:92-108; correction recorded at report/sections/03d_graded_ramanujan_continuum.tex:168-174.
- **The Ruelle zeta (and the all-odd tower) as graded Ramanujan objects.** (FE) and (Ram) fail even under Selberg's 1/4, because the even band is the odd band shifted by -1. report/sections/03e_selberg_letters.tex:126-129.
- **The reflection (PGL_2(R)) grading as the Selberg/Riemann grading.** It assigns the closed geodesics to the even sector and the archimedean ladder to the odd one, the opposite of the Riemann assignment, and carries no critical-line modes. report/sections/03d_graded_ramanujan_continuum.tex:144-151.
- **The draft's e^{t/2} rescaling of the modular scattering sector.** It can never unitarise that sector under any positive norm, since Re(lambda + 1/2) < 0. report/sections/03f_selberg_letters_finite.tex:38-43.
- **Truncated Maass-Selberg positivity as an RH criterion.** The truncated norm is positive throughout the strip whether or not RH holds. report/sections/03f_selberg_letters_finite.tex:43-45.
- **A doubled-bond CP (cMPS) realisation of the Selberg flow.** Both flat supertraces are negative distributions, hence cannot be cMPS ring norms. report/sections/03e_selberg_letters.tex:213-218.
- **The vacuum rebound state (SHW renewal picture inside K_S).** The vacuum is absorbing, the renewal integral diverges, and the selected cMPS has a single nonzero Schmidt weight. report/sections/04c_phantasm_channels.tex:97-109.
- **The prime-chain Lindbladian as a source of zeros.** Its spectrum is real - a union of M/M/1 bands and their Minkowski sums - and contains no zero of zeta, unconditionally for the classical part and on a weighted space for the full generator. report/sections/04c_phantasm_channels.tex:142-160.
- **Pair-correlation statements from the vacuum-decay population sector.** The formal trace of the squared distributional trace is not a defined product of distributions. report/sections/04c_phantasm_channels.tex:88-95.
- **Critical-CFT entanglement scaling for the Phantasm bond state.** The level density is Hagedorn, not Cardy, so the finite-entanglement scaling law does not apply. report/sections/04c_phantasm_channels.tex:200-205.
- **Exact finite-dimensional representations of the full BC algebra.** They collapse every phase generator to the identity. report/sections/04d_bc_symmetry_generators.tex:45-58.
- **Imposing Weyl-translation covariance on the Phantasm.** With full symplectic covariance it collapses the generator cone to the depolarizer and removes the oscillatory zero-like modes. report/sections/04d_bc_symmetry_generators.tex:143-157.
- **Arithmetic covariance alone as a source of a uniform odd rate.** The symplectic odd-sector counterexample has full Weil, Galois and parity covariance and unequal odd decay rates. report/sections/04d_bc_symmetry_generators.tex:161-182.
- **The reset test as a no-go criterion.** It applies only to a fixed no-event generator with scalar reset, not to the full cone. report/sections/04d_bc_symmetry_generators.tex:233-236.
- **The expectation of (-1)^F as the carrier of the supertrace sign in a graded cMPS.** It is identically +-1 for parity-homogeneous boundaries and carries no spectral information. report/sections/04f_cmps_twisted_supertrace.tex:44-48.
- **The phase-side guess's vacuum grading.** Prime jumps do not preserve it: a Gdb-even input acquires odd terms for every nonempty positive-rate prime set. report/sections/04g_phase_side_lindbladian.tex:104-115.
- **The rates 1/p.** The no-jump quadratic form is infinite and the finite-prime semigroups have no trace-norm limit at any positive time. report/sections/04g_phase_side_lindbladian.tex:130-133.
- **A prime cutoff as a bond cutoff.** The doubled-bond exponential stays invertible, hence non-compact, so the parity-inserted trace is not an ordinary trace. report/sections/04g_phase_side_lindbladian.tex:133-135.
- **A parity closure as a quotient by Q^x.** It changes only the boundary functional and imposes nothing of the adelic quotient; explicit 2x2 counterexample. report/sections/04g_phase_side_lindbladian.tex:143-155.
- **"Fermionic primes give zeros on Re s = 0".** True of each finite factor 1 - p^{-s}, false of the continued product 1/zeta, whose poles in the strip are the zeros of zeta with their orders. report/sections/04g_phase_side_lindbladian.tex:171-175, correcting report/sections/03b_graded_permutation.tex:139-147.
- **The Ramanujan-sum sector with prime jumps alone as the identification of K_S with a BC bond.** Ruled out by the phase-side negative. report/sections/04g_phase_side_lindbladian.tex:174-177.
