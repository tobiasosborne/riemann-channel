# Lane L03: the riemann-cmps campaign (brief, prover proofs, refuter reviews)

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| `notes/riemann-cmps/astra-brief.md` | 29 (very long lines; read in full) | yes | 19 (L03-001 … L03-014, L03-041, L03-045, L03-048, L03-049, L03-058) |
| `notes/riemann-cmps/astra-proofs.md` | 1356 | yes | 33 |
| `notes/reviews/riemann-cmps-2026-09-12.md` | 777 (Round 1 lines 1–708, Round 2 lines 709–777) | yes | 20 |
| `notes/reviews/round2-2026-09-12.md` | 281 | yes | 9 — note this file is **not** about the riemann-cmps campaign at all; it is the round-2 re-review of the quantum-Ihara sidequest (`notes/quantum-ihara-general.md`, `notes/prior-art-quantum-ihara.md`, `scripts/qihara_general.py`). Its ideas are logged here anyway (L03-053 … L03-061). |

Total entries: **61**.

---

## Ideas and leads

### L03-001 The Phantasm as a graded cMPS bond: the whole working picture
- Source: `notes/riemann-cmps/astra-brief.md`:5
- Raised by: TJO / orchestrator (Claude), quoting HANDOFF.md "the Bost--Connes reframe"
- Status at last mention: partially explored — the *spectral* half is forced and realised (T1.4 + T4.1); the *physical cMPS* half is explicitly not established (`astra-proofs.md`:1340–1355, T8.1)
- Content: "dilation time is the one-dimensional space of a continuous matrix product state (cMPS); the bond carries a 'Riemann Lindbladian' whose unique fixed point is the pole of zeta at s = 1 and whose relaxation modes are the zeros; because the ring norms of a cMPS are sums of squares while the zeros enter the explicit formula with a minus sign, the bond must be Z_2-graded, the zeros fermionic (odd), the pole bosonic (even), and the ring norm a supertrace." Everything else in this lane is an attempt to make one piece of that sentence rigorous or to show it cannot be made rigorous.
- Lead: build a cMPS whose actual Hilbert-space ring norm (not a formal supertrace) reproduces the prime measure, with a graded bond. If it worked, RH becomes a uniform-decay statement about a physical transfer semigroup.
- Related: L03-015, L03-021, L03-024, L03-031, L03-051

### L03-002 The five-part audit frame (forced / impossible / concrete / prime-chain / prototype)
- Source: `notes/riemann-cmps/astra-brief.md`:5
- Raised by: orchestrator (Claude)
- Status at last mention: executed; answered in T8.1
- Content: the brief asks for "what is FORCED (spectrum, parities), what CANNOT exist (no-go theorems), what exists concretely (the Riemann channel as the odd sector; the vacuum-decay Lindbladian), what the prime-chain (Bost--Connes, side A) picture gives and does not give, and the finite-field prototype (Artin--Schreier) where everything is explicit". This five-way split is itself reusable as a template for the next campaign on a different candidate object.
- Lead: re-run the same five-part audit on any future Phantasm candidate before investing in it.
- Related: L03-051

### L03-003 Graded spectral datum + supertrace distribution as the basic object
- Source: `notes/riemann-cmps/astra-brief.md`:7; `astra-proofs.md`:13–21
- Raised by: orchestrator (Claude)
- Status at last mention: registered and proved (T1.1, T1.2)
- Content: a countable multiset of pairs (lambda, epsilon) with epsilon in {+1,-1}, subject to (G1) Re lambda <= c and (G2) sum m (1+|lambda|)^{-N} < infinity; supertrace str e^{tG} = sum epsilon m e^{lambda t} as a distribution on (0, infinity); net signed multiplicity nu(lambda) = m(lambda,+1) - m(lambda,-1); two data are equivalent "up to cancelling pairs" iff they have the same nu. This is the notebook's minimal formal home for a fermionic spectrum.
- Lead: none stated beyond its use in T1–T4; but the "cancelling pairs" equivalence is exactly the freedom a physical construction could exploit (add a boson–fermion pair at the same eigenvalue and nothing in the trace notices).
- Related: L03-004, L03-018

### L03-004 Rigidity: the supertrace determines the net spectrum
- Source: `astra-brief.md`:13; `astra-proofs.md`:64–108 (T1.2), 140–168 (T1.4)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, `proved-here` (T1.1, T1.2); T1.4 `conditional-on H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC`
- Content: pair the supertrace with cut-offs of t^k e^{-st} for k >= N+1; the result is k! sum nu(lambda)(s-lambda)^{-(k+1)}, meromorphic on C, whose principal part at lambda reads off nu(lambda). Hence any graded datum with supertrace comb(u) has nu(1)=+1, nu(rho)=-m_rho, nu(-2k)=-1; any datum with supertrace 2 P_+(t) has nu(0)=+1, nu(-conj(rho)/2)=-m_rho, nu(-(k+1/2))=-1.
- Lead: this is the tool that makes "the Phantasm's single-particle graded spectrum is forced" a theorem rather than a hope; reuse it whenever a candidate object is proposed — compute its supertrace and compare.
- Related: L03-003, L03-021, L03-022

### L03-005 Positivity forces the parities (finite flip sets)
- Source: `astra-brief.md`:15; `astra-proofs.md`:199–238 (T2.2)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, proved for finite flip set F_Z, arbitrary F_T
- Content: flip the parities of an arbitrary set of eigenvalues away from the reference (pole even, everything else odd). If the flip set among the nontrivial zeros is finite and the resulting supertrace is a positive distribution, then the pole is not flipped and no nontrivial zero is flipped. Trivial zeros may be flipped freely: comb + 2 sum_{k in F_T} e^{-2ku} >= 0 always. So "the zeros are fermionic" is *forced by positivity*, not chosen.
- Lead: extend to infinite flip sets (see L03-006, L03-034); that would make the parity assignment completely rigid.
- Related: L03-006, L03-022, L03-034

### L03-006 The infinite-parity-rigidity question (T2(c)) — the campaign's sharpest open problem
- Source: `astra-brief.md`:15; `astra-proofs.md`:239–271 (T2.3, T2.4), 1355; review `riemann-cmps-2026-09-12.md`:98, 104–110
- Raised by: orchestrator (Claude); analysed by codex prover; sharpened by Opus reviewer
- Status at last mention: open. Prover: `sketched` scope statement (T2.4). Reviewer: "I could not turn it into a proof or a counterexample."
- Content: does positivity of the supertrace alone force *all* infinitely many zero parities to be odd? The obstruction: with F_Z infinite the flipped subseries 2 sum_{rho in F_Z} m_rho e^{rho u} is only a distribution and can carry atoms at prime powers, so f = mu - comb is a signed measure whose diffuse part is >= 0 but whose atoms can be negative down to -Lambda(n). Landau's theorem is toothless because the abscissa of mu is already 1 from the pole. Prover's precise missing step: "extracting atomic and diffuse parts is not the same as selecting spectral terms."
- Lead: the reviewer states the exact surviving question: "whether a conjugation-symmetric infinite F_Z can have atomic contribution > -Lambda(n) at every prime power, i.e. 'density at most 1/2' in the atom weighting" (review:98). Settle that and T2(c) closes. Consequence: full parity rigidity, i.e. the fermionic character of the zeros would follow from positivity alone with no finiteness hypothesis.
- Related: L03-005, L03-033, L03-034

### L03-007 No-go for ungraded realisations: the zeta numerator *is* the odd sector
- Source: `astra-brief.md`:17; `astra-proofs.md`:282–310 (T3.1)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered; finite case `proved-here`, trace-class case `conditional-on H-LIDSKII`
- Content: if N_n = sum b_i^n - sum alpha_j^n with at least one uncancelled alpha, no finite matrix and no trace-class operator has Tr E^n = N_n for all n. Proof by residues: at u = 1/alpha the prescribed generating function has residue +m_alpha/alpha while any ordinary trace function has residue -m_E(alpha)/alpha with m_E >= 0. Negative net multiplicity is unavoidable, i.e. a numerator forces a grading.
- Lead: none stated; it is the load-bearing negative result behind "the bond must be graded".
- Related: L03-008, L03-009, L03-010

