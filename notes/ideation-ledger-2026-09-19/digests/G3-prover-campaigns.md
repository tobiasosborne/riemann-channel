# Digest G3: the codex prover campaigns

Source lanes: L03 (riemann-cmps), L04 (ring-norm-tensor), L05 (yolo Lindbladian +
zeta conditions), L06 (graded Ramanujan + Selberg letters), L07 (Selberg dictionary,
resonances, Weil positivity). 357 lane entries, all absorbed below.

## Themes

1. The forced graded spectrum: rigidity, parities, and the sign of the prime part.
2. Why a grading is needed: the ungraded and bosonic no-go theorems.
3. The realisation gap: a supertrace is not a ring norm.
4. Explicit graded tensors: curves, tiny L-functions, graded expanders.
5. The graded Ramanujan definition and its qualifications.
6. The Artin-Schreier prototype and the locality dichotomy.
7. Side A: counts as ring norms, toral dynamics, Euler products of MPS.
8. Where RH would have to come from: positivity, metrics, manifest forms.
9. Weil positivity for transfer operators: what it buys and what it does not.
10. Channels that actually carry the zeros (and what they cost).
11. Bost-Connes, the prime chain, and what criticality really is.
12. The yolo phase-side Lindbladian: the audit and its exact by-products.
13. Euler product versus word multiplicity; the other grading.
14. Selberg as the worked infinite example.
15. The modular cusp: where the mechanism stops, and the Mayer route.
16. Representation theory and the archimedean factor.
17. Continuum structure: jumps, drift, aliasing, resonance divisors.
18. Independence of the zeta conditions, and the limits of the catalogue method.
19. Resonance physics: genuine mechanisms, rewritings, and proposed experiments.
20. Bookkeeping, provenance and method.

## Items

### G3-T1-1 The working picture, and the five-part audit template
- Absorbs: L03-001, L03-002
- Class: PARTIAL
- Raised by: TJO
- What: The whole programme in one sentence: dilation time is the line of a continuous matrix product state; its bond carries a "Riemann Lindbladian" whose unique fixed point is the pole of zeta at s = 1 and whose relaxation modes are the zeros; because ring norms are sums of squares while the zeros enter the explicit formula with a minus sign, the bond must be Z_2-graded, the zeros odd, the pole even, the ring norm a supertrace. The campaign split this into five questions — what is forced, what cannot exist, what exists concretely, what the prime chain gives, and what the finite-field prototype shows — and answered them. The spectral half is forced and realised; the physical cMPS half is not established.
- Lead: re-run the same five-part audit on any future Phantasm candidate before investing in it; it is the cheapest filter the notebook has.
- Where: notes/riemann-cmps/astra-brief.md:5; notes/riemann-cmps/astra-proofs.md:1340-1355

### G3-T1-2 Supertrace rigidity: the net spectrum is determined
- Absorbs: L03-003, L03-004
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: A graded spectral datum is a countable multiset of pairs (lambda, epsilon) with a growth bound, and its supertrace str e^{tG} = sum epsilon m e^{lambda t} as a distribution on (0, infinity). Pairing with cut-offs of t^k e^{-st} gives k! sum nu(lambda)(s-lambda)^{-(k+1)}, meromorphic on C, whose principal parts read off the net signed multiplicity nu. Hence any datum with supertrace equal to the prime comb has nu(1) = +1, nu(rho) = -m_rho, nu(-2k) = -1, and any datum with supertrace 2P_+ has nu(0) = +1, nu(-conj(rho)/2) = -m_rho.
- Lead: this is the standing test — compute any candidate object's supertrace and compare. Note also the freedom it leaves: a boson-fermion pair at the same eigenvalue is invisible.
- Where: notes/riemann-cmps/astra-proofs.md:64-108, :140-168

### G3-T1-3 Positivity forces the parities; the infinite flip set is the sharpest open problem
- Absorbs: L03-005, L03-006, L03-033, L03-034, L03-035
- Class: PARTIAL
- Raised by: orchestrator, sharpened by reviewer
- What: Flip the parity of an arbitrary set of eigenvalues away from the reference assignment. If the flip set among the nontrivial zeros is finite and the supertrace stays a positive distribution, then the pole is not flipped and no zero is flipped — "the zeros are fermionic" is forced, not chosen. The reviewer strengthened part (i) to be unconditional (monotone convergence of the cut-offs forces the pole even with no domination premise), and reduced the infinite case to one clean analytic question: can a conjugation-symmetric infinite flip set have atomic contribution greater than -Lambda(n) at every prime power, i.e. "density at most 1/2" in the atom weighting? Landau's theorem is useless here because the abscissa is already 1 from the pole and s = 1 is a genuine singularity.
- Lead: settle the density-1/2 question. It is self-contained analytic number theory about sub-multisets of zeros, and it closes T2(c) — full parity rigidity from positivity alone.
- Where: notes/riemann-cmps/astra-proofs.md:199-271; notes/reviews/riemann-cmps-2026-09-12.md:98, :713-731

### G3-T1-4 The prime part carries -2, and the generator whose supertrace is exactly 2P_+
- Absorbs: L03-011, L03-012, L03-013, L03-014, L07-016
- Class: EXPLORED-registered
- Raised by: TJO (as an observation), proved by prover, confirmed by reviewer twice
- What: Tr_dist Z(t) = 1 - 2 P_+(t) - e^{-t/2}/(e^t - 1) with P_+(t) = sum_{n>=2} (Lambda(n)/n) delta(t - 2 log n): coefficient -2, not -1 and not +2, and the distribution is not supported only at prime lengths. The report's earlier +Lambda(n) n^{-1/2} is wrong and applied the rate-1/4 damping twice; the factor 2 is the Jacobian dt = 2du and is variable-dependent, the sign is not. The concrete generator B := C_even + (K_S + l^2)_odd, G := 0 + B + diag(-(k+1/2)) has str e^{tG} = 2P_+ exactly, its fixed vectors are the even line, and RH becomes "every odd K_S mode has real part -1/4". Positivity does not fix the trivial-zero ladder's parity; only exact equality to 2P_+ does.
- Lead: promote G from a Hilbert-space semigroup to a trace-preserving generator on an operator algebra — the prover flags exactly this gap. Separately, find a physical reason (not a positivity reason) fixing the ladder's parity: it is the one parity the arithmetic leaves free.
- Where: notes/riemann-cmps/astra-proofs.md:373-447; notes/selberg/astra-proofs.md:728-744; notes/reviews/weil-positivity-2026-09-12.md:283-314

### G3-T2-1 Zeros require a bond grading and the periodic (Ramond) closure
- Absorbs: L05-061, L06-001, L06-002, L06-034, L06-037
- Class: EXPLORED-registered
- Raised by: TJO (the question), orchestrator (the answer)
- What: With bond H = H_+ + H_-, doubled transfer E and Gamma = Ad(P), the antiperiodic closure gives Tr E^n and the periodic one gives str E^n; the graded ring zeta is det(1-uE_1)/det(1-uE_0), so poles are net-even modes and zeros are net-odd modes. Two elementary obstructions explain TJO's feeling that quantum expanders only exist ungraded: an ungraded finite transfer has ring zeta det(1-uE)^{-1}, a reciprocal polynomial with no finite zeros at all; and a finite CPTP channel with all Kraus letters even has at least two stationary states, so it cannot be a unique-state graded expander. The minus sign lives in the mixed (+,-) coherences, not in the odd ket population: a tensor whose letters never move between parities has no zeros.
- Lead: state RH, FE and Ramanujan about the *divisor* of the parity-closed ring zeta rather than about a spectrum; the definition then passes verbatim to the continuum. Also fix shard 05's wording — the Weil-LPS channels have poles, not "nontrivial zeros".
- Where: notes/ramanujan-graded/definition.md:20-66; notes/ramanujan-graded/astra-proofs.md:1356-1391, :1603; notes/zeta-conditions/astra-constructions.md:120-122

### G3-T2-2 The zeta numerator is the odd sector: the trace/supertrace criteria
- Absorbs: L03-007, L03-008, L03-009, L03-010, L03-022, L03-023, L04-022
- Class: EXPLORED-negative
- Raised by: orchestrator, proved by prover, reproduced by reviewer
- What: If N_n = sum b_i^n - sum alpha_j^n with an uncancelled alpha, no finite matrix and no trace-class operator has Tr E^n = N_n (residue argument: the prescribed generating function has residue +m/alpha, an ordinary trace function has residue -m/alpha with m >= 0). So a numerator forces a grading; equivalently no all-even datum can have supertrace 2P_+ or the prime comb. The sharp criterion: (N_n) is a trace sequence iff exp(sum N_n u^n/n) is a normalised genus-zero canonical product with no nonconstant zero-free exponential factor, and a supertrace sequence of a finite graded matrix iff it is rational. A translation-invariant MPS has ring norm Tr(E_A^n) with E_A finite, so curve counts of genus >= 1 are never ordinary MPS ring norms; the same residue argument kills every ungraded carry automaton for the elliptic counts, while an abstract graded 2|2 transfer (diag(1,q) even, the integral Frobenius matrix odd) has supertrace N_n. For graphs the Ihara zeta has no finite zeros, so the graph case needs no grading and the curve case does — that dichotomy is the cleanest statement of what is special about RH relative to the Ramanujan-graph analogy.
- Lead: apply the genus-zero criterion to xi itself. Xi is entire of order one and genus one, so a trace-class realisation of the zeta side is excluded for genus reasons — a second no-go independent of the sign argument, stated nowhere in the files.
- Where: notes/riemann-cmps/astra-proofs.md:282-368; notes/ring-norm-tensor/astra-proofs.md:448-470

### G3-T2-3 What power traces cannot see (and where the continuum differs)
- Absorbs: L03-044, L05-054
- Class: LEAD-unpursued
- Raised by: prover
- What: On the lattice, zero eigenvalues and nilpotent blocks are invisible to every positive power trace — the de Bruijn even block Tr E_0^n = q^n hides q^J - 1 zero eigenvalues and possible nilpotents. For a cMPS a zero eigenvalue is *not* invisible: it contributes a constant to N(L) and a factor z to the determinant, and the degree gap obeys (D_+ - D_-)^2 = N(0) = |Tr Pi|^2, tying the superdimension of the bond to the vacuum norm.
- Lead: every trace and supertrace criterion in the campaigns explicitly cannot see the kernel. Nobody asks whether the Phantasm's even sector could hide structure there — an unexplored escape hatch from all the no-gos above.
- Where: notes/riemann-cmps/astra-proofs.md:1115-1166; notes/zeta-conditions/astra-constructions.md:50-61

### G3-T2-4 The bosonic genus bound: the drafted proof was false, the repair is load-bearing
- Absorbs: L04-023, L04-024, L04-025, L04-026, L04-027
- Class: EXPLORED-registered
- Raised by: orchestrator (drafted wrong), repaired by prover, confirmed by numerics and reviewer
- What: The drafted chain ended "<= 2 Tr(E_++) Tr(E_--)", which is false because Tr(sum A_s ⊗ conj A_s) = sum |Tr A_s|^2, not sum ||A_s||_HS^2 (one-species counterexample a = B = diag(1,-1): right side 0, left side 8; it failed on 173 of 400 random instances). The repair works with word traces: Tr S_±^n = sum_w |Tr a_w|^2 >= 0 and |Tr M^n|^2 <= Tr S_+^n Tr S_-^n by Cauchy-Schwarz at every n, and a Cesaro average then forces g <= 1 — so fermionic species are necessary at genus two. Two escapes remain open: even-odd cancellation on a larger bond (explicitly "does not exclude anything", so the proof only covers the minimal 1|2 bond) and an infinite bond. Equality does not give matrix proportionality or normality — only proportionality of word-trace vectors — and nilpotent transients are invisible to all of it; the Euler characteristic bookkeeping is (m-k)^2 - (z_e - z_o) = 2 - 2g with mk >= g, so C^{1|g} is not the minimal bond for g >= 4.
- Lead: decide the cancellation question — construct a purely bosonic genus-two tensor on a larger bond with cancelling spectrum, or prove none exists. That decides whether "fermions are forced" is a theorem or an artefact of minimality, and the same question is the crux for the Riemann case.
- Where: notes/ring-norm-tensor/astra-proofs.md:473-612; notes/reviews/ring-norm-tensor-2026-09-14.md:252-301

