# Lane L06: graded Ramanujan and Selberg letters campaigns

## Coverage

| file | lines | read fully? | ideas found |
|---|---:|---|---:|
| `notes/ramanujan-graded/astra-brief.md` | 80 | yes | 5 (L06-001, 002, 034, 036, 060) |
| `notes/ramanujan-graded/definition.md` | 410 | yes | 26 |
| `notes/ramanujan-graded/astra-proofs.md` | 1670 | yes | 23 |
| `notes/ramanujan-graded/finite/` scripts | — | not in my file list (referenced only) | — |
| `notes/selberg-letters/astra-brief.md` | 81 | yes | 3 (L06-044, 050, 061) |
| `notes/selberg-letters/draft.md` | 204 | yes | 14 |
| `notes/selberg-letters/astra-proofs.md` | 681 | yes | 22 |
| `notes/reviews/selberg-letters-2026-09-16.md` | 319 | yes | 6 |

Total entries: **71**. Several ideas recur across a draft and its prover report; those are one
entry with all source lines.

## Ideas and leads

### L06-001 TJO's quest question: is the Ramanujan property only known for ungraded bonds / antiperiodic closure?
- Source: `notes/ramanujan-graded/definition.md:3-8`; restated `notes/ramanujan-graded/astra-brief.md:1`
- Raised by: TJO
- Status at last mention: pursued, answered (the answer became shards 02h/03c/03d)
- Content: TJO asked for "the correct definition" of the Ramanujan property, "working from the MPS picture", one that "makes sense in the continuous limit", and said "My feeling is we only have quantum expanders for ungraded bond space / antiperiodic BCs. Can that be." The orchestrator's answer: the feeling is correct about the literature as it stood, because every known quantum expander (Hastings, Harrow, Weil-LPS, A2 complexes) lives on an ungraded bond where periodic and antiperiodic closures coincide and the ring zeta `1/det(1-uE)` has only poles.
- Lead: build graded examples (done: Clifford-graded Harrow channels, the Pauli qubit channel). Consequence: zeros, not just poles, become available in the transfer picture, which is what a zeta with a Riemann hypothesis needs.
- Related: L06-002, L06-003, L06-016

### L06-002 Zeros require a bond grading plus the periodic (Ramond) closure
- Source: `notes/ramanujan-graded/definition.md:20-30, 43-66`; conventions `notes/ramanujan-graded/astra-brief.md:56-61`
- Raised by: orchestrator (Claude)
- Status at last mention: registered (shards 02h, 03c; PROVED as bookkeeping, `astra-proofs.md:52-61`)
- Content: With bond `H = H_+ ⊕ H_-`, parity `P`, doubled transfer `E = Σ A_s ⊗ conj(A_s)` and `Γ = Ad(P)`, the two closures give `N_1(n) = Tr E^n` (antiperiodic) and `N_P(n) = str E^n` (periodic). The graded ring zeta is `Z_P(u) = det(1-uE_1)/det(1-uE_0)`; poles are net-even modes, zeros are net-odd modes. The divisor is `nu = m_0 - m_1`.
- Lead: state RH/FE/Ramanujan about the *divisor* of the parity-closed ring zeta, not about a spectrum. Consequence: the definition then passes verbatim to the continuum.
- Related: L06-001, L06-010, L06-015

### L06-003 Two different mechanisms for the same divisor statement: "band type" and "circle type"
- Source: `notes/ramanujan-graded/definition.md:36-41, 356-361`
- Raised by: orchestrator (Claude)
- Status at last mention: raised, the gap is still open (item 5 of the "not understood" list)
- Content: In Harrow-type examples the odd sector is Hermitian, lands in a band, and the circle only appears after the non-backtracking (Hashimoto) lift. In curve-type examples (Artin-Schreier 06b, elliptic 06h) the odd block is `sqrt q` times a unitary directly, with no lift and no Hermitian channel. What is missing is "a graded channel of *circle type* with a group-theoretic (Harrow-like) mechanism: a non-Hermitian graded channel whose odd block is `sqrt q`-unitary because of a representation, not because it was written down that way."
- Lead: find the general principle relating "Hermitian channel + non-backtracking lift" to "odd block unitary". The Ihara-Bass quadratic is that principle for graphs; the analogue for curves is the Hodge index. Consequence: the Riemann case needs the circle-type mechanism in the continuum on regular data.
- Related: L06-044, L06-052, L06-032

### L06-004 D1: graded Weil-Hodge inequality |Tr E_1^n| <= Tr E_0^n
- Source: `notes/ramanujan-graded/definition.md:67-72`; proof/correction `notes/ramanujan-graded/astra-proofs.md:72-116`
- Raised by: orchestrator (Claude); corrected by codex prover
- Status at last mention: CORRECTED (ledger L01-L02)
- Content: Both closures are sums of squares (`Tr E^n = Σ_w |Tr A_w|^2`, `str E^n = Σ_w |Tr(P A_w)|^2`), hence `Tr E_0^n >= |Tr E_1^n|` and `rho(E_1) <= rho(E_0) = rho(E)`. The draft's extra claim — that equal spectral radii force a net cancellation — is false: the single even letter `A = P = diag(1,-1)` on `C^{1|1}` has even spectrum {1,1}, odd {-1,-1}, equal radii and disjoint eigenvalue sets.
- Lead: the inequality is a consequence of norm positivity, "not the positive definiteness of a centred Weil kernel, which is a different condition" (`astra-proofs.md:110-112`). Establishing the centred/Weil-kernel positivity separately is the unfinished job.
- Related: L06-005, L06-020

### L06-005 Positive operators need not be even; the Perron mode can be averaged into the even sector
- Source: `notes/ramanujan-graded/definition.md:77` (parenthesis); `notes/ramanujan-graded/astra-proofs.md:100-103`, ledger L02 at `:1402`
- Raised by: orchestrator (Claude), corrected by codex prover
- Status at last mention: registered as a correction
- Content: The draft said the even algebra contains every positive operator; `I + X` with `P = Z` is a counterexample. What is true: if `ER = qR` with `R >= 0` then `R_0 = (R + PRP)/2 >= 0` is even, nonzero and also an eigenvector, so `rho(E_0) = q`.
- Lead: "none stated" beyond using the averaged Perron matrix when a gauge is needed.
- Related: L06-004, L06-030

### L06-006 D2: the P-mode and parity-twisted (signed) unitality
- Source: `notes/ramanujan-graded/definition.md:88-98, 101-105`; `notes/ramanujan-graded/astra-proofs.md:118-151`, ledger L28 at `:1428`
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED (with a terminology correction)
- Content: `E(P) = P Σ_s eps_s A_s A_s^*`, so `P` is an even eigenvector with eigenvalue `r` exactly when `Σ_s eps_s A_s A_s^* = r·1`. For mixed-unitary letters `r = Σ_s eps_s w_s`, the signed weight; in a representation channel it is the sign character on the walk element. The condition is signed *unitality* in the notebook's Schrödinger convention, not signed trace preservation (which would use `A_s^* A_s`).
- Lead: the P-mode is structural but *not* trivial, so Ramanujan constrains it: for unitary letters this is a *balance condition* `|w_even - w_odd| <= lambda_H`, or in adjacency units `|N_even - N_odd| <= 2 sqrt(D-1)` (`astra-proofs.md:1540-1548`). Consequence: a candidate graded expander with too many even letters is automatically non-Ramanujan.
- Related: L06-007, L06-017

### L06-007 The trivial set, and whether "1" is universally trivial
- Source: `notes/ramanujan-graded/definition.md:81-99`; corrections `notes/ramanujan-graded/astra-proofs.md:1531-1548`, ledger L31 `:1431`, L41 `:1441`
- Raised by: orchestrator (Claude), sharpened by codex prover
- Status at last mention: CORRECTED into a "signed trivial divisor with parities"
- Content: The draft listed the fixed point `q`, its period images, and the value 1 as trivial, and asserted period modes are even. Both fail: `Phi = (Ad Z + Ad Y)/2` graded by `Z` has a unique fixed state and an *odd* period mode `Phi(X) = -X`. And "1" is trivial only as the designated `H^0` partner of `q` in the projective-curve case, not whenever an eigenvalue happens to equal one.
- Lead: replace the scalar trivial *set* by a designated invariant subspace or a signed multiset with parities and multiplicities. Consequence: without it, RH statements silently exempt real modes.
- Related: L06-006, L06-020, L06-048

### L06-008 Critical circle as the geometric mean of the two reference values; correlation lengths all equal 2/omega
- Source: `notes/ramanujan-graded/definition.md:107-114`; correction `notes/ramanujan-graded/astra-proofs.md:62-70` (H-count), `:1550-1557`, ledger L36 `:1436`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED (needs *two* reference rates, not one)
- Content: The critical circle `|mu| = sqrt q` is the geometric mean of the fixed point `q` and the value 1; for a generator it is `Re z = omega/2`. "The fluctuation of the ring norm is the square root of its leading term", i.e. all correlation lengths equal `2/omega`. The prover's correction: a normalised TP generator has spectral bound zero, so the critical rate is *not* determined by the spectrum; one must supply a pair of reference rates `(a_+, a_-)` with centre `c`. Amplitude damping has even rates `0, -gamma` and odd rates `-gamma/2 ± i omega`, centre `-gamma/2`, despite spectral bound zero.
- Lead: always carry the pair of reference rates as geometric data. Consequence: a "critical line" claim is meaningless without it.
- Related: L06-002, L06-041

### L06-009 Definition of graded RH, FE, Ramanujan, and the manifest (Hilbert-Polya) form
- Source: `notes/ramanujan-graded/definition.md:116-132`; verdict table `notes/ramanujan-graded/astra-proofs.md:1474-1508`
- Raised by: orchestrator (Claude)
- Status at last mention: registered (def:graded-rh-fe-ramanujan, shard 02h), with the prover's qualifications
- Content: RH = every nontrivial divisor point has `|lambda| <= sqrt q`; FE = an even similarity `J` with `J E J^{-1} = q E^{-1}` on the support of `nu`; Ramanujan = both; manifest = a Gamma-even positive definite `G` with `E^† G E = q G` on the retained sectors. The prover proved the finite equivalences (RH + FE + reality <=> circle; manifest <=> diagonalisable with spectrum on the circle) and stressed that operator FE is strictly stronger than divisor FE (Jordan data must match, ledger L32 `:1432`).
- Lead: the manifest form is the Hilbert-Polya object; on an infinite bond it must be stated on weighted/anisotropic regular data with domain and norm-equivalence qualifications (`astra-proofs.md:1504-1508`). That analytic upgrade is unfinished.
- Related: L06-020, L06-048, L06-054

