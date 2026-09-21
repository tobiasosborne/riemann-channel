# Lane L02: worklogs, open problems shard, lab log

## Coverage

| file | lines | read fully? | ideas found |
| --- | --- | --- | --- |
| docs/worklog/2026-09-11.md | 98 | yes | 19 (L02-001 .. L02-019) |
| docs/worklog/2026-09-12.md | 470 | yes | 44 (L02-020 .. L02-063) |
| docs/worklog/2026-09-13.md | 281 | yes | 18 (L02-064 .. L02-081) |
| docs/worklog/2026-09-14.md | 266 | yes | 31 (L02-082 .. L02-112) |
| docs/worklog/2026-09-15.md | 140 | yes | 17 (L02-113 .. L02-129) |
| docs/worklog/2026-09-16.md | 63 | yes | 10 (L02-130 .. L02-139) |
| docs/worklog/2026-09-17.md | 104 | yes | 6 (L02-140 .. L02-145) |
| docs/worklog/2026-09-18.md | 150 | yes | 11 (L02-146 .. L02-156) |
| docs/worklog/2026-09-19.md | 81 | yes | 8 (L02-157 .. L02-164) |
| report/sections/10_open_problems_dead_routes.tex | 149 | yes | 3 new (L02-165 .. L02-167); the rest are cross-references folded into the worklog entries above |
| report/sections/12_lab_log.tex | 249 | yes | 0 new — it is the worklogs' mirror at decision level; used to confirm shard ids and statuses, cited inside the entries |
| report/sections/00_frontmatter_status.tex | 74 | yes | 1 (L02-168) — the only forward-looking item there is the single-model-family caveat |

## Ideas and leads

### L02-001 Wick-rotating Bost–Connes into a Hilbert–Pólya operator
- Source: docs/worklog/2026-09-11.md:12-14
- Raised by: orchestrator (Claude); rejected by TJO
- Status at last mention: raised, not pursued; superseded by the permutation / transfer-matrix framing
- Content: The founding session asked whether one can Wick-rotate the Bost–Connes Hamiltonian (spectrum {log n}) into a Hilbert–Pólya operator. The obstruction recorded is that {log n} and the zeros are Fourier dual through the explicit formula, so "energies on one side are times on the other". TJO found the presentation too jargon-laden and had the whole thing rebuilt from scratch.
- Lead: none stated; the replacement route is the permutation picture. The duality obstruction is worth recalling whenever a "just rotate the BC generator" idea reappears.
- Related: L02-003, L02-013, L02-048

### L02-002 Elliptic curve over F_2 as the smallest two-sided instance
- Source: docs/worklog/2026-09-11.md:15-16
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued at the time ("Still too far"); realised much later in other form
- Content: The plan was a finite model with a gas over closed points on side A and Frobenius on H^1 on side B, linked by Lefschetz. TJO judged it too far from elementary at that point.
- Lead: the eventual four-letter elliptic tensor of shard 06h and the Pauli-letter qubit are this idea realised concretely; the detour through permutations was TJO's explicit instruction.
- Related: L02-016, L02-107, L02-120

### L02-003 Infinite permutations: find the *other* small matrix with the same fixed-point counts
- Source: docs/worklog/2026-09-11.md:17-23
- Raised by: TJO (permutations first) and orchestrator
- Status at last mention: partially explored; this became the notebook's definition of "side B"
- Content: The single identity 1/det(1 - TM) = exp Σ Tr(M^n) T^n/n makes a permutation's characteristic polynomial a Bose partition function with one mode per cycle. For a finite permutation RH is automatic ("unitary"); for an infinite permutation the hard part is producing a *different, small* matrix with the same fixed-point counts. Such a matrix exists iff the zeta is rational, and RH is then about the radii of its eigenvalues. Three shift examples are given (two symbols; golden mean; a four-symbol cyclic rule with eigenvalues 2, 1±i, 0) showing RH can hold or fail.
- Lead: "given the counts, construct the small matrix and bound its radii" is the whole notebook in miniature; the 2026-09-19 extension-disc work is the quantitative version of how much the counts pin down.
- Related: L02-004, L02-095, L02-160

### L02-004 Automata, Bowen–Lanford, and rationality/realisability criteria
- Source: docs/worklog/2026-09-11.md:24-25
- Raised by: orchestrator (Claude); sources Manning, Dwork, Puri–Ward
- Status at last mention: raised, not pursued
- Content: Rationality of a dynamical zeta (Manning, Dwork) and realisability of an integer sequence as a fixed-point count (Puri–Ward) were flagged as the classical background for "when does side B exist". Never developed into a shard.
- Lead: a realisability criterion would say exactly which count sequences admit a finite side B — the same question the ring-norm-tensor campaign kept hitting.
- Related: L02-003, L02-089, L02-112

### L02-005 RH as a flow: entropy 1, Lyapunov 1, T log T Weyl law, absorption sign, archimedean term
- Source: docs/worklog/2026-09-11.md:26-28
- Raised by: orchestrator (Claude), at TJO's insistence on the actual RH
- Status at last mention: partially explored; the inference list is used throughout
- Content: If RH is a flow with closed-orbit periods log p, one can read off: topological entropy 1, Lyapunov exponent 1, a T log T Weyl law for the zeros, a sign saying the zeros are absorbed rather than emitted, and an archimedean term. Selberg is named as the one family where all of this is realised and RH is a theorem.
- Lead: use Selberg as the calibration case for every structural guess — the strategy finally adopted on 2026-09-16.
- Related: L02-026, L02-130