### G3-T2-5 The infinite-bond bosonic no-go, and the ceiling on any finite bond
- Absorbs: L04-028, L04-049, L04-051, L05-053, L05-064, L05-081
- Class: EXPLORED-negative
- Raised by: orchestrator, repaired and scoped by prover
- What: If the zeros are the odd modes of a cMPS transfer semigroup with an all-even Kraus decomposition then sum_rho e^{2t Re mu_rho} <= 2 ||S_+(t)||_HS ||S_-(t)||_HS < infinity, while the left side diverges — so odd (fermionic) jumps are forced in that analytic setting, under H-KRAUS-HS (the drafted 2 Tr S_+ Tr S_- version needs extra positivity that complete positivity does not supply). Nothing says odd jumps suffice, that finitely many suffice, or that the regularised object is a Hilbert norm. On the finite side: a nonzero finite-dimensional constant cMPS has analytic N(L) and cannot equal an atomic prime comb; the literal claim "fixed finite tensors give only supersingular zetas" is false (the campaign's own ordinary elliptic and genus-two tensors refute it); a finite bond *can* give infinitely many Euler primes, but never a nonrational Z(u), never infinitely many distinct divisor points, and under u = q^{-s} only periodic copies of finitely many points — not Riemann's zero distribution. Incommensurable log p lengths cannot be manufactured by going continuous either.
- Lead: four conjectural requirements are itemised for any proposed Riemann cMPS — analytic domains, a regularised trace, a tensor factorisation, and positivity. Use them as a checklist; and note that the graded norm constructions evade the old trace-class no-go precisely by having negative *net* coherence multiplicities.
- Where: notes/ring-norm-tensor/astra-proofs.md:614-643, :1092-1100; notes/zeta-conditions/astra-constructions.md:31-48, :361-373

### G3-T3-1 A supertrace is not a norm: the campaign's central honesty caveat
- Absorbs: L03-021, L05-052, L06-035, L06-047
- Class: PARTIAL
- Raised by: prover
- What: Verbatim: "assigning a negative spectral multiplicity does not construct a fermionic cMPS or identify a supertrace with its ordinary norm"; an even eigenvalue 1 and an odd eigenvalue 2 give supertrace -1; "a parity insertion requires a specified physical construction and boundary convention before any norm claim can be made". The vocabulary that came out of this: a *graded CP transfer* has an actual Kraus realisation E = sum A_i ⊗ conj A_i with nonnegative ring norms, a *graded spectral transfer* is merely a graded operator with a divisor — and the notebook's Artin-Schreier, Riemann and flat-trace constructions are all spectral, not CP. Three objects must also be kept apart: a physical ring norm, a ring amplitude str F^n, and an open-chain sum of amplitudes (a one-letter model with letter F has norm |Tr(Pi F^n)|^2, not Tr(Pi F^n)). The Selberg proposal of a doubled bond with even drift and no jumps was refuted three ways: a single Kraus operator is not its own doubled transfer, multiplication operators are not Hilbert-Schmidt on a non-atomic L^2, and str e^{tB_perp} = 2 - e^t - e^{-t} < 0 while any cMPS ring norm is nonnegative.
- Lead: the concrete missing object is a boundary condition / parity-insertion convention on a ring that turns a genuine Hilbert norm into a supertrace. That is the single most valuable target in the whole group; failing that, admit the larger graded *spectral* category explicitly.
- Where: notes/riemann-cmps/astra-proofs.md:11, :1292-1293; notes/ramanujan-graded/astra-proofs.md:1447-1453; notes/selberg-letters/astra-proofs.md:292-337

### G3-T3-2 The parity-dimension obstruction to any doubled-bond realisation
- Absorbs: L06-039
- Class: LEAD-unpursued
- Raised by: prover (one paragraph)
- What: Every doubled Kraus bond has n_0 - n_1 = (D_+ - D_-)^2 >= 0, i.e. at least as many even as odd dimensions, whereas a cohomological (Weil / Selberg) grading can have more odd than even dimensions.
- Lead: this may be the actual reason no CP realisation of the Artin-Schreier or Riemann graded transfers has ever been found. Any proposed CP realisation must either have more even than odd dimensions or live on an infinite bond where the count fails — check this before attempting one.
- Where: notes/ramanujan-graded/astra-proofs.md:1621-1625

### G3-T3-3 Zeta data do not determine the physical state
- Absorbs: L05-068, L06-042
- Class: LEAD-unpursued
- Raised by: prover (asides, not asked for)
- What: Three different tensors give identical ring norms and functional equation for the same elliptic curve: the four-letter 1|1 construction (maximally mixed stationary state, nonzero entanglement), the shard 06g product letters diag(1,pi)/sqrt2 (zero entanglement, no full-bond TP gauge), and a two-letter damping representative (pure stationary vacuum). Relatedly the letter degree is data, not a property of the channel — redundant copies change the Hastings benchmark while implementing the same channel — so "Ramanujan" is a property of a presentation.
- Lead: if this is general, zeta data alone can never pin down the Phantasm, and something beyond the zeta (a metric, an entanglement spectrum, a fixed point) must select the realisation. Ask also whether there is a presentation-independent formulation of Ramanujan (an infimum over Kraus conventions).
- Where: notes/zeta-conditions/astra-constructions.md:187-189; notes/ramanujan-graded/astra-proofs.md:1589-1591

### G3-T4-1 The natural elliptic tensor, and why genus two breaks the rule
- Absorbs: L04-012, L04-013, L04-029, L04-044
- Class: EXPLORED-registered
- Raised by: orchestrator, proved by prover
- What: For an ordinary elliptic curve take the ket bond V = Lambda^*(H^{1,0}) = C + C dz = C^{1|1} with A_s = a_s diag(1, pi) and P = diag(1,-1). The doubled bond is diag(1, conj pi, pi, q) with parity = total form degree — exactly H^0, H^{0,1}, H^{1,0}, H^2 of the torus — and every word gives Tr(P A_w) = (1 - pi^n) prod a_{s_i}, so the ring norm is |1 - pi^n|^2 = N_n. The count is a supertrace because it is a Lefschetz number, and the modes are fermionic exactly when they are odd-degree forms. This is the campaign's one *natural* tensor rule; genus two breaks it, since C + H^{1,0}(J) is the exterior algebra truncated after degree one and is not the cohomology of the curve. Two honest caveats: bond-odd is not physically fermionic (the physical letters are even, the physical vector has Schmidt rank one, so its configurations do not enumerate points), and the Jacobian product tensor contains a Frobenius-invariant graded subspace with str F^n|_S = N_n(C) whose rank-six projector is provably *not* of the form B ⊗ conj B'.
- Lead: the non-product projector is a real structure — an entangled boundary condition on a ring. Nobody asked what physical operation it is, or whether the Riemann case needs one. And nobody built a tensor whose basis configurations actually enumerate rational points.
- Where: notes/ring-norm-tensor/astra-proofs.md:300-332, :645-651, :977-1009

### G3-T4-2 What a practitioner can build tonight: pair shift, four-letter elliptic, Kloosterman, supersingular
- Absorbs: L05-065, L05-066, L05-067, L05-073, L05-076, L05-083
- Class: EXPLORED-registered
- Raised by: TJO (the request), built by prover
- What: E0, the pair shift: four letters (a,b) in {0,1}^2 with A_{(a,b)} = diag(1,[a=b]) on C^{1|1} gives N_n = 4^n - 2^n and Z(u) = (1-2u)/(1-4u) — a zero by literal destructive interference with a subshift, with infinitely many surviving Euler primes on a finite bond. The general recipe behind it (the sub-system rule) needs three extra hypotheses: unit-coefficient word states, a repetition- and rotation-compatible subsystem, and "zeros = subsystem poles" only before net cancellation. For y^2 = x^3+x+1 over F_5, four letters on C^{1|1} (two diagonal with Gram overlap pi, two parity-changing) give the elliptic zeta with a genuine TP channel on the whole bond, RH visible because pi conj(pi) = 5; the projective rung adds (1-u) and the functional equation. Over F_4 the requested q^n - Kl_n norm exists on a 1|1 bond with four printed letters, and y^2+y = x^3 over F_4 gives a double zero at u = -1/2 on the real axis of the critical circle with the Artin-Schreier involution realised exactly as U = Pi.
- Lead: "U = Pi" is the cleanest realisation in the notebook of "odd sector = nontrivial character"; check whether it generalises beyond Artin-Schreier. The standing pattern to test: an exponential-sum L-factor alone is never a positive norm, only the curve completion is.
- Where: notes/zeta-conditions/astra-constructions.md:162-197, :266-281, :365-375

### G3-T4-3 Genus two: the certified F_5 tensor and the nine-letter family
- Absorbs: L04-002, L04-030, L04-031, L04-032, L04-033, L04-037, L04-038, L04-039, L04-042, L04-043, L04-060
- Class: EXPLORED-registered
- Raised by: orchestrator, built by prover, checked by numerics and reviewer
- What: Two even and one odd tensor on C^{1|2} reproduce N_n for the supplied F_5 curve at every n, proved by a Krawczyk-style rational contraction certificate (nine active coordinates, radius 1e-30, exact rational Jacobian) and independently re-run by the reviewer. Separately, for q + 1 >= 4 sqrt q (every prime power q >= 16) a closed-form nine-letter tensor has even spectrum {1,q,0,0,0} and odd block exactly diag(conj D, D), with a C^{1|g} extension whenever q + 1 >= 2g sqrt q; base change reaches that regime for any ordinary curve. The block equations are E_o = [[M,N],[conj N, conj M]] with rank N <= number of odd species, which alone kills the one-fermion ansatzes: the suggested a_1 = 1, B_1 = 0, a_2 = 0 forces M = 0 and a negation-symmetric odd spectrum, impossible for any ordinary curve with nonzero Frobenius trace, and fourteen further ansatzes failed numerically (only 3 even + 2 odd and CM-diagonal 2+2 solved). The reviewer noticed two unstated facts: the threshold q + 1 >= 2g sqrt q is *exactly* nonnegativity of the Weil lower bound on N_1, and the symmetric split t = wg = (q+1)/2 is optimal for the ansatz, not lazy.
- Lead: the Weil-lower-bound coincidence is unexplained and suggestive — the construction dies precisely when the curve might have no points. Also: whether the F_{q^m} tensor descends to F_q was never asked, and failed searches prove no lower bound on species count. Adopt the characteristic polynomial (not eigenvalue thresholds) as the standard acceptance test — the three nilpotent even modes appear as eigenvalues of size ~1e-5, the cube root of the residual.
- Where: notes/ring-norm-tensor/astra-proofs.md:710-794, :824-974; notes/ring-norm-tensor/numerics.md:152-184; notes/reviews/ring-norm-tensor-2026-09-14.md:324-330

### G3-T4-4 The selection problem: no closed form without an extra principle
- Absorbs: L04-003, L04-018, L04-019, L04-034, L04-035, L04-036, L04-040, L04-041, L04-047
- Class: PARTIAL
- Raised by: numerics lane, echoed by prover
- What: Three independent restarts of the free 2-even-1-odd genus-two ansatz reach residual < 1e-25 with completely different spec M and couplings: the solution set is a positive-dimensional family that is not a single gauge orbit, and no entry pattern tied to q survives. In every small-q solution M is *not* the Hodge Frobenius and |m_i|^2 != q — the cohomological branch M = conj D, N = 0 is a saddle that failing searches are attracted to and no solution reaches. Gauge is A_s -> G A_s G^{-1} with G = diag(g_0, H), so B_1 = 0 and "all B_s diagonal" are genuine restrictions; integral ideal classes (Latimer-MacDuffee, Waterhouse) are *not* complex gauge orbits, since complex tensors forget the ideal class; and the CM type is arithmetic marking that the counts cannot recover. Existence for two even and one odd species is exactly a real polynomial feasibility system in 28 unknowns, and by real-closed-field transfer a complex solution implies an algebraic one — so "only transcendental entries work" is not a legitimate conclusion. Conjecture T4.C (a universal three-species tensor for every ordinary genus-two curve) is open, as is natural selection from the curve data.
- Lead: the CM-diagonal ansatz is the one called "the most promising shape for a closed form", solves exactly with two odd species, and the prover never touched it — its unknowns reduce to a 3x3 Gram matrix plus two rank-one couplings, small enough for symbolic elimination. Impose one of the three named extra principles (Hodge metric normality, Rosati self-adjointness, a physical-index normalisation) as an extra equation on the feasibility system. Also unasked: what cond(V) of the Hodge basis means arithmetically, and whether there is a species-count threshold at small q above which the cohomological branch reappears.
- Where: notes/ring-norm-tensor/numerics.md:186-216, :346-375; notes/ring-norm-tensor/astra-proofs.md:796-822, :1041-1060

### G3-T4-5 Tiny L-functions: Horner automata, Gauss sums, voltage covers, Artin factorisation
- Absorbs: L05-060, L05-069, L05-070, L05-071, L05-072, L05-074, L05-075
- Class: EXPLORED-registered
- Raised by: TJO ("tiny L functions"), built by prover
- What: The Horner Dirichlet MPS uses the residue field F_q[x]/M as bond, letter H_c the Horner step, start at 1 and close with the character row: b_n = chi^T (sum_c H_c)^n |1> and L(u,chi) = sum b_n u^n, giving explicit degree-one L-functions over F_2 and F_3 with |alpha|^2 = q. Character factorisation of a graded tensor is honest representation theory (N_n^chi = (1/dim chi) Tr(P_chi Gamma E^n), Z = prod_chi L^{dim chi}), but calling the factors *Artin* needs an actual cover and its monodromy; the genuine tiny Artin example is a voltage double cover of a rose, whose sign factor has logarithmic trace (-1)^n and is therefore not a norm. The two-loop Z/2 graph cover gives the correct inverse-pairing mechanism: the reversal / no-backtracking identity forces the common product q = 3 in the reduced Bass quadratics, and the script converts them into a physical 1|1 graded elliptic norm tensor. The standard Gauss-sum convention gives 1 + Gu, not 1 - Gu.
- Lead: closing the Horner automaton into a trace is wrong — it imposes the residue-automaton return condition f = x^n f + b, not Frobenius orbits. That is the sharpest concrete statement anywhere of the side A / side B gap. Also: every physical mode of the Ihara cover is *even*, which refutes "even = trivial character, odd = nontrivial" as a general theorem; that pattern is specific to Artin-Schreier cohomology and must be re-derived for each new group action.
- Where: notes/zeta-conditions/astra-constructions.md:104-118, :199-300

### G3-T4-6 Graded quantum expanders exist: Clifford theory, the Pauli qubit, LPS
- Absorbs: L06-011, L06-014, L06-015, L06-016, L06-018, L06-038
- Class: EXPLORED-registered
- Raised by: orchestrator, corrected by prover
- What: Take a group G with an index-2 subgroup, sign character eps, and an irreducible pi whose restriction splits: then P pi(g) P = eps(g) pi(g), so coset parity grades the letters, and Harrow's transfer bounds every non-trivial constituent sector by sector — graded quantum expanders are abundant. The graded quantum Ihara-Bass identity holds sector by sector with trivial edge exponent -(D-2)(D_+-D_-)^2/2, vanishing exactly for a balanced grading. The smallest example is literally an elliptic curve: letters X,X,Y,Y,Z,Z on a qubit with P = Z give D = 6, q = 5, graded zeta (1+2u+5u^2)/((1-u)(1-5u)) and ring norms 1 + 5^n - (mu^n + conj mu^n), the point counts of y^2 = x^3+4x+b over F_5 — verified exactly three times. The zeta Artin-factorises over the constituents, zeros for odd constituents and poles for even ones. The LPS bipartite example has the extremal Hecke eigenvalue in the odd sector; the full Weil representation graded by even/odd functions is not a unique-state graded expander (two stationary states).
- Lead: two small unfinished objects. The (5;13) LPS reduced formula f_4 f_{-4}/(f_14 f_{-14}) with b = 13 fell out of an audit and was never identified arithmetically. And a genuine bound on the Weil cross-coherences would give a graded expander with an arithmetic pedigree — "work on the irreducible blocks" was chosen instead.
- Where: notes/ramanujan-graded/definition.md:182-229; notes/ramanujan-graded/astra-proofs.md:341-489, :1316-1328

### G3-T5-1 The graded Ramanujan definition and the bookkeeping it needs
- Absorbs: L06-004, L06-005, L06-006, L06-007, L06-008, L06-009, L06-040, L06-041
- Class: EXPLORED-registered
- Raised by: orchestrator, corrected by prover
- What: RH = every nontrivial divisor point has |lambda| <= sqrt q; FE = an even similarity J with J E J^{-1} = q E^{-1} on the support of the divisor; Ramanujan = both; manifest (Hilbert-Polya) = a Gamma-even positive definite G with E^† G E = q G. Both closures are sums of squares, so Tr E_0^n >= |Tr E_1^n| automatically — a consequence of norm positivity, *not* of a centred Weil kernel. Four corrections the definition needs: the trivial "set" must be a designated invariant subspace or a signed multiset with parities (period modes need not be even; "1" is trivial only as the H^0 partner of q); the P-mode E(P) = P sum eps_s A_s A_s^* is structural but not trivial, giving a real balance condition |N_even - N_odd| <= 2 sqrt(D-1); a critical line means nothing without a supplied *pair* of reference rates, since a normalised TP generator always has spectral bound zero; and operator FE is strictly stronger than divisor FE because Jordan data must match.
- Lead: carry the pair of reference rates and the signed trivial divisor as explicit data in every claim; check H-leading (a simple retained even Perron mode with no odd mode at q) before quoting any growth rate, since equal even and odd copies of the identity give zero supertrace at every length.
- Where: notes/ramanujan-graded/definition.md:67-132; notes/ramanujan-graded/astra-proofs.md:1474-1557

### G3-T5-2 Divisor statements are weaker than dynamical statements
- Absorbs: L06-010, L06-012, L06-013, L06-017
- Class: EXPLORED-negative
- Raised by: orchestrator (drafted), refuted by prover
- What: Three drafted upgrades all fail. "Band in both sectors iff net divisor on the circle": the converse is false — an explicit primitive C^{1|1} example with D = 14 has the out-of-band value 10 cancelling completely between sectors and invisible in the zeta, so a no-hidden-mode hypothesis is needed. Graded Alon-Boppana for the odd sector is REFUTED: Phi = (1/4)(Ad I + Ad I + Ad P + Ad P) has rho(Phi_1) = 0 in every dimension, and a primitive degree-16 family has rho(Phi_1) = 0 with unbounded bond, because in the odd restriction a word contributes 2 Re(Tr U_+ conj Tr U_-) which can be negative. "Every parity coherence decays at exactly the critical rate" overstates: an eigenvalue bound allows Jordan polynomial factors and a one-sided divisor bound controls only visible modes. And a circle numerator need not be a Weil polynomial, let alone a curve: N_P(1) = 16/3 for one unitary example, and six I's with two X's and two Y's give (1-3u)^4 over F_9, which would force -2 rational points.
- Lead: find the structural hypothesis that *does* force the large eigenvalue into a prescribed sector — all that survives is max{rho(Phi_0 off I), rho(Phi_1)} >= lambda_H. And find the arithmetic restriction under which "channels are curves" is true.
- Where: notes/ramanujan-graded/astra-proofs.md:206-339, :1246-1354

### G3-T5-3 The status table: which of the notebook's own objects satisfy the definition
- Absorbs: L06-036, L06-048, L06-054, L06-055
- Class: PARTIAL
- Raised by: orchestrator (the audit), answered by prover
- What: A case-by-case verdict with a minimal repair for each row, several never applied. Two rows matter most. The Riemann graded generator of 04b is a graded *spectral* semigroup, not a constructed doubled-bond transfer; its regular zero modes have centre -1/4 iff RH, but the odd archimedean ladder -(k+1/2) sits strictly to the left and is not in the trivial set, so a full single-line/FE statement fails *even assuming RH*. The Selberg two-term complex has both constant roots (s = 1, 0) as net *odd* zeros, so there is no even Perron pole at all and the notebook's own definition of a graded transfer channel does not cover its best infinite example. The Selberg flat tower must have its first band selected rather than its descendants declared trivial, and the full Ruelle divisor fails FE and Ramanujan even under coercivity.
- Lead: for the Riemann generator the repair list is explicit — supply reference rates 0 and -1/2, treat the archimedean ladder as structural data, complete the pole pair, and supply the resonance-divisor realisation. Otherwise widen the central definition or accept that the two best infinite objects sit permanently in the spectral bin.
- Where: notes/ramanujan-graded/astra-proofs.md:1600-1611; notes/selberg-letters/astra-proofs.md:111, :134-145

### G3-T6-1 The corrected Artin-Schreier sign law, and the fermionic sign as a permutation sign
- Absorbs: L03-036, L03-037, L03-042
- Class: EXPLORED-registered
- Raised by: orchestrator (drafted, declared possibly false), refuted and replaced by prover, verified 12/12 by reviewer
- What: S_n(g) = (-1)^{n-1} delta_n Tr E_g^n with delta_n = det(S | ker P(S)) — the determinant of the cyclic shift on the radical, not the drafted eta(-1)^{d_n}, which depends on the rank alone. The proof introduces an embedding matrix A_{ri} = theta^{q^{r+i}} satisfying A^t = A, A^2 = C, A^{[q]} = SA, AS = S^{-1}A — identities that use cyclic indices, not diagonalisation, so they survive q | n where S is not semisimple. Equivalently the sign is the periodic function 1 - 2·1[2h | n], and two cheap coefficient tests decide when the naive readings hold: P(-1) != 0 for alpha_i = -lambda_i(E_g), P(-eta(-1)) != 0 for the drafted law. When the radical is trivial, S_n(g) = sgn(Frob_n) Tr E_g^n: the fermionic sign of the count on a ring of n sites is the sign of the Frobenius permutation.
- Lead: this is the "permutations before curves" statement. The unasked question: is there a *zeta-side* permutation whose signature produces the minus sign in the explicit formula? Separately the A-matrix trick (an equivariant square root of the trace-form Gram matrix) looks reusable for any cyclic-module sign computation.
- Where: notes/riemann-cmps/astra-proofs.md:871-984, :1209-1259

### G3-T6-2 RH for the prototype from scaled unitarity; the transfer is a Clifford circuit
- Absorbs: L03-040, L03-041, L03-043, L04-005, L04-006
- Class: EXPLORED-registered
- Raised by: orchestrator (from numerics), proved by prover, verified index-for-index by reviewer
- What: E_g E_g^† = q I because summing the oldest input spin collapses the row inner product — so every eigenvalue has modulus sqrt q and is semisimple: the Riemann hypothesis for this curve family, from the transfer matrix alone, with no appeal to Weil. Moreover E_g/sqrt q factors as Fourier ∘ quadratic phase ∘ cyclic permutation, three Clifford operations, with an explicit symplectic M_g in Sp(2J, F_q): the Artin-Schreier transfer *is* a finite metaplectic/Weil operator. Consequently |Tr E_g^n|^2 = q^{n + dim ker(M_g^n - I)}, so the Weil bound saturates exactly when M_g has order dividing n; and the family is supersingular, proved over arbitrary finite fields by a finite-value-set plus linear-recurrence plus Vandermonde argument with no RH modulus premise.
- Lead: "a quadratic exponential-sum transfer matrix is a Clifford circuit" says the prototype chain is free/Gaussian, hence efficiently simulable — which may be exactly why it is tractable and the zeta side is not. Nobody interpreted this. Also unasked: which symplectic conjugacy classes arise as M_g, i.e. what the distribution of maximal Artin-Schreier curves looks like group-theoretically. And the "finite value set + recurrence + Vandermonde" technique is a general "spectrum is roots of unity" detector, never pointed anywhere else.
- Where: notes/riemann-cmps/astra-proofs.md:1021-1259; notes/ring-norm-tensor/astra-proofs.md:89-145

### G3-T6-3 The character-sector grading and the root-of-unity filter
- Absorbs: L03-038, L03-039
- Class: EXPLORED-registered
- Raised by: prover (a construction the brief did not ask for), repaired by reviewer
- What: bbE = (E_0 + 1)_even + (sum_{a != 0} F_{ag})_odd has str bbE^n = #C(F_{q^n}) for all n, with F F^† = q I and odd dimension (q-1)q^J = 2g(C): the grading *is* the trivial-versus-nontrivial additive-character decomposition of the Hilbert-90 fibre sum. Three repairs the reviewer insists on: the point at infinity is not a character sector so the two poles split; the odd summands are the corrected F_{ag}; and "carries exactly" is true only of the nonzero net spectrum. Separately the root-of-unity filter L(g,T)^h = prod_{omega^{2h}=1} D_g(omega T)/D_g(T)^h gives a finite constructive recipe for the Frobenius spectrum from the transfer spectrum — rotate the eigenvalue multiset by roots of unity and subtract — using no Weil root-size input anywhere.
- Lead: this is the only place in the campaigns where the graded picture is completely explicit and completely correct; it is the template any zeta-side construction should imitate. Ask whether a "rotation and subtraction" analogue exists on the zeta side, converting a transfer spectrum into the zeros.
- Where: notes/riemann-cmps/astra-proofs.md:1046-1166; notes/reviews/riemann-cmps-2026-09-12.md:401-424

### G3-T6-4 The locality dichotomy: cut ranks and Conjecture T0.C
- Absorbs: L04-007, L04-008, L04-009, L04-010
- Class: PARTIAL
- Raised by: orchestrator (drafted wrong), corrected by prover, half-closed by numerics and reviewer
- What: A contiguous bipartition of a *ring* cuts two virtual edges, so the flattening rank is at most D^2 (not D), and the bound is sharp. In a self-dual normal basis the quadratic Artin-Schreier amplitude has cut rank <= D^2 for *every* n — the prover's growing table 2,4,8,16,8,4,2 was a basis artefact — while the cubic amplitude Tr(x^{1+q+q^2}) has cut rank 2,4,8,16 (q=2) and 1,9,27 (q=3), roughly doubling every two sites. Conjecture T0.C states the surviving dichotomy: after fixing a normal-basis prescription and quotienting by trace-invisible Artin-Schreier coboundaries, a fixed finite tensor with amplitudes psi(Tr g(x)) for every n can exist only if the trace function has quadratic degree. Self-dual normal bases exist only for n odd, or n = 2 mod 4 with q even.
- Lead: prove the growth half, or find a nonquadratic trace function with bounded cut rank in the self-dual basis. If T0.C is true it is the sharp statement of "equation-local tensors only see Gauss sums", and it tells the Phantasm that a Riemann tensor cannot be equation-local.
- Where: notes/ring-norm-tensor/astra-proofs.md:146-237; notes/ring-norm-tensor/numerics.md:274-322

### G3-T7-1 Counts as honest ring norms; one toral system for both sides
- Absorbs: L04-004, L04-011, L04-014, L04-015, L04-020
- Class: EXPLORED-registered
- Raised by: TJO / orchestrator, proved by prover
- What: For an ordinary elliptic curve #E(F_{q^n}) is literally the index of the principal ideal (1 - pi^n) in the endomorphism order — the count *is* the norm of an ideal, and under Lenstra E(F_{q^n}) = O/(pi^n - 1)O as O-modules (verified, but only for conductor-1 orders, and with no choice of isomorphisms compatible for all n). The single toral system (T^2, M) realises both sides: its fixed-point zeta is Z(E,u), and by Mobius inversion it has exactly as many primitive closed orbits of each length as E has closed points of each degree — though the resulting bijection is non-canonical. The Koopman picture is an injection of index q, not a permutation; its only finite orbit is {0}, and the flat supertrace det(1 - M^{nT}) = N_n is contributed by k = 0 alone, so the count lives in the bond and the physical index carries no counting information; an honest infinite-label Fourier tensor exists but adds nothing.
- Lead: the count-as-ideal-norm is the only place in the campaigns where the count is an arithmetic norm rather than a supertrace fitted to it. Never followed: is there a Riemann-side ring whose ideal norms are the zero-counting data? Also untried: a curve with conductor f > 1, to see whether the tensor construction notices.
- Where: notes/ring-norm-tensor/astra-proofs.md:241-299, :333-372

### G3-T7-2 pi-adic digits and the carry automaton
- Absorbs: L04-021
- Class: PARTIAL
- Raised by: TJO ("optional but valuable"), proved with the expected reason corrected
- What: Every class in O/pi^n O has a unique digit expansion; two words agree in the cyclic quotient O/(pi^n - 1) exactly when integral cyclic carries exist, and those carries are *bounded* by C_D/(|pi| - 1), so the cyclic equivalence is recognised by a finite automaton. Surjectivity nonetheless fails: for O = Z[i], pi = 1+2i the digits hit two of four classes at n = 1, and |1 - pi^2|^2 = 32 > 25 at n = 2. So the failure of a finite carry automaton is *not* unboundedness of carries; it is that recognising equality of digit words is not counting quotient classes with weight one.
- Lead: what does the carry automaton compute, and is there a weighted or graded version whose signed ring count is N_n *and* which factors as sum_s A_s ⊗ conj A_s? Nothing was attempted; this is the concrete bridge between the arithmetic norm and a Kraus factorisation.
- Where: notes/ring-norm-tensor/astra-proofs.md:422-470

### G3-T7-3 MPS ring norms as an Ihara-type Euler product (the quantum-Ihara sidequest)
- Absorbs: L03-053, L03-054, L03-055, L03-058
- Class: EXPLORED-registered
- Raised by: the note's author, re-derived and verified by reviewer
- What: Theorem 1 of the quantum-Ihara note is a genuine loop-admitting *extension* of Watanabe-Fukumizu, not a special case: WF's hyperedges are 2-element subsets of V, so a bouquet is not one of their graphs. Its Corollary 2 expresses MPS ring norms |Tr(A_{i_l}...A_{i_1})|^2 as an Ihara-type Euler product over primitive classes (verified for l = 1..5, Euler product truncated at |w| <= 6 agreeing to 3.6e-7), with a norm bound (max_i ||E_ibar E_i||)^{-1/2}. Corollary 3 handles the unitary (quantum-walk, "Ramanujan-like") case, Corollary 4 the D = 2 degeneration where T = E_1 + E_2. Reversal of non-backtracking words is a bijection because the edge involution is an involution, so both convention differences wash out of det(1 - u·).
- Lead: this is a ring-norm generating function *with* an Euler product built from an MPS, which sits directly against the theorem that curve counts are never MPS ring norms — worth asking which arithmetic-like zetas *are* realisable this way. Also: does the loop-admitting extension have a Bass-type determinant proof? And "reversal is a symmetry of the word set" is the graph-side analogue of rho -> 1 - rho.
- Where: notes/reviews/round2-2026-09-12.md:14-59, :99-126

### G3-T8-1 Rosati positivity derives Ramanujan — the one place RH is proved rather than assumed
- Absorbs: L04-016, L04-017, L04-045, L04-046, L04-050
- Class: EXPLORED-registered
- Raised by: orchestrator, proved by prover, singled out by reviewer
- What: The Rosati involution is an R-algebra involution of K ⊗ R = C^g; positivity forbids it from permuting distinct primitive idempotents and from being the identity on a factor, so it is complex conjugation at each place, and applying the embeddings to pi pi^† = q gives |phi_j(pi)|^2 = q at *every* place. Total degree in dimension two would only give |pi_1|^2|pi_2|^2 = q^2 — it does not supply the two separate equalities. This is the one place in the files where RH is derived rather than assumed; the elliptic PH operator (q^{-1/2} M^* on H^1 with the Hodge metric, unitary because lifted Frobenius is a conformal similarity) has the conclusion inside its hypotheses unless H-DEG is split. Honest negative: in the constructed genus-two tensors the odd transfer is sqrt q times a unitary *by construction*, so RH is manifest only after the Frobenius moduli have been supplied, and for the certified tensor the required metric identification is missing. There is no lifted Riemann dynamics and no positive Hodge/Rosati metric on the zeta side — "that missing dynamics and positivity, rather than the formal notation for a supertrace, is the substantive break in the analogy".
- Lead: find the Riemann-side analogue of a positive involution on a commutative algebra whose positivity forces conjugation place by place. Equivalently: is there a metric on the bond, determined by the arithmetic, in which a counting tensor is automatically normal with odd block sqrt q times unitary? That would be RH from complete positivity. Note also that promoting a PH unitary to a self-adjoint Hamiltonian needs a phase branch the curve does not supply — on the Riemann side that branch would be the height.
- Where: notes/ring-norm-tensor/astra-proofs.md:374-397, :1011-1090

### G3-T8-2 Band type versus circle type, and the finite Hashimoto-lift theorem
- Absorbs: L06-003, L06-043, L06-057, L06-058, L06-060
- Class: EXPLORED-registered
- Raised by: orchestrator (the open item), proved constructively by prover, verified by reviewer
- What: Two mechanisms give the same divisor statement: in Harrow-type examples the odd sector is Hermitian, lands in a band, and the circle appears only after the non-backtracking (Hashimoto) lift; in curve-type examples the odd block is sqrt q times a unitary directly. The finite lift theorem settles the relation: with T = SR - J_0 and Sigma = RS self-adjoint, one has Sigma R = R(T + qT^{-1}), an explicit two-sided inverse pushforward for mu != ±1, a companion model C with an explicit metric G_C satisfying C^* G_C C = q G_C, and an operator functional equation. G_C is positive definite iff the band bound is *strict*: at an endpoint the companion has a genuine size-two Jordan block (exact counterexamples: the 5-regular graph K_3 □ Q_3, and a ten-letter Pauli channel). The critical-circle points ±sqrt q are *not* exceptional for the pushforward; only mu = ±1 is. The compact Selberg and finite graph cases are the same theorem twice — LETTERS/HAAR gives reality, ANALYSIS gives the pushforward isomorphism, BOUND gives the line or circle, ENDPOINT gives the full operator form.
- Lead: the inverse pairing is doing the work; whether a non-inverse-paired analogue exists is open. And a Hilbert-Polya operator must either exclude the threshold or accept a semisimplification — this is a structural constraint on what a Phantasm operator can be.
- Where: notes/selberg-letters/astra-proofs.md:395-496, :593-623; notes/ramanujan-graded/definition.md:36-41

### G3-T8-3 The metric converse: skew-adjointness, Riesz bases, and the Gram experiment nobody ran
- Absorbs: L05-026, L05-027, L05-028, L05-029, L05-030, L07-026, L07-053
- Class: PARTIAL
- Raised by: prover (both campaigns), independently in the resonances lane
- What: "The generator is anti-Hermitian so its spectrum is on a line" is only true for a genuinely *skew-adjoint* operator: -d/dx on L^2(0,infinity) is closed and skew-symmetric but its spectrum contains a half-plane. In finite dimensions the exact converse is: T is diagonalisable with all eigenvalues of real part -2gamma iff there is a positive definite M with B^* M + M B = 0 for B = T + 2gamma — and diagonalisability must be checked separately, since a Jordan block at the right spectrum gives a term linear in t, impossible for any positive metric. Infinite-dimensionally one needs the eigenvectors to be a Riesz basis with uniform two-sided bounds, plus a maximal-domain statement. The evidence is bad: the Gram condition number of the zero eigenvectors grows from about 10 (first 24 ordinates) to about 700 (last 24 of 3000), largest neighbouring overlap 0.570 -> 0.939; under RH, fixed depth 1/4 and increasing zero density force overlaps towards one, so no *bounded* renorming of the model space K_S can exist. The Krein/PT framing gives the same question: does the solution cone of K^* G = GK contain a positive matrix?
- Lead: compute Gram condition numbers at 3000, 10000 and 30000 zeros and fit the growth. Divergence kills the Riesz-basis route to a metric proof; boundedness would be strong positive evidence. Cheap, decisive, flagged twice in two separate campaigns, never run. Discipline: a positive matrix obtained by fitting known zeros has no evidentiary value — the input must be prime- or branch-defined.
- Where: notes/yolo-lindblad/astra-structure.md:546-601; notes/resonances/astra-freeassoc.md:99-103, :417-450

### G3-T9-1 Weil positivity for an arbitrary transfer operator; the trivial set is not optional
- Absorbs: L07-045, L07-066, L07-067, L07-070, L07-079, L07-080, L07-081
- Class: EXPLORED-registered
- Raised by: orchestrator, proved by prover, corrected twice by reviewer
- What: nu_l = r^{-l}(Tr X^l - sum_S mu^l) is positive definite iff every retained mode has |mu| <= r. If the retained multiset is invariant under mu -> r^2/conj(mu) then the Weil form equals the mode-pairing form and positivity is equivalent to every mode being its own partner; an off-circle pair makes the whole form negative by Lagrange interpolation. So "positivity is the spectral-gap half of RH, nothing more" — and every candidate transfer operator must come with a *declared* trivial set, radius and duality. A wrong trivial set flips the criterion: with the unenlarged S_0 the Hastings clause is false for *every* unitary family, because Phi(I) = I always makes alpha = D an eigenvalue and D > 2 sqrt(D-1) for D >= 4. Huang's graph criterion is literally h_k = nu_0 - nu_k with the same r and the same trivial set (verified to 1e-13 on five graphs), and for a finite exponential sum positive definiteness is equivalent to boundedness. An adjoint-paired family can have no reciprocal duality at all while the Weil form is still well defined and positive.
- Lead: write the missing definition of "Ramanujan for a lead" — a bound on poles of a continued boundary response, after a specified centring and subtraction of trivial factors, with the coupling and reciprocal pairing declared. Temperedness of the continuous spectrum does not imply it. And escalate the Toeplitz window with the expected off-line distance or the numerics report false positives (a pair at radius 1.01 needs L = 40).
- Where: notes/weil-positivity/astra-proofs.md:90-201, :395-441; notes/reviews/weil-positivity-2026-09-12.md:237-264, :399-427

### G3-T9-2 The Kraus dichotomy, and how the functional equation and RH enter as conditions
- Absorbs: L05-055, L05-056, L05-057, L07-068, L07-069, L07-077, L07-078
- Class: EXPLORED-registered
- Raised by: orchestrator, corrected by prover and reviewer
- What: Every Ad-family has nonnegative ring traces and a conjugation-closed spectrum with no pairing hypothesis at all — one of the two symmetries RH needs is free, and there is no Kraus counterexample to it. Inverse pairing buys the functional equation (mu -> (D-1)/mu); adjoint pairing buys Hilbert-Schmidt self-adjointness of Sigma, hence a real spectrum; both at once force every letter unitary, and then Weil positivity is exactly Hastings' bound. ("Both pairings iff a scalar multiple of a unitary" is false — Ad is quadratic in B, so it is B^†B = I; B = 2I disproves the drafted version.) The escape hatch: B_i = G U_i G^{-1} is inverse-paired, far from adjoint-paired, yet Sigma is similar to a self-adjoint operator so its spectrum is real — confirmed 6/6 numerically, not proved to be the only such class. As conditions on a graded tensor: the exact FE is parity-preserving invariance of the reduced nonzero net spectrum under lambda -> q/lambda (additively lambda -> kappa - lambda for a generator, which is the natural symmetry there), and RH is |lambda|^2 = q with sufficient visible mechanism a positive metric E_-^† M E_- = q M. Inverse-paired letters do *not* give the FE for a raw doubled sum (B = diag(1,2) counterexample).
- Lead: the unused object is the *continuous-time* Weil criterion — take nu(t) = sum exp((lambda - kappa/2)t), extend by conjugate reflection, and require positive definiteness of every kernel matrix (nu(t_j - t_k)); then Re lambda <= kappa/2 with equality under additive reflection. Stated once and never used, yet it is the generator-side Weil positivity condition the cMPS programme needs. Also open: is every inverse-paired family with real Sigma-spectrum of the similarity form? That is the finite-dimensional model of the Hilbert-Polya metric problem.
- Where: notes/weil-positivity/astra-proofs.md:226-441; notes/zeta-conditions/astra-constructions.md:63-88; notes/weil-positivity.md:96-101

### G3-T9-3 Weil positivity is blind to Jordan blocks; continuous ring norms from the Dyson expansion
- Absorbs: L07-071, L07-072
- Class: EXPLORED-registered
- Raised by: orchestrator (the brief), proved by prover
- What: For X = r[[1,1],[0,1]] every nu_l equals 2, so the Weil form is positive definite, yet ||(X/r)^k e_2|| diverges and no inner product unitarises X/r (the continuous version is identical). So "RH iff Weil positivity" holds with multiplicities, but "RH iff a Hilbert-Polya inner product exists" needs semisimplicity in addition — repeated zeros of zeta would be exactly this issue. On the side-A half, for L(x) = Kx + xK^† + sum R_j x R_j^† the trace of e^{tL} is a sum over jump sequences of |Tr A|^2 >= 0 with the *free propagators retained between jumps*; the propagator-free product drafted in the brief is false for non-commuting K and R_j, invisible at first order by cyclicity and wrong from the second (0.19440805 against 0.19452865).
- Lead: never equate "all modes on the line" with "there is a self-adjoint operator". The Dyson formula is the continuous analogue of "ring norms are nonnegative" and gives no line reflection and no positive definiteness of shifted subtracted traces — those need side-B structure.
- Where: notes/weil-positivity/astra-proofs.md:601-666, :676-741

### G3-T9-4 The Riemann dictionary under Weil positivity, and its four missing inputs
- Absorbs: L07-073, L07-074, L07-075, L07-076
- Class: PARTIAL
- Raised by: orchestrator, made precise by prover, reviewed
- What: Centre at a = -1/4; the reflection rho -> 1 - conj(rho) becomes eta -> -1/2 - conj(eta) with fixed line Re eta = -1/4, and the exact identity is sum_rho ghat(rho) conj(ghat(1 - conj rho)) = double integral of g(t) conj(g(s)) e^{(t-s)/4} Tr_dist Z(t-s), with the exponent /2 forced because Z runs at frequency gamma/2. Corrections: xi is entire so the trivial set is empty ({0,-1/2} only after an artificial augmentation), and the negative-time extension is tau(-u) = e^{u/2} conj(tau(u)). The modes of Z cannot be a trace-class eigenvalue list at all, since |e^{t eta(rho)}| >= e^{-t/2} — distributional or flat traces are the only option. Four hypotheses carry the dictionary: H-ZD (test space and convergence), H-ZEF (the arithmetic evaluation, confirmed numerically to six digits with 70 zeros), H-ZM (the link to the compressed semigroup), H-ZW (the infinite-dimensional Weil converse).
- Lead: H-ZW is explicitly *not* available from the finite interpolation or from Bochner-Schwartz, because F(0) = infinity and one cannot interpolate away infinitely many unwanted modes with a finite polynomial — the reviewer calls that refusal the most valuable sentence in T6, and an infinite-dimensional version of the Lagrange separation is a genuine open problem stated here. H-ZM is the one nobody has attempted.
- Where: notes/weil-positivity/astra-proofs.md:743-938

### G3-T10-1 The vacuum-decay Lindbladian and the reusable absorbing-vacuum gadget
- Absorbs: L03-017, L03-018, L03-019, L03-031, L05-039
- Class: EXPLORED-registered
- Raised by: orchestrator, built and corrected by prover
- What: With -(B + B^†) = |j><j| and e^{tB} -> 0, the map L(x) = bB x + x bB^† + J x J^† is a CPTP generator whose unique stationary density is the vacuum, whose spectrum is {0} ∪ spec(B) ∪ conj spec(B) ∪ pair sums, with the two coherence lists odd and the rest even. The brief's rank-one Lindblad formula does not survive to infinite dimension (H-LP supplies no bounded exit vector), and the replacement works for *any* strongly stable contraction semigroup with no exit vector needed — a general-purpose gadget that turns any candidate Riemann semigroup into a genuine channel carrying it as odd coherences, and which reproduces the qualitative behaviour without importing a zero-built model space. But the zeros then appear *twice* (each rho on |v><vac| and on |vac><v>), plus an even pair-sum sector the forced datum does not have, so this channel realises the *double* of the Phantasm's datum. The pair-sum "form factor" |Tr Z(t)|^2 is not a distribution at all — the diagonal pair values accumulate in a bounded interval — so no pair-correlation conclusion follows.
- Lead: halve the coherence sector, e.g. by a reality or self-conjugacy constraint on the bond, to get an actual realisation of the forced datum. And note the gadget's own moral: this behaviour is generic, so it carries no arithmetic content by itself.
- Where: notes/riemann-cmps/astra-proofs.md:450-570; notes/yolo-lindblad/astra-structure.md:808-821

### G3-T10-2 The renewal equation fails, the bond is unentangled, and the complementary-halves statement
- Absorbs: L03-020, L03-024, L03-051, L07-048, L07-050
- Class: EXPLORED-negative
- Raised by: orchestrator (from HANDOFF), refuted by prover, reproduced by reviewer
- What: The drafted fixed-point equation rho_inf ∝ integral of Z(t) Omega Z(t)^* is *not* solved by Omega: the integral equals T·Omega and diverges, and in the original model space it is not even type-correct. What would be needed is a nontrivial rebound inside the model space with finite holding time. The stationary bond is rank one, so the half-chain Schmidt spectrum is {1} — every ring amplitude containing a jump vanishes identically, so the only periodic field configuration is the vacuum. Hence the complementary-halves statement: the vacuum-decay channel has the zeros as odd relaxation modes but a pure stationary state and trivial entanglement; the prime-chain Gibbs Lindbladian has the ring lengths as entanglement spectrum but a real spectrum with no zeros; no construction has both, and the Phantasm needs both (a definitional clause, not a theorem). The SHW renewal generator with reinsertion state Omega is a genuine new transfer process, but the scalar exit does not determine Omega, and a formal trace-preserving reinsertion rule is not a proof that the minimal semigroup is conservative.
- Lead: the design brief for the next candidate is explicit — a channel with a *mixed* stationary bond whose entanglement spectrum is the ring lengths and whose odd relaxation spectrum is the zeros, once each. For the renewal route, the missing input is precisely the rebound state and a reason for choosing it: test three candidate Omegas on the finite one-port model and compare against the unchanged no-event poles.
- Where: notes/riemann-cmps/astra-proofs.md:571-592; notes/reviews/riemann-cmps-2026-09-12.md:599-611; notes/resonances/astra-freeassoc.md:329-367

### G3-T10-3 The model space is assumed, not constructed (H-LP), and the candidate zeta bond
- Absorbs: L03-015, L03-016, L04-048
- Class: PARTIAL
- Raised by: prover (as a scope flag), endorsed by reviewer
- What: The whole Riemann-channel side rests on H-LP: that Z(t) = e^{tB} is a strongly continuous contraction semigroup on the model space with pure point spectrum {-conj(rho)/2}, one eigenvector per zero, and Z(t) -> 0 strongly. Nothing "independently establishes innerness of the symbol xi(1-2i tau)/xi(1+2i tau), completeness of its asserted modes, or the asserted geometric identification", and the identification of the added even line with the constant function / Eisenstein residue on the modular surface is a borrowed naming convention, not a construction. The proposed ket space for zeta, C + one odd mode per positive-height zero, has two named problems: its (-,-) sector is much larger than the desired pole sector with nothing specified to kill or regularise it, and ket/bra exchange is complex conjugation while the functional equation is rho -> 1 - rho, which agree only on the critical line — so treating the FE as automatic ket/bra exchange puts RH into the interpretation.
- Lead: prove innerness of the symbol and completeness of the mode system from the functional equation. Find the extra duality that the bra/ket exchange is missing. And note what the elliptic case suggests: there the (-,-) sector carried exactly H^2 with eigenvalue q, so the question is what plays the role of H^2 for zeta.
- Where: notes/riemann-cmps/astra-proofs.md:369, :436-447; notes/ring-norm-tensor/astra-proofs.md:1064-1072

### G3-T11-1 Normal KMS only above the transition; the thermofield bond, entropies and Hagedorn growth
- Absorbs: L03-025, L03-026, L03-048, L03-049, L03-050
- Class: EXPLORED-registered
- Raised by: orchestrator, proved by prover, constants fixed by reviewer
- What: For alpha_t = Ad(N^{it}) a normal KMS_beta state exists iff beta > 1 and equals N^{-beta}/zeta(beta) (with two wording corrections: the arithmetic system is the Bost-Connes algebra, not all of B(l^2), and the high-temperature range is 0 < beta <= 1). The Gibbs state factorises over prime sites, so the thermofield double has entanglement at each site and none between sites — bond dimension one along the prime chain — with entanglement spectrum beta log n + log zeta(beta), i.e. the ring lengths. The entropy constants: S(rho_beta) = 1/(beta-1) + log(1/(beta-1)) + (1 - gamma) + o(1); with a prime cutoff at beta = 1 the constant is *exactly* zero, by an identical cancellation of the two Mertens constants; with a bond cutoff it is -gamma/2, and the observed -0.25 is the 0.671/log N correction. The number of entanglement levels below E is floor(e^E) — Hagedorn growth with beta_H = 1, the same threshold as the Bost-Connes transition — which is not Cardy (4.85e8 against 9.6e4 at E = 20).
- Lead: the prime-cutoff cancellation is "a pretty fact worth stating with the cancellation visible". The falsifiable consequence: the CFT finite-entanglement scaling law does not apply, the log log N term in the truncated entropy is the departure, and it is a computable fingerprint to test any future proposed bond for the prime gas against.
- Where: notes/riemann-cmps/astra-proofs.md:601-637; notes/reviews/riemann-cmps-2026-09-12.md:530-597

### G3-T11-2 The prime chain's spectrum is real: the zeros must live in a different bond
- Absorbs: L03-027, L03-028, L03-029, L03-030
- Class: EXPLORED-negative
- Raised by: orchestrator, proved and corrected by prover
- What: The prime-by-prime detailed-balance Lindbladian (isometries mu_p|n> = |pn>, up-rate r_p, down-rate r_p p^beta) restricted to the diagonal is a product of independent birth-death chains whose spectrum is the closure of the finite Minkowski sums of explicit bands — real, hence unable to contain the nonreal zero modes; the closure is genuinely essential (limit points in no finite sum). Under sum_p r_p p^beta < infinity the full quantum generator is bounded self-adjoint on the KMS-weighted space, so the off-diagonal sectors are real too. "The Bost-Connes transition is ergodicity breaking" is *not* established: what is proved is escape of the normal Gibbs mass as beta -> 1+ and absence of a stationary probability on finite-support configurations — not a closing gap, multiple steady states, or loss of dynamical ergodicity, all of which need a specified generator. Side A supplies the ring lengths and a reversible relaxation model; side B supplies the zeros; the two are proved not to be the same object.
- Lead: the prover flags one uncovered case — an unbounded quantum closure for the natural rate choice r_p = p^{-beta}, which the bounded proof does not reach. And the real content behind the slogan is missing: specify a generator and prove an actual gap statement. The campaign's whole difficulty is then to find the map coupling the two sides.
- Where: notes/riemann-cmps/astra-proofs.md:638-765

### G3-T11-3 The Galois / cover test: two candidate graded bonds that cannot both exist
- Absorbs: L03-045, L03-046, L03-047
- Class: LEAD-unpursued
- Raised by: orchestrator (statement X1), sharpened by reviewer
- What: Gal(Q^ab/Q) has the Dirichlet characters as its character group, and the prime-chain MPO has eigenvalues L(beta, conj chi)/zeta(beta) in the character basis, only the principal one having a pole — so a Galois-symmetric graded bond would have even sector = the pole, odd sector = the zeros of the L(s,chi). But in the Artin-Schreier case the graded object computes the zeta of the *cover*, whose numerator is the product over all nontrivial characters, so the faithful analogue is the Dedekind zeta of Q(zeta_N), not zeta alone. Two caveats: the MPO eigenvalues are *values* of L at a fixed beta, not zeros — nothing in the notebook puts any L-zero into the prime chain — and the prime chain's real spectrum proves it is not the Galois-graded bond.
- Lead: the decisive test, stated by the reviewer and never run: by the rigidity theorem a graded datum with supertrace 2P_+ has *only* the zeta zeros, while a datum carrying the zeros of all L(s,chi) has a different supertrace (the ray-class prime comb). The two cannot both hold for the same bond, so either the Galois analogy or the 2P_+ normalisation must give. Cheap and decisive on any future Galois-symmetric proposal.
- Where: notes/reviews/riemann-cmps-2026-09-12.md:505-524

### G3-T11-4 The annulus basis and the true reversible prime dynamics
- Absorbs: L05-031, L05-032, L05-033, L05-040, L05-047
- Class: EXPLORED-registered
- Raised by: prover (a structural discovery, not asked for)
- What: On the radial local space at p the normalised annulus indicators h_{p,k} form an orthonormal basis with V_p h_{p,k} = h_{p,k+1} exactly — a plain unilateral shift — while the vacuum is *not* the occupation-zero vector but a geometric superposition. So the phase (Haar) picture and the shell (occupation) picture are genuinely different representations of the same infinitely many shifts, with vanishing product of reference overlaps; an abstract bijection of bases does not intertwine them. The unique normal stationary density of a one-prime reversible pair is diagonal in *annuli*, not in Ramanujan shells, with a uniqueness proof covering coherences. The drafted shell Markov chain was wrong twice: the shell-diagonal algebra is not preserved, and the detailed-balance rate was backwards (d = u p^beta, not u/p). A single forward prime has a full spectral disk lambda_p(z-1), |z| <= 1 — not the real spectrum of the reversible occupation chain, which is a different operator.
- Lead: resolving each shell edge into its own jump does deliver the Gibbs fixed point exactly, at the cost of one jump per edge instead of one per prime — i.e. losing "the letters are the primes". That trade-off deserves an explicit decision. Any future model must declare which reference vector and which basis it uses.
- Where: notes/yolo-lindblad/astra-structure.md:605-687; notes/yolo-lindblad/astra-finite-model.md:337-391

### G3-T11-5 At criticality the right object is a weight on a completed configuration space
- Absorbs: L05-008, L05-009, L05-010, L05-034, L05-035, L05-036, L05-037, L07-049
- Class: EXPLORED-registered
- Raised by: orchestrator (the question), answered by prover
- What: Every nontrivial Ramanujan shell observable has expectation b^{1-beta} prod_{p|b}(1 - p^{beta-1}) -> 0 as beta -> 1+, the cleanest sense in which criticality selects the vacuum; and the Gibbs phase states converge weak-* to Haar on the *entire* phase algebra, not merely on Ramanujan sums. But "the critical state is the pure vector state of e_0" is false: Haar is the vector state of e_0 on B(L^2) and pure there, while its restriction to C(Zhat) is Haar integration, hence mixed. The corrected critical reversible dynamics lives on the radial local algebra, needs no summability of rates, and its stationary product state's valuation distribution is *exactly* Haar's — but that state has no normal extension to B(G) for any beta. At beta = 1 the occupation Gibbs object is a normal faithful semifinite *weight*, not a state, and the KMS identity forces any normal KMS density to be a multiple of it; the completed product measure is a genuine probability on configurations with infinitely many occupied primes, which is the concrete answer to "what is at b -> infinity". Forward dynamics do *not* select Haar — they converge weak-* to delta_0. Relatedly the Bost-Connes critical measure's divergence is at *large* jumps, so no Levy-style small-jump completion applies and a new state space is needed.
- Lead: this is the best available replacement for the guess's "critical KMS fixed point". The next step is to ask what the *ring norm* or transfer spectrum of this critical dynamics is, since its density is non-normal and no naive trace exists. Do not conflate the unnormalised occupation weight, the completed product probability, and Haar on the phase algebra, even where restricted formulas agree.
- Where: notes/yolo-lindblad/astra-structure.md:236-268, :689-765; notes/resonances/astra-freeassoc.md:355-361

### G3-T12-1 The yolo guess, its Galois structure, and the grading that is not preserved
- Absorbs: L05-001, L05-002, L05-003, L05-004, L05-041
- Class: EXPLORED-negative
- Raised by: orchestrator (from TJO's central priority), audited by prover
- What: The guess was jumps R_p = sqrt(1/p) V_p ⊗ T_{log p} on phases times an archimedean line, with letters = primes and ring norm Tr[Gamma_b e^{tT}]. What survives: V_p is an isometry commuting with every Galois unitary, the Ramanujan shells |b> = c_b/sqrt(phi(b)) span exactly the Galois-fixed sector and reduce both V_p and its adjoint, and all four drafted shell ladder formulas are correct once the missing case distinction is added. What dies: "the prime jump *is* the Galois (Shor) map" holds only for sqrt(p) V_p^* at a level coprime to p, and the proposed grading (even = the constant function) is *not preserved by the generator* — the dissipator produces odd cross terms |1><p| + |p><1| with coefficient lambda_p sqrt(p-1)/p for every prime, confirmed numerically. Without an invariant odd sector the whole "RH = uniform decay of the odd sector" reading has nothing to act on. Bookkeeping: D = x d/dx + 1/2 is skew-adjoint, so -iD is the Hamiltonian, and on multiplicative Haar the 1/2 disappears.
- Lead: the shell ladder is the one fully solid piece and any successor can be built on it, but a successor must either pick a grading the prime jumps actually preserve or supply a dynamics that does. Fix the measure convention once in shared definitions — this is exactly the kind of factor that would move a "critical line at 1/2" claim.
- Where: notes/yolo-lindblad/astra-structure.md:29-128; notes/yolo-lindblad/astra-finite-model.md:289-297

### G3-T12-2 Rate 1/p kills it: no normal limit, no ordinary trace
- Absorbs: L05-020, L05-021, L05-048
- Class: EXPLORED-negative
- Raised by: prover
- What: With lambda_p = 1/p the no-jump operator has infinite quadratic form on every nonzero vector, and worse, the finite-prime semigroups have *no trace-norm limit at any positive time*: every shell diagonal entry and the vacuum survival both tend to zero, while a trace-norm limit would be a positive trace-one operator with zero diagonal in a complete basis. Adding a trace-preserving archimedean factor cannot help, since partial trace is trace-norm continuous. Separately, on the infinite doubled space the cutoff generator is bounded, so its exponential has a bounded inverse and cannot be compact: Tr[Gamma_b e^{tL_F}] is not an ordinary trace, and "a finite prime cutoff is not a finite bond cutoff". The critical rate is exactly the divergent one, sum_p 1/p (reproved without prime asymptotics).
- Lead: either renormalise the divergence explicitly, or move to the radial local algebra where summability is not needed. And whatever "ring norm" means for an infinite bond has to be *defined* before it is computed — parity supplies no regularisation.
- Where: notes/yolo-lindblad/astra-structure.md:15-27, :420-445

### G3-T12-3 The zero hunt: exact resolvents, the shift beta+1, and a real spread instead of a line
- Absorbs: L05-025, L05-043, L05-044, L05-045, L05-046
- Class: EXPLORED-negative
- Raised by: orchestrator (designed the hunt), executed by prover
- What: The ordered-word vacuum resolvent is exactly 1/(1 - sum_{p<=P} p^{-z}) and the multiset one exactly a *shifted* partial zeta, with z = s + beta + 1; pole exclusion in the target rectangle is analytic (a uniform bound plus triangularity), not a failed root search, and argument-principle windings vanish on a fine mesh. No pole moves toward s = 1. The shift comes from the rate and the two vacuum amplitudes and cannot be discarded. The full finite doubled generator is triangular with *real* eigenvalues spreading over an interval (397 distinct values in [-1.643,-1.213]), so a purely dissipative commuting-jump phase model cannot produce relaxation frequencies on a line. A parity jump does implement an exact uniform -2gamma shift on the odd sector, and Galois dephasing gives exactly -gamma on cross-character coherences (error 5.6e-17 over 13630 coherences) — but the hunt lives entirely in the Galois-trivial sector, so the shift is irrelevant there, and the unmodified guess has no invariant sector for it to act on.
- Lead: a successor must have amplitudes that do not produce the beta+1 shift, must get its frequencies from a Hamiltonian or the archimedean factor, and must put the zeta data in a *non*-trivial character sector if dephasing is to matter. Guard: a shrinking ratio F/(1/zeta_P) is not evidence of a hidden reciprocal-zeta factor.
- Where: notes/yolo-lindblad/astra-finite-model.md:196-335; notes/yolo-lindblad/astra-structure.md:529-544

### G3-T12-4 Exact by-products: Gauss vectors, log L minus log zeta, and a compound-Poisson BC transfer
- Absorbs: L05-005, L05-006, L05-007
- Class: EXPLORED-registered
- Raised by: orchestrator (the drafts), proved and corrected by prover
- What: V_p^* ghat_chi = p^{-1/2} conj(chi(p)) ghat_chi is exact, but the Lindblad recycling term uses forward images, so the coherence |e_0><ghat_chi| is *not* a scalar mode (explicit mod-3 counterexample, orthogonal residual 0.61 — not a truncation artefact); the one-dimensional compression carries an extra 1/p the draft missed. The exact identity behind it: sum_p (psi(p)-1)/p^beta = log L(beta,psi) - log zeta(beta) + prime-power corrections, with every bad prime contributing -p^{-beta} and nothing omitted. And the Bost-Connes transfer operator is *exactly* the exponent of a compound-Poisson generator with jump rates p^{-k beta}/k on prime powers, with eigenvalue L(beta, conj chi)/zeta(beta) on the Gauss vector (for primitive chi; imprimitive fails, mod 6 counterexample).
- Lead: build the *Galois-unitary* dephasing model (jumps U_{a_p} with a_p ≡ p mod b) rather than the isometry model: its coherence decay rates are literally log L - log zeta up to prime powers, so character sectors carry L-data by construction. The open part is bad primes, where no such unit exists. The compound-Poisson generator is a fully specified arithmetic dynamics whose spectrum is L/zeta with no zeros put in by hand — its weakness is that the eigenvalues are values at real beta, not on the critical line.
- Where: notes/yolo-lindblad/astra-structure.md:130-234

### G3-T12-5 The reciprocal-zeta matrix element, the cancellation-free Ramanujan carrier, and the unbounded evaluation at 1
- Absorbs: L05-011, L05-012, L05-017, L05-019, L05-038
- Class: PARTIAL
- Raised by: orchestrator (the central question), answered by prover
- What: The brief asked which generating function of the dynamics has 1/zeta in a denominator with poles exactly at the zeros; the answer is that there is presently no defined ring norm of the guess and no such resolvent. What *is* exact: with A(w) = sum n^{-w} V_n = prod_p (I - p^{-w}V_p)^{-1}, the inverse has vacuum matrix element exactly 1/zeta(w + 1/2), together with a table of which length weight produces which shift. Two nearby facts: inside the critical strip the poles of sigma_{1-s}(n)/zeta(s) are exactly the zeros with their orders, because all numerator zeros have Re s = 1 — a clean cancellation-free scalar carrier; but c_b(1) = mu(b) is *not* a jump overlap (all overlaps are nonnegative and put zeta in the numerator), and evaluation at the integer 1 is an unbounded functional even on the Galois-fixed sector, which is the structural reason the Ramanujan 1/zeta cannot be a matrix element. Also: every V_n is a conserved Heisenberg observable of the forward dynamics, which is why vacuum coherences cannot fully decay.
- Lead: three named missing steps would turn the reciprocal-zeta matrix element into a spectral statement — extend the family in operator norm past Re w > 1, establish a closed generator, and make its poles generator eigenvalues. A successor also needs a *bounded* functional playing the role of "value at 1". And the conserved commutative family {V_n}, indexed by the integers, was noticed only as an obstruction and never explored as a structure — what algebra does it generate, and what is its joint spectrum?
- Where: notes/yolo-lindblad/astra-structure.md:270-363, :469, :767-806

### G3-T12-6 The adelic route: real prime periods and four missing ingredients
- Absorbs: L05-022, L05-023, L05-024
- Class: LEAD-unpursued
- Raised by: orchestrator (the draft), proved elementarily and scoped by prover
- What: Prime periods log p do arise geometrically: the adele-class point with component zero at p has stabiliser the image of Q_p^x, so after quotienting by the compact norm kernel the norm coordinate is R_+ / p^Z with logarithmic period log p. "Merely translating an auxiliary logarithmic line and inserting Pi performs none of these operations." To identify a ring observable with an adelic orbit trace one needs four things — a specified quotient or correspondence, an intertwiner, a test-function trace regularisation, and equality of the resulting distributions with all local normalisations — and none is supplied. Connes's 1999 trace formula proves a local cutoff formula and a finite-set-of-places formula, and explicitly distinguishes the global problem; it does not supply an unconditional ordinary heat trace of anything like this Lindbladian.
- Lead: make the substitution honestly — let the archimedean coordinate be the norm coordinate of an actual adele-class orbit modulo the compact norm kernel, rather than a free line with a translation on it. Then tick the four items in order.
- Where: notes/yolo-lindblad/astra-structure.md:505-525

### G3-T12-7 The campaign's own hand-off list, and the three directions the negative does not close
- Absorbs: L05-049, L05-050
- Class: LEAD-unpursued
- Raised by: prover
- What: Four next computations, in order: select the algebra and limiting dynamics (a summable-rate phase model or the radial local model); at a finite bond cutoff record the changed isometry relations and test grading invariance, complete positivity and the stationary density; compare the three actual generating functions (word resolvent, Poisson evolution, multiset inverse) against exact controls, with the warning that matching an arithmetic scalar after changing the functional is not a spectral realisation; and only then attempt the adelic route. What the negative audit explicitly leaves undecided: an additional archimedean operator, a different boundary functional, or a justified infinite-domain construction.
- Lead: no shard has taken any of this up. The boundary-functional item is the cheapest: enumerate candidate boundary functionals on the word expansion and see which one produces multiset rather than word multiplicities.
- Where: notes/yolo-lindblad/astra-structure.md:828-829; notes/yolo-lindblad/astra-finite-model.md:403

### G3-T13-1 Commuting jumps do not restore the Euler product
- Absorbs: L05-013
- Class: EXPLORED-negative
- Raised by: prover
- What: Even though the V_p all commute, the ordered-word resolvent keeps multinomial multiplicities Omega(n)!/prod k_p! — "pq" occurs twice in the length-two word sum but once in a multiset Euler product — and Poisson evolution gives products of Poisson, not geometric, weights. Neither the shell stay term nor a parity insertion removes them: "a parity insertion changes a trace functional; it does not replace Omega(n)!/prod k_p! by one."
- Lead: what *does* restore the Euler weights is a different construction — either prod_p (I - z_p V_p)^{-1} directly, or an occupation-space trace with one coordinate per prime. Anyone hoping "commuting jumps give an Euler product" should stop here.
- Where: notes/yolo-lindblad/astra-structure.md:365-383, :447-449

### G3-T13-2 The exterior occupation parity: the grading the arithmetic actually wants
- Absorbs: L05-014, L05-015
- Class: LEAD-unpursued
- Raised by: prover (in passing, one paragraph)
- What: Take one occupation coordinate k_p >= 0 per prime with finite support; unique factorisation identifies the basis with the integers and the energy sum k_p log p with log n, so the thermal trace is zeta(s). Restrict to occupancies 0 and 1 and give each configuration parity (-1)^{sum k_p}: the absolutely convergent *signed* trace is sum mu(n) n^{-s} = 1/zeta(s). "This is an exterior occupation-space parity. It is different from the fixed doubled-bond parity in this brief." (Caution: the slogan "all primes fermionic, zeros on Re s = 0" is correct only about the finite factors, not about the continued 1/zeta.)
- Lead: the programme has been using one grading where the arithmetic wants another. Pursuing the exterior/fermionic occupation parity gives 1/zeta as a supertrace with no boundary-functional games, and would give "zeros = odd sector" an honest fermionic realisation. Never followed up.
- Where: notes/yolo-lindblad/astra-structure.md:451-454

### G3-T14-1 Why Selberg, and the letters principle
- Absorbs: L06-044, L06-071
- Class: EXPLORED-registered
- Raised by: orchestrator, cautioned by reviewer
- What: In every manifest example in the book the unitarity of the odd block has a source that is not complete positivity: Parseval, Deligne, or it was put in by hand. The Selberg zeta of a compact hyperbolic surface is the one infinite object where the trace formula is a theorem, the divisor is known, and the source of reality is known (self-adjointness of the Laplacian). The organising idea is to separate what the *letters* give (reality and the form's branch norms, from Haar-unitarity of the sl2 flows and the sl2 relations) from what an extra bound gives (the critical-line placement, Selberg's 1/4) — exactly as Ramanujan is an extra bound for a Hermitian graph channel. The reviewer's caution: once every retained rate is on the line and the block is semisimple, *some* positive form always exists, so "derived from the letters" is new content only because this particular form is the transported Haar form.
- Lead: the letters principle generalises and is the campaign's most transferable idea; apply it to any new candidate by asking separately what the letters force and what must be imported.
- Where: notes/selberg-letters/draft.md:7-22; notes/reviews/selberg-letters-2026-09-16.md:162-179

### G3-T14-2 The two-term stable transverse complex, and grading as cancellation
- Absorbs: L06-045, L06-046, L06-056, L06-070, L07-013, L07-058, L07-059
- Class: EXPLORED-registered
- Raised by: orchestrator (the question), answered by prover, checked by reviewer
- What: Of four candidate transfers, the function flow gives the tower determinant, the full transverse forms give the Ruelle zeta Z_S(s)/Z_S(s+1), and the *two-term stable* transverse complex (even A, odd A+1) gives Z_S itself as D_tow(s-1)/D_tow(s). The complex is built from a letter: df = (U_+ f) eta_+ intertwines A and A+1 because [A, U_+] = -U_+, and the reviewer verified the divisor identity nu(z) = m_A(z) - m_A(z-1) against the Selberg divisor at every point type. This is graded cancellation made concrete — bosonic and fermionic determinants pairing so that an orbit-counting partition function is governed by a reduced determinant — and it suggests a relative or boundary complex for the cusp. Two warnings: the full retained Ruelle divisor has a *parity-exchanging* symmetry nu(-s) = -nu(s), not the notebook's parity-preserving FE; and grading explains the sign, not the modulus — "cancellation can remove or retain poles but cannot move a surviving off-line pole onto a line", and a cohomological description that silently discards the cusp resonance sector proves a statement about the wrong object.
- Lead: prove the global leafwise closed-range cohomology statement behind d — the pairing of even level m with odd level m+1 with the odd level zero surviving is currently asserted only on resonant modules. That would upgrade the determinant ratio from a divisor identity to an actual cohomological cancellation, the natural home for "zeros are fermionic". Separately, the parity-exchanging reflection is a *second kind* of functional equation and may be the more natural symmetry for a supersymmetric object; whether the Riemann side has an analogue is unexamined.
- Where: notes/selberg-letters/astra-proofs.md:90-158, :145; notes/resonances/astra-freeassoc.md:538-556

### G3-T14-3 The first-band manifest form, branch tags, and the 1/4 threshold
- Absorbs: L06-050, L06-051, L06-052, L06-053, L06-066, L06-069, L07-008, L07-009
- Class: EXPLORED-registered
- Raised by: orchestrator, corrected by prover, reviewer-verified
- What: For a first-band resonant state, the Casimir gives Omega u = lambda(1+lambda)u and the pushforward is a Laplace eigenfunction; since the Laplacian is a sum of squares of skew-adjoint letters, the eigenvalue is >= 0, forcing lambda into [-1,0] ∪ (-1/2 + iR) (away from negative-integer exceptional parameters). The transported Haar form G(u,v) = <pi_* u, pi_* v> makes e^{t/2}e^{-tX} unitary exactly when the 1/4 coercivity holds. Three corrections are load-bearing: Omega = X^2 + U_+U_- - X (not +X), so the operator FE is J X J^{-1} = 1 - X; the *single total* pushforward form is degenerate on a partner pair (Gram matrix [[1,1],[1,1]]), and branchwise orthogonal pullbacks are needed — exactly the same phenomenon on graphs and channels; and at Laplace eigenvalue exactly 1/4 the algebraic multiplicity is twice the geometric one, so no positive form makes the full block unitary. The continuous Ramanujan statement is the equivalence "first band on the midpoint line iff no nonconstant exceptional eigenvalue", with the constant mode excised. For PSL(2,Z) the discrete 1/4 is *known* (Booker-Lee-Strömbergsson), byte-verified.
- Lead: the branch labelling is part of the data of a Hilbert-Polya form — any Phantasm construction must carry a branch tag, since the "natural" untagged form never works. And the negative-integer exceptional first-band parameters are unexamined although the tower divisor says genuine extra order sits at -2, -3, ....
- Where: notes/selberg-letters/astra-proofs.md:162-231; notes/selberg/astra-proofs.md:400-463; notes/reviews/selberg-letters-2026-09-16.md:63-87

### G3-T14-4 The tower determinant, and the missing continuous Ihara-Bass
- Absorbs: L06-059, L07-007, L07-010, L07-011, L07-012, L07-021, L07-022
- Class: PARTIAL
- Raised by: orchestrator, sign-corrected and scoped by prover, reviewed
- What: Laplace-transforming the Guillemin flat trace and expanding 1/(4 sinh^2(x/2)) gives D(sigma) = prod_{j>=1} Z_Sel(sigma+j), a flat dynamical determinant normalised to 1 at +infinity, with Lambda_fl = +D'/D (the drafted minus sign was wrong). D is *not* identified with a Fredholm determinant on L^2, no anisotropic resolvent is constructed, and "trace resonances" are deliberately not identified with Pollicott-Ruelle resonances — the DFG theorem excludes exactly the integer points at issue. There is no continuous Ihara-Bass: nothing constructs a vertex-space determinant or a quadratic operator relation for the flow, and on sampling the adjacency becomes 2 e^{-tau/2} cos(tau sqrt(sigma - 1/4)), a functional calculus of the Laplacian (not of -2 Delta), with aliasing. The orientation convention (opposite directions not identified) is *forced* by ord_0 zeta_R = 2g-2. The Selberg trace formula is deliberately not used as an input.
- Lead: find the continuous analogue of the vertex compression 1 - uA + qu^2 — it would give the continuous "adjacency operator" whose Ramanujan bound is the target; nobody attempted it. And build the anisotropic space so that "resonance" means an eigenvalue of an actual operator, which is the step that would make side B an operator spectrum rather than a divisor. The first-band compression is proved; the literal full-tower compression to a single Laplacian determinant is not.
- Where: notes/selberg/astra-proofs.md:299-398, :483-524; notes/selberg-letters/astra-proofs.md:234-290

### G3-T14-5 The Lindbladian from the sl2 letters, and the perturbed Selberg zeta nobody computed
- Absorbs: L06-049, L07-004, L07-005
- Class: PARTIAL
- Raised by: TJO ("Lindblad from the vector fields on PSL, small operator = Laplacian"), proved by prover
- What: With the two non-compact sl2 generators as jumps, the Heisenberg Lindbladian on multiplication observables is (1/2)(H^2 + E^2), and on the K-invariant sector the constant is exactly 1: it equals -2 Delta, with the first-derivative terms cancelling between the two jumps. Off that sector the identity is (1/2)(H^2+E^2) = 2 Omega + (1/2)W^2 — the compact direction enters the Casimir with a minus sign, so the symbol is indefinite and the Casimir is *not* a Lindbladian globally. Adding the jumps to the geodesic drift gives L_kappa = -X + 2 kappa Omega + (kappa/2) W^2; the jumps alone preserve K-invariants, but with the drift that subspace is no longer invariant and the diffusion does not preserve ker U_- either. "With drift there is a new differential operator whose divisor requires new analysis; neither preservation nor a universal destruction theorem is asserted."
- Lead: compute the divisor of L_kappa for small kappa > 0 — a perturbed Selberg zeta. Concrete, finite-effort, and wholly unexplored; the prover explicitly declined to assert either outcome. Anyone saying "the Riemann Lindbladian is the Casimir" must carry the W^2/2 term.
- Where: notes/selberg/astra-proofs.md:105-257; notes/selberg-letters/astra-proofs.md:309-335

### G3-T14-6 Prime circles: the prime comb with no zeros at all
- Absorbs: L07-001, L07-002, L07-003
- Class: EXPLORED-negative
- Raised by: TJO / orchestrator, corrected by prover
- What: One circle of circumference log p per prime, with rotation flow, has positive-time orbital trace exactly the prime comb; but the generator's spectrum is the union of (2 pi i/log p)Z, which is precisely the *pole* set of the finite Euler product — a product with no zeros anywhere in C. The smeared direct sum is not trace class (the constant modes give one eigenvalue of infinite multiplicity), and the undamped comb is not even tempered, since sum_p log p/(1+log p)^N diverges for every N. The moral: zeros live only past analytic continuation, and a finite prime construction is blind to them; a partial Euler product is not a normal family converging to the continued function in the strip.
- Lead: any candidate mechanism must say *where continuation happens* — this is the criterion the resonances lane used to reject several candidates. If one wanted this route back, the missing step is a non-commuting coupling between the circles.
- Where: notes/selberg/astra-proofs.md:47-101; notes/resonances/astra-freeassoc.md:473

### G3-T15-1 The cusp scattering term is the prime comb (in dips), with the constants pinned
- Absorbs: L07-014, L07-015, L07-019, L07-020
- Class: EXPLORED-registered
- Raised by: TJO / orchestrator, constants corrected by prover, cross-checked by reviewer
- What: With m(r) = -(1/2)(phi'/phi)(1/2+ir) one gets C = -P + A exactly: the prime atoms are *dips* of weight -Lambda(n)/n at t = ±2 log n, and A(t) = 1/2 - 1/(4 sinh(|t|/2)) away from the origin. The +1/2 comes from the Abel boundary distribution of the two Dirichlet series differing from their ordinary boundary value by pi delta_0 — "treating both as convergent series and cancelling their poles would lose it". Multiplying the channel weights by e^{-t/4} = n^{-1/2} turns them into Lambda(n)/n, which is the rate-1/4 damping identity, but the unqualified sentence "the cusp term is the trace of the Riemann channel damped at rate 1/4" needs a subtraction/sign convention and a separately justified channel trace formula. The reviewer confirmed, unclaimed by the file, that the -1/2 multiplier is exactly the trace-formula normalisation, and flagged that the modular continuous term carries a further (K_0/4)h(1/4) contact term with K_0 = phi(1/2) = -1 plus other parabolic terms.
- Lead: this is the only place where the primes of zeta enter the modular geometry, so every candidate mechanism should be measured against whether it uses it. Write out *all* the parabolic terms for PSL(2,Z) before comparing the cusp distribution with any channel trace — the extra contact term sits exactly at the spectral parameter 1/4 that the RH condition names, and nobody followed it up.
- Where: notes/selberg/astra-proofs.md:534-746; notes/reviews/selberg-2026-09-12.md:102-120

### G3-T15-2 The scattering sector: where the Selberg mechanism stops (H-CUSP-BRIDGE, -3/4 versus -1/4)
- Absorbs: L06-061, L06-062, L06-063, L06-067, L07-029
- Class: PARTIAL
- Raised by: orchestrator, results by prover, minor fixes by reviewer
- What: For the modular group the scattering determinant has a pole at s_0 = rho/2 for every nontrivial zero, and the Selberg zeta has a zero there — so RH is equivalent to those zeros lying on Re s = 1/4. But the first-band mechanism fails exactly there: at a scattering pole one must use the leading Laurent coefficient of the Eisenstein series, whose constant term makes it non-L^2, so the Haar-transported form is unavailable. Worse, the rates do not match: for a putative flow state at lambda = s_0 - 1 the rescaling e^{t/2} can never give unitarity in a positive norm because Re(lambda + 1/2) < 0 independently of RH; under RH the correct flow rate would be -3/4, whereas the Riemann functional model's centre is -1/4, and the right reflection is s -> 1/2 - s, not s -> 1 - s. Truncated Maass-Selberg positivity does not rescue it: the leading coefficient is positive throughout 0 < Re s_0 < 1/2, not only at 1/4, and its growth in Y is exactly the missing integrability. The tower bookkeeping also puts the modular scattering band at Re sigma = 1/4 - j, a *different family* from the compact Laplace band — substituting one for the other is an error.
- Lead: the single named gap is H-CUSP-BRIDGE — a specified noncompact flow resolvent realisation, with finite-rank resonant data at s_0 - 1, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a compatible positive modal pairing. What is *not* ruled out: a weighted-space form, since the no-go covers only L^2/C^infinity classes. First literature question: are rho/2 actual resonances of the scalar flow generator, or do they appear only in a related determinant after auxiliary shifts?
- Where: notes/selberg-letters/astra-proofs.md:339-393, :347; notes/resonances/astra-freeassoc.md:119

### G3-T15-3 The Mayer transfer operator as the induced cusp-return operator — the top-ranked route
- Absorbs: L07-032, L07-033, L07-034, L07-035, L07-036, L07-037, L07-061
- Class: LEAD-unpursued
- Raised by: TJO (the Gauss map is in the data list), developed by prover
- What: Mayer's operator (L_s f)(z) = sum_{n>=1} (n+z)^{-2s} f(1/(n+z)) satisfies Z_Sel(s) = det(1 - L_s^2), and its countable alphabet *is* the family of cusp excursions; the primes enter only through the scattering determinant inside the global Selberg object. The sharpest concrete object in the whole group: the exact Hurwitz-zeta tail sum_{n>M}(n+z)^{-2s}f((n+z)^{-1}) = sum_l (f^{(l)}(0)/l!) zeta(2s+l, M+1+z), whose leading singular term at s = 1/2 factors through f(0) and therefore has *rank-one* residue, while the whole tail is not rank one. Explicit Taylor-basis matrix entries are written out and directly implementable in mpmath. Caveat: a zero of det(1-L_s^2) solves lambda_j(s) = ±1, a spectral-parameter-dependent pencil, not the spectrum of one operator — linearising it (a suspension generator) is part of the resonance-to-transfer bridge.
- Lead: the rank-one residue is the only place in the notebook where the Riemann channel's postulated rank-one dissipation |j><j| could be *derived* from arithmetic rather than assumed. The programme: continue the tail exactly, identify the cusp boundary coordinate, Schur-complement it out, and ask whether the remaining complement admits a positive centred pairing computable from its coefficients — that would turn an abstract positive kernel into a boundary-energy identity. Script `mayer_cusp_tail.py` is specified in detail and unwritten. Provenance gap: the Lewis-Zagier / Chang-Mayer period-function correspondence's Eisenstein/resonance part is recorded as memory and unverified; if it is wrong the whole route changes shape.
- Where: notes/resonances/astra-freeassoc.md:139-189, :584-592

### G3-T15-4 Uniform attenuation: coboundaries, the unbounded roof, and isochronous loops
- Absorbs: L07-028, L07-030, L07-031, L07-052
- Class: PARTIAL
- Raised by: orchestrator (seed), mechanism supplied by prover
- What: A genuine width mechanism exists: if a weighted flow has potential V = c + Xf then multiplication by e^f removes the nonconstant part and every periodic orbit loses exactly c times its period (Livsic). The elementary physical counterpart: a loop with return factor r has every mode at Re lambda = log|r|/L whatever the eigenphases — so a single exit is *not* itself an obstruction to uniform widths, which quietly removes the strongest physical objection to the programme. What blocks the transfer to the modular case is named precisely: constant curvature makes expansion uniform per unit geodesic time but does not make *cusp return times* constant, and inducing the flow introduces an unbounded roof and boundary conditions — "precisely where the missing information can reside". An unbounded coboundary would also destroy the bounded similarity.
- Lead: run the falsifiable test — compare total attenuation divided by length for periodic continued-fraction words of one, two and three digits, with lengths 2 log((n+sqrt(n^2+4))/2). One mismatch disproves any proposed coboundary identity, and constant per-branch loss should fail because the roofs differ. Cheap, decisive, never run. For prime circles, impose |r_p| = e^{-w_0 L_p} and compare the resulting determinant's divisor with xi — that check matters more than the easy width check.
- Where: notes/resonances/astra-freeassoc.md:105-137, :392-415

### G3-T15-5 Hecke rigidity acts on the wrong spectral sector
- Absorbs: L07-044, L07-046, L07-047
- Class: EXPLORED-negative
- Raised by: orchestrator (seeds), computed by prover
- What: On Eisenstein series t_p(s) = p^{s-1/2} + p^{1/2-s}, which on the critical line is 2 cos(r log p) — real. At s = rho/2, even under RH, it is p^{-1/4+i gamma/2} + p^{1/4-i gamma/2}, generically complex, so the continued cusp state cannot simply inherit the original self-adjoint Hecke action in a positive Hilbert space. This is "the strongest available arithmetic rigidity, but currently acting on the wrong spectral sector". Related restraint: Poisson-like statistics of arithmetic Laplace spectra and GUE-like statistics of zeta ordinates are different conjectural statements, Hecke commutativity proves neither, and nothing here forbids superradiance.
- Lead: a new boundary representation might have centred local parameters p^{rho-1/2} and their inverses, unimodular under RH — but it must be *constructed* from the cusp data with its positive form, not assigned. Cheap first check: evaluate t_p(rho/2) at the first few verified zeros for two primes. And run the cheapest experiment in the lane: attach one lead to a small Weil-LPS Ramanujan graph, vary the opening, and see whether anything Ramanujan survives — i.e. whether "Ramanujan for a lead" can exist at all.
- Where: notes/resonances/astra-freeassoc.md:297-327, :596-602

### G3-T16-1 Ramanujan = temperedness; the Lie-walk normalisation; Repka's 3/4 and Selberg's 3/16
- Absorbs: L06-026, L06-027, L06-028, L07-006
- Class: EXPLORED-registered
- Raised by: orchestrator, proved and corrected by prover
- What: For tempered pi, Fell absorption gives pi ⊗ conj pi < lambda, so the diffusion spectrum on the K-invariant sector is contained in [1/2, infinity): the gap 1/2 *is* the tempered threshold, the continuous Ramanujan value — and for PSL_2(R) the prover proved the converse, so the type-zero bound is *equivalent* to temperedness, sharply attained on every discrete series. Normalisation matters: the equally averaged Lie walk has threshold 1/(2d) = 1/4, not 1/2, and the exact rate on a constituent is 2s(1-s) + m^2/2 — note the uncorrected 1/4 is numerically the Riemann rate, a coincidence not to be fooled by. Repka's theorem (tensor square of the complementary series contains a complementary constituent iff s > 3/4) explains the 3/16 coincidence: the complementary constituent's slow geodesic exponent is -2(1-s), and the boundary 2(1-s) = 1/2 is exactly s = 3/4, whose Laplace value is 3/16 — an explanation of the parameter coincidence, not a proof of Selberg's automorphic theorem. Separately, the spectral gap of the two-jump quantum Lindbladian is governed by how pi ⊗ conj pi decomposes, and the prover deliberately deflates it: parameters can accumulate at zero, so no gap follows from writing a tensor-product Casimir.
- Lead: supply the direct-integral and domain theory for pi ⊗ conj pi and ask what its K-types do; tying a gap there to the 1/4 property would be a representation-theoretic route to the continuous Ramanujan statement. Nobody tried. Whether the geodesic-exponent boundary can be pushed toward the automorphic 3/16 is untouched.
- Where: notes/ramanujan-graded/astra-proofs.md:811-1024, :911-928; notes/selberg/astra-proofs.md:255

### G3-T16-2 The reflection grading on PGL_2(R), the K-type grading, and the Gamma-factor ladder
- Absorbs: L06-030, L06-031, L06-032, L06-033, L06-064, L06-065
- Class: PARTIAL
- Raised by: orchestrator, corrected by prover
- What: Inducing a discrete series from PSL_2 to PGL_2 with P = I + (-I) and a reflection jump puts the critical continuum in the *even* sector and an archimedean ladder of discrete series in the *odd* sector — the opposite of the Riemann assignment. The odd ladder's lowest exponents match the pole lists of Gamma((z+1)/2) and Gamma((z+2)/2), whose product has the pole list of Gamma(z+1) — but this is a statement about *lists of lowest exponents* only; neither determinant is proved to be a Gamma function, and the zero rung, multiplicities, descendants and quadratic rates are unaccounted. Two candidate gradings were compared and one died: the K-type grading makes the geodesic generator X *odd*, so it is not a grading for the flow at all, full K-parity is not Hodge degree, and the hoped "supercancellation" is false (the theta factor is strictly positive, 0.7300003 at t = 1). What survives is that K-parity genuinely grades the *diffusion* letters. A by-product: on selected Hodge bundles the diffusion heat supertrace is not the Euler characteristic but carries a remainder 2(1 - e^{-2t}) Tr e^{-2t Delta_0}.
- Lead: prove or disprove that the odd flow determinant of this construction *is* a Gamma factor — that would supply the archimedean factor of the Phantasm from representation theory. And the K-parity diffusion representation channel, with its own doubled parity and spectral analysis, has never been analysed. The McKean-Singer remainder is an explicit computable non-topological defect that *is* the Laplace spectral data; nobody asked what its zeta is.
- Where: notes/ramanujan-graded/astra-proofs.md:1026-1244, :1167-1186; notes/selberg-letters/astra-proofs.md:498-544

### G3-T16-3 The archimedean completion: one pole versus two
- Absorbs: L05-018, L05-042, L05-082, L07-057
- Class: LEAD-unpursued
- Raised by: prover (one paragraph each), orchestrator (the unbuilt ladder)
- What: A single simple pole at u = 1/q is *incompatible* with the uncompleted self-reciprocal curve-type functional equation for q > 1, because reflection also demands a pole at u = 1 — and the same bookkeeping applies to generator poles at 0 and kappa. Riemann's zeta has one pole; a self-reciprocal FE demands two; that mismatch is exactly what the completion absorbs, so the archimedean factor is not optional. The same point appears from the other side: sigma_{1-s}(n)/zeta(s) also has a pole at s = -2, so "poles exactly the nontrivial zeros" is globally false without a completion, and removing the trivial-zero poles requires one. Yet the Gamma-factor oscillator ladder of the yolo guess was *never specified* — no jump operators, rates, grading, domains or trace prescription — and an oscillator heat trace and a Lindblad transfer trace are different objects; any trace-preserving archimedean-only addition also leaves the phase marginal unchanged. (Conformal/thermal quasinormal ladders are a suggestive analogy for the archimedean part only; they do not explain why the irregular arithmetic set occupies one row.)
- Lead: build the truncated-oscillator version specified in the yolo brief — it is the one piece of the guess never tested and the only piece that could supply the missing archimedean structure. Then run the one specific divisor comparison: divide the gamma and rational factors of the scattering determinant out of a thermal/CFT two-point function and see whether anything survives in the zeta part.
- Where: notes/zeta-conditions/astra-constructions.md:371; notes/yolo-lindblad/astra-structure.md:41-43, :471; notes/resonances/astra-freeassoc.md:518-536

### G3-T17-1 Odd letters must be jumps — and the even-Hamiltonian escape
- Absorbs: L06-019, L06-020, L06-021, L06-022
- Class: PARTIAL
- Raised by: orchestrator, corrected by prover
- What: An odd letter cannot be O(1)-close to the identity (P A P = -A forces ||A - I|| >= 1), so it enters a continuum limit as sqrt(h) R with R an odd jump of finite rate, never as a drift: parity-changing dynamics is *dissipative*, "fermionic zeros are relaxation modes and there is no Hamiltonian odd letter" (on a fixed finite bond, with the collective bound sum_odd ||A_a(h)||_HS^2 = O(h), not a per-letter limit). For a jump Lindbladian the sector Hastings band becomes an affine *interval* of diffusion rates — "not an assertion that they all have the same real part" — so a Poissonised jump Lindbladian is exactly the wrong shape for a critical line. Sampling is also treacherous: exact sampling pushes forward signed multiplicities and can cancel aliases, with an explicit CP example where the entire sampled divisor vanishes at h = 1 while the continuous odd rates violate the critical bound.
- Lead: the prover's one-sentence aside reopens what this appeared to close — under parity covariance there is no parity-changing Hamiltonian term, but an *even* Hamiltonian can give odd coherences arbitrary oscillation frequencies, and a net zeta need not detect every relaxation mode. That is a concrete design principle for a Riemann Lindbladian: imaginary parts from an even Hamiltonian on the coherences, real part 1/2 from the odd jump rates. Never followed.
- Where: notes/ramanujan-graded/astra-proofs.md:553-702, :645-650, :491-551

### G3-T17-2 The divisor of an infinite bond: resonances of regular data
- Absorbs: L06-023, L06-024, L06-025
- Class: PARTIAL
- Raised by: orchestrator, made precise by prover
- What: For an infinite graded bond the divisor must not be the L^2 spectrum but must come from correlation functions of regular data: fix a graded Banach realisation, assume analytic Fredholm continuation of the resolvent, and set multiplicities from the rank of the Riesz projection restricted to each parity sector (scalar pole *order* is not multiplicity). The motivation is the 2026-09-14 negative that no statement on the model space can see the rate 1/4. Two gaps are flagged and not closed: invariance of the divisor under a change of regular realisation "needs a further compatibility theorem; calling both spaces regular supplies no such theorem"; and for continuous spectrum there is no canonical scalar signed measure for a non-normal generator — one must specify positive traces on the sector spectral algebras to avoid infinity minus infinity.
- Lead: prove the compatibility theorem, or accept that the divisor is data-dependent — without it the Phantasm's divisor is not an invariant of the semigroup, which would undermine any RH statement made about it. Supply the sector traces for the Riemann and Selberg cases, or use sector supports instead of an invented scalar continuous divisor.
- Where: notes/ramanujan-graded/astra-proofs.md:704-809, :766-795

### G3-T17-3 Continuum realisability: Poissonisation, singular transfers, and the half-entropy no-go
- Absorbs: L05-062, L05-063, L05-078, L05-079, L05-080
- Class: EXPLORED-registered
- Raised by: orchestrator, built and scoped by prover
- What: Poissonisation is a universal but lossy bridge from lattice to continuum (it always exists, changes the FE/RH and may fail kinetic regularity). An exact cMPS embedding needs E = exp(hT) with Choi conditional positivity: a matrix logarithm is not enough, and a *singular* E has no exponential at positive time — a small sharp obstruction. Kinetic regularity requires R_a R_b = (-1)^{p_a p_b} R_b R_a, so a fermionic species has R_a^2 = 0. The half-entropy cMPS (even {2,1,1,1}, N(L) = e^{2L} - e^L) realises the requested ratio but is not a Lindblad gauge on the full bond, and there is an exact 1|1 no-go: on homogeneous regular 1|1 data, a normalised generator with a unique fixed point has even rates {0,-gamma} and odd {-gamma/2 ± i omega} and cannot produce the half-difference. The FE cMPS works: one regular lowering fermion at rate two with a Hamiltonian energy difference gives even {2,0}, odd {1±i}, N(L) = |1 - e^{(1+i)L}|^2 >= 0 and Zcal(2-z) = Zcal(z) — the generator shifted by half the reflection constant is skew-adjoint on the odd sector, which is the S7 mechanism realised concretely. Caution: without an FE to fix the centre, "half the rate" is convention-dependent and a growth shift moves it.
- Lead: the 1|1 no-go is deliberately scoped — ask whether the half-difference becomes possible on C^{1|2} or larger, which connects directly to "genus >= 2 needs fermionic species". And the FE cMPS's honest caveat is the lead: its ring vector has only its vacuum amplitude, so the mechanism works but the state is trivial; making it nontrivial is the next step.
- Where: notes/zeta-conditions/astra-constructions.md:124-138, :319-348, :156-160

### G3-T18-1 FE, RH and mixing are independent; positivity plus FE does not force RH
- Absorbs: L05-058, L05-059, L05-077
- Class: EXPLORED-registered
- Raised by: orchestrator (the question), decided by prover
- What: Eight homogeneous Kraus families on a 1|1 bond, all TP, realise every combination: FE+RH+mixing, FE+mixing without RH, RH+mixing without FE, and mixing alone — with physical letters (scaled identity and Paulis with positive coefficients), all Möbius exponents nonnegative integers, proved by embedding disjoint full shifts. Tensoring with an idle all-even qubit destroys uniqueness while moving no divisor point. An explicit CPTP tensor with poles {1,1/16} and odd eigenvalues {8,2} has FE and a unique stationary state while RH fails, with a printed negative Weil minor. The one impossibility: in the exact projective curve normal form with real coefficients, RH already makes the odd multiset reciprocal and {1,q} supplies the even pair, so "no FE, yes RH, yes projective pole condition" cannot occur. "Unique fixed point" is itself three distinct conditions — a simple uncancelled Perron eigenvalue, a channel on the specified bond (a singular Perron matrix gives only a restriction), and stationarity/mixing (uniqueness alone permits periodicity, with a bit-flip witness).
- Lead: RH is not going to fall out of FE plus a unique fixed point; that closes a whole class of hoped-for shortcuts. Whenever the notebook says "unique fixed point", say which of the three is meant.
- Where: notes/zeta-conditions/astra-constructions.md:90-102, :302-317

### G3-T18-2 The target specifications: TJO's wish lists and the checklist for a "tiny Riemann"
- Absorbs: L04-001, L05-051, L05-084
- Class: LEAD-unpursued
- Raised by: TJO, answered by prover
- What: For varieties, TJO's five-item scorecard: a natural MPS tensor determined by the variety data; a prescription for which bond modes are bosonic and which fermionic, and why; a theorem that ring norms give the correct counts; an identification of the Polya-Hilbert operator; and the Ramanujan property for the MPS. Items (2) and (3) are done, (4) is answered as a unitary not a Hamiltonian, (1) and (5) are open — a tensor exists, but nothing makes RH fall out of the tensor rather than being inserted through the eigenvalues. For zeta, the "factor by factor" method produced a precise sufficient checklist: a convergent positive integer prime Euler product with infinitely many prime species; a specified meromorphic continuation and completion with the intended pole divisor; reciprocal or additive symmetry of the retained modes; and either the critical-line condition itself *or* Weil positive definiteness plus that symmetry.
- Lead: item (4) of the tiny-Riemann checklist — Weil positivity plus symmetry — is the only route in the list that does not presuppose knowing where the zeros are, and it pairs exactly with the unused continuous-time Weil kernel criterion. Prioritise it. For varieties, the target is a tensor written from the *equation* of the curve with RH read off from complete positivity.
- Where: notes/ring-norm-tensor/astra-brief.md:5; notes/zeta-conditions/astra-brief.md:15-18; notes/zeta-conditions/astra-constructions.md:369

### G3-T19-1 TJO's framing and the five genuine mechanisms
- Absorbs: L07-024, L07-065
- Class: PARTIAL
- Raised by: TJO, closing assessment by prover
- What: "RH is a Ramanujan property, i.e. the existence of an EXTREMAL object, a 'Riemann quantum expander': a mixing transfer operator whose ring norms are exactly the prime measure, which has a duality, and which is manifestly self-adjoint on some bond space; then Weil positivity puts all modes on the circle." The obstruction named in the same breath: the zeros are *resonances* of the modular surface, not eigenvalues, and the Riemann channel turns them into eigenvalues at the price of Hermiticity. TJO's rule: no general construction will work, use the data we have — primes, the one cusp, the scattering phase, Hecke operators, Weil-LPS channels, Bost-Connes, the Gauss map, the explicit formula. The lane's verdict: there are five genuine mechanisms in the notebook — uniform attenuation per travel time, an attenuation coboundary, arithmetic tempering in a constructed representation, a positive canonical energy from local data, and the interlacing structure of certain matrix ensembles — and *none* is yet identified with the Riemann cusp sector.
- Lead: "the next useful result would be an explicit arithmetic identity for the cusp transfer or its boundary pairing — even an obstruction showing that a proposed pairing cannot work — rather than one more general dilation of a function we already know." Apply the operative test to every candidate: which of our data does it use?
- Where: notes/resonances/astra-brief.md:5-7; notes/resonances/astra-freeassoc.md:646

### G3-T19-2 One-exit inverse design: the missing arithmetic law for the residues
- Absorbs: L07-025, L07-027, L07-062
- Class: PARTIAL
- Raised by: orchestrator (seed), developed and corrected by prover
- What: With H_eff = H - (i/2)vv^* the secular equation is 1 + (i/2) sum_k |v_k|^2/(z - E_k) = 0, and eigenvalues are *not* obtained by subtracting widths once resonances overlap. Conversely, Hermite-Biehler interlacing turns any finite set of equal-width poles into real energies E_k and positive residues |v_k|^2 = 2V(E_k)/U'(E_k), with the mode geometry a Cauchy Gram matrix. Two consequences: "GUE positions plus equal widths" is *not* the fingerprint of scalar loss, since any finite equal-width non-lattice pole set has a one-port realisation; and scalar loss means B + B^* = -2w_0 I, which cannot be rank one above dimension one, so eigenvalue equality is much weaker than that operator identity.
- Lead: the special information lies in the *couplings*, not the width pattern — "the new content would be an arithmetic formula for the spectral weights |v_k|^2 that forces the secular roots to have the same imaginary part". That is the concrete missing identity, and it is the same one item (6) of the rewritings list points at. The proposed script sweeps opening strength, perturbs residues at fixed energies, and forms exit Gram matrices at increasing height; it was only partially run in memory.
- Where: notes/resonances/astra-freeassoc.md:45-103, :594-602

### G3-T19-3 Canonical systems, Krein strings, and Suzuki's prime-defined kernel
- Absorbs: L07-038, L07-039, L07-040, L07-041, L07-043, L07-063
- Class: LEAD-unpursued
- Raised by: orchestrator (TJO's "positive-mass prime string"), developed by prover against the local TeX
- What: A canonical system JY' = z H Y with H >= 0 gives a self-adjoint boundary problem and a Herglotz Weyl function. Suzuki's intermediate object is concrete and *purely arithmetic*: with an explicit Psi built from the prime sum sum_{n<=e^t} Lambda(n)n^{-1/2}(t - log n) plus elementary terms, the kernel G(t,u) = Psi(t) + Psi(u) - Psi(t-u) is globally nonnegative definite iff RH. A 16x16 calibration at 40 digits gives eigenvalues 0.0223 to 0.8174 from the prime-defined matrix against 0.0217 to 0.8065 from 3000 zero ordinates. Two disciplines: positive *local* energy does not make the monodromy elliptic (explicit two-slab counterexample with transfer diag(-16,-1/16)) — the relevant positivity belongs to the spectral operator or its boundary response; and a passive realisation of the already-inner scattering function is unconditional and cannot prove anything, whereas a positive realisation of the *centred* response is equivalent to RH.
- Lead: the one proposed experiment that could *discover* structure rather than confirm RH — factor the prime-defined kernel (Cholesky/Schur) and inspect how the factors change as the interval crosses log p^k, looking for an arithmetic recurrence. Script `prime_screw_kernel.py` is fully specified and unwritten. Also unfollowed: "integrating twice and using Suzuki's kernel is a cleaner way to implement width removal on compact test supports". Warning: off RH the gammas in the source can be complex, so substituting imaginary parts of zeros assumes the conclusion.
- Where: notes/resonances/astra-freeassoc.md:191-240, :604-633

### G3-T19-4 Wigner time delay and the removal of the common width
- Absorbs: L07-042
- Class: PARTIAL
- Raised by: orchestrator (seed), corrected by prover
- What: The delay q_S(x) = -d/dx arg S(x) = 4 Re (xi'/xi)(1+2ix) receives 2w/((x-a)^2+w^2) from each pole; the completion matters, since S carries an extra Blaschke factor and q_S = q_phi + 1/(x^2+1/4), so positivity of the completed model delay is not an unconditional statement about physical cusp delay. Under RH the delay is a Poisson smoothing of a density of states at depth 1/4, and removing the common width is multiplication by e^{|t|/4} in Fourier variables — exponentially ill-conditioned and needing a specified regularisation at the origin. Classified a rewriting unless the removal's positivity has a prime-side cause.
- Lead: TJO's seed question is still unanswered and is the right one: "is there a physical quantity that is sensitive to the equality of widths and computable from the primes?" Concrete test: perturb an equal-width pole pair to 1/4 ± epsilon keeping the FE pairing, and search for a negative direction only *after* common-width removal.
- Where: notes/resonances/astra-freeassoc.md:242-295

### G3-T19-5 The rewritings, and the analogies that do not transfer
- Absorbs: L07-051, L07-054, L07-055, L07-056, L07-060, L07-064
- Class: EXPLORED-negative
- Raised by: prover (self-assessment)
- What: Eight statements restate RH without causing it — a centred Hermitian zero operator; a positive centred canonical system; the width-removed delay as a positive density of states; unbroken PT symmetry; the cusp Ruelle band being an exact line; inverse scattering reconstructing equal-width poles; the continued Euler product as a density-of-states determinant; and xi as a real-rooted expected characteristic polynomial / the de Bruijn-Newman threshold. Each item names the extra ingredient that would promote it. Four specific analogies are refuted or deflated: the local Euler factor R_p is *not* inner (it has poles on Im tau = -1/2; only the Blaschke factor b_p is inner, |R_2| = 54.2 against |b_2| = 0.0093 at y = 0.49); the Thouless formula needs an actual self-adjoint chain, an integrated density of states and a controlled limit, none of which come from relabelling the Euler product; complex scaling in the cusp is a complex *translation* in r = log y, not exterior rotation, and in any case "exposes existing poles and does not move them onto a new line"; and depolarising detailed balance gives equal rates easily but on the wrong spectrum (the density-operator lift has real parts -1/2 and difference frequencies). For the real-rootedness route, "it is emphatically not enough that every matrix in an ensemble be Hermitian" — H = ±I_2 has average characteristic polynomial x^2+1.
- Lead: item (6)'s useful output is the constraint on residues, which would still have to be derived arithmetically — the same missing identity as the one-exit design. For the MSS route, reproduce the counterexample and a genuine small example, then ask whether any *finite prime construction* gives the MSS algebraic form with the right trace coefficients and a controlled limit.
- Where: notes/resonances/astra-freeassoc.md:369-390, :452-516, :558-578, :635-644

### G3-T20-1 Prove supplied hypotheses instead of citing them
- Absorbs: L03-032, L03-061, L04-056, L05-016
- Class: EXPLORED-registered
- Raised by: prover (as a working method), endorsed by reviewer
- What: Four hypotheses supplied in the riemann-cmps brief turned out to be provable in-file (the M/M/1 spectrum in half a page, a Stickelberger-type statement, the Weil character-modulus formula, a Gauss-sum fact) — and in two cases the byte-verified quote that would have supported them *does not exist in the repository's sources*, so proving them removed the provenance problem entirely. The same happened for the Hilbert-Schmidt eigenvalue bound after exhaustive arXiv searching found no quotable statement: it follows from Schur triangularisation in one line. A companion tool: an explicit Euler-Maclaurin/Bernoulli continuation of zeta, written out so that continuation steps never smuggle in zero data.
- Lead: adopt this as policy — when a byte-verified quote is missing, try proving the statement before weakening the claim that depends on it. Audit the remaining H-* inventory the same way.
- Where: notes/riemann-cmps/astra-proofs.md:638-662, :798-931; notes/ring-norm-tensor/sources.md:557-577; notes/yolo-lindblad/astra-structure.md:456-465

### G3-T20-2 Dependency rot: in this book the printed status is derived from the deps
- Absorbs: L03-052, L04-052, L04-053
- Class: EXPLORED-registered
- Raised by: Opus reviewer
- What: Two claims were recorded `proved` while resting on `sketched` inputs, and one had `deps = -` although its Riemann specialisation needs the Lax-Phillips hypothesis — which had *disappeared* from the dependency chain of the channel branch. Prescription: re-add the missing deps so the gate demotes the status automatically. Two hypothesis splits were also prescribed and applied: H-TWIST into its unconditional algebraic half (a two-line Kronecker identity) and its sketched physical half, which makes the genus-two theorems unconditional matrix theorems; and H-DEG into a lattice-geometry half and an arithmetic half (deg Frob = q), without which the elliptic PH theorem looks circular because the quoted hypothesis literally ends with RH for elliptic curves.
- Lead: add a gate check that flags any `proved` row whose text mentions "zeros" but whose deps contain no zeta input. Two strengthenings remain available: the H-TWIST algebraic identity is unconditional *including odd letters* (the shards' hedge to all-even letters is conservative and can be dropped), and one polish line would make the non-circularity of the elliptic theorem self-evident.
- Where: notes/reviews/riemann-cmps-2026-09-12.md:741-758; notes/reviews/ring-norm-tensor-2026-09-14.md:73-124, :767-782

### G3-T20-3 Provenance: what is named but not quoted
- Absorbs: L03-060, L04-054, L04-055, L04-057, L04-058, L06-029, L07-017, L07-018
- Class: EXPLORED-registered
- Raised by: sources lanes and Opus reviewers
- What: A standing list of citations that are assumed rather than byte-verified: the type III_1 clause (the local source labels only the *critical* temperature, i.e. beta = 1, not the whole range — fixed in round 2); the CM eigenspace decomposition used under the Rosati theorem, not quotable from arXiv (Shimura-Taniyama / Lang); Waterhouse's stratification, which the quotable source indexes by j-invariants rather than F_q-isomorphism classes and which is a torsor with no canonical base point; Deuring's lifting theorem, the general manifold Lefschetz theorem and the general Hodge L^2 inner product, all named-not-quoted; Repka 1978, explicitly not inspected in session (cross-checked only against a second paper); and, in the Selberg lane, H-SZ's entireness, spectral divisor and trivial divisor, plus H-LAP, with "no quote at all", and H-GUI which swallows both the nondegeneracy and wave-front conditions and needs a measure-valued reading. A standing warning: one very recent unrefereed preprint with typographic errors in its front matter is used only for attribution and must never be the authority for a proof.
- Lead: mark each `assumed (named-not-quoted)` before promoting the dependent theorems past conditional; the mitigating consistency checks (e.g. via ord_0 of the Ruelle zeta) show the statements are right, merely unsourced.
- Where: notes/ring-norm-tensor/sources.md:148-488, :627-658; notes/reviews/selberg-2026-09-12.md:26-80

### G3-T20-4 Process and numerics discipline
- Absorbs: L03-056, L03-057, L03-059, L04-059, L06-068, L07-023
- Class: EXPLORED-registered
- Raised by: Opus reviewers
- What: A pile of small, mostly unapplied fixes. The quantum-Ihara note never defines its norm, and the Neumann step needs submultiplicativity (rescale any norm by 1/10 and take X = 1); its `exact_check` evaluates only one form of the identity and draws from the same RNG stream as the float checks, so the "exact" instances are not reproducible independently of execution order; one cited proof (a NeurIPS supplement) is not in the local refs, and it is the closest prior art to the new theorem. In the ring-norm lane, hypothesis ranges and a radical-operator justification were off by one or terse, and the displayed certificate constants use a looser bound than the run. Six ledger rows in the Selberg lane report the draft's *questions* as errors found, which matters because the lab book reads the ledger as a list of errors. Both Selberg-side briefs asked for scratch scripts and both prover files used inline non-writing Python, leaving the directories empty — the reviewer re-derived every number independently and they are exact, so this is a process defect only.
- Lead: require scratch files, seed exact checks separately, and distinguish "drafted" from "asked" in prover ledgers.
- Where: notes/reviews/round2-2026-09-12.md:245-255; notes/reviews/ring-norm-tensor-2026-09-14.md:126-210; notes/reviews/selberg-letters-2026-09-16.md:124-145

## Top leads in this group

1. **G3-T15-3** — the Mayer cusp tail's leading singular term at s = 1/2 has *rank-one* residue: the only place where the Riemann channel's postulated rank-one dissipation could be derived from arithmetic rather than assumed. One paragraph, never pursued.
2. **G3-T19-3** — factor Suzuki's purely prime-defined kernel and look for an arithmetic recurrence in the Schur/Cholesky factors as the interval crosses log p^k: the only proposed experiment whose input contains no zeros and which could discover structure. Script specified, unwritten.
3. **G3-T8-3** — compute Gram condition numbers of the zero eigenvectors at 3000/10000/30000 ordinates and fit the growth. Cheap, decisive either way for the Riesz-basis metric route, flagged in two separate campaigns, never run.
4. **G3-T13-2** — the exterior occupation parity gives 1/zeta as an absolutely convergent signed trace with no boundary-functional games. A single paragraph saying the arithmetic wants a *different* grading from the one the programme uses.
5. **G3-T9-2** — the continuous-time Weil kernel criterion (positive definiteness of (nu(t_j - t_k)) for a generator). Stated once, never used, and named elsewhere as the only route that does not presuppose where the zeros are.
6. **G3-T17-1** — an *even* Hamiltonian can give odd coherences arbitrary frequencies. A prover aside that reopens the route "odd letters must be jumps" appeared to close, and hands a design principle: imaginary parts from an even Hamiltonian on the coherences, real part from odd jump rates.
7. **G3-T14-5** — compute the divisor of the drift-plus-diffusion generator L_kappa for small kappa: a perturbed Selberg zeta, finite effort, and the prover explicitly declined to assert either preservation or destruction.
8. **G3-T1-3** — settle the "density at most 1/2" question about conjugation-symmetric infinite flip sets. One sentence in a review, but it is the entire remaining content of infinite parity rigidity.
9. **G3-T4-4** — solve the CM-diagonal genus-two ansatz symbolically: the only shape called "most promising for a closed form", solved numerically, then untouched; its unknowns reduce to a 3x3 Gram matrix.
10. **G3-T11-3** — run the cover-zeta test: a graded bond with supertrace 2P_+ carries only the zeta zeros, a Galois-symmetric one carries all Dirichlet L-zeros, and they have different supertraces. Cheap and decisive on any future Galois proposal.
11. **G3-T3-2** — the parity-dimension obstruction n_0 - n_1 = (D_+ - D_-)^2 >= 0. A one-paragraph count that may be the actual reason no CP realisation of the Artin-Schreier or Riemann transfers has ever been found; check it before attempting one.
12. **G3-T16-2** — prove or disprove that the odd flow determinant of the PGL_2 reflection grading *is* a Gamma factor. Currently only the lists of lowest exponents match; success would supply the Phantasm's archimedean factor from representation theory.
13. **G3-T14-2** — prove the global leafwise closed-range cohomology behind df = (U_+ f) eta_+, turning the Selberg determinant ratio from a divisor identity into an actual cohomological cancellation — the natural home for "zeros are fermionic".
14. **G3-T6-1** — find the *zeta-side* permutation whose signature produces the minus sign, as the Frobenius permutation sign does for Artin-Schreier curves. The most TJO-shaped statement in the group ("permutations before curves") and nobody looked.
15. **G3-T15-4** — run the periodic continued-fraction attenuation test: one mismatch disproves any proposed cusp coboundary identity. Two sentences, cheap, never run; and it is paired with the quietly important fact that a single exit is *not* an obstruction to uniform widths.

Briefly-mentioned items among the above: 1, 2, 4, 5, 6, 7, 11, 13, 15 (nine of fifteen). Runners-up of the same kind, all one-paragraph asides: the invisible zero eigenvalues and nilpotent blocks that every trace criterion leaves open (G3-T2-3); the conserved commutative family {V_n} of the forward prime dynamics (G3-T12-5); the extra (K_0/4)h(1/4) contact term sitting exactly at spectral parameter 1/4 (G3-T15-1); the coincidence that the genus-two field threshold is exactly the Weil *lower* bound (G3-T4-3); the McKean-Singer defect 2(1-e^{-2t})Tr e^{-2t Delta_0} that *is* the Laplace spectral data (G3-T16-2); the negative-integer exceptional first-band parameters where the tower divisor says extra order lives (G3-T14-3); nilpotent transients as free parameters invisible to every counting constraint (G3-T2-4); and the (5;13) reduced graded L-function f_4 f_{-4}/(f_14 f_{-14}) never identified arithmetically (G3-T4-6).

## Dead routes (consolidated)

Drafted statements shown false, with the correction, and routes explicitly closed.

- The drafted Artin-Schreier sign law S_n(g) = -(-eta(-1))^n conj(Tr E_g^n). False; the truth is (-1)^{n-1} delta_n Tr E_g^n with delta_n the shift determinant on the radical. Valid iff P(-eta(-1)) != 0. (G3-T6-1)
- The notebook claim alpha_i = -lambda_i(E_g). False in general; exact criterion P(-1) != 0. (G3-T6-1)
- The drafted universal super-transfer block in the odd sector. Disproved by exact point counts (N_1 = 10 against -2). (G3-T6-3)
- "The trivial character sector carries exactly the two poles." The point at infinity is not a character sector; the poles split. (G3-T6-3)
- Assuming a self-dual normal basis in the sign law: it does not exist for even n, which is the whole point. Only the existence of a normal basis is used. (G3-T6-1)
- "Phase" as a characterisation of a Weil implementer: only *centred*, exactly phase-free covariance determines it. (G3-T6-2)
- The root-of-unity phase of the Artin-Schreier transfer does *not* follow from "the entries are roots of unity" (there are zero entries and a q^{-1/2}). (G3-T6-2)
- The J = 0 transfer convention: the minimal transfer is the scalar Gauss sum; the module's q-state register adds spurious zero eigenvalues. (G3-T6-2)
- The cut-rank bound "at most D" for a ring: it is D^2, and sharp. The growing table 2,4,8,16,8,4,2 is basis noise; in a self-dual normal basis the quadratic amplitude has cut rank <= D^2 for every n. (G3-T6-4)
- "Fixed finite lattice tensors give only supersingular zetas." False, refuted by the campaign's own ordinary elliptic and genus-two tensors. (G3-T2-5)
- The rebound/renewal fixed point solved by Omega: the integral equals T·Omega and diverges, and is not even type-correct in the original space. (G3-T10-2)
- The rank-one Lindblad formula in infinite dimension: no bounded exit vector exists; replaced by the absorbing-vacuum construction. (G3-T10-1)
- The vacuum-decay channel as a realisation of the forced datum: it gives each zero *twice* plus an even pair-sum sector. (G3-T10-1)
- |Tr Z(t)|^2 as a form factor / route to pair correlation: not a distribution; the pair list violates the growth condition. (G3-T10-1)
- A cMPS with the vacuum-decay bond as a source of entanglement: the stationary bond is pure and every ring amplitude with a jump vanishes. (G3-T10-2)
- Landau's theorem applied to force infinite parity rigidity: toothless, the abscissa is already 1 from the pole. (G3-T1-3)
- The single-cosine oscillation argument; pairing a distribution on (0,infinity) directly with t^k e^{-st}; the imaginary-part-only integration by parts. All replaced by the common-cutoff construction and full complex bookkeeping. (G3-T1-2, G3-T1-3)
- The prime chain as a home for the zeros: its spectrum is real, classically in general and for the full generator on the weighted space. (G3-T11-2)
- "The Bost-Connes transition is ergodicity breaking" as a statement about a Riemann Lindbladian: not established; what is proved is loss of normalisability. (G3-T11-2)
- The notebook §5 prime weights +Lambda(n)n^{-1/2} with the damping applied twice: out by -2 and double-counted. (G3-T1-4)
- Any ordinary ungraded fixed-finite-bond MPS as a source of positive-genus curve counts: excluded. (G3-T2-2)
- The drafted bosonic bound sum_odd |mu|^2 <= 2 Tr(E_++)Tr(E_--): false, one-species counterexample a = B = diag(1,-1). (G3-T2-4)
- The drafted genus-two ansatz a_1 = 1, B_1 = 0, a_2 = 0: forces M = 0 and a negation-symmetric odd spectrum; impossible for any ordinary curve with nonzero trace. (G3-T4-3)
- A vacuum species with a *single* fermionic species (numerically, not proved); the CM-diagonal ansatz with one odd species; purely bosonic C^{1|2} with 3 or 4 even species. (G3-T4-3, G3-T2-4)
- 0 + I_2 as the q-eigenvector, or an invariant vacuum line, on the minimal genus-two bond: either would let the odd species be deleted. (G3-T4-3)
- "Only transcendental tensor entries work": refuted by real-closed-field transfer. (G3-T4-4)
- Small least-squares residuals and four-decimal matrices as certificates; a naive eigenvalue threshold reading a 3x3 nilpotent block as five nonzero eigenvalues. (G3-T4-3)
- Equality in the genus-one case giving matrix proportionality or normality: only word-trace vectors are proportional; nilpotent transients are invisible. (G3-T2-4)
- The minimum bond for genus g being C^{1|g}: the condition is mk >= g, and at g = 4 the 2|2 bond wins. (G3-T2-4)
- "The permutation k -> M^T k of Z^2": not a permutation, injective of index q. (G3-T7-1)
- The digit map onto O/(pi^n - 1): need not be onto; and the failure of the carry automaton is *not* unbounded carries. (G3-T7-2)
- Integral ideal classes as complex MPS gauge orbits: complex tensors forget the ideal class. (G3-T4-4)
- Bra/ket conjugation as the functional equation: conj(rho) = 1 - rho only on the critical line, so it would put RH into the interpretation. (G3-T10-3)
- Doubling the cohomology twice (using full cohomology as the ket and then taking a norm). (G3-T4-1)
- The phase-side Lindbladian at rates 1/p: no densely defined no-jump operator and no trace-norm limit at any positive time. (G3-T12-2)
- The doubled-bond grading "even = span{e_0}": not preserved by the prime jumps; explicit odd cross terms for every prime. (G3-T12-1)
- "The prime jump *is* the Galois (Shor) map" unqualified; and Gauss-vector coherences as scalar Lindblad modes (extra 1/p, large orthogonal residual). (G3-T12-1, G3-T12-4)
- c_b(1) = mu(b) as a vacuum-to-shell jump overlap: all overlaps are nonnegative and put zeta in the numerator; evaluation at 1 is unbounded. (G3-T12-5)
- Commuting jumps restoring the Euler product: word/Poisson multiplicities survive, and parity insertion does not remove them. (G3-T13-1)
- The guessed vacuum generating functions having a pole at s = 1 or at the zeros: analytic pole exclusion uniform in the cutoff, with the shift beta+1 irremovable. (G3-T12-3)
- A shrinking F/(1/zeta_P) ratio as evidence of a hidden reciprocal-zeta factor: a partial Euler product outside its half-plane. (G3-T12-3)
- Parity closure implementing the quotient by Q^x; Tr[Gamma_b e^{tL_F}] as an ordinary trace; a finite prime cutoff as a finite bond cutoff. (G3-T12-2)
- Forward phase dynamics selecting Haar: they converge weak-* to delta_0, whose phase restriction is not Haar. (G3-T11-5)
- "Haar is the pure vector state of e_0 on C(Zhat)": Haar is mixed on the commutative phase algebra. (G3-T11-5)
- Shell-diagonal Gibbs weights as stationary, with the drafted reverse rate u/p: the correct rate is u p^beta, and the quantum generator still creates coherences. (G3-T11-4)
- The forward phase prime having the real spectrum of the reversible occupation chain: it has the full disk. (G3-T11-4)
- A Levy-style small-jump completion of the Bost-Connes measure at criticality: the divergence is at *large* jumps. (G3-T11-5)
- "Character-diagonal unitary jumps cannot produce frequencies": false without an inversion-symmetry assumption. (G3-T12-4)
- "All primes fermionic, zeros on Re s = 0": true of the finite factors only. (G3-T13-2)
- "Poles exactly the nontrivial zeros" for sigma_{1-s}(n)/zeta(s): globally false, there is a pole at s = -2. (G3-T16-3)
- D = x d/dx + 1/2 as a Hamiltonian: it is skew-adjoint; -iD with a fixed measure is the Hamiltonian. (G3-T12-1)
- A spectral line alone giving anti-Hermiticity (Jordan block counterexample); formal skew-symmetry constraining the spectrum (-d/dx on the half-line). (G3-T8-3)
- A bounded renorming of the model space making the generator normal: overlaps tend to one. (G3-T8-3)
- Inverse-closed letters giving the FE for a raw doubled transfer: B = diag(1,2) counterexample. (G3-T9-2)
- "Both pairings iff a scalar multiple of a unitary": it is B^†B = I; B = 2I disproves it. (G3-T9-2)
- A Kraus counterexample to conjugation closure under inverse pairing: none exists. (G3-T9-2)
- Hastings' bound with the *unenlarged* trivial set for a unitary family: false for every unitary family. (G3-T9-1)
- Deducing the infinite Weil converse from finite interpolation or Bochner-Schwartz: unavailable, F(0) = infinity. (G3-T9-4)
- Two trivial modes of Z from "the poles of xi at 0 and 1": xi is entire, the honest answer is the empty trivial set; and the naive negative-time extension is wrong by e^{u/2}. (G3-T9-4)
- The Dyson product without free propagators between jumps; the superoperator trace over M_n ⊗ M_n^*. (G3-T9-3)
- Arranging cos(l theta) <= 0 for most l: the rotation always returns near the identity. (G3-T9-1)
- Positivity of all ring norms giving a bosonic gas: diag(1,-1) has a_2 = -2. Integrality of N(L) at arbitrary real lengths is vacuous. (G3-T2-5, G3-T17-3)
- A nonzero finite-dimensional constant cMPS as a prime gas: N(L) is analytic, the comb is atomic. (G3-T2-5)
- A matrix logarithm as a cMPS embedding; a singular E having an exponential at positive time. (G3-T17-3)
- Positivity plus a functional equation forcing RH: explicit CPTP counterexample with poles {1,1/16} and odd eigenvalues {8,2}. (G3-T18-1)
- A unique stationary state implying mixing: a printed periodic channel refutes it. (G3-T18-1)
- On a 1|1 bond: kinetic regularity, full Lindblad normalisation, uniqueness and the exact half-entropy difference cannot all hold. (G3-T17-3)
- Closing the Horner automaton into a trace: it imposes a residue-automaton return condition, not Frobenius orbits. (G3-T4-5)
- The drafted Z/2 L-function of the pair shift (half multiplicities a_2 = 5/2); the Z(A^1/F_4)/Z(A^1/F_2) reading as an Artin quotient. (G3-T4-5, G3-T4-2)
- "Even = trivial character, odd = nontrivial" as a general theorem: refuted by the Ihara cover, where every physical mode is even. (G3-T4-5)
- Tr(Pi F^n) as a physical norm (it is |Tr(Pi F^n)|^2); exp(sum G_n u^n/n) giving 1 - Gu (it gives 1 + Gu). (G3-T3-1, G3-T4-5)
- The individual Kloosterman L-factor or Artin sign factor as a positive norm: only the completion is. (G3-T4-2, G3-T4-5)
- The 06g product letters as TP-gaugeable on the whole bond; H^0 as a second decoupled even block. (G3-T18-1)
- A finite bond giving a nonrational Z(u), infinitely many divisor points, or Riemann's zero distribution. (G3-T2-5)
- A single simple pole with an uncompleted self-reciprocal FE. (G3-T16-3)
- Odd-sector Alon-Boppana: refuted, rho(Phi_1) = 0 with unbounded bond. (G3-T5-2)
- "Equal spectral radii force net cancellation"; "the even algebra contains every positive operator"; "every structural period mode is even"; "every odd constituent supplies a zero". All false with one-line counterexamples. (G3-T5-1, G3-T5-2)
- "Net divisor on the circle iff both sectors in band": converse false, hidden modes cancel. (G3-T5-2)
- "Unitary letters make ring norms integral word counts" (16/3); "a circle numerator is a Weil polynomial or a curve" ((1-3u)^4 over F_9 would force -2 points). (G3-T5-2)
- "Exact sampling makes divisor RH and FE mesh-independent": false without a no-aliasing hypothesis. (G3-T17-1)
- "Each odd letter has a fixed sqrt(h) R limit": only the collective Hilbert-Schmidt bound holds. (G3-T17-1)
- "The divisor is the union of scalar correlation poles"; "continuous spectrum automatically gives a scalar signed measure". (G3-T17-2)
- The Lie walk threshold 1/2 (it is 1/(2d)); "tempered iff every geodesic exponent has real part -1/2"; "infinite-dimensional pi implies purely continuous diffusion spectrum"; the odd ladder starting at n/2. (G3-T16-1, G3-T16-2)
- P as a Hilbert-Schmidt eigenmode; str e^{tT} as an ordinary heat integral; "hyperbolic classes live only in the even sector". (G3-T16-2)
- "The lowest-exponent ladder is literally the Gamma divisor": only positions match. (G3-T16-2)
- K-type grading m = 0 versus ±2 as the Selberg/form-degree grading: not a G-invariant splitting, and K-parity makes the geodesic generator odd; "K-type supertrace supercancels" is false (theta factor 0.7300003). (G3-T16-2)
- Omega = X^2 + U_+U_- + X (wrong ordering) and J X J^{-1} = -1 - X (wrong sign). (G3-T14-3)
- The single total pushforward form on the first band: degenerate; branchwise orthogonalisation is required. (G3-T14-3)
- The single-copy exterior drift as a graded CP/cMPS transfer: refuted three ways, including negative flat supertraces. (G3-T3-1)
- A Selberg-centred FE/Ramanujan statement for the full retained Ruelle divisor: the even band is translated by -1. (G3-T5-3)
- Exponentiation turning the flow/Laplacian relation into the Ihara quadratic with the same adjacency; "first-band intertwining resolves the full-tower compression". (G3-T14-4)
- "First-band cusp states push forward to E(z, rho/2)": undefined at a pole; the Laurent coefficient is not in L^2. (G3-T15-2)
- e^{t/2} as the unitarising factor for the scattering sector: impossible; under RH it would be e^{3t/4}, centre -3/4, not -1/4. (G3-T15-2)
- "Truncated-norm positivity forces Re s_0 = 1/4": positive throughout the strip. (G3-T15-2)
- "Graph/channel pushforward is exceptional at ±sqrt q": false, only ±1 is. (G3-T8-2)
- "Full Hashimoto Hilbert-Polya iff closed sector Ramanujan": needs the *strict* band; endpoints give Jordan blocks. Quantum pushforward uses Ad(U_i), not Ad(U_i^*). (G3-T8-2)
- "Selberg's 1/4 is open for PSL_2(Z)": false, known by Booker-Lee-Strömbergsson. (G3-T14-3)
- Prime circles as side B; smearing the direct sum to get a trace; treating the undamped comb as tempered; calling a circle-translation generator dissipative. (G3-T14-6)
- The Casimir as a global Lindbladian on the full quotient; Lambda_fl = -d/dsigma log D (wrong sign); "the graph analogue of D is 1/det(1-uT)". (G3-T14-5, G3-T14-4)
- A positive prime comb in the cusp transform: the atoms are dips; and the unqualified "cusp term = channel trace damped at 1/4". (G3-T15-1)
- Identifying trace resonances with Pollicott-Ruelle resonances; "uniform curvature therefore RH"; replacing the modular scattering band by the compact Laplace band. (G3-T14-4, G3-T15-2)
- "GUE positions plus equal widths is the fingerprint of scalar loss"; positive canonical energy making the monodromy elliptic; local Euler factors as inner functions. (G3-T19-2, G3-T19-3, G3-T19-5)
- Reading the cusp dilation as exterior complex scaling, and complex scaling as a width mechanism. (G3-T19-5)
- Choosing the renewal rebound state to tune the spectrum; picking circle return factors to give the desired decay. (G3-T10-2, G3-T14-6)
- Deriving equal widths from Hecke self-adjointness continued to rho/2; substituting Selberg's 1/4 for RH; importing Deligne without identifying the cusp sector. (G3-T15-5)
- Thouless/Furstenberg reading of the Euler product; detailed balance/KMS as a source of scalar damping; treating the delay positivity as Weil positivity. (G3-T19-5, G3-T19-4)
- SPT protection of signs and phases as a route to moduli — "not revived by changing its vocabulary to supersymmetry". (G3-T14-2)
- "Every matrix Hermitian therefore real-rooted average characteristic polynomial": H = ±I_2 gives x^2+1. (G3-T19-5)
- "Watanabe-Fukumizu's corollary as a special case" of the quantum-Ihara theorem: a bouquet is not a WF graph. (G3-T7-3)

## Bookkeeping issues

- `obs:complementary-halves` was `proved` while its first clause rests on a `sketched` input, and `prop:absorbing-vacuum-channel` had `deps = -` although its Riemann specialisation needs the Lax-Phillips hypothesis — which had disappeared from the channel branch's dependency chain (notes/reviews/riemann-cmps-2026-09-12.md:741-758). In this book the printed status is *derived* from the deps, so a wrong dep list silently promotes a claim.
- Suggested gate check, never added: flag any `proved` row whose text mentions "zeros" but whose deps contain no zeta input (same review, :429).
- `db/claims.tsv` statement column for `num:bc-entropy` still lacks the constants, and the gate will not catch the drift (notes/reviews/riemann-cmps-2026-09-12.md:764).
- `thm:supertrace-rigidity` must record that the cut-offs are nonnegative and monotone in both parameters, or the unconditional pole-parity half cannot be reconstructed (same review, :729).
- Shard 05's closing paragraph calls the Weil-LPS channel's divisor points "nontrivial zeros"; they are poles, and an ungraded expander cannot supply zeros at all (notes/ramanujan-graded/astra-proofs.md:1603).
- `report/sections/04_riemann_channel.tex` l.169-173 has the prime part of Tr Z(t) with the wrong sign and the damping applied twice; the factor 2 is a Jacobian and the shard must name its variable (notes/selberg/astra-proofs.md:728-744).
- H-SZ's entireness, spectral divisor, trivial divisor and order at s = 0, and H-LAP, have no byte-cited source; this blocks promoting the continuous-Ramanujan theorem past conditional (notes/reviews/selberg-2026-09-12.md:26-47).
- H-GUI swallows the Anosov nondegeneracy and wave-front conditions and needs a measure-valued reading for the Laplace pairing (same review, :49-67, :122-133).
- H-CM's eigenspace clause is not quotable from arXiv and should be marked `assumed (named-not-quoted)` before the Rosati theorem is promoted (notes/reviews/ring-norm-tensor-2026-09-14.md:158-166).
- H-WAT needs a j-invariant / quadratic-twist gloss and a base point; H-DEG must stay split so the elliptic PH theorem is visibly non-circular; Deuring, the general Lefschetz theorem and the general Hodge inner product are named-not-quoted (notes/ring-norm-tensor/sources.md:148-488).
- The H-TWIST hedge in the shards ("all-even letters") is conservative and can be dropped — the algebraic identity is unconditional including odd letters (notes/reviews/ring-norm-tensor-2026-09-14.md:774-782).
- Ledger item 5 of the ring-norm proofs still records the growing cut-rank table as evidence of unboundedness and needs rewording after the self-dual-basis result (notes/ring-norm-tensor/astra-proofs.md:1110).
- The quantum-Ihara note never defines its norm (the Neumann step needs submultiplicativity), its `exact_check` shares an RNG stream with the float checks so the exact instances are not order-independent, and one cited proof is absent from `refs/src/` (notes/reviews/round2-2026-09-12.md:245-255).
- Six rows of the Selberg-letters prover ledger report the draft's *questions* as errors found; the lab book reads that ledger as a list of errors (notes/reviews/selberg-letters-2026-09-16.md:124-145).
- "Stable" for the covector eta_+ collides with the dual-bundle naming convention of the cited literature; a reader checking against it will mis-assign the weight (same review, :147-160).
- The order of the modular Selberg zero at rho/2 is an inference, not stated in the cited divisor item; the RH equivalence uses only the location (same review, :89-107).
- Both Selberg-side briefs asked for scratch scripts and both prover files used inline non-writing Python, leaving `notes/<lane>/scratch/` empty — the quoted numbers are exact but not re-runnable (notes/reviews/selberg-2026-09-12.md:153-159).
- The type III_1 attribution overreached its byte-verified support (the source labels only the critical temperature); fixed in round two, but should be verified against Bost-Connes 1995 if anything load-bearing ever depends on it (notes/reviews/riemann-cmps-2026-09-12.md:490).
- One very recent unrefereed preprint with typographic front matter is used for attribution only and must never be quoted as the authority for a proof (notes/ring-norm-tensor/sources.md:359-363).
- Minor unapplied scope repairs in the ring-norm lane: a hypothesis range J >= 1 that should be J >= 0, a terse radical-operator step, a terse congruence step, a boundary case described as zero rather than linearly dependent, and displayed certificate constants using a looser bound than the run (notes/reviews/ring-norm-tensor-2026-09-14.md:126-210).

## Audit

Total lane entries in the five files: **357** (L03: 61, L04: 60, L05: 84, L06: 71, L07: 81).
Absorbed: **357** — every lane ID appears in exactly one item's `Absorbs` list. None deliberately left out.
Items: **80**, across 20 themes.