### L06-010 The odd gap is the decoherence rate of parity coherences; "RH says all parity coherences decay at exactly the critical rate"
- Source: `notes/ramanujan-graded/definition.md:165-171`; correction ledger L34 `notes/ramanujan-graded/astra-proofs.md:1434`, `:1584-1587`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED (the slogan overstates)
- Content: A graded quantum expander is `(D_+|D_-, D, lambda_0, lambda_1)` with an even-sector bound `lambda_0` and `rho(Phi_1) <= lambda_1`. The physical reading: `-log lambda_1` is the decoherence rate of the coherences between the two parity blocks. The correction: an eigenvalue bound controls asymptotic decay possibly with Jordan polynomial factors, and a one-sided divisor RH bounds only *visible* modes, so "every coherence decays at exactly the critical rate" needs full-sector control plus semisimplicity.
- Lead: a physically meaningful RH statement would be a statement about actual coherence decay, which requires the stronger full-sector, Jordan-free version. Consequence: this is the difference between a divisor statement and a dynamical statement.
- Related: L06-009, L06-055

### L06-011 D3: graded quantum Ihara-Bass, sector by sector, with the (1-u^2) exponent
- Source: `notes/ramanujan-graded/definition.md:148-156`; proof `notes/ramanujan-graded/astra-proofs.md:153-204`
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED (thm:graded-qihara-bass, shard 03c)
- Content: `det(1 - uT_k) = (1-u^2)^{n_k(D-2)/2} det(1 - u Sigma_k + (D-1)u^2)` for `k = 0, 1`, with `n_0 = D_+^2 + D_-^2`, `n_1 = 2 D_+ D_-`. Hence the trivial edge exponent of the graded zeta is `-(D-2)(D_+-D_-)^2/2`, which vanishes exactly for a balanced grading `D_+ = D_-`.
- Lead: balanced gradings (Clifford gradings always are) give a clean zeta with no leftover trivial edge factors. Consequence: this is what makes the Pauli example's zeta exactly an elliptic L-function.
- Related: L06-013, L06-016, L06-058

### L06-012 D4: band iff circle, but only for the *net* divisor — hidden modes can cancel
- Source: `notes/ramanujan-graded/definition.md:158-163`; correction `notes/ramanujan-graded/astra-proofs.md:206-274`, ledger L03 `:1403`, L08 `:1408`
- Raised by: orchestrator (Claude), corrected by codex prover
- Status at last mention: CORRECTED
- Content: Both-sector band bounds imply the divisor bound; the converse is false. Explicit primitive counterexample on `C^{1|1}`: ten copies of `I`, two of `X`, two of `Z`, `D = 14`, `b = 13`; `spec Sigma_0 = {14, 10}`, `spec Sigma_1 = {10, 6}`, and `Z_{P,T} = (1-6u+13u^2)/((1-u)(1-13u))`. The out-of-band value 10 cancels completely between sectors and is invisible in the zeta.
- Lead: a "hidden mode" hypothesis (H-nohidden: every retained adjacency class occurs in one parity sector only) is needed for the converse, and "the examples do not generally satisfy it" (`:236-238`). Consequence: any RH-from-divisor argument must be told whether it is a statement about modes or about a quotient.
- Related: L06-011, L06-055, L06-057

### L06-013 D5: graded Alon-Boppana for the odd sector — REFUTED
- Source: `notes/ramanujan-graded/definition.md:173-180`; refutation `notes/ramanujan-graded/astra-proofs.md:276-339`, ledger L05 `:1405`
- Raised by: orchestrator (Claude); refuted by codex prover
- Status at last mention: pursued, negative (REFUTED)
- Content: The draft conjectured that the odd sector cannot beat the Hastings value, `rho(Phi_1) >= lambda_H - o(1)`. False: `Phi = (1/4)(Ad I + Ad I + Ad P + Ad P)` has `Phi_1 = 0` in every dimension. A primitive degree-16 family also has `rho(Phi_1) = 0` with unbounded bond: `Depol_2 ⊗ Psi_m` with `Psi_m` the clock/shift channel on odd `m`. Reason: in the odd restriction a word contributes `2 Re(Tr U_{w,+} conj Tr U_{w,-})`, which can be negative, so Hastings' positivity step fails.
- Lead: what survives is `max{rho(Phi_0|_{I^perp}), rho(Phi_1)} >= lambda_H - O(...)`; "It does not place the large eigenvalue in a prescribed sector" (`:326-331`). Finding which structural hypothesis *does* force the odd sector to be large is an open question.
- Related: L06-012, L06-058

### L06-014 D6: Clifford theory supplies the grading — graded Harrow expanders
- Source: `notes/ramanujan-graded/definition.md:182-208`; proof/corrections `notes/ramanujan-graded/astra-proofs.md:341-489`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED and registered (thm:graded-harrow, shard 03c)
- Content: Take `G` with index-2 subgroup `G_0`, sign character `eps`, and `pi` irreducible with reducible restriction `pi|G_0 = pi_+ ⊕ pi_-`. Then `P pi(g) P = eps(g) pi(g)`: coset parity grades the letters. The even sector is `pi_+ ⊗ conj pi_+ ⊕ pi_- ⊗ conj pi_-`, the odd sector `pi_+ ⊗ conj pi_- ⊕ c.c.`. Trivial and sign representations each occur once, both even (spanned by `I` and `P`). Harrow's transfer then bounds every other constituent by the Cayley second eigenvalue, sector by sector.
- Lead: this is the notebook's recipe for manufacturing graded quantum expanders in quantity. Consequence: graded expanders are abundant, answering TJO's question affirmatively.
- Related: L06-001, L06-015, L06-016, L06-018

### L06-015 Artin factorisation of the graded quantum Ihara zeta into L-functions of constituents
- Source: `notes/ramanujan-graded/definition.md:204-208`; proof `notes/ramanujan-graded/astra-proofs.md:434-441`, ledger L37 `:1437`
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED with a correction
- Content: `Z_{P,T}(u) = prod_{sigma in Ghat} det(I - u T_sigma)^{a_{1,sigma} - a_{0,sigma}}`, with an Euler product `L_sigma(u) = prod_{[c]} det(I - u^{l(c)} sigma(c))^{-1}` over primitive cyclically reduced bouquet words. The correction (L37): `T_sigma` is built from the *individual* representation letters `sigma(s)` and the reversal, not from the single averaged matrix `sigma(W)`.
- Lead: "the L-functions of the graded expander are the sigma-factors, with zeros for odd-sector constituents and poles for even-sector ones". Consequence: a dictionary between representation constituents and zeta factors — the closest thing in the notebook to an Artin formalism on the channel side.
- Related: L06-014, L06-016

### L06-016 The qubit Pauli channel is an elliptic curve over F_5
- Source: `notes/ramanujan-graded/definition.md:223-229`; exact proof `notes/ramanujan-graded/astra-proofs.md:1316-1328`; reverified `notes/selberg-letters/astra-proofs.md:488-493`; independently recomputed by the reviewer `notes/reviews/selberg-letters-2026-09-16.md:42-44`
- Raised by: orchestrator (Claude)
- Status at last mention: registered (prop:qubit-graded-zeta, shard 03c), exactly verified three times
- Content: Letters `X,X,Y,Y,Z,Z` on a qubit with `P = Z`, `D = 6`, `q = 5`. Even spectrum `{6, -2}`, odd `{-2,-2}`, graded quantum Ihara zeta `(1 + 2u + 5u^2)/((1-u)(1-5u))`, ring norms `8, 32, 104, 640, 3208, 15392 = 1 + 5^n - (mu^n + conj mu^n)` with `mu = -1+2i`. These are the point counts of `y^2 = x^3 + 4x + b` over `F_5`. Word reading: `str T^n = 4 × #{cyclically non-backtracking Pauli words of length n with product proportional to Z}`.
- Lead: the smallest graded quantum expander is literally an elliptic curve. Correction (L09 `:1409`): the qubit is a *projective* representation of `Z_2 × Z_2`; use the actual Pauli group for ordinary Clifford theory.
- Related: L06-014, L06-017, L06-058

### L06-017 D13: the general C^{1|1} graded channel and the question "is the numerator always a Weil polynomial?"
- Source: `notes/ramanujan-graded/definition.md:381-391`; answer `notes/ramanujan-graded/astra-proofs.md:1246-1354`, ledger L26-L27 `:1426-1427`
- Raised by: orchestrator (Claude); answered negatively by codex prover
- Status at last mention: CORRECTED; the Weil/curve question answered NO twice
- Content: For `D` inverse-paired homogeneous unitary letters on `C^{1|1}`, with `r = N_even - N_odd`, `alpha = Σ_even a_i conj d_i` (real), `beta = Σ_odd a_i conj d_i`, one gets `spec Sigma_0 = {D, r}`, `Sigma_1 = [[alpha, beta],[conj beta, alpha]]`, `lambda_± = alpha ± |beta|`, and `Z_{P,T}(u) = f_{lambda_+} f_{lambda_-}/[(1-u)(1-bu) f_r]`. The numerator need not be integral (`U = diag((1+2√2 i)/3, 1)` gives `N_P(1) = 16/3`), and even an integral Weil numerator need not be a curve: six `I`'s, two `X`'s, two `Y`'s give `(1-3u)^4` over `F_9`, which would force `-2` rational points.
- Lead: "Weil" is an arithmetic condition on all algebraic conjugates; a curve interpretation needs far more than the circle bound. Consequence: the "channels are curves" slogan must be restricted to arithmetically special letter sets — finding the right restriction is open.
- Related: L06-016, L06-058

### L06-018 LPS bipartite graded example; the extremal Hecke eigenvalue can live in the odd sector
- Source: `notes/ramanujan-graded/definition.md:210-221`; audit `notes/ramanujan-graded/astra-proofs.md:451-489`, ledger L06-L07 `:1406-1407`
- Raised by: orchestrator (Claude); numerics corrected by codex prover
- Status at last mention: CORRECTED
- Content: `G = PGL_2(F_p)`, `G_0 = PSL_2(F_p)`, `pi` the order-4-character principal series, `S` the LPS quaternions in the odd coset: all letters odd, Cayley graph bipartite. Numerics at `(p;q) = (5;13)` and `(13;5)`. In the `(13;5)` case "the extremal Hecke eigenvalue 4.2497 lives in the *odd* sector". Corrections: the numerator degrees 36/196 were raw odd counts; reduced degrees are 4/4 and 144/144, and the `(13;5)` case retains a nontrivial denominator of degree 140, so it is not a curve denominator. All-odd letters give period two, not a mixing expander.
- Lead: for `(5;13)` the audit identifies the candidate reduced formula `f_4(u) f_{-4}(u) / (f_{14}(u) f_{-14}(u))` with `b = 13` (`:471-472`) — a small explicit object nobody followed up. Consequence: a concrete graded L-function to identify arithmetically.
- Related: L06-014, L06-015, L06-012

