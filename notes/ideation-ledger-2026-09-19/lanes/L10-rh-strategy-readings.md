# Lane L10: RH strategy review 2026-09-19, Lindblad readings, small reviews

Scope: the five-lane multi-agent RH-strategy review of 2026-09-19 (several lanes stopped
mid-work at the user's request), two reading notes on Lindbladian mixing papers, and three
small source/review files. This ledger records *ideas, leads, proposals, dead routes and
next-step items only* — not the established mathematics.

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| notes/rh-strategy-2026-09-19/SYNTHESIS.md | 84 | yes | 16 (L10-001..016) |
| notes/rh-strategy-2026-09-19/SESSION.md | 22 | yes | 1 (L10-017) |
| notes/rh-strategy-2026-09-19/RECOVERY.md | 53 | yes | 1, operational only (L10-018) |
| notes/rh-strategy-2026-09-19/cusp-bridge.md | 128 | yes | 18 (L10-019..036) |
| notes/rh-strategy-2026-09-19/positivity-products.md | 168 | yes | 17 (L10-037..053) |
| notes/rh-strategy-2026-09-19/graded-channels.md | 172 | yes | 18 (L10-054..071) |
| notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md | 183 | yes | 16 (L10-072..087) |
| notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md | 160 | yes | 12 (L10-088..099) |
| notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md | 59 | yes | 5 (L10-100..104) |
| notes/extract/2609.12284-reading.md | 219 | yes | 11 (L10-105..115) |
| notes/extract/2609.13121-reading.md | 175 | yes | 12 (L10-116..127) |
| notes/extract/shw-unbounded-generators-sources.md | 133 | yes | 5 (L10-128..132) |
| notes/extract/bc-symmetry-sources.md | 55 | yes | 3 (L10-133..135) |
| notes/reviews/provenance-2026-09-12.md | 367 | yes | 8 (L10-136..143) |
| notes/reviews/theorem1-algebra-2026-09-12.md | 187 | yes | 6 (L10-144..149) |

Total: 149 entries. Where the same idea recurs across files it has one entry carrying all
source lines (e.g. the Hardy sign correction, observable closure, the nonnormality lemma).

---

## Ideas and leads

### L10-001 The main research target: prime-defined graded cMPS letters whose observable decay modes are the zero divisor
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:7
- Raised by: orchestrator (Claude), restating TJO's steering
- Status at last mention: raised as the programme's target; not achieved
- Content: "Construct prime-defined, graded cMPS letters and a physical field correlation whose observable decay modes are exactly the Riemann zero divisor. Derive their common width from those letters, with a stationary arithmetic bond and a controlled infinite limit." The synthesis is explicit that the repo supplies pieces, not the construction: the letters must come first and the zeros must come out, never be inserted.
- Lead: build the letters from primes, compute the physical two-point function, read off the divisor. If it worked it would be the Phantasm — RH as a decay-width statement about a concrete physical channel.
- Related: L10-009, L10-013, L10-064, L10-069, L10-099.

### L10-002 The relevant object is the observable odd *subquotient*, not the full odd transfer spectrum
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:9; graded-channels.md:108,118; riemann-vs-selberg-cmps.md:126
- Raised by: orchestrator (Claude), from the graded-channels and cMPS lanes
- Status at last mention: partially explored — demonstrated exactly in a finite toy, not in any arithmetic model
- Content: the decay modes that matter may be only those visible to actual field insertions ("determined by field insertions and their reachable/observable spaces"), not every eigenvalue of the odd transfer. A regular fermionic cMPS with a faithful mixed stationary bond can naturally select one decay band in a two-point function. This changes the target from "make all odd rates equal" to "make the observable ones equal".
- Lead: for any candidate arithmetic channel, compute the insertion-generated Krylov space and its observable quotient before looking at the spectrum. It would explain why a channel can have extra fast modes without spoiling RH.
- Related: L10-064, L10-065, L10-088, L10-096.

### L10-003 Candidate first-band flow parameter lambda = rho/2 - 1, desired line Re lambda = -3/4
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:13-21; cusp-bridge.md:7; riemann-vs-selberg-operators.md:19,140
- Raised by: repo (H-CUSP-BRIDGE), carried into the review
- Status at last mention: raised, unproved — the missing cusp first-band identification
- Content: modular scattering zeros sit at `s = rho/2`; if those were geodesic first-band resonances the flow exponent would be `lambda = s-1 = rho/2-1`, so RH would read `Re lambda = -3/4`. The same zeros seen through the Hardy/cMPS model give `b = -conj(rho)/2`, i.e. `Re b = -1/4`. Three different centres (-1/2 Selberg, -3/4 flow, -1/4 model) for three different operators.
- Lead: settle which operator actually carries the divisor before arguing about widths. Consequence: the "same 1/4" language in older shards is ambiguous without this.
- Related: L10-004, L10-019, L10-075, L10-086.

### L10-004 Even under RH the Riemann scattering Laplace parameter is nonreal — the sharpest Riemann/Selberg difference
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:24-28; riemann-vs-selberg-operators.md:18; riemann-vs-selberg-cmps.md:18
- Raised by: orchestrator (Claude) / riemann_selberg_modes lane
- Status at last mention: established as a structural obstruction
- Content: at `s = 1/4 + i gamma/2`, `mu = s(1-s) = 3/16 + gamma^2/4 + i gamma/4`, nonreal for gamma nonzero. So proving the Selberg `mu >= 1/4` gap cannot turn Riemann scattering modes into self-adjoint Laplace eigenfunctions. The Eisenstein Laurent eigenfunctions grow like `y^(1-s)` and are outside L2. The surviving cusp boundary term in integration by parts exactly balances the imaginary part.
- Lead: stop looking for a self-adjointness argument in this sector; look instead for an arithmetic rigidity of resonance widths. Consequence: rules out a whole family of "make it self-adjoint" strategies.
- Related: L10-076, L10-085.

### L10-005 Normalized Eisenstein Gram K_ij = 1/(1 - conj(s_i) - s_j) and the one-exit identity C*K + KC = -11*
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:32; cusp-bridge.md:34-54; riemann-vs-selberg-operators.md:46-58
- Raised by: cusp-bridge lane (new checked deduction)
- Status at last mention: proved (conditional on the repo's Maass–Selberg identity); does not select RH
- Content: the leading truncated Eisenstein Laurent states, normalized by `c_i Y^(1/2-s_i)`, have exactly the Cauchy Gram `K_ij = 1/(1-conj(s_i)-s_j)`, positive definite for any distinct parameters in the strip. With `C = diag(s_i - 1/2)` one gets `C*K + KC = -11*`: a finite one-exit dissipativity identity. But positivity holds for off-line poles too, so it is not RH-sensitive.
- Lead: use the identity as the normalization target and debugging oracle for any proposed arithmetic exit map. Consequence: fixes the shape of the physical model (one escape channel), not its widths.
- Related: L10-023, L10-029, L10-050, L10-079.

### L10-006 Uniform modal width = uniform exit energy per stored modal energy
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:34; positivity-products.md:98-118
- Raised by: positivity_products lane
- Status at last mention: proved as a finite identity; the arithmetic version is the open target
- Content: for a passive realization `A*G + GA = -C*C` with `Av = lambda v`, `-Re(lambda) = ||Cv||^2 / (2 <v,Gv>)`. So proving `||Cv||^2 = 2 kappa <v,Gv>` for every retained resonant mode would force width kappa. This does not need normality of A and does not assert simplicity of zeros.
- Lead: construct C and G arithmetically and prove the modal equality. Warning recorded: defining them from already-centered real zero frequencies is circular.
- Related: L10-047, L10-048, L10-087.

### L10-007 Full centered unitarity in the physical norm is *too strong* and would wrongly exclude valid decay models
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:34; cusp-bridge.md:92; riemann-vs-selberg-operators.md:66,146; riemann-vs-selberg-cmps.md:130
- Raised by: cusp-bridge lane, cross-checked by the graded-channels lane (graded-channels.md:156)
- Status at last mention: proved as a finite lemma; a genuine correction to earlier repo instinct
- Content: with one exit of rank one and `N >= 2` modes all of width 1/4, `B` cannot be normal (its Hermitian part would have to be `-(1/2)I`, rank N, contradicting rank-one exit). Individual eigenmodes have one lifetime; coherent superpositions need not. "Demanding centered unitarity in the *physical* norm would wrongly exclude this physically natural possibility."
- Lead: seek a *second*, arithmetic positive form that orthogonalizes the modes, rather than demanding the physical transfer become unitary after rescaling. Consequence: separates "divisor on the line" (RH) from "unitarizable semigroup" (strictly stronger).
- Related: L10-030, L10-048, L10-086.

### L10-008 Individual prime-power blocks are indefinite — no sum-of-independent-positive-prime-blocks ansatz
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:35; positivity-products.md:24-32
- Raised by: positivity_products lane (new elementary deduction)
- Status at last mention: proved, negative
- Content: one prime power `n=p^k` contributes `Delta K_a(t,u) = w[h_a(t-u)-h_a(t)-h_a(u)]` with `w = Lambda(n)/sqrt(n)`, `a = log n`. On nodes `A, -A` with `a/2 < A < a` this is `w(2A-a)[[0,1],[1,0]]`, eigenvalues `±w(2A-a)`. Indefinite at its first visibility.
- Lead: any positivity proof must use correlated cross-prime/archimedean compensation or a nonlinear update. It does not refute positivity of the total kernel.
- Related: L10-041, L10-045, L10-051.

### L10-009 The four-dimensional regular fermionic cMPS whose two-point function has all poles at Re = -1/4
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:39-49; graded-channels.md:73-82,86-108; riemann-vs-selberg-cmps.md:16,106-116
- Raised by: graded-channels lane, independently dissected by the cmps_decay_comparison lane
- Status at last mention: proved exactly (finite toy); not arithmetic
- Content: bond `C^(2|2)`, `P = Z ⊗ I`, one fermion letter `R = X ⊗ |0><1|`, `H = diag(aX+bZ, cX+dZ)`, `Q = -iH - R*R/2`. At `a=c=d=1/2, b=0` the fermionic two-point resolvent is exactly `8z(z^2+z+1)/[5(8z^4+8z^3+14z^2+6z+1)]`; all four poles have real part -1/4, imaginary parts `±(sqrt7 ± 2)/4`. The full odd transfer also has a band at width 3/4 which the field insertions simply do not see. No zeta zeros and no projector were supplied.
- Lead: treat this as the first controlled test case for a prime-defined analogue. Consequence: an existence proof that "one vertical line of observable decay modes" can emerge from letters alone.
- Related: L10-002, L10-010, L10-011, L10-064, L10-088.

### L10-010 Physical observable closure: R and R* lie in the linear Majorana space, preserved by the signed transfer
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:49; riemann-vs-selberg-cmps.md:24-41
- Raised by: cmps_decay_comparison lane (new exact deduction)
- Status at last mention: proved for the whole quadratic family
- Content: with `w1 = X⊗X`, `w2 = X⊗Y`, `w3 = Y⊗I`, `w4 = X⊗Z` (`{wi,wj} = 2 delta_ij`, all anticommuting with `P = Z⊗I`, `R = (w1 + i w2)/2`), the signed Heisenberg transfer `L_eta*(O) = Q*O + OQ - R*OR` preserves `span(w1..w4)`, with an explicit 4x4 drift matrix M. The four-mode cancellation is *structure*, not an eigenvalue projector, because the Hamiltonians in this family are quadratic in the Majoranas.
- Lead: for arithmetic letters, check closure of a finite generating family of odd observables under the correctly signed transfer first, before any spectral numerics.
- Related: L10-009, L10-099.

### L10-011 Three distinct requirements: observable closure, reflection symmetry, independent coercivity
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:51-63; riemann-vs-selberg-cmps.md:62-92
- Raised by: orchestrator (Claude) synthesizing the two cMPS lanes
- Status at last mention: established as a recipe; each requirement shown independent by a counterexample
- Content: on the observable space, with `N = M + I/4`, a letter-derived involution J gives `JNJ = -N` (reflection). Then for `a > 1/4`, `N^2` reduces in a positive metric to minus `S = [[(a-c)^2+d^2-1/16, -2d sqrt(a^2-1/16)],[-2d sqrt(a^2-1/16), (a+c)^2+d^2-1/16]]`, and the independent inequality `S >= 0` forces the common width. This is "a literal finite physical analogue of Selberg's quadratic relation followed by its Laplace spectral bound". None of the three may be inferred from the other two.
- Lead: for arithmetic letters, supply J from arithmetic symmetries (not eigenvalue matching), then look for a sum-of-squares or boundary-flux proof of the analogue of `S >= 0`.
- Related: L10-093, L10-094, L10-095, L10-099.

### L10-012 Two perturbations that break the toy: b = 0.01 splits the widths; 0.01 P breaks the closure
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:58-62; riemann-vs-selberg-cmps.md:49-56,96-102,114
- Raised by: cmps_decay_comparison lane (exact perturbation runs)
- Status at last mention: proved, negative (delimiting results)
- Content: setting `b = 0.01` keeps CAR, CP, faithful stationarity and four-mode selection but splits widths to ~0.24622128 / ~0.25377872; the exact centered linear coefficient `-2bd y` makes this exact, not numerical. Adding `0.01 P` to H keeps grading and the stationary state but is a *quartic* fermion interaction: it destroys linear observable closure and makes all eight odd poles visible (output denominator degree exactly eight, coprime numerator).
- Lead: "the smallest immediate arithmetic experiment" is to look for the analogue of the `P/100` term in any candidate prime letters — an uncontrolled component outside the generating family kills observable selection.
- Related: L10-010, L10-090, L10-091.

### L10-013 Uetake (2007) already supplies a factored modular Lax–Phillips generator with the zeros as eigenvalues
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:67; riemann-vs-selberg-operators.md:26,72,178
- Raised by: riemann_selberg_modes lane (live literature search), archived by the parent
- Status at last mention: verified primary source; narrows an old repo gap, proves nothing new
- Content: Uetake, *The Lax–Phillips infinitesimal generator and the scattering matrix for automorphic functions*, Ann. Polon. Math. 92 (2007) 99–122, DOI 10.4064/ap92-2-1, cached at `refs/src/uetake-2007/paper.pdf`. Causal scalar factor `F(p) = xi(2p)/xi(-2p)`. Theorem 4.2 (p.112): meromorphic resolvent, pole order agreement, dense span of generalized eigenvectors. Theorem 4.4 (p.114): eigenvalues of `-2A_c` are the nontrivial zeros with algebraic multiplicity, and imaginary spectrum of `2A_c + 1/2` is exactly RH. Theorem 5.1 (p.118): explicit automorphic boundary profiles.
- Lead: use Uetake's model as the wave-side endpoint of the missing intertwiner, and his Section 5 Poincaré-series profiles as *non-zero-defined* test data. No TeX source was located, only the publisher PDF.
- Related: L10-014, L10-016, L10-080, L10-087.

### L10-014 The "half shift" is a change of generator, not of clock: u_tt = (1/4 - Delta)u
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:69; riemann-vs-selberg-operators.md:84-90,144
- Raised by: riemann_selberg_modes lane
- Status at last mention: established, and it corrects an earlier loose phrase ("different clocks")
- Content: for Laplace parameter `s(1-s)`, the wave exponents are `q = ±(s-1/2)`, so the decaying outgoing branch is `q = s-1/2` while geodesic first-band bookkeeping is `lambda = s-1`; hence `q = lambda + 1/2`. With `r = log y`, `u_0 = y^(1/2) v(r,t)`, the cusp zero-mode wave equation becomes `v_tt = v_rr` — free escape modes down the cusp. The `1/4` in `Delta - 1/4` is the geometric threshold/half-density correction, *not* the arithmetic width; that every arithmetic pole has `Re q = -1/4` is extra information.
- Lead: keep the two appearances of 1/4 separate in all future writing.
- Related: L10-003, L10-015, L10-085.

### L10-015 Candidate intertwiner T u = (Pu, PCu) with WT = TC
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:71; riemann-vs-selberg-operators.md:92-96,150-156
- Raised by: riemann_selberg_modes lane
- Status at last mention: algebraic identity proved; domains/quotient/residues open — an explicit unfinished lead
- Content: if a first-band Poisson pushforward P satisfies `Delta P = -P(A^2+A)` with `A = -X`, set `C = A + 1/2` and `T u = (Pu, PCu)`. Block multiplication with `W = [[0, I],[1/4-Delta, 0]]` gives `WT = TC` directly. So the missing flow-to-wave bridge has a concrete map to test rather than only a matching spectrum. P lands in non-L2 Eisenstein data, so the identity is currently distributional/algebraic, not a bounded isometry.
- Lead: prove (a) the Bonthonneau–Weich pole exists with the claimed finite multiplicity; (b) P matches the Eisenstein Laurent chain injectively; (c) T satisfies the outgoing cusp asymptotics; (d) the LP regular-data projection maps the chain into the genuine half-line generator domain preserving chain length. Success would derive the shift at operator level and join two established resonance pictures without using RH.
- Related: L10-013, L10-031, L10-080.

### L10-016 Two repository corrections recorded but not yet applied to shards
- Source: notes/rh-strategy-2026-09-19/SYNTHESIS.md:73; cusp-bridge.md:64,76,110; riemann-vs-selberg-operators.md:20,74-78
- Raised by: cusp-bridge lane, confirmed independently by the riemann_selberg_modes lane
- Status at last mention: recorded, deliberately not edited into shards ("recorded here for a separate reviewed correction")
- Content: (1) `report/sections/04_riemann_channel.tex:71-75` and `notes/riemann-channel-note.md:59-64` write `Z(t)* k_lambda = exp(-it conj(lambda)) k_lambda` and call it decaying; substitution gives exponent `+beta t/2`, i.e. growth. The correct formula for the defined lower-half-plane compression is `Z(t) k_lambda = exp(it conj(lambda)) k_lambda`, generator eigenvalue `-conj(rho)/2`. (2) The entire-xi scattering symbol differs from the raw Eisenstein coefficient by the rational factor `(2i tau - 1)/(2i tau + 1)`: `S(tau) = [(2i tau-1)/(2i tau+1)] phi(1/2 + i tau)`.
- Lead: apply both under the repo's review discipline. Both matter when constructing an operator rather than matching a scalar pole set; Uetake's original LP scattering matrix has yet another elementary factor and one extra generator pole at `p = -1/2`.
- Related: L10-027, L10-081.

### L10-017 User steering: decay modes are central, cMPS is the physically natural setting, and "why Riemann differs from Selberg" deserves its own lanes
- Source: notes/rh-strategy-2026-09-19/SESSION.md:7
- Raised by: TJO
- Status at last mention: acted on — two extra lanes launched, then stopped at shutdown
- Content: recorded steering: "work must be written continuously. Decay modes are central; cMPS should be the physically natural setting. Two additional agents requested to understand precisely why Riemann differs from Selberg." This reoriented the positivity lane (positivity-products.md:96) and the graded-channels lane (graded-channels.md:69-71) mid-flight.
- Lead: the reorientation is itself the lead — "seek arithmetic output/exit energy identities for the amplitude decay modes, not merely an abstract positive kernel".
- Related: L10-006, L10-047, L10-061.

### L10-018 Off-site copy of the checkpoint archive (operational, not mathematical)
- Source: notes/rh-strategy-2026-09-19/RECOVERY.md:44-48
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not done
- Content: `scripts/research_checkpoint.py` writes checksummed snapshots to `.recovery/` including gitignored `refs/src/`, but "They are on the same disk as the repository, so they do not protect against disk loss. Copy a completed archive and its `.sha256` receipt to another disk for that protection."
- Lead: copy `.recovery/ARCHIVE.tar.gz` plus receipt to a second disk. No mathematical consequence.
- Related: -

### L10-019 H-CUSP-BRIDGE is where the repo stops, and why
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:7
- Raised by: repo (HANDOFF.md), restated by the cusp-bridge lane
- Status at last mention: open blocker
- Content: modular scattering zeros at `s = rho/2`, proposed flow resonance `lambda = rho/2 - 1`, and "the compact Haar-pairing proof is unavailable because the Eisenstein Laurent coefficients are outside L²".
- Lead: everything in the cusp lane is aimed at this. Consequence: it is the single named gap between the repo's Selberg machinery and a Riemann statement.
- Related: L10-003, L10-031, L10-080.

### L10-020 An existence claim for "some positive metric" is not evidence of a mechanism
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:9,42
- Raised by: cusp-bridge lane
- Status at last mention: methodological warning, established
- Content: the compact branchwise positive form yields unitary centered flow *iff* the extra Selberg 1/4 coercivity holds, and its full algebraic block fails at a Jordan threshold (`03e_selberg_letters.tex:144-178`). Separately, the Cauchy Gram is positive definite for arbitrary distinct parameters in the whole strip, so "it does not select RH".
- Lead: demand that any positivity claim be *sensitive* to the line — construct a positive form that fails for off-line parameters, or admit it is only normalization.
- Related: L10-005, L10-069.

### L10-021 The cusp prime-comb damping identity is only an identity of atomic measures
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:11
- Raised by: cusp-bridge lane, citing `report/sections/09c_selberg_tower_cusp.tex:122-138`
- Status at last mention: recorded caution
- Content: it "implies no operator identification or RH statement. Any proposed affine bridge must supply an intertwiner on regular/resonant data, not infer it from the prime weights."
- Lead: do not treat the prime-comb weights as evidence of an operator correspondence.
- Related: L10-019, L10-015.

### L10-022 The FE affine relabelling b = lambda' + 1/2, and the dangerous alternative same-label formula
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:24; SYNTHESIS.md:22
- Raised by: cusp-bridge lane (checked scalar deduction)
- Status at last mention: proved as scalar bookkeeping; explicitly *not* an operator theorem
- Content: with `s = rho/2`, `lambda = s-1`, `b = -conj(rho)/2`, one gets `b = -1 - conj(lambda)`; the FE partner `rho' = 1 - conj(rho)` has `lambda' = -1/2 - conj(rho)/2`, so `b = lambda' + 1/2`. As multisets with multiplicities the Riemann modal spectrum is the cusp-flow subset shifted by +1/2. "The alternative same-label formula uses an adjoint/conjugate and reverses the sign; conflating these two maps is dangerous."
- Lead: fix one convention repo-wide; it also explains why the correct centres are -3/4 and -1/4.
- Related: L10-003, L10-083.

### L10-023 The naive Hadamard finite-part cusp pairing is identically zero — one renormalization ruled out
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:26-30,56,121
- Raised by: cusp-bridge lane
- Status at last mention: proved, negative (for this specific pairing only)
- Content: all denominators `1 - s_i - conj(s_j)` have positive real part since `Re s < 1/2`, so subtracting the full constant-term divergence entrywise "leaves the **zero matrix**, rather than a positive resonance norm". "This is a concrete obstruction to the naive finite-part renormalized Haar pairing, not a no-go for all nonlocal or weighted pairings."
- Lead: different pairings, subleading Laurent data, or nonlocal boundary terms remain open.
- Related: L10-005, L10-029.

### L10-024 Even under RH, the normalized cusp Gram cannot make the centered flow unitary for N >= 2
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:44-52; riemann-vs-selberg-operators.md:66
- Raised by: cusp-bridge lane
- Status at last mention: proved, negative
- Content: `A*K + KA = -K - 11*`, so at the RH centre `(A + 3/4 I)*K + K(A + 3/4 I) = (1/2)K - 11*`, which cannot vanish because K has rank N while `11*` has rank one. Only for N=1 does it vanish, exactly at `Re(s_1) = 1/4`.
- Lead: this is the finite prototype of L10-007 — the *physical* norm is the wrong place to look for centered unitarity.
- Related: L10-007, L10-030.

### L10-025 Bonthonneau–Weich closes only the resolvent component of the bridge
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:58,62,98,106; riemann-vs-selberg-operators.md:16,177
- Raised by: cusp-bridge lane (web search, then parent archive)
- Status at last mention: verified primary theorem; explicitly insufficient
- Content: Bonthonneau–Weich, *Ruelle–Pollicott resonances for manifolds with hyperbolic cusps*, arXiv:1712.07832, DOI 10.4171/JEMS/1103, cached at `refs/src/1712.07832/preprint.tex`. Theorem 1 gives a globally meromorphic flow resolvent with finite-rank residues; Corollary 1 covers cofinite Fuchsian orbifolds with a footnote naming `PSL(2,Z)` and `Gamma(2)`. But "The source says the identification with discretized transfer spectra / first band remains future work" (`preprint.tex:172`).
- Lead: BW plus Uetake are the two endpoints; the identification between them is the work.
- Related: L10-013, L10-015, L10-031.

### L10-026 Finite Hardy Gram isometry: normalized truncated Laurent states map isometrically to Hardy kernels
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:68-74,122; riemann-vs-selberg-operators.md:60; graded-channels.md:154 (cross-check VALID)
- Raised by: cusp-bridge lane (checked deduction C), independently audited twice
- Status at last mention: proved unconditionally on leading states; limits explicit
- Content: with `C = diag(s_i - 1/2)`, `tau_i = i conj(C_i)`, the Hardy kernels `k_i(x) = 1/(x - conj(tau_i))` have Gram `i/(conj(tau_j) - tau_i) = -1/(conj(C_i)+C_j) = K_ij`. So there is "an explicit isometry of finite modal spans" intertwining the diagonal shifted action C with the model semigroup. It holds even for hypothetical off-line zeros.
- Lead: extend to generalized Laurent/Jordan data. Stated limitation: the first-band eigenvalue was *assigned*, no actual flow resonant state was constructed, and completeness in `K_S` is not addressed.
- Related: L10-005, L10-031.

### L10-027 The Hardy sign/adjoint proof
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:76; riemann-vs-selberg-operators.md:20
- Raised by: cusp-bridge lane; independently checked by the riemann_selberg_modes lane
- Status at last mention: proved; correction not yet applied to shards
- Content: in `H²(C_-)` multiplication by `exp(-itz)` is contractive for `t>=0`; reproducing kernels are eigenvectors of its adjoint with eigenvalue `exp(it conj(lambda))`. Old and corrected scalar moduli at `beta=1/2, t=1` are `exp(1/4)` and `exp(-1/4)` respectively.
- Lead: see L10-016.
- Related: L10-016.

### L10-028 Deduction D: an exact finite cMPS/Lindblad realization of the cusp Gram
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:84-90,123
- Raised by: cusp-bridge lane
- Status at last mention: proved as a finite construction; "an admissible finite physical model, not a proof mechanism yet"
- Content: `R = K^(1/2)`, `B = RCR^(-1)`, `j = 1* R^(-1)` give `B* + B = -j*j`, hence `B = -iH - (1/2)j*j`. On bond `C|vac> ⊕ C^N` with jump `L = |vac> j` and `Q = 0 ⊕ B`, the canonical relation `Q + Q* + L*L = 0` holds, and the vacuum-to-mode coherences carry exactly the decay eigenvalues `s_i - 1/2`.
- Lead: its limitations are the programme: takes a finite pole list as input, absorbing pure vacuum, no prime-defined letters, no mixed BC critical stationary state.
- Related: L10-005, L10-036, L10-100.

### L10-029 Next test 1: extend the cusp Gram/exit identity to generalized Laurent (Jordan) data
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:96
- Raised by: cusp-bridge lane (ranked first)
- Status at last mention: raised, not pursued (lane stopped)
- Content: start with a synthetic double scattering pole, take all bivariate Laurent coefficients of Maass–Selberg including logarithmic cusp terms, compute the resulting confluent Cauchy matrix and its dissipative generator, then compare with repeated-zero Hardy kernel derivatives. Success: an explicit positive Gram identity plus a matching Jordan chain preserving algebraic multiplicity. Failure: an unavoidable extra boundary term or chain-length mismatch, which "would isolate a real obstruction".
- Lead: "This is the quickest useful theorem, and it avoids silently assuming zero simplicity." Note recorded: a positive centered unitary form on the full Jordan chain would require semisimplicity and is *stronger than RH*.
- Related: L10-026, L10-048, L10-086.

### L10-030 Next test 2: construct the actual noncompact first-band pushforward on regular data
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:98
- Raised by: cusp-bridge lane
- Status at last mention: raised, not pursued
- Content: use BW's resolvent (`preprint.tex:143-164`), start with one scattering pole and match its distributional state to the Eisenstein Laurent coefficient through the Poisson transform. Success: finite-rank Riesz range, wavefront/cusp-growth conditions, a nonzero multiplicity-preserving pushforward at `lambda = s-1`, with the sign of X explicitly fixed. Failure: proof that the pole occurs only in a related determinant or a different flow sector — "It would then be inappropriate to import compact DFG positivity."
- Lead: this is the concrete version of closing H-CUSP-BRIDGE.
- Related: L10-015, L10-019, L10-025.

### L10-031 Next test 3: derive the cMPS exit map j and H from a cusp boundary / Schur-complement / Mayer-tail construction
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:100
- Raised by: cusp-bridge lane
- Status at last mention: raised, not pursued
- Content: seek analytic formulas for `j` and `H` from modular branches or prime input, then compare finite approximants against the Cauchy Gram realization. Explicit failure condition: "`j` or `H` is fitted from a supplied list of zero locations, or cutoffs change the divisor uncontrollably."
- Lead: the matrix construction of L10-028 is the debugging oracle; the Mayer-tail route is the only *letters-first* suggestion in this lane.
- Related: L10-028, L10-005.

### L10-032 Next test 4: SHW-style mixed rebound on the modal bond, preserving the coherence decay sector
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:102; graded-channels.md:130-134
- Raised by: cusp-bridge lane; echoed as priority 2 by the graded-channels lane
- Status at last mention: raised, not pursued; the finite criterion for it *was* proved (L10-101)
- Content: in the finite Gram realization, try a Siemon–Holevo–Werner rebound density on the modal bond and compute which coherence sectors survive. Success: a symmetry/invariant subspace preserving the original decay generator while yielding a nontrivial stationary density. Failure: rebounding alters every zero mode, or the stationary state stays absorbing and pure. Recorded caution: "No finite approximation can by itself furnish the infinite critical KMS state."
- Lead: mixing the rebound in is the only route from the pure absorbing vacuum to the BC-style mixed stationary bond.
- Related: L10-028, L10-101, L10-128.

### L10-033 Nonnormality is necessary, not a defect
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:92,124; riemann-vs-selberg-operators.md:66
- Raised by: cusp-bridge lane
- Status at last mention: proved as a finite lemma
- Content: see L10-007 for the statement. The extra remark here: "A separate arithmetic positive form could orthogonalize the modes; proving that form from non-spectral data remains the RH-sized step."
- Lead: name the arithmetic form. Related to the Krylov metric found in the toy (L10-065).
- Related: L10-007, L10-024, L10-065.

### L10-034 Numerical diagnostic scripts as sign/normalization debuggers, explicitly not evidence
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:78,109,126; positivity-products.md:81-92; graded-channels.md:49,163-165; riemann-vs-selberg-operators.md:118; riemann-vs-selberg-cmps.md:58,96
- Raised by: all lanes
- Status at last mention: done, reproducible offline
- Content: `cusp_bridge_diagnostic.py`, `positivity-products-check.py`, `graded_channels_checks.py`, `regular_cmps_decay_check.py`, `regular_cmps_decay_exact.py`, `riemann_selberg_toy_modes.py`, `riemann_vs_selberg_cmps_check.py`, `cmps_renewal_check.py`, each with saved JSON/TXT output. The three-mode on-line centered defect norm is about 2.2544 — "it is not zero under RH".
- Lead: reuse these as regression oracles for any arithmetic candidate. Every lane insists the algebra, not the floating point, carries the claims.
- Related: L10-005, L10-024.

### L10-035 Two small check-normalization bugs worth remembering
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:49,170-172
- Raised by: graded-channels lane
- Status at last mention: fixed
- Content: (a) a NumPy integer failed JSON serialization at export while all mathematical assertions passed; (b) SymPy's integer-polynomial gcd retains the common constant factor 5 in the denominator and its derivative, so the simple-pole assertion must check gcd *degree zero*, not literal 1. "this was a check-normalization issue, not a repeated pole."
- Lead: apply the same gcd-degree convention in any future coprimality assertion.
- Related: L10-034.

### L10-036 Claim-status ledger discipline: "positive centered metric from arithmetic input" is the one open RH-equivalent item
- Source: notes/rh-strategy-2026-09-19/cusp-bridge.md:112-127
- Raised by: cusp-bridge lane
- Status at last mention: the table's single Open row
- Content: of eleven ledger rows, ten are reviewed repo results, checked deductions or numerical checks. The only "Open / RH-equivalent after spectral identification, plus semisimplicity if full blocks included" row is "Positive centered metric from arithmetic input — The unresolved arithmetic mechanism".
- Lead: this is the honest statement of where the cusp route stands.
- Related: L10-006, L10-029.

### L10-037 Deligne tensor amplification needs an independently controlled pole set, and ordinary graph transfer powers fail
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:15, auditing `07_deligne_via_graphs.tex:132-160,195-208`
- Raised by: positivity_products lane
- Status at last mention: recorded obstruction
- Content: the tensor-power engine needs nonnegative local coefficients *and* control of the amplified global object's poles; for ordinary graph transfer powers "the interesting spectrum remains poles".
- Lead: any product must be shown to convert the target modes into something whose growth is independently bounded.
- Related: L10-038, L10-044, L10-053.

### L10-038 Slicing over a one-dimensional base costs only one factor sqrt(q), independent of tensor exponent
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:16, citing `07_deligne_via_graphs.tex:224-236`
- Raised by: positivity_products lane
- Status at last mention: recorded — this is *the* mechanism that kills the Deligne loss in the finite-field case
- Content: "What kills the Deligne loss is not tensor powers alone"; the fixed sqrt(q) loss under slicing is what makes amplification work there.
- Lead: find the analytic analogue — a product/slicing operation whose exponential growth loss is sublinear in tensor degree.
- Related: L10-044, L10-053.

### L10-039 Rosati positivity is not an independent RH proof for the constructed odd transfer
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:17, citing `notes/ring-norm-tensor/astra-proofs.md:1013-1037`
- Raised by: positivity_products lane
- Status at last mention: recorded, negative
- Content: the constructed odd transfer already inputs the Frobenius moduli that Rosati positivity proves; complete positivity of its MPS transfer therefore adds nothing. The genus-two audit separates a spectral realization from the arithmetic Hodge metric.
- Lead: do not re-derive positivity from data that already encodes the conclusion.
- Related: L10-053.

### L10-040 Suzuki's screw kernel: an arithmetic recurrence with a sign-controlled extension law would be new structure
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:18, citing `notes/resonances/astra-freeassoc.md:214-240,604-631` and `refs/src/2206.03682/screwz_15.tex`
- Raised by: repo, restated by the positivity_products lane
- Status at last mention: open target
- Content: finite-interval positivity is insufficient and is even unconditional on sufficiently small intervals; existing numerical Cholesky factors are a discovery aid only.
- Lead: find the recurrence. This becomes the Schur-pivot problem of L10-042/L10-052.
- Related: L10-042, L10-052.

### L10-041 A cheap two-point diagnostic for any claimed sum-of-squares factorization
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:36
- Raised by: positivity_products lane
- Status at last mention: raised, not used further
- Content: for the full even Psi with `Psi(0)=0`, the two-node matrix at `A, -A` has eigenvalues `Psi(2A)` and `4Psi(A) - Psi(2A)`. "This makes the cancellation mechanism visible before large Gram matrices are built."
- Lead: apply to any candidate factorization before scaling up. Small, cheap, never followed up.
- Related: L10-008.

### L10-042 The increment Toeplitz reformulation: sparse four-diagonal prime updates
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:58-77,140
- Raised by: positivity_products lane (elementary deduction)
- Status at last mention: proved; equivalent to full kernel positivity, hence RH-equivalent, but "not a proof"
- Content: differences `d_j = v_{j+1} - v_j` have Toeplitz Gram `c_h(m) = Psi((m+1)h) + Psi((m-1)h) - 2 Psi(mh)`, congruent to the screw Gram by an invertible matrix, so PSD conditions are exactly equivalent. Each prime power with `a/h = L + theta` contributes only at `m = ±L` (weight `-w h(1-theta)`) and `m = ±(L+1)` (weight `-w h theta`) — at most four diagonals, with trigonometric polynomial `-2 w h[(1-theta)cos(Lx) + theta cos((L+1)x)]`.
- Lead: "derive a sign-controlled innovation/Schur recurrence for the **sum** of archimedean and sparse prime Toeplitz pieces". Also reduces repeated Psi evaluations from quadratic to linear in grid size.
- Related: L10-008, L10-052.

### L10-043 Avoid rediscovering Suzuki's own scalar criterion
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:38, citing `screwz_15.tex:400-425`
- Raised by: positivity_products lane
- Status at last mention: warning
- Content: Suzuki already proves `Psi(t) >= 0` for every real t is equivalent to RH, and `Psi(t) = O(1)` iff RH. "Merely replacing matrix positivity with this scalar positivity is not new progress."
- Lead: none — a stop sign.
- Related: L10-040.

### L10-044 The fixed-loss amplification lemma: epsilon_k/k -> 0 would prove RH
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:42-52
- Raised by: positivity_products lane (elementary conditional reduction)
- Status at last mention: proved as a conditional reduction; the required product does not exist
- Content: if for each k an arithmetic product gives a scalar meromorphic response `R_k(z)` with (1) survival of `k lambda` as a genuine pole for every `lambda` in the centered retained divisor Sigma, (2) `R_k` the Laplace transform of `r_k` with `|r_k(t)| <= M_k (1+t)^{d_k} exp(epsilon_k t)` and `epsilon_k/k -> 0`, (3) the same meromorphic continuation — then `k Re lambda <= epsilon_k`, so `Re lambda <= 0`, and reflection gives `Re lambda = 0`. Crucially `M_k` may be exponential or worse in k; only the coefficient of t must be sublinear.
- Lead: "testing the exponential loss, not the state-space dimension or prefactor, is the right early feasibility test." A matrix coefficient may miss a mode and a signed trace may cancel it; either breaks (1).
- Related: L10-037, L10-038, L10-053.

### L10-045 Why ordinary tensoring does not help, stated as a rule
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:52
- Raised by: positivity_products lane
- Status at last mention: proved, negative
- Content: from `||T(t)|| <= M exp(ct)` one gets only `||T(t)^{⊗k}|| <= M^k exp(kct)`, i.e. `epsilon_k = kc`, so the amplification bound recovers `Re lambda <= c` with no improvement.
- Lead: none — a stop sign for naive tensor powers.
- Related: L10-044.

### L10-046 Numerical evidence and the warning against a mesh-independent lower bound
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:81-92
- Raised by: positivity_products lane
- Status at last mention: done; explicitly labelled a sanity check
- Content: at mesh `h=1/4`, A=2 gives min eigenvalue of K 0.0210158467482652494 and min increment Toeplitz eigenvalue 0.000747659951048785; A=4 gives 0.0146176837661784046 and 0.000375484666271565. Agreement to 32 digits at 40 and 70 decimal digits. "The small positive increment eigenvalue also warns against seeking a mesh/interval-independent lower bound."
- Lead: any proposed uniform bound must scale with the mesh.
- Related: L10-042, L10-052.

### L10-047 The stronger identity C*C = 2 kappa G is stronger than divisor RH — keep the modal version separate
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:118
- Raised by: positivity_products lane
- Status at last mention: recorded as a distinction
- Content: `C*C = 2 kappa G` on the whole retained state space yields `A*G + GA = -2 kappa G`, i.e. metric skew-adjointness after centering, which in finite dimension excludes Jordan blocks. "Because Weil positivity is blind to Jordan blocks, this full identity is stronger than divisor RH."
- Lead: aim at the modal statement `||Cv||^2 = 2 kappa <v,Gv>` only.
- Related: L10-006, L10-029, L10-109.

### L10-048 Generic exit positivity records a mode-dependent extra escape term and does not force equal widths
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:120-124
- Raised by: positivity_products lane, using the cusp lane's identity
- Status at last mention: established
- Content: with `A = diag(s_i - 1)` and `G_ij = 1/(1-conj(s_i)-s_j)`, `A*G+GA = -G - 11*`, so the modal width is `-Re(s_i - 1) = 1/2 + |1|^2/(2 G_ii)`: an extra escape term that exists throughout the strip.
- Lead: "isolate a prime-defined mechanism that fixes the exit-to-storage ratio, or compensates that extra escape via correlated return amplitudes, rather than re-prove positivity of this Gram."
- Related: L10-005, L10-006.

### L10-049 The exact bridge specification <V(t),V(u)>_G = Psi(t) + Psi(u) - Psi(t-u)
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:128-138; SYNTHESIS.md:79
- Raised by: positivity_products lane
- Status at last mention: raised as a specification; not established
- Content: with the Riemann no-event normalization `A` (modes `-conj(rho)/2`) and `B = 2A + 1/2` (centered modes `1/2 - conj(rho)`), define `V(t) = ∫_0^t exp(rB) b dr` for an arithmetic boundary distribution b. Establishing the displayed identity from physical letters and prime/archimedean data — including the mixed t,u correlations — would make the right side a Gram kernel, so Suzuki would give RH. "agreement only at `t=u` or only at finitely many times is insufficient."
- Lead: "Its advantage is that it says which cMPS observable to calculate." Under RH the mode components are `(exp(i gamma t)-1)/(i gamma)` matching Suzuki's Eq_109, "but those components must not be used as the construction". `b` may be a distribution; it is `V(t)` that must have finite norm.
- Related: L10-001, L10-051, L10-052.

### L10-050 Schur complements of the time-bin Gram are the physical energy of the next output amplitude
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:140
- Raised by: positivity_products lane
- Status at last mention: raised as an interpretation, not followed up
- Content: the Toeplitz entries of L10-042 are the Gram entries of finite time-bin amplitudes `V((j+1)h) - V(jh)`; "Their Schur complements are the energy of the next output amplitude after projecting onto previously observed amplitudes." Prime-power contributions are not independent PSD channels, so interference among physical histories and the archimedean sector is essential.
- Lead: a physical reading of the sought arithmetic recurrence — it names what a positivity proof would *mean*.
- Related: L10-008, L10-042, L10-052.

### L10-051 The prime kink no-go: no bounded-generator finite-energy cMPS can equal the exact Suzuki covariance
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:144-152
- Raised by: positivity_products lane (elementary deduction)
- Status at last mention: proved, negative — and packaged as a cheap stopping test
- Content: `Psi'(a+) - Psi'(a-) = -log(p)/sqrt(p^k)` at each prime-power time `a = log(p^k)`, so `K(t,t) = 2Psi(t)` has genuine first-derivative kinks. But for bounded B and a Hilbert vector b, `V(t) = ∫_0^t exp(rB)b dr` is entire, hence real-analytic on the diagonal. So every fixed finite-dimensional, time-homogeneous cMPS amplitude model of this form is excluded.
- Lead: "calculate the jump at `log 2`. If the proposed exact prime-history model is analytic there, its bridge identity is impossible." An exact candidate needs an unbounded generator/distributional boundary, explicit delay propagation at prime lengths, or another singularity mechanism.
- Related: L10-049, L10-129.

### L10-052 Ranked next tests of the positivity lane (three, with explicit stop conditions)
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:156-160
- Raised by: positivity_products lane
- Status at last mention: raised, not pursued (lane completed as an audit)
- Content: (1) arithmetic cMPS time-bin covariance and exit ratio around the `log 2` and `log 3` ridges, with correct normalization `B = 2A + 1/2`; stop if analytic at log 2, or if it assigns an independent positive block per prime, or if it produces the density-operator pair-difference spectrum instead of the amplitude modes. (2) nonlinear innovations for the prime-defined Toeplitz matrices — an arithmetic formula for each Schur pivot `d - k*K^{-1}k`; "a putative negative vector must be interval-certified and converted to a smooth test before interpreting it as mathematical failure". (3) product loss and spectral survival audit for k=1,2,3, with surviving scaled poles, even/odd cancellation and growth exponents; stop if all bounds are `epsilon_k = k epsilon_1`, or if the pole is erased by a supertrace.
- Lead: "Only pursue uniform width after the actual arithmetic bridge is verified."
- Related: L10-042, L10-044, L10-049, L10-051.

### L10-053 The genus-two Jacobian/curve projector warning: a tensor product can silently count a different object
- Source: notes/rh-strategy-2026-09-19/positivity-products.md:160, citing `06f_ring_norm_genus_two.tex:213-221`
- Raised by: positivity_products lane
- Status at last mention: recorded as concrete evidence that this failure is easy
- Content: a tensor product may count a different object without an arithmetic projection, and a supertrace may erase the pole one wants.
- Lead: any amplification proposal must exhibit the projector.
- Related: L10-037, L10-044.

### L10-054 Finite Hashimoto companion metric positivity is equivalent to an *extra* strict band, with Jordan blocks at the endpoint
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:20, citing `03f_selberg_letters_finite.tex:54-89,132-144`
- Raised by: repo, restated by the graded-channels lane
- Status at last mention: reviewed repo result
- Content: `G = [[I, Sigma/2],[Sigma/2, qI]]` with `C*GC = qG`; positivity is equivalent to `|Sigma| < 2 sqrt(q)`, and endpoint roots have Jordan blocks. "Thus constructing an invariant Hermitian form is not yet the RH step."
- Lead: the "extra band" is always where the content is; the metric is bookkeeping.
- Related: L10-020, L10-095.

### L10-055 No universal odd-sector Alon–Boppana floor exists
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:21, citing `03c_graded_ramanujan.tex:132-144`
- Raised by: repo (prior prover's counterexample), restated
- Status at last mention: pursued, negative
- Content: `E = (Ad I + Ad P)/2` kills the odd block, and primitive bounded-degree examples also exist. "Therefore 'RH because odd relaxation is an extremal expander rate' is unsupported without a separate arithmetic normalization/duality condition."
- Lead: any expander-style argument needs an arithmetic normalization or duality first.
- Related: L10-115, L10-127.

### L10-056 The parity jump sqrt(gamma) P shifts all odd rates by -2 gamma and leaves the even block alone
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:22, citing `03b_graded_permutation.tex:218-240`; graded-channels.md:59
- Raised by: repo, restated by the graded-channels lane
- Status at last mention: established, and shown to be a trap
- Content: `gamma(Ad P - I)` preserves an already-uniform odd spectrum but does not force the rest of the dissipator to be scalar. In the tight-frame language, `R = sqrt(gamma)P` supplies `4 gamma I_O`, so with desired `c = 1/4` it exhausts the budget at `gamma = 1/8`.
- Lead: other noises may share the rate budget instead — this is the escape route from the all-parity-damping ansatz.
- Related: L10-058, L10-059, L10-060.

### L10-057 The doubled-bond cMPS supertrace is the parity-twisted closure norm, hence nonnegative
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:23, citing `04e_cmps_parity_overlap.tex:12-34`; riemann-vs-selberg-cmps.md:132
- Raised by: repo (marked sketched/unreviewed), restated
- Status at last mention: recorded caution
- Content: "the formal graded spectral transfer and its trace distribution need not have a Kraus realization". Separately: "The Selberg flat supertrace is a signed orbit distribution of a single-copy geometric complex. The full doubled-bond Lindbladian supertrace is a different object."
- Lead: never conflate the flat supertrace with the ring norm; neither the toy's physical correlation nor its ring norm has been identified with the explicit formula.
- Related: L10-120, L10-098.

### L10-058 The letter-level Dirichlet-form defect proposal
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:25
- Raised by: graded-channels lane
- Status at last mention: proposed, then sharpened into L10-059 and L10-060
- Content: "formulate a letter-level *Dirichlet-form defect* for uniform odd dissipation. Test whether arithmetic symmetry constraints kill that defect, rather than assuming a positive metric from preassigned zeta zeros."
- Lead: the whole point is to avoid assuming a positive metric built from the answer.
- Related: L10-059, L10-060.

### L10-059 The Hilbert–Schmidt obstruction: a parity jump plus any dissipative prime noise cannot both act on the full odd block
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:29-41
- Raised by: graded-channels lane (checked deduction)
- Status at last mention: proved, negative — with four explicit escape hatches
- Content: for `L(X) = -i[H0,X] + gamma(PXP - X) + D(X)` bistochastic and preserving the whole odd space O, if `L|_O + 2 gamma I` is HS-skew-adjoint then all `R_a` are scalar and `D = 0`. The proof uses `-Re Tr(X* D(X)) = (1/2) sum_a ||[R_a*, X]||_HS^2` and the fact that the commutant of all off-diagonal block matrices is `C I`. No zeta data enter.
- Lead: the four escapes are the leads — (i) a nontracial invariant state and a different metric, (ii) a proper odd *resonance subspace* rather than the whole coherence space, (iii) an invariant positive form not equal to the HS form, (iv) sharing the target decay rate between parity dephasing and other noises. Recorded: "Equal real parts of eigenvalues alone do not imply HS skew-adjointness."
- Related: L10-002, L10-056, L10-060, L10-069.

### L10-060 Uniform decay as a tight-frame identity for commutators: C_O* C_O = 2c I_O
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:51-59
- Raised by: graded-channels lane (checked deduction)
- Status at last mention: proved; proposed as the useful letter problem
- Content: define `C_O X = ([R_1*,X],...,[R_m*,X])` on the odd subspace. The Hermitian part of the restricted generator is `-(1/2)C_O*C_O`, so `L|_O + cI` is HS-skew-adjoint iff `C_O*C_O = 2c I_O`. "Thus the useful letter problem is a **tight-frame identity for commutators**, not merely parity covariance. It makes uniform decay a quadratic identity among arithmetic letters which can be checked without knowing eigenvalues."
- Lead: for a tracial model with a fixed metric this is *linear* in the Kossakowski matrix, so Choi positivity makes it a semidefinite feasibility problem (graded-channels.md:138).
- Related: L10-059, L10-069.

### L10-061 The C^(1|1) finite witness with supertrace |1 - e^{(-1/4 + i omega)t}|^2
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:61-67
- Raised by: graded-channels lane
- Status at last mention: proved as a witness; materially limited
- Content: `P = Z`, `H0 = (omega/2)Z`, jumps `sqrt(1/8)X` and `sqrt(1/8)Y`. Even spectrum `{0, -1/2}`, odd block `-1/4 I` plus rotation `±i omega`, unique stationary density `I/2`. Supertrace `1 + e^{-t/2} - 2e^{-t/4} cos(omega t) = |1 - e^{(-1/4+i omega)t}|^2`: "the correct two reference rates, mixed stationary state, and additive functional equation at the finite rational-zeta level, from balanced population-exchange letters". The check script uses `omega = sqrt(2)`, never a zeta ordinate.
- Lead: it demonstrates an escape from the all-parity damping ansatz. Limitation: `R_X^2 != 0`, so it violates cMPS kinetic regularity; unitary remixing to raising/lowering makes squares zero but the mutual anticommutator nonzero. So it is graded GKLS data, not a finite-kinetic-energy fermionic cMPS.
- Related: L10-056, L10-062, L10-063.

### L10-062 Kinetic regularity is an independent condition
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:67, citing `06h_zeta_conditions.tex:57-62,157-172`; riemann-vs-selberg-cmps.md:102, citing `refs/src/1211.3935/calculus.tex:309-313`
- Raised by: repo, restated in two lanes
- Status at last mention: established constraint
- Content: finite kinetic energy for a fermionic cMPS requires `R^2 = 0` (and, with several jumps, more). The repo already warns it is independent of the other zeta conditions.
- Lead: screen every candidate letter set against `R^2 = 0` before spectral work.
- Related: L10-061, L10-063, L10-100.

### L10-063 The arbitrary frequency sqrt(2) shows why the trace-identification problem is indispensable
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:67
- Raised by: graded-channels lane
- Status at last mention: recorded caution
- Content: the C^(1|1) witness has a *free* oscillation frequency; nothing in the construction picks out arithmetic values. "No RH inference follows from this toy, and its arbitrary frequency shows why the trace-identification problem remains indispensable."
- Lead: a mechanism producing one vertical line is cheap; producing the *right* ordinates is the hard part.
- Related: L10-061, L10-099.

### L10-064 The regular 2|2 cMPS: the jump returns to active internal states, not an absorbing vacuum
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:73-82
- Raised by: graded-channels lane, in direct response to user steering
- Status at last mention: built and checked; the base case for everything downstream
- Content: "The emitted fermion resets the internal two-level system while flipping bond parity. The even Hamiltonian repopulates the emitting level inside each parity sector." Stationary density unique and faithful with Schmidt weights ~0.0145898, 0.0381966, 0.2618034, 0.6854102 and entropy 0.796154 nats. Parity covariant, trace preserving, mixing, ring supertraces nonnegative at six lengths. Odd modes split into two bands at -1/4 and -3/4, both oscillating at `(sqrt7 ± 2)/4`.
- Lead: the slow band is "a tangible candidate for the **proper physical decay subspace**"; the fast band "must be classified/cancelled by an actual trace identity, never simply discarded to fit RH."
- Related: L10-002, L10-009, L10-065.

### L10-065 The letter-generated Krylov basis carries an explicit rational positive invariant metric
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:110-118
- Raised by: graded-channels lane (exact input/output strengthening)
- Status at last mention: proved exactly
- Content: the source Krylov space `span{L_eta^k(R sigma)}` and the sink-observable space each have dimension four. With `A = L_eta|_odd`, `K = A + I/4`, `v = R sigma`, the companion `K_comp = [[0,0,0,-9/256],[1,0,0,0],[0,1,0,-11/8],[0,0,1,0]]` admits `G = [[10496/27,0,-32/3,0],[0,32/3,0,-1],[-32/3,0,1,0],[0,-1,0,1]]`, positive definite, with `K_comp*G + G K_comp = 0`, checked by principal minors. "This metric is constructed on a space generated by physical letters and field insertion; no eigenvectors or zeta frequencies are assigned."
- Lead: this is the concrete instance of the "second arithmetic positive form" that L10-007/L10-033 ask for. It is *not* the physical HS norm, in accord with the cusp lane's warning.
- Related: L10-007, L10-033, L10-069.

### L10-066 Priority 1: deform the *letters*, not the eigenvalues, and allow arithmetic finite-level character actions
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:122-128
- Raised by: graded-channels lane (highest priority)
- Status at last mention: raised, not pursued
- Content: from the `2|2` toy take `R = X ⊗ lowering`, `H = diag(H_+, H_-)`, then "permit arithmetic finite-level character actions on the internal index". Impose parity, `R^2 = 0`, canonical gauge and a faithful stationary bond *before* seeking uniform widths. Form the insertion-generated Krylov space and its observable quotient with the parity-twisted transfer, and derive its polynomial/intertwining relations directly from the letters.
- Lead: "The immediate experiment is parameter classification of this `2|2` family and exact residues, not an expensive search over guessed zeta ordinates."
- Related: L10-002, L10-009, L10-064, L10-069.

### L10-067 Failure criteria for the observable-subspace route, stated in advance
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:128,134,140,146
- Raised by: graded-channels lane
- Status at last mention: recorded
- Content: failure if "the four-mode cancellation is destroyed by every meaningful arithmetic extension, positivity uses fitted eigenvalues, or a trace/divisor assertion silently suppresses poles visible to required insertions"; if "physical source/sink poles move, the proposed cMPS violates kinetic regularity, or the bond remains absorbing"; if "the existing covariant perturbations retain free nonuniform decay parameters"; if "metrics degenerate, modes escape, reference/trivial factors are inconsistent, or divergent prime rates are assumed to produce a normal semigroup".
- Lead: use these as pre-registered stop conditions.
- Related: L10-066, L10-068, L10-069, L10-070.

### L10-068 The minimal missing identity: A_obs* G + G A_obs = -(1/2) G on the observable realization
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:126
- Raised by: graded-channels lane
- Status at last mention: stated as the missing lemma
- Content: "for independently specified local/arithmetic letters, there must be a positive form `G` on the *observable* odd realization with `A_obs*G + G A_obs = -(1/2)G`, and an input/output divisor identity tying precisely these poles (including their algebraic multiplicities) to the Riemann zeros under `b = -conj(rho)/2`. The toy supplies the former in finite dimension but supplies no arithmetic divisor identity. Prime-dependent coefficients may not be fitted to known zero positions."
- Lead: this is the cleanest single statement of what would have to be proved.
- Related: L10-002, L10-065, L10-006.

### L10-069 Priority 3: an SDP feasibility test of the commutator-frame defect inside the existing finite BC covariance cone
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:136-140,43
- Raised by: graded-channels lane
- Status at last mention: raised, not pursued
- Content: for primes p = 3,5,7, impose the linear stationary/covariance constraints and examine the Hermitian part on a candidate observable coherence space. For a tracial model with a fixed metric, `C_O*C_O = 2cI` is linear in the Kossakowski matrix, so Choi positivity makes it a concrete semidefinite feasibility problem. Screening input: the BC cone already contains generators with full Weil/Galois/parity covariance, a unique tracial stationary density and *unequal* odd rates (`04d:161-182`), while imposing all Weyl covariance collapses to pure depolarization and kills oscillations (`04d:143-157`).
- Lead: "Full covariance plus stationarity alone has already failed, so merely rerunning that ansatz is not useful" — the new content would have to be the *observable subspace* restriction. For nontracial or nonnormal models use the appropriate weighted form and do not import the HS no-go.
- Related: L10-059, L10-060, L10-134.

### L10-070 Priority 4: a regulator theorem separating bond dimension, prime cutoff, continuum spacing and temperature limits
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:142-146
- Raised by: graded-channels lane
- Status at last mention: raised, not pursued
- Content: each approximant must specify its regular source/sink spaces and physical observable transfer; then check local uniform convergence of the correlation resolvent on contours isolating poles, convergence of residues and their ranks, controlled noncancellation, and separately persistence of the positive metric. "A finite correlation's scalar pole order alone does not certify geometric/algebraic modal multiplicities" (`03d_graded_ramanujan_continuum.tex:78-97`).
- Lead: this is the step between any finite success and an actual theorem.
- Related: L10-071, L10-098.

### L10-071 The companion counterexample C_n showing finite positivity need not survive regulator removal
- Source: notes/rh-strategy-2026-09-19/graded-channels.md:146
- Raised by: graded-channels lane
- Status at last mention: proved, negative
- Content: `C_n = [[2 - 1/n, 1],[-1, 0]]` has positive invariant `G_n = [[1, 1-1/(2n)],[1-1/(2n), 1]]`, but `lambda_min(G_n) = 1/(2n) -> 0`; the limiting companion has a nonzero Jordan nilpotent and admits no positive invariant metric. A second warning alongside the repo's `1/p` prime-jump cutoff mass loss (`04g_phase_side_lindbladian.tex:121-135`).
- Lead: any limit argument must control the *conditioning* of the metric, not just its existence at each n.
- Related: L10-070, L10-120.

### L10-072 BW's time-reversal convention must be declared before importing its s into the repo's lambda
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:16
- Raised by: riemann_selberg_modes lane
- Status at last mention: recorded caution
- Content: the repo flow convention is `A = -X`, `(X + lambda)u = 0`, `exp(tA)u = exp(t lambda)u`, with `Delta f = -lambda(1+lambda)f`, `lambda = s-1`. BW instead name the generator X with resolvent `(X-s)^{-1}`.
- Lead: state the time direction explicitly in any BW-based argument.
- Related: L10-025, L10-015.

### L10-073 Ruling out Selberg complementary modes still needs mu >= 1/4, and mu = 1/4 can carry a Jordan block
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:17,135
- Raised by: riemann_selberg_modes lane
- Status at last mention: established
- Content: compact first-band modes satisfy `lambda = -1/2 ± sqrt(1/4 - mu)`; self-adjointness gives the vertical -1/2 line OR the real interval [-1,0]. At `mu = 1/4` the doubled quadratic root can carry a Jordan block: "the divisor lies on the line but centered unitarity on the full block fails."
- Lead: this is the exact template the toy in L10-011 reproduces in finite dimension.
- Related: L10-011, L10-029, L10-083.

### L10-074 A live search did not find a cusp first-band/Eisenstein theorem — a search limitation, not a no-go
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:28
- Raised by: riemann_selberg_modes lane
- Status at last mention: recorded
- Content: compact and convex-cocompact quantum-classical correspondence papers were recovered, "whose hypotheses do not automatically include a cusp. It did not establish a later cusp first-band/Eisenstein theorem. This is a search limitation, not a claim no such theorem exists."
- Lead: a targeted literature search for a cusp first-band theorem is still worth doing.
- Related: L10-025, L10-030.

### L10-075 The cusp boundary flux exactly balances the nonreal spectral parameter
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:34-42
- Raised by: riemann_selberg_modes lane (derived)
- Status at last mention: proved
- Content: on the truncated fundamental domain, `mu ||f||^2 = ∫(|f_x|^2+|f_y|^2) dx dy - ∫_0^1 conj(f(x,Y)) f_y(x,Y) dx`. For the leading Eisenstein Laurent mode the boundary term is `|c|^2 (1-s) Y^{1-2sigma}`, whose imaginary part gives `Im(mu)||f||^2 = eta |c|^2 Y^{1-2sigma} + o(1)`, consistent with `Im(mu) = eta(1-2sigma)`. "Dropping this term would manufacture a false reality proof."
- Lead: any energy argument in this sector must carry the boundary term explicitly. A self-adjoint domain requires the boundary pairing to vanish in the limit; these outgoing modes do not satisfy that.
- Related: L10-004, L10-087.

### L10-076 K as the Gram of exponentials, the isometry into L2(0,inf), and the causal flux law
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:46-58
- Raised by: riemann_selberg_modes lane (independent audit)
- Status at last mention: proved
- Content: `K_ij = ∫_0^inf exp(conj(C_i)t) exp(C_j t) dt` is the Gram of the explicit output functions `g_i(t) = exp(C_i t)`. The map `v -> sum_i v_i exp(C_i t)` is an isometry from `(C^N, K)` into L2(0,inf); the modal semigroup becomes left translation and obeys `d/dt ||exp(tC)v||_K^2 = -|sum_i exp(tC_i)v_i|^2`. "stored energy equals future emitted energy, and decay is energy leaving through one channel. It is not dependent on RH."
- Lead: the causal output interpretation is the physically natural picture of the cusp Gram.
- Related: L10-005, L10-026.

### L10-077 The Riemann FE symmetry C' = -1/2 - conj(C) allows two different widths summing to 1/2
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:64; riemann-vs-selberg-cmps.md:69
- Raised by: riemann_selberg_modes lane
- Status at last mention: established
- Content: the Riemann FE gives scattering-pole partner `s' = 1/2 - conj(s)`, i.e. symmetry about `Re(C) = -1/4`, but the geometric scattering identity `phi(s)phi(1-s) = 1` exchanges poles and zeros and does *not* impose that same-pole-set symmetry. Reflection symmetry alone permits eigenvalues off the imaginary axis, "exactly as a functional equation permits off-line zeros."
- Lead: never treat FE as producing equal widths; it needs the coercivity partner.
- Related: L10-011, L10-084, L10-094.

### L10-078 Read Uetake's "basis" conservatively as the completeness actually proved
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:72
- Raised by: riemann_selberg_modes lane
- Status at last mention: recorded caution
- Content: "Read 'basis' in 4.4 conservatively as the completeness statement actually proved in 4.2; no Riesz-basis bounds are provided by these lines."
- Lead: do not import Riesz-basis bounds — this matters directly for the non-Riesz argument of L10-113/L10-121.
- Related: L10-013, L10-113, L10-121.

### L10-079 Raw Eisenstein, original LP, and factored Hardy scattering symbols differ by explicit elementary factors
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:74-78
- Raised by: riemann_selberg_modes lane
- Status at last mention: established
- Content: `S(tau) = [(2i tau - 1)/(2i tau + 1)] phi(1/2 + i tau)`. Uetake's original LP scattering matrix on p.110 is `-[(p-1/2)/(p+1/2)] F(p)` with one extra generator pole at `p = -1/2`, removed by his construction; his alternative convention on p.116 is `F(p)(1/2+p)/(1/2-p)`. "They agree on the nontrivial arithmetic modal set after the stated transformations; they are not interchangeable as whole symbols."
- Lead: fix which symbol any construction uses before comparing residues.
- Related: L10-016.

### L10-080 Domain caution: do not import dom(A_c) = dom(L) ∩ K
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:80
- Raised by: riemann_selberg_modes lane
- Status at last mention: recorded as "a concrete warning against an invalid domain inference"
- Content: "the generator of a compressed half-line translation ordinarily allows nonzero boundary traces, whose zero extension is not in the whole-line derivative domain." The model semigroup and spectral statements can still be used with the correct half-line generator domain; "deriving an unbounded Lindblad/no-event letter requires spelling out the boundary/exit domain separately."
- Lead: exactly the point where Siemon–Holevo–Werner's exit-space formalism (L10-128) would be needed.
- Related: L10-013, L10-128, L10-129.

### L10-081 The two-state passive toy: a direct counterexample to deriving RH from CP + passivity + one channel + FE
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:102-114
- Raised by: riemann_selberg_modes lane
- Status at last mention: proved, negative — and identified as a constructive hint
- Content: `j = (sqrt(2g), 0)`, `H = [[0,w],[w,0]] - Omega I`, `B = -iH - (1/2)j*j`, eigenvalues `b_± = -g/2 + i Omega ± sqrt(g^2/4 - w^2)`. At `g = 1/2` the centre is exactly -1/4 with FE symmetry `b -> -1/2 - conj(b)`, and there is a CPTP vacuum cMPS completion for every real w. But `w > 1/4` gives both widths 1/4 (underdamped); `0 < w < 1/4` gives two distinct widths summing to 1/2, both inside the strip; `w = 1/4` gives equal widths with a nonzero nilpotent (Jordan threshold, `t exp((-1/4 + i Omega)t)` matrix elements). At `w = 1/8` the widths are exactly `1/4 ± sqrt(3)/8`.
- Lead: "a letter-defined coercive coupling theorem could force an underdamped regime, just as a spectral-gap inequality selects the Selberg branch. The scalar toy inequality `w > g/2` is not currently available for the modular boundary operator."
- Related: L10-011, L10-082, L10-087, L10-092.

### L10-082 The toy is PT-symmetric after centering — but PT alone permits both regimes
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:116
- Raised by: riemann_selberg_modes lane
- Status at last mention: raised once, not pursued
- Content: "The toy can be written as an effective PT-symmetric Hamiltonian after centering. That symmetry alone permits both regimes; proving its unbroken regime is the difficult bound. No physical PT principle is asserted for the arithmetic system."
- Lead: RH would be "PT unbroken" for the arithmetic operator — a reformulation, not a proof. Worth noting because the PT literature has techniques for proving unbroken regimes.
- Related: L10-081, L10-011.

### L10-083 Which experiment sees which rate: four distinct observables, four distinct widths
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:120-125
- Raised by: riemann_selberg_modes lane
- Status at last mention: established as bookkeeping
- Content: (1) geodesic correlation — poles of the Laplace transform of `<f ∘ flow_t, g>`; the Riemann subset would have `lambda = rho/2 - 1`, width 3/4 under RH, only after the missing identification; a coefficient can vanish for a particular test pair. (2) automorphic wave escape — `q = s - 1/2`, width 1/4, realized by Uetake's factored LP semigroup. (3) bond/cMPS coherence — amplitude rates are the b's; *population* survival of a single eigenmode has rate `2 Re(b)`, width 1/2 under RH, "coherence/population sectors must not be conflated". (4) stationary emitted field — the vacuum-exit realization has a pure absorbing vacuum with no ongoing output; a mixed critical BC stationary state or a nontrivial stationary ring construction is an additional requirement.
- Lead: state which observable is meant before quoting any width. Four different numbers (3/4, 1/4, 1/2, none) for the same zeros.
- Related: L10-003, L10-014, L10-028.

### L10-084 Two different 1/4's, and two different positive forms
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:144,146
- Raised by: riemann_selberg_modes lane
- Status at last mention: established distinctions
- Content: the `1/4` in `Delta - 1/4` is the geometric threshold/half-density correction; that every arithmetic scattering pole has `Re q = -1/4` is extra arithmetic information. Separately: the physical output/Hardy metric obeys a rank-one loss law with nonorthogonal modes, while a manufactured diagonal modal metric can unitarize centered eigenmodes if the divisor is on the line and the block is semisimple. "In infinite dimension a bounded invertible unitarizing similarity requires further uniform basis bounds; a formal algebraic modal completion is a weaker assertion."
- Lead: the "uniform basis bounds" caveat is exactly what the `||Z_t|| = 1` argument (L10-113) says cannot hold.
- Related: L10-007, L10-113, L10-121.

### L10-085 A multiple Riemann zero is compatible with the model — RH alone allows t·exp decay
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:142; cusp-bridge.md:96; positivity-products.md:118
- Raised by: three lanes independently
- Status at last mention: established distinction
- Content: "Model-space positivity accommodates multiplicity. RH alone allows polynomial times exponential decay; centered skew-adjointness would additionally impose semisimplicity and is stronger." The dissipative cMPS realization can accommodate Jordan blocks.
- Lead: never let a construction quietly assume simple zeros.
- Related: L10-029, L10-047, L10-109.

### L10-086 Lemma target 2: the modewise cusp leakage estimate ||jv||^2 >= (1/2)||v||^2
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:158-170
- Raised by: riemann_selberg_modes lane
- Status at last mention: stated as the target; explicitly RH-equivalent after the identification
- Content: on a common dense core with a genuine trace map j and physical energy norm satisfying `2 Re<v,Bv> = -||jv||^2`, an eigenmode gives `-2 Re(b) = ||jv||^2/||v||^2`. The needed arithmetic input is the *modewise* estimate `||jv||^2 >= (1/2)||v||^2` derived from automorphic cusp matching *before knowing zero locations*; with the FE pair `b -> -1/2 - conj(b)` it forces equality and width 1/4.
- Lead: "The quantifier matters: demanding this bound for *every* vector in a finite modal span is impossible for a one-row j when the dimension exceeds one; demanding a scalar dissipator is therefore the wrong target." Uetake's Section 5 Poincaré-series profiles supply non-zero-defined test data. "Neither bare cyclicity of the original minimal model nor generic positivity can prove it, as both hold for the unequal-width toys."
- Related: L10-006, L10-081, L10-087.

### L10-087 Uetake's cyclicity formulation as an alternative RH criterion
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-operators.md:26,170
- Raised by: riemann_selberg_modes lane
- Status at last mention: noted, not explored
- Content: the abstract states "an RH-equivalent cyclicity condition"; Theorem 6.3 (p.120) formulates it through cyclicity of an explicitly augmented input-output system.
- Lead: read Theorem 6.3 properly and see whether the augmentation is arithmetically natural. Explicitly flagged that bare cyclicity of the minimal model is not enough.
- Related: L10-013, L10-086.

### L10-088 The finite physical decay-selection theorem
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:106-116
- Raised by: cmps_decay_comparison lane (proved there)
- Status at last mention: proved; "a finite mechanism and counterexample family, not an arithmetic RH theorem"
- Content: on `C^(2|2)` with `P = Z⊗I`, `R = X⊗|0><1|`, `H = diag(aX+bZ, cX+dZ)`, `Q = -iH - R*R/2`, the output response `F(z) = tr[R*(z - L_eta)^{-1}(R sigma)]` has poles contained in the spectrum of the explicit 4x4 M, for *any* stationary sigma. If `b=0`, the candidate divisor has reflection `lambda -> -1/2 - lambda`; all four lie on `Re lambda = -1/4` exactly under the three non-strict inequalities; for `a > 1/4`, `S > 0` is an explicit letter-defined sufficient condition.
- Lead: the arithmetic analogue is L10-099.
- Related: L10-009, L10-010, L10-011.

### L10-089 bd = 0 is *necessary* for a common width in the quadratic family
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:43-47
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved
- Content: with `y = z + 1/4`, `det(zI - M) = y^4 + alpha y^2 - 2bd y + beta`, with `alpha = 2(a^2+b^2+c^2+d^2) - 1/8`. If all four poles have real part -1/4, reality of M forces the polynomial to be even in y, so `bd = 0`. "Ordinary parity symmetry, CAR regularity, complete positivity and a faithful mixed stationary state do not enforce it."
- Lead: an arithmetic model must supply the vanishing of the analogue of `bd`.
- Related: L10-012, L10-088.

### L10-090 Mode selection is robust within the quadratic class; generic parity-even interactions destroy the selection itself
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:56,114
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved
- Content: "**mode selection is robust within the quadratic class; uniform widths require a symmetry plus a band inequality; generic parity-even interactions destroy the selection itself**". `0.01 P` is a quartic fermion interaction; "The additional four modes cannot be dismissed as unphysical solely from grading."
- Lead: any arithmetic enlargement must be checked for the quartic analogue.
- Related: L10-012, L10-010.

### L10-091 Numeric residue size is only illustrative; denominator degree and coprimality prove visibility
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:100
- Raised by: cmps_decay_comparison lane
- Status at last mention: recorded methodological rule
- Content: for the `H + P/100` perturbation the reduced output denominator has degree exactly eight with numerator and denominator coprime — an exact statement, whereas the residues (~4.6e-5, 1.6e-4) are only indicative.
- Lead: assert visibility via exact coprimality, never via a residue magnitude threshold.
- Related: L10-035, L10-090.

### L10-092 The weak-drive counterexample: reflection survives, coercivity fails
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:92,114
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved, negative
- Content: at `a = c = 1/20, b = 0, d = 1/2` the four physical output poles remain, widths are approximately 0.0060754 and 0.4939246, exact discriminant `-2399/10000`. "This is a concrete counterexample to inferring uniform decay from the symmetry alone."
- Lead: the coercivity inequality is genuinely independent content.
- Related: L10-011, L10-081.

### L10-093 The explicit involution J derived directly from the letters
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:62-69
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved for b=0
- Content: `J = [0 0 -1 0; 0 0 0 1; -1 0 0 0; 0 1 0 0]`, `J^2 = I`, `JNJ = -N` with `N = M + I/4`, "derived directly from the letters, with no diagonalization".
- Lead: "Supply J from arithmetic symmetries, not by matching already computed eigenvalues."
- Related: L10-011, L10-099.

### L10-094 The full elementary width criterion: alpha >= 0, beta >= 0, alpha^2 - 4 beta >= 0
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:71-77
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved
- Content: with b=0, `alpha = 2(a^2+c^2+d^2) - 1/8` and `beta = (a^2-c^2-d^2)^2 + (-a^2-c^2+d^2)/8 + 1/256`. All four modes have width 1/4 exactly when both roots of `u^2 + alpha u + beta` are real and nonpositive. Strict inequalities give four distinct nonzero imaginary centered roots. "Endpoint Jordan behavior must be checked separately if an operator unitarizing metric is claimed."
- Lead: the arithmetic analogue is a three-inequality condition, not a single one.
- Related: L10-011, L10-085.

### L10-095 The positive metric G = diag(a+1/4, a-1/4) and the self-adjoint reduction to S
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:79-90
- Raised by: cmps_decay_comparison lane
- Status at last mention: proved
- Content: diagonalizing J (not M) gives `N = [[0,A],[B,0]]` with `AB = [[q^2-(a-c)^2-d^2, 2d(a-q)],[2d(a+q), q^2-(a+c)^2-d^2]]`, `q = 1/4`. For `a > q`, `AB` is self-adjoint in `G = diag(a+q, a-q)`, and minus it is similar to the real symmetric S. "a letter-derived symmetry gives a quadratic spectral relation, and the independent inequality `S >= 0` yields uniform modal widths."
- Lead: "The toy's 2x2 S is the complete model calculation for this step." Look for a sum-of-squares or boundary-flux proof of the arithmetic `S >= 0`.
- Related: L10-011, L10-099.

### L10-096 The physical norm transfer and the fermionic-correlation signed transfer must not be conflated
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:102; graded-channels.md:106, citing `refs/src/1211.3935/calculus.tex:378-403`
- Raised by: cmps_decay_comparison lane and graded-channels lane
- Status at last mention: established, verified against the cached Haegeman–Cirac–Osborne–Verstraete source
- Content: "the physical norm uses the plus-sign transfer, whereas a fermionic field two-point function uses the signed transfer between insertions. These two transfers must not be conflated. The signed transfer is not itself being asserted to be a physical CPTP evolution; it is the required fermionic correlation propagation inside a physical cMPS." The orientation with creation at the left endpoint gives the displayed trace expression in the canonical `l=I, r=sigma` gauge.
- Lead: use `L_eta` for correlations and `L` for dynamics, always labelled.
- Related: L10-009, L10-010, L10-100.

### L10-097 The critical BC state is not a normal density — a type-III/GNS formulation would be needed
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:134-138, citing `04c_phantasm_channels.tex:123-132`; cusp-bridge.md:102 (`:123-131,162-169`)
- Raised by: cmps_decay_comparison lane and cusp-bridge lane
- Status at last mention: recorded as a real limit problem
- Content: "treating it as a finite trace-one matrix would suppress a real limit problem. A proposed type-III/GNS formulation must replace the finite Schmidt-density argument with a specified state, positive covariance/GNS form, domains for its evolution and convergence of local physical correlations." Careful wording: "The word 'nonnormal' here concerns normality of a state as a functional; it is distinct from nonnormality of the finite decay matrix."
- Lead: the type-III/GNS route is named but never attempted. "Neither property by itself derives reflection symmetry, observable closure or the coercivity estimate."
- Related: L10-032, L10-070, L10-102.

### L10-098 Hyperbolicity is not itself a Lindblad emission process
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:128
- Raised by: cmps_decay_comparison lane
- Status at last mention: recorded conceptual correction
- Content: "The flow's Liouville measure is preserved; resonance decay describes relaxation of correlations of regular data, not loss of the L2 norm under the full transport group." The cusp adds an outgoing scattering boundary and a non-self-adjoint resonance problem; its positive boundary-energy identity is the natural passive-system/cMPS starting point, "but does not make all escape widths equal."
- Lead: the dissipation in the physical picture comes from the *cusp boundary*, not from hyperbolicity.
- Related: L10-014, L10-076.

### L10-099 The exact next arithmetic lemma: an arithmetic observable quadratic reduction (five numbered steps)
- Source: notes/rh-strategy-2026-09-19/riemann-vs-selberg-cmps.md:140-150
- Raised by: cmps_decay_comparison lane
- Status at last mention: stated as the concrete target; not pursued
- Content: replace "find a Lindbladian with the zeros as eigenvalues" by: (1) a finite generating family of odd observables closing under the correctly signed Heisenberg transfer, with explicit intertwiner and boundary source/sink (in the toy: the four Majoranas); (2) a letter symmetry giving `J(A+kappa)J = -(A+kappa)` with `kappa = 1/4`, J from arithmetic symmetries; (3) the square of the centered observable generator reducing, in an independently defined positive form, to minus an arithmetic self-adjoint S, with an analogue of `S >= 0` proved by sum-of-squares or boundary flux; (4) the selected output's meromorphic response having the desired zeta/scattering divisor including archimedean factors and correct affine normalization, distinguishing genuine cancellation from an omitted mode; (5) passing these identities to regular-data correlations on fixed domains with controlled meromorphic convergence and algebraic multiplicities.
- Lead: "The smallest immediate arithmetic experiment is to derive the signed Heisenberg image of the first proposed prime/cusp output letter and its first two commutators, and calculate the component outside its proposed generating family." Nonzero uncontrolled components are the analogue of `P/100`.
- Related: L10-001, L10-010, L10-011, L10-066, L10-068.

### L10-100 Three distinct spectra must be kept apart: no-jump Q, transfer L, and poles visible to insertions
- Source: notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:11-13
- Raised by: parent (orchestrator Claude)
- Status at last mention: established as a discipline
- Content: "A physical construction must say which of these carries the zeta divisor and prove that the modes are observable. The absorbing-vacuum construction does this for odd coherences but has trivial stationary entanglement; arbitrary mixed reinsertion need not preserve those modes."
- Lead: label every claimed spectrum with its object.
- Related: L10-002, L10-083, L10-101.

### L10-101 The finite inverse renewal criterion: M = -(B sigma + sigma B*) >= 0
- Source: notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:15-41; SYNTHESIS.md:33; graded-channels.md:132,150
- Raised by: parent (orchestrator Claude); cross-reviewed VALID by the graded-channels lane, which supplied a uniqueness strengthening
- Status at last mention: proved
- Content: for stable B with `E = -(B+B*) >= 0`, `L_Omega(X) = BX + XB* + Omega tr(EX)` is CP and trace preserving with explicit letters `R_ab = sqrt(w_a e_b)|v_a><u_b|`, `Q = B`. For target sigma with `r = tr(E sigma) > 0`, a reset density making sigma stationary exists iff `M >= 0`, and then `Omega = M/r` uniquely. Conversely every reset has a unique normalized stationary density `W/tr W` (from `X = tr(EX) W`); "faithfulness requires further controllability hypotheses."
- Lead: "Once an arithmetic no-jump generator and a proposed BC cutoff state are specified independently, positivity of the explicit matrix `M` is a falsifiable compatibility condition. The reset cannot be chosen freely while retaining that state."
- Related: L10-032, L10-102, L10-103.

### L10-102 Reinsertion changes the physical transfer spectrum — preserving no-jump modes is insufficient
- Source: notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:55; SYNTHESIS.md:33; riemann-vs-selberg-cmps.md:136
- Raised by: parent, verified numerically
- Status at last mention: proved by example
- Content: for `B = -iX - diag(1,0)/2` with no-jump modes `-1/4 ± i sqrt(15)/4`: resetting to `I/2` gives transfer modes `{0, -1/2, -1/2 ± 2i}`; resetting to `diag(1,0)` gives `{0, -1/2, -1/4 ± i sqrt(63)/4}`. "The same no-jump object therefore leads to different physical decay modes after reinsertion."
- Lead: decide which spectrum is supposed to carry the zeros before choosing a reset.
- Related: L10-100, L10-101.

### L10-103 Every biased diagonal target fails the renewal positivity; only the uniform target succeeds
- Source: notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:57
- Raised by: parent
- Status at last mention: proved exactly
- Content: for `sigma = diag(p, 1-p)` the required reset numerator has determinant `-(1-2p)^2`, so only `p = 1/2` works. "This is an exact algebraic example of the compatibility constraint, not a numerical conjecture."
- Lead: a Gibbs-weighted BC cutoff state is a *biased* target — this is a direct warning about that route.
- Related: L10-032, L10-101, L10-134.

### L10-104 The grading obstruction: stable graded bond + rank-one homogeneous exit is impossible
- Source: notes/rh-strategy-2026-09-19/cmps-renewal-bridge.md:43-47; graded-channels.md:152 (cross-review VALID)
- Raised by: parent; independently confirmed
- Status at last mention: proved, negative — with explicit escapes
- Content: if both parity sectors are nonzero, B commutes with P, and `E = -(B+B*)` has rank one, then E's range lies wholly in one parity sector and the other sector evolves unitarily, so B cannot be stable on the whole graded bond.
- Lead: escapes named — "More exits, a reference sector with different dynamics, an operator/coherence grading, or a restricted resonance realization". It does not rule out the reference-vacuum embedding or a proper observable coherence space.
- Related: L10-002, L10-028, L10-059.

### L10-105 The Poisson-equation / mean-absorption-time method as a transferable certificate
- Source: notes/extract/2609.12284-reading.md:91-100,143-150
- Raised by: orchestrator (Claude), reading Shang, arXiv:2609.12284
- Status at last mention: identified as "the transferable item"
- Content: in the Heisenberg picture, `L†(G^+ - beta P) = -Q`, so `Y = G^+ - beta P` solves `L†Y = -(1-P)` and is bounded (`-beta P <= Y <= kappa^2 Q`). "a bounded solution of the Poisson/Lyapunov equation certifies uniform worst-case exponential mixing" — the quantum analogue of `t_mix <~ max expected hitting time × log(1/eps)`. The paper's Theorem 1 gives `t_mix(eps) <= 3 kappa^2 ceil(2 log_2(1/eps))`, dimension-independent, with *no spectral information used at any point*.
- Lead: for the notebook's absorbing-vacuum channel the analogues are `q(t) = Tr(Z_t X Z_t†)` and the Gramian `W = ∫_0^inf Z_t† Z_t dt` (finite N: `B†W + WB = -1`), with `sup_rho D(rho_t, Omega)` lying between `||Z_t||^2` and `||Z_t||`.
- Related: L10-113, L10-115.

### L10-106 Exact spectrum of the reset Lindbladian (fact i)
- Source: notes/extract/2609.12284-reading.md:107-116
- Raised by: orchestrator (Claude), inferred and numerically checked, not in the paper
- Status at last mention: checked numerically to 1e-14, not registered
- Content: `spec L = {0} ∪ {-sigma_j(A)^2} ∪ {-(lambda_i + lambda_k)/2, i != k}`, proved via the matrix determinant lemma: `prod_j(z+lambda_j)(1 - <b|(z+FF†)^{-1}|b>) = det(z + FF† - |b><b|) = det(z + AA†)`. All eigenvalues real.
- Lead: recorded as follow-up 4 — "a small worked example of 'gap = mixing rate, Jordan blocks invisible to trace-distance mixing'".
- Related: L10-107, L10-108, L10-115.

### L10-107 Gap equals mixing rate here: a benign, not a non-normal, example (fact ii)
- Source: notes/extract/2609.12284-reading.md:118-123,143-147
- Raised by: orchestrator (Claude)
- Status at last mention: checked
- Content: `gap ∈ [sigma_min(A)^2/2, sigma_min(A)^2]`; in the lower-bound instance the slowest mode is the psi-|2> coherence at half the population rate. "no cutoff, no dimension-dependent burn-in, no transient amplification (prefactor sqrt(q_0) <= 1)."
- Lead: this paper gives *no* general relation between spectrum and mixing time — it is a worked benign case, so it cannot be cited as evidence that gap controls mixing in the Riemann setting.
- Related: L10-105, L10-116.

### L10-108 Jordan blocks occur at codimension one and the mixing theorem is blind to them (fact iii)
- Source: notes/extract/2609.12284-reading.md:125-131
- Raised by: orchestrator (Claude)
- Status at last mention: checked with an explicit instance
- Content: with `A = diag(1, 1/3)`, `b = (cos th, sin th)`, `th* = 0.49088...`, the eigenvalue -1/9 has algebraic multiplicity 3 and geometric multiplicity 2 (one 2x2 Jordan block). Theorem 1 holds uniformly in (A,b), so the trace-distance bound does not see it: `t e^{-t/9}` is absorbed into constants. "Same moral as 'Weil positivity is blind to Jordan blocks'."
- Lead: a mixing-time formulation of RH would likewise be blind to multiple zeros — either a feature or a sign it is the wrong formulation.
- Related: L10-047, L10-085, L10-118.

### L10-109 Rank-one reset bonds make the ring zeta factorise (fact iv)
- Source: notes/extract/2609.12284-reading.md:133-139,205-206
- Raised by: orchestrator (Claude)
- Status at last mention: raised, explicitly low priority
- Content: with `R_j = J_j` and `Q_cMPS = -G/2`, `sum_j J_j ⊗ J̄_j` has rank one, so `det(z - T) = det(z - K)(1 - <<G|(z-K)^{-1}|R>>)`: the ring zeta `1/det(z-T)` factorises into a free part and a secular factor whose zeros are `-spec(AA†)`. "There is no grading and no fermionic structure in the paper."
- Lead: "Low priority: ring zeta of rank-one reset bonds via the determinant lemma, as a toy for sdet factorisations; unlikely to reach arithmetic content."
- Related: L10-113.

### L10-110 Shang's structural class: fixed no-event generator plus scalar reset, a cousin of the vacuum-decay model
- Source: notes/extract/2609.12284-reading.md:176-181, citing `04d_bc_symmetry_generators.tex:233-236`
- Raised by: orchestrator (Claude)
- Status at last mention: recorded placement
- Content: the difference from the repo's vacuum-decay model is that the dark state psi is annihilated by the no-event generator while the reset target `|r>` overlaps it (`p > 0`), "which is what makes the population block a nontrivial rank-one feedback".
- Lead: a nonzero overlap between dark state and reset target is the mechanism that turns a pure fixed point into a nontrivial feedback — potentially useful for the mixed-reset question.
- Related: L10-101, L10-109.

### L10-111 The paper's own scope caveat: initialization avoids the slow mode
- Source: notes/extract/2609.12284-reading.md:62-69, quoting pdp.tex:1051
- Raised by: a paper (Shang, arXiv:2609.12284)
- Status at last mention: quoted
- Content: "The lower bound is not an oracle lower bound for linear-system solving, nor a lower bound for every purely dissipative design. Its input has an easily prepared solution, and initialization at $\ket r$ does not populate the slow mode used in the proof."
- Lead: directly the model for L10-114 — restrict the initial states.
- Related: L10-114.

### L10-112 The AI-authorship statements in both read papers
- Source: notes/extract/2609.12284-reading.md:26-27 (pdp.tex:1065); notes/extract/2609.13121-reading.md:17-18 (BZ:640, BZ:307)
- Raised by: the papers
- Status at last mention: recorded verbatim
- Content: Shang: "The Lindbladian construction and the complexity analysis were developed through multiple rounds of discussion between the author and the GPT6 Astra, where AI makes the main technical contributions." Becker–Zworski: appendix credited to "Chat GPT 6"; "the key Volterra factorisation argument was suggestedby ChatGPT" (typo verbatim).
- Lead: relevant precedent for the repo's own prover-lane methodology (Codex/Astra as prover, Opus as refuter).
- Related: -

### L10-113 ||Z_t|| = 1 for every t, independently of RH — the biggest recorded negative
- Source: notes/extract/2609.12284-reading.md:153-167,196-198,218-219
- Raised by: orchestrator (Claude), marked [inferred] and **unreviewed**
- Status at last mention: raised, awaiting a second reader; ranked follow-up 2
- Content: for inner S on the lower half-plane and `phi_t(z) = e^{-itz}`, the model-space kernel estimate gives `||Z_t|| >= |phi_t(w)| - |S(w)| = e^{-t eps} - |S(x - i eps)|` at `w = x - i eps`. For `S(tau) = xi(1-2i tau)/xi(1+2i tau)`, Stirling gives a Gamma ratio ~ `x^{-2 eps}` and the convexity bound gives `|zeta(1-2eps+2ix)| << x^{eps+delta}` with `|zeta(1+2eps+2ix)|` bounded below, so `|S(x-i eps)| -> 0` as `x -> inf` for each fixed `0 < eps < 1/4` (mpmath: eps=0.2 gives |S| = 0.72, 0.60, 0.095, 0.027 at x = 10, 100, 1000, 5000). Hence the Riemann semigroup is not uniformly exponentially stable, the Riesz-basis/Lyapunov certificate `A†G + GA = -2 Delta G` with G bounded invertible **cannot hold on all of K_S**, and the absorbing-vacuum channel on `C ⊕ K_S` has **infinite worst-case trace-distance mixing time**.
- Lead: "If confirmed, record as a proved negative: 'no worst-case mixing-time form of RH for the Riemann/absorbing-vacuum channel'." Consequence: any mixing-time form of "all rates 1/4" must restrict initial states or use a weighted norm. This directly limits the Lyapunov targets of L10-006/L10-047.
- Related: L10-006, L10-047, L10-084, L10-114, L10-121.

### L10-114 Restricted mixing: find the initial-state class on which the Poisson argument does go through
- Source: notes/extract/2609.12284-reading.md:199-202; 2609.13121-reading.md:106,155
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued
- Content: candidates named: `X` with `Tr(XW)` finite, or smooth vectors / the domain of a power of B. "check whether 'all modes at rate 1/4' is then equivalent to a uniform exponential bound on that class (a Gearhart–Pruss-type statement in a weighted norm)." The Becker–Zworski note gives the right form: `||Z(t)f|| <= C(f) e^{-t/4}` on a regularity class.
- Lead: this is the repair for L10-113 — the correct statement of RH as decay is one-sided and class-restricted.
- Related: L10-111, L10-113, L10-121, L10-122.

### L10-115 Truncated Riemann semigroup non-normality: the cheap decisive numerical test
- Source: notes/extract/2609.12284-reading.md:189-195; 2609.13121-reading.md:112-116,158-161
- Raised by: orchestrator (Claude), ranked follow-up 1
- Status at last mention: raised, not run
- Content: for the Blaschke product with the first N zero pairs (`w = -gamma_n/2 - i/4`), compute in the normalized-kernel basis the Gram condition number `cond(Gamma_N)`, `M_N = sup_t e^{t/4}||Z_t^{(N)}||`, and `||W_N||` (compare with 2, the value for a normal operator with all population rates 1/2). Test: `M_N` and `||W_N||` grow without bound in N, as the `||Z_t|| = 1` argument predicts; measure the growth law against the zero density `log(gamma/2pi)`. The Becker–Zworski analogue is already measured: for `V = x^2/2, h=1`, the Fock-truncated generator has eigenvector condition number 17.5, 145, 1.2e3, 1.1e4, 9.3e4 at d = 4,6,8,10,12, with no Jordan blocks.
- Lead: "Cheap, decisive for TJO's 'non-normal/Jordan effects' hypothesis."
- Related: L10-113, L10-121.

### L10-116 Becker–Zworski: optimal relaxation rate = spectral gap for a non-normal GKLS generator, on a weighted class only
- Source: notes/extract/2609.13121-reading.md:46-51,99-108
- Raised by: a paper (Becker–Zworski, arXiv:2609.13121)
- Status at last mention: read; identified as "a worked example that this is the correct form"
- Content: Theorem 1 gives `||e^{tL}T - Pi||_1 <= C_{h,V} e^{-gamma_h t}(||T||_1 + ||r|_diag - 1||_{L^2(mu)} + ||G_0||_{L^2(mu)})` with `gamma_h = lambda_1(h)/(2h)`, "and this exponent is optimal". Crucially there is no gap on all of trace class. The repo's own RH statement, after the FE reflection, is one-sided ("no mode slower than 1/4"), so the correct analogue is `||Z(t)f|| <= C(f) e^{-t/4}` on a regularity class.
- Lead: adopt this *form* for the RH decay statement. "the operator-norm version can fail even when the spectral bound is right."
- Related: L10-113, L10-114, L10-122.

### L10-117 The untypeset tail of Becker–Zworski contains the no-gap proof that a typeset remark relies on
- Source: notes/extract/2609.13121-reading.md:22-27,68-72,175
- Raised by: orchestrator (Claude), reading the source
- Status at last mention: recorded
- Content: lines 977–1132 come after `\end{document}` and are not typeset: a quadratic-model section with an energy bound, a proof that there is no spectral gap on trace class (`‖LX_N‖_1/‖X_N‖_1 = 2/H_N -> 0`, and in fact `‖e^{tL}|_{tr X=0}‖_{1->1} = 1`), and a slow-decay example `E(t) ~ c/(2t)` for trace-class T with infinite energy. Remark 1 in the typeset text *relies* on the no-gap claim, whose proof lives only in the tail, which also cites bib keys commented out of the bibliography.
- Lead: if the no-gap fact is used downstream, it must be reproved or the tail cited as such. `‖e^{tL}|_{tr X=0}‖_{1->1} = 1` is the exact analogue of the `||Z_t|| = 1` claim.
- Related: L10-113, L10-116.

### L10-118 A Jordan block at the slowest rate is ruled out by a Becker–Zworski-type bound
- Source: notes/extract/2609.13121-reading.md:109-111
- Raised by: orchestrator (Claude), inference
- Status at last mention: raised
- Content: "a Jordan block at `-gamma_h` whose generalized eigenvector lies in the admissible class would force a `t e^{-gamma_h t}` term, contradicting the bound. So the theorem rules that out, for the slowest rate only. The paper does not discuss Jordan structure."
- Lead: an RH decay bound on a regularity class would similarly rule out Jordan blocks *at the extreme rate only* — worth stating precisely, since multiple zeros are otherwise allowed.
- Related: L10-085, L10-108, L10-127.

### L10-119 The doubled-space form of the transfer generator is generic, so it is not evidence
- Source: notes/extract/2609.13121-reading.md:120-123
- Raised by: orchestrator (Claude), inference
- Status at last mention: recorded caution
- Content: `M = Q_x + Q_y + h ∂_x ∂_y` is exactly `Q⊗1 + 1⊗Q̄ + R⊗R̄` with `R ~ sqrt(h) ∂`. "This form is generic for any vectorised Lindbladian, so it is not special evidence."
- Lead: do not cite structural resemblance of vectorised generators as support.
- Related: L10-120.

### L10-120 The SUSY splitting is clean but the Witten index cancels the entire nonzero spectrum — negative as a ring-norm mechanism
- Source: notes/extract/2609.13121-reading.md:124-129
- Raised by: orchestrator (Claude), inference
- Status at last mention: pursued, negative
- Content: the SUSY pair `Q ≃ -a*a/2h`, `S ≃ -aa*/2h` with `∂_x Q = S ∂_x` moves the off-diagonal information into the "1-form/fermionic" sector, which has no zero mode — "a clean case of a graded splitting that separates the fixed point from relaxation". But the supertrace `tr e^{-tH/2h} - tr e^{-t aa*/2h} = 1` (the Witten index) cancels everything nonzero. "A trace formula needs the opposite (zeros surviving with a sign), so as a ring-norm mechanism this is **negative**."
- Lead: a graded splitting that is *too* clean destroys the trace formula. Any grading used for the Phantasm must have a supertrace that does *not* collapse.
- Related: L10-057, L10-125.

### L10-121 Sarason's formula as the route to computing ||Z(t)||
- Source: notes/extract/2609.13121-reading.md:152-157
- Raised by: orchestrator (Claude), speculation to test, ranked follow-up 1
- Status at last mention: raised, not done
- Content: `||Z(t)|| = dist_{L^inf}(e^{i tau t}, S·H^inf)` (sign conventions to fix). "Zeros at constant height with spacing -> 0 are not interpolating, so the reproducing kernels are not a Riesz basis. Expect: no uniform bound. Checkable numerically with finitely many zeros (Blaschke truncation)."
- Lead: an independent route to the same `||Z_t|| = 1` conclusion as L10-113, which would settle it.
- Related: L10-113, L10-115, L10-084.

### L10-122 The pure-fixed-point reduction ||A - Pi||_1 = 2||A - Pi||_op
- Source: notes/extract/2609.13121-reading.md:92-95,158-161
- Raised by: a paper (Becker–Zworski, BZ:676-679), flagged as directly applicable
- Status at last mention: raised, not used
- Content: for `A >= 0` with trace 1 and pure Pi, `A - Pi` has at most one negative eigenvalue, so `||A - Pi||_1 = 2||A - Pi|| <= 2||A - Pi||_2`. "it turns trace-norm mixing into operator/HS estimates whenever the fixed point is pure. Directly applicable, elementary."
- Lead: apply to the notebook's vacuum-decay Lindbladian and compute the exact trace-norm decay alongside the eigenvector condition number.
- Related: L10-115, L10-114.

### L10-123 A discrete arithmetic Witten Lindbladian on l^2(N) — proposed as a clean negative
- Source: notes/extract/2609.13121-reading.md:162-165
- Raised by: orchestrator (Claude), marked [speculation]
- Status at last mention: raised, not done; predicted outcome negative
- Content: "on ℓ²(ℕ) choose a jump `a` with `aν=0`, `ν_n ∝ n^{−β/2}` (normalisable iff β>1, pole at β=1). Compute `a*a` spectrum and coherence rates. Predicted outcome: real spectrum, no zeros. Worth doing only as a clean negative confirming that a single-jump 'purified Gibbs' Lindbladian cannot carry the zeros."
- Lead: cheap; would close off the single-jump purified-Gibbs family for good. The `β=1` pole is the zeta-flavoured detail.
- Related: L10-124, L10-134.

### L10-124 Vacuum coherences of a purified-Gibbs Lindbladian are real-rate: zeros cannot appear without a non-self-adjoint Witten Laplacian
- Source: notes/extract/2609.13121-reading.md:136-143
- Raised by: orchestrator (Claude), inference marked negative
- Status at last mention: established as a negative
- Content: the diagonal is a reversible classical diffusion with real spectrum and Gibbs invariant measure, and the vacuum coherences `|ν><φ_k|` are exact eigenmodes with rates `λ_k/2h`. "The coherence rates are spectra of a self-adjoint `H >= 0`, so they are real, with no oscillation. Zeros (complex modes `β/2 + iγ/2`) cannot appear this way without a non-self-adjoint 'Witten Laplacian'. Not KMS-detailed-balance in the quantum sense: Π is not faithful."
- Lead: names exactly what would have to be broken — self-adjointness of the effective Laplacian — for a purified-Gibbs construction to carry zeros.
- Related: L10-123, L10-134.

### L10-125 A 3x3 non-normal toy test of the Lyapunov criterion restricted to the slowest sector
- Source: notes/extract/2609.13121-reading.md:166-167
- Raised by: orchestrator (Claude), ranked follow-up 4
- Status at last mention: raised, not done
- Content: "Check the Jordan-block inference in (a) on a 3×3 non-normal toy: whether a BZ-type weighted-norm bound with t-independent constant is equivalent to the Lyapunov criterion `A†G+GA ≤ −2γG` restricted to the slowest sector."
- Lead: small and cheap; would tell us whether the weighted-norm decay statement and the Lyapunov certificate are the same thing sector by sector — directly relevant to L10-006/L10-068.
- Related: L10-006, L10-068, L10-118.

### L10-126 Log-Sobolev enters only as a tool on the classical measure and does not give the rate
- Source: notes/extract/2609.13121-reading.md:95,117
- Raised by: orchestrator (Claude)
- Status at last mention: recorded
- Content: the log-Sobolev inequality for mu (Barthe–Roberto plus Gross hypercontractivity) is used only to relax `d ∈ L^inf` to `d ∈ L^q`. "It does not give the rate. Nothing about cutoff."
- Lead: do not expect log-Sobolev machinery to supply a uniform rate in the arithmetic setting.
- Related: L10-127.

### L10-127 Neither Lindblad paper supplies expanders, a Hastings bound, Ramanujan graphs or cutoff
- Source: notes/extract/2609.12284-reading.md:183-185,214-215; 2609.13121-reading.md:147-148,173-174
- Raised by: orchestrator (Claude)
- Status at last mention: established negative
- Content: neither paper has families, degree, an Alon–Boppana/Hastings-type bound, or cutoff. Shang's bound has no cutoff (prefactor <= 1 from t = 0) and its rates range over `[kappa^{-2}/2, 2]`, "so no 'one rate' structure". Neither has KMS/GNS detailed balance for a faithful state, cMPS, grading/supertrace, or number theory.
- Lead: stop mining the Lindblad-mixing literature for the Ramanujan side; the transferable content was two method items (L10-105, L10-122) and two negatives (L10-113, L10-120).
- Related: L10-055, L10-105, L10-113.

### L10-128 Siemon–Holevo–Werner's exit-space / reinsertion / rebound formalism as the template for an unbounded arithmetic generator
- Source: notes/extract/shw-unbounded-generators-sources.md:11-79
- Raised by: TJO's pointer (fetched 2026-09-12)
- Status at last mention: quotes byte-verified and registered; the formalism is available but not yet used for a Riemann generator
- Content: a **no-event semigroup** maps every pure state to a multiple of a pure state and is necessarily `C_t rho C_t*` with `C_t = exp(tK)` a strongly continuous contraction semigroup; the exit space is defined by `<j psi, j phi> = -(<K psi, phi> + <psi, K phi>)`; `||J phi||^2 = ||phi||^2 - lim_t ||e^{tK}phi||^2 <= ||phi||^2`; a **standard** semigroup is the minimal solution from a CP perturbation of a no-event generator; reinsertion maps `reins: tc(Exit) -> th` satisfy `tr reins(sigma) <= tr sigma`, and jump operators correspond precisely to Kraus operators of the reinsertion via `L_alpha = M_alpha j`. Worked example: the half-sided shift on `L^2(R^+, dx)` has exit space `C` with `j psi = psi(0)` and a rebound state Omega.
- Lead: this is the exact machinery the domain caution of L10-080 and the kink no-go of L10-051 call for — an unbounded no-event generator with a genuine boundary exit. The half-sided-shift example is the natural model for the Hardy/half-line compression.
- Related: L10-032, L10-051, L10-080, L10-129, L10-131.

### L10-129 Semigroups probability-preserving to first order but not for finite times
- Source: notes/extract/shw-unbounded-generators-sources.md:116-121 (TORUN.tex:147)
- Raised by: a paper (Siemon–Holevo–Werner, citing Davies and Holevo examples)
- Status at last mention: quoted, not explored
- Content: "Further examples are given of semigroups, which appear to be probability preserving to first order (i.e., when looking only at the generator on the finite-rank part of its domain), but not for finite times."
- Lead: a direct warning for any arithmetic generator checked only at the level of the formal GKLS relation `Q + Q* + sum R*R = 0`; conservativity at finite times is a separate theorem.
- Related: L10-070, L10-128.

### L10-130 Nonstandard dynamical semigroups
- Source: notes/extract/shw-unbounded-generators-sources.md:95-107 (TORUN.tex:646,650)
- Raised by: a paper (Siemon–Holevo–Werner)
- Status at last mention: quoted, not explored
- Content: `gen_hat rho = gen rho - tr(gen rho) rho_hat`, same domain. "The key observation is that `gen` is infinitesimally trace preserving on `dom gen^0`, so `ppert = gen - gen^0` is already as large as it can be."
- Lead: nonstandard generators are a genuine extra class — if a Riemann no-event generator turns out non-conservative, this is how to repair it without changing the no-event part.
- Related: L10-128, L10-129.

### L10-131 Arveson "units" of a dynamical semigroup
- Source: notes/extract/shw-unbounded-generators-sources.md:109-114 (TORUN.tex:677)
- Raised by: a paper (Siemon–Holevo–Werner, citing Arveson)
- Status at last mention: quoted once, never used
- Content: "Bill Arveson calls no-event semigroups with this property the *units* of the semigroup."
- Lead: Arveson's product-system/units theory is an unexplored structural frame for the no-event letters; nobody in the repo has looked at it.
- Related: L10-128.

### L10-132 A sign error in the source's gauge lemma (Kgauge)
- Source: notes/extract/shw-unbounded-generators-sources.md:123-129 (TORUN.tex:378 vs :402)
- Raised by: orchestrator (Claude), reading the source
- Status at last mention: recorded and resolved
- Content: the displayed (Kgauge) has `K' = K + sum conj(lambda) L + (1/2)(i beta + sum |lambda|^2)`, while the dissipativity computation in the proof uses `K' = K - sum conj(lambda) L - (1/2) sum |lambda|^2 (+ i beta/2)`. "Only the second sign leaves the generator invariant under `L -> L + lambda`." Verdict: "Read (Kgauge) with the proof's sign."
- Lead: use the proof's sign in any gauge-fixing of the arithmetic letters.
- Related: L10-128.

### L10-133 The BC finite-level representation obstruction B0.2 comes from the algebra relations, not from approximating the zeros
- Source: notes/extract/bc-symmetry-sources.md:14-34
- Raised by: repo (notes/bc-symmetry-generators.md), sources registered
- Status at last mention: established
- Content: from Connes–Marcolli math/0404128: `varphi_beta(e(a/b)) = b^{-beta} prod_{p | b} (1 - p^{beta-1})/(1 - p^{-1})` for `0 < beta <= 1`, plus `mu_n* mu_n = 1` and `mu_n e(r) mu_n* = (1/n) sum_{ns=r} e(s)`. "These relations, not any approximation of the zeta zeros, give the finite representation obstruction B0.2."
- Lead: the obstruction is structural — a finite matrix representation of the BC algebra is blocked by the isometry relations themselves.
- Related: L10-069, L10-134.

### L10-134 The prime-level matrix extension B1.1 is stipulated, not sourced
- Source: notes/extract/bc-symmetry-sources.md:33-34,45-49
- Raised by: orchestrator (Claude), flagging provenance honestly
- Status at last mention: recorded as our own stipulation
- Content: "The prime-level matrix extension in B1.1 is stipulated and analysed here; it is not claimed in this source." Also: "Our finite cone uses equality, for trace preservation, and derives its conditional Choi description explicitly. The source's unbounded-domain and conservativity caveats remain applicable to any future adelic limit; finite-dimensional feasibility alone is not such a limit theorem."
- Lead: a finite feasibility result in the BC cone is not a step toward the adelic limit until a limit theorem exists.
- Related: L10-069, L10-070, L10-129, L10-133.

### L10-135 vom Ende on unique decompositions of generators — consulted, not used
- Source: notes/extract/bc-symmetry-sources.md:52-55
- Raised by: orchestrator (Claude)
- Status at last mention: "abstract consulted, not used as a premise or registered claim"
- Content: Frederik vom Ende, *Understanding and Generalizing Unique Decompositions of Generators of Dynamical Semigroups*, arXiv:2310.04037.
- Lead: canonical uniqueness of the (K, L_alpha) decomposition matters if one wants to claim an arithmetic generator's letters are *the* letters rather than one gauge among many. Never followed up.
- Related: L10-132.

### L10-136 The NIPS 2009 supplementary material is the one document that could extend Watanabe–Fukumizu to loops
- Source: notes/reviews/provenance-2026-09-12.md:170-173,342-345
- Raised by: Opus reviewer (adversarial provenance review)
- Status at last mention: raised, not fetched
- Content: `1103.0605:section3.tex:374-375` says "A direct proof of Corollary `cor:IBfornonhyper`, without discussing hypergraphs, is found in the supplementary material of the NIPS 2009 paper". That supplement is not in `refs/src/`. "The claim cannot be repaired by appeal to a document nobody in this repo has read."
- Lead: fetch it. If its direct proof covers loops, the repo's Theorem 1 priority claim is repaired; otherwise the bouquet case is genuinely ours.
- Related: L10-137.

### L10-137 A bouquet is not a Watanabe–Fukumizu graph — Theorem 1 is a loop-admitting *extension*, not a special case
- Source: notes/reviews/provenance-2026-09-12.md:140-167,193-210,328
- Raised by: Opus reviewer
- Status at last mention: MAJOR issue, VERDICT wf-equivalence INVALID, with draft replacement wording supplied
- Content: WF edges are two-element subsets of V, so loops (degree-1 subsets) and multiple edges are excluded; their `d_i` counts hyperedges (D/2 on a bouquet, not D); and their own scalar Ihara–Bass specialisation evaluates on a bouquet to `(1-u^2)^{D/2-1}(1 - u + (D/2-1)u^2)`, which is wrong — the truth is `(1-u^2)^{D/2-1}(1 - Du + (D-1)u^2)`. The algebra of the identification is nonetheless exactly right (push-through for A, `i ↔ ī` relabelling for D, the pair prefactor, no dropped weight hypothesis), verified numerically on a bouquet.
- Lead: adopt the reviewer's draft wording. "Do **not** let this stand as a priority concession: for arbitrary (non-invertible) weights *on a bouquet*, no local source covers the case."
- Related: L10-136, L10-138.

### L10-138 The order-of-composition and source-vs-target-weight differences wash out of det(1 - u·)
- Source: notes/reviews/provenance-2026-09-12.md:91-115,333
- Raised by: Opus reviewer
- Status at last mention: MINOR issue; one sentence requested
- Content: WF compose prime cycles first-step-leftmost while the note composes last-step-leftmost, and reversing a product of >= 3 matrices is not a cyclic permutation, so individual Euler factors differ. They agree because (a) reversal is a bijection of cyclically non-backtracking index sequences (sigma is an involution), and (b) with `d = diag(uE_e)` and `B_{e,e'} = [e' != ē]`, `M = dB` and `T = Bd`, so `det(1-M) = det(1-uT)` by Sylvester. Verified to 4e-16. Noted in passing: "WF are internally inconsistent here: their hypergraph definition gives the *reverse* of their graph definition."
- Lead: add the reversal-bijection / Sylvester sentence.
- Related: L10-137.

### L10-139 Fifteen of thirty-nine citation addresses do not resolve — but zero misquotes
- Source: notes/reviews/provenance-2026-09-12.md:9-13,77-79,329-332,349-353
- Raised by: Opus reviewer
- Status at last mention: MAJOR, with exact fixes listed
- Content: "**no quoted string is misquoted or fabricated**". But 11 citations name a nonexistent file (`1801.00876` → `tenseur9.tex`, `2304.05714` → `PT-RC_reloaded.tex`, `0706.0556` → `sd10.tex`, `0709.1142` → `main.tex` not `expand.tex`, `2309.15873` → `AiM_Final.tex`, `2405.04361` → `v3.tex`), 2 point past EOF (`2204.06424:main.tex:3068` and `:3095-3096`; the file is 2342 lines — the real loci are `main.bbl:30`, `main.bbl:94,100`), and 2 ranges exclude the quote they label (eq. 2.8 is at 479–482 not 480–485; eq. 2.10 at 503–505 not 505–510).
- Lead: rewrite the filenames and ranges. "`refs/README.md` promises re-checkability against these paths; as written, 11 citations do not resolve."
- Related: L10-140.

### L10-140 Matsuura–Ohta's own extension to U(N_c) is *better* for the repo's claim 3
- Source: notes/reviews/provenance-2026-09-12.md:286-290,334
- Raised by: Opus reviewer
- Status at last mention: MINOR issue with an upside
- Content: the source line 470 reads "While the above discussion assumes $G$ to be a finite group, the same procedure can be extended to the case where $G$ is the compact Lie group $U(N_c)$" — which "refutes the prior-art gloss that 2607.27935 gives the L-function 'for a representation $R$ of **any** group", but is better for claim 3 "since `ρ_adj` of `U(N_c)` is precisely the notebook's object."
- Lead: reword the gloss and *claim the upside*.
- Related: L10-141.

### L10-141 "Finite Galois group" is an inference, not in the local bytes
- Source: notes/reviews/provenance-2026-09-12.md:260-284,335
- Raised by: Opus reviewer
- Status at last mention: MINOR, defensible but over-attributed
- Content: "of the Galois group of a covering" is supported; "finite" appears nowhere in the local sources, following only from graph finiteness (`AiM_Final.tex:203`, `v3.tex:470`). The downstream conclusion stands: `Ad(U_i)` for generic unitaries generates an infinite group, so the notebook's object is not literally a Stark–Terras L-function.
- Lead: attach the inference explicitly or drop "finite".
- Related: L10-140.

### L10-142 Pick one vectorisation convention repo-wide
- Source: notes/reviews/provenance-2026-09-12.md:248-251,336
- Raised by: Opus reviewer
- Status at last mention: MINOR, open
- Content: prior-art writes `A_X = sum_i U_i ⊗ Ū_i`, conflicting with the theorem note's own `Ad(A) = Ā ⊗ A` (`quantum-ihara-general.md:19`) and with MO's `rho_adj(U_e) = U_e ⊗ U_e†`.
- Lead: fix one convention everywhere; conventions of this kind have already caused two sign errors elsewhere in the repo (L10-016, L10-132).
- Related: L10-016, L10-132.

### L10-143 Script/report gaps: the displayed form det(1 + D - A) is never evaluated
- Source: notes/reviews/provenance-2026-09-12.md:303-320,338-339; theorem1-algebra-2026-09-12.md:161-166
- Raised by: Opus reviewer (both reviews)
- Status at last mention: MINOR, fix suggested
- Content: `scripts/qihara_general.py` tests the equivalent `1 - uM(u)` form, not the displayed `1 + D(u) - A(u)`; the two are identical by one line of linearity, "but strictly the *displayed* identity is never evaluated. A two-line addition evaluating `det(1 + D(u) - A(u))` directly would close the gap." Also: docstring/label drift (case (c) mislabelled, case (d) undocumented); "at three complex u" when two are real; case (c) (D=2) is run and passes but is omitted from §5; `exact_check` draws random rationals from an RNG shared with the float checks, so the "exact" instances are not reproducible independently of execution order; `w5` assigned twice; `pref` multiplies over a `set` so iteration order is nondeterministic.
- Lead: add the direct evaluation and a separate RNG for the exact checks.
- Related: L10-144, L10-149.

### L10-144 Theorem 1's "identity of rational functions" clause is redundant and mildly misleading
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:19-34
- Raised by: Opus reviewer (REFUTE-stance verifier)
- Status at last mention: MINOR, exact replacement wording supplied
- Content: steps ⟨1⟩1–⟨1⟩7 are valid *pointwise* at any single u satisfying ASSUME; nothing needs small `|u|`, a Neumann series, or continuation. The ASSUME set is the complement of the zero locus of `prod_p det(1 - u^2 E_ī E_i)`, which equals 1 at u=0, hence cofinite. Verified numerically at `|u|/r` up to 32 outside the Neumann disc (rel. err <= 1e-14).
- Lead: replace the last sentence of ⟨1⟩8 with the supplied wording.
- Related: L10-145, L10-146.

### L10-145 The norm bound in Theorem 1 needs three repairs
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:36-43
- Raised by: Opus reviewer
- Status at last mention: MINOR
- Content: `min_i ||E_ī E_i||^{-1/2}` is (a) undefined when some `E_ī E_i = 0` (nilpotent Kraus data), (b) better written `(max_i ||E_ī E_i||)^{-1/2}`, (c) requires a submultiplicative norm, which the note never specifies.
- Lead: write `|u| < (max_i ||E_ī E_i||)^{-1/2}` with the operator norm and the convention `0^{-1/2} := inf`.
- Related: L10-144.

### L10-146 Corollary 3 divides by 1 - u^2 without stating the exclusion
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:45-54
- Raised by: Opus reviewer
- Status at last mention: MINOR
- Content: `A(u) = uSigma/(1-u^2)`, `D(u) = Du^2/(1-u^2)` and the determinant identity all need `u^2 != 1`, yet the conclusion is an identity of polynomials. It extends by continuity, but the corollary never says so, and Theorem 1's hypothesis genuinely fails at `u^2 = 1` here. Verified symbolically for D = 2,4,6 with N=2, including at `u = ±1`.
- Lead: append "for `u^2 != 1`, hence for all u since both sides are polynomials."
- Related: L10-144.

### L10-147 Corollary 4's "as they partly do in Corollary 3" is false at D = 2
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:56-65
- Raised by: Opus reviewer
- Status at last mention: MINOR
- Content: at D=2 the exponent `N(D-2)/2 = 0`, so the cancellation is total, not partial. Secondary nit in the same step: the written justification skips the case where the second factor has a *pole* at some `u_0`; the conclusion still holds because `det_W(1-uT)` is a polynomial, so the pair-product must vanish at `u_0`, putting it in the named set anyway.
- Lead: "…as they do in Corollary 3, completely when D = 2 and partially when D >= 4", plus one sentence on the pole case.
- Related: L10-144.

### L10-148 The invertibility hypothesis could be relaxed to one representative per pair
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:103-107,176-179
- Raised by: Opus reviewer
- Status at last mention: noted; not adopted
- Content: "`det(1-BC) = det(1-CB)` already makes the hypothesis at one representative of each pair imply it at the other, so 'for all i' could be relaxed to 'for one i per pair' without changing anything." The "for all i" form "is if anything stronger than the proof needs".
- Lead: a free strengthening of the theorem, never applied.
- Related: L10-144.

### L10-149 The discrimination controls: deliberately-wrong variants that *do* fail
- Source: notes/reviews/theorem1-algebra-2026-09-12.md:69-98,162-163
- Raised by: Opus reviewer
- Status at last mention: done, all tests discriminating; VERDICTs thm1/cor2/cor3/cor4 all VALID
- Content: the reviewer wrote the tests from the *statement*, not the code, and added two deliberately-wrong variants — substituting `(1 - u^2 E_i E_ī)^{-1}` inside A and D, and multiplying the resolvent on the left — both of which come out **unequal**, proving the tests are ordering- and side-sensitive. Coverage gap in the author's script: D = 2 was never tested, nor singular/nilpotent/zero E, nor u outside the Neumann disc; all pass.
- Lead: adopt the discrimination-control pattern (write a knowingly-wrong variant and confirm the test catches it) for future numerical verification — several of the 2026-09-19 lanes' scripts assert only that the right thing passes.
- Related: L10-034, L10-143.

---

## Small but possibly consequential

1. **L10-041 — the two-point diagnostic `Psi(2A)`, `4Psi(A) - Psi(2A)`.** Mentioned once as a way to see the cancellation mechanism before building large Gram matrices; a two-line test any proposed sum-of-squares factorization must pass, and nobody ran it.
2. **L10-082 — the PT-symmetric reading of the two-state toy.** RH becomes "the unbroken PT regime"; the PT literature has actual techniques for proving unbrokenness, and this connection was raised in one sentence and dropped.
3. **L10-131 — Arveson's "units" of a dynamical semigroup.** A whole structural theory of no-event semigroups (product systems) sits behind a single quoted line and has never been looked at in this repo.
4. **L10-123 — the discrete arithmetic Witten Lindbladian with `ν_n ∝ n^{−β/2}`.** Cheap, has a zeta-flavoured pole at β=1, and would definitively close off the single-jump purified-Gibbs family; predicted negative, never run.
5. **L10-125 — the 3x3 non-normal toy testing whether a weighted-norm decay bound equals a sectoral Lyapunov criterion.** This is exactly the question behind L10-006 and L10-068 and could be settled in an afternoon.
6. **L10-050 — Schur complements as "the energy of the next output amplitude".** A physical reading of the sought arithmetic recurrence, stated once; it says what a positivity proof would *mean* physically and might suggest where the sign comes from.
7. **L10-136 — the WF NIPS 2009 supplementary material.** One unfetched document decides whether a repo priority claim is repaired or whether the bouquet case is genuinely new work.
8. **L10-148 — relaxing Theorem 1's hypothesis to one representative per pair.** A free strengthening, noted by the reviewer and never applied.

---

## Dead routes recorded

- **Sum of independent positive prime-power blocks for the Suzuki kernel.** Each prime-power contribution is indefinite at its first visibility on a symmetric interval — `positivity-products.md:24-32`, restated `SYNTHESIS.md:35` and `positivity-products.md:75`.
- **Naive Hadamard finite-part renormalization of the cusp Haar pairing.** Subtracting the whole constant-term divergence leaves the zero matrix — `cusp-bridge.md:26-30,56,121`.
- **Making the centered cusp flow unitary in the normalized cusp Gram.** Impossible for N >= 2 even if every pole satisfies RH, since `(A+3/4)*K + K(A+3/4) = (1/2)K - 11*` has a rank-N term against a rank-one term — `cusp-bridge.md:44-52`.
- **Demanding centered unitarity / equal survival norm for every superposition in the physical norm.** Uniform widths with one rank-one exit force nonnormality — `cusp-bridge.md:92,124`, `riemann-vs-selberg-operators.md:66,146`, `riemann-vs-selberg-cmps.md:130`.
- **Adding dissipative bistochastic prime noise to a parity jump that already spends the whole rate budget, on the *full* odd block in the HS metric.** Forces all jumps scalar and the dissipator zero — `graded-channels.md:29-41`; budget arithmetic at `graded-channels.md:59`.
- **"RH because odd relaxation is an extremal expander rate" (an odd-sector Alon–Boppana floor).** No universal floor exists; `E = (Ad I + Ad P)/2` kills the odd block — `graded-channels.md:21`.
- **Imposing full Weyl covariance on the BC generator cone.** Collapses to pure depolarization and kills the oscillations — `graded-channels.md:43,140`, citing `04d_bc_symmetry_generators.tex:143-157`. Conversely, full Weil/Galois/parity covariance plus a unique tracial stationary density still permits *unequal* odd rates — `04d:161-182`.
- **Any fixed finite-dimensional, time-homogeneous, bounded-generator cMPS amplitude model claiming to reproduce the exact Suzuki covariance.** Such a model is real-analytic on the diagonal; the true kernel has prime kinks `Psi'(a+) - Psi'(a-) = -log(p)/sqrt(p^k)` — `positivity-products.md:144-152`.
- **Ordinary tensor powers as Deligne-style amplification.** They give `epsilon_k = kc` and recover nothing — `positivity-products.md:52`; ordinary graph transfer powers leave the interesting spectrum as poles — `positivity-products.md:15`.
- **Rosati/Frobenius-moduli positivity as an independent RH proof for the constructed odd transfer.** The moduli are already an input — `positivity-products.md:17`.
- **Re-proving `Psi(t) >= 0` as if it were new.** Suzuki already has `Psi >= 0 ⇔ RH` and `Psi = O(1) ⇔ RH` — `positivity-products.md:38`.
- **Hoping the Selberg `mu >= 1/4` gap will settle the Riemann sector.** `mu = 3/16 + gamma^2/4 + i gamma/4` is nonreal even under RH, and the Eisenstein Laurent data are outside L2 — `SYNTHESIS.md:24-28`, `riemann-vs-selberg-operators.md:18`, `riemann-vs-selberg-cmps.md:18`.
- **Deriving RH from generic cMPS/passivity/one-channel/FE properties.** The two-state toy with `g=1/2` satisfies all of them and has two distinct widths for `0 < w < 1/4` — `riemann-vs-selberg-operators.md:102-114`.
- **Inferring uniform decay from the reflection symmetry alone.** Weak drive `a=c=1/20, b=0, d=1/2` keeps the reflection and has widths ~0.0060754 / ~0.4939246, discriminant `-2399/10000` — `riemann-vs-selberg-cmps.md:92,114`.
- **Assuming parity/CAR/CP/faithful stationarity give a common width.** `bd = 0` is necessary and is not implied by any of them; `b = 1/100` splits the widths exactly — `riemann-vs-selberg-cmps.md:43-56`.
- **Assuming grading alone protects observable mode selection.** Adding `0.01 P` (a quartic fermion interaction) keeps grading, CAR, CP and the stationary state but makes the output denominator degree eight — `riemann-vs-selberg-cmps.md:54,114`; same toy in `graded-channels.md`.
- **Importing `dom(A_c) = dom(L) ∩ K` from Uetake p.110.** A compressed half-line translation generator allows nonzero boundary traces — `riemann-vs-selberg-operators.md:80`.
- **Treating `S(tau)` and the raw Eisenstein coefficient `phi` as the same symbol.** They differ by `(2i tau - 1)/(2i tau + 1)`, and Uetake's original LP matrix has yet another factor plus an extra pole at `p = -1/2` — `SYNTHESIS.md:73`, `riemann-vs-selberg-operators.md:74-78`.
- **The old Hardy kernel formula in shard 04 and `notes/riemann-channel-note.md`.** `Z(t)* k_lambda = exp(-it conj(lambda)) k_lambda` gives growth `exp(+beta t/2)`, not decay — `cusp-bridge.md:64,76`, `riemann-vs-selberg-operators.md:20`.
- **A worst-case trace-distance mixing-time form of RH for the Riemann/absorbing-vacuum channel.** `||Z_t|| = 1` for every t independently of RH, so the mixing time is infinite and no bounded-invertible Lyapunov certificate exists on all of `K_S` — `2609.12284-reading.md:153-167` (marked unreviewed; a second reader is requested at :196-198).
- **A SUSY/Witten-index graded splitting as a ring-norm mechanism.** The supertrace cancels the entire nonzero spectrum (`tr e^{-tH/2h} - tr e^{-t aa*/2h} = 1`); a trace formula needs the opposite — `2609.13121-reading.md:124-129`.
- **A single-jump "purified Gibbs" / Witten Lindbladian carrying the zeros.** Its coherence rates are the spectrum of a self-adjoint `H >= 0`, hence real, with no oscillation — `2609.13121-reading.md:136-143`; predicted negative again for the discrete version at :162-165.
- **Mining the Lindblad-mixing literature for expanders / Ramanujan / cutoff content.** Neither paper contains any — `2609.12284-reading.md:183-185,214-215`, `2609.13121-reading.md:147-148,173-174`.
- **A biased diagonal BC cutoff state with a scalar measure-and-prepare reset.** The reset numerator has determinant `-(1-2p)^2`, so only the uniform target works — `cmps-renewal-bridge.md:57`.
- **A stable graded bond with a single homogeneous rank-one exit.** One parity sector is forced to evolve unitarily — `cmps-renewal-bridge.md:43-47`, cross-confirmed `graded-channels.md:152`.
- **Assuming a finite positive invariant metric survives a regulator limit.** `C_n = [[2-1/n, 1],[-1,0]]` has positive `G_n` with `lambda_min(G_n) = 1/(2n) -> 0`, and the limit admits none — `graded-channels.md:146`; compare the `1/p` prime-jump cutoff mass loss at `04g_phase_side_lindbladian.tex:121-135`.
- **"Theorem 1 is the one-vertex case of Watanabe–Fukumizu's corollary."** A bouquet is not a WF graph; their own scalar Ihara–Bass specialisation is *false* on a bouquet — `provenance-2026-09-12.md:140-167,328,355-360`.
- **"Artin–Ihara L-function for a representation of *any* group" (prior-art gloss).** The source says finite groups, extended to `U(N_c)` — `provenance-2026-09-12.md:286-290,334`.