### L02-006 Existence of side B is cheap; the radius bound is the whole content
- Source: docs/worklog/2026-09-11.md:29-32
- Raised by: orchestrator (Claude)
- Status at last mention: registered as a working principle throughout the book
- Content: For regular graphs the Ihara–Bass compression gives side B for free (the Bass blocks are the graph's cohomology written out) and RH ⇔ Ramanujan; K_4 satisfies it and the prism C_16 × K_2 fails (computed). So constructing *a* transfer matrix is never the difficulty — bounding its spectral radius is.
- Lead: stop rewarding constructions that merely produce a side B; the test is whether the construction *forces* the radius bound. This is the criterion behind the 2026-09-16 "most consequential step".
- Related: L02-130, L02-136

### L02-007 Shor's U_a as the level-N Galois symmetry and a snapshot of the dilation flow
- Source: docs/worklog/2026-09-11.md:33-34
- Raised by: orchestrator (Claude)
- Status at last mention: partially explored; folded into conj:galois-graded-bond
- Content: The modular-exponentiation unitary U_a of Shor's algorithm is Bost–Connes' level-N Galois symmetry and a snapshot of the dilation flow; its periods are tied to Dirichlet L-function zeros.
- Lead: compute the Γ_0(N) scattering determinant and see the Dirichlet L-zeros sorted by character, with the Shor map acting on the bond — still not done.
- Related: L02-061, L02-077, L02-167

### L02-008 Quantum expanders give a quantum Ihara zeta; RH ⇔ Hastings-Ramanujan
- Source: docs/worklog/2026-09-11.md:35-37
- Raised by: orchestrator (Claude)
- Status at last mention: registered and proved in general form (thm:qihara-general)
- Content: The edge superoperator on M_n ⊗ C^D satisfies an Ihara–Bass formula (verified numerically); RH for it is the Hastings-Ramanujan bound; the object is the Artin–Ihara L-function of the bouquet graph twisted by Ad(U).
- Lead: generalise off unitaries (done) and then ask what replaces Ramanujan without unitarity (still open).
- Related: L02-024, L02-025, L02-118

### L02-009 Channel = MPS transfer matrix; zeta = generating function of ring norms
- Source: docs/worklog/2026-09-11.md:38-45
- Raised by: orchestrator (Claude)
- Status at last mention: registered; the notebook's core dictionary
- Content: Tr E^n is the periodic-boundary ring norm of an MPS, so the zeta is the generating function of ring norms; AKLT plays the role of K_4; side B *is* the transfer matrix. The direct sum over ring sizes is the single-ring space and the gas is its symmetric Fock space, giving the same zeta as a Bose gas with single-particle energies -log E (Feynman cycles).
- Lead: every later campaign is an attempt to find the tensor whose ring norms are the arithmetic counts.
- Related: L02-010, L02-084, L02-095

### L02-010 Correction: -log E is *not* the entanglement Hamiltonian
- Source: docs/worklog/2026-09-11.md:42-45; report/sections/10_open_problems_dead_routes.tex:144-146
- Raised by: orchestrator (Claude), self-corrected
- Status at last mention: recorded as an error, corrected in notes/what-rh-has-become.md §8 and obs:hilbert-polya-hermitian
- Content: The founding conversation called -log E the "entanglement Hamiltonian". That is wrong: the transfer generator is non-Hermitian, and the imaginary parts of the zeros are its oscillation frequencies, not energies of a Hermitian entanglement Hamiltonian.
- Lead: none stated; a standing warning against Hermitian-sounding language for E.
- Related: L02-009, L02-033, L02-060

### L02-011 cMPS/Selberg as a continuum limit — flagged by TJO as overreach
- Source: docs/worklog/2026-09-11.md:46; report/sections/10_open_problems_dead_routes.tex:143-145
- Raised by: orchestrator (Claude); flagged down by TJO
- Status at last mention: dead as originally framed — "the functional integral framing of Selberg as a continuum limit (TJO: too far)"
- Content: The founding session tried to push the MPS picture to a cMPS/QFT description of Selberg. TJO called it overreach on the QFT side, and separately clarified that "QFT" in his usage did not mean functional integrals.
- Lead: the legitimate version arrived later as the graded transfer / ring-norm formulation, stated so that it passes to the continuum verbatim.
- Related: L02-016, L02-114, L02-130

### L02-012 Bost–Connes as a matrix-product operator over the prime chain
- Source: docs/worklog/2026-09-11.md:47-48
- Raised by: orchestrator (Claude)
- Status at last mention: computed; partially explored
- Content: BC written as an MPO along the chain of primes: bond Z/b, the Shor map as the transfer, eigenvalues L(β, χ̄)/ζ(β), KMS boundary vectors, and a collapse at β = 1.
- Lead: the β = 1 collapse is exactly where the later reframe puts the interesting object (critical KMS as fixed point).
- Related: L02-048, L02-057, L02-058

### L02-013 The sought object (the Phantasm, first statement)
- Source: docs/worklog/2026-09-11.md:49-52
- Raised by: orchestrator (Claude) with TJO steering
- Status at last mention: open; the notebook's target
- Content: A cMPS whose rings are the primes and whose transfer generator has the zeros as its spectrum. In that picture the prime number theorem is primitivity of the transfer channel and RH is the statement that there is a single correlation length. The space is forced to be a Q^×-quotient of adelic geometry (the product formula reads as flatness), and "expander = compression = Lax–Phillips".
- Lead: the three slogans (PNT = primitivity, RH = one correlation length, product formula = flatness) are testable on any candidate; none has been realised on an infinite arithmetic object.
- Related: L02-017, L02-048, L02-113, L02-130

### L02-014 Holevo–Werner lift: Lévy–Khinchin form and infinite divisibility of the zeta distribution
- Source: docs/worklog/2026-09-11.md:53-55
- Raised by: orchestrator (Claude)
- Status at last mention: partially explored; reappears in the SHW reading
- Content: Dilation-covariant semigroups have a Lévy–Khinchin form, and Khinchin's infinite divisibility of the zeta distribution is the arithmetic instance. The warning recorded is that dilation theorems give *existence* of a lift, not positivity.
- Lead: the concrete follow-up is the compensated-gauge computation in which the Lévy exponent of the BC Holevo generator is identified with the loss form 2 log|ζ(σ)/ζ(σ - iτ)|.
- Related: L02-036, L02-039

### L02-015 Scattering symbol S(τ): zeros, innerness, the σ = 1 prime-phase identity, 3000-zero test
- Source: docs/worklog/2026-09-11.md:56-58
- Raised by: TJO ("go hard" computation)
- Status at last mention: computed; numerics in scripts/scat.py, scripts/ringnorm.py, data/zeros3000.npy
- Content: The scattering symbol of the Riemann channel, its zeros, its innerness, an identity for the phase on σ = 1 written through the primes, and a ring-norm test against the first 3000 zeros.
- Lead: the 3000-zero data and the Cauchy–Gram condition numbers computed on it later became the Riesz-basis obstruction.
- Related: L02-046, L02-036

### L02-016 TJO's four standing working rules
- Source: docs/worklog/2026-09-11.md:68-73; report/sections/12_lab_log.tex:29-32
- Raised by: TJO
- Status at last mention: registered as the notebook's working rules
- Content: (a) stay elementary, no jargon dumps, one step at a time; (b) no curves or field extensions when a permutation will do; (c) "QFT" did not mean functional integrals; (d) length quantisation should come from a flatness-type condition.
- Lead: rule (d) is a genuine mathematical constraint, not just style — see L02-017.
- Related: L02-011, L02-017, L02-095

### L02-017 Length quantisation should come from a flatness condition
- Source: docs/worklog/2026-09-11.md:73 and 51-52
- Raised by: TJO
- Status at last mention: raised, not pursued as a separate item
- Content: TJO's instruction that the discreteness of the ring lengths (log p) must *come out of* a flatness-type condition rather than being imposed. The founding session's matching remark is that the product formula reads as flatness on the adelic quotient.
- Lead: find a model in which a flat-connection / product-formula condition forces the allowed ring lengths to be exactly {log n}. Never attempted directly; if it worked it would explain why the primes and only the primes appear.
- Related: L02-013, L02-020, L02-100

### L02-018 Algebraic-integer recognition of the Weil–LPS joint eigenvalues
- Source: docs/worklog/2026-09-11.md:85-87; report/sections/10_open_problems_dead_routes.tex:146-148
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, negative — "discarded as inconclusive and, on reflection, tautological (integer adjacency matrix)"
- Content: An attempt to recognise the joint eigenvalues of the Weil–LPS channels as small-degree algebraic integers from 5-digit numerical output.
- Lead: none; do not repeat. The non-tautological version is the Hecke identification, conj:weil-lps-hecke.
- Related: L02-165

### L02-019 MPS formulation of the Weil conjectures; the Dwork operator cannot see RH
- Source: docs/worklog/2026-09-11.md:89-98; report/sections/10_open_problems_dead_routes.tex:148-149
- Raised by: TJO ("whether the Weil conjectures admit an MPS formulation this way")
- Status at last mention: answered; positive for quadratic Artin–Schreier curves, negative beyond (obs:as-nonquadratic)
- Content: For quadratic Artin–Schreier curves the answer is exactly yes, with RH manifest as unitarity of the transfer matrix. Beyond quadratic the shift basis loses locality, and the only uniform object is Dwork's p-adic transfer operator, which cannot see RH.
- Lead: dead as a route to RH for curves, but the quadratic case became the notebook's Polya–Hilbert reference point.
- Related: L02-052, L02-059, L02-087

### L02-020 Circle flows of circumference log p — prime-by-prime ansätze are blind to zeros
- Source: docs/worklog/2026-09-12.md:5-22; report/sections/10_open_problems_dead_routes.tex:97-110
- Raised by: TJO (proposed the circle-flow Lindblad generator)
- Status at last mention: pursued, negative; registered as obs:prime-by-prime-blind (sketched)
- Content: The translation generator on a circle of circumference log p, summed over primes, has by Poisson summation trace Σ_n Λ(n) δ(s - log n) — the von Mangoldt weights fall out of the circumference automatically — and a dynamical zeta equal to the Euler product. But for any finite set S of primes the poles are exactly the rotation frequencies (2πi/log p)Z, so zeros exist only in the infinite product. The same holds for product states and commuting dilations. Verbatim: "The only relation between primes is additive." Two remarks kept: in the Witt convention L_1 - L_{-1} is the dilation flow (source and sink) and L_0 the rotation; and the explicit formula as a trace identity for s > 0 after damping by e^{-s/2} reads "circles damped at rate 1/2 plus the even part of the dilation flow on R equals e^{s/2} + e^{-s/2} minus the trace over the zeros".
- Lead: a hard negative constraint — any candidate must couple the primes non-trivially.
- Related: L02-017, L02-026, L02-103, L02-166

### L02-021 Rationality bookkeeping omitted from the Deligne note
- Source: docs/worklog/2026-09-12.md:37
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued (explicitly "omitted")
- Content: notes/deligne-via-graphs.md develops the whole Deligne argument in twisted-graph language — two sides, the sign difference between graph and curve, the "power up, dominate, take roots" engine, big monodromy as "only the contractions are invariant", the sign as the reason the interesting eigenvalues cannot make poles — but leaves out the rationality bookkeeping.
- Lead: fill it in if the graph-language account is ever used as more than exposition. Recorded there too: the proof does *not* use a Hermitian form, in contrast with Weil's Hodge index argument and the Artin–Schreier Parseval unitarity.
- Related: L02-004, L02-054

### L02-022 What the prior-art search did NOT find
- Source: docs/worklog/2026-09-12.md:55-72; report/sections/12_lab_log.tex:49-57
- Raised by: TJO ("was the quantum Ihara construction new?"); three Opus lanes plus byte-checked TeX
- Status at last mention: recorded in notes/prior-art-quantum-ihara.md
- Content: The matrix-weighted Ihara zeta with adjoint weights and its Bass formula are in Matsuura–Ohta (arXiv:2204.06424, eqs. 2.8-2.11), with the Artin–Ihara L-function reading in arXiv:2607.27935; the arbitrary-weight Bass formula for loopless graphs is Watanabe–Fukumizu (JMLR 2011); representation-twisted zetas go back to Sunada 1986. Not found anywhere: a zeta attached to a quantum *channel*, the reading "RH ⇔ Ramanujan quantum expander", or the MPS/ring-norm reading.
- Lead: those three are the notebook's own contributions and are what to write up first. Standing preference recorded from this session onward: arXiv TeX source, never PDF.
- Related: L02-008, L02-023, L02-024

### L02-023 The Weil-representation Ramanujan-channel instance is not in the literature
- Source: docs/worklog/2026-09-12.md:69-72
- Raised by: Opus literature lane
- Status at last mention: recorded
- Content: Iyer–Jain–Jordan–Somma (arXiv:2602.15180, Feb 2026) state exactly-Ramanujan channels from LPS generators via Harrow's theorem, but with SU(2) irreps; the Weil-representation instance computed in this notebook is not in the literature.
- Lead: this is the publishable corner of the Weil–LPS computation; its Hecke identification is conj:weil-lps-hecke.
- Related: L02-121, L02-165

### L02-024 Ihara–Bass for an arbitrary Kraus family (no unitarity, no invertibility)
- Source: docs/worklog/2026-09-12.md:74-91
- Raised by: orchestrator (Claude); proved in Lamport style, reviewed twice by Opus
- Status at last mention: registered, proved (thm:qihara-general and corollaries 2-4)
- Content: For an arbitrary Kraus family the (D-1)u^2 term becomes an operator D(u) and u·DΦ becomes a deformed channel A(u), both built from (1 - u^2 Ad(A_k† A_k))^{-1}; the unitary formula is a corollary. Side A stays positive for every Kraus family: Tr T^ℓ = Σ_w |Tr A_w|^2.
- Lead: since the quadratic pairing of eigenvalues is gone, ask what replaces Ramanujan — the next entry.
- Related: L02-008, L02-025

### L02-025 Cheap next step: a random-MPS pole-radius hunt
- Source: report/sections/10_open_problems_dead_routes.tex:17-30 (conj:kraus-ramanujan, status open)
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: Conjecture: there is a Ramanujan-type reading of the poles of the channel zeta for non-unitary Kraus families, with the canonical form Σ A_k† A_k = 1 constraining them. The concrete suggested experiment is a random-MPS pole-radius hunt at bond dimension 2-4, physical dimension 2, "to see whether the poles cluster on one circle at all".
- Lead: an afternoon of numerics; a positive answer would extend the Ramanujan dictionary to all channels, a negative one would say unitarity is essential.
- Related: L02-024, L02-114

### L02-026 Selberg Lindbladian from the vector fields on PSL, with the Laplacian as the small operator
- Source: docs/worklog/2026-09-12.md:120-124
- Raised by: TJO (exploration question)
- Status at last mention: pursued; shards 09b/09c, 13 propositions proved by codex, Opus-reviewed VALID
- Content: Replace channels by Lindblad generators; the circle of circumference log p gives a Poisson comb; the Selberg analogue should be a Lindbladian built from the vector fields on PSL whose "small operator" is the Laplacian.
- Lead: the direct ancestor of the 2026-09-16 Selberg-letters campaign.
- Related: L02-027, L02-130, L02-133

### L02-027 Astra's six corrections to the Selberg dictionary
- Source: docs/worklog/2026-09-12.md:136-150
- Raised by: codex prover (gpt-6-astra)
- Status at last mention: applied; shards 09b/09c
- Content: (1) The direct sum over primes has a *local orbital* trace, not a Hilbert-space trace, and the comb is not tempered. (2) The Casimir carries the compact direction with a minus sign, so the two-jump Lindbladian equals 2Ω = -2Δ only on the K-invariant sector. (3) The Laplace transform of the flat trace is +D'/D for the tower D(ς) = Π_{j≥1} Z(ς + j) (the draft had a minus). (4) The constant mode r_0 = i/2 must be excluded from the first band. (5) The cusp comb has negative sign (dips) with an exact +1/2 coming from the pole of ζ at 1 — the numerics agent found the same constant independently. (6) "cusp term = channel trace" is only an identity of prime measures after subtracting the archimedean part.
- Lead: item (5), the sign and exact +1/2, is the concrete handle on the cusp/archimedean bookkeeping a CCM modular computation would need. Six standard inputs were recorded as `assumed` rows, so the dependent propositions print `proved-conditional`.
- Related: L02-135, L02-144

### L02-028 PSL(2,Z) Kraus operators from Jones' Thompson-group representations
- Source: docs/worklog/2026-09-12.md:156-181
- Raised by: orchestrator (Claude); parked by TJO
- Status at last mention: pursued, negative, parked
- Content: Since Thompson's group T is piecewise PSL(2,Z), Jones' representations restrict to PSL(2,Z) and could supply Kraus operators. Assessment: the modular group *is* already the Riemann channel (Lax–Phillips scattering of the cusp); its Selberg zeta splits into Maass zeros on Re s = 1/2 (Hermitian, Laplacian) and zeros at ρ/2 from ζ(2s) in the scattering determinant (resonances; RH puts them on Re s = 1/4). The generators S, U give a Cayley graph that is a tree of triangles, so the untwisted zeta is trivial and a twisted one sees only the representation. Scratch numerics: the cubic Cayley graphs of PSL_2(F_p) on {S, T, T^{-1}} have λ_2 = 2.757, 2.791, 2.885, 2.919, 2.895, 2.920, 2.924 for p = 5..23 against 2√2 = 2.828, and the Weil-block channels λ_2 = 0.919 ... 0.970 against 2√2/3 = 0.943 — expanders (Selberg 3/16) but not Ramanujan beyond p = 7.
- Lead: recorded lesson — "Generators are the wrong Kraus choice for the same reason abelian Cayley graphs were: a presentation is not arithmetic; LPS generators are Hecke operators." The scratch script was deliberately kept out of the repo.
- Related: L02-029, L02-030, L02-121

### L02-029 Mayer's transfer operator L_s = Σ_n π_s(ST^n) as the object the transfer picture singles out
- Source: docs/worklog/2026-09-12.md:176-181 and 337-343
- Raised by: orchestrator (Claude); then ranked first by the codex free-association lane
- Status at last mention: raised, not pursued (details "from memory, not byte-cited")
- Content: The elements the transfer picture singles out are the Gauss-map branches ST^n. Mayer's operator gives Z(s) = det(1 - L_s) det(1 + L_s), with Maass forms at eigenvalue ±1 on Re s = 1/2 and Eisenstein period functions at s = ρ/2 (Lewis–Zagier, Chang–Mayer). The codex lane's first pick was the same operator as the induced cusp-return transfer operator, with cusp tail Σ_{n>M} (n+z)^{-2s} f(1/(n+z)) = Σ_ℓ f^{(ℓ)}(0) ζ(2s+ℓ, M+1+z)/ℓ! (rank-one leading residue at s = 1/2, full tail not rank one), and a Schur complement separating an interior block from the cusp coordinate as the place to look for a boundary pairing; explicit Taylor-basis matrix entries were supplied.
- Lead: build the Schur complement and look for the boundary pairing. Never executed; this is the most concrete unexecuted proposal in the resonances lane, and the one operator in which the Riemann zeros appear at ρ/2 by a known mechanism.
- Related: L02-028, L02-135, L02-144

### L02-030 SPT protection fixes signs, not moduli (dead route)
- Source: docs/worklog/2026-09-12.md:183-190; report/sections/10_open_problems_dead_routes.tex:112-141
- Raised by: orchestrator (Claude)
- Status at last mention: dead route, registered as obs:spt-protection-is-sign-data (sketched)
- Content: What an SPT phase protects (a phase, quantised, robust) matches the *sign* data of an L-function — root numbers as products of local ε-factors with the product formula as anomaly cancellation, Gauss-sum signs as Arf / Gauss–Milgram invariants, Hilbert reciprocity as a local-to-global cocycle. RH is modulus data, and moduli are not protected: a Ramanujan graph stops being Ramanujan under a small symmetric perturbation, and the PSL(2,F_p) Cayley graphs fail the bound for p ≥ 11 while keeping every symmetry.
- Lead: none; cohomological protection cannot deliver RH. Two relabellings kept: the Weil–LPS channels live on the edge Hilbert space of the Z/p × Z/p cluster-state phase (the Heisenberg group is that edge's projective representation and SL(F_p) its automorphism group, acting by the Weil representation); and BC at β = 1 is a critical point of spontaneous Galois symmetry breaking, not an SPT.
- Related: L02-031, L02-028

### L02-031 Weil's criterion as bulk–boundary mode pairing
- Source: docs/worklog/2026-09-12.md:187-190; report/sections/10_open_problems_dead_routes.tex:129-135
- Raised by: orchestrator (Claude)
- Status at last mention: registered; developed into the Weil-positivity campaign
- Content: What survives of the SPT idea is the reading of Weil's criterion: the reflection ρ ↦ 1 - ρ̄ pairs the mode at a zero with the mode at its mirror image, RH says every mode is its own partner, and Weil's form is that pairing written on the primes through the explicit formula.
- Lead: the finite, arbitrary-Kraus version of exactly this is the inflow-identity campaign.
- Related: L02-030, L02-032

### L02-032 The inflow identity for an arbitrary Kraus family (T1–T6)
- Source: docs/worklog/2026-09-12.md:192-209 and 211-234
- Raised by: TJO — "chase the inflow identity in the most general quantum setting"
- Status at last mention: registered, shards 08b/08c; reviewed, no INVALID
- Content: T1: Weil positivity of the rescaled trace sequence ν_ℓ = r^{-ℓ}(Tr X^ℓ - trivial) is equivalent to the one-sided bound |μ| ≤ r off the trivial set (Herglotz, Poisson kernel). T2: a duality μ ↦ r^2/μ̄ of the spectrum makes the bound two-sided and turns the Weil form into the mode-pairing form — the finite inflow identity. T3: Kraus dichotomy — inverse pairing buys the functional equation, adjoint pairing buys reality of spec Σ, unitarity buys both. T4: a Bochner version for Lindblad-type generators with the continuous ring norms from the Dyson expansion. T5: a Hilbert–Pólya inner product exists iff the generator is semisimple on the circle. T6: the zeta instance as a dictionary entry.
- Lead: "the duality that makes the bound two-sided" is the structural requirement a Riemann-side candidate must supply; in graded language it became the functional-equation condition J E J^{-1} = q E^{-1}.
- Related: L02-031, L02-033, L02-034, L02-114

### L02-033 Weil positivity is blind to Jordan blocks
- Source: docs/worklog/2026-09-12.md:204-206 and 233-234
- Raised by: orchestrator (Claude), proved in the campaign
- Status at last mention: registered
- Content: A Hilbert–Pólya inner product needs semisimplicity on the circle *in addition* to Weil positivity; positivity alone cannot exclude a Jordan block.
- Lead: exactly the obstruction that resurfaced on the Selberg side as the Jordan block at Laplace eigenvalue 1/4, and again at the endpoints of the finite Hashimoto lift — the same gap in three places.
- Related: L02-032, L02-132, L02-136

### L02-034 Three of the orchestrator's drafted Weil-positivity statements were wrong
- Source: docs/worklog/2026-09-12.md:222-226
- Raised by: codex prover and Opus numerics lane, independently
- Status at last mention: corrected
- Content: (a) An inverse-paired Kraus family has conjugation-closed spectrum and nonnegative ring traces — but it is the Ad form, not the pairing, that gives both. (b) "Unitary up to a scalar" is not enough for the two pairings to coincide (counterexample at B = 2). (c) The Dyson product needs the free propagators between jumps. Two reviewer MINOR items were also fixed: the ring trace needs no pairing, and it is spec Σ, not spec T, that the adjoint pairing makes real.
- Lead: none stated; kept as a record of which plausible statements fail.
- Related: L02-032, L02-040

### L02-035 Huang's graph criterion, Suzuki's kernel form, and the prime-weight sign
- Source: docs/worklog/2026-09-12.md:235-241
- Raised by: Opus reviewer
- Status at last mention: partially applied; prop:ringnorm-trace was "still to be restated (HANDOFF 1c)" at that point
- Content: Huang's graph criterion is h_k = ν_0 - ν_k, the boundedness form of Weil positivity (verified by the reviewer on K_4, Petersen, K_5 and a ladder); Suzuki's kernel form and Weil/Li were cited from TeX. The reviewer's X3 independently confirms the centred prime weight -2Λ(n) n^{-1/2} in shard 04's convention, recorded as obs:ringnorm-sign-correction.
- Lead: the boundedness form h_k = ν_0 - ν_k is a second, cheaper test any candidate can be run against.
- Related: L02-032

### L02-036 The Riemann channel is a no-event semigroup — Stinespring-with-prime-jumps answered negatively
- Source: docs/worklog/2026-09-12.md:250-256; report/sections/10_open_problems_dead_routes.tex:32-41
- Raised by: TJO's pointer to Siemon–Holevo–Werner (arXiv:1707.02266)
- Status at last mention: conj:stinespring-jump-form answered negatively *as literally stated*; the shard still carries it as an open paragraph
- Content: ρ ↦ Z(t)* ρ Z(t) sends pure states to multiples of pure states, so it is a no-event semigroup and necessarily of the form C_t ρ C_t* with C_t a contraction semigroup. Hence it has *no* jump operators at all: "any generator with nonzero jump term produces mixed states at first order". A Stinespring form of Z(t) whose jumps are the prime dilations therefore cannot exist.
- Lead: the shard still suggests a blind re-test in a second model family — write Z(t) through Cauchy kernels and test a Holevo-form generator with jumps at k log p on K_S. "A negative answer with a reason is a result."
- Related: L02-037, L02-038, L02-039

### L02-037 The exit space is the cusp; J is the Lax–Phillips arrival-time wavefunction
- Source: docs/worklog/2026-09-12.md:257-267 and 301-302
- Raised by: orchestrator (Claude) reading SHW
- Status at last mention: recorded as an identification; corrects the notebook's own wording in shard 04
- Content: The exit space (E, j) with ⟨jψ, jφ⟩ = -⟨(B + B*)ψ, φ⟩ is one-dimensional for a scalar inner function (rank-one dissipative part, Livšic) — i.e. the cusp — and is C^h for Γ(N) with h cusps. Jψ(t) = j Z(t) ψ is an isometry K_S → L^2(R_+; E) because Z(t) → 0 strongly: this is the Lax–Phillips outgoing translation representation restricted to K_S, read as the arrival-time wavefunction at the cusp. SHW's half-sided-shift example is exactly this structure, with non-closable jump operators |φ_α⟩⟨j|.
- Lead: for Γ(N) the exit space is C^h — several cusps give a *matrix*-valued inner function, the natural place for the character grading of conj:galois-graded-bond. Not pursued.
- Related: L02-036, L02-038, L02-061, L02-167

### L02-038 The SHW renewal generator: reinsert at a rebound state Ω
- Source: docs/worklog/2026-09-12.md:268-276; report/sections/10_open_problems_dead_routes.tex:63-79
- Raised by: orchestrator (Claude) reading SHW; adopted into conj:phantasm-both-halves
- Status at last mention: open — "whether its spectral problem sees RH is open"
- Content: Every standard generator whose no-event part is Z is parametrised by a single subnormalised rebound state Ω: Lρ = Bρ + ρB* + ⟨j, ρj⟩ Ω, conservative iff Tr Ω = 1 — a renewal process "exit at the cusp, reinsert at Ω". Its spectrum is governed by the scalar equation 1 = m̂_Ω(λ), with m_Ω the cusp arrival density from Ω. This is "the more intricate semigroup their framework hands us for free".
- Lead: solve 1 = m̂_Ω(λ) for an arithmetically natural Ω and see whether the roots are the zeros — a concrete, small, unexecuted computation. The vacuum choice of Ω is already excluded, so a *mixed* rebound state is the live case.
- Related: L02-036, L02-050, L02-056, L02-167

### L02-039 The gauge lemma: moving primes between the no-event part and the jumps
- Source: docs/worklog/2026-09-12.md:277-289
- Raised by: orchestrator (Claude) reading SHW
- Status at last mention: recorded as a precise statement of what the Sz.-Nagy–Foias step does and does not preserve
- Content: In the compensated gauge λ_p = -√r_p, the Bost–Connes Holevo generator at σ > 1 becomes a no-event generator K' = i·drift - Σ_p p^{-σ}(1 - U_p) whose symbol is the Lévy exponent, with loss form 2 log|ζ(σ)/ζ(σ - iτ)|, plus compensated jumps √r_p (U_p - 1). Shard 04's bridge "drop the divergent real part, keep the phase" is: subtract the divergent constant log ζ(σ) as σ → 1; the finite remainder -log|ζ(1 - iτ)| is *indefinite*, hence not a dissipative generator, and the inner-function construction replaces it by a contraction with the same phase. (The sign of the gauge lemma is as in SHW's proof, not as displayed; noted in the extract.)
- Lead: this pinpoints exactly what is lost at the Sz.-Nagy–Foias step — positivity — which is where the whole difficulty sits. Anyone attacking the compressed semigroup should start here.
- Related: L02-014, L02-036, L02-041

### L02-040 Unbounded version of the continuous ring norms via SHW's iterated dilation
- Source: docs/worklog/2026-09-12.md:290-294
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: The Weil-positivity Dyson formula (thm:cmps-ring-norms) is the trace over events of SHW's iterated dilation J^{(n)}_τ with free propagators between jumps; SHW's remark that no further domain questions arise once J is bounded is "the route to the unbounded version of the continuous ring norms".
- Lead: carry the finite-dimensional ring-norm theorem to unbounded generators — needed if the ring-norm machinery is ever to touch an infinite arithmetic object.
- Related: L02-032, L02-116

### L02-041 Non-standard generators: explosion plus reinsertion at infinity in the infinite-activity BC regime
- Source: docs/worklog/2026-09-12.md:295-300
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued — verbatim "Idea only; nothing computed."
- Content: SHW's non-standard generators (a domain producing no new pure states) come from explosion plus reinsertion at infinity. The arithmetic place where the no-event loss rate diverges is the infinite-activity Bost–Connes regime σ ≤ 1 (total jump rate log ζ(σ)); a conservative completion of the *critical* process by reinsertion at the cusp is the candidate non-standard object.
- Lead: build it. This is the only proposal in the notebook that addresses the critical regime σ ≤ 1 directly, where the normal-KMS obstruction bites.
- Related: L02-038, L02-058, L02-167

### L02-042 The cusp basis is the wrong basis (Porter–Thomas widths)
- Source: docs/worklog/2026-09-12.md:306-310
- Raised by: orchestrator (Claude), as a negative orientation
- Status at last mention: recorded; partly undercut by the codex lane
- Content: A rank-one cusp coupling gives Porter–Thomas distributed widths for GUE-distributed positions, so the cusp basis is the wrong basis for the physics one wants.
- Lead: undercut by correction (i) below — equal-width poles at arbitrary positions *do* have a one-port realisation, so the information is in the couplings, not in the widths.
- Related: L02-046

### L02-043 Kotani's Zeta string / canonical systems: RH iff a positive-mass Krein string exists
- Source: docs/worklog/2026-09-12.md:310-317
- Raised by: orchestrator (Claude), ranked first among the mechanisms; source Suzuki 2206.03682 §9
- Status at last mention: raised, not pursued
- Content: Under RH, Σ_γ 2/(γ^2 - z) is the Weyl function of a Krein string with mass density m(x) ~ 4x (log x)^{-2}; conversely RH holds iff such a positive-mass string exists. Dictionary recorded: J-unitary = inverse pairing, positive mass = the missing adjoint pairing.
- Lead: an exact restatement of RH as the existence of a positive object — structurally the same shape as "a Ramanujan channel exists". The notebook never tried to build the string from ring-norm data.
- Related: L02-032, L02-114

### L02-044 Ruelle resonances of the cusped flow (Bonthonneau–Weich)
- Source: docs/worklog/2026-09-12.md:317-320; docs/worklog/2026-09-19.md:21
- Raised by: orchestrator (Claude)
- Status at last mention: partially explored — "Bonthonneau–Weich to fetch"; the TeX was finally cached on 2026-09-19
- Content: Ruelle resonances of the cusped geodesic flow were ranked as a mechanism connecting a transfer spectrum with resonances. Caution recorded: Faure–Tsujii lines from uniform expansion give the Selberg line, not the ζ line.
- Lead: the source is now local; nobody has used it.
- Related: L02-029, L02-131, L02-158

### L02-045 Complex scaling as continuation in the BC dilation parameter; Thouless; Wigner delay
- Source: docs/worklog/2026-09-12.md:320-322
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: Three smaller mechanisms from the same ranked list: factorised scattering and the Thouless formula; "complex scaling = continuation in the BC dilation parameter"; and the remark that the Wigner delay is positive regardless of RH, so it carries no RH information.
- Lead: the complex-scaling identification is a one-line dictionary entry that would make resonance technology directly available on the BC side; never tested.
- Related: L02-044, L02-048

### L02-046 The codex lane's three corrections, including the Riesz-basis obstruction
- Source: docs/worklog/2026-09-12.md:325-337
- Raised by: codex prover (gpt-6-astra), resonances free-association lane (646 lines, 15 mechanisms ranked, three proposed computations)
- Status at last mention: recorded; (ii) is a genuine structural obstruction
- Content: (i) Equal-width poles at arbitrary positions DO have a one-port realisation by inverse design — Hermite–Biehler interlacing gives residues |v_k|^2 = 2V(E_k)/U'(E_k) — so "GUE positions plus equal widths" is not by itself a fingerprint of scalar loss; the information is in the couplings. (ii) Equal modal widths do not give a uniform norm-decay law, because the modes are non-orthogonal: the Cauchy Gram matrix 2√(w_n w_m)/(w_n + w_m - i(a_m - a_n)) has condition number 9.9 for the first 24 ordinates and 701 for the last 24 of 3000, so a bounded renorming of K_S is excluded by the Riesz-basis / interpolating-sequence criterion — "a Hilbert–Pólya space must be a different completion, not an equivalent norm on the model space". (iii) Positive canonical-system energy does not force every spatial transfer matrix to be elliptic.
- Lead: (ii) is the sharpest negative in the notebook about Hilbert–Pólya: do not look for a metric on K_S. It is the reason the later work insists on regular data and weighted norms.
- Related: L02-042, L02-082, L02-116

### L02-047 Suzuki's prime-defined screw kernel
- Source: docs/worklog/2026-09-12.md:341-343
- Raised by: codex prover (its third proposed computation)
- Status at last mention: calibrated in-session only
- Content: On t_j = j/8, j ≤ 16, the prime-defined kernel eigenvalues lie in [0.0223, 0.817] versus [0.0217, 0.806] for the zero-defined kernel.
- Lead: extend the calibration; the gap between the two kernels is a measurable proxy for how much of the zero data the primes alone determine — close in spirit to the extension disc of 2026-09-19.
- Related: L02-043, L02-160

### L02-048 The Bost–Connes reframe: dilation time is the 1D space of a cMPS
- Source: docs/worklog/2026-09-12.md:345-362; report/sections/12_lab_log.tex:69-70
- Raised by: TJO (clarification on sides), then set as the central priority
- Status at last mention: open; the notebook's central programme
- Content: BC as used so far is side A only (a product state over primes, ζ(β) a partition function, the dilation spectrum being the ring lengths log n) — "hence underwhelming". The flip: dilation time is the 1D space of a cMPS, the bond carries the Riemann Lindbladian, its unique fixed point is the pole at s = 1, i.e. the critical KMS_1 state (not a Gibbs state at β > 1); the zeros are the relaxation modes; the physical cMPS is pure and the KMS state is its entanglement spectrum. The Gibbs states at β > 1 form the symmetry-broken steady-state manifold labelled by the Galois group, and the BC phase transition is ergodicity breaking of the Lindbladian.
- Lead: every later campaign is an attempt to construct this object. If it worked, RH becomes "one relaxation rate".
- Related: L02-013, L02-049, L02-050, L02-167

### L02-049 The bond must be graded: zeros fermionic, pole bosonic, ring norm a supertrace
- Source: docs/worklog/2026-09-12.md:356-359
- Raised by: orchestrator (Claude), forced by a sign
- Status at last mention: registered; later turned into a no-go theorem and a proved supertrace identity
- Content: A cMPS ring norm is a positive sum of squares, while the zeros enter the explicit formula with a minus sign (Deligne's third ingredient; the reviewer's X3 "dips"). So the bond must be graded, the zeros fermionic, the pole bosonic, and the ring norm a supertrace — as in the Artin–Schreier lane.
- Lead: this single sign argument drove the whole graded programme (shards 02f/04e/04f and 02h/03c/03d).
- Related: L02-054, L02-081, L02-114

### L02-050 The rebound state is fixed by demanding the critical BC state as steady state
- Source: docs/worklog/2026-09-12.md:360-362
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: The existing Riemann channel has no fixed point (Z(t) → 0); a fixed point requires SHW reinsertion, and demanding the critical BC state as the steady state fixes the rebound state through ρ_∞ ∝ ∫_0^∞ Z(t) Ω Z(t)* dt.
- Lead: invert that integral equation for Ω — a small, concrete, never-attempted computation that would produce the unique candidate rebound state.
- Related: L02-038, L02-048, L02-056, L02-167

### L02-051 The Phantasm campaign (items 0a–0c) and TJO naming the object
- Source: docs/worklog/2026-09-12.md:364-380; report/sections/12_lab_log.tex:72-91
- Raised by: TJO — "Our job is clear: we must pursue the Bost–Connes reframe. We must understand everything we can about the cMPS implicitly defined. The entanglement, the fermionic aspect, transfer operator. All inferable info." and "Phantasm is my word for the mythical object we are chasing."
- Status at last mention: registered; conj:phantasm-both-halves replaced item 0b
- Content: One codex prover (T1–T8, 1356 lines, 199k tokens), three Opus lanes in parallel, then an Opus REFUTE review; new shards 02c, 04b, 04c, 06b, plus conj:galois-graded-bond.
- Lead: the campaign's three outputs are rigidity, a no-go, and a realisation (next three entries).
- Related: L02-048, L02-053, L02-054, L02-167

### L02-052 Artin–Schreier sign law: two wrong drafts and the exact law
- Source: docs/worklog/2026-09-12.md:382-397
- Raised by: numerics lane (falsifications) and codex prover (the correct law)
- Status at last mention: proved; confirmed in 624 further checks
- Content: The founding session's α_i = -λ_i(E) "uniformly in n" is false (fails at q = 3, a = (1,1) and (0,1,1)). The orchestrator's replacement S_n = -(-η(-1))^n conj(Tr E^n) fitted 40 data points and then failed twice more. The exact law is S_n = (-1)^{n-1} δ_n Tr E_g^n with δ_n = det(S|_{ker P_g(S)}), the determinant of the Frobenius shift on the radical of the ring form; equivalently a periodic sign flipping exactly when 2h | n, where h is the smallest power of q above the order of vanishing of z^J P_g(z) at -1. The founding claim holds iff P_g(-1) ≠ 0, the orchestrator's iff P_g(-η(-1)) ≠ 0. The proof constructs a square root A of the normal-basis Gram matrix with A^2 = C, A^{[q]} = SA; on the whole space it is Stickelberger's theorem.
- Lead: methodological lesson — fit-then-falsify by an independent numerics lane caught two wrong laws in a row.
- Related: L02-019, L02-059, L02-137

### L02-053 Rigidity of a graded supertrace distribution; the infinite parity case is open
- Source: docs/worklog/2026-09-12.md:399-406; report/sections/10_open_problems_dead_routes.tex:78-79
- Raised by: codex prover
- Status at last mention: proved for finite flips; obs:parity-infinite-open remains open
- Content: The supertrace distribution of a graded generator determines its net graded spectrum up to cancelling pairs. The explicit formula then forces the pole to be even and the nontrivial zeros odd; the trivial zeros and the ladder have undetermined parity. Positivity forces the parities for *finite* flips; the infinite case is open, "and the prover said exactly why". (The reviewer strengthened part (i): the pole is even with no domination premise.)
- Lead: settle the unrestricted infinite parity question; if it settles positively, the parity assignment of the whole divisor is forced rather than assumed.
- Related: L02-049, L02-054, L02-167

### L02-054 No-go: no ungraded trace has the point counts of a genus ≥ 1 curve
- Source: docs/worklog/2026-09-12.md:405-409; sharpened at docs/worklog/2026-09-13.md:152-155
- Raised by: codex prover; sharpened by the Opus reviewer
- Status at last mention: proved (thm:no-ungraded-trace, shard 04b)
- Content: No finite matrix and no trace-class operator has the point counts of a genus ≥ 1 curve as its trace sequence (Lidskii plus a residue sign), so no bosonic MPS ring norm can. A zeta with a numerator forces the grading, and the Ihara zeta of a graph does not have one. Reviewer's sharpening: the operative hypothesis is "honest trace", not positivity, and (1-u)/(1-2u) is an instance of the theorem, not a counterexample.
- Lead: this is the theorem that makes the grading non-optional.
- Related: L02-049, L02-071, L02-113

### L02-055 Realisation: an explicit graded generator whose supertrace is the prime measure
- Source: docs/worklog/2026-09-12.md:409-412 and 451-462
- Raised by: codex prover; independently re-derived by the Opus reviewer
- Status at last mention: proved
- Content: On C_+ ⊕ (K_S ⊕ ℓ^2(N))_- the generator 0 ⊕ B ⊕ diag(-(k + 1/2)) has supertrace exactly 2P_+(t) = 2 Σ (Λ(n)/n) δ(t - 2 log n); the uncentred distributional trace of Z(t) alone is 1 - 2P_+ - e^{-t/2}/(e^t - 1). The reviewer re-derived the latter independently and rejected three plausible wrong variants by 3-4 orders of magnitude.
- Lead: the realisation is *spectral*, not CP — there is no supplied Kraus realisation, which is exactly the gap later named explicitly and confirmed as a negative for Selberg.
- Related: L02-127, L02-134

### L02-056 The vacuum-decay Lindbladian: right spectrum, trivial entanglement
- Source: docs/worklog/2026-09-12.md:411-416; report/sections/10_open_problems_dead_routes.tex:69-72
- Raised by: codex prover
- Status at last mention: pursued, negative (prop:vacuum-renewal-trivial-entanglement)
- Content: The vacuum-decay Lindbladian on B(C ⊕ K_S) is a genuine CPTP semigroup with the Riemann channel as its odd coherences (each zero once) and the pair sums as even populations. But its stationary state is the pure vacuum — trivial entanglement — and the vacuum is absorbing rather than a rebound state: the renewal integral diverges.
- Lead: the vacuum choice of rebound state is excluded; a *mixed* rebound state is what conj:phantasm-both-halves now requires.
- Related: L02-038, L02-050, L02-167

### L02-057 The prime-chain detailed-balance Lindbladian has a real spectrum (no zeros)
- Source: docs/worklog/2026-09-12.md:416-419
- Raised by: codex prover
- Status at last mention: pursued, negative
- Content: It has the Gibbs density as its fixed point; its diagonal spectrum is the closure of Minkowski sums of M/M/1 bands (real, no zeros), and its off-diagonal part is real-spectral on a weighted space when the down rates are summable (the reviewer added that the reality statement needs its weighted space and β > 1).
- Lead: detailed balance is the wrong symmetry — it forces reality, hence no oscillation frequencies. Any candidate must break detailed balance.
- Related: L02-056, L02-100

### L02-058 Normal KMS states exist only for β > 1; the critical state is not a normal density
- Source: docs/worklog/2026-09-12.md:419-421; report/sections/10_open_problems_dead_routes.tex:74-78
- Raised by: codex prover (prop:normal-kms-gibbs)
- Status at last mention: proved; it is the first obstacle named in conj:phantasm-both-halves
- Content: Normal KMS states of Ad(N^{it}) exist only for β > 1; at β = 1 the fixed point is not a normal density. So K_S with its pure vacuum cannot be the whole bond, and the missing identification of K_S with the Bost–Connes bond is the first obstacle.
- Lead: either enlarge the bond (a type III generalisation at β = 1, which the conjecture allows) or abandon normality.
- Related: L02-041, L02-048, L02-167

### L02-059 The Weil bound is saturated iff M_g^n = 1
- Source: docs/worklog/2026-09-12.md:424-426
- Raised by: codex prover
- Status at last mention: proved
- Content: For Artin–Schreier the transfer unitary is a Weil-representation operator of an explicit symplectic map M_g, and |S_n|^2 = q^{n + dim ker(M_g^n - 1)}, so the Weil bound is saturated exactly when M_g^n = 1. The point count is the supertrace of (E_0 ⊕ 1)_+ ⊕ (⊕_a F_{ag})_- (even = trivial character, odd = nontrivial characters).
- Lead: a clean criterion tying extremality (Ramanujan saturation) to a finite-order condition on a symplectic matrix — the kind of "letters force the bound" statement the 2026-09-16 campaign was after.
- Related: L02-052, L02-087, L02-130

### L02-060 TJO: the BC state literally is the entanglement spectrum
- Source: docs/worklog/2026-09-12.md:428-434; report/sections/12_lab_log.tex:86-89
- Raised by: TJO — "If the BC state is the fixed point of the Lindblad it literally is the entanglement spectrum"
- Status at last mention: agreed and computed (scripts/bc_entropy.py)
- Content: Consequently the Gibbs entropy log ζ(β) - β ζ'/ζ(β) and its cutoffs are *entanglement* data: log P + log log P under a prime cutoff at β = 1; (1/2) log N under a bond cutoff; a power law below and saturation above. Correction recorded: the level density e^E is Hagedorn, not Cardy, so the CFT finite-entanglement scaling law (and a stray c = 12) does not apply. The reviewer pinned the constants: exactly 1 - γ_E, with cutoff constants 0 (Mertens constants cancel) and -γ_E/2.
- Lead: entanglement scaling is now a diagnostic any candidate bond must match, and the Hagedorn density rules out CFT-style arguments.
- Related: L02-048, L02-094

### L02-061 TJO: the theory must carry the crazy symmetry group (Galois, symplectic, adeles)
- Source: docs/worklog/2026-09-12.md:434-440; report/sections/10_open_problems_dead_routes.tex:81-93
- Raised by: TJO
- Status at last mention: registered as conj:galois-graded-bond (open)
- Content: TJO's demand that the object admit "the crazy symmetry group of something BC-shaped, Galois, symplectic, adeles". Recorded in two forms: the trivial-versus-nontrivial-character reading of the grading, which the Artin–Schreier super-transfer matrix already exhibits; and conj:galois-graded-bond — the Γ_0(N) model space, whose scattering determinant involves the Dirichlet L-functions mod N, carries the zeros of L(s, χ) organised by the characters of (Z/N)^×, with the Shor map as the level-N Galois symmetry on the bond. The symplectic side is the Weil-representation structure of the Artin–Schreier transfer unitary.
- Lead: "This is a computation, not yet done." The Riemann-side test of the character grading, and the highest-value unexecuted item in the open-problems shard.
- Related: L02-007, L02-037, L02-077, L02-167

### L02-062 Prior art for the graded picture: Deninger, Connes, fermionic (c)MPS
- Source: docs/worklog/2026-09-12.md:442-449
- Raised by: orchestrator (Claude), recorded honestly
- Status at last mention: recorded
- Content: The graded operator with an even pole and odd zeros whose Lefschetz trace is the explicit formula is Deninger's programme (math/0505354:316-326, 874-880); the minus sign is Connes's absorption spectrum (math/9811068:575-581); the fermionic MPS supertrace is Bultinck–Williamson–Haegeman–Verstraete; the fermionic cMPS with a graded bond is already in Haegeman–Cirac–Osborne–Verstraete 2013. The notebook's own: the tensor-network reading, the rigidity/no-go/realisation statements, the two halves, and the Artin–Schreier sign law with its Weil-representation structure.
- Lead: none stated; it demarcates what is new.
- Related: L02-049, L02-054

### L02-063 obs:complementary-halves downgraded by a dependency gap the gate cannot see
- Source: docs/worklog/2026-09-12.md:466-470
- Raised by: Opus reviewer (round 2)
- Status at last mention: honest status `sketched`
- Content: The reviewer found a dependency gap the gate cannot see: the absorbing-vacuum channel's K_S clause had dropped the Lax–Phillips input, and the complementary-halves observation rested on sketched infinite-dimensional bookkeeping without declaring it. Both were repaired mechanically and the gate then downgraded the observation.
- Lead: the "two halves" statement (one object with both the BC fixed point and the zeros as relaxation modes) is weaker than it looks; conj:phantasm-both-halves is its open form. Also a warning that the gate cannot detect undeclared dependencies.
- Related: L02-051, L02-167

### L02-064 Ihara zeta for simplicial complexes: are the zeros "surface-like"?
- Source: docs/worklog/2026-09-13.md:3-8
- Raised by: TJO (sidequest)
- Status at last mention: answered; shards 02d, 08d/08e
- Content: TJO's question: since the fermion–zeros connection for graphs looks increasingly central and the zeros may carry "surface-like" qualities, is there a natural Ihara-type theorem for simplicial complexes generalising the finite-graph result, and what is its natural quantum generalisation?
- Lead: the answer was that the surface-like feature survives only as an odd chamber contribution to a graded divisor, and on the building vertex side it cancels completely; "None of this touches the Riemann side."
- Related: L02-071, L02-073, L02-049

### L02-065 "No fable subagents", and recover killed agents' transcripts
- Source: docs/worklog/2026-09-13.md:11-15
- Raised by: TJO
- Status at last mention: registered as standing practice
- Content: Two literature lanes were launched on the default (Fable) model; TJO said "no fable subagents" and they were stopped and relaunched on Opus. A Sonnet recovery pass over the *killed* transcripts showed they had already fetched ~35 e-prints and extracted the key identities, so the Opus lanes built on that instead of refetching.
- Lead: stopped agents leave usable JSONL transcripts — always do a cheap recovery pass before relaunching.
- Related: -

### L02-066 There is no Ihara-type zeta for a general simplicial complex
- Source: docs/worklog/2026-09-13.md:17-39
- Raised by: Opus literature lanes; sources Deitmar–Hoffman 2004, Lubotzky ICM 2018, Hong–Kwon 2024, Kang–Yu 2026
- Status at last mention: dead route, settled in the literature
- Content: The vertex-level Ihara identity exists for *buildings* and only there (Kang–Li for the PGL_3 building; Fang–Li–Wang for Sp_4; Kang–Yu for PGL_n with the Euler factor derived as a graded determinant over the cochain complex, a torsion, crediting Hoffman 2003 for reading Bass's proof that way). The only general-triangulation object is Bénard–Chaubet–Dang–Schick's combinatorial Ruelle zeta: a polynomial, vanishing order b_1, torsion type, no RH. Storm's hypergraph zeta is just the Ihara zeta of the incidence bipartite graph at √u.
- Lead: do not look for a general-complex Ihara zeta; the building data (opposition, algebraic lengths) is what makes the identity and the RH exist.
- Related: L02-067, L02-070

### L02-067 Knill's graph torsion has never been joined to Ihara
- Source: docs/worklog/2026-09-13.md:40-48
- Raised by: Opus literature lane
- Status at last mention: raised, not pursued
- Content: Knill's graph torsion SDet(D) = Π det(D_k)^{(-1)^k} is an explicitly "fermionic versus bosonic" superdeterminant that has never been joined to the Ihara zeta. Related cohomological facts recorded: Deitmar 1995 (alternating product over Λ^l n, with vanishing order the degree-WEIGHTED supertrace -Σ p(-1)^p dim H^p, the plain Euler sum vanishing); Dyatlov–Zworski (order -χ at 0 on surfaces, ζ_R = ζ_1/ζ_0 ζ_2), the placement flipping with dimension; Matsuura–Ohta 2025 writing Bass's identity as a Berezin integral with a Dirac operator off-diagonal between vertex and edge fermions, the exponent E - V being an index (chirality, not Grassmann parity).
- Lead: joining Knill's torsion to Ihara would give a second, independent graded presentation of a graph zeta — exactly the kind of object the notebook wants. One paragraph of literature, never followed up.
- Related: L02-071, L02-073

### L02-068 Higher-rank RH is a one-sided band in the correct variable
- Source: docs/worklog/2026-09-13.md:29-34, 86-88 and 146-149
- Raised by: Lubetzky–Lubotzky–Parzanchevski / Kamber; confirmed by the prover; sharpened by the reviewer
- Status at last mention: registered, proved (prop:one-sided-rh-variable)
- Content: The higher Hashimoto operator is the geodesic flow on pointed cells; a Ramanujan complex gives a Ramanujan digraph, with poles at u = k^{-s} where |s| = 1 or Re s ≤ 1/2, and interior poles do occur (the reviewer sharpened the source's clause to 0 < |Re s| < 1/2). Kamber: L_p-expander iff |λ| ≤ q^{(p-1)/p}. So in higher rank "RH" is a one-sided band, not a circle.
- Lead: whenever a candidate gives a band rather than a circle, check whether the correct variable turns it into a circle.
- Related: L02-114, L02-126

### L02-069 Universal Bass–Schur identity for every complex and arbitrary weights
- Source: docs/worklog/2026-09-13.md:63-66 and 141-145
- Raised by: codex prover (T2.2); verified by the reviewer on 13 complexes including seven random ones
- Status at last mention: proved
- Content: det(I - zT_k) = det K_k(z) det(I - z R_k K_k^{-1} S_k) — a rational compression by one dimension, valid for every complex and arbitrary weights.
- Lead: the cheap half of "side B exists" in full generality; the analytic content is still the radius bound.
- Related: L02-006, L02-070

### L02-070 The vertex-level identity is a building phenomenon (∂Δ^3 counterexample)
- Source: docs/worklog/2026-09-13.md:60-68
- Raised by: codex prover (T0.3, T0.4, T2.4)
- Status at last mention: proved
- Content: The ordered rule "add a vertex not closing a cell" gives outdegree 2q^2 + q on the Ã_2 building, not Kang–Li's q^2 — the missing condition is OPPOSITION in the projective-plane link, a building notion; colour-2 edges are reversed colour-1 edges of algebraic length 2 (the u^2), and the unrestricted chamber flow is two reversal-transposed copies. The graded total over cell dimensions is D_B/D_E = (1-u^3)^χ/det P_3, the completed vertex L-function, not Kang–Li's Z = 1/D_E. On ∂Δ^3, T_1 = 0 and Z = (1 - u^4)^6, and no matrix polynomial P of any size gives (1-u^3)^χ/det P.
- Lead: dead end for generalising Kang–Li off buildings.
- Related: L02-066, L02-069

### L02-071 "Fermionic zeros" must mean net odd multiplicity after cancellation
- Source: docs/worklog/2026-09-13.md:68-71
- Raised by: codex prover (T3.1/T3.3)
- Status at last mention: registered
- Content: The superdeterminant form is exact, but on the building vertex side every chamber root cancels: the reduced vertex L-function is a reciprocal polynomial with no finite zeros. So "fermionic zeros" is net odd multiplicity *in a specified graded presentation*, to be checked after cancellation.
- Lead: the same trap later bit the graded Weil–LPS numerics — never quote a raw odd count as a genus.
- Related: L02-049, L02-125

### L02-072 There is no honest curve-weight dictionary for the chamber circles
- Source: docs/worklog/2026-09-13.md:71-76
- Raised by: codex prover (T3.4/T3.5, T4.2); the whole constituent table was verified character by character by the reviewer
- Status at last mention: registered (negative)
- Content: The k-cells ↔ H^{k-1} dictionary is parity only. The three chamber circles come from principal series (q^{-1/2}), tempered nonspherical constituents (q^{-1/2} and q^{-1/4} from the SAME constituent) and Steinberg twists (1), so there is no honest curve-weight dictionary. Also: no ordinary fermion determinant has parity = cell dimension, though a Berezinian with auxiliary copies exists.
- Lead: stop trying to read building zetas as curve zetas.
- Related: L02-071

### L02-073 The recommended object: a graded geodesic determinant with specified data
- Source: docs/worklog/2026-09-13.md:88-94 and 127-137
- Raised by: codex prover (T7.1)
- Status at last mention: recommended; uniqueness explicitly not claimed
- Content: Z = sdet(I - ⊕_k (-1)^{k+1} T_k^U(u))^{-1} over a complex with *specified* data (states, successors, algebraic lengths, transports; parity k+1). Ordered default for arbitrary complexes, pointed opposition data for buildings, voltage quotients for the Artin/quantum case. "Natural" means functorial under isomorphisms of that data.
- Lead: prove or disprove uniqueness of the object given the data — explicitly left open.
- Related: L02-066, L02-114

### L02-074 The genuine Artin block is the voltage quotient; covariant weights are pure gauge
- Source: docs/worklog/2026-09-13.md:81-86 and 115-119
- Raised by: codex prover (T5.5/T5.6); confirmed numerically and by the reviewer on Z/4, S_3 and Q_8 Cayley complexes
- Status at last mention: proved
- Content: Chronological weights π(s) are not flat; covariant weights on the FULL Cayley complex are pure gauge, det(I - u T^E) = det(I - uT)^{dim V}. The genuine Artin block is the voltage quotient: det(I - uT) = Π_ρ det(I - u T_ρ)^{dim ρ}, and the channel's block for π ⊗ π̄ is the product over its constituents with multiplicities. Euler-factor bookkeeping on the Ã_2 example: trivial block (1-u)^13 (1-u^3), 12-dimensional block (1-u^3)^64 with 64 = χ·12/|G|, the Z/3-stabiliser anomaly sitting entirely in the trivial block.
- Lead: a warning for quantum constructions — a twist that is pure gauge tells you nothing; every proposed twist must be checked against this.
- Related: L02-075, L02-118

### L02-075 Ramanujan complexes give Ramanujan quantum expanders automatically
- Source: docs/worklog/2026-09-13.md:110-119 and 133-137
- Raised by: Opus numerics lane plus codex prover
- Status at last mention: computed and registered
- Content: The 12-dimensional twist of the Ã_2 complex (permutation representation on PG(2,3) minus the constant) gives commuting, unital, trace-preserving Φ_1, Φ_2 with largest nontrivial |13μ| = 6.4817 < 2√12 = 6.9282 and all 143 joint eigenvalues inside the deltoid — a Ramanujan quantum expander of type Ã_2, automatically, since 13 spec Φ_1 ⊂ spec A_1. By Harrow's argument this holds for every representation and every Ramanujan complex, giving type Ã_{d-1}. Two surprises the brief did not anticipate: the LSV complex is NOT 3-colourable (so Kang–Li's type-preservation hypothesis fails) and all generators have order 3, so 24336 triangles carry a Z/3 stabiliser.
- Lead: a free supply of higher-rank quantum expanders exists; none has been connected to the Riemann side.
- Related: L02-008, L02-118

### L02-076 BC's state as the prescribed stationary state: the cone of arithmetic-covariant generators
- Source: docs/worklog/2026-09-13.md:163-208; report/sections/12_lab_log.tex:93-111
- Raised by: TJO (clarified the framing); computed by codex, no subagents or independent reviewers
- Status at last mention: registered, sketched/numerical, unreviewed
- Content: With the BC state prescribed as the stationary state of an unknown Lindbladian, and both the no-event generator and the jumps allowed to vary, the exact cone is a linear section of the conditional Choi positive cone. At the critical tracial extension I/p the real span dimensions are (p-1)(p+1)^2 for Galois covariance, 2p-2 for full linear Weil covariance, p+1 for additional Weyl+Galois covariance, and 1 for Weyl+Weil (depolarisation). The Weyl+Galois class already has real spectrum; Weyl translation covariance is an extra assumption, not a synonym for the requested symplectic structure. An explicit p = 7 GKLS generator built as a small scalar-orbit perturbation of depolarisation preserves I/p and all linear Weil/Galois symmetries but has two different odd decay rates. A two-prime reset construction shows that fixed local semigroups plus CRT marginal compatibility still leave a free coupling. Shear-conjugacy-class examples happened to have equal odd real parts at p = 3, 5, 7, so they could not serve as the counterexample.
- Lead: symmetry alone does not force equal odd decay rates — the p = 7 example is the counterexample, so the Ramanujan property needs an input beyond covariance.
- Related: L02-077, L02-100

### L02-077 The next missing input: an arithmetic map to the scattering bond
- Source: docs/worklog/2026-09-13.md:210-214
- Raised by: orchestrator/codex, stated as the next missing input
- Status at last mention: open
- Content: Verbatim: "The next missing input is an arithmetic representation or CP comparison map to the scattering bond that constrains the Kossakowski blocks and inter-prime couplings. The Gamma_0(N) scattering/character computation, prime powers, real place, metaplectic compatibility and critical adelic limit remain open. None was inferred from the finite calculations."
- Lead: five named open sub-items, each concrete. The Γ_0(N) scattering/character computation is the same one conj:galois-graded-bond needs.
- Related: L02-061, L02-076, L02-167

### L02-078 The coherent extension a·I + (r-a)P of the finite BC phase marginal
- Source: docs/worklog/2026-09-13.md:182-188
- Raised by: codex
- Status at last mention: registered, not explored
- Content: The finite BC phase marginal fixes diagonal probabilities only and is uniform at criticality. Away from criticality its diagonal extension fails full Weil invariance, but a coherent extension a·I + (r - a)P can be positive and Weil invariant, so ruling out the diagonal extension would not rule out the coherent one. Also: no finite-dimensional unital representation of the full BC algebra retains nontrivial phases, so these finite models cannot be presented as exact BC representations.
- Lead: the coherent extension is a live, unexplored option for the finite models.
- Related: L02-076

### L02-079 Ramanujan condition in Q and R for a boson–fermion cMPS
- Source: docs/worklog/2026-09-13.md:224-241
- Raised by: TJO
- Status at last mention: discussion only; "remains unreviewed and has not been promoted to new registered claims or a permanent evidence script"
- Content: The line condition should be imposed on an arithmetically identified invariant sector E; for a finite diagonalisable block A it is equivalent to A† G + G A = -2Δ G for some positive G. Qualification recorded: the earlier GKLS cone did not impose regular cMPS supercommutation relations. Output exported as outputs/ramanujan-boson-fermion-cmps.md.
- Lead: identify the invariant sector E arithmetically — that identification is the missing input.
- Related: L02-080, L02-114, L02-157

### L02-080 Regular two-fermion example: equal widths versus coercivity
- Source: docs/worklog/2026-09-13.md:235-241; revisited docs/worklog/2026-09-19.md:15-22
- Raised by: orchestrator (Claude); revisited by the 2026-09-19 review agents
- Status at last mention: exploratory, unregistered
- Content: A regular two-fermion cMPS has elementary odd modes at -κ/2 ± ig, while the full odd space also contains -3κ/2 ± ig. Regularity also gives zero instantaneous stationary-state Dirichlet form at R_f, which distinguishes the desired spectral statement from coercivity in a prescribed metric.
- Lead: the distinction "spectral statement versus coercivity in a prescribed metric" is the crux; the 2026-09-19 finding (physical correlation selecting four equal-width modes) is the follow-up.
- Related: L02-079, L02-157

### L02-081 The ring norm of a cMPS really is a supertrace (TJO's caution, then a proof)
- Source: docs/worklog/2026-09-13.md:254-281; report/sections/12_lab_log.tex:113-126
- Raised by: TJO — "I am very cautious about the ring norm being a supertrace for a cMPS: has this been proven?" plus "do not launch any subagents. Please work on this alone."
- Status at last mention: registered (shards 02f/04e/04f), sketched, no independent review
- Content: On arrival it was *not* proved — the book had only cited the lattice fMPS graded contraction (Bultinck et al.) and the graded cMPS matrix structure (Haegeman–Cirac–Osborne–Verstraete). Result: ⟨Ψ_B'|(-1)^F|Ψ_B⟩ = Tr[(B ⊗ B̄') exp(L T_η)] for arbitrary data; with a bond grading (-1)^F only maps B to PBP, so its expectation is ±1 for the natural boundaries; the supertrace over the doubled-bond grading P ⊗ P̄ is the norm of the ring closed with P (the periodic fermion ring), a positive sum of squares whose odd part is an interference term. Its Laplace transform in the ring length is str(z - T)^{-1} = d/dz log sdet(z - T), and Frullani gives the sdet ratio. Evidence: 89 checks including exact agreement of explicit Jordan–Wigner Fock vectors (6 sites, hard-core boson + two fermion species).
- Lead: recorded surprise — purely bosonic *reducible* bonds already have a nonzero odd sector (‖Ψ_+ - Ψ_-‖^2). Still unreviewed.
- Related: L02-049, L02-094

### L02-082 Two Lindblad papers: ‖Z(t)‖ = 1, so RH is not a worst-case mixing statement
- Source: docs/worklog/2026-09-14.md:3-20; report/sections/12_lab_log.tex:128-137
- Raised by: TJO — "two papers on lindblads landed today. Please dispatch opus subagents to read them carefully (tex source preferred always)... I believe they are both relevant for Ramanujan properties (which should have sth to do with mixing times) and cMPS."
- Status at last mention: unreviewed, not registered as a claim
- Content: Becker–Zworski (2609.13121, Witten Lindbladians in 1D) give sharp trace-norm relaxation at the gap on *regular* inputs but no uniform rate on trace class — "suggestive, one-sided; real rates only". Shang (2609.12284) gives worst-case mixing O(κ^2 log 1/ε) via absorption time, weakly relevant. Both readers independently concluded ‖Z(t)‖ = 1 for all t for the Riemann semigroup, so RH is not a worst-case mixing statement: any mixing form must live on regular data or weighted norms.
- Lead: a permanent constraint on how "Ramanujan = fast mixing" can be stated; it forced the regular-data formulation of the divisor.
- Related: L02-046, L02-116

### L02-083 Lubetzky–Peres cutoff on Ramanujan graphs
- Source: docs/worklog/2026-09-14.md:19-20
- Raised by: orchestrator (Claude) — "Recalled pointer... (unchecked)"
- Status at last mention: raised, not pursued, unchecked
- Content: Cutoff phenomena for random walks on Ramanujan graphs (Lubetzky–Peres) as the sharp mixing statement one might hope to transport.
- Lead: check it; if cutoff is the right form of "Ramanujan = mixing", it would say what the regular-data statement should look like.
- Related: L02-082, L02-122

### L02-084 The Weil numerator as a P-closed ring norm; genus ≥ 2 needs structure
- Source: docs/worklog/2026-09-14.md:22-30 and 47-54
- Raised by: TJO — "whether the numerator/denominator of an elliptic-curve zeta should be realised by boson–fermion MPS ring norms"
- Status at last mention: verified for genus 1 on four real elliptic curves; a genus-2 realisation found by least squares on C^{1|2}
- Content: Yes, via the P-closed (periodic fermion) ring: a minimal bond C^{1|1} realises N_n = |1 - α^n|^2 even with *bosonic* tensors — which is Hasse's deg(1 - φ^n). Cauchy–Schwarz gives |α| ≤ √q for free and the functional equation is the saturation case. The physical state is a product state and the count sits in the scalar 1 - α^n (ket) times its conjugate (bra). Circular unless the tensor comes from the curve; genus ≥ 2 needs fermionic species.
- Lead: "circular unless the tensor comes from the curve" is the standing requirement that launched the ring-norm-tensor campaign.
- Related: L02-085, L02-090, L02-093

### L02-085 TJO's five-point wish list for the ring-norm tensor
- Source: docs/worklog/2026-09-14.md:37-45; report/sections/12_lab_log.tex:139-155
- Raised by: TJO — "an educated guess for the MPS tensor for the absolute simplest case where the variety doesn't have an obvious Polya Hilbert hamiltonian"
- Status at last mention: answered (shards 02g, 06c-06f)
- Content: Five requirements: (1) a natural tensor from the variety data, (2) the graded decomposition and why, (3) a theorem that ring norms give the counts, (4) the Polya–Hilbert operator, (5) the Ramanujan property — all modulo MPS gauge.
- Lead: the cleanest statement in the notebook of what a successful construction must deliver; applicable verbatim to any future candidate.
- Related: L02-084, L02-086, L02-088

### L02-086 A Deligne-type surface (curve with coefficients / elliptic K3) as the next rung
- Source: docs/worklog/2026-09-14.md:59-62 and 110-112
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued — listed under "Open"
- Content: If TJO meant a Deligne-type surface rather than a curve, that is the next rung; note that for a surface the middle cohomology is *even* (bosonic) and the Ramanujan shape is the graph one (trivial eigenvalue q^2, nontrivial modulus q).
- Lead: a surface would test whether the grading story is really about parity or only about curves; the even middle cohomology makes it a genuinely different case.
- Related: L02-085, L02-092

### L02-087 The quadratic Artin–Schreier family is supersingular in every characteristic
- Source: docs/worklog/2026-09-14.md:73-77 and 104-107
- Raised by: codex prover (T0)
- Status at last mention: proved
- Content: Gauss sums plus eventual periodicity show the family is supersingular in every characteristic, so E_g/√q has finite order; the ring cut rank is D^2, not D; the amplitude-locality dichotomy survives only as a restricted conjecture, since cut rank is basis dependent (numerics lane). The broad slogan "finite tensors are supersingular" is FALSE.
- Lead: the notebook's "obvious Polya–Hilbert Hamiltonian" is degenerate, which is exactly why a non-supersingular example was needed.
- Related: L02-019, L02-091

### L02-088 Tier A: the lifted Frobenius as a toral endomorphism
- Source: docs/worklog/2026-09-14.md:78-84
- Raised by: codex prover
- Status at last mention: proved
- Content: N_n = det(1 - M^n) = |1 - π^n|^2 = |O/(π^n - 1)| — literally a ring norm; the count is a Lefschetz number. The ket bond is Λ^*(H^{1,0}) = C^{1|1}, the double is H^*(T^2), the grading is form degree, and (-,-) is H^2 with eigenvalue q = the degree. The Polya–Hilbert unitary is q^{-1/2} M^* on harmonic forms, unitary because the lift is a conformal similarity of degree q; Hasse's bound comes from the positive degree form; the gauge is GL_2(Z) change of lattice basis, with classes the ideal classes (Latimer–MacDuffee, Waterhouse). The Fourier pullback is an injection of index q, not a permutation, with the zero mode as its only finite orbit.
- Lead: "the Fourier pullback is not a permutation" kills any naive attempt to realise the count as a permutation orbit count.
- Related: L02-084, L02-089

### L02-089 No nonnegative automaton counts the points
- Source: docs/worklog/2026-09-14.md:85-86
- Raised by: codex prover, correcting the orchestrator's draft
- Status at last mention: proved
- Content: Base-π expansions have bounded cyclic carries (correcting the draft), the cyclic map need not be onto, and no nonnegative automaton counts the points.
- Lead: a second, independent no-go against a purely combinatorial/positive side B, complementing thm:no-ungraded-trace.
- Related: L02-004, L02-054

### L02-090 The genus bound: a false drafted inequality, and the correct one
- Source: docs/worklog/2026-09-14.md:87-93
- Raised by: orchestrator drafted it; refuted independently by the prover and by the numerics lane (173/400 random instances)
- Status at last mention: proved in corrected form
- Content: The drafted bound Σ_odd |μ|^2 ≤ 2 Tr(E_{++}) Tr(E_{--}) is FALSE, because Tr(A ⊗ conj A) = |Tr A|^2 (take a = B = diag(1,-1)). The genus bound g ≤ 1 for bosonic species is proved instead by |Tr M^n|^2 ≤ Tr(S_+^n) Tr(S_-^n) for all n plus a Cesàro argument. Euler bookkeeping: (m - k)^2 - (z_e - z_o) = 2 - 2g; minimal genus-two bond dimension is three; odd letters and cancellation evade the bound; an infinite-bond version forces fermionic jumps under explicit analytic hypotheses (Hilbert–Schmidt, not trace, constants).
- Lead: "odd letters and cancellation evade the bound" is the loophole any higher-genus or Riemann-side construction must exploit.
- Related: L02-054, L02-084, L02-091

### L02-091 Tier B genus two: a nine-letter tensor, Rosati as the PH metric, CM type as a marking
- Source: docs/worklog/2026-09-14.md:94-103
- Raised by: codex prover plus numerics lane
- Status at last mention: registered (shards 06c-06f), reviewed
- Content: The literal placement (trace line = q-eigenvector, vacuum invariant) and the drafted vacuum ansatz are impossible. What works: an explicit nine-letter tensor (depolarising even block + diagonal odd block, normal transfer) whenever q + 1 ≥ 4√q; and a two-even, one-odd tensor for y^2 = x^5 + x^3 + x^2 - 2 over F_5 certified by an exact rational contraction argument. The Jacobian is the bosonic product of two genus-one rings and the curve is a rank-six non-product boundary inside it. Rosati positivity forces conjugation at every CM place and gives the moduli and the PH metric; CM type is a marking, not a gauge. Numerics: the CM-diagonal ansatz (all even letters diagonal) with two odd letters solves genus two; one odd letter with a vacuum letter never does; no closed form is pinned by the counts.
- Lead: "no closed form is pinned by the counts" — the counts underdetermine the tensor, the same underdetermination later measured by the extension disc.
- Related: L02-090, L02-092, L02-160

### L02-092 Open items of the ring-norm-tensor campaign
- Source: docs/worklog/2026-09-14.md:109-112
- Raised by: orchestrator (Claude)
- Status at last mention: open, verbatim list
- Content: "Universal three-letter tensor and a natural selection of its entries; bosonic realisations with cancellation on larger bonds; whether the certified tensor's unitary similarity is an even ket gauge carrying the Hodge metric; the Deligne-type surface as the next rung; any lifted Riemann dynamics." Assessment observations from the same campaign: the candidate Riemann bond is C ⊕ H_{>0}; ket/bra exchange is conjugation, not the functional equation; fermionic jumps are necessary in the stated setting; the toral example gives no general "permutation" principle.
- Lead: five named open items; "any lifted Riemann dynamics" is the one that would matter most, since the Tier A lift has no Riemann analogue.
- Related: L02-086, L02-088, L02-091

### L02-093 Reviewer MAJOR items: cut rank bounded by 4; split the norm identity
- Source: docs/worklog/2026-09-14.md:114-124
- Raised by: Opus reviewer (stance REFUTE)
- Status at last mention: applied in the shards
- Content: MAJ-1: the cut-rank boundedness question is not open — it is bounded by 4 in a self-dual normal basis by a one-line nearest-neighbour argument. MAJ-2: the finite-bond norm identity must be split into its algebraic half (a two-line theorem) and its physical Fock-space half, which is only sketched in shard 04f. The reviewer also noted that q + 1 ≥ 2g√q is exactly nonnegativity of the Weil lower bound on N_1, and the optimal split for that ansatz.
- Lead: the physical Fock-space half of the norm identity is still only sketched — a real gap.
- Related: L02-081, L02-091

### L02-094 One explicit MPS per genus, with entanglement and parent Hamiltonians
- Source: docs/worklog/2026-09-14.md:126-149; report/sections/12_lab_log.tex:157-162
- Raised by: TJO — "how hard is it to describe a specific example of each genus, write down the actual matrices for the corresponding MPS?" and then "works out some usual entanglement properties etc., and also parent Hamiltonian"
- Status at last mention: registered (shard 06g), sketched/numerical, unreviewed
- Content: Genus 0 (P^1/F_5): bond C^2, letters ∞ and F_5, a cat state of two product states. Genus 1 (y^2 = x^3 + x + 1 / F_5): one letter diag(1, π), a product state. Genus 2: the certified letters over F_5 and a nine-letter closed form over F_25. Genus 3 (y^2 = x^7 + x + 1 / F_37, counts 41, 1455, 50915): the closed form on C^{1|3} with 16 letters. Every genus needs only the L-polynomial; the closed form needs q + 1 ≥ 2g√q. Correlation lengths: 1/log q even, 2/log q for every odd mode — "that IS RH". Entanglement: block Schmidt spectrum from a D^2 × D^2 matrix built from E^l and E^{n-l} Γ; entropy ≤ 2 log D; genus 0 gives H(1/(1+q^n)), genus 1 zero, genus 2 certified 1.6636, closed forms exactly log 8 and log 12 with a flat spectrum from the depolarising letters. Parent Hamiltonians: injectivity at k = 2 (certified) or k = 1 (closed forms); ring ground spaces unique (genus 0 two-fold, GHZ-like); Ψ_P is a ground state exactly of the parent Hamiltonian with parity-twisted wrapping terms, the antiperiodic ring of the untwisted one.
- Lead: "correlation length 2/log q for every odd mode IS RH" is the cleanest physical restatement of RH in the notebook — worth carrying to the continuum.
- Related: L02-114, L02-081

### L02-095 Back to basics: the permutation (1 2)(3 4 5) as gas, oscillators, and one-matrix MPS
- Source: docs/worklog/2026-09-14.md:151-176; report/sections/12_lab_log.tex:165-180
- Raised by: TJO — "I want to go right back to basics. Let us consider a permutation, e.g. (1 2)(3 4 5)", then "this seems important. please record it durably, also in the lab book"
- Status at last mention: registered (shard 03b), sketched/numerical, unreviewed
- Content: The point-letter ring norm is the number of periodic points Λ_σ(n) — the weight "log p" is the number of starting points on the prime ring. The gas of rings is the Fock space of one oscillator per cycle by unique factorisation, H = 2N_2 + 3N_3, ζ = Tr e^{-βH}; the same number is the twisted Fock trace Tr u^N Γ(P) over the five-oscillator bond space (fixed monomials = gas configurations); the square-root-weight vector is a product state whose norm is ζ, Gibbs only on the diagonal algebra (the full Gibbs state needs the ket/bra doubling).
- Lead: the notebook's minimal working model, and the base case for the extension-disc computation.
- Related: L02-096, L02-098, L02-161

### L02-096 Grading the 3-cycle odd: zeros from boundary conditions, and a holonomy that moves them
- Source: docs/worklog/2026-09-14.md:164-168
- Raised by: TJO's second question
- Status at last mention: registered (shard 03b)
- Content: With Ramond (periodic-fermion) closure, str P^n = 2[2|n] - 3[3|n] and ζ = (1 - u^3)/(1 - u^2): zeros at the primitive cube roots, and the pole at u = 1 is eaten by the odd fixed vector — "rigidity in miniature". A holonomy on the odd cycle moves the zeros (h = -1 keeps the pole). Untwisted closure has no zeros at all.
- Lead: boundary conditions and holonomy are the two dials that create and move zeros in the smallest possible example; both are unexplored on larger objects.
- Related: L02-049, L02-095, L02-097

### L02-097 Fermionic primes: 1 - u^l per prime; all-fermionic gives 1/ζ and Möbius as fermion parity
- Source: docs/worklog/2026-09-14.md:167-168; corrected at docs/worklog/2026-09-14.md:219-220
- Raised by: orchestrator (Claude); corrected by the astra lanes
- Status at last mention: registered with a correction
- Content: A fermionic prime is a two-level system contributing 1 - u^l for every length l; if all primes are fermionic the zeta is 1/ζ, the Möbius function is fermion parity, and the "zeros" sit on Re s = 0. Correction from the yolo lanes: "fermionic primes: zeros on Re s = 0" holds per finite factor only.
- Lead: a fully fermionic gas gives the wrong line, so the grading cannot simply be "all primes odd".
- Related: L02-096, L02-103

### L02-098 The letters principle: physical dimension between the Kraus rank and the grading
- Source: docs/worklog/2026-09-14.md:169-174
- Raised by: TJO's third question — what principle fixes the number of physical letters?
- Status at last mention: registered (shard 03b)
- Content: With point letters the Ramond *norm* is still Tr P^n (the signs square); the sign lives only in the even–odd coherences of the doubled bond. The ladder at n = 6 is: one letter (2·3)^2 = 1; one letter per cycle 2^2 + 3^2 = 13; one letter per point 5. Principle: physical dimension ≥ Kraus rank of the transfer channel (the minimal choice canonical up to a unitary, the zeta blind above it), and letters must be *coarser* than the grading. 0/1 letters force one letter; weighted letters (√q, phases) allow several.
- Lead: a selection rule for any future construction — it says how much physical detail is meaningful.
- Related: L02-095, L02-100, L02-127

### L02-099 A parity jump shifts every odd eigenvalue uniformly
- Source: docs/worklog/2026-09-14.md:175-176; docs/worklog/2026-09-15.md:102-106
- Raised by: orchestrator (Claude), checked on a random graded Lindbladian
- Status at last mention: registered (prop:parity-jump-uniform-shift)
- Content: A parity jump √γ Π shifts every odd eigenvalue by -2γ and no even one — the letter-level form of the uniform-rate statement. The prover later identified this same P as the even letter that breaks odd-sector Alon–Boppana.
- Lead: the only known *mechanism* producing a uniform odd rate from a letter, hence the natural candidate for how a Riemann Lindbladian would put all zeros on one line.
- Related: L02-100, L02-118, L02-119

### L02-100 obs:jump-operator-guidance — prime jumps + Galois dephasing + an even–odd Hamiltonian
- Source: docs/worklog/2026-09-14.md:177-184
- Raised by: TJO's follow-up question, mid-recording: prime jumps versus Bost–Connes symmetry jumps for the Riemann cMPS
- Status at last mention: registered as an observation, sketched
- Content: Jumps matter only through the Lindbladian. Galois jumps are character-diagonal, hence character dephasing = the uniform rate (e^{-t/4}), producing no frequencies, and as a full per-step average they are a character measurement that kills the zeros. Prime jumps act on every character sector and carry the lengths (the record) but alone give a real spectrum. The grading must be *transverse* to the primes. The frequencies need an even–odd Hamiltonian that neither family supplies. Ansatz shape: prime jumps + Galois dephasing at 2γ = 1/4 + an even–odd Hamiltonian.
- Lead: the most explicit shape ever written for the Riemann Lindbladian, with the missing piece named (an even–odd Hamiltonian). Later corrected: Galois-diagonal jumps DO produce frequencies when the rates are inversion-asymmetric.
- Related: L02-099, L02-101, L02-103

### L02-101 The yolo Lindbladian guess
- Source: docs/worklog/2026-09-14.md:189-205; report/sections/12_lab_log.tex:182-195
- Raised by: TJO — "Can we yolo guess the right lindblad given the circumstantial info we have found in this project so far?" then "dispatch two super smart codex astra xhighs to investigate this"
- Status at last mention: pursued, clean negative (shard 04g)
- Content: The guess: bond L^2(Ẑ) ⊗ L^2(R_+^*); grading by the profinite Fourier mode (constant function = the critical KMS state on the phases, even; nonconstant, odd); one prime jump per prime, V_p = multiplication by p (a Galois unit away from p, the shift at p, the Shor map on finite levels) at rate 1/p; Galois dephasing at 1/4; an archimedean Γ ladder and a dilation Hamiltonian.
- Lead: see the audit outcome below for what held and what failed.
- Related: L02-100, L02-102, L02-103

### L02-102 The Ramanujan-sum sector as the candidate identification of K_S (item 0b')
- Source: docs/worklog/2026-09-14.md:198-200 and 222-226
- Raised by: orchestrator (Claude)
- Status at last mention: partially ruled out — "0b' stays open; the Ramanujan-sum sector with prime jumps alone is ruled out as the K_S identification"
- Content: Using c_b(1) = μ(b) and Σ_b c_b(n) b^{-s} = σ_{1-s}(n)/ζ(s), the Ramanujan-sum sector was proposed as the identification of K_S.
- Lead: only the "with prime jumps alone" version is dead; the sector itself is still a candidate. Identifying K_S arithmetically remains the first obstacle to conj:phantasm-both-halves.
- Related: L02-058, L02-103, L02-167

### L02-103 The yolo audit: what held and what failed (exact negatives)
- Source: docs/worklog/2026-09-14.md:206-220
- Raised by: two codex gpt-6-astra xhigh lanes (896 and 1351 lines / checks), re-run by the orchestrator
- Status at last mention: registered (shard 04g), sketched/numerical, no Opus review yet
- Content: Holds: V_p isometries, Galois covariance, Ramanujan-shell formulas (the vacuum leaks into shell p), the Gauss-vector eigenrelation at good primes, ⟨c_b⟩_β → 0 iff b > 1, Haar as a vector state of e_0 (mixed on C(Ẑ)), uniform Galois dephasing, and exactly ⟨v, Π (1 - p^{-w} V_p) v⟩ = 1/ζ(w + 1/2). Fails: the grading is not preserved ([L, Γ_b] ≠ 0 for every prime); vacuum–character coherences are not modes (an extra 1/p, residual 0.61); the vacuum generating functions are exactly 1/(1 - S_P(s + β + 1)) and ζ_P(s + β + 1) — shifted, with no singularity in the strip at any cutoff (zeros only via continuation of the scalar); shell Gibbs weights are not stationary (an exact 2×2 counterexample: the ratio must be p^β and coherences still appear); rates 1/p give no normal semigroup (vacuum survival → 0 at any t > 0); the parity ring trace is not a trace at a prime cutoff; parity closure is not the Q^× quotient (2-dimensional counterexample); Connes 1999 supplies local/finite-place cutoff formulas only.
- Lead: "The phase-side prime jumps are side A again (the Euler product), with the Fourier side included this time" — adding the Fourier dual does not escape the side-A trap.
- Related: L02-020, L02-100, L02-101, L02-104

### L02-104 Next if pursued: an Opus review of shard 04g, and a summable-rate / radial local model
- Source: docs/worklog/2026-09-14.md:223-226
- Raised by: orchestrator and the codex lanes themselves
- Status at last mention: raised, not pursued
- Content: Two named next steps: an Opus REFUTE review of shard 04g (still not done), and the lanes' own suggestion — "a summable-rate or radial local model with a genuine bond cutoff before asking for a metric".
- Lead: the summable-rate variant directly addresses the "rates 1/p give no normal semigroup" failure.
- Related: L02-103, L02-168

### L02-105 Line up the zeta conditions and impose them factor by factor
- Source: docs/worklog/2026-09-14.md:228-243; report/sections/12_lab_log.tex:197-210
- Raised by: TJO — "line up all the conditions we want a zeta to obey: functional equation, rh/ramanujan, unique fixed point etc etc and try to impose them factor by factor on the cMPS ring norm ... include tiny L functions ... completely concrete MPS/cMPS that any practitioner would understand"
- Status at last mention: registered (shard 06h)
- Content: Ten conditions C1–C10 written as exact algebra on (A_s, Π) and on (Q, R); a catalogue of 13 explicit constructions with every matrix printed; 461 checks re-run by the orchestrator; a D1–D8 correction ledger.
- Lead: the complementary strategy to guessing the whole object — build the conditions up one at a time. It produced the independence result and the finite-bond limits.
- Related: L02-101, L02-106, L02-112

### L02-106 The simplest nontrivial zeta with a pole and a zero: the pair shift
- Source: docs/worklog/2026-09-14.md:233-237
- Raised by: TJO's question — "simplest nontrivial zeta with a couple of poles and zeros"
- Status at last mention: registered
- Content: The pair shift on m^2 letters with the diagonal graded odd, letters diag(1, [a = b]) on C^{1|1}: Z = (1 - mu)/(1 - m^2 u), N_n = m^{2n} - m^n, RH by half entropy, a genuine gas, no functional equation. For m = 2 it is the ratio of the affine-line zetas over F_4 and F_2.
- Lead: the minimal example in which a *numerator* appears; everything about the grading can be tested on it in two lines.
- Related: L02-095, L02-105

### L02-107 Four-letter trace-preserving elliptic tensors on C^{1|1}
- Source: docs/worklog/2026-09-14.md:244-249
- Raised by: codex lane (zeta-conditions)
- Status at last mention: registered (shard 06h)
- Content: A_0 = diag(√t, π/√t), A_1 = diag(0, √(t - q/t)), A_2 = √h |0⟩⟨1|, A_3 = √h |1⟩⟨0| with t = (q+r)/2, h = (q-r)/2: even spectrum {q, r}, odd {π, π̄}; functional equation via J = diag(1,-1)_even ⊕ swap_odd (J E J^{-1} = q E^{-1}; the orchestrator's first J was wrong and was corrected in the script); RH via E_-^† E_- = q; a unique maximally mixed fixed point; mixing. Affine (r = 0) and projective (r = 1) versions; the supersingular y^2 + y = x^3 over F_4 has a real double zero.
- Lead: the first tensor in the notebook satisfying *all* the conditions at once — the template for what a Riemann-side tensor would have to look like.
- Related: L02-106, L02-114, L02-117

### L02-108 FE, RH and mixing are independent conditions
- Source: docs/worklog/2026-09-14.md:250-251
- Raised by: codex lane
- Status at last mention: registered
- Content: With Pauli letters (even {16, r}, odd {x, y}) all combinations of FE / RH / mixing are realisable except FE = N with RH = Y and the exact projective pair; an idle qubit kills uniqueness of the fixed point.
- Lead: no free lunch — no condition implies another, so each must be imposed by a separate structural input.
- Related: L02-105, L02-111

### L02-109 Tiny L-functions from Horner MPS
- Source: docs/worklog/2026-09-14.md:252-256
- Raised by: TJO's instruction to include tiny L-functions; realised by the codex lane
- Status at last mention: registered
- Content: Horner MPS: bond F_q[x]/M, letters f ↦ xf + c, with a character closing row. Over F_2 mod x^3 + x + 1 this gives (1-u)(1 - αu) with |α|^2 = 2; over F_3 mod x^2 + 1, 1 - αu with |α|^2 = 3 (odd characters). Also Gauss 1 + Gu; Kloosterman 1 + 3u + 4u^2 over F_4 as the affine count of y^2 + xy = x^3 + 1; a rose with Z/2 voltages giving Artin factors with poles and reduced Bass quadratics reciprocal at q = 3. Caveat: these are *amplitudes*, not norms, and closing the automaton into a trace is wrong.
- Lead: the amplitude/norm distinction is a trap worth remembering — Dirichlet L-functions appear as amplitudes, while the ring-norm formalism wants norms.
- Related: L02-061, L02-105

### L02-110 cMPS instances: half entropy and an amplitude-damping additive functional equation
- Source: docs/worklog/2026-09-14.md:257-258
- Raised by: codex lane
- Status at last mention: registered
- Content: Half entropy: Q = 1/2, R = diag(1,0) gives (z-1)/(z-2). Amplitude damping: R = √2 |0⟩⟨1|, H = diag(0,1) gives even {0, -2}, odd {-1 ± i}, N(L) = |1 - e^{(1+i)L}|^2, and an *additive* functional equation Z(2 - z) = Z(z).
- Lead: the first continuum example with a functional equation of the additive (Riemann) type rather than the multiplicative (curve) type.
- Related: L02-107, L02-114

### L02-111 Three corrections from the zeta-conditions lane
- Source: docs/worklog/2026-09-14.md:259-263
- Raised by: codex lane, correcting the orchestrator
- Status at last mention: applied
- Content: (a) Inverse-closed letters do not give the functional equation for the raw doubled transfer (diag(1,2) counterexample); the mechanism lives in the non-backtracking construction. (b) The swap L-function of the pair shift is not an Artin factor — a *directed* voltage cover is. (c) "Unique fixed point" is three separate conditions: a simple Perron root, a whole-bond TP gauge, and mixing. (d) The affine rung needs its own tensor.
- Lead: (a) says the functional equation is a property of the Hashimoto / non-backtracking lift, not of the letters — which is exactly what the later finite Hashimoto-lift theorem formalises.
- Related: L02-108, L02-136

### L02-112 What a finite bond can never do
- Source: docs/worklog/2026-09-14.md:264-266
- Raised by: codex lane
- Status at last mention: registered (limits)
- Content: A finite bond can carry infinitely many Euler primes, but never a nonrational Z, never an atomic prime comb, and never infinitely many distinct divisor points; and a single simple pole is incompatible with the uncompleted self-reciprocal functional equation.
- Lead: a hard dimension count — the Riemann object must have an infinite bond, and the functional equation must be the completed one.
- Related: L02-105, L02-116

### L02-113 TJO's quest item: what IS the Ramanujan property in the graded case?
- Source: docs/worklog/2026-09-15.md:3-19
- Raised by: TJO — "I am increasingly interested in the Ramanujan property for cMPS/Lindblads ... even here I am not sure in the graded case if we really understand the Ramanujan property yet. Do we? My feeling is we only have quantum expanders for ungraded bond space/antiperiodic BCs. Can that be. Please work alone."
- Status at last mention: answered; TJO's feeling was correct
- Content: Yes: every quantum expander in the literature and in the book lives on an *ungraded* bond, its ring zeta has only poles, and on an ungraded bond the periodic and antiperiodic closures coincide (prop:no-ungraded-zeros). Zeros need a grading and the periodic closure; they are the eigenvalues on the odd sector (parity coherences) of the doubled bond.
- Lead: a clean statement of why the existing expander literature cannot contain the sought object.
- Related: L02-114, L02-118

### L02-114 The definition of the graded Ramanujan property
- Source: docs/worklog/2026-09-15.md:21-32
- Raised by: orchestrator (Claude), then audited by the codex prover
- Status at last mention: registered (def:graded-transfer-channel, def:graded-rh-fe-ramanujan, shard 02h), sketched
- Content: Everything is stated on the divisor ν = m_even - m_odd of the periodic ring zeta 1/sdet(1 - uE): growth q = the Perron root; a trivial set {q, its period images, 1, FE partners}; critical circle |λ| = √q, or the line Re z = ω/2 for generators. RH = one-sided square-root cancellation; FE = an even similarity J E J^{-1} = q E^{-1}; Ramanujan = both; the manifest (Hilbert–Pólya) form is a Γ_b-even positive form making E/√q unitary on the nontrivial sectors. It is stated on the *ring norms* so it passes to the continuum verbatim (e^{εT} has the same ring norms for every ε, prop:graded-continuum-exact).
- Lead: this is the notebook's target definition; the whole 2026-09-16 Selberg campaign is the attempt to satisfy it on an infinite object.
- Related: L02-113, L02-115, L02-130

### L02-115 Graded Chernoff: parity-changing dynamics is dissipative in the continuum
- Source: docs/worklog/2026-09-15.md:28-30 and 120-124
- Raised by: orchestrator (Claude); refined by the prover (D7, D8)
- Status at last mention: registered (prop:graded-chernoff)
- Content: In a genuine Chernoff limit the grading survives only in the jump operators, because an odd letter is never close to the identity. The prover's refinement: at fixed finite bond the odd Kraus letters are collectively O(√ε) by a Choi odd-block estimate; individual limits need a Kraus gauge; a homogeneous GKSL presentation exists via a canonical noise basis. Also: exactness needs non-aliasing meshes — at ε = 1 a CP example's lattice divisor cancels completely while str e^{LT} does not vanish between samples.
- Lead: this dictates where the grading can live in a continuous-time model: in the dissipator, never in the Hamiltonian part alone.
- Related: L02-099, L02-114

### L02-116 For infinite bonds the divisor must be defined from regular data
- Source: docs/worklog/2026-09-15.md:30-32
- Raised by: orchestrator (Claude)
- Status at last mention: registered (obs:divisor-regular-data)
- Content: For infinite bonds the divisor is defined from correlation functions of *regular data*, not from the L^2 spectrum — because ‖Z(t)‖ = 1 (the previous day's negative).
- Lead: any infinite-dimensional statement must specify its class of regular data; this is the formal echo of the Riesz-basis obstruction.
- Related: L02-046, L02-082, L02-135

### L02-117 The P-mode is structural, not trivial
- Source: docs/worklog/2026-09-15.md:34-38 and 110-116
- Raised by: orchestrator (Claude), self-corrected before the prover lane; framing further corrected by the prover
- Status at last mention: registered
- Content: The first draft put the P-mode (E(P) = r_P P under the parity-twisted identity Σ ε_s A_s A_s^† = r_P 1, a new identity the 06h elliptic tensor satisfies with r_P = 1) into the trivial set. Wrong: for the Pauli letters r_P = -2 lies inside the band and contributes a pole pair on the critical circle. So the P-mode is structural, and for unitary letters Ramanujan imposes a *balance condition on the letters*. The prover later corrected the framing: Σ ε_s A_s A_s^† = r·1 is signed *unitality* in the map convention, not trace preservation.
- Lead: "Ramanujan imposes a balance condition on the letters" is precisely the letter-level mechanism the 2026-09-16 campaign then sought on an infinite object.
- Related: L02-107, L02-127, L02-130

### L02-118 thm:graded-harrow — graded quantum expanders exist, from index-two subgroups
- Source: docs/worklog/2026-09-15.md:40-46
- Raised by: orchestrator (Claude)
- Status at last mention: registered (corrected by the prover), sketched
- Content: An irreducible representation induced from an index-two subgroup is graded by coset parity (Clifford theory); Ad(P) is an intertwiner splitting End(V) into the two sectors; the trivial and sign representations both sit in the even sector (the fixed point and the P-mode); every other constituent obeys Harrow's bound; and the graded quantum Ihara–Bass identity (thm:graded-qihara-bass, sector by sector, with (1-u^2) exponents n_k(D-2)/2 that cancel for balanced gradings) puts the odd edge eigenvalues on |μ| = √q — zeros on the critical circle.
- Lead: the first *mechanism* producing zeros on the critical circle from group data; index-two gradings are the supply of examples.
- Related: L02-113, L02-119, L02-121

### L02-119 REFUTED: there is no odd-sector Alon–Boppana bound
- Source: docs/worklog/2026-09-15.md:46-48 and 102-106
- Raised by: orchestrator proposed prop:graded-alon-boppana; REFUTED by the codex prover (D5)
- Status at last mention: refuted; recorded as obs:odd-gap-no-alon-boppana
- Content: (1/4)(2 Ad 1 + 2 Ad P) has Φ_odd = 0 on every C^{m|m}, and primitive degree-16 families with ρ(Φ_odd) = 0 exist. Hastings' lower-bound argument needs nonnegative word traces, which fail on the odd sector. The even letter P is precisely the parity jump of prop:parity-jump-uniform-shift. So "Ramanujan" for the odd sector is a band (an upper bound), not an optimality statement.
- Lead: do not expect the odd gap to be optimal — the odd sector can be arbitrarily good, which is a freedom rather than an obstruction.
- Related: L02-099, L02-118, L02-126

### L02-120 A qubit with Pauli letters counts the points of an elliptic curve over F_5
- Source: docs/worklog/2026-09-15.md:51-54
- Raised by: orchestrator (Claude), numerics
- Status at last mention: registered (prop:qubit-graded-zeta), numerical
- Content: Pauli letters X, X, Y, Y, Z, Z on C^{1|1} with P = Z give even {6, -2} and odd {-2, -2}; the graded quantum Ihara zeta is (1 + 2u + 5u^2)/((1-u)(1-5u)) and str T^n = 8, 32, 104, 640, 3208, 15392 are the point counts of y^2 = x^3 + 4x + b over F_5.
- Lead: the smallest possible statement of the whole programme — "a qubit with Pauli letters counts the points of an elliptic curve".
- Related: L02-107, L02-118, L02-128

### L02-121 Graded Weil–LPS: both sectors, character formulas, and an odd extremal Hecke eigenvalue
- Source: docs/worklog/2026-09-15.md:56-65
- Raised by: orchestrator (Claude), numerics
- Status at last mention: registered, numerical
- Content: PGL_2(F_p) principal series I(χ, χ^{-1}) with χ of order 4 (splits on PSL_2; P obtained from the commutant by exact group averaging), LPS generators of norm q with (q/p) = -1, all in the odd coset. For (5;13) and (13;5) both sectors sit in the band, the P-mode is -(q+1), Harrow containment holds, and the character formulas are Tr = Σ |χ_π(w)|^2 and str = Σ |χ_+ - χ_-|^2 on words; graded Ihara–Bass holds on both sectors of the 504- and 1176-dimensional Hashimoto operators. In the (13;5) case the *extremal Hecke eigenvalue is odd*. A bug was found in the orchestrator's own script: sectors read off the diagonal of Γ_b are valid only when P is diagonal, so the representation is now rotated into the P-eigenbasis first.
- Lead: "the extremal Hecke eigenvalue is odd" ties the graded structure to arithmetic extremality — worth checking on more pairs.
- Related: L02-023, L02-118, L02-125, L02-165

### L02-122 Harrow's continuum limit is temperedness
- Source: docs/worklog/2026-09-15.md:67-71 and 125-128
- Raised by: orchestrator (Claude); sharpened by the prover (D11)
- Status at last mention: registered (obs:continuous-harrow-tempered)
- Content: For the representation Lindbladian (1/2d) Σ B_j^2, Ramanujan = temperedness of π ⊗ π̄ (Fell absorption), with gap 1/2 as the tempered threshold, no normalisable fixed point and no discrete divisor; at edge level the statement is about the matrix-coefficient exponents -s, -(1-s) of the flow on the constituents. The prover's refinement: the equally averaged two-generator walk has threshold 1/4 while T_* of shard 09b has 1/2, sharp for every D_k; for PSL_2(R) representations the type-zero bound -T_* ≥ 1/2 is EQUIVALENT to temperedness — "the diffusion meaning of continuous Ramanujan"; discrete series are tempered with faster exponents; discrete and continuous constituents coexist.
- Lead: gives the continuum meaning of Ramanujan (temperedness) independently of any zeta, and it is the right target for the Riemann-side bond.
- Related: L02-114, L02-123

### L02-123 The reflection grading puts the Selberg zeros in the EVEN sector
- Source: docs/worklog/2026-09-15.md:71-76 and 129-133; corrected again at docs/worklog/2026-09-16.md:57-58
- Raised by: orchestrator (Claude); corrected by the prover (D12, D8)
- Status at last mention: registered as obs:selberg-grading-choice, then corrected
- Content: For PGL_2(R) > PSL_2(R) the induced irreducibles are the discrete-series pairs D_k^+ ⊕ D_k^-, the odd letter is the reflection jump, the odd sector D_k ⊗ D_k = Σ D_{2k+2m} is the archimedean ladder, and the even sector carries the critical continuum and the closed geodesics (the supertrace sees only elliptic classes). So the *reflection* grading assigns the zeros to the EVEN sector — the wrong place; the grading that makes Selberg zeros odd is the transverse form-degree grading of Dyatlov–Zworski. Prover refinements: genuine PGL_2(R) pairs need k ≥ 2 even (k = 1 needs a cover); exact odd rates κ(n + 2nj + 2j^2) + 2γ with odd minimum 2κk; P is a bounded but not Hilbert–Schmidt eigenoperator (no HS divisor point); the heat supertrace needs regularisation, and the localised regular-character functional vanishes on hyperbolic elements (χ_+ = χ_- there), so the geodesics are even; the Γ-ladder match is positional only. Later still: K-type parity makes X odd but is not a flow grading, is not the Hodge grading, and does not supercancel (theta factor > 0).
- Lead: the choice of grading is not free; only the transverse/form-degree one works, which is why the 2026-09-16 campaign built a two-term transverse complex.
- Related: L02-131, L02-137

### L02-124 Unverified: the complementary-series threshold 3/4 versus Selberg's 3/16
- Source: docs/worklog/2026-09-15.md:77-78 and 128
- Raised by: orchestrator (Claude), "from memory"
- Status at last mention: flagged, unverified; H-repka "stays unverified"
- Content: The complementary-series threshold s = 3/4 (attributed to Repka, from memory) against Selberg's 3/16 = (3/4)(1/4).
- Lead: verify H-repka against a source; a small piece of bookkeeping propping up a threshold comparison.
- Related: L02-122

### L02-125 L07: only the NET divisor survives in the graded Weil–LPS zetas
- Source: docs/worklog/2026-09-15.md:96-101
- Raised by: codex prover's independent audit, correcting the orchestrator
- Status at last mention: corrected and applied
- Content: The graded Weil–LPS zetas are not P(u) over four trivial factors with deg P = 36/196. Even and odd sectors *share* eigenvalues, and only the net divisor survives: (5;13) reduces to (1 - 4u + 13u^2)(1 + 4u + 13u^2)/[(1-u)(1-13u)(1+u)(1+13u)] — 16 cancelled pairs, no nontrivial poles; (13;5) has reduced degrees 144/144 with 140 nontrivial pole factors on the circle. The orchestrator's script had printed the raw odd count as a "genus"; it now prints the net divisor.
- Lead: the same trap as T3.1/T3.3 on complexes — always reduce before interpreting.
- Related: L02-071, L02-121

### L02-126 D4: the band and the circle differ without a no-cancellation hypothesis
- Source: docs/worklog/2026-09-15.md:107-109
- Raised by: codex prover
- Status at last mention: corrected
- Content: The band condition holds iff the circle condition holds for the retained NET divisor; bounds on both sectors imply it, but the converse fails without a no-cancellation hypothesis — a primitive degree-14 example with even {14, 10} and odd {10, 6} has a hidden mode 10 outside the band.
- Lead: any "Ramanujan" claim must state whether it is about the sectors or the net divisor.
- Related: L02-114, L02-125

### L02-127 Definition corrections: signed trivial divisor, a pair of reference rates, CP versus spectral transfer
- Source: docs/worklog/2026-09-15.md:110-116
- Raised by: codex prover
- Status at last mention: applied to shard 02h
- Content: (a) The trivial set must be a *signed divisor* with multiplicities and parities, since period modes can be odd — (Ad Z + Ad Y)/2 graded by Z has the odd mode X at -1. (b) The continuum needs a PAIR of reference rates: a trace-preserving spectral bound is 0 and does not determine the critical line (amplitude damping has centre -γ/2). (c) "Graded CP transfer" must be distinguished from "graded spectral transfer": Artin–Schreier, Riemann and Selberg have no supplied Kraus realisation; a doubled bond always has n_0 - n_1 = (D_+ - D_-)^2 ≥ 0, whereas a cohomological grading may have more odd than even.
- Lead: (c) is the central structural gap of the whole notebook — the arithmetic objects are spectral, not CP — and (b) says the critical line is not determined without extra data.
- Related: L02-055, L02-114, L02-134

### L02-128 D13: numerators need not be integral, and integral Weil need not be a curve
- Source: docs/worklog/2026-09-15.md:134-136
- Raised by: codex prover
- Status at last mention: registered
- Content: The exact qubit formula has α = Σ_even a_i conj(d_i), β = Σ_odd a_i conj(d_i), with odd eigenvalues α ± |β|. Numerators are generally non-integral (a Ramanujan example with N_P(1) = 16/3), need not be Weil, and an integral Weil numerator need not come from a curve ((1-3u)^4 over F_9).
- Lead: integrality is an extra arithmetic condition the channel formalism does not supply — a missing constraint if one wants curves rather than merely Weil-shaped zetas.
- Related: L02-120, L02-114

### L02-129 D6 and the bipartite / Artin-factor corrections; a shard-05 wording error
- Source: docs/worklog/2026-09-15.md:117-119 and 137-138
- Raised by: codex prover
- Status at last mention: applied
- Content: Bipartite Cayley graphs give period-two (not mixing) graded expanders; the qubit is an ordinary representation of the Pauli group (G_0 = ⟨iI, Z⟩) and projective only on the abelian quotient; Artin factors are det(1 - u T_σ)^{a_1 - a_0} with T_σ built from the individual letters. Separately the prover caught a pre-existing wording error in shard 05: "every nontrivial zero sits on the critical circle" for the *ungraded* quantum Ihara zeta, which has poles only — fixed to "pole".
- Lead: none stated; bookkeeping.
- Related: L02-113, L02-118

### L02-130 The most consequential step: derive the odd-block form from the letters, on an infinite object, Selberg first
- Source: docs/worklog/2026-09-16.md:3-10; report/sections/12_lab_log.tex:212-232
- Raised by: TJO asked what the most consequential step toward a full proof would be; then "investigate ... make a brief, hand it off to a codex exec gpt 6 astra xhigh prover, wait, report, stop", then "run a review with opus"
- Status at last mention: pursued; PROVED 0 / CORRECTED 7 / REFUTED 0 / OPEN 1, shards 03e/03f, Opus-reviewed, nine items promoted to `proved`
- Content: The gap to close is between "graded spectral transfer" and a transfer whose odd-block unitarity is *derived* from the letters, on an infinite object — Selberg first, because there the trace formula is a theorem, the divisor is known, and the source of reality is known (self-adjointness of the Laplacian).
- Lead: the notebook's own statement of its critical path. If the odd-block form could be derived from letters on an infinite object, the Ramanujan property would stop being an assumption.
- Related: L02-006, L02-114, L02-127, L02-136

### L02-131 D2: Z_S is the ring zeta of the stable two-term transverse complex; Ruelle fails the FE
- Source: docs/worklog/2026-09-16.md:30-36
- Raised by: codex prover
- Status at last mention: proved
- Content: The Selberg zeta is the ring zeta of the *stable two-term transverse complex* (even -X, odd -X+1), with Z_S(s) = D_tow(s-1)/D_tow(s) and flat supertrace (1 - e^t)F. Full transverse forms give the Ruelle zeta instead, whose even band is shifted by -1 and FAILS the notebook's functional equation and Ramanujan conditions even under coercivity. Exact trivial divisors computed (Ruelle net orders 1, c, 2c-1, 2c at 1, 0, -1, -n; tower cN^2 + 2; Selberg threshold 2 d_{1/4}). Closed geodesics are fermionic because dim E_s = 1.
- Lead: only the *stable two-term* truncation satisfies the notebook's conditions — a sharp selection principle for which graded complex to use.
- Related: L02-123, L02-114

### L02-132 D3: branchwise orthogonal pullbacks, reality from Haar, and a Jordan block at 1/4
- Source: docs/worklog/2026-09-16.md:37-40
- Raised by: codex prover, correcting the orchestrator
- Status at last mention: proved
- Content: Ω = λ(1 + λ) on Res^0 (the orchestrator's ordering sign was wrong); the pushforward isomorphism is DFG analysis cited by line, not algebra; reality comes from Haar measure; and the form must be the ORTHOGONAL sum of branchwise pullbacks, since the total pullback has Gram [[1,1],[1,1]] on partner branches and is degenerate. The operator functional equation is J X J^{-1} = 1 - X. At a Laplace eigenvalue 1/4 there is a Jordan block (algebraic 2d versus geometric d), so a full operator Hilbert–Pólya statement needs the strict bound.
- Lead: the Jordan obstruction at the 1/4 threshold is the same phenomenon as "Weil positivity is blind to Jordan blocks"; it says the exceptional eigenvalue must be excluded by a strict inequality.
- Related: L02-033, L02-114

### L02-133 D4: continuous Ihara–Bass in first-band operator form; the full-tower compression is still missing
- Source: docs/worklog/2026-09-16.md:41-43
- Raised by: codex prover
- Status at last mention: proved for the first band; "full-tower compression still not supplied"
- Content: The first-band operator form of the continuous Ihara–Bass is proved (a quadratic intertwining π_*(A^2 + A) = -Δ π_* plus the horocyclic ladder). The sampled adjacency is a *cosine functional calculus* of Δ, not -2Δ.
- Lead: supply the full-tower compression — a named, concrete, unfinished piece of the Selberg programme.
- Related: L02-026, L02-130

### L02-134 D5: no doubled-bond CP realisation of the Selberg object
- Source: docs/worklog/2026-09-16.md:44-45
- Raised by: codex prover
- Status at last mention: proved (negative)
- Content: The flat supertraces are negative distributions and therefore cannot be cMPS ring norms; adding the two dissipative jumps preserves neither the K-sector nor the first band.
- Lead: a hard negative — the Selberg object is a graded *spectral* transfer, not a graded CP transfer. This confirms the CP/spectral gap in the best-understood case.
- Related: L02-055, L02-127

### L02-135 D6 (OPEN): H-CUSP-BRIDGE — the Riemann zeros inside the Selberg divisor
- Source: docs/worklog/2026-09-16.md:46-51
- Raised by: codex prover; the one item left OPEN
- Status at last mention: open; the claim row stays `sketched`
- Content: The Riemann zeros ρ/2 are Selberg zeros of the modular surface (FJS divisor theorem, byte-checked). But the first-band states push to Eisenstein Laurent coefficients, not L^2; the orchestrator's e^{t/2} rescaling can never unitarise that sector — its centre is -3/4 under RH, while the Riemann model's -1/4 belongs to -conj(ρ)/2 and is not identified. The Maass–Selberg truncated norm is positive throughout the strip, and Selberg's 1/4 for PSL_2(Z) is KNOWN (Booker–Lee–Strombergsson, Theorem 1.1, now cit:bls-selberg-level-one). Missing: H-CUSP-BRIDGE.
- Lead: supply the cusp bridge — a statement connecting the Eisenstein Laurent data to a positive form. The single named missing hypothesis on the Selberg route; CCM was later proposed as a computational form of it.
- Related: L02-029, L02-116, L02-144

### L02-136 D7: the finite Hashimoto-lift theorem with a letter-derived metric
- Source: docs/worklog/2026-09-16.md:52-56
- Raised by: codex prover
- Status at last mention: proved; "Settles the 'Hermitian channel plus lift' open item (inverse-paired setting)"
- Content: For graphs and graded quantum Hashimoto lifts: Σ R = R(T + q T^{-1}), an inverse pushforward F_μ, a companion model, and a letter-derived metric G_C = [[1, S/2], [S/2, q]] with C* G C = q G, positive iff the band is STRICT; Jordan blocks at the endpoints; exact counterexamples K_3 × Q_3 and a ten-letter Pauli channel. The quantum pushforward uses Ad(U_i), not Ad(U_i^*).
- Lead: the finite prototype of "odd-block unitarity derived from the letters" — the exact statement the infinite case is missing. The endpoint Jordan blocks recur from D3.
- Related: L02-111, L02-130, L02-132

### L02-137 Methodological principle: draft slightly too strong, let one xhigh lane audit
- Source: docs/worklog/2026-09-16.md:60-63; docs/worklog/2026-09-13.md:54-55
- Raised by: orchestrator (Claude)
- Status at last mention: registered as working practice — "Pattern held: drafting slightly too strong and letting one xhigh lane audit is productive."
- Content: Briefs are deliberately drafted a little stronger than believed, and the prover lane then marks the false ones. On complexes eleven statements were marked FALSE-as-drafted; on Selberg 34 of a 40-row ledger were genuine corrections. The Selberg ledger's orchestrator corrections were L01 (map direction), L02-L03, L07-L09 (Ruelle/tower bookkeeping), L10 (Casimir sign), L12 (total pullback degenerate), L14 (FE sign), L28 (1/4 known for PSL_2(Z)), L30 (wrong rate on the Riemann sector), L32 (endpoint not an exception to the isomorphism), L35 (Ad(U_i)).
- Lead: keep doing it; it is the notebook's main error-finding mechanism.
- Related: L02-052, L02-090

### L02-138 TJO's mid-session check: the bond is where the Laplacian acts
- Source: docs/worklog/2026-09-16.md:26-28
- Raised by: TJO — "the bond is where the Laplacian acts, the ring has physical letters determined by jumps?"
- Status at last mention: answered yes with a refinement
- Content: Yes, with the refinement that the Laplacian side is the *adjacency* and the critical-line divisor lives on the *flow* side, the two tied by the continuous Ihara–Bass (DFG bands).
- Lead: keeps the adjacency/flow distinction explicit — a recurring source of confusion (see also the cosine functional calculus remark).
- Related: L02-133

### L02-139 Reviewer MINORs on the Selberg campaign, including "the D3 headline over-credits the letters"
- Source: docs/worklog/2026-09-16.md:15-24 and 60
- Raised by: Opus reviewer (four independent scripts, 153 checks, 31 byte-checked citations)
- Status at last mention: applied; round 2 all VALID
- Content: Four MINOR items — state the Poisson range in D3; note that shard 04f is sketched (D5); the order m at ρ/2 is inferred (D6); and 6 of the 40 ledger rows answer questions rather than correcting claims. Cosmetic: η_+ lies in DFG's E_u^*, and "the D3 headline over-credits the letters".
- Lead: the letter-derivation claim is weaker than it first reads — worth remembering when quoting the campaign's result.
- Related: L02-130, L02-132

### L02-140 CCM "Zeta spectral triples" as a machine from window data to a self-adjoint operator
- Source: docs/worklog/2026-09-17.md:3-26 and 41-46
- Raised by: TJO — "download tex source of arXiv:2511.22755 and carefully read it. I want to understand this paper, by obtaining a highly optimised arb prec flint c implementation of the algorithm described therein. The point of the impl is extendibility."
- Status at last mention: plan written and prototype reproduces the paper; sidequest, no shard registered by design
- Content: The structural reading: the construction is a machine from window explicit-formula data (atoms, kernels, trivial divisor) to a self-adjoint operator with provably real spectrum. The extension roadmap maps it onto the notebook's cases — Dirichlet, Hecke/GL(2), graph and curve transfer operators as the Carathéodory–Fejér anchor, Selberg compact and modular with the cusp comb, the graded divisor formulation, and the prolate side.
- Lead: apply the machine to the notebook's own transfer operators; the roadmap is in plan.md Sections 5-6 and only the graph rung has been built.
- Related: L02-144, L02-148

### L02-141 A typo in CCM's correction constant c(L)
- Source: docs/worklog/2026-09-17.md:29-34
- Raised by: orchestrator (Claude), by reading plus quadrature
- Status at last mention: settled — their code was right, the display is a typo
- Content: The displayed c(L) (integral of (1 - e^{-x/2})/(e^x - e^{-x}), 0.352 at λ = 3) is not the one the paper's own identity requires (∫ (1 - e^{-x/2}) ρ = 0.575, closed form derived and checked by quadrature), and the definition of γ_L(n) double counts it. The difference is n-independent, a multiple of the identity, so ξ and the spectrum are unchanged and only ε_N shifts; their table reproduces exactly with the corrected version.
- Lead: none; a note for anyone re-implementing.
- Related: L02-140

### L02-142 The secular function is not monotone between poles
- Source: docs/worklog/2026-09-17.md:35-37
- Raised by: orchestrator (Claude)
- Status at last mention: settled; it drove the algorithm design
- Content: Σ_j ξ_j/(j - s) is not monotone between poles because ξ_j changes sign; zeros 13 and 14 at λ = √13 share one pole interval. Root isolation must use the 2N count as its completeness check — a naive grid missed 2-4 of 120 roots.
- Lead: completeness by count, not by search range; the rule recurs in the benchmark.
- Related: L02-145, L02-147

### L02-143 The empirical accuracy law: about 5.5 digits per unit of x = λ^2
- Source: docs/worklog/2026-09-17.md:38-40; docs/worklog/2026-09-18.md:10-16
- Raised by: orchestrator (Claude), empirical
- Status at last mention: measured and confirmed at scale
- Content: |z_1 - γ_1| ~ 5e4 (1 - χ_4(λ)) and ε_N ~ 10 (1 - χ_4(λ)) with the Fuchs asymptotic the paper quotes, at both λ = 3 and √13: about 5.5 digits per unit of x, so x = 100 should give hundreds of digits. The benchmark confirmed it: first-zero accuracy exponential in x (5.4 digits per unit, e^{-4πx}) and independent of N; the error at height γ grows like 10^{0.37γ}; N saturates at about 7.5x.
- Lead: the convergence rate in x is exactly CCM's prolate step, the one thing a finite divisor cannot exercise.
- Related: L02-149, L02-162

### L02-144 The modular surface through CCM as a computational form of H-CUSP-BRIDGE
- Source: docs/worklog/2026-09-17.md:41-46
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: On finite transfer operators the CCM construction degenerates to Carathéodory–Fejér on Toeplitz matrices (exact once the window exceeds the divisor size); on the modular surface it would take prime geodesics plus the cusp comb (shard 09c) and should return the Maass r_j together with γ_n/2 — "a computational form of H-CUSP-BRIDGE (shard 03f)".
- Lead: a concrete, buildable experiment that would test the one open item of the Selberg campaign numerically. Nobody has built it.
- Related: L02-027, L02-135, L02-140

### L02-145 zst: the certified pipeline, and the three bugs with their lessons
- Source: docs/worklog/2026-09-17.md:55-101
- Raised by: TJO — "I like the plan in substance. Please impl a vertical tracer bullet mvp", with red-green TDD, mutation testing, fuzzing, and local copies of ground-truth sources cited in code
- Status at last mention: delivered and working
- Content: `./build/zst --x 13 --N 120 --prec 700 --zeros 50` runs in 5.0 s against mpmath's 108 s (uncertified), with ε_N certified to 1e-69, even-simplicity CERTIFIED, 120/120 roots, |z_1 - γ_1| ≤ 2.44e-55 and |z_50 - γ_50| ≤ 2.04e-3. Three bugs with general lessons: (1) arb's `acb_mat_eig_enclosure_rump` fails unless inverse iteration has converged below the even-block gap (~4e-31) — iterate to stationarity with one reused LU and re-verify with one's own Krawczyk operator; (2) the normalisation Σ ξ_j = 1 amplifies the eigenvector by 1e18-1e28, so the secular function is a difference of huge terms and `arb_calc_isolate_roots` cannot certify signs on any sub-interval — replaced by point candidates plus tiny-interval Newton and completeness by count; (3) two of the N = 40 positive roots lie at s ≈ 107 and 339, far beyond the last pole N, so "a search range is the wrong notion of completeness". Fuzzing found one real defect (b_0 was a rounding neighbourhood of zero rather than exactly zero; b_n is odd in n). Mutation testing (27/30, then 35/40 and 29/40 killed) found and closed two real gaps.
- Lead: the reusable rules — print `mag_printd(arb_radref(x))` rather than trusting `arb_printn` display rounding, and use completeness by count. Debt recorded in zst/README.md: two out-of-bounds reads inside uninstrumented FLINT calls that ASan cannot see.
- Related: L02-142, L02-147

### L02-146 The zst benchmark: how far beyond the paper one can go
- Source: docs/worklog/2026-09-18.md:3-16 and 41-45
- Raised by: TJO — "Now the code is there how far can we reasonably go beyond the paper? I am curious how many zeros we can reach and how accurately. Some kind of impromptu benchmark would be interesting."
- Status at last mention: done through x = 50 at time of writing (x = 60, 80, 100 running)
- Content: Grid x ∈ {13, 20, 30, 40, 50, 60, 80, 100}, N ≈ 10x, prec ≈ 40x + 200 bits, plus N-scans at x = 20 and 30; every row certified. First zero to 2.4e-55 (x = 13), 1.2e-92 (20), 2.6e-146 (30), 3.0e-200 (40), 2.9e-249 (50); zeros certified below 1e-3: 47, 95, 172, 251, 315. x = 100 (N = 1000, 4000 bits) was OOM-killed at the 10.7 GB cgroup limit, so the Krawczyk step was reworked to O(N^2) per iteration with a single precomputed C0 = I - R J(ỹ) and the residual formed by arb_dot; x = 80 then ran at 2.4 GB where the old code used 5.1 GB.
- Lead: the scaling laws are now measured, which is what makes the prolate comparison meaningful.
- Related: L02-143, L02-147

### L02-147 Four scale-only defects and the interval-arithmetic rule
- Source: docs/worklog/2026-09-18.md:18-50
- Raised by: orchestrator (Claude), each found by the benchmark and fixed test-first
- Status at last mention: all fixed
- Content: (1) The interval-LDL^T inertia certificate failed from x = 20 because pivot radii grow like the squared condition number; replaced by verified positive definiteness of the deflated matrix E - 2ε + c v v^T and of O - 2ε (approximate Cholesky plus a ball residual, Rump's isspd), with amplification only linear in the condition number — the 2×2 unit test caught that the deflation constant must exceed s - ε. (2) The QR candidate generator dominated runtime (612 of 673 s at x = 40) and cannot run below the dynamic range of the rank-one term; replaced by a sign scan with bisection per pole interval plus a geometric tail grid, since tail roots cluster just past N (400.34, 406.74 at N = 400) in pairs separated by about a tenth of their distance from N; x = 40 dropped from 673 s to 119 s with an identical table. (3) Overlapping certified balls used to discard the entire list; now a Newton step on the hull of the pair decides rigorously. (4) Far-out roots failed interval-Newton because the plain ball evaluation of h' carries the full dependency error; a mean-value form h'(m) + h''(X)(X - m) fixes it (x = 50, N = 400 completes in 262 s, previously incomplete after 1342 s). General rule recorded: "plain interval evaluation of a cancelling sum is useless; mean-value or point-plus-tiny-box forms are needed".
- Lead: also recorded as *not done* — mutation testing of the day's changes, deferred because the mutation script's `make clean` would remove the binary the running grid uses.
- Related: L02-145, L02-146

### L02-148 MVP-2: what of the CCM framework generalises to the Ihara zeta (it is classical)
- Source: docs/worklog/2026-09-18.md:55-73
- Raised by: TJO — "run a 2nd vertical tracer bullet mvp: this time we focus on ihara zeta for graphs. I want to understand what parts of the connes et al framework generalise easy, which not"
- Status at last mention: plan written; 31 of 36 theory claims proved, all checked numerically, confirmed by a numerics lane (446 checks)
- Content: The linear algebra generalises verbatim and is classical: group Z, window {-M..M}, Weil form = the notebook's own Toeplitz Wform (thm:weil-positivity-finite), the rank-two commutator = the rank-two displacement Z T Z* - T of the cyclic shift, the Loewner matrix = a Loewner matrix on the circle, and Lemma `key` = a new unitary key lemma (U = Z* - |Z*ξ⟩⟨η|, U* T U = T exactly, three lines); the circle conclusion = Carathéodory–Fejér 1911 = Connes–van Suijlekom's Corollary `corcar` (CS:792) = Makhoul 1981; ε_M = Pisarenko's noise floor; a Cayley transform makes the graph case an instance of CS:1356.
- Lead: the three-line unitary key lemma is a small original result worth stating separately.
- Related: L02-140, L02-149, L02-159

### L02-149 What does NOT generalise: the analytic content (the prolate step)
- Source: docs/worklog/2026-09-18.md:74-79
- Raised by: orchestrator / theory lane
- Status at last mention: recorded
- Content: A finite graph has a finite divisor, so there is a critical window K = R + 1 where the construction is exact, under-resolved below and degenerate above (even-simplicity fails). There is no second truncation, no Dirichlet-kernel approximation, no transcendental archimedean term (the graph's gamma factor is the rational (1-u^2)^{|E|-|V|}), no regularised determinant, and no Hermite/prolate structure at all: "the one step whose absence blocks CCM's proof is the one a finite graph cannot exercise".
- Lead: the sharpest statement of where the difficulty lives; any finite model is structurally incapable of testing it.
- Related: L02-143, L02-162

### L02-150 What the graph adds: run the chain on a FALSE Riemann hypothesis
- Source: docs/worklog/2026-09-18.md:80-85 and 128-134
- Raised by: orchestrator / theory lane; computed and certified in ihz
- Status at last mention: computed
- Content: For a non-Ramanujan graph the construction still returns a circle spectrum; ε_M crosses zero and diverges like -m ρ^{2M} (the slope recovers the offending eigenvalue); the even block stays PSD and the odd block goes negative, so ξ_min turns odd and CCM's prescription fails while the kernel vector still recovers the divisor exactly. "Reality is free for any Toeplitz matrix; positivity is the whole content; RH enters only as ε → 0, Weil's criterion verbatim." Certified instances: twoK4 odd-block minimum -2.673 at Mp = 2 with the two off-circle points missed by the circle roots; necklace:6 odd block -8.257, -26.83, -54.93, -89.05, -139.13, -199.67 at Mp = 6..11 with ratios 3.25, 2.05, 1.62, 1.56, 1.44 approaching ρ^2 = 1.386 from above; prism:16 full minima 30.084 down to -214.2 at Mp = 3..14, matching the theory lane digit for digit.
- Lead: being able to *falsify* on demand is a capability no Riemann-side computation has; it is the cheapest way to test whether a proposed positivity argument really uses RH.
- Related: L02-006, L02-153, L02-154

### L02-151 Sign and grading in the CCM chain: a mixed divisor is indefinite by construction
- Source: docs/worklog/2026-09-18.md:86-88
- Raised by: orchestrator / theory lane
- Status at last mention: recorded
- Content: An ungraded graph gives poles with the sign flipped relative to CCM. A curve (purely odd divisor) gives CCM's sign with the same code, and this is already in the literature (Hallouin–Perret 2019, cited at CS:800). A mixed divisor is indefinite by construction — "the chain requires one parity".
- Lead: directly relevant to the graded programme — the CCM positivity machine cannot accept a mixed (even + odd) divisor, which is precisely what a graded Riemann object would have.
- Related: L02-049, L02-114, L02-153

### L02-152 Traps found in the CCM/Ihara prototype and in ihz integration
- Source: docs/worklog/2026-09-18.md:89-95 and 139-147
- Raised by: both prototype lanes, and the three ihz Opus workers
- Status at last mention: fixed
- Content: η is the delta at the window edge, not all-ones in the position basis (both lanes hit it; a wrong η gives real but wrong roots); the trivial ±1 copies are not reciprocal-closed and must be subtracted in the even extension; FLINT's `arb_fmpz_poly_complex_roots` hangs on repeated roots (square-free factor first); `acb_mat_eig_multiple_rump` fails at n = 24 without precision doubling; double precision cannot certify ε = 0 at the critical window (condition 1e16-1e18), which is the argument for arb plus an exact rank stage. In integration: two workers called `_fmpz_vec_init` without `fmpz_vec.h` (pointer truncation on LP64); the ported `eigmin` converges to the smallest-*modulus* eigenvalue, which is not the minimum once a block has negative eigenvalues (necklace at Mp = 6 read +6.39 before the fix, -8.257 after); dyadic bisection of [0, π] puts split points exactly on graph divisor angles (3π/4 for Petersen), so the first cut must be at an irrational fraction and endpoint roots certified by Newton on the block.
- Lead: a reusable trap list for any future implementation.
- Related: L02-148, L02-154

### L02-153 The ihz plan G1–G5 and its named experiments
- Source: docs/worklog/2026-09-18.md:96-102
- Raised by: orchestrator (Claude)
- Status at last mention: G1-G3 built; the experiments mostly not run
- Content: `ihz/`, a sibling of `zst/`: `eigmin.c` ported verbatim, an exact integer stage (Hashimoto, traces, Ihara–Bass as an exact polynomial identity, square-free charpoly for the truth spectrum) and a ball stage (Toeplitz form, certified eigenpair, roots on the circle by theta-substitution, U'' and the Cayley form as certified cross-checks, Prony multiplicities); about 1400 lines and two weeks. Experiments named: the under-resolved law ("the one place the graph can inform zeta"), the non-Ramanujan slope, irregular graphs (Weil positivity without duality), the curve sign, the mixed-divisor refusal, and the anti-palindromic search.
- Lead: the under-resolved law is explicitly flagged as the one experiment whose result could transfer to zeta.
- Related: L02-150, L02-155, L02-156

### L02-154 The exact integer anchor: Carathéodory–Fejér recovery is an integer identity at the critical window
- Source: docs/worklog/2026-09-18.md:119-127
- Raised by: three Opus workers on ihz
- Status at last mention: verified on twelve named graphs and the F_5 curve
- Content: At the critical window the integer kernel polynomial of D T D equals the squarefree retained characteristic polynomial exactly — no balls involved. The ball stage then certifies the roots on the circle to 1e-73, the unitary key lemma U^T(T - ε)U = T - ε and the determinant identity; Prony weights contain the multiplicities (Petersen 5,5,4,4; Heawood 6,6,6,6). Under-resolved ε values match the prototype (Petersen 9.4476568, Q3 3.0, Heawood 12.0); at the critical window ε is a ball of radius 1e-75 around 0; one window later the kernel is three-dimensional and the Krawczyk certificate declines, as it must.
- Lead: a clean exact statement of what "the window is critical" means operationally.
- Related: L02-148, L02-159

### L02-155 The under-resolved Q-2 data, unanalysed
- Source: docs/worklog/2026-09-18.md:135-138
- Raised by: orchestrator (Claude); explicitly deferred
- Status at last mention: "Not analysed; to be looked at with TJO."
- Content: Even-block ε below the critical window: necklace:6 gives 0.629, 0.183, 0.0571, 0.0125, 0.0052 at Mp = 5..9 (ratio about 0.3); prism:16 gives 5.86, 0.183, 0.0135, 4.4e-4, 9.3e-6 at Mp = 9..13 (ratio about 0.03).
- Lead: fit the decay law. The under-resolved regime is the named "one place the graph can inform zeta" and the data is already sitting there unfitted.
- Related: L02-153, L02-163

### L02-156 ihz items explicitly not done
- Source: docs/worklog/2026-09-18.md:148-150 and 103-104
- Raised by: orchestrator (Claude)
- Status at last mention: not done
- Content: Fuzz and mutation testing (relaxed by TJO — "You may relax testing disciplines in interest of smoother orchestration"); irregular graphs in C; the anti-palindromic search (Q-3); the Q-2 fit; the Cayley form as a certified cross-check (the unitary route was certified instead). Lane reports and the theory claims are unreviewed by a second model family, and nothing under report/, db/, top-level notes/*.md or scripts/ was touched, so no claim was registered.
- Lead: irregular graphs would test Weil positivity *without* duality — structurally interesting, since the Riemann side has no obvious duality either.
- Related: L02-153, L02-155, L02-168

### L02-157 A regular fermionic cMPS whose physical correlation selects four equal-width modes
- Source: docs/worklog/2026-09-19.md:15-22
- Raised by: review subagents at TJO's request (five agents: cusp/scattering, positivity and products, graded channels, then the Riemann/Selberg operator and physical cMPS differences); independently reviewed
- Status at last mention: exploratory — "not an RH proof or new registered theorem status"
- Content: The principal constructive finding of the final review session: a regular fermionic cMPS whose physical correlation selects four equal-width modes despite the presence of additional odd transfer modes. An independent review explains the selection by linear Majorana closure and separates reflection from the coercivity inequality needed for equal widths. Perturbation examples show which properties survive. Reports in notes/rh-strategy-2026-09-19/.
- Lead: the most promising live mechanism for "why would all the odd modes have the same width" — i.e. a candidate mechanism for RH itself in this language. Unregistered.
- Related: L02-080, L02-114, L02-119

### L02-158 The operator lane: cusp flux, wave/geodesic shifts, and self-adjoint Laplace data
- Source: docs/worklog/2026-09-19.md:19-22
- Raised by: review subagents (the two additional agents TJO asked for)
- Status at last mention: exploratory
- Content: The operator lane clarified cusp flux, wave/geodesic shifts and the distinct role of self-adjoint Laplace data in the precise Riemann/Selberg operator comparison. Uetake's full 2007 paper and Bonthonneau–Weich's TeX were cached locally.
- Lead: the Riemann/Selberg operator difference is the same gap as H-CUSP-BRIDGE; the two newly cached sources have not been used.
- Related: L02-044, L02-135

### L02-159 The window form is an exact compression; the only implicit model is Pisarenko
- Source: docs/worklog/2026-09-19.md:52-62
- Raised by: TJO, from the CCM tutorial of an earlier session — "the method seems to assume a form for tr(A^k), collect incomplete data, build a model for the higher traces, and use positivity and Toeplitz structure on the minimal eigenvector; could one build better estimators for tr(A^l), l > K, from the traces up to K?"
- Status at last mention: answered; registered as shard 08g, 45 checks, unreviewed
- Content: Step (3) of that reading is not something the chain does: the window form is the exact compression of the full Weil form (traces up to lag K for a graph; primes ≤ λ^2 with exact pole and archimedean terms for zeta), and the only implicit model of the higher traces is the Pisarenko extension — K atoms on the circle (the kernel roots of W_K - ε_K, i.e. the spectrum of the perturbed operator) plus a noise floor ε_K at lag zero.
- Lead: corrects a natural misreading of the CCM method — the machine does not extrapolate.
- Related: L02-148, L02-160

### L02-160 The extension disc: positivity alone cannot beat one Schur parameter per lag
- Source: docs/worklog/2026-09-19.md:63-68; report/sections/12_lab_log.tex:234-249
- Raised by: orchestrator (Claude), answering TJO
- Status at last mention: registered (shard 08g), unreviewed
- Content: Given n_0..n_K with a definite window, the admissible n_{K+1} fills a closed disc: centre the Levinson/Yule–Walker one-step predictor (Burg's maximum-entropy extension), radius det W_K / det W_{K-1}. Boundary points are the singular windows with K+1 atoms on the circle (Carathéodory–Fejér, byte-cited from Connes–van Suijlekom 2511.23257:752). With exactly K+1 distinct atoms the truth sits on the boundary, one lag before the critical window. Each further lag is one Schur parameter, so positivity alone cannot beat the disc.
- Lead: a rigorous ignorance measure quantifying exactly how underdetermined side B is by the counts — the quantitative form of the founding "find the other small matrix" question.
- Related: L02-003, L02-091, L02-161, L02-163

### L02-161 Integrality of the counts adds nonnegativity and a Newton congruence
- Source: docs/worklog/2026-09-19.md:69-73
- Raised by: orchestrator (Claude)
- Status at last mention: registered
- Content: The counts add nonnegativity and a Newton-identity congruence N_{K+1} ≡ -Σ c_i N_{K+1-i} mod (K+1) (integer characteristic polynomial). For (1 2)(3 4 5) the candidates are {0,2,4}, {0,3}, {2} at K = 1, 2, 3 — pinned one lag early, where Pisarenko alone gives -0.5. For the Petersen graph the rescaling multiplies the radius by q^{(K+1)/2} (35.5, 40.6, 49.4 in counts), so integrality pins nothing.
- Lead: arithmetic helps only when the disc is small relative to the lattice spacing, i.e. only for tiny objects; this suggests looking for other arithmetic constraints that survive rescaling.
- Related: L02-095, L02-160

### L02-162 For zeta, a better estimator means more primes
- Source: docs/worklog/2026-09-19.md:74-77
- Raised by: orchestrator (Claude)
- Status at last mention: registered
- Content: For ζ the mean of the higher traces is the pole (already exact), higher powers of known primes are outside the window's support, and the unknown fluctuation *is* the zeros — so a better estimator means more primes. The remaining freedom is the choice of extremal extension, whose convergence rate is CCM's prolate step, which a finite divisor cannot exercise.
- Lead: closes off the "smarter extrapolation" idea for zeta; the only lever is the prolate/asymptotic step.
- Related: L02-143, L02-149, L02-159

### L02-163 Proposed, not run: the disc radius as a rigorous ignorance measure
- Source: docs/worklog/2026-09-19.md:78-79
- Raised by: orchestrator (Claude)
- Status at last mention: "Proposed, not run"
- Content: Two experiments: compute the disc radius per window in `ihz` as a rigorous ignorance measure; and compute the Schur-complement radius of the window Loewner form in `zst` against the observed e^{-4πx}.
- Lead: the second would connect the abstract ignorance measure to the measured exponential accuracy law — a direct, cheap test of whether the disc explains the empirical rate.
- Related: L02-143, L02-155, L02-160

### L02-164 Reproducibility: BLAS thread contention changes recorded digits
- Source: docs/worklog/2026-09-19.md:30-41; docs/worklog/2026-09-18.md:47-50
- Raised by: orchestrator (Claude), during shutdown validation
- Status at last mention: fixed — commit validation runs the full hook with two BLAS threads
- Content: Excessive BLAS thread contention was found: two threads reproduced the recorded rounded errors while one thread changed a displayed error from 5.5e-12 to 3.7e-12; a second platform-dependent fixture difference was only a printed signed zero, so the graded Ramanujan script now adds positive zero after rounding its display. Also added: atomic checksummed recovery snapshots including Git-ignored sources, with the maintenance utility excluded from evidence-script parity. Lessons from the previous day: `pkill -f` on a pattern matching one's own shell kills the shell, and fully buffered output from a killed process leaves an empty file (use `stdbuf -oL`).
- Lead: captured outputs are thread-count sensitive; fix the thread count in CI, which was done.
- Related: L02-147

### L02-165 conj:weil-lps-hecke — the joint spectra as Hecke eigenvalues via Jacquet–Langlands
- Source: report/sections/10_open_problems_dead_routes.tex:43-51
- Raised by: orchestrator (Claude)
- Status at last mention: open
- Content: The joint spectra of the commuting Weil–LPS channels Φ^± are conjectured to be Hecke eigenvalues of weight-2 forms for the quaternion algebra ramified at {2, ∞}, via Jacquet–Langlands. The visible structure is consistent: joint eigenvalue pairs, small-degree algebraic integers, and multiplicities equal to those of the irreducibles of PSL(F_p) in W^± ⊗ conj(W^±).
- Lead: "Needs LMFDB and the Jacquet–Langlands bookkeeping" — a finite amount of work that would turn a numerical coincidence into an arithmetic identification.
- Related: L02-018, L02-023, L02-121

### L02-166 conj:assemble-over-p — assembling the Weil–LPS channels over all primes
- Source: report/sections/10_open_problems_dead_routes.tex:53-61
- Raised by: orchestrator (Claude)
- Status at last mention: open — "Nothing is known beyond the obstruction recorded below" (the obstruction being obs:prime-by-prime-blind)
- Content: The Weil–LPS channels for different p should assemble into one object whose rings are the primes and whose transfer spectrum is the zeros of ζ. This is the parent campaign's DG-GLOBAL question in this guise.
- Lead: the obstruction is already known — any prime-by-prime assembly is blind to zeros — so the assembly must be non-product. Nothing has been tried.
- Related: L02-013, L02-020, L02-165

### L02-167 conj:phantasm-both-halves — one graded Lindbladian with the BC fixed point and the zeros as odd modes
- Source: report/sections/10_open_problems_dead_routes.tex:63-79
- Raised by: orchestrator (Claude), replacing item 0b of the reframe programme
- Status at last mention: open
- Content: There is a Z_2-graded Lindbladian (or a type III generalisation at β = 1) whose stationary state is the Bost–Connes KMS state, with entanglement Hamiltonian log N, and whose odd relaxation modes are the nontrivial zeros. The SHW rebound-state equation with a *mixed* rebound state is its finite-dimensional shadow; the vacuum rebound state is excluded. Two obstacles are named: the fixed point constrains the Lindbladian only partially, and at β = 1 the fixed point is not normal, so K_S with its pure vacuum cannot be the whole bond — the missing identification of K_S with the Bost–Connes bond is the first obstacle. A second open item from the same campaign is the unrestricted infinite parity question.
- Lead: identify K_S arithmetically, then solve the mixed-rebound-state equation. This is the notebook's central open conjecture.
- Related: L02-038, L02-050, L02-053, L02-056, L02-058, L02-102

### L02-168 Only one model family has ever been used as reviewer
- Source: report/sections/00_frontmatter_status.tex:42-46; docs/worklog/2026-09-18.md:103-104 and 148-150
- Raised by: orchestrator (Claude), recorded in the status vocabulary
- Status at last mention: standing caveat — "Both author and reviewers to date are Claude models (single family); no second model family has been used."
- Content: The `proved` tag requires a written proof under notes/ plus a reviewer other than the author returning "VERDICT <id>: VALID" in notes/reviews/, but in practice all reviewers are Claude models. The codex/astra lanes are a second family on the *author* side for some campaigns; the review side is not. Several bodies of work are explicitly flagged as unreviewed by a second family: the ihz lane reports, the Ihara theory claims, shard 04g, the cMPS parity rows, the graded permutation rows, and shard 08g.
- Lead: run a second-family REFUTE review on the highest-value `proved` rows and on shard 04g, which is explicitly listed as a next step.
- Related: L02-104, L02-156

## Small but possibly consequential

1. **L02-050** — The rebound state is determined by ρ_∞ ∝ ∫ Z(t) Ω Z(t)* dt; inverting that one integral equation would produce the unique candidate Ω for the Phantasm, and nobody has tried.
2. **L02-038** — The SHW renewal spectrum is governed by the scalar equation 1 = m̂_Ω(λ); solving it for an arithmetically natural Ω is a small computation that could settle whether the renewal picture sees the zeros at all.
3. **L02-017** — "Length quantisation should come from a flatness-type condition" (TJO): if realised, it would explain why exactly the lengths log n appear, which no candidate currently does.
4. **L02-029** — Mayer's operator with the explicit cusp tail and a Schur complement separating the interior block from the cusp coordinate: the only operator in the notebook in which the Riemann zeros appear at ρ/2 by a known mechanism, and the proposed boundary-pairing computation was never run.
5. **L02-067** — Knill's graph torsion SDet(D) = Π det(D_k)^{(-1)^k} has never been joined to the Ihara zeta; doing so would give a second, independent graded presentation of a graph zeta.
6. **L02-121** — "In the (13;5) case the extremal Hecke eigenvalue is odd": a one-line numerical observation tying graded parity to arithmetic extremality, never followed up on other pairs.
7. **L02-155** — The unanalysed Q-2 under-resolved decay data (ratios about 0.3 and 0.03) sits in the explicitly named "one place the graph can inform zeta" and only needs a fit.
8. **L02-163** — Comparing the Schur-complement radius of the window Loewner form in `zst` against the measured e^{-4πx} would test whether the ignorance disc explains the empirical accuracy law; proposed and never run.

## Dead routes recorded

- **Wick-rotating Bost–Connes to Hilbert–Pólya** — obstructed by the Fourier duality between {log n} and the zeros (docs/worklog/2026-09-11.md:12-14).
- **cMPS/Selberg as a functional-integral continuum limit** — TJO: too far (docs/worklog/2026-09-11.md:46; report/sections/10_open_problems_dead_routes.tex:143-145).
- **Algebraic-integer recognition of the Weil–LPS joint eigenvalues from five-digit output** — inconclusive and tautological, the adjacency matrix being integral (docs/worklog/2026-09-11.md:85-87; report/sections/10_open_problems_dead_routes.tex:146-148).
- **Dwork's p-adic transfer operator as a route to RH for curves** — it cannot see RH (docs/worklog/2026-09-11.md:93-95; report/sections/10_open_problems_dead_routes.tex:148-149).
- **Any prime-by-prime ansatz (direct sums of circle flows, product states, commuting dilations)** — blind to zeros; the finite-S spectrum is only the partial Euler product's poles (docs/worklog/2026-09-12.md:5-22; report/sections/10_open_problems_dead_routes.tex:97-106).
- **Kraus operators from PSL(2,Z) group generators (Jones / Thompson representations)** — expanders but not Ramanujan beyond p = 7; "a presentation is not arithmetic" (docs/worklog/2026-09-12.md:156-181).
- **SPT / cohomological protection as a source of RH** — protection is sign data, RH is modulus data (docs/worklog/2026-09-12.md:183-190; report/sections/10_open_problems_dead_routes.tex:112-127).
- **A Stinespring form of Z(t) with prime dilations as jump operators** — the Riemann channel is a no-event semigroup, so it has no jumps at all (docs/worklog/2026-09-12.md:250-256).
- **A bounded renorming of K_S into a Hilbert–Pólya space** — excluded by the Riesz-basis / interpolating-sequence criterion; a different completion is needed (docs/worklog/2026-09-12.md:325-337).
- **Vacuum rebound state / absorbing-vacuum Lindbladian** — stationary state is the pure vacuum, trivial entanglement, divergent renewal integral (docs/worklog/2026-09-12.md:411-416).
- **Prime-chain detailed-balance Lindbladian** — real spectrum, no zeros (docs/worklog/2026-09-12.md:416-419).
- **A normal KMS fixed point at β = 1** — normal KMS states exist only for β > 1 (docs/worklog/2026-09-12.md:419-421).
- **A general-complex Ihara zeta** — does not exist; only buildings, and the one general object (combinatorial Ruelle zeta) has no RH (docs/worklog/2026-09-13.md:34-39).
- **Reading building zetas as curve zetas** — no honest curve-weight dictionary; the three chamber circles come from mixed representation-theoretic sources (docs/worklog/2026-09-13.md:71-76).
- **The vertex-level Kang–Li identity off buildings** — ∂Δ^3 counterexample; no matrix polynomial of any size works (docs/worklog/2026-09-13.md:66-68).
- **Covariant weights on the full Cayley complex** — pure gauge, det(I - u T^E) = det(I - uT)^{dim V} (docs/worklog/2026-09-13.md:81-83).
- **Bosonic (ungraded) ring norms for genus ≥ 1** — no honest trace has those point counts (docs/worklog/2026-09-12.md:405-407; sharpened at docs/worklog/2026-09-13.md:152-155).
- **A nonnegative automaton counting the points of the ordinary elliptic curve** — does not exist (docs/worklog/2026-09-14.md:85-86).
- **The drafted bound Σ_odd |μ|^2 ≤ 2 Tr(E_++) Tr(E_--)** — FALSE; 173/400 random counterexamples (docs/worklog/2026-09-14.md:87-89).
- **The literal Tier-B placement and the vacuum ansatz for genus two** — impossible; one odd letter with a vacuum letter never solves genus two (docs/worklog/2026-09-14.md:94-95 and 101-103).
- **The yolo phase-side Lindbladian** — grading not preserved, rates 1/p give no normal semigroup, shell Gibbs weights not stationary, parity closure is not the Q^× quotient, no singularity in the strip at any cutoff (docs/worklog/2026-09-14.md:206-220).
- **The Ramanujan-sum sector with prime jumps alone as the identification of K_S** — ruled out (docs/worklog/2026-09-14.md:222-226).
- **Inverse-closed letters as a source of the functional equation** — diag(1,2) counterexample; the mechanism lives in the non-backtracking construction (docs/worklog/2026-09-14.md:259-261).
- **A finite bond carrying a nonrational zeta, an atomic prime comb, or infinitely many divisor points** — impossible (docs/worklog/2026-09-14.md:264-266).
- **Quantum expanders on ungraded bonds as candidates for zeros** — ungraded ring zetas have poles only, and periodic and antiperiodic closures coincide (docs/worklog/2026-09-15.md:16-19).
- **An odd-sector Alon–Boppana bound** — REFUTED; Φ_odd = 0 examples exist and Hastings' argument needs nonnegative word traces (docs/worklog/2026-09-15.md:102-106).
- **The reflection (and K-type) grading as the grading making Selberg zeros odd** — it puts them in the even sector, is not a flow grading, is not the Hodge grading, and does not supercancel (docs/worklog/2026-09-15.md:71-76; docs/worklog/2026-09-16.md:57-58).
- **The Ruelle zeta (full transverse forms) as the graded object for Selberg** — its even band is shifted by -1 and it fails the notebook's FE and Ramanujan conditions even under coercivity (docs/worklog/2026-09-16.md:31-34).
- **A doubled-bond CP (cMPS) realisation of the Selberg object** — the flat supertraces are negative distributions, and adding the two dissipative jumps preserves neither the K-sector nor the first band (docs/worklog/2026-09-16.md:44-45).
- **e^{t/2} rescaling to unitarise the Riemann sector of the modular surface** — can never work; the centre is -3/4 under RH, not -1/4 (docs/worklog/2026-09-16.md:47-49).
- **Naive grid or search-range root isolation in the CCM secular function** — not monotone between poles, and roots occur far beyond the last pole; completeness must be by count (docs/worklog/2026-09-17.md:35-37 and 87-89).
- **Interval LDL^T inertia as the even-simplicity certificate at scale** — pivot radii grow like the squared condition number; fails from x = 20 (docs/worklog/2026-09-18.md:20-24).
- **Plain interval evaluation of the cancelling secular derivative** — useless; mean-value forms are required (docs/worklog/2026-09-18.md:33-39).
- **A mixed (even + odd) divisor in the CCM chain** — indefinite by construction; the chain requires one parity (docs/worklog/2026-09-18.md:86-88).
- **Extrapolating the higher traces beyond the window** — the chain models nothing beyond it, and positivity alone cannot beat one Schur parameter per lag (docs/worklog/2026-09-19.md:57-68).