### L06-019 D7: exactness of the continuum limit, and the aliasing counterexample
- Source: `notes/ramanujan-graded/definition.md:233-236`; correction `notes/ramanujan-graded/astra-proofs.md:491-551`, ledger L10 `:1410`
- Raised by: orchestrator (Claude); corrected by codex prover
- Status at last mention: CORRECTED
- Content: For a graded cMPS generator `T`, `E_h = e^{hT}` has `N_P^{(h)}(n) = N_P(nh)`, so RH/FE/Ramanujan should be mesh-independent. The correction: sampling pushes forward signed multiplicities and can *cancel* aliases. Explicit CP example: `Q = (1/2)I - i diag(0, 2π)`, no jumps, `P = Z`; even rates `1,1`, odd rates `1 ± 2πi`; at `h = 1`, `E_h = e·I_4` and the entire sampled divisor cancels, `Z_{P,E_h} = 1`, while the continuous odd rates violate the critical bound.
- Lead: carry H-noalias (injectivity of `exp` on the compared rates, true for all small `h`). Consequence: a lattice check of a continuum RH can be vacuously true.
- Related: L06-021, L06-045

### L06-020 D8: odd letters must be jumps — "fermionic zeros are relaxation modes"
- Source: `notes/ramanujan-graded/definition.md:238-248`; correction `notes/ramanujan-graded/astra-proofs.md:553-654`, ledger L11-L12 `:1411-1412`, L38 `:1438`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED (prop:graded-chernoff, shard 03d)
- Content: An odd letter cannot be `O(1)`-close to the identity (`P A P = -A` forces `||A - I|| >= 1`), so it enters a continuum limit as `sqrt(h) R` with `R` an odd jump of finite rate, never as a drift. Hence in the continuum, parity-changing dynamics is *dissipative*: "fermionic zeros are relaxation modes and there is no Hamiltonian odd letter". Corrections: the theorem is on a *fixed finite* bond in operator norm; the bound is collective, `Σ_{a odd} ||A_a(h)||_HS^2 = O(h)`, not a per-letter limit.
- Lead: this is the stated reason `obs:jump-operator-guidance` needed an even-odd *Hamiltonian on the doubled bond* (on the coherences) rather than an odd letter. Consequence: it constrains any Riemann Lindbladian construction to put the grading in the coherences.
- Related: L06-021, L06-046, L06-049

### L06-021 An even Hamiltonian can still give odd coherences arbitrary frequencies; a net zeta need not see every relaxation mode
- Source: `notes/ramanujan-graded/astra-proofs.md:645-650`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "Under parity covariance there is no parity-changing Hamiltonian term on the bond in this presentation. An **even** Hamiltonian can nevertheless give arbitrary oscillation frequencies to odd coherences. Parity-changing population transitions come from noise; zeros of a net zeta need not detect every one of those relaxation modes."
- Lead: this reopens a route D8 appeared to close — the imaginary parts of the zeros can come from an even Hamiltonian acting on the coherences, while the real part `1/2` comes from the odd jump rates. Consequence: a concrete design principle for a Riemann Lindbladian.
- Related: L06-020, L06-049

### L06-022 D9: jump Lindbladians — the Ramanujan band is affine
- Source: `notes/ramanujan-graded/definition.md:250-255`; proof `notes/ramanujan-graded/astra-proofs.md:656-702`
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED
- Content: For `T = Σ_i g_i (Ad U_i - 1)`, `e^{tT} = e^{-G t} e^{G t Phi}` and `spec T_k = G(spec Phi_k - 1)`, so a sector Hastings band becomes the interval `[-G(1+lambda_H), -G(1-lambda_H)]`. For the Pauli jump Lindbladian the even rates are `0, -2(g_X + g_Y)` and the odd rates `-2(g_Y + g_Z), -2(g_X + g_Z)`; the P-mode rate is twice the total odd-letter rate.
- Lead: the prover notes this is "an interval of diffusion rates, not an assertion that they all have the same real part" (`:674-675`) — i.e. a Poissonised jump Lindbladian is exactly the wrong shape for a critical *line*. Consequence: the critical line must come from a drift, which is what the Selberg campaign later concluded independently (L06-049).
- Related: L06-020, L06-049

### L06-023 D10: the divisor when there is no trace — relative resonance divisor via Riesz projections
- Source: `notes/ramanujan-graded/definition.md:257-267`; `notes/ramanujan-graded/astra-brief.md:50-53`; construction `notes/ramanujan-graded/astra-proofs.md:704-809`, ledger L13-L14 `:1413-1414`
- Raised by: orchestrator (Claude); made precise by codex prover
- Status at last mention: CORRECTED and registered (obs:divisor-regular-data, shard 03d)
- Content: For an infinite graded bond, define the divisor not as the `L^2` spectrum but from correlation functions of regular data. The prover's replacement: fix a graded Banach realisation `B`, assume analytic Fredholm continuation of the resolvent, and set `m_k(lambda) = rank(Pi_lambda|_{B_k})` from the Riesz projection, `nu = m_0 - m_1`. Scalar pole *order* is not multiplicity. Hypotheses: H-C0, H-regular, H-Fredholm, H-detect, H-trace-dist.
- Lead: the motivation is the `||Z(t)|| = 1` negative of 2026-09-14 — no statement on `K_S` can see the rate `1/4`, but the divisor of regular-data correlations can. "The manifest form must then be stated on a weighted or anisotropic space of regular data, exactly as resonances are for Anosov flows."
- Related: L06-024, L06-025, L06-054

### L06-024 Invariance of the resonance divisor under a change of regular realisation is not proved
- Source: `notes/ramanujan-graded/astra-proofs.md:766-769`
- Raised by: codex prover
- Status at last mention: raised, not pursued (flagged as missing)
- Content: "Analytic continuation is unique on the fixed connected domain. Thus the divisor is well defined for these specified data. Its invariance under a change of regular realization needs a further compatibility theorem; calling both spaces 'regular' supplies no such theorem."
- Lead: prove the compatibility theorem, or accept that the divisor is data-dependent. Consequence: without it the Phantasm's divisor is not an invariant of the semigroup, which would undermine any RH statement made about it.
- Related: L06-023, L06-054

### L06-025 There is no canonical signed *measure* for continuous spectrum without extra traces (H-spectral-trace)
- Source: `notes/ramanujan-graded/astra-proofs.md:780-795`, ledger L14 `:1414`
- Raised by: codex prover
- Status at last mention: raised as a required hypothesis; not pursued
- Content: The draft wanted `nu` to become a signed measure when the spectrum is continuous. For a general non-normal generator there is no scalar signed measure. One must specify positive traces/weights `tau_k` on the sector spectral algebras with local finiteness and exponential integrability; then `nu(A) = tau_0(P_0(A)) - tau_1(P_1(A))` avoids `∞ - ∞`. Also: "A Cauchy transform of a continuous measure is also generally not meromorphic across its support."
- Lead: supply such traces for the Riemann/Selberg cases, or use sector supports rather than an invented scalar continuous divisor.
- Related: L06-023, L06-024

### L06-026 D11: Harrow's continuum limit is exactly temperedness
- Source: `notes/ramanujan-graded/definition.md:269-289`; corrected `notes/ramanujan-graded/astra-proofs.md:811-1024`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED and registered (obs:graded-continuous-harrow, shard 03d)
- Content: For `pi` tempered, Fell absorption gives `pi ⊗ conj pi < lambda`, so `spec(-T_*)` on the K-invariant sector is `⊆ [1/2, ∞)`: the gap `1/2` is the tempered threshold, the continuous Ramanujan value. The prover proved the converse for `PSL_2(R)`: the type-zero bound `-T_* >= 1/2` is *equivalent* to temperedness. Sharpness holds for every discrete series `D_k^±` via the mixed tensor decomposition.
- Lead: "Ramanujan = temperedness of `pi ⊗ conj pi`", with flow entropy `omega = 1` and critical rate `1/2`; discrete zeros appear only after passing to a lattice quotient, where the constituents become Maass forms.
- Related: L06-027, L06-028, L06-029