### L03-008 Criterion: when is a sequence a trace sequence / a supertrace sequence?
- Source: `astra-brief.md`:17; `astra-proofs.md`:311–340 (T3.2)
- Raised by: orchestrator (Claude); proved and sharpened by codex prover
- Status at last mention: registered, proved (necessity of the trace-class half `conditional-on H-LIDSKII`)
- Content: (N_n) is a trace sequence of a trace-class operator iff Z(u) = exp(sum N_n u^n/n) = prod (1-lambda_i u)^{-1} with sum|lambda_i| < infinity — a *normalised genus-zero canonical product with no nonconstant zero-free exponential factor* (the prover's sharpening; a factor e^{cu} would change N_1 alone). It is a supertrace sequence of a finite graded matrix iff Z is rational with Z(0)=1, even net spectrum = reciprocal poles, odd net spectrum = reciprocal zeros.
- Lead: apply the criterion to the completed zeta itself — xi is entire of order one, *not* genus zero, so a literal trace-class realisation of the zeta side is excluded by this criterion; that is the clean way to say why a Hadamard-product-of-genus-1 object cannot be a naive transfer trace.
- Related: L03-007, L03-009, L03-023

### L03-009 Curve counts are never an MPS ring norm (positive genus)
- Source: `astra-brief.md`:17 (T3(d)(ii)); `astra-proofs.md`:341–368 (T3.3)
- Raised by: orchestrator (Claude); proved by codex prover; independently reproduced by Opus reviewer (review:140–142)
- Status at last mention: registered, `proved-here` for the MPS contraction
- Content: for a translation-invariant MPS with fixed local tensor A, <Psi_n|Psi_n> = Tr(E_A^n) with E_A = sum_s A_s ⊗ conj(A_s) a genuine finite matrix; T3.1 then forbids it from equalling #C(F_{q^n}) for a curve of genus >= 1. The reviewer closed two loopholes explicitly: an infinite physical index is covered by the trace-class half, and an n-dependent gauge is outside the hypothesis. The reviewer also ran an independent Prony fit on `q=3, a=(0,1)` and recovered four negative integer multiplicities.
- Lead: any future cMPS candidate must therefore either be graded or have an n-dependent tensor; those are the only two escapes the theorem leaves.
- Related: L03-007, L03-024, L03-054

### L03-010 Graph vs curve: "the sign" is exactly whether the zeta has a numerator
- Source: `astra-brief.md`:17 (T3(d)(iii), "Deligne's third ingredient in the notebook's language"); `astra-proofs.md`:341–368 (T3.3 ⟨1⟩3)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, proved, with pedantry added
- Content: for a finite (q+1)-regular graph the non-backtracking counts Tr T^l are trivially a trace sequence and the Ihara zeta 1/det(1-uT) has no finite zeros; the graph case needs no grading, the curve case does. The prover adds the caveat that 1/det(1-uT) does have a zero at infinity as a rational function on the sphere, and warns that this "is not a general criterion for physical fermions".
- Lead: none stated. But the dichotomy is the cleanest available statement of what is special about RH relative to the Ramanujan-graph analogy the whole notebook is built on.
- Related: L03-009, L03-053, L03-055

### L03-011 The corrected prime part of the zero trace (the sign correction)
- Source: `astra-brief.md`:3 (obs:ringnorm-sign-correction), :19; `astra-proofs.md`:381–419 (T4.1, eq. 4.2), 1290
- Raised by: TJO/notebook (as an observation), verified by codex prover, independently reconfirmed numerically by Opus reviewer (review:160–171)
- Status at last mention: registered, `conditional-on` the zeta inputs; the reviewer rejected all three plausible wrong variants by 3–4 orders of magnitude
- Content: Tr_dist Z(t) = 1 - 2 P_+(t) - e^{-t/2}/(e^t - 1), where P_+(t) = sum_{n>=2} (Lambda(n)/n) delta(t - 2 log n). The prime part carries coefficient **-2**, not -1 and not +2, and the full distribution is *not* supported only at prime lengths. This replaces the report's earlier positive zero trace.
- Lead: none stated — it is a correction that all downstream ring-norm statements must respect.
- Related: L03-012, L03-021

### L03-012 The graded generator G whose supertrace is exactly the prime measure
- Source: `astra-brief.md`:19; `astra-proofs.md`:373–419 (T4.1)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, `conditional-on H-LP, H-TRACE, H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC`
- Content: B := C_even ⊕ (K_S ⊕ l²(N_{>=1}))_odd, G := 0 ⊕ B ⊕ diag(-(k+1/2)). Then e^{tG} is a strongly continuous contraction semigroup, its fixed vectors are exactly the even line, and str e^{tG} = 2 P_+(t). This is the concrete object that realises the forced datum of T1.4.
- Lead: promote G from a Hilbert-space semigroup to a trace-preserving generator on an operator algebra — the prover flags exactly this gap ("It is a Hilbert-space semigroup; it has not been shown to be a trace-preserving generator on an operator algebra", `astra-proofs.md`:434).
- Related: L03-004, L03-013, L03-021, L03-024

### L03-013 The ladder's parity is not fixed by positivity
- Source: `astra-brief.md`:19 (T4(b)); `astra-proofs.md`:420–435 (T4.2)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, proved
- Content: C ⊕ K_S alone gives supertrace 2P_+ + A(t) with A(t) = e^{-t/2}/(e^t-1) > 0; counting the trivial-zero ladder as even gives 2P_+ + 2A(t). Both are positive. So positivity alone cannot decide whether the trivial zeros are bosonic or fermionic; only exact equality to 2P_+ pins them (and then they are odd).
- Lead: find a physical or geometric reason (not a positivity reason) to fix the ladder's parity. It is the one parity in the whole picture that the arithmetic does not force.
- Related: L03-005, L03-012, L03-021

### L03-014 RH as "all odd K_S modes have real part exactly -1/4"
- Source: `astra-brief.md`:19 (T4(d)); `astra-proofs.md`:436–447 (T4.3)
- Raised by: orchestrator (Claude); restated with corrections by codex prover; confirmed by reviewer (review:187–189)
- Status at last mention: registered as a remark, spectral equivalence `conditional-on H-LP, H-ZETA-LOC`; geometric names `sketched`
- Content: the generator modes are -conj(rho)/2, so Re = -sigma/2 = -1/4 iff sigma = 1/2. The statement is restricted to the odd K_S sector and explicitly *does not* cover the odd trivial-zero ladder, which sits at -(k+1/2). The fixed even line is added by hand and represents the pole of zeta (not of xi, which is entire — a correction the earlier Weil-positivity review also made).
- Lead: none stated; it is the target statement the whole programme is aiming at.
- Related: L03-012, L03-013, L03-016

### L03-015 Identify the even line with the constant function / Eisenstein residue on the modular surface
- Source: `astra-brief.md`:19 (T4(d)); `astra-proofs.md`:436–447 (T4.3)
- Raised by: TJO / orchestrator; flagged as unproved by codex prover
- Status at last mention: raised, not pursued — prover says "Identifying that line with those geometric objects is not a construction made here", status `sketched`
- Content: the even fixed vector is supposed to be "the constant function on the modular surface, the residue of the Eisenstein series at s = 1". Nothing in the campaign constructs that identification; it is a naming convention borrowed from the Lax–Phillips picture.
- Lead: actually construct the isomorphism between the added even line and the Eisenstein residue, which would connect the graded generator to the automorphic side rather than to a bookkeeping device.
- Related: L03-014, L03-016

### L03-016 H-LP is assumed, never constructed — the biggest unaudited input
- Source: `astra-proofs.md`:369 (H-LP), 1332 (inventory), 1355; review:486, 748
- Raised by: codex prover (as a scope flag); endorsed by Opus reviewer
- Status at last mention: open — "Not constructed or analytically validated here"
- Content: the whole Riemann-channel side rests on H-LP: that Z(t) = e^{tB} is a strongly continuous contraction semigroup on the model space K_S with pure point spectrum {-conj(rho)/2}, one eigenvector per zero, and Z(t) -> 0 strongly. The prover states explicitly that nothing "independently establishes innerness of that symbol [S(tau) = xi(1-2i tau)/xi(1+2i tau)], completeness of its asserted modes, or the asserted geometric identification".
- Lead: prove innerness of S and completeness of the mode system from the functional equation. The reviewer separately found (review:748) that H-LP had *disappeared from the dependency chain* of the channel branch of the lab book and must be re-declared.
- Related: L03-014, L03-015, L03-049

### L03-017 The vacuum-decay Lindbladian: a genuine channel with the zeros as odd coherences
- Source: `astra-brief.md`:21; `astra-proofs.md`:450–517 (T5.1), 538–553 (T5.3)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, `proved-here` (finite model and the infinite absorbing extension); Riemann specialisation `conditional-on H-LP`
- Content: with -(B + B†) = |j><j| and e^{tB} -> 0, the map L(x) = bB x + x bB† + J x J† on B(C ⊕ H) with J = |vac><j| is a CPTP generator whose unique stationary density is |vac><vac|; its spectrum is {0} ⊎ {b_i} ⊎ {conj b_i} ⊎ {b_i + conj b_j}, the two coherence lists odd and the rest even. T5.3 extends this to any strongly stable contraction semigroup with **no bounded exit vector needed** — which matters because H-LP supplies none.
- Lead: this is the only honest *channel* (as opposed to Hilbert-space semigroup) in the campaign carrying the zeros. Next step: find a variant whose stationary state is not pure.
- Related: L03-019, L03-020, L03-031, L03-051

### L03-018 The zeros appear *twice* in the vacuum-decay channel, not once
- Source: `astra-proofs.md`:554–570 (T5.4), 1299–1300; review:230–234, 605
- Raised by: codex prover (as a correction to the brief's T5(d)); emphasised by Opus reviewer
- Status at last mention: pursued, negative for the identification with T4's datum
- Content: the odd spectrum is spec(B) ∪ conj spec(B); since the zeta multiset is conjugation invariant, each value -conj(rho)/2 occurs with total multiplicity **2 m_rho**, once on |v_n><vac| and once on |vac><v_n|. T4's forced datum has nu = -m_rho. So the vacuum-decay channel realises the *double* of the Phantasm's datum, plus an even pair-sum sector T4 does not have at all.
- Lead: halve the coherence sector — e.g. by a reality/self-conjugate constraint on the bond — to get an actual realisation of T4's datum by a channel.
- Related: L03-017, L03-019, L03-051

### L03-019 The pair-sum "form factor" |Tr Z(t)|² — raised and explicitly refused
- Source: `astra-brief.md`:21 (T5(d), "no claim about pair correlation is to be proved"); `astra-proofs.md`:554–570 (T5.4), 1302
- Raised by: orchestrator (Claude); analysed and blocked by codex prover; confirmed by reviewer (review:230–232)
- Status at last mention: pursued, negative / formal only
- Content: the even population modes carry the exponents -(conj(rho_n) + rho_m)/2, whose formal trace looks like the form factor sum_{n,m} e^{-(conj rho_n + rho_m)t/2} = |Tr Z(t)|². The prover shows this is *not* a distribution: the diagonal pair values -Re(rho_n) accumulate in a bounded interval, violating (G2), and a product of the distributional traces is undefined. "No pair-correlation conclusion follows."
- Lead: if one wanted pair correlation (Montgomery/GUE) out of this picture, one would first need a regularised pairing that respects (G2) — e.g. a smeared form factor with a test function, which is the standard number-theoretic move anyway.
- Related: L03-018, L03-035

### L03-020 The SHW renewal equation is *not* solved by the vacuum (HANDOFF item 0b)
- Source: `astra-brief.md`:21 (T5(e)); `astra-proofs.md`:571–592 (T5.5), 1303
- Raised by: orchestrator (Claude), from HANDOFF item 0b; refuted by codex prover; reproduced numerically by reviewer (review:241)
- Status at last mention: **dead as drafted** — the brief's claim "the fixed-point equation rho_infty ∝ int_0^infty Z(t) Omega Z(t)* dt is solved by Omega itself" is false
- Content: J Omega = 0 and e^{t bB} Omega e^{t bB†} = Omega, so int_0^T ... dt = T Omega, which diverges; in the original K_S the equation is not even type-correct, since Omega lives in the added line. The vacuum is an absorbing, non-emitting state with infinite holding time, so the no-event semigroup on the enlarged space is not strongly stable.
- Lead: the prover states what would be needed: "a nontrivial rebound inside K_S" with finite holding time. That is a concrete design constraint on the next channel candidate.
- Related: L03-017, L03-031, L03-051

### L03-021 A supertrace is not a norm — the campaign's central honesty caveat
- Source: `astra-proofs.md`:11, 436–447 (T4.3), 1292–1293
- Raised by: codex prover
- Status at last mention: raised, standing objection to the whole reframe
- Content: verbatim: "assigning a negative spectral multiplicity does not construct a fermionic cMPS or identify a supertrace with its ordinary norm"; and "an even eigenvalue 1 and an odd eigenvalue 2 give supertrace -1"; and "A parity insertion requires a specified physical construction and boundary convention before any norm claim can be made." Also: for fixed t > 0 every asserted eigenvalue of Z(t) has modulus at least e^{-t/2}, so Z(t) is not compact and not trace class; and a finite-dimensional ordinary cMPS transfer has an *analytic* ring-norm function of length (by the earlier Dyson theorem) and can never equal a nonzero atomic prime measure.
- Lead: the concrete missing object is a boundary condition / parity-insertion convention on a ring that turns a genuine Hilbert norm into a supertrace. That is the single most valuable target in the lane.
- Related: L03-001, L03-012, L03-024

### L03-022 No all-even datum can have supertrace 2P_+ or comb
- Source: `astra-proofs.md`:420–435 (T4.2 ⟨1⟩2)
- Raised by: codex prover
- Status at last mention: registered, proved
- Content: T1.4 forces negative net multiplicity at every zero and every ladder value; an all-even datum has only nonnegative net multiplicities. So a *bosonic* bond is impossible, independently of positivity arguments. This is the cleanest "the bond must be graded" statement in the file.
- Related: L03-004, L03-005, L03-007

### L03-023 Zeta's genus-one Hadamard product vs the genus-zero criterion
- Source: `astra-proofs.md`:311–340 (T3.2 claim 1 and its "no nonconstant zero-free exponential factor" clause), 1287; review:132
- Raised by: codex prover (as a sharpening); reviewer confirmed necessity
- Status at last mention: noted, not pursued as a zeta statement
- Content: the trace-class criterion requires 1/Z(u) to be *exactly* a normalised genus-zero canonical product; a factor e^{cu} is excluded because it changes N_1 alone while leaving all N_n (n >= 2) unaltered. Nobody in the file applies this to xi, whose Hadamard product has genus one.
- Lead: state the corollary explicitly — the completed zeta cannot be 1/det(1 - u E) for any trace-class E, for genus reasons, independently of the sign/numerator argument. A second, independent no-go.
- Related: L03-008, L03-007

### L03-024 A cMPS with this bond has trivial entanglement (pure fixed point)
- Source: `astra-brief.md`:21 (T5(e) last sentence); `astra-proofs.md`:571–592 (T5.5), 1304
- Raised by: orchestrator (Claude); proved by codex prover under H-CMPS and *also directly*; reproduced by reviewer (review:242)
- Status at last mention: pursued, negative
- Content: the stationary bond state is rank one, so the nonzero Schmidt spectrum of the half-chain is {1}. The direct argument is stronger and needs no H-CMPS: every ring amplitude containing a jump vanishes, because the jump maps into the vacuum, further jumps annihilate it, and the no-event operator preserves the two blocks. So the only periodic field configuration is the vacuum.
- Lead: the Phantasm needs a bond with a *nontrivial* entanglement spectrum (ideally the ring lengths). This proposition says the vacuum-decay construction cannot supply it — so the next candidate must have a mixed stationary bond.
- Related: L03-017, L03-020, L03-026, L03-051

### L03-025 Normal KMS states exist only above the Bost--Connes transition
- Source: `astra-brief.md`:23 (T6(a)); `astra-proofs.md`:601–637 (T6.1)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, `proved-here` (type III comparison `conditional-on H-BC-POS`)
- Content: for alpha_t = Ad(N^{it}) on B(l²(N)), a *normal* KMS_beta state exists iff beta > 1 and equals N^{-beta}/zeta(beta). The prover corrects the supplied wording twice: the arithmetic system is the Bost--Connes C*-algebra, not all of B(l²); and the high-temperature range is 0 < beta <= 1, not all beta <= 1.
- Lead: none stated; it is the reason the critical bond cannot be a normal density on this Hilbert space.
- Related: L03-026, L03-030, L03-032

### L03-026 The thermofield double over primes has bond dimension one
- Source: `astra-brief.md`:23; `astra-proofs.md`:601–637 (T6.1 ⟨1⟩2)
- Raised by: orchestrator (Claude); proved by codex prover
- Status at last mention: registered, proved
- Content: rho_beta = ⊗_p [(1-p^{-beta}) sum_k p^{-beta k}|k><k|], and the TFD purification factorises over prime sites: "It has entanglement between left and right at each site, but none between different prime sites." The entanglement spectrum is {beta log n + log zeta(beta)} — the ring lengths, up to the factor beta (T4's ring time uses 2 log n) and an additive constant.
- Lead: bond dimension one along the prime chain means the prime chain carries *no* matrix-product structure to speak of; any interesting bond must come from elsewhere.
- Related: L03-024, L03-030, L03-038, L03-045

### L03-027 The prime-by-prime detailed-balance Lindbladian, and its purely real spectrum
- Source: `astra-brief.md`:23 (T6(b)); `astra-proofs.md`:663–703 (T6.3)
- Raised by: orchestrator (Claude); proved and corrected by codex prover
- Status at last mention: pursued, negative — "This spectrum is real and therefore cannot contain the nonreal Riemann zero generator modes"
- Content: L_beta with isometries mu_p|n> = |pn>, up-rate r_p and down-rate r_p p^beta, restricted to the diagonal, is a product of independent birth--death chains, one per prime. Its spectrum on L²(pi) is the *closure* of {0} ∪ the finite Minkowski sums of the bands I_p = [-r_p(p^{beta/2}+1)², -r_p(p^{beta/2}-1)²]. The closure is essential (reviewer: the infinite sum of left endpoints converges to about -1.0025 for r_p = p^{-(beta+2)}, so there are spectral limit points in no finite Minkowski sum).
- Lead: dead end as a home for the zeros; the brief's own conclusion is that "the reframe must put the zeros in a different bond".
- Related: L03-028, L03-030, L03-042, L03-052

### L03-028 The off-diagonal sectors of the prime chain are also real
- Source: `astra-brief.md`:23 ("say what you can about the off-diagonal part"); `astra-proofs.md`:704–729 (T6.4)
- Raised by: orchestrator (Claude); proved by codex prover under a stronger rate condition
- Status at last mention: pursued, negative, with a caveat
- Content: under sum_p r_p p^beta < infinity (which the brief's own example r_p = p^{-beta} fails), the full quantum generator is bounded self-adjoint and nonpositive on the KMS-weighted space ||x||_beta = ||rho_beta^{-1/4} x rho_beta^{-1/4}||_HS. Fixed-difference matrix-unit sectors are real symmetric Jacobi matrices. So the quantum part carries no zeros either.
- Lead: the prover flags an explicit gap — "An unbounded quantum closure of the prime-generator example r_p = p^{-beta} is not provided by the bounded proof of T6.4" (`astra-proofs.md`:1355). Somebody could close that case; it is the natural rate choice.
- Related: L03-027, L03-052

### L03-029 "The Bost--Connes transition is ergodicity breaking" — corrected to a weaker statement
- Source: `astra-brief.md`:23 (T6(c)); `astra-proofs.md`:730–765 (T6.5), 1311
- Raised by: orchestrator (Claude); corrected by codex prover; reviewer calls the correction "the most valuable paragraph in T6" (review:298)
- Status at last mention: pursued, corrected — the drafted slogan is not established
- Content: what is proved is (i) escape of the normal Gibbs mass as beta -> 1+ (Tr(P rho_beta) <= rank(P)/zeta(beta) -> 0) and (ii) absence of a stationary probability on finite-support integer configurations below the threshold. What is *not* proved is a spectral gap closing, multiple stationary states of a specified Lindbladian, or loss of dynamical ergodicity. "A claim about a Riemann Lindbladian's ergodicity, gap, or multiple steady states needs a specified generator and is not established."
- Lead: specify a generator and prove an actual gap statement — that is the missing content behind the slogan.
- Related: L03-025, L03-027, L03-052

### L03-030 The critical bond must live somewhere other than the prime chain
- Source: `astra-brief.md`:23 (T6(c), "the reason the reframe must put the zeros in a different bond (T4), not in the prime chain"); `astra-proofs.md`:765 ("The prime Gibbs chain supplies ring-length energies and an independent reversible relaxation model; it supplies no construction of the Riemann zero bond in T4.")
- Raised by: orchestrator (Claude); confirmed by codex prover
- Status at last mention: registered as a structural conclusion
- Content: side A (the prime gas / Bost--Connes chain) gives the ring lengths and a reversible relaxation model with real spectrum; side B (the Riemann channel) gives the zeros. The two are proved not to be the same object.
- Lead: find the map that couples them — the campaign's whole difficulty.
- Related: L03-027, L03-051, L03-052

### L03-031 The absorbing-vacuum channel needs no bounded exit vector — a reusable construction
- Source: `astra-proofs.md`:538–553 (T5.3), 1301
- Raised by: codex prover (as a replacement for the brief's rank-one formula, which fails in infinite dimensions)
- Status at last mention: registered, `proved-here`
- Content: for *any* strongly continuous, strongly stable contraction semigroup Z_t on a separable Hilbert space, formula (5.2) — conjugation by 1 ⊕ Z_t plus the feed X -> Tr[(I - Z_t† Z_t)X] Omega — defines a CPTP semigroup with unique stationary density Omega and exact odd coherence evolution. The brief's rank-one Lindblad formula does not survive to infinite dimension, since H-LP supplies no bounded exit vector or generator-domain identity.
- Lead: this is a general-purpose gadget: given *any* candidate Riemann semigroup, it produces a genuine channel carrying that semigroup as odd coherences. Reuse it on future candidates.
- Related: L03-017, L03-018, L03-016

### L03-032 The M/M/1 spectral theorem proved in-house
- Source: `astra-brief.md`:9 (H-MM1); `astra-proofs.md`:638–662 (T6.2)
- Raised by: orchestrator (as an assumed hypothesis); **proved** by codex prover
- Status at last mention: registered, `proved-here`, promoted from hypothesis to theorem
- Content: conjugate to a Jacobi matrix, identify the band by the sine transform, and handle the boundary by a Sherman--Morrison rank-one resolvent; the only spectral point outside the band is the simple eigenvalue 0.
- Lead: the pattern — "a supplied H-* that turns out to be provable in half a page" — recurs (H-GAUSS, H-STICK, the Weil character-modulus formula). Worth auditing the remaining H-* inventory the same way.
- Related: L03-040, L03-046, L03-049

### L03-033 Reviewer's strengthening: the pole's parity is unconditionally even
- Source: review `riemann-cmps-2026-09-12.md`:90–101, 699, 713–731 (Round 2 re-verdict)
- Raised by: Opus reviewer (a new proof, supplied in the review)
- Status at last mention: registered in the lab book as `prop:parity-infinite-dominated` part (i); Round-2 verdict VALID
- Content: with F_Z possibly infinite, positivity of the supertrace *alone* forces b = 0 (pole even), by monotone convergence of the cutoff pairings: h_{eps,R,s} >= 0 increases pointwise to t^k e^{-st}, so int t^k e^{-st} dmu = R_k(s) >= 0 for real s > 1, while b = 1 makes R_k(s) -> -infinity as s -> 1+. No Landau, no domination premise. The domination premise is needed only for the F_Z = empty half.
- Lead: the reviewer flags a *completeness repair needed elsewhere*: the lab book's `thm:supertrace-rigidity` paragraph must record that the cut-offs are "nonnegative and monotone in both parameters", or part (i) cannot be reconstructed (review:729).
- Related: L03-005, L03-006

### L03-034 Which conjugation-symmetric infinite flip sets survive? (the "density 1/2" heuristic)
- Source: review:98
- Raised by: Opus reviewer
- Status at last mention: raised, not pursued — explicitly could not be turned into a proof or counterexample
- Content: flipping *every* zero gives mu = 2e^u - comb - 2/(e^{2u}-1), whose prime atoms are -Lambda(n) < 0 — positivity fails. Flipping a cofinite set fails the same way; flipping asymmetrically fails by reality. "So the only surviving question is whether a conjugation-symmetric infinite F_Z can have atomic contribution > -Lambda(n) at every prime power, i.e. 'density at most 1/2' in the atom weighting."
- Lead: this is a concrete, self-contained analytic-number-theory question about the distribution of sums of e^{rho u} over sub-multisets of zeros. Solving it closes T2(c).
- Related: L03-006, L03-005

### L03-035 Landau's theorem is toothless here — and exactly why
- Source: `astra-proofs.md`:261–271 (T2.4); review:106–110
- Raised by: codex prover; mechanism verified by Opus reviewer
- Status at last mention: recorded as a dead route for the intended argument
- Content: with b = 0 the abscissa of convergence of int t^k e^{-st} dmu is exactly 1, forced by nu(1) = +1, and s = 1 *is* a singularity — so Landau is satisfied without saying anything at all about the zeros.
- Lead: none; recorded so nobody reruns the Landau argument on mu or on mu + comb.
- Related: L03-006, L03-034

### L03-036 The corrected Artin--Schreier sign law (the radical determinant)
- Source: `astra-brief.md`:25 (drafted law, declared possibly false); `astra-proofs.md`:871–931 (T7.3), 1345–1347; review:328–340
- Raised by: orchestrator (drafted, from 40 brute-force cases); refuted and replaced by codex prover; independently verified 12/12 by Opus reviewer
- Status at last mention: registered, `conditional-on H-NORMAL`; the drafted law is dead
- Content: S_n(g) = (-1)^{n-1} delta_n Tr E_g^n with delta_n = det(S | ker P(S)), where P(z) = sum_j (a_j/2)(z^j + z^{-j}) and S is the cyclic shift. The correction is *the determinant of the shift on the radical*, not the drafted eta(-1)^{d_n}, which depends on the rank alone. The proof introduces the embedding matrix A_{ri} = theta^{q^{r+i}} with A^t = A, A² = C, A^{[q]} = SA, AS = S^{-1}A — identities that use cyclic indices, not diagonalisation, and therefore survive q | n where S is not semisimple.
- Lead: the A-matrix trick (a square root of the trace-form Gram matrix over the algebraic closure, equivariant for Frobenius) looks reusable for any cyclic-module sign computation, not just this family.
- Related: L03-037, L03-039, L03-040

### L03-037 The periodic sign 1 - 2·1[2h | n] and the two endpoint criteria
- Source: `astra-proofs.md`:932–984 (T7.4, eqs. 7.6–7.8); review:342–372
- Raised by: codex prover; verified 12/12 by reviewer including both known FAIL cases
- Status at last mention: registered, proved
- Content: with f(z) = z^J P(z), v_± the vanishing orders of f at ±1 (both always even), and h = the least power of q strictly greater than v_-, the sign is exactly S_n(g) = (1 - 2·1[2h | n]) t_n — a *periodic* function of n. The notebook's claim alpha_i = -lambda_i(E_g) holds for all n exactly when P(-1) != 0 (7.7); the brief's drafted law holds for all n exactly when P(-eta(-1)) != 0 (7.8). These are conditions on the coefficients alone, and they *predict* the observed failures.
- Lead: the criteria are cheap coefficient tests; use them to pick families where the naive transfer works before running any numerics.
- Related: L03-036, L03-041, L03-043

### L03-038 The root-of-unity filter: build the Frobenius spectrum from the transfer spectrum
- Source: `astra-proofs.md`:1046–1113 (T7.7, eqs. 7.9–7.10); review:401–411
- Raised by: codex prover (a construction the brief did not ask for)
- Status at last mention: registered, `conditional-on H-NORMAL, H-AS`
- Content: L(g,T)^h = prod_{omega^{2h}=1} D_g(omega T) / D_g(T)^h, and the reciprocal-root multiplicity is m_{F_g}(z) = (1/h) sum_{omega^{2h}=1} m_E(omega^{-1} z) - m_E(z). So: diagonalise the finite transfer matrix, rotate its eigenvalue multiset by the 2h-th roots of unity, subtract — and you get the Frobenius eigenvalues, with **no Weil root-size input used anywhere** (|alpha| = sqrt q comes from scaled unitarity of the transfer, T7.6).
- Lead: this is a self-contained, finite, constructive recipe for a Frobenius spectrum from a transfer matrix. Worth asking whether an analogue exists on the zeta side — a "rotation and subtraction" that converts a transfer spectrum into the zeros.
- Related: L03-036, L03-039, L03-042

### L03-039 The corrected projective super-transfer, and the character-sector grading
- Source: `astra-brief.md`:25 (T7(d), drafted); `astra-proofs.md`:1115–1166 (T7.8, eq. 7.11), 1312; review:413–424, 505–524 (X1)
- Raised by: orchestrator (drafted); corrected by codex prover; read and repaired by Opus reviewer as statement X1
- Status at last mention: registered; the drafted block is dead (L03-060); the reviewer's repaired reading is `sketched` as `obs:character-sector-grading`
- Content: bbE = (E_0 ⊕ 1)_even ⊕ (⊕_{a != 0} F_{ag})_odd has str bbE^n = #C(F_{q^n}) for all n >= 1, with F F† = q I and odd dimension (q-1)q^J = 2g(C). The grading *is* the trivial-vs-nontrivial additive-character decomposition of the Hilbert-90 fibre sum — with two repairs the reviewer insists on: (i) the point at infinity is **not** a character sector, so the two poles split, T = 1/q from the trivial-character block E_0 and T = 1 from the point at infinity; (ii) the odd summands are the corrected F_{ag}, not E_{ag}; (iii) "carries exactly" is true only of the *nonzero net* spectrum, since E_0 also carries q^J - 1 invisible zero eigenvalues.
- Lead: this is the only place in the whole campaign where the graded picture is completely explicit and completely correct. It is the template any zeta-side construction should imitate.
- Related: L03-038, L03-045, L03-060

### L03-040 The transfer matrix is a Clifford / Weil-representation element
- Source: `astra-brief.md`:25 (T7(e), "E_g/sqrt(q) conjugates every Weyl operator to a Weyl operator up to a phase (Clifford) in every case tested"); `astra-proofs.md`:1167–1208 (T7.9, eq. 7.13); review:426–447
- Raised by: orchestrator (from numerics); proved with an explicit matrix by codex prover; verified index-for-index by Opus reviewer
- Status at last mention: registered, exact covariance and symplecticity `proved-here`; identification with the named W `conditional-on H-WEIL-EXACT`
- Content: E_g/sqrt q factors as (Fourier on the first register, scaled by a_J) ∘ (quadratic phase) ∘ (cyclic permutation) — three Clifford operations — and the composite symplectic matrix M_g in Sp(2J, F_q) is written out explicitly in (7.13). So the Artin--Schreier transfer matrix *is* a finite-dimensional metaplectic/Weil operator.
- Lead: a quadratic exponential sum transfer matrix is a Clifford circuit. That is a genuinely physical statement — it says the prototype "quantum chain" is free/Gaussian, hence efficiently simulable, which may explain why everything here is computable and why the zeta side is presumably not.
- Related: L03-041, L03-042, L03-044

### L03-041 d_n = dim ker(M_g^n - I): the Weil bound saturates iff M_g has order n
- Source: `astra-brief.md`:25 (T7(e)); `astra-proofs.md`:1209–1259 (T7.10, eq. 7.14); review:449–457
- Raised by: orchestrator (Claude); proved directly by codex prover (without assuming the Weil character formula)
- Status at last mention: registered, `proved-here`
- Content: |Tr E_g^n|² = q^{n + dim ker(M_g^n - I)}, proved by observing that Ad(U_g^n) *permutes* the q^{2J} centred Weyl matrices by M_g^n, so Tr Ad(U_g^n) = #ker(M_g^n - I), and Tr Ad(V) = |Tr V|² for unitary V. Hence |S_n(g)| <= q^J q^{n/2} with equality iff M_g^n = I. Saturation of the Weil bound is a *finite order condition on a symplectic matrix*.
- Lead: "maximality of the curve at level n" becomes "the symplectic matrix has order dividing n" — a purely group-theoretic criterion. Worth pushing: which symplectic conjugacy classes arise as M_g, and what does that say about the distribution of maximal Artin--Schreier curves?
- Related: L03-040, L03-042, L03-043

### L03-042 The fermionic sign is the sign of the Frobenius permutation
- Source: `astra-brief.md`:25 (T7(f)); `astra-proofs.md`:1209–1259 (T7.10 ⟨1⟩3)
- Raised by: TJO / orchestrator (this is the conceptual payoff the brief was fishing for); proved for d_n = 0 by codex prover
- Status at last mention: registered, proved in the nondegenerate case; the general case is the determinant delta_n, not a universal eta(-1)^{d_n}
- Content: when the radical is trivial, S_n(g) = (-1)^{n-1} Tr E_g^n = sgn(Frob_n) Tr E_g^n — "the fermionic sign of the count on a ring of n sites is the sign of the Frobenius permutation". This is the elementary, permutation-level statement of why the curve's count needs a minus sign, i.e. of why the zeros are odd.
- Lead: this is the "permutations before curves" statement TJO wants. Next step: is there a *zeta-side* permutation whose sign plays the same role — i.e. an explicit S_infinity-like object whose signature produces the minus sign in the explicit formula?
- Related: L03-036, L03-041, L03-001

### L03-043 Scaled unitarity of the transfer: E_g E_g† = q I
- Source: `astra-brief.md`:25 ("promotes prop:as-unitarity"); `astra-proofs.md`:1021–1045 (T7.6); review:393–399
- Raised by: notebook / orchestrator; proved with full index bookkeeping by codex prover
- Status at last mention: registered, `proved-here`
- Content: the row inner product collapses because summing the *oldest* input spin z gives q·1[x = x'] whenever a_J != 0. Consequence: every eigenvalue of E_g has modulus sqrt q, semisimple — the Riemann hypothesis for this curve family, obtained from the transfer matrix alone with **no** appeal to Weil.
- Lead: this is the notebook's proof-of-concept that "RH = unitarity of a transfer matrix, up to scale". The analogue on the zeta side would be exactly the Phantasm. Note the prover's separate correction that for J = 0 the minimal transfer is the scalar Gauss sum, not the module's redundant q-state register.
- Related: L03-038, L03-040, L03-051

### L03-044 The de Bruijn even block and its invisible zero eigenvalues
- Source: `astra-brief.md`:25; `astra-proofs.md`:1115–1166 (T7.8 ⟨1⟩3), 1313
- Raised by: orchestrator; proved by codex prover
- Status at last mention: registered, proved
- Content: Tr E_0^n = q^n for all n >= 1; E_0^J is the all-ones matrix and E_0^{J+1} = q E_0^J, so the only nonzero eigenvalue is q, with multiplicity one, and the other q^J - 1 are zero, possibly with nilpotent blocks. These are invisible to every positive power trace — so the even sector can be reduced to the scalar q for trace purposes.
- Lead: "invisible zero eigenvalues and nilpotent blocks" is a general escape hatch that all the trace/supertrace criteria leave open; nobody in the campaign explores what could be hidden there. Could the Phantasm's even sector hide structure in its kernel?
- Related: L03-008, L03-039

### L03-045 The Bost--Connes / Galois analogy: a graded bond would compute the *cover's* zeta
- Source: review:505–524 (X1); `astra-brief.md`:5 (BC reframe)
- Raised by: orchestrator as statement X1; substantially sharpened by Opus reviewer
- Status at last mention: "observation, not a theorem", lab-book status `sketched`
- Content: Gal(Q^ab/Q) = Zhat^× has the Dirichlet characters as its character group; `prop:bc-mpo` gives prime-chain transfer eigenvalues L(beta, conj chi)/zeta(beta) in the character basis; only the principal character's L has a pole at s = 1. So a Galois-symmetric graded bond would have even sector ↔ the pole of zeta, odd sector ↔ the zeros of the L(s,chi). **But** the reviewer's sharpening: in the Artin--Schreier case the graded object computes the zeta of the *cover*, whose numerator is prod_{a != 0} L(ag,T) — *all* nontrivial characters together — not the zeta of the base P¹. So the faithful analogue is the Dedekind zeta of Q(zeta_N), not zeta alone.
- Lead: testable consequence, stated by the reviewer: by T1.2, a graded datum with supertrace 2P_+ has *only* the zeta zeros; a datum carrying the zeros of all L(s,chi) has a different supertrace (the ray-class prime comb). **The two cannot both hold for the same bond.** So either the Galois analogy or the 2P_+ normalisation has to give. Deciding which is a concrete next step.
- Related: L03-039, L03-046, L03-030

### L03-046 prop:bc-mpo gives *values* of L, not zeros
- Source: review:522 (caveat (i))
- Raised by: Opus reviewer
- Status at last mention: raised as a caveat, not pursued
- Content: "`prop:bc-mpo` is `sketched`, and its eigenvalues L(beta, conj chi)/zeta(beta) are *values* of L at a fixed beta, not *zeros* of L; nothing in the notebook puts any L-zero into the prime chain."
- Lead: if one wanted L-zeros in the prime chain, one would have to vary beta and look for a spectral, not a value, statement. Nobody has tried.
- Related: L03-045, L03-027

### L03-047 The prime chain demonstrably is *not* the Galois-graded bond
- Source: review:522 (caveat (ii))
- Raised by: Opus reviewer
- Status at last mention: pursued, negative
- Content: T6.3/T6.4 prove the prime-chain generator's spectrum is real (classically in general, and for the full generator on the weighted space under sum r_p p^beta < infinity), so the existing prime-chain construction *cannot* be the Galois-symmetric graded bond the analogy imagines. "The analogy is a research direction, not a corollary."
- Related: L03-045, L03-027, L03-030

### L03-048 Hagedorn temperature = Bost--Connes transition; the spectrum is not Cardy
- Source: review:589–597 (X2d); `astra-brief.md`:23 (context)
- Raised by: orchestrator as statement X2(d); checked and refined by Opus reviewer
- Status at last mention: registered, VALID
- Content: the number of entanglement levels below E is exactly floor(e^E) — exponential (Hagedorn) growth. The Hagedorn temperature is beta_H = 1 "because sum_n e^{-beta log n} = zeta(beta) converges iff beta > 1 — which is the *same* threshold as the Bost--Connes transition, and that is the substantive point." Against Cardy's exp(2 pi sqrt(cE/6)): at E = 20, 4.85e8 vs 9.6e4.
- Lead: consequence — the CFT finite-entanglement-scaling law S = (c kappa/6) log chi does **not** apply to this bond, so no CFT central charge can be read off. The independent signature is the log log N term in the truncated entropy (L03-050). If someone later wants to claim a CFT dual for the prime gas, this is the obstruction to beat.
- Related: L03-049, L03-050, L03-026

### L03-049 Entropy constants of the Gibbs state, fixed by the review
- Source: review:530–543 (X2a), 544–563 (X2b), 565–587 (X2c), 702, 764
- Raised by: orchestrator as statement X2(a)–(c); constants determined by Opus reviewer
- Status at last mention: registered as `num:bc-entropy`; Round-2 VALID, with a db-drift note
- Content: (a) S(rho_beta) = 1/(beta-1) + log(1/(beta-1)) + (1 - gamma) + o(1), with 1 - gamma = 0.42278434 (the brief's two-term form invites the false reading S - A - B -> 0). (b) With a prime cutoff p <= P at beta = 1, the constant is **exactly 0** — the two Mertens constants cancel identically, -gamma from sum log p/(p-1) - log P and +gamma from sum -log(1-1/p) - log log P. (c) With a bond cutoff n <= N, the constant is -gamma/2 = -0.288608, and the numerically observed -0.25 is the 0.671/log N correction, not the limit.
- Lead: (b) is "a pretty fact and worth stating with the cancellation visible rather than as a numerical near-zero". Bookkeeping lead: the `db/claims.tsv` statement column for `num:bc-entropy` still lacks the constants (review:764) and the gate will not catch the drift.
- Related: L03-048, L03-026

### L03-050 The log log N term as the signature of non-CFT entanglement scaling
- Source: review:593 (X2d), 585 (X2c)
- Raised by: Opus reviewer
- Status at last mention: raised, one sentence, not developed
- Content: the truncated entropy (1/2) log N + log log N - gamma/2 "is **not** of the form alpha log chi — the log log N term is the departure". The approach to the limit is logarithmically slow, so "no amount of direct summation will display it".
- Lead: the log log N term is a computable, falsifiable fingerprint. If a future bond is proposed for the prime gas, check whether its finite-chi entropy carries this term.
- Related: L03-048, L03-049

### L03-051 The complementary-halves statement: neither construction has both properties
- Source: review:599–611 (X3), 733–760 (Round 2 re-verdict); `astra-proofs.md`:1340–1355 (T8.1)
- Raised by: orchestrator as statement X3; three repairs supplied by Opus reviewer
- Status at last mention: registered as `obs:complementary-halves`; Round-2 VALID **conditional on a dependency repair**
- Content, as finally worded: "The vacuum-decay channel has the zeros as odd relaxation modes (each zero twice, as a coherence and its conjugate, plus an even pair-sum sector) but a pure stationary state, hence trivial entanglement. The prime-chain Gibbs Lindbladian, for beta > 1, has rho_beta as stationary state, with entanglement spectrum beta log n + log zeta(beta), proportional to the ring lengths 2 log n, but a real spectrum with no zeros ... No construction in this book has both, and the Phantasm would need both."
- Lead: the sharpest statement of what is missing. The reviewer also notes the last clause is *definitional, not a theorem* and should be labelled as such. Concrete design brief for the next candidate: a channel with a mixed stationary bond whose entanglement spectrum is the ring lengths and whose odd relaxation spectrum is the zeros, once each.
- Related: L03-017, L03-024, L03-027, L03-030

### L03-052 Dependency repair: the lab book's channel branch had lost H-LP
- Source: review:741–758 (Round 2), 748
- Raised by: Opus reviewer
- Status at last mention: prescribed repair; verdict reverts to MINOR if not applied
- Content: `obs:complementary-halves` was recorded `proved` while its first clause rests only on `obs:zero-coherences-populations`, which is `sketched`; and `prop:absorbing-vacuum-channel` was `proved` with `deps = -` although its Riemann specialisation needs `asm:lax-phillips-modes`. Prescription: add `asm:lax-phillips-modes` to `prop:absorbing-vacuum-channel`, and add `obs:zero-coherences-populations` + `prop:prime-chain-offdiagonal` to `obs:complementary-halves`; the gate then demotes the status automatically.
- Lead: general methodological point the reviewer makes — "in this book the printed status is *derived* from the deps and a wrong dep list silently promotes a claim". Worth a gate check that flags any `proved` row whose text mentions "zeros" but whose deps contain no zeta input.
- Related: L03-016, L03-051

### L03-053 Theorem 1 of the quantum-Ihara note is a loop-admitting *extension* of Watanabe--Fukumizu, not an instance
- Source: `notes/reviews/round2-2026-09-12.md`:78, 116–126
- Raised by: Opus reviewer (round-2 provenance check); fix applied by the author of the note
- Status at last mention: registered; verdict VALID; Theorem 1 and Corollaries 2–4 promoted `sketched` -> `proved` (round2:279)
- Content: WF's graphs are hypergraphs whose hyperedges are 2-element subsets of V (`1103.0605:section2.tex:17-25`), so a loop {i} is not an edge and F is a set (no multiple edges). A bouquet — one vertex, all edges loops — is therefore *not* one of their graphs, and their arbitrary-weight corollary does not apply to it. The notebook's Theorem 1 covers it. "SPECIAL CASE" was removed from both notes.
- Lead: this is a genuinely new matrix-weighted Ihara--Bass formula for the bouquet. Its natural next question: does the loop-admitting extension have a Bass-type determinant proof, and does it degenerate correctly to WF on loopless graphs?
- Related: L03-010, L03-054, L03-055

### L03-054 Corollary 2: MPS ring norms as an Ihara-type Euler product
- Source: `round2-2026-09-12.md`:14–15, 231–236
- Raised by: the note's author; re-derived independently by Opus reviewer
- Status at last mention: registered, VALID, promoted to `proved`
- Content: the corollary is stated in the literal |Tr(A_{i_l} ... A_{i_1})|² form; the reviewer verified it for l = 1..5, checked all values real and >= 0, checked the Euler product over primitive classes truncated at |w| <= 6 (3.6e-7, consistent with truncation), and checked the norm bound min_k ||A_k||^{-2} = (max_i ||E_ī E_i||)^{-1/2}.
- Lead: this is precisely a *ring-norm* generating function with an Euler product — i.e. side A's object built from an MPS. It connects directly to L03-009 (which says curve counts are *not* such norms). Worth asking what arithmetic-like zetas *are* realisable this way.
- Related: L03-009, L03-053, L03-055

### L03-055 Corollary 3 (unitary case) and Corollary 4 (D = 2)
- Source: `round2-2026-09-12.md`:39, 42–59
- Raised by: the note's author; verified symbolically by Opus reviewer
- Status at last mention: registered, VALID, promoted to `proved`
- Content: Corollary 3 assumes E_ī = E_i^{-1} and produces an exponent N(D-2)/2 against -N; the cancellation is total exactly at D = 2. Corollary 4: for D = 2 the non-backtracking operator is simply T = E_1 ⊕ E_2, because the only non-backtracking successor of i is i itself, and Theorem 1 then expresses the product through the single pair factor det_V(1 - u² E_2 E_1).
- Lead: the unitary case E_ī = E_i^{-1} is the "Ramanujan-like" case (a quantum walk); the D = 2 degeneration is the sanity check. Neither is pushed further.
- Related: L03-053, L03-054, L03-010

### L03-056 Norm convention undefined in the quantum-Ihara note (N1)
- Source: `round2-2026-09-12.md`:38, 245
- Raised by: Opus reviewer
- Status at last mention: **not fixed** — the one round-1 item still open
- Content: ||·|| appears in the bound (max_i ||E_ī E_i||)^{-1/2} and in the Neumann step but is defined nowhere; for an arbitrary norm, ||X|| < 1 does not give 1 - X invertible (rescale any norm by 1/10 and take X = 1) — the Neumann step needs submultiplicativity.
- Lead: add "||·|| denotes the operator norm on End(V)" to §1. Cosmetic but currently a genuine gap.
- Related: L03-053

### L03-057 Residual cosmetic issues N2–N7 in the quantum-Ihara note and script
- Source: `round2-2026-09-12.md`:246–251
- Raised by: Opus reviewer
- Status at last mention: raised, fixes prescribed, not applied at time of writing
- Content: N2 — "the set of admissible u is cofinite" asserted without its one-line reason (the excluded set is the zero locus of prod_p det(1 - u² E_ī E_i), a polynomial equal to 1 at u = 0). N3 — "such u" under-states the theorem's own pointwise form. N4 — the target-vs-source edge-weighting claim is the one claim in the new paragraph with no address; cite `1103.0605:section3.tex:162-169` and `:185-193`. N5 — the sympy `exact_check` still evaluates only the 1 - uM(u) form, not the displayed 1 + D - A form. N6 — case (a) runs at two values of u, not three. N7 — `w5` assigned twice, and `exact_check` draws from the same RNG stream as the float checks, so the "exact" instances are not reproducible independently of execution order; seed it separately.
- Lead: each is a one-line fix; N5 and N7 are the two that affect reproducibility.
- Related: L03-053, L03-056

### L03-058 Reversal of non-backtracking words is a bijection because sigma is an involution
- Source: `round2-2026-09-12.md`:83, 99–105
- Raised by: the note's author (as a convention wash-out); re-derived and checked exhaustively by Opus reviewer
- Status at last mention: registered, correct
- Content: WF compose a prime cycle as u_{e_1} ... u_{e_k}, the reverse of the note's E_{i_l} ... E_{i_1}. Reversal is an involution on the admissible (cyclically non-backtracking) set, preserves length and primitivity, and commutes with rotation classes — checked exhaustively at D = 6 for l = 2,3,4,5. Combined with det(1 - XY) = det(1 - YX) for the target-vs-source weighting, both convention differences wash out of det(1 - u·).
- Lead: the "reversal is a symmetry of the word set" observation is the graph-side analogue of the functional-equation symmetry rho -> 1 - rho; worth noting in case the analogy is ever pushed.
- Related: L03-053, L03-010

### L03-059 A cited proof is not in the local refs (NeurIPS supplement)
- Source: `round2-2026-09-12.md`:253–255
- Raised by: Opus reviewer
- Status at last mention: recorded, "no claim leans on it"
- Content: `1103.0605:section3.tex:374-375` points to a hypergraph-free proof of `cor:IBfornonhyper` in the NeurIPS 2009 supplement, which is not in `refs/src/`.
- Lead: fetch it if the loop-admitting extension is ever written up for publication — it is the closest prior art to Theorem 1.
- Related: L03-053

### L03-060 The H-BC-POS type-III_1 citation overreaches its local evidence
- Source: review:490, 700; `astra-proofs.md`:597
- Raised by: Opus reviewer
- Status at last mention: fixed in round 2 — `cit:bc-kms-unique` now claims only uniqueness for 0 < beta <= 1 plus the beta > 1 Gibbs classification
- Content: the only byte-verified local support (`math/0404128`) labels the **critical temperature** as type III_1, i.e. beta = 1, not the whole range 0 < beta <= 1. The prover's attribution line was honest ("as supplied; no external source was consulted") and nothing downstream depends on the clause, but the hypothesis as written asserted more than the evidence carried.
- Lead: byte-verify the type III_1 claim against Bost--Connes 1995 itself if it is ever needed for anything load-bearing.
- Related: L03-025

### L03-061 Proving supplied hypotheses instead of citing them (H-GAUSS, H-STICK, the Weil character modulus)
- Source: `astra-proofs.md`:798–827 (T7.1), 871–931 (T7.3 ⟨1⟩2, which proves H-STICK), 1209–1259 (T7.10 ⟨1⟩1, which proves the H-WEIL-REP character clause), 638–662 (T6.2 proving H-MM1); review:336, 493, 453, 654
- Raised by: codex prover (a working method); endorsed by Opus reviewer
- Status at last mention: registered as a methodological result
- Content: four hypotheses supplied in the brief turned out to be provable in-file, and in two cases (H-STICK, and the Weil character-modulus formula) the byte-verified quote that would have supported them **does not exist in the repository's sources** — the reviewer records that the wanted Stickelberger statement "was not found verbatim in any arXiv TeX source" (review:336, and `notes/extract/riemann-cmps-sources.md` §F). Proving them removed the provenance problem entirely.
- Lead: adopt this as policy — when a byte-verified quote is missing, try proving the statement before weakening the claim that depends on it.
- Related: L03-032, L03-036, L03-041, L03-060

---

## Small but possibly consequential

1. **L03-023 — zeta's genus-one product vs the genus-zero trace criterion.** The criterion is stated and proved but never applied to xi; doing so gives a second, sign-independent no-go for a trace-class transfer realisation of zeta.
2. **L03-034 — the "density at most 1/2" question.** One sentence in the review, but it is the *entire* remaining content of T2(c), and it is a self-contained analytic question about sub-multisets of zeros.
3. **L03-042 — the fermionic sign is the sign of the Frobenius permutation.** Mentioned in the brief and proved only in the nondegenerate case; it is the most elementary, most TJO-shaped statement in the lane ("permutations before curves") and nobody has looked for the zeta-side permutation.
4. **L03-040 — the transfer matrix is a Clifford circuit.** Proved but never interpreted: it says the finite-field prototype is a free/Gaussian quantum chain, which may be exactly why it is tractable and the zeta side is not.
5. **L03-041 — Weil-bound saturation = finite order of a symplectic matrix.** Turns maximality of Artin--Schreier curves into a conjugacy-class question in Sp(2J, F_q); nobody asks which classes occur.
6. **L03-044 — invisible zero eigenvalues and nilpotent blocks.** Every trace/supertrace criterion in the file explicitly cannot see them; that is an unexplored place for the Phantasm's even sector to hide structure.
7. **L03-013 — the ladder's parity is free.** The one parity the arithmetic does not fix; a physical argument that fixes it would be new information, not bookkeeping.
8. **L03-045 last clause — the cover-zeta test.** A graded bond carrying all Dirichlet L-zeros and a graded bond with supertrace 2P_+ are provably different objects. That is a cheap, decisive test on any future Galois-symmetric proposal.

---

## Dead routes recorded

- **The drafted Artin--Schreier sign law** S_n(g) = -(-eta(-1))^n conj(Tr E_g^n). False in general; exact counterexamples at (q,a,n) = (3,(2,1),1) and (5,(1,1),2), i.e. already for n prime to q. `astra-brief.md`:25; `astra-proofs.md`:985–1020 (T7.5), 1346–1347; review:374–391. Valid iff P(-eta(-1)) != 0.
- **The notebook's `prop:as-transfer-matrix` claim alpha_i = -lambda_i(E_g).** Declared false in the brief itself ("THAT CLAIM IS FALSE IN GENERAL"); the exact unconditional coefficient criterion is P(-1) != 0. `astra-brief.md`:3; `astra-proofs.md`:932–984 (7.7), 1348–1349.
- **The drafted universal super-transfer block** -eta(-1) ⊕_{a != 0} E_{ag} in the odd sector. Disproved by an exact point count: for q = 3, g = 2x² + x⁴, the true N_1 = 10 while the draft gives -2 (and 298 vs 190 at n = 5). `astra-proofs.md`:1115–1166 (T7.8 ⟨1⟩5), 1312; review:413–424.
- **The rebound/renewal fixed point rho_infty ∝ int_0^infty Z(t) Omega Z(t)* dt solved by Omega.** False: the integral equals T·Omega and diverges, and in the original K_S it is not even type-correct. `astra-brief.md`:21; `astra-proofs.md`:571–592 (T5.5 ⟨1⟩1), 1303.
- **The rank-one Lindblad formula for the infinite-dimensional Riemann case.** H-LP supplies no bounded exit vector or generator-domain identity; the finite formula does not extend. Replaced by the absorbing-vacuum construction. `astra-proofs.md`:538–553 (T5.3), 1301.
- **Landau's theorem applied to mu or mu + comb to force infinite parity rigidity.** Toothless: the abscissa is already 1 from the pole and s = 1 is a genuine singularity, so Landau says nothing about the zeros. `astra-proofs.md`:261–271 (T2.4); review:106–110.
- **The single-cosine oscillation argument in T2(b).** "A cosine cannot be considered independently of other terms of the same growth"; replaced by a mean/mean-square argument on the whole leading trigonometric polynomial. `astra-proofs.md`:1281; review:77.
- **Pairing a distribution on (0, infinity) directly with t^k e^{-st}.** Not defined; needs the common-cutoff construction. `astra-proofs.md`:1275.
- **The imaginary-part-only integration by parts in T1(a).** Derivatives of e^{(Re lambda)t} are not uniformly bounded from an upper bound on Re lambda alone; the full complex lambda is needed. `astra-proofs.md`:1274; review:22.
- **The prime chain as a home for the zeros.** Its spectrum is real: unconditionally for the classical/diagonal part, and on the KMS-weighted space for the full generator under sum_p r_p p^beta < infinity. `astra-proofs.md`:663–729 (T6.3, T6.4); review:273–292, 522.
- **"The Bost--Connes transition is ergodicity breaking" as a statement about a Riemann Lindbladian.** Not established; what is proved is loss of normalisability of the stationary law. `astra-proofs.md`:730–765 (T6.5), 1311.
- **|Tr Z(t)|² as a form factor / route to pair correlation.** Not a distribution: the pair list violates (G2) and the product of distributional traces is undefined. `astra-proofs.md`:554–570 (T5.4), 1302.
- **The vacuum-decay channel as a realisation of T4's forced datum.** It realises the *double* (each zero twice) plus an even pair-sum sector T4 does not have. `astra-proofs.md`:554–570, 1299–1300; review:605.
- **A cMPS with the vacuum-decay bond as a source of entanglement.** The stationary bond is pure, Schmidt spectrum {1}; every ring amplitude containing a jump vanishes identically. `astra-proofs.md`:571–592 (T5.5 ⟨1⟩2), 1304; review:242.
- **Any ordinary (ungraded) fixed-finite-bond translation-invariant MPS as a source of positive-genus curve counts.** Excluded, including within the quadratic Artin--Schreier family itself. `astra-proofs.md`:341–368 (T3.3 ⟨1⟩2), 1286.
- **The module's J = 0 transfer convention.** For J = 0 the minimal transfer is the scalar quadratic Gauss sum; the module's redundant q-state register adds spurious zero eigenvalues and is not the claimed one-dimensional scaled unitary. `astra-proofs.md`:760–765, 1315.
- **Assuming a self-dual normal basis.** It does not exist for even n, and even n is the whole point of the corrected sign law; only the existence of a normal basis is used. `astra-proofs.md`:1316; review:494.
- **"Phase" as a characterisation of a Weil implementer.** Arbitrary label-dependent phases allow multiplication by a Weyl displacement and change traces; only the *centred*, exactly phase-free covariance determines the implementer up to a scalar. `astra-proofs.md`:780–789 (H-WEIL-EXACT), 1350; review:444.
- **The claim "the trivial character sector carries exactly the two poles" (statement X1 as drafted).** The point at infinity is not a character sector; the poles split, T = 1/q from E_0 and T = 1 from infinity. review:512.
- **"Watanabe--Fukumizu's corollary as a special case" framing of the quantum-Ihara Theorem 1.** A bouquet is not a WF graph (their hyperedges are 2-element subsets, so loops and multiple edges are excluded); the theorem is a loop-admitting extension. `round2-2026-09-12.md`:78, 116–126.