### L06-027 Normalisation correction: the equally averaged Lie walk has threshold 1/(2d), not 1/2
- Source: `notes/ramanujan-graded/astra-proofs.md:829-838`, ledger L15 `:1415`
- Raised by: codex prover
- Status at last mention: CORRECTED
- Content: For `Phi_h = (1/2d) Σ_j (e^{√h B_j} + e^{-√h B_j})`, `T_walk = (1/2d) Σ_j B_j^2 = T_*/d` in the two-generator case, so the threshold is `1/(2d) = 1/4`, not `1/2`. To get `T_*` use steps `exp(±√(dh) X_j)` or speed up time by `d`. On a constituent with Casimir `-s(1-s)` and K-type `m`, the exact rate is `-T_* = 2s(1-s) + m^2/2` (confirming the brief's guess at `astra-brief.md:44-45`).
- Lead: none stated; but note that the *uncorrected* threshold `1/4` is numerically the Riemann rate, which is a coincidence worth not being fooled by.
- Related: L06-026

### L06-028 The Repka threshold s = 3/4 and Selberg's 3/16: "Is that a coincidence?"
- Source: `notes/ramanujan-graded/definition.md:290-293`; brief request `notes/ramanujan-graded/astra-brief.md:46-48`; answer `notes/ramanujan-graded/astra-proofs.md:911-928, 1001-1011`
- Raised by: TJO-style question posed by the orchestrator; answered by codex prover
- Status at last mention: partially explored — explained, not resolved
- Content: H-repka (Repka 1978, AJM 100, 747-774, DOI 10.2307/2373909): for the complementary series `pi_s`, `1/2 < s < 1`, the tensor square contains a complementary constituent iff `s > 3/4`, and then only `pi_{2s-1}` with multiplicity one. So the quantum Lindbladian of `pi_s` is Ramanujan for `1/2 < s <= 3/4` although `pi_s` itself is not tempered. The prover's explanation: for `s > 3/4` the complementary constituent's rate is `4(2s-1)(1-s) < 1/2` and its slow geodesic exponent is `-2(1-s)`; the boundary `2(1-s) = 1/2` is exactly `s = 3/4`, whose Laplace value `s(1-s) = 3/16`. "This explains the arithmetic coincidence of parameters; it is not a proof of Selberg's automorphic 3/16 theorem."
- Lead: the geodesic-exponent boundary condition `2(1-s) = 1/2` is the mechanism; whether it can be pushed to give anything about the automorphic `3/16` is untouched.
- Related: L06-026, L06-053

### L06-029 The Repka citation was deliberately left unverified in text
- Source: `notes/ramanujan-graded/astra-proofs.md:917-928`
- Raised by: codex prover
- Status at last mention: flagged, unverified
- Content: "The 1978 article was not available for direct text inspection in this session; no theorem number is invented." The existence direction is cross-checked against Zhang arXiv:1402.2950 Theorem 4.1 with `alpha = beta = 1-s`, `rho = 1/2`.
- Lead: fetch Repka 1978 and byte-verify, as the Selberg lane later did for Booker-Lee-Strömbergsson (L06-069).
- Related: L06-028

### L06-030 D12: graded continuous Harrow for PGL_2(R) — the reflection grading
- Source: `notes/ramanujan-graded/definition.md:295-323`; corrected `notes/ramanujan-graded/astra-proofs.md:1026-1244`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED
- Content: `pi = Ind_{PSL_2}^{PGL_2} D_k^+` with `P = I ⊕ (-I)` and `T = kappa T_* + gamma(R - I)`, `R = Ad pi(r)` the reflection jump. Even sector: two copies of `D_k^+ ⊗̂ D_k^-`, purely principal (rates `kappa(1/2 + 2r^2)` and that `+ 2 gamma`). Odd sector: `⊕_{l>=0} (D_{2k+2l}^+ ⊕ D_{2k+2l}^-)`, purely discrete series, rates `kappa(n + 2nj + 2j^2)` (the draft's "ladder n/2" was wrong, L20 `:1420`), minimum `2 kappa k`. Even `k >= 2` is required for genuine PGL representations (L19 `:1419`).
- Lead: the reflection grading puts the critical continuum in the *even* sector and the archimedean ladder in the odd sector — "the opposite of the Riemann assignment (zeros odd)".
- Related: L06-031, L06-032, L06-033

### L06-031 The odd archimedean ladder matches the Gamma-factor pole list — positionally only
- Source: `notes/ramanujan-graded/definition.md:313-323`; correction `notes/ramanujan-graded/astra-proofs.md:1167-1186`, ledger L24 `:1424`
- Raised by: orchestrator (Claude); qualified by codex prover
- Status at last mention: CORRECTED, partially explored
- Content: For `k = 1`, `D_1 ⊗ D_1 = ⊕ D_{2+2m}` gives exponents `-(1+m)`, the `Gamma_C` ladder; `Sym^2 D_1 = ⊕_{j} D_{2k+4j}` and `Lambda^2 D_1 = ⊕_j D_{2k+2+4j}` give exponent lists `-(k+2j)` and `-(k+1+2j)`, matching the pole lists of `Gamma((z+1)/2)` and `Gamma((z+2)/2)`, whose product has the pole list of `Gamma(z+1)`. Prover: "This is a statement about lists of lowest exponents... Neither determinant is proved to be one of those Gamma functions."
- Lead: prove (or disprove) that the odd heat/flow determinant of this construction *is* a Gamma factor, accounting for the quadratic rates `n + 2nj + 2j^2`, the descendants, multiplicities, and the missing zero rung. Consequence: that would supply the archimedean factor of the Phantasm from representation theory.
- Related: L06-030, L06-052

### L06-032 Which grading is the Phantasm's: PGL_2 (zeros even) or transverse form degree (zeros odd)?
- Source: `notes/ramanujan-graded/definition.md:325-338, 365-366`; prover's verdict `notes/ramanujan-graded/astra-proofs.md:1227-1240`, ledger L40 `:1440`; resolved in the Selberg lane `notes/selberg-letters/astra-proofs.md:11, 519, 591`
- Raised by: orchestrator (Claude)
- Status at last mention: superseded by L06-045 (the two-term stable transverse complex)
- Content: The section argues the Phantasm needs the *form-degree* grading of the geodesic flow, following Dyatlov-Zworski's alternating product over `k` of the flat-trace zeta on `k`-forms, with Selberg as the fermionic (odd-degree) factor. The prover: the two gradings are genuinely different (holomorphic/antiholomorphic versus stable/unstable transverse degree), and "the alternating flat determinants carry the orientation sign".
- Lead: settled a session later — the full exterior algebra gives Ruelle, and the *two-term stable* transverse complex gives Selberg.
- Related: L06-030, L06-045, L06-064

### L06-033 Untested statement: the K-type grading m = 0 vs m = ±2 as the continuous analogue of the parity-jump uniform shift
- Source: `notes/ramanujan-graded/definition.md:334-338` ("Not drafted as a claim"); refuted later at `notes/ramanujan-graded/astra-proofs.md:1236-1240` and `notes/selberg-letters/astra-proofs.md:498-542`
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, negative
- Content: The proposal: on the doubled bond of a `PSL_2(R)` representation channel, the form-degree grading is the K-type grading `m = 0` (functions) versus `m = ±2` (1-forms), and the uniform shift `m^2/2 = 2` is the continuous analogue of `prop:parity-jump-uniform-shift`. The first prover: "selecting K-types 0, ±2 alone does not define an invariant splitting under all of G or an Ad(P) grading". The Selberg prover then showed `P_K` makes `X` odd, so it is not even a grading for the flow.
- Lead: dead as stated; see L06-064 for what survives.
- Related: L06-032, L06-064

### L06-034 D14: the two elementary obstructions behind TJO's question
- Source: `notes/ramanujan-graded/definition.md:393-394`; `notes/ramanujan-graded/astra-brief.md:49`; proof `notes/ramanujan-graded/astra-proofs.md:1356-1391`, ledger L29 `:1429`
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED
- Content: (i) An ungraded finite transfer has ring zeta `det(I - uE)^{-1}`, a reciprocal polynomial with no finite zeros. (ii) A finite CPTP channel on `H_+ ⊕ H_-` with all Kraus letters even has at least two stationary states (one per block), hence cannot be a unique-state graded expander. Correction L29: "no positive odd operator" does *not* imply "no odd fixed operator" (the identity channel fixes every coherence); the uniqueness of the fixed state is what rules it out.
- Lead: none stated; this is the formal answer to "can that be".
- Related: L06-001

### L06-035 Distinguish a graded CP transfer from a graded spectral transfer
- Source: `notes/ramanujan-graded/astra-proofs.md:1447-1453`, ledger L35 `:1435`; adopted `notes/selberg-letters/draft.md:56-58`, `notes/selberg-letters/astra-proofs.md:301, 610`
- Raised by: codex prover
- Status at last mention: registered as a vocabulary change and used throughout the Selberg campaign
- Content: A **graded CP transfer** `(H, P, E)` has an actual Kraus realisation `E = Σ A_i ⊗ conj A_i` with `Gamma = Ad(P)` and nonnegative ring norms. A **graded spectral transfer** `(V, Gamma, M)` is just a graded operator with a divisor. The notebook's Artin-Schreier (06b), Riemann (04b) and flat-trace constructions are spectral, not CP.
- Lead: "Admit the larger graded spectral category, or supply a separate CP realization." This is the single largest outstanding realisation problem in both campaigns.
- Related: L06-003, L06-044, L06-047, L06-057

### L06-036 Which of the notebook's cases actually satisfy the definition — the verdict table and its "minimal change" column
- Source: `notes/ramanujan-graded/astra-brief.md:29-34`; `notes/ramanujan-graded/astra-proofs.md:1600-1611`
- Raised by: orchestrator (brief), answered by codex prover
- Status at last mention: registered as the status table (obs:graded-ramanujan-status)
- Content: A case-by-case verdict with a required minimal change for each: regular Ramanujan graphs (distinguish degree `D` from edge growth `D-1`; endpoint Jordan qualification); Weil-LPS channels of 05 (its zeta has poles and **no zeros** — "The last paragraph of 05 calling these 'nontrivial zeros' should say poles"); the full Weil representation graded by even/odd functions (two stationary states, not a unique-state graded expander); the D6 induced PGL examples ("period-two graded expander", no curve denominator); the Pauli example (keep direct-transfer and non-backtracking zetas separate; the direct adjacency transfer has `Z_P(u) = (1+2u)/(1-6u)`, whose zero at `-2` is **not** on `|mu| = sqrt 6`); 06h projective (no correction needed); 06h affine (singular transfer, no full inverse FE; impose FE on the retained divisor or pass to the projective completion); Artin-Schreier (spectral only); Riemann graded generator (see L06-054); Selberg flat tower (see L06-055).
- Lead: each row is a concrete repair task; several were never done.
- Related: L06-035, L06-054, L06-055

### L06-037 The Weil-LPS channels of shard 05 have poles, not zeros — a mislabelling to fix
- Source: `notes/ramanujan-graded/astra-proofs.md:1603`
- Raised by: codex prover
- Status at last mention: raised as a required repair; unclear whether applied
- Content: "The direct channel is of real band type. Its ungraded Ihara zeta has poles on the circle, and **no zeros**. ... The last paragraph of 05 calling these 'nontrivial zeros' should say poles."
- Lead: fix shard 05's wording. Consequence: an ungraded expander cannot supply zeros at all (L06-034), so the earlier reading of 05 was structurally impossible.
- Related: L06-034, L06-036

### L06-038 The full Weil representation graded by even/odd functions is not a unique-state graded expander
- Source: `notes/ramanujan-graded/astra-proofs.md:1604`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: All letters preserve the two inequivalent Weil blocks, so there are at least two stationary states. The block-channel results prove nothing about the cross-transfer coherences.
- Lead: "Work on the irreducible ungraded blocks, or establish a new full-bond sector theorem with its actual trivial multiplicities." The second option — a genuine bound on the Weil cross-coherences — is unexplored and would give a graded expander with an arithmetic pedigree.
- Related: L06-036, L06-014

### L06-039 A dimension obstruction to realising a cohomological grading on a doubled bond
- Source: `notes/ramanujan-graded/astra-proofs.md:1621-1625`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "every such bond has `n_0 - n_1 = (D_+ - D_-)^2 >= 0`, while its formal cohomological grading can have more odd than even dimensions."
- Lead: a hard parity-dimension obstruction to turning a cohomological (Weil/Selberg) grading into a doubled Kraus bond. Any proposed CP realisation must either have more even than odd dimensions or use an infinite bond where the counting fails. Consequence: this may be the real reason no CP realisation of the Artin-Schreier/Riemann transfers has been found.
- Related: L06-035, L06-047

### L06-040 H-leading: the ring norm does not automatically grow like q^n
- Source: `notes/ramanujan-graded/astra-proofs.md:1512-1520`
- Raised by: codex prover
- Status at last mention: registered as a required hypothesis
- Content: `rho(E) = rho(E_0)` does not prove `nu(q) = 1` or `N_P(n) ~ q^n`. Equal even and odd copies of the identity give zero supertrace at every length; periodic examples can vanish at every odd length. One must assume a simple retained even Perron mode with no odd mode at `q`.
- Lead: check H-leading in each example before quoting a growth rate.
- Related: L06-007, L06-008

### L06-041 Perron gauges: rescaling the letters by sqrt q does not make the fixed point the identity
- Source: `notes/ramanujan-graded/astra-proofs.md:1522-1529`, ledger L30 `:1430`
- Raised by: codex prover
- Status at last mention: CORRECTED
- Content: If `ER = qR` with `R > 0`, conjugating letters by `R^{-1/2}` and dividing by `sqrt q` yields a unital transfer; if `E^*(L) = qL` with `L > 0`, the letters `q^{-1/2} L^{1/2} A_i L^{-1/2}` are TP. The Perron matrices can be chosen even by averaging *when faithful*; a singular Perron matrix supplies no whole-bond gauge.
- Lead: none stated; a bookkeeping rule.
- Related: L06-005, L06-040

### L06-042 The letter degree is data, not a property of the channel
- Source: `notes/ramanujan-graded/astra-proofs.md:1589-1591`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "The letter degree is data: redundant copies change the Hastings benchmark even if normalized copies implement the same channel. There is no unique degree attached to a channel unless a Kraus/word convention is retained."
- Lead: this makes "Ramanujan" a property of a *presentation*, not of a channel. Whether there is a presentation-independent formulation (an infimum over Kraus/word conventions?) is unasked.
- Related: L06-010, L06-016

### L06-043 A Jordan block at the band endpoint blocks the manifest form
- Source: `notes/ramanujan-graded/astra-proofs.md:268-270`, ledger L33 `:1433`; finite version `notes/selberg-letters/astra-proofs.md:435, 486, 494`; continuum version `notes/selberg-letters/astra-proofs.md:226`
- Raised by: codex prover (both lanes)
- Status at last mention: registered (a sharp iff in the finite case)
- Content: At a band endpoint `a = ±2 sqrt q` the Hashimoto companion matrix has a genuine size-two Jordan block, so a positive invariant metric on the full algebraic band exists iff the band bound is **strict**. Exact counterexamples: the 5-regular graph `K_3 □ Q_3` (Ramanujan, endpoint `-4` of multiplicity two, Hashimoto nullities 2 and 4 at `-2`); and a ten-letter Pauli channel (`I×4, X×4, Z×2`, `D=10, q=9`, odd adjacency `{6,-2}`, odd Hashimoto eigenvalue 3 with nullities 1, 2).
- Lead: "On the direct sum of eigenstates alone, one can use branchwise pullbacks under `R` and obtain unitarity for the closed bound, at the cost of losing half the endpoint algebraic multiplicity." Consequence: a Hilbert-Polya operator must either exclude the threshold or accept a semisimplification.
- Related: L06-053, L06-055, L06-060

### L06-044 Why Selberg: the only infinite object where the source of reality is known
- Source: `notes/selberg-letters/draft.md:7-22`; brief `notes/selberg-letters/astra-brief.md:1-2`
- Raised by: orchestrator (Claude)
- Status at last mention: registered (shard 03e)
- Content: "In every manifest example in the book the unitarity of the odd block has a source that is not complete positivity: Parseval (Artin-Schreier), Deligne (Weil-LPS), or it is put in by hand (06h)." The Selberg zeta of a compact hyperbolic surface is the one infinite object where the trace formula is a theorem, the divisor is known, and the source of reality is known (self-adjointness of the Laplacian). The programme: derive the reality and the FE from the *letters* (Haar-unitarity of the sl2 flows plus the sl2 relations), and make the critical-line placement an additional positivity (Selberg's 1/4), exactly as Ramanujan is an extra bound for a Hermitian graph channel.
- Lead: this "letters principle" — separate what the letters give from what an extra bound gives — is the campaign's organising idea, and it generalises.
- Related: L06-003, L06-051, L06-061

### L06-045 The two-term stable transverse complex: even A, odd A+1, ring zeta = Z_S
- Source: `notes/selberg-letters/draft.md:69-90` (as a question); answer `notes/selberg-letters/astra-proofs.md:5, 90-97, 153-158`; reviewer's independent check `notes/reviews/selberg-letters-2026-09-16.md:188-192`
- Raised by: orchestrator (draft asks which of `zeta_R`, `Z_S`, `D_tow` is the right ring zeta); answered by codex prover
- Status at last mention: registered (def:stable-transverse-complex, shard 02h; thm in 03e)
- Content: Four candidate transfers and their ring zetas: function flow `A = -X` even gives `1/D_tow(s)`; the same all-odd gives `D_tow(s)`; full transverse forms give `zeta_R(s) = Z_S(s)/Z_S(s+1)`; and the **two-term stable transverse complex** (even `A`, odd `A+1`) gives `Z_S(s) = D_tow(s-1)/D_tow(s)`. The odd space is `D'(SM) eta_+` where `eta_+` is the covector dual to `U_+`, with `L_X eta_+ = -eta_+`. The complex is built from a letter: `df = (U_+ f) eta_+` intertwines `A` and `A+1` since `[A, U_+] = -U_+`.
- Lead: this is the object the Selberg campaign delivers. The reviewer verified `nu(z) = m_A(z) - m_A(z-1)` against the Selberg divisor at every point type.
- Related: L06-032, L06-046, L06-062

### L06-046 The pairing "d pairs even level m with odd level m+1, the odd level zero survives" is a leafwise cohomology claim, not proved
- Source: `notes/selberg-letters/astra-proofs.md:156`
- Raised by: codex prover
- Status at last mention: asserted on resonant modules only, flagged
- Content: "On nonexceptional ladder modules, `d` pairs even level `m` with odd level `m+1`; the odd level zero survives. This is the first-band mechanism behind the determinant quotient. We assert this algebra on resonant modules, not an unproved closed-range theorem for a global leafwise cohomology."
- Lead: prove the global leafwise (closed-range) cohomology statement. Consequence: it would upgrade the Selberg determinant ratio from a divisor identity to an actual cohomological cancellation, which is the natural home for "zeros are fermionic".
- Related: L06-045, L06-062

### L06-047 D5: no doubled-bond CP realisation of the Selberg transfer; the negative-supertrace obstruction
- Source: `notes/selberg-letters/draft.md:137-156`; refutation `notes/selberg-letters/astra-proofs.md:9, 292-337`, ledger L20-L23 `:571-574`
- Raised by: orchestrator (draft); refuted by codex prover
- Status at last mention: pursued, negative (prop:selberg-no-cp-realisation, shard 03e)
- Content: The draft proposed the bond `L^2(SM) ⊗ Λ^*(C^2) = L^2(SM) ⊗ C^{2|2}` with even drift and no jumps as a CP realisation. Three obstructions: (a) a single Kraus operator is not its own doubled transfer — conjugation has generator `T_⊥ ⊗ 1 + 1 ⊗ conj T_⊥`, graded trace `|Tr(P K_t)|^2` not `Tr(P K_t)`, and doubled growth `e^2` not `e`; (b) multiplication operators `M_f` are not Hilbert-Schmidt on a non-atomic `L^2`; (c) a direct sign obstruction — `str e^{tB_⊥} = 2 - e^t - e^{-t} < 0`, so both flat ring distributions are *negative*, while any cMPS ring norm is nonnegative.
- Lead: explicitly left open — "This does not prohibit an embedding with a different regularization or a restricted correlation functional; it does prohibit the identification asserted in the draft without additional construction" (`:328`). Finding such a regularisation is the open route.
- Related: L06-035, L06-039, L06-049

### L06-048 The two-term complex's rightmost rate is carried by the odd block, so "growth is even and simple" fails
- Source: `notes/reviews/selberg-letters-2026-09-16.md:183-187`; underlying `notes/selberg-letters/astra-proofs.md:111`, ledger L08 `:559`
- Raised by: Opus reviewer (recorded as a non-issue)
- Status at last mention: recorded so it is not re-litigated
- Content: For the Selberg two-term complex both constant roots (`s = 1, 0`) of `Z_S` are net **odd** zeros — there is no even Perron pole and no pole partner. So `def:graded-transfer-channel`'s requirement that the growth mode be even and simple fails for this object, and the reference pair `(1,0)` is supplied geometric data, not Perron data.
- Lead: either widen `def:graded-transfer-channel` or accept that the Selberg object is permanently in the spectral bin. Consequence: the notebook's central definition does not cover its best infinite example.
- Related: L06-035, L06-045, L06-007

### L06-049 "Drift = flow, jumps = adjacency": the critical-line divisor is a drift phenomenon
- Source: `notes/selberg-letters/draft.md:151-156`; result `notes/selberg-letters/astra-proofs.md:309-316, 330-335`, ledger L25 `:576`
- Raised by: orchestrator (Claude); partially confirmed by codex prover
- Status at last mention: CORRECTED — the slogan holds, the "destroys unless drift is kept" claim does not
- Content: On smooth multiplication observables, adding the two dissipative jumps `R = sqrt(kappa) H, sqrt(kappa) E` gives `L_kappa = -X + (kappa/2)(H^2+E^2) = -X + 2 kappa Omega + (kappa/2) W^2`. The jumps alone preserve K-invariants and equal `-2 kappa Delta` there; with the drift, that subspace is no longer invariant, and the diffusion does not preserve `ker U_-` either: `[U_-, (1/2)(H^2+E^2)] u = (2 lambda - 1) U_+ u` on a first-band state.
- Lead: "With drift there is a new differential operator whose divisor requires new analysis; neither preservation nor a universal destruction theorem is asserted." Computing the divisor of `L_kappa` for small `kappa > 0` is a concrete, wholly unexplored calculation — a perturbed Selberg zeta.
- Related: L06-022, L06-020, L06-047

### L06-050 D3: the first-band manifest form transported from Haar by the pushforward
- Source: `notes/selberg-letters/draft.md:92-121`; brief priority `notes/selberg-letters/astra-brief.md:48-50`; proof `notes/selberg-letters/astra-proofs.md:162-231`
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED and registered (thm:selberg-first-band-form, shard 03e)
- Content: For `u` in `Res^0_X(lambda) = {(X+lambda)u = 0, U_- u = 0}`, `Omega u = lambda(1+lambda) u` and `Delta pi_* u = -lambda(1+lambda) pi_* u`. Since `Delta` is a sum of squares of skew-adjoint letters, `-lambda(1+lambda) >= 0`, forcing `lambda in [-1,0] ∪ (-1/2 + iR)`. The form `G(u,v) = <pi_* u, pi_* v>_{L^2(M)}` is the Haar form transported by the letters, and `e^{t/2} e^{-tX}` is `G`-unitary iff the 1/4 coercivity holds.
- Lead: this is the "reality from the letters, bound from outside" template made precise for an infinite object.
- Related: L06-044, L06-051, L06-052, L06-053

### L06-051 The Casimir ordering error, and the corrected FE sign
- Source: draft `notes/selberg-letters/draft.md:95-98`; corrections `notes/selberg-letters/astra-proofs.md:205-210`, ledger L10 `:561`, L14 `:565`; reviewer confirmation `notes/reviews/selberg-letters-2026-09-16.md:27-31`
- Raised by: orchestrator (error), codex prover (correction), Opus reviewer (independent check)
- Status at last mention: CORRECTED, reviewer-verified
- Content: `Omega = X^2 + U_+ U_- - X` (the draft's `+X` in that ordering is wrong). Consequently the operator FE is `J A J^{-1} = -1 - A` for `A = -X`, i.e. `J X J^{-1} = 1 - X` (the draft's `-1 - X` is wrong).
- Lead: none stated; recorded as a dead route for the wrong sign.
- Related: L06-050, L06-062

### L06-052 The draft's single total pushforward form is degenerate; branchwise orthogonal pullbacks are needed
- Source: `notes/selberg-letters/draft.md:109-115`; correction `notes/selberg-letters/astra-proofs.md:177-183, 220`, ledger L12 `:563`; finite analogue `:486`, ledger L33 `:584`
- Raised by: orchestrator (error); corrected by codex prover
- Status at last mention: CORRECTED
- Content: For `sigma ≠ 1/4`, a Laplace eigenfunction `f` has two inverse images `u_±` at distinct flow eigenvalues, but `pi_*(u_+ - u_-) = 0`, so the Gram matrix of the total pushforward form on that pair is `||f||^2 [[1,1],[1,1]]` — degenerate. The repair is `G_⊕(u,v) = Σ_lambda <pi_* u_lambda, pi_* v_lambda>`, an explicit modal choice declaring branches orthogonal. Exactly the same phenomenon occurs on graphs and channels (partner lifts have the same vertex image).
- Lead: the branch labelling is part of the data of a Hilbert-Polya form; the "natural" untagged form never works. Consequence: any Phantasm construction must carry a branch tag.
- Related: L06-050, L06-060, L06-043

### L06-053 The 1/4 threshold is a real obstruction: algebraic multiplicity is twice geometric
- Source: `notes/selberg-letters/astra-proofs.md:7, 183, 226`, ledger L13 `:564`; H-NOEDGE `:43`; reviewer confirmation `notes/reviews/selberg-letters-2026-09-16.md:193-197`
- Raised by: codex prover
- Status at last mention: registered (shard 03e), reviewer-verified as "correct and sharp"
- Content: At `lambda = -1/2` (Laplace eigenvalue exactly 1/4) the first-band isomorphism gives geometric multiplicity `d_{1/4}`, but `ord_{-1/2} D_tow = 2 d_{1/4}`, so the flow block is not semisimple. A finite-dimensional `A` with `A^* G + GA = -G` and `G > 0` is semisimple, so no positive form makes the full algebraic block unitary. "Replacing it by two diagonal copies of `E_{1/4}` preserves the divisor and allows a positive form, but changes the operator to a semisimplification. We make no such replacement silently."
- Lead: divisor Ramanujan does not need H-NOEDGE; full operator Hilbert-Polya does. So a Hilbert-Polya operator for Riemann must either exclude the threshold or be a semisimplification. Consequence: this is a structural warning about what a Phantasm operator can be.
- Related: L06-043, L06-009, L06-050

### L06-054 The Riemann graded generator of 04b: what would have to be supplied
- Source: `notes/ramanujan-graded/astra-proofs.md:1610`; related `notes/ramanujan-graded/definition.md:257-267`, ledger L39 `:1439`
- Raised by: codex prover
- Status at last mention: raised as a repair list; not done
- Content: The Riemann graded generator is a graded *spectral* semigroup `C_+ ⊕ (K_S ⊕ ladder)_-`, not a constructed doubled-bond cMPS/GKSL transfer. "The regular nontrivial-zero modes have centre `-1/4` **iff RH**. The odd ladder `-(k+1/2)`, `k >= 1`, lies strictly to the left and is not in the draft's finite trivial set. It prevents a full single-line/FE statement even assuming RH."
- Lead: specify reference rates `0, -1/2`, remove the archimedean ladder as structural data, complete the pole pair, and supply the D10 analytic realisation. Consequence: without this the notebook's central object does not satisfy its own definition even under RH.
- Related: L06-023, L06-031, L06-035, L06-036

### L06-055 The Selberg flat tower of 09c: select the first band, don't declare descendants trivial
- Source: `notes/ramanujan-graded/astra-proofs.md:1611`; same conclusion reached independently `notes/selberg-letters/astra-proofs.md:134-145`, ledger L04-L05 `:555-556`
- Raised by: codex prover (both lanes)
- Status at last mention: registered (the D2 verdict table of shard 03e)
- Content: The full tower has a first band `-1/2 ± i r_j`, descendants `-1/2 - k ± i r_j`, and integer topological modes; the draft's trivial set does not make the tower single-line or reflection-symmetric. Verdicts: `Z_S` satisfies RH/Ram iff the 1/4 coercivity and FE always; the full Ruelle divisor and the all-band tower satisfy RH iff coercivity but **fail FE and Ram even under coercivity**, because the even band is translated by `-1` and reflection about `1/2` sends it to a non-existent even band. "One may explicitly remove the entire even shifted spectral band of `zeta_R` as additional supplied structural data... This is a *change of retained data*, not a consequence of calling a Jacobian shift a 'period image'."
- Lead: use the two-term complex, which gives `Z_S` directly and avoids the discretionary removal.
- Related: L06-045, L06-036

### L06-056 The full retained Ruelle divisor has an inverse-zeta (parity-exchanging) symmetry, not the notebook's FE
- Source: `notes/selberg-letters/astra-proofs.md:145`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "The full retained Ruelle divisor instead has `nu^R_ret(-s) = -nu^R_ret(s)`: its reflection about zero exchanges the two parities. This inverse-zeta symmetry is not the notebook's parity-preserving (FE)."
- Lead: a *second kind* of functional equation exists in the notebook's setting — an antisymmetry under reflection about the origin that swaps even and odd. Whether the Riemann side has an analogue (and whether it is the more natural symmetry for a supersymmetric object) is unexamined.
- Related: L06-009, L06-055

### L06-057 D7: the finite Hashimoto-lift theorem — this settles the notebook's "Hermitian channel + lift → odd block unitary" open item
- Source: `notes/selberg-letters/draft.md:179-193`; proof `notes/selberg-letters/astra-proofs.md:8, 395-496`; reviewer verification `notes/reviews/selberg-letters-2026-09-16.md:40-44, 198-200`
- Raised by: orchestrator (Claude); proved constructively by codex prover; independently verified by the Opus reviewer
- Status at last mention: registered (shard 03f), reviewer VALID
- Content: With `T = SR - J_0`, `J_0^2 = 1`, `RS = Sigma = Sigma^*`, `R J_0 S = D`, one has `Sigma R = R(T + qT^{-1})`, an explicit two-sided inverse pushforward `F_mu f = (mu S - J_0 S)f/(mu^2-1)` for `mu ≠ ±1`, a companion model `C = [[Sigma, q],[-1, 0]]`, an explicit metric `G_C = [[1, Sigma/2],[Sigma/2, q]]` with `C^* G_C C = q G_C`, and an operator FE `F_C = [[0, sqrt q],[q^{-1/2}, 0]]`. `G_C` is positive definite iff the **strict** band `|a| < 2 sqrt q` holds. Correction L35: the quantum pushforward uses `Ad(U_i)`, not `Ad(U_i^*)`, in the notebook's source-letter convention.
- Lead: "It is not a theorem for arbitrary Hermitian CP channels without an inverse-paired lift" (`:496`) — the inverse pairing is doing the work, and whether a non-inverse-paired analogue exists is open.
- Related: L06-003, L06-043, L06-060

### L06-058 mu = ±sqrt q is *not* an exception to the pushforward isomorphism
- Source: `notes/selberg-letters/astra-proofs.md:414, 479`, ledger L32 `:583`; reviewer check `notes/reviews/selberg-letters-2026-09-16.md:198-200`
- Raised by: codex prover; verified by the reviewer
- Status at last mention: CORRECTED, reviewer-verified
- Content: The draft expected the exceptional set to include the critical-circle points `±sqrt q`. It does not: `F_mu` is a two-sided inverse there too. The generic exception is only `mu = ±1` (the cycle/reversal modes). The endpoints obstruct *semisimplicity*, not the eigenspace isomorphism.
- Lead: none stated; a correction that removes a spurious worry about the critical circle.
- Related: L06-057, L06-043

### L06-059 D4: the continuum Ihara quadratic and the sampled adjacency is a cosine functional calculus
- Source: `notes/selberg-letters/draft.md:123-135`; correction `notes/selberg-letters/astra-proofs.md:234-290`, ledger L18 `:569`
- Raised by: orchestrator (Claude); corrected by codex prover
- Status at last mention: CORRECTED
- Content: The draft proposed `U_+` as the continuum non-backtracking lift with the bands as its ladder (`Res_X(lambda) = ⊕_m U_+^m Res^0_X(lambda+m)`, `U_-^m U_+^m = m! prod_j (2 lambda + m + j)`), and `mu = e^lambda`, `q = e^{-1}` as the continuum Ihara quadratic. The correction: on sampling at time `tau`, `mu_± = e^{tau lambda_±}`, `q_tau = e^{-tau}`, and the adjacency is `a_tau(sigma) = 2 e^{-tau/2} cos(tau sqrt(sigma - 1/4))` — a functional calculus of `Delta`, **not** `-2 Delta`, and sampling aliases frequencies.
- Lead: the notebook's open item (operator-level compression of `D_tow` into a Laplacian determinant) is proved **for the first band only**; "a literal full-tower compression to a single Laplacian determinant is still not supplied" (`:257, 286`). That remains open.
- Related: L06-019, L06-045, L06-057

### L06-060 The finite and continuum mechanisms are the same theorem twice
- Source: `notes/selberg-letters/astra-proofs.md:435-437, 486, 593-623`
- Raised by: codex prover
- Status at last mention: registered as the two "labelled-input theorems"
- Content: Both the compact Selberg and the finite graph/channel cases split into: [LETTERS/HAAR] giving reality and the form's branch norms; [ANALYSIS/FINITE ANALYSIS] giving the pushforward isomorphism; [BOUND] (Selberg 1/4 or Hastings/Ramanujan) giving the critical line/circle; and [ENDPOINT] (no threshold / strict band) giving the full operator Hilbert-Polya form. In both, the untagged pullback is degenerate and the endpoint gives a Jordan block.
- Lead: the parallel is exact enough that any new mechanism found on one side should be tested on the other. Consequence: this is the campaign's transferable structure.
- Related: L06-043, L06-050, L06-052, L06-057

### L06-061 D6: the modular surface, the Riemann zeros, and where the mechanism stops
- Source: `notes/selberg-letters/draft.md:158-177`; brief `notes/selberg-letters/astra-brief.md:57-58`; result `notes/selberg-letters/astra-proofs.md:10, 339-393`
- Raised by: orchestrator (Claude)
- Status at last mention: OPEN (exploratory), registered as obs:modular-scattering-sector (shard 03f)
- Content: For `Gamma = PSL_2(Z)`, the scattering determinant `phi(s) = sqrt(pi) Gamma(s-1/2) zeta(2s-1)/(Gamma(s) zeta(2s))` has a pole at `s_0 = rho/2` for every nontrivial zero `rho`, and `Z_S` has a zero there. So RH is equivalent to *these* zeros lying on `Re s = 1/4`. But the D3 mechanism fails exactly there: at a scattering pole one must use the leading Laurent coefficient `e_{-m}` of the Eisenstein series, whose cusp constant term `c_{-m} y^{1-s_0}` makes it non-`L^2`, so the Haar-transported form is unavailable.
- Lead: what is missing is **H-CUSP-BRIDGE** — "a specified noncompact flow resolvent realization, with finite-rank resonant data at `s_0 - 1`, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a compatible positive modal pairing" (`:358`). This is the single named gap between the Selberg mechanism and RH.
- Related: L06-062, L06-063, L06-067

### L06-062 The rate mismatch: the scattering sector's flow centre is -3/4, not -1/4
- Source: `notes/selberg-letters/astra-proofs.md:347, 374`, ledger L30 `:581`
- Raised by: codex prover
- Status at last mention: registered as a correction and an obstruction
- Content: For a putative flow first-band state at `lambda = s_0 - 1`, the proposed rescaling `e^{t/2}` can never make the flow unitary in a positive norm, because `Re(lambda + 1/2) = Re s_0 - 1/2 < 0`, independently of RH and of how the form was built. Under RH the correct flow rate would be `-3/4` (factor `e^{3t/4}`), whereas the Riemann functional-model centre of shard 04b is `-1/4` (it uses `B` eigenvalues `-conj rho/2`). Also, the compact reflection `s -> 1-s` does not preserve this odd zero subset; the right reflection is `s -> 1/2 - s`, i.e. `lambda -> -3/2 - lambda`.
- Lead: "At the corrected centre, existence of an invariant positive form would need a new construction, with RH and Jordan data accounted for." Consequence: the identification of the Riemann channel with a flow compression is *not* established by the affine relations; the rates differ by a factor.
- Related: L06-061, L06-054

### L06-063 Truncated Maass-Selberg positivity does not imply RH
- Source: `notes/selberg-letters/draft.md:171-177` (proposed); result `notes/selberg-letters/astra-proofs.md:375-391`, ledger L31 `:582`
- Raised by: orchestrator (proposal); refuted by codex prover
- Status at last mention: pursued, negative
- Content: The draft hoped `Re s = 1/4` would become a positivity statement of the form "a truncated norm is nonnegative". The prover derived the Maass-Selberg identity (D6-MS) from Green's identity and computed the leading bivariate Laurent coefficient at `s = w = s_0`: `||Lambda^Y e_{-m}||^2 = |c_{-m}|^2 Y^{1-2 Re s_0}/(1 - 2 Re s_0) > 0`. This is positive throughout `0 < Re s_0 < 1/2`, not only at `1/4`; its growth in `Y` is exactly the missing integrability.
- Lead: what is *not* ruled out — "unrestricted `C^∞` functions on a noncompact surface need not lie in `L^2`; the draft's proposed class 'finite words applied to `L^2` or `C^∞`' does not define a general no-go for every weighted form". So a weighted-space form is still permitted.
- Related: L06-061, L06-062

### L06-064 D8: K-type parity makes the geodesic generator odd — it is not a grading for the flow
- Source: `notes/selberg-letters/draft.md:195-203`; proof `notes/selberg-letters/astra-proofs.md:498-544`, ledger L37-L40 `:588-591`
- Raised by: orchestrator (Claude); proved with a counterexample by codex prover
- Status at last mention: CORRECTED, obs:selberg-grading-choice rewritten
- Content: With `P_K f = (-1)^{m/2} f` on K-types, `P_K H P_K = -H`, `P_K E P_K = -E`, `P_K W P_K = W`, so the two-jump diffusion is even but `X = H/2` is **odd**: `P_K` does not commute with the flow. Also, full K-type parity is not Hodge degree (Hodge uses two weight-zero copies and weights `±2`; K parity has one scalar copy and all even weights). And the draft's "supercancellation" is false: on a spherical principal-series constituent, `Tr(P_K e^{t L_adj}) = e^{-2 sigma t} Σ_n (-1)^n e^{-2n^2 t} ≠ 0`, with the theta factor strictly positive by Poisson summation (value `0.730000328323` at `t = 1`).
- Lead: what survives — "K parity genuinely grades the diffusion letters", so it remains a possible grading for the *diffusion representation channel*, with its own doubled parity and spectral analysis (`:519, 542`). That channel has never been analysed.
- Related: L06-033, L06-032, L06-065

### L06-065 The Hodge-bundle diffusion supertrace is not the Euler characteristic
- Source: `notes/selberg-letters/astra-proofs.md:529-534`
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: On weight `m`, `L_adj = 2 Omega - m^2/2`, so weights `0` and `±2` carry a relative diffusion shift `-2`. Even on the selected Hodge bundles the diffusion heat supertrace is `2(1 - e^{-2t}) Tr e^{-2t Delta_0} + e^{-2t} chi(M)`, not the constant `chi(M)`.
- Lead: the deviation `2(1 - e^{-2t}) Tr e^{-2t Delta_0}` is an explicit, computable non-topological remainder — it is exactly a Laplace heat trace, i.e. the Selberg spectral data, appearing as a *defect* of McKean-Singer. Nobody asked what that remainder's zeta is.
- Related: L06-064

### L06-066 Reviewer Issue 1: the first-band lambda-set needs its parameter restriction; the exceptional points are not empty
- Source: `notes/reviews/selberg-letters-2026-09-16.md:63-87`; applied `notes/selberg-letters/astra-proofs.md:663-665`
- Raised by: Opus reviewer
- Status at last mention: MINOR, fix applied verbatim in shard 03e
- Content: The display `lambda in [-1,0] ∪ (-1/2 + iR)` holds only for `lambda ∉ -1 - N_0`. The reviewer notes the exceptional points are genuinely non-empty: `ord_{-N} D_tow = c N^2 + 2` against the band prediction 2, so at `lambda in {-2,-3,...}` there is real extra order. "At `lambda in {-2,-3,...}` nothing in the cited material excludes first-band states".
- Lead: what lives at the negative-integer exceptional parameters of the first band is unexamined, and the tower divisor says something does.
- Related: L06-050, L06-045

### L06-067 Reviewer Issue 2: the order m of the modular Selberg zero at rho/2 is an inference, not in the source
- Source: `notes/reviews/selberg-letters-2026-09-16.md:89-107`; applied `notes/selberg-letters/astra-proofs.md:666-668`
- Raised by: Opus reviewer
- Status at last mention: MINOR, marked as an inference in shard 03f
- Content: FJS's divisor items 1,2,3,4,7 carry explicit multiplicities; item 6 — the one used — does not. The order-`m` claim is standard but inferred (from equating residues of `Z_S'/Z_S` and `phi'/phi`). The RH equivalence uses only the location.
- Lead: derive the multiplicity properly if it is ever needed; the RH statement does not depend on it.
- Related: L06-061

### L06-068 Reviewer Issue 4: six ledger rows report the draft's *questions* as claims
- Source: `notes/reviews/selberg-letters-2026-09-16.md:124-145`; applied `notes/selberg-letters/astra-proofs.md:671-673`
- Raised by: Opus reviewer
- Status at last mention: MINOR, applied (40 rows = 34 corrections + 6 answers)
- Content: L06 corrects nothing (the draft already described the function flow as the all-odd tower transfer); L04, L05, L20, L23, L26 attribute to the draft claims the draft explicitly posed as open questions or instructions. "This matters because the lab book reads the ledger as a list of *errors found*."
- Lead: a process lesson for future prover lanes — distinguish "drafted" from "asked".
- Related: L06-055, L06-047

### L06-069 Reviewer Issue: Selberg's 1/4 is *known* for PSL_2(Z) (Booker-Lee-Strömbergsson)
- Source: `notes/selberg-letters/astra-proofs.md:356`, ledger L28 `:579`; verification `notes/reviews/selberg-letters-2026-09-16.md:16-20, 272-278`
- Raised by: codex prover; byte-verified by the Opus reviewer
- Status at last mention: registered (cit:bls-selberg-level-one)
- Content: The draft called Selberg's 1/4 property "open" for the modular group. It is not: Booker-Lee-Strömbergsson, arXiv:1803.06016, Theorem 1.1 — "The Selberg eigenvalue conjecture is true for `Gamma_1(N)` for `N <= 880`, and for `Gamma(N)` for `N <= 226`" — covers level one. The general congruence-level conjecture is different.
- Lead: so on the modular surface the *discrete* side of the coercivity is settled; the obstruction to RH is entirely in the continuous/scattering sector, which is precisely where the mechanism fails (L06-061).
- Related: L06-061, L06-028

### L06-070 Reviewer Issue 5: "stable" for eta_+ collides with DFG's dual-bundle naming
- Source: `notes/reviews/selberg-letters-2026-09-16.md:147-160`; applied `notes/selberg-letters/astra-proofs.md:674-675`
- Raised by: Opus reviewer
- Status at last mention: MINOR, fix applied verbatim in shard 02h
- Content: `U_+` is DFG's stable field, but the covector `eta_+` annihilates `E_0 ⊕ E_u` and so lies in DFG's `E_u^*` (their `*`-convention switches `u` and `s`). "A reader checking D2 against D5's `B_⊥` or against the draft's `E_u^*, E_s^*` will mis-assign the `e^t` weight."
- Lead: none; a naming trap recorded so nobody re-derives the weights with the wrong sign.
- Related: L06-045

### L06-071 Reviewer Issue 6: "derived from the letters" is stronger than what was proved
- Source: `notes/reviews/selberg-letters-2026-09-16.md:162-179`; applied `notes/selberg-letters/astra-proofs.md:676-678`
- Raised by: Opus reviewer
- Status at last mention: MINOR, reworded verbatim in shard 03e
- Content: Once every retained `lambda` has `Re lambda = -1/2` and the block is semisimple, the *existence* of a positive `G` is the notebook's own (HP) equivalence (`prop:hp-inner-product-discrete`). What the letters genuinely supply is (i) the branch norms `||pi_* u||_{L^2(M)}` via Haar and `pi_*`, and (ii) the reality/line location. The new content is that this *particular* form is the transported Haar form, plus the threshold obstruction.
- Lead: a caution for the whole "letters principle" — deriving a form from the letters is only new content if the form is canonical, since *some* form always exists once the line and semisimplicity hold.
- Related: L06-044, L06-050, L06-053

## Small but possibly consequential

1. **L06-021** (even Hamiltonian, odd coherences). One sentence in a prover's aside, never followed: it reopens exactly the route D8 seemed to close and hands a design principle for a Riemann Lindbladian — imaginary parts from an even Hamiltonian on the coherences, real part from odd jump rates.
2. **L06-039** (the `n_0 - n_1 = (D_+-D_-)^2 >= 0` obstruction). A one-paragraph dimension count that may be the actual reason no CP realisation of the Artin-Schreier / Riemann graded transfers has ever been found.
3. **L06-049** (divisor of the drift-plus-diffusion generator `L_kappa`). A perturbed Selberg zeta; the prover explicitly declined to assert either preservation or destruction, so the calculation is wide open and finite-effort.
4. **L06-065** (the Hodge-bundle diffusion supertrace defect `2(1-e^{-2t}) Tr e^{-2t Delta_0}`). A computable non-topological remainder of McKean-Singer that *is* the Laplace spectral data; nobody asked what its zeta is.
5. **L06-056** (the parity-exchanging reflection `nu(-s) = -nu(s)` of the Ruelle divisor). A second kind of functional equation, antisymmetric and parity-swapping, which might be the more natural symmetry for a supersymmetric object.
6. **L06-018** (the `(5;13)` reduced formula `f_4 f_{-4}/(f_{14} f_{-14})`, `b = 13`). A tiny explicit graded L-function that fell out of an audit and was never identified arithmetically.
7. **L06-046** (the leafwise closed-range cohomology behind `df = (U_+ f) eta_+`). Proving it would turn the Selberg determinant ratio from a divisor identity into an actual cohomological cancellation — the natural home for "zeros are fermionic".
8. **L06-066** (the negative-integer exceptional first-band parameters). The tower divisor says genuine extra order sits at `-2, -3, ...`; nothing in the cited material says what state carries it.

## Dead routes recorded

- **Odd-sector Alon-Boppana.** REFUTED. `Phi = (1/4)(Ad I + Ad I + Ad P + Ad P)` has `Phi_1 = 0` in every bond dimension, and a primitive degree-16 family `Depol_2 ⊗ Psi_m` has `rho(Phi_1) = 0` with unbounded bond. `notes/ramanujan-graded/definition.md:173-180` → `notes/ramanujan-graded/astra-proofs.md:276-339`, ledger L05 `:1405`.
- **"Equal spectral radii force net cancellation."** False: the single letter `P = diag(1,-1)` has even `{1,1}`, odd `{-1,-1}`. `notes/ramanujan-graded/astra-proofs.md:104-109`, ledger L01 `:1401`.
- **"The even algebra contains every positive operator."** False: `I + X` with `P = Z`. Ledger L02 `notes/ramanujan-graded/astra-proofs.md:1402`.
- **"Net divisor on the circle iff both entire sectors in the band."** Converse false; primitive degree-14 counterexample where the out-of-band value 10 cancels. `notes/ramanujan-graded/astra-proofs.md:253-264`, ledger L03 `:1403`.
- **"Every structural period mode is even."** False: `(Ad Z + Ad Y)/2` graded by `Z` has odd eigenoperator `X` at `-1`. Ledger L31 `notes/ramanujan-graded/astra-proofs.md:1431`, `:1531-1538`.
- **"Every odd eigenvalue/constituent supplies a zeta zero."** False; a zero survives only if odd multiplicity exceeds even at that point. Ledger L08 `notes/ramanujan-graded/astra-proofs.md:1408`.
- **LPS numerator degrees 36 and 196 over four trivial factors.** Wrong: reduced degrees are 4/4 and 144/144, with a degree-140 nontrivial denominator in the `(13;5)` case; not a curve denominator. `notes/ramanujan-graded/astra-proofs.md:462-479`, ledger L07 `:1407`.
- **"The qubit is an ordinary irrep of the Pauli group modulo its centre."** False — it is projective on that abelian quotient. Ledger L09 `notes/ramanujan-graded/astra-proofs.md:1409`.
- **"Exact sampling makes net-divisor RH and FE mesh-independent."** False without H-noalias; explicit CP example where the whole sampled divisor cancels at `h = 1`. `notes/ramanujan-graded/astra-proofs.md:536-544`, ledger L10 `:1410`.
- **"Each odd letter has a fixed `sqrt h R` limit."** False; only the collective bound `Σ_{odd} ||A_a(h)||_HS^2 = O(h)` holds. Ledger L12 `notes/ramanujan-graded/astra-proofs.md:1412`.
- **"The divisor is the union of scalar correlation poles."** Wrong object: scalar pole order does not measure eigenspace multiplicity. Ledger L13 `notes/ramanujan-graded/astra-proofs.md:1413`.
- **"Continuous spectrum automatically gives a scalar signed measure."** False for a non-normal generator. Ledger L14 `notes/ramanujan-graded/astra-proofs.md:1414`.
- **The Lie walk's threshold is 1/2.** Wrong normalisation; it is `1/(2d) = 1/4`. Ledger L15 `notes/ramanujan-graded/astra-proofs.md:1415`.
- **"Tempered iff every geodesic correlation exponent has real part -1/2."** False: discrete series are tempered and decay faster (`cosh(t/2)^{-n}`, exponent `-n/2`), and descendants add further lines. Ledger L16 `notes/ramanujan-graded/astra-proofs.md:1416`.
- **"Infinite-dimensional `pi` implies purely continuous diffusion spectrum."** False; D12's odd sector is entirely discrete. Ledger L17 `notes/ramanujan-graded/astra-proofs.md:1417`.
- **The odd diffusion ladder "starts at n/2".** Wrong: the exact rates are `kappa(n + 2nj + 2j^2)`, minimum `2 kappa k`. Ledger L20 `notes/ramanujan-graded/astra-proofs.md:1420`.
- **`P` as an HS eigenmode at `-2 gamma`.** False: `P ∉ HS(H)` when both blocks are infinite-dimensional; it supplies no HS divisor point. Ledger L21 `notes/ramanujan-graded/astra-proofs.md:1421`.
- **`str e^{tT}` as the ordinary integral of the heat kernel against the squared character difference.** False: the even heat operator is not trace class. Ledger L22 `notes/ramanujan-graded/astra-proofs.md:1422`.
- **"Hyperbolic classes live only in the even sector; the odd sector is compact."** False: the regular even and odd character contributions are equal on hyperbolic elements and cancel. Ledger L23 `notes/ramanujan-graded/astra-proofs.md:1423`.
- **"The lowest-exponent ladder is literally the `Gamma_C`/`Gamma_R` divisor."** Only the *positions* match; zero rung, multiplicities and descendants are unaccounted, and no determinant is proved to be a Gamma function. Ledger L24 `notes/ramanujan-graded/astra-proofs.md:1424`, `:1180-1186`.
- **"Unitary letters make ring norms integral word counts."** False: `N_P(1) = 16/3` for a band-satisfying unitary example. Ledger L26 `notes/ramanujan-graded/astra-proofs.md:1426`.
- **"A circle numerator is a curve L-polynomial, or at least a Weil polynomial."** False twice: non-integral numerators exist, and `(1-3u)^4` over `F_9` is an integral Weil polynomial that would force `-2` points. Ledger L27 `notes/ramanujan-graded/astra-proofs.md:1427`.
- **K-type grading `m = 0` vs `m = ±2` as the Selberg/form-degree grading on a doubled bond.** Dead: selecting those K-types does not define a `G`-invariant splitting (`notes/ramanujan-graded/astra-proofs.md:1236-1240`, ledger L40 `:1440`), and `P_K` makes the geodesic generator `X` odd so it is not a grading for the flow at all (`notes/selberg-letters/astra-proofs.md:502-506`, ledger L37 `:588`).
- **"K-type supertrace supercancels every positive Laplace eigenvalue."** False: the theta factor `Σ_n (-1)^n e^{-2tn^2}` is strictly positive (`0.730000328323` at `t=1`). `notes/selberg-letters/astra-proofs.md:512-518, 535-541`, ledger L39 `:590`.
- **`Omega = X^2 + U_+U_- + X`.** Wrong ordering; the truth is `Omega = X^2 + U_+U_- - X`. Ledger L10 `notes/selberg-letters/astra-proofs.md:561`.
- **`J X J^{-1} = -1 - X`.** Wrong sign; it is `J A J^{-1} = -1 - A` for `A = -X`, i.e. `J X J^{-1} = 1 - X`. Ledger L14 `notes/selberg-letters/astra-proofs.md:565`.
- **The single total pushforward form `<pi_* u, pi_* v>` on the first band.** Degenerate: Gram matrix `||f||^2 [[1,1],[1,1]]` on a partner pair. Needs branchwise orthogonalisation. Ledger L12 `notes/selberg-letters/astra-proofs.md:563`, `:220`; finite analogue ledger L33 `:584`.
- **The single-copy exterior drift as a graded CP/cMPS transfer.** Refuted three ways (doubled generator, non-HS multiplication observables, negative flat supertraces). `notes/selberg-letters/astra-proofs.md:326-328`, ledger L20-L23 `:571-574`.
- **"Full retained Ruelle divisor has a Selberg-centred FE/Ramanujan statement."** Fails: the even band is translated by `-1` and reflection about `1/2` sends it to a non-existent band. Ledger L04 `notes/selberg-letters/astra-proofs.md:555`, `:139-140`.
- **Exponentiation turns the flow/Laplacian relation into the Ihara quadratic with the same adjacency.** False: the sampled adjacency is `2 e^{-tau/2} cos(tau sqrt(sigma - 1/4))`, a functional calculus of `Delta`, not `-2 Delta`. Ledger L18 `notes/selberg-letters/astra-proofs.md:569`.
- **"First-band intertwining resolves the full-tower compression."** No: only the first-band polynomial relation and the ladder are proved; the literal global compression is unsupplied. Ledger L19 `notes/selberg-letters/astra-proofs.md:570`, `:257, 286`.
- **"First-band cusp states push forward to `E(z, rho/2)`."** The value is undefined at a pole; use the leading Laurent coefficient, which has a nonzero `y^{1-s_0}` constant term and is not in `L^2`. Ledger L27 `notes/selberg-letters/astra-proofs.md:578`.
- **`e^{t/2}` as the unitarising factor for the scattering sector.** Impossible for any positive eigenvector norm since `Re s_0 - 1/2 < 0`; under RH the factor would be `e^{3t/4}`, centre `-3/4`, not the Riemann model's `-1/4`. Ledger L30 `notes/selberg-letters/astra-proofs.md:581`, `:347`.
- **"Truncated-norm positivity forces `Re s_0 = 1/4`."** False: the leading Maass-Selberg norm `|c_{-m}|^2 Y^{1-2 Re s_0}/(1-2 Re s_0)` is positive throughout the strip. Ledger L31 `notes/selberg-letters/astra-proofs.md:582`, `:386-391`.
- **"Graph/channel pushforward is exceptional at `±sqrt q`."** False: `F_mu` is a two-sided inverse there; only `mu = ±1` is generically exceptional. Ledger L32 `notes/selberg-letters/astra-proofs.md:583`.
- **"Full Hashimoto Hilbert-Polya iff closed sector Ramanujan."** Needs the **strict** band; endpoints give size-two Jordan blocks. Exact counterexamples `K_3 □ Q_3` and the ten-letter Pauli channel. Ledger L34 `notes/selberg-letters/astra-proofs.md:585`, `:494`.
- **Quantum pushforward with `Ad(U_i^*)`.** Wrong convention; use `Ad(U_i)`. Ledger L35 `notes/selberg-letters/astra-proofs.md:586`.
- **"Selberg's 1/4 is open for `PSL_2(Z)`."** False; known by Booker-Lee-Strömbergsson Theorem 1.1. Ledger L28 `notes/selberg-letters/astra-proofs.md:579`; byte-verified `notes/reviews/selberg-letters-2026-09-16.md:16-20`.
