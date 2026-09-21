# Lane L01: founding transcript, HANDOFF, README, main notes

Scope: every idea, lead, conjecture, proposal, "what if", reviewer/prover remark,
open item and dead route that appears in the eight files assigned to this lane.
Established mathematics is only described where it is the content of an idea.

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| `transcript/transcript.md` | 1398 | yes | L01-001 … L01-041 (41) |
| `HANDOFF.md` | 955 | yes | L01-042 … L01-098 (57) |
| `README.md` | 174 | yes | L01-099 … L01-101 (3) |
| `notes/what-rh-has-become.md` | 186 | yes | L01-102 … L01-106 (5) |
| `notes/riemann-channel-note.md` | 140 | yes | L01-107 … L01-110 (4) |
| `notes/deligne-via-graphs.md` | 241 | yes | L01-111 … L01-119 (9) |
| `notes/weil-lps-channels.md` | 98 | yes | L01-120 … L01-122 (3) |
| `notes/artin-schreier-mps.md` | 82 | yes | L01-123 … L01-125 (3) |

Total: 125 entries. No file was without ideas.

## Ideas and leads

### L01-001 Bose gas over the naturals (TJO's first guess), corrected to a gas over primes
- Source: `transcript/transcript.md`:60-66, 70-87
- Raised by: TJO
- Status at last mention: raised, corrected immediately (superseded by L01-002)
- Content: TJO proposed the single-particle space `l^2(N)` with `h_0 e_n = (log n) e_n`, then bosonic Fock space on top, expecting the partition function to be `zeta(beta)`. The correction: the trace of `e^{-beta h_0}` on `l^2(N)` is already `zeta(beta)`, so no Fock space is needed; and the Fock space over `l^2(N)` gives `prod_n (1 - n^{-beta})^{-1}`, which is not zeta and whose `n=1` mode has energy `log 1 = 0` and condenses at every temperature.
- Lead: use `l^2(primes)` instead, one mode per prime with energy `log p`; then `l^2(N)` is the Fock space by unique factorisation. This is Julia's free Riemann gas, made rigorous by Bost-Connes.
- Related: L01-002, L01-053

### L01-002 The free Riemann gas: primes are particles, integers are many-body states
- Source: `transcript/transcript.md`:74-87
- Raised by: orchestrator (Claude), attributing Julia and Bost-Connes
- Status at last mention: established background; became "side A" of the whole notebook
- Content: one bosonic mode per prime with energy `log p`; occupation numbers `(k_p)` correspond to `n = prod p^{k_p}`; `Tr e^{-beta H} = prod_p (1-p^{-beta})^{-1} = zeta(beta)`. The Euler product is literally the Fock-space product over modes, and the pole at `beta = 1` is the Bose condensation temperature where the Bost-Connes phase transition sits.
- Lead: none stated at this point; it became the fixed "side A" of every later construction.
- Related: L01-001, L01-053, L01-072

### L01-003 Wick-rotating the Bost-Connes Hamiltonian to get Hilbert-Polya
- Source: `transcript/transcript.md`:103, 107-137
- Raised by: TJO
- Status at last mention: pursued, negative; replaced by a Fourier-duality reading
- Content: TJO asked whether, assuming RH, going to real time in the BC trace produces the Hilbert-Polya Hamiltonian, with the critical line as "real time". The answer: `Tr(e^{-H/2} e^{-itH}) = zeta(1/2+it)`, a damped return amplitude, so the zeros are special *times* of the BC flow and never eigenvalues of `H` (whose spectrum is `{log n}`). The correct relation is Fourier duality: the explicit formula says one spectrum is the Fourier transform of the other. "energy on side A = time on side B".
- Lead: look for side B as a *dual* object, not a rotation; this motivated everything after.
- Related: L01-004, L01-005, L01-035

### L01-004 Berry-Keating reading: `log n` are classical periods, `xp` is the candidate
- Source: `transcript/transcript.md`:127-137, 444
- Raised by: orchestrator (Claude), citing Berry-Keating and Connes
- Status at last mention: raised, used as orientation, not pursued directly here
- Content: matching the Gutzwiller trace formula to the explicit formula makes the primitive periodic orbits have periods `log p`, repetitions `k log p`, and amplitudes `p^{-k/2}` saying every orbit is hyperbolic with Lyapunov exponent exactly 1. `H_PH = xp` generates dilations, and `mu_n` of BC is dilation by `n`, so `mu_n = e^{i(log n)D}`. "BC energy of `mu_n` is `log n`. Dilation time of `mu_n` is `log n`. Same number, opposite role."
- Lead: pass from the BC algebra to the adele class space, where dilation is the operator and the zeros are an absorption spectrum. Consequence: an operator whose one-parameter group is indexed by `log n`.
- Related: L01-003, L01-029, L01-030

### L01-005 The zeros as an absorption spectrum, not an emission spectrum
- Source: `transcript/transcript.md`:135, 440, 444; `notes/what-rh-has-become.md`:120
- Raised by: orchestrator (Claude), attributing Connes
- Status at last mention: recurring structural constraint; later hardened into the "fermionic zeros" requirement
- Content: the sign of the zero term in the explicit formula is opposite to the Selberg case. Connes reads this as: the zeros are lines *missing* from a continuum, not eigenvalues added to a discrete spectrum. Any model of side B must reproduce this sign.
- Lead: a candidate side B must produce the absorption sign; Connes's adele-class-space construction does, Selberg's surfaces do not.
- Related: L01-057, L01-104, L01-113

### L01-006 Soule's zeta as a simpler instance (rejected), and the F_1 hope
- Source: `transcript/transcript.md`:143, 183
- Raised by: TJO
- Status at last mention: raised, judged the wrong small case; the F_1 hope recorded but not pursued
- Content: TJO suggested Soule's zeta over `F_1` as a toy. The reply: for projective n-space it gives `zeta(s) = s(s-1)...(s-n)`, all zeros real, no critical line, because "over F_1 the Frobenius is trivial". Its only relevance is the hope that if `Spec Z` were a curve over `F_1` one could imitate the elliptic-curve proof with `Spec Z x_{F_1} Spec Z` playing the role of `E x E`.
- Lead: the F_1 hope is a hope about side B (the missing product), not a small example of RH. Later re-appears as "zeta lacks the product" (L01-114).
- Related: L01-114, L01-118

### L01-007 The elliptic curve over F_2 as the mandatory test bed for any side-B proposal
- Source: `transcript/transcript.md`:147-185, especially 185
- Raised by: orchestrator (Claude)
- Status at last mention: raised as an acceptance test, never formally applied
- Content: for `E: y^2 + y = x^3` over `F_2`, `Z(T) = (1+2T^2)/((1-T)(1-2T))`, side A is the closed-point gas and side B is the 2x2 Frobenius on `H^1` with `alpha = +- i sqrt 2`. "a construction that claims to produce side B for Spec Z should at least reproduce the 2x2 Frobenius when run on E over F_2."
- Lead: use this as a unit test on any proposed Riemann construction. Consequence: cheap falsification of over-general proposals.
- Related: L01-088, L01-092

### L01-008 The permutation (1 2)(3 4 5) as the elementary model of the whole subject
- Source: `transcript/transcript.md`:195-239, 247; `HANDOFF.md`:284-289
- Raised by: orchestrator (Claude), then adopted and restarted from by TJO
- Status at last mention: registered (shard 03b, `scripts/graded_permutation.py`, 46 checks in CI), unreviewed
- Content: for a permutation matrix, `1/det(1-TM) = prod_cycles 1/(1-T^{|c|})` is a Bose gas with one mode per cycle and energy = cycle length, while `Tr(M^n)` counts fixed points of `sigma^n`. Side A counts cycles, side B is the linear algebra of a small matrix with the same fixed-point counts. "That is the entire bridge. There is no fancy math in it."
- Lead: everything later is this picture with upgrades; TJO explicitly returned to it on 2026-09-14 to rebuild the grading from scratch.
- Related: L01-009, L01-010, L01-079

### L01-009 RH for a finite permutation is "the matrix is unitary", automatic
- Source: `transcript/transcript.md`:253, 286-290; `notes/what-rh-has-become.md`:23-25
- Raised by: TJO (as a question), confirmed by orchestrator
- Status at last mention: settled, elementary
- Content: a permutation matrix permutes an orthonormal basis, so all eigenvalues lie on the unit circle. The "RH analogue" at this level holds for free, so no hard content exists until the permutation is infinite.
- Lead: the difficulty must be located elsewhere - in the existence and eigenvalue radii of a *different*, small matrix.
- Related: L01-010, L01-011

### L01-010 The mildest infinite permutation: one infinite cycle is empty, many finite cycles is the real case
- Source: `transcript/transcript.md`:296, 302-314
- Raised by: TJO
- Status at last mention: settled; option 2 declared empty
- Content: TJO asked which of (1) infinitely many finite cycles and (2) one infinite cycle is harder. One infinite cycle is the shift on `Z`: no fixed points at any `n`, `Z(T) = 1`, nothing to study, and in the Frobenius setting infinite cycles never occur. Infinitely many finite cycles gives `fix(sigma^n) = sum_{d|n} d c_d`, `Z(T) = prod_d (1-T^d)^{-c_d}`, which is the real case.
- Lead: the hardness moves to a question about the *counts*: is `fix(sigma^n)` a finite sum of exponentials, i.e. is `Z(T)` rational?
- Related: L01-011, L01-012

### L01-011 The key surprise: the small matrix's eigenvalues are NOT on the unit circle
- Source: `transcript/transcript.md`:314-316
- Raised by: orchestrator (Claude)
- Status at last mention: settled, and it reshaped the statement of RH used throughout
- Content: for `x -> x^2` on the closure of `F_2`, `fix(sigma^n) = 2^n`, so the small matrix is `[2]`. The infinite permutation matrix was unitary; its finite replacement is not. So "RH = unit circle" cannot survive. What replaces it for a curve: the finite matrix is block diagonal with block `w` equal to `q^{w/2}` times a unitary.
- Lead: restate RH as a constraint on the *radii* of the small matrix's eigenvalues relative to the leading one.
- Related: L01-013, L01-102

### L01-012 Which infinite permutations have rational `Z`, and the realisability question
- Source: `transcript/transcript.md`:400, 404-417
- Raised by: TJO
- Status at last mention: partially explored; "fully understood for order-2 recurrences and open in general"
- Content: rational cases are shifts of finite type (Bowen-Lanford 1970), sofic shifts (Manning 1971, Coven-Paul - the first place where numerator and denominator, bosons and fermions, both appear), hyperbolic dynamics, and Frobenius on solution sets over finite fields (Dwork, Grothendieck). Non-rational is generic. Rationality is equivalent to a linear recurrence for `fix(sigma^n)`, but not every linear recurrence is realisable: one needs `sum_{d|n} mu(n/d) fix(sigma^d) = 0 mod n` with nonnegative quotient. Lucas numbers are realisable (hence permutation 2 exists), Fibonacci numbers are not (Puri-Ward 2001; Everest-van der Poorten-Puri-Ward 2002).
- Lead: "which infinite permutations have rational Z" reduces to an arithmetic question about integer sequences, open in general. Nobody in the notebook returned to it.
- Related: L01-013, L01-010

### L01-013 Permutation 3: the elementary example where the RH property actually holds
- Source: `transcript/transcript.md`:338-352; `notes/what-rh-has-become.md`:39
- Raised by: orchestrator (Claude), computed in-session
- Status at last mention: reused as the standard elementary example; feeds shard 06h
- Content: alphabet `{0,1,2,3}` with the rule "each symbol is followed by itself or the next one cyclically" gives a 4x4 counting matrix with eigenvalues `2, 1+i, 1-i, 0`, so `fix(sigma^n) = 2^n + (1+i)^n + (1-i)^n` and the subleading pair has modulus exactly `sqrt 2`. The golden-mean shift (rule "1 never followed by 1") has eigenvalues `phi, -1/phi` and fails: `phi^{-1} != sqrt(phi)`. So the RH-type property is a property some infinite permutations have and others lack.
- Lead: a laboratory for the question "what makes a system Ramanujan"; in the variable `T = e^{-s}` the poles sit at `Re s = log 2` and `Re s = (1/2) log 2`.
- Related: L01-011, L01-082

### L01-014 The zeta of an automaton / shift of finite type (Artin-Mazur, Bowen-Lanford) as the elementary frame
- Source: `transcript/transcript.md`:358, 362-376
- Raised by: TJO ("so I guess you are describing a kind of zeta for automata?")
- Status at last mention: adopted as the standing frame
- Content: `Z(T) = 1/det(1 - TA)` for the adjacency matrix `A`; cycles are closed paths, primes are primitive closed paths, `fix(sigma^n) = Tr A^n`. For a general graph the eigenvalues sit at any radii, so there is no RH for automata in general. Caveat recorded: "the automaton is not the object with the zeta function" - the permutation is the shift on accepted periodic sequences and the automaton only supplies the counting matrix.
- Lead: arithmetic examples are automaton-like objects for which the radius constraint is a theorem or a conjecture.
- Related: L01-013, L01-018

### L01-015 What the primes force on the hypothetical flow (the constraint table)
- Source: `transcript/transcript.md`:429-444
- Raised by: TJO ("what can be inferred about the automaton here?")
- Status at last mention: raised, used as a design specification, never systematically revisited
- Content: the object cannot be a permutation or finite automaton since `log p` are rationally independent; it is a flow with one primitive orbit per prime of period `log p`, so the alphabet is infinite and the primes are the natural candidate for it. Constraints translated: PNT gives entropy `h = 1`; the explicit-formula weight `log p . p^{-k/2}` says every orbit is hyperbolic with Lyapunov exponent exactly 1, uniformly; `N(T) ~ (T/2pi) log T` says the side-B operator is one-dimensional in character; the Gamma factor is an "orbit at infinity"; the sign says absorption.
- Lead: any candidate must be one-dimensional, uniformly hyperbolic with exponent 1, infinitely many symbols, absorption sign. This is a checklist for rejecting proposals.
- Related: L01-005, L01-016, L01-004

### L01-016 Selberg as the one family where all of it is realised, and its two mismatches
- Source: `transcript/transcript.md`:442-444, 456-474
- Raised by: orchestrator (Claude)
- Status at last mention: became a full sub-programme (shards 03e/03f, 09b/09c)
- Content: for a compact constant-negative-curvature surface, the primes are closed geodesics, the zeta is Selberg's, side B is the Laplacian with eigenvalues `1/4 + r_n^2`, and RH holds because the operator is self-adjoint. Two features do not match the primes: the Selberg zero count is `T^2` (a two-dimensional surface) against `T log T` for zeta, and the Selberg sign is the emission sign.
- Lead: the Riemann flow must be one-dimensional with absorption sign; that is "the current edge".
- Related: L01-015, L01-025, L01-069

### L01-017 The Ihara zeta of a finite regular graph as the "vestigial Selberg"
- Source: `transcript/transcript.md`:480, 492-522
- Raised by: TJO ("there must be an even simpler example than Selberg ... something continuous but exhibiting the phenomena in vestigial form")
- Status at last mention: adopted as the central elementary model of the whole project
- Content: for a `(q+1)`-regular graph, `Z(u) = 1/det(1-uT)` with `T` the non-backtracking edge matrix, and Ihara-Bass compresses to `det(1-uA+qu^2)`. Each vertex eigenvalue `lambda` gives `mu mu' = q`, so RH holds iff `|lambda| <= 2 sqrt q`, i.e. iff the graph is Ramanujan. `K_4` works; the prism `C_16 x K_2` has `lambda_2 = 2.848 > 2 sqrt 2` and two zeros move off the line to `0.67` and `0.33`.
- Lead: the graph case is the honest guide - side B, the trace identity and self-adjointness exist for every graph and most graphs still fail RH.
- Related: L01-018, L01-019, L01-103

### L01-018 TJO's instinct: the cohomology is a red herring
- Source: `transcript/transcript.md`:528, 532-553
- Raised by: TJO
- Status at last mention: confirmed in the form "existence of side B is cheap, the radius bound is the content"
- Content: the implied "cohomology" for a graph is explicit and cheap: Bass's decomposition gives `H^1`-with-Frobenius blocks `mu^2 - lambda mu + q`, `H^0`/`H^2` from `lambda = q+1`, and `2(m-n)` dimensions with eigenvalues `+-1` carrying the topological `H^1` (zeros at `Re s = 0`, like the trivial zeros). For Ihara's arithmetic graphs, `A` is the Hecke operator `T_p` and the 2-dimensional blocks *are* the Frobenius action on `H^1` by Eichler-Shimura. Conclusion: "cohomology as the space on which the small matrix acts is not where the difficulty lives"; the radius bound always comes from elsewhere (Weil's Hodge index, Deligne's weights, Selberg's conjecture).
- Lead: stop looking for a Hilbert space; look for the mechanism that rules out exceptional eigenvalues. This steering survives to the end of the notebook.
- Related: L01-017, L01-113, L01-119

### L01-019 Ramanujan means tempered: no eigenvalue outside the spectrum of the universal cover
- Source: `transcript/transcript.md`:520; `notes/what-rh-has-become.md`:66
- Raised by: orchestrator (Claude)
- Status at last mention: reused as the definition that survives the continuum limit
- Content: `[-2 sqrt q, 2 sqrt q]` is the spectrum of `A` on the infinite `(q+1)`-regular tree, so the Ramanujan condition says the finite graph's eigenvalues sit inside the continuous spectrum of its infinite cover. The prism fails because its bottleneck produces a small-Laplacian-eigenvalue analogue; Selberg's exceptional eigenvalues below `1/4` are the continuous form.
- Lead: "tempered" is the right word, and it is what later became the continuum criterion for Harrow channels (L01-076).
- Related: L01-017, L01-076

### L01-020 TJO's old Shor idea: find the autonomous quantum system that realises Shor, use it as the PH candidate
- Source: `transcript/transcript.md`:559, 563-576; `HANDOFF.md`:762-764
- Raised by: TJO (crediting discussions with Wim van Dam, Atiyah, Jon Keating, Michael Berry)
- Status at last mention: pursued, largely negative; listed under "Ideas raised but not pursued"
- Content: Shor's `U_a: |x> -> |ax mod N>` is a finite permutation with all cycles of length `r = ord_N(a)`, so its zeta is trivially rational and RH is automatic - Shor carries no RH content by itself. What it does carry: it computes side B (the spectrum) without walking side A, which is the hard direction of the analogy. `U_a` sits inside Bost-Connes as the Galois action `gamma -> a gamma` on the phase operators; those commute with `H = log n`, so they are symmetries, not dynamics, and the Shor periods are governed by Dirichlet L-functions, not zeta (Artin's primitive-root conjecture is only known under GRH).
- Lead: `U_a = e^{i(log a)D}` restricted to a finite quotient; the PH operator `D` needs the whole family across all `a` and all levels at once. Concretely: at level `p`, `x -> ax` is `diag(a, a^{-1})` in `SL_2(F_p)` acting through the Weil representation - a direct tie to the parent campaign's SP-WEYL.
- Related: L01-021, L01-053, L01-060

### L01-021 The quantum expander (Hastings/Harrow) as a quantum Ihara object - TJO's proposal
- Source: `transcript/transcript.md`:582, 590-616; `HANDOFF.md`:702-706
- Raised by: TJO
- Status at last mention: registered and proved (HANDOFF item 1 and item 8; `scripts/qihara.py`, later the general Kraus theorem)
- Content: for a unital channel with `D` unitary Kraus operators closed under adjoint, define the quantum Hashimoto operator `T(rho (x) |i>) = sum_{j != i^{-1}} U_i rho U_i^dag (x) |j>` on `M_n (x) C^D`. Bass's proof goes through verbatim (it only uses source, target and the edge-reversal involution `J`), giving `det(1-uT) = (1-u^2)^{n^2(D-2)/2} det(1 - u D Phi + (D-1)u^2)`. Hence **RH for this zeta iff `Phi` is a Ramanujan quantum expander in Hastings' sense**. Unitarity is essential: `J^2 = 1` fails for non-unitary Kraus operators.
- Lead: this is the theorem that made "RH is a Ramanujan property" precise; it opened the quantum-expander literature as a laboratory.
- Related: L01-022, L01-023, L01-038, L01-096

### L01-022 Do exactly-Ramanujan quantum expanders exist at fixed `D`?
- Source: `transcript/transcript.md`:614
- Raised by: orchestrator (Claude), flagged as unknown from memory
- Status at last mention: raised, not pursued in this lane
- Content: random examples split (at `n=3, D=4` the second eigenvalue was 3.62 against the bound 3.46, RH fails; at `n=4, D=6` it was 3.59 against 4.47, RH holds). Hastings shows random unitaries are asymptotically Ramanujan, the quantum counterpart of Friedman. But "the classical constructions, Lubotzky-Phillips-Sarnak and Marcus-Spielman-Srivastava, do not obviously quantise."
- Lead: the LPS question was later answered by Harrow's construction (L01-038); the MSS question was never attempted. Consequence if MSS quantised: an exactly-Ramanujan family with no arithmetic input.
- Related: L01-038, L01-039

### L01-023 The quantum expander zeta is an Artin-Ihara L-function of a free group
- Source: `transcript/transcript.md`:616, 660
- Raised by: orchestrator (Claude)
- Status at last mention: identified; the prior-art check later confirmed Matsuura-Ohta had the Ad-weighted case
- Content: the vertex space `M_n` carries the adjoint representation of the free group `F_{D/2}` via `g_i -> U_i . U_i^dag`, so `zeta_Phi` is the Artin-Ihara (Stark-Terras) L-function of the bouquet graph with `D/2` loops twisted by that representation. Classical Ihara is the sub-L-function on the diagonal subalgebra when the `U_i` are permutations.
- Lead: "read the Artin-Ihara twist as a representation choice" - G-injective MPS give twists by genuine group representations, where the L-function factors over irreps.
- Related: L01-026, L01-096, L01-116

### L01-024 Side A of the quantum expander: primes are primitive words with real non-integer multiplicities
- Source: `transcript/transcript.md`:618-624
- Raised by: orchestrator (Claude)
- Status at last mention: raised, connected to Hastings' proof technique, not pursued further
- Content: `Tr(T^n) = sum over cyclically reduced words w of length n of |Tr U_w|^2`. So the gas has one mode per primitive conjugacy class of the free group, with energy its length and a weight given by the character. "That is closer to a Selberg zeta with a unitary twist than to a graph."
- Lead: the RH question becomes a question about how the character values `|Tr U_w|^2` are distributed over long words - which is what Hastings' proof controls. Nobody followed this route.
- Related: L01-021, L01-023

### L01-025 The channel IS an MPS transfer matrix; the zeta is the generating function of ring norms
- Source: `transcript/transcript.md`:630, 634-654
- Raised by: TJO ("I was rather expecting to connect this to matrix product states")
- Status at last mention: adopted as the notebook's core dictionary
- Content: for MPS tensors `A_i`, `E = sum_i A_i (x) conj A_i`, and `Tr(E^n) = sum_{words} |Tr A_w|^2 = <psi_n|psi_n>`, the norm of the periodic MPS on `n` sites. So `zeta_A(u) = 1/det(1-uE) = exp(sum_n <psi_n|psi_n> u^n/n)` is the generating function of ring norms, and this is Ruelle's dynamical zeta of a 1D lattice model with the transfer matrix replaced by an MPS transfer matrix. Non-backtracking is a nearest-neighbour hard constraint, so the quantum Ihara zeta is a constrained-MPS ring-norm generating function.
- Lead: "the closed walk count of the graph is the squared norm of the ring state" - this identification drives everything afterwards.
- Related: L01-021, L01-026, L01-027

### L01-026 AKLT is `K_4`
- Source: `transcript/transcript.md`:652
- Raised by: orchestrator (Claude)
- Status at last mention: verified by hand in-session; a permanent sanity example
- Content: the AKLT tensors are the three Paulis over `sqrt 3`, so `D = 3`, `q = 2`, and `D Phi` on `M_2` has spectrum `3, -1, -1, -1`, exactly `K_4`'s adjacency spectrum (the Paulis mod phase form the Klein four-group whose Cayley graph on all three non-identity elements is `K_4`). Hence the non-backtracking ring gas of AKLT has the Ihara zeta of `K_4` and satisfies RH. Checked by hand at length 3: six cyclically reduced Pauli words, each `|Tr sigma_x sigma_y sigma_z|^2 = 4`, total 24 = closed non-backtracking walks of length 3 on `K_4`.
- Lead: physical states with known entanglement structure are Ramanujan objects; a bridge between condensed matter and the zeta side.
- Related: L01-025, L01-078

### L01-027 Three levers for "new quantisations" of Ihara
- Source: `transcript/transcript.md`:656-660
- Raised by: orchestrator (Claude), answering TJO
- Status at last mention: lever 1 partially pursued (general Kraus theorem, item 8); levers 2 and 3 raised, not pursued
- Content: (1) drop unitarity - general canonical-form Kraus operators give the directed zeta `1/det(1-uE)` with no Bass factorisation since edge reversal is no longer an involution; the gas picture survives. (2) change the constraint - non-backtracking is one classical automaton on physical indices; any local constraint gives a different zeta, and Bass factorisation is the special property of the reversal-symmetric one. (3) read the twist as a representation choice - G-injective MPS give genuine group representations and the L-function factors over irreps.
- Lead: lever 1 became item 8 (Ihara-Bass for arbitrary Kraus families) and item 10 (the Kraus dichotomy). Levers 2 and 3 remain open experiments.
- Related: L01-023, L01-096, L01-097

### L01-028 The gas of rings as a direct sum over sizes, and the two Fock descriptions
- Source: `transcript/transcript.md`:666, 670-705
- Raised by: TJO ("the gas of pbc systems lives naturally in a fock-type space where we use direct sum as 'or'")
- Status at last mention: settled with one correction, and reused
- Content: correction: the direct sum over sizes `H_1 = (+)_n (C^D)^{(x)n}` is the *single-particle* space, not the gas; the gas is the symmetric Fock space over it, and the `1/n` is the rotation orbifold weight. The same zeta has a second Fock reading on the bond side: `zeta(u) = 1/det(1 - u e^{-H_T})` with `H_T = -log E` on the doubled bond, an ideal Bose gas whose single-particle Hamiltonian is `H_T` and where `n` is a *winding number*. The Euler product makes the modes explicit as `(v, a, b)` with energy `|v|` and weight `alpha_a(v) conj alpha_b(v)` (for unitary Kraus operators, a phase, i.e. an imaginary chemical potential).
- Lead: "one partition function, two Fock spaces" - the BC/Hilbert-Polya swap in a setting where both sides exist and are finite.
- Related: L01-025, L01-029

### L01-029 MPS gas and Bost-Connes are the free and the commutative versions of one construction
- Source: `transcript/transcript.md`:705
- Raised by: orchestrator (Claude), as a "structural remark for later"
- Status at last mention: raised once, never followed up
- Content: `(+)_n (C^D)^{(x)n}` without the rotation quotient is the full Fock space of `D` generators, and `S_i -> A_i` is a representation of the Cuntz algebra `O_D` (Fannes-Nachtergaele-Werner's original construction of finitely correlated states). By Cuntz and Laca-Raeburn, the Bost-Connes algebra is a Cuntz-type algebra for the semigroup `N` under multiplication, whose Fock space is symmetric rather than free because integers are multisets of primes, not words. "necklaces sit in between."
- Lead: none stated. Possible: build the Riemann object as an intermediate (necklace) algebra between `O_D` and BC.
- Related: L01-025, L01-028

### L01-030 The cMPS limit of Ihara loses the primes; length quantisation needs hyperbolicity
- Source: `transcript/transcript.md`:711, 715-748
- Raised by: TJO ("evidently MPS get replaced by cMPS and we should have one side being a QFT")
- Status at last mention: partially explored; TJO pushed back on the QFT framing
- Content: plain cMPS replaces `E` by `e^{LT}` with `T` a Lindbladian on the doubled bond; `zeta(s) = 1/det(s-T)` after Schwinger proper time, so side B is an open system whose zeros are the Lindbladian spectrum. What it loses: the primes. "In the continuum the ring length is a free real parameter and the product over primes dissolves into `int dL/L`." Selberg's lengths are discrete because rings are closed geodesics and hyperbolicity isolates them. The full dictionary: MPS matrices -> flat `U(chi)` connection, `Tr A_w` -> holonomy character, quantum Ihara zeta -> twisted Selberg zeta, Ihara-Bass -> twisted Laplacian, Ramanujan -> no eigenvalue below `1/4`.
- Lead: two things do not carry over and are "the fingerprints of hyperbolicity" - the length is fixed by geometry rather than summed freely, and the `prod_k` tower has no MPS counterpart because a bond space has no transverse direction. "Both are what a quantisation of Ihara would have to invent to reach Selberg."
- Related: L01-031, L01-032, L01-069

### L01-031 Selberg zeta as a one-loop QFT determinant with geodesics as worldline instantons
- Source: `transcript/transcript.md`:740-748; `HANDOFF.md`:757-761
- Raised by: orchestrator (Claude), citing D'Hoker-Phong and Sarnak
- Status at last mention: raised, not pursued; TJO flagged it as going too far
- Content: `det(Delta_rho + s(s-1)) = Z(s,rho) x (elementary factors)`; the worldline expansion of `log det` localises by the Selberg trace formula onto closed geodesics with windings, and the transverse fluctuations produce the `prod_k` tower. So the Bose gas of primes is the worldline gas of the QFT, and the trace identity is one-loop perturbation theory.
- Lead: recorded in HANDOFF under "Ideas raised but not pursued".
- Related: L01-030, L01-032

### L01-032 "Length quantisation is a flatness condition" - TJO's guess, later matched by the product formula
- Source: `transcript/transcript.md`:754, 864; `HANDOFF.md`:757-761
- Raised by: TJO
- Status at last mention: matched, then not developed further
- Content: TJO rejected the functional-integral framing and guessed that the quantisation of ring lengths is "some kind of flatness condition". The later match: for each prime's ring to close at length `log p`, the archimedean stretch must be undone by the p-adic places, and it is, because `prod_v |p|_v = 1`. "The product formula is the flatness condition you were guessing at."
- Lead: the space on which each prime is a closed ring of its own length is the adele class quotient `Q^x \ A`.
- Related: L01-030, L01-036

### L01-033 Bost-Connes as a matrix-product operator over the chain of primes
- Source: `transcript/transcript.md`:754, 762-801; `HANDOFF.md`:707-712
- Raised by: TJO ("here we also have a way to start talking about both sides via MPS. Please develop that carefully")
- Status at last mention: registered and verified (`scripts/bcmpo.py`, HANDOFF item 2)
- Content: sites are the primes; `l^2(N)` is the tensor product along the chain; the Gibbs state is a *product state* of bond dimension 1; `mu_n` is a product of single-site shifts. The content is in the phase operators: `e(a/b)` is an MPO with bond space `Z/b`, local tensor `r -> p^{k_p} r mod b` (which is Shor's map), boundary vectors "start at `r=1`" and "read out `e^{2 pi i a r/b}`". Dirichlet characters diagonalise all the transfer matrices, with eigenvalues `lambda_chi(beta) = L(beta, conj chi)/zeta(beta)`. Extremal KMS states differ only in the boundary vector; as `beta -> 1+` every nontrivial sector collapses, which is the BC phase transition.
- Lead: "the coupling that BC adds is exactly the residue bond space `Z/b`", so DG-GLOBAL's inter-prime maps have to reproduce `r -> p^k r mod b`. A checkable target.
- Related: L01-020, L01-034, L01-049

### L01-034 BC is "one derivative short": the L-functions are the transfer eigenvalues, not the zeros
- Source: `transcript/transcript.md`:799
- Raised by: orchestrator (Claude)
- Status at last mention: recorded as a structural diagnosis
- Content: in the MPS-ring picture the transfer eigenvalues *are* the zeros; in the BC MPO the eigenvalues are the L-functions themselves, so the critical line is a statement about analytic continuation of transfer eigenvalues in the temperature, not yet a spectrum.
- Lead: the fix is to find the object where the transfer spectrum is the zeros - which is what TJO asked for next.
- Related: L01-033, L01-035

### L01-035 "An MPS whose transfer generator has the Riemann zeros as its spectrum, and whose rings are the primes"
- Source: `transcript/transcript.md`:807, 811-842; `HANDOFF.md`:53-66
- Raised by: TJO ("surely to get any sensible entanglement hamiltonian we need entanglement ... what we are looking for is an interesting MPS with nontrivial entanglement hamiltonian")
- Status at last mention: this became the Phantasm and the central priority of the whole repository
- Content: forced features, each already determined: (a) lengths `log n` are incommensurate so it is a cMPS, `e^{LT}`; (b) the ring-norm measure is fixed by the explicit formula, `Tr e^{LT} = sum_n Lambda(n) delta(L - log n) + smooth`; (c) the spectrum of `T` is the zeros, so the bond is infinite-dimensional; (d) crucially, `e^{LT}` is the transfer map of a state, so `T` must generate a completely positive semigroup - a Lindbladian. The hierarchy: PNT = Perron-Frobenius primitivity; RH = all nontrivial eigenvalues have `Re lambda = -1/2`, one correlation length `xi = 2` with an infinite tower of frequencies.
- Lead: "What is not determined: the physical index." The open problem is the inverse problem "find the tensors from the ring spectrum". Finite bond dimension gives smooth ring norms, so the infinite tower is unavoidable; the natural candidate bond algebra is BC itself.
- Related: L01-036, L01-042, L01-057

### L01-036 The bond space of the sought cMPS is the adele class group, reached from the MPS side
- Source: `transcript/transcript.md`:840, 862-873
- Raised by: orchestrator (Claude)
- Status at last mention: raised and reused as the standing guess for the bond
- Content: taking all `b` together puts `Zhat` on the bond; adding the archimedean place (the continuous length direction) gives the idele class group, so the bond is functions on `Q^x \ A^x` and `T` generates scaling - Connes's adele class space, "arrived at from the MPS side, with the bonus that the MPS picture demands `T` be a Lindbladian and demands ring-norm positivity, which is the shape of Weil's positivity criterion."
- Lead: the MPS framing adds two *constraints* Connes's framing does not have: complete positivity and ring-norm positivity.
- Related: L01-032, L01-035, L01-098

### L01-037 The circle of circumference `log p` as the local bond, and why it has no expansion
- Source: `transcript/transcript.md`:854-860; `HANDOFF.md`:849-856
- Raised by: orchestrator (Claude)
- Status at last mention: settled negative; recorded as the "circle flows" discussion
- Content: rotation by `L` on `L^2(R/(log p)Z)` has trace `log p . sum_k delta(L - k log p)` by Poisson summation, so the direct sum over primes reproduces `sum_n Lambda(n) delta(L - log n)` exactly. But its spectrum is `2 pi i m/log p`, all on the imaginary axis, decay rate 0: a disjoint union of cycles with no expansion at all. For finite prime sets the spectrum is just the poles of the partial Euler product; **zeros exist only in the infinite product**.
- Lead (negative): "Prime-by-prime ansaetze (direct sums, commuting dilations) cannot see zeros." Any construction must couple the primes.
- Related: L01-039, L01-101, L01-117

### L01-038 Lax-Phillips as the compression that makes the expander, and the Stinespring question
- Source: `transcript/transcript.md`:862-875, 1007-1016; `HANDOFF.md`:713-717, 931-935
- Raised by: orchestrator (Claude); the Stinespring question is the repo's founding open problem
- Content: compress the dilation semigroup to the orthogonal complement of the trivial sector; this is exactly Lax-Phillips on the modular surface, where the compressed evolution `Z(t)` is a contraction semigroup whose spectrum is cusp-form frequencies plus resonances at the zeros. Faddeev-Pavlov (1972): RH iff `Z(t)` decays at one uniform exponential rate. Verified numerically: `S(tau) = xi(1-2i tau)/xi(1+2i tau)` is unimodular, inner, with zeros at `gamma_n/2 - i beta_n/2`, and its phase is exactly the imaginary part of the BC Levy exponent at `beta = 1`.
- Lead: **the open question.** "Whether the Lax-Phillips semigroup admits a Stinespring form with the compressed prime dilations as Kraus operators, so that the modular surface's bond algebra becomes a genuine channel." If it does, RH becomes a Ramanujan bound for a specific quantum expander and the physical index is whatever the Stinespring dilation adds. Suggested as a blind codex lane with the note as the only input.
- Related: L01-036, L01-041, L01-107

### L01-039 Lift Werner/Holevo dilation results for semigroups - TJO's proposal
- Source: `transcript/transcript.md`:881, 885-905; `HANDOFF.md`:765-768
- Raised by: TJO ("reinhard werner and alexander holevo variously worked on stinesprings of semigroups. I bet we can just lift their results")
- Status at last mention: partially explored; "probably yes for the form of the object, and provably no for the hard part"
- Content: Holevo's classification of covariant quantum dynamical semigroups gives a Levy-Khinchin form (Hamiltonian + Gaussian + jump part with a Levy measure on `G`). With `G = R_+^x`, Khinchin's fact that the zeta distribution is infinitely divisible makes `log N` compound Poisson with jumps `k log p` at rate `p^{-k sigma}/k`, so `E[N^{i tau}] = zeta(sigma - i tau)/zeta(sigma)`. Three consequences: the semigroup is a Mellin multiplier with symbol `(zeta(sigma-i tau)/zeta(sigma))^t`, so zeta on vertical lines *is* the spectrum and the zeros are frequencies the semigroup kills; the Levy measure has finite mass iff `sigma > 1`, so the BC transition is the compound-Poisson/infinite-activity threshold; the Gaussian part is the archimedean place (Tate). Caveat recorded: "I would want to check the exact Werner reference you have in mind"; the Tuebingen Markov-dilation results are Kuemmerer's.
- Lead: "Write Holevo's generator for `G = R_+^x` with the von Mangoldt jump measure and the Gamma-factor Gaussian part ... then study what compression of that semigroup reproduces the Lax-Phillips resonances. If the two agree on a co-invariant subspace, that subspace is the bond space of the cMPS, and its physical index is the Stinespring environment." Where the lift stops: dilation theorems give existence, not positivity; Weil's criterion is exactly "F admits a GNS representation on the dilation group".
- Related: L01-038, L01-108, L01-098

### L01-040 The Holevo-form generator lives on the wrong space (the two placements are different objects)
- Source: `transcript/transcript.md`:1016; `notes/riemann-channel-note.md`:79-87
- Raised by: orchestrator (Claude)
- Status at last mention: recorded as the precise shape of the open problem
- Content: "A Holevo-form Lindbladian with the primes as jump operators lives on the full regular representation, has symbol `zeta^t`, and is not the compressed object." It is a genuine Markov semigroup only for `sigma > 1`, has no zeros there, and at `sigma = 1/2` is not a semigroup at all (the symbol is unbounded).
- Lead: whether a jump-type generator on `K_S` reproduces `Z(t)` - "a negative answer with a reason is a result".
- Related: L01-038, L01-039, L01-107

### L01-041 TJO's correction: entanglement Hamiltonians are always Hermitian - where did we lose that?
- Source: `transcript/transcript.md`:1164, 1168-1182, 1202; `notes/what-rh-has-become.md`:178, 182
- Raised by: TJO
- Status at last mention: corrected in the notes; the corrected slogan is used everywhere afterwards
- Content: two operators had been given one name. The entanglement Hamiltonian of an MPS is built from the *fixed points* of `E` alone, is Hermitian and blind to the subleading spectrum. The object carrying the zeros is the transfer generator, which is genuinely non-Hermitian and must be, since the imaginary parts of the zeros are oscillation frequencies of the prime counts. The correct slogan: write `T = -1/2 + iH` on the subleading sector; then `H` has eigenvalues `gamma - i(beta - 1/2)`, so **RH says `H` is Hermitian**, and `H` is Hilbert-Polya's operator.
- Lead: a caveat that matters - "on the Lax-Phillips model space the eigenvectors are Cauchy kernels and are not orthogonal, so RH gives the spectrum on a circle, not literally `Z(t) = e^{-t/4} U(t)` with `U` unitary. A self-adjoint Hilbert-Polya operator would give the stronger form." This later became the Riesz-basis dead route.
- Related: L01-095, L01-105, L01-089

### L01-042 The Bost-Connes reframe: dilation time is the 1D space of a cMPS (central priority)
- Source: `HANDOFF.md`:53-66
- Raised by: TJO (steering, 2026-09-12 evening)
- Status at last mention: **CENTRAL PRIORITY**, programme items 0a'-0f
- Content: the reframe in one sentence: "dilation time is the one-dimensional space of a cMPS; the bond carries the Riemann Lindbladian; its unique fixed point is the pole at `s = 1`, i.e. the critical KMS_1 state; the zeros are its relaxation modes; the physical cMPS is pure and the KMS state is its entanglement spectrum." The Gibbs states at `beta > 1` are the symmetry-broken steady-state manifold labelled by the Galois group, and the BC phase transition is ergodicity breaking of the Lindbladian. RH is the uniform-rate statement after the `e^{-t/4}` rescaling: a "Riemann quantum expander".
- Lead: everything numbered 0a'-0f in the HANDOFF is an attempt on this.
- Related: L01-035, L01-043, L01-044

### L01-043 The fermionic zeros: the bond must be `Z_2`-graded and the ring norm is a supertrace
- Source: `HANDOFF.md`:68-78; `notes/what-rh-has-become.md`:120
- Raised by: orchestrator (Claude), forced by a conflict; endorsed and extended by TJO
- Status at last mention: registered (thm:cmps-ring-norms, shard 07; shards 02f/04e/04f)
- Content: a cMPS ring norm is a positive sum of squares, but the zeros enter the explicit formula with a minus sign (confirmed by the `-2 Lambda(n) n^{-1/2}` dips). So the bond must be graded: the pole is the bosonic sector carrying the fixed point, the zeros are fermionic modes, and the ring norm is a supertrace - the ordinary norm of a fermionic ring with its parity insertion. This is the curve picture (`H^1` odd, counts `1 + q^n - sum alpha^n`) and the Artin-Schreier lane already carries the sign.
- Lead: TJO: "the Weil conjectures should have the same fermionic interpretation; pursue the analogies concretely and rigorously." This launched the ring-norm-tensor campaign.
- Related: L01-005, L01-062, L01-075, L01-084

### L01-044 The two Lindbladians are complementary halves; the Phantasm needs both
- Source: `HANDOFF.md`:88-104
- Raised by: orchestrator/prover during the 2026-09-12 "riemann-cmps" campaign
- Status at last mention: registered as obs:complementary-halves and conj:phantasm-both-halves (replacing item 0b)
- Content: the vacuum-decay Lindbladian on `B(C (+) K_S)` is a genuine CPTP semigroup with zeros as odd coherences, pair sums as even populations, and a PURE stationary vacuum; but the vacuum is absorbing (the renewal integral diverges), so the SHW rebound state cannot be the vacuum. The prime-chain detailed-balance Lindbladian has a Gibbs fixed point, real spectrum (Minkowski sums of M/M/1 bands) and no zeros; normal KMS states only for `beta > 1`.
- Lead: item 0b' - the SHW renewal equation with a MIXED rebound state `Omega` on `K_S`; the obstacle is the missing identification of `K_S` with the Bost-Connes bond.
- Related: L01-042, L01-046, L01-058

### L01-045 Rigidity: the supertrace of a graded generator determines its net graded spectrum
- Source: `HANDOFF.md`:83-87, 122-124
- Raised by: codex prover, reviewed by Opus (0 INVALID, 5 MINOR applied)
- Status at last mention: proved for finite parity flips; infinite flips OPEN (item 0c', obs:parity-infinite-open)
- Content: the explicit formula forces the pole even and the zeros odd, with finite parity flips excluded by positivity. The infinite case is the gap: "the prover isolated the missing step (negative mass at prime-power atoms of `mu - comb`)".
- Lead: "a positivity-alone argument or a counterexample-shaped obstruction". If it closed, the grading would be forced rather than assumed.
- Related: L01-043, L01-046

### L01-046 The no-go: no trace-class operator has a genus >= 1 point count as its trace sequence
- Source: `HANDOFF.md`:87-90
- Raised by: codex prover
- Status at last mention: proved (reviewed)
- Content: no finite or trace-class operator has a genus >= 1 point count as trace sequence, so no bosonic MPS ring norm can, and a zeta numerator is exactly an odd sector. Combined with the realisation on `C_+ (+) (K_S (+) ladder)_-` where `0 (+) B (+) diag(-(k+1/2))` has supertrace exactly `2 P_+`.
- Lead: this is the theorem that makes the grading unavoidable rather than aesthetic.
- Related: L01-043, L01-075, L01-084

### L01-047 The bond fixed point IS the entanglement spectrum (TJO's steering)
- Source: `HANDOFF.md`:106-110
- Raised by: TJO
- Status at last mention: adopted; `scripts/bc_entropy.py`
- Content: so the Gibbs entropy and its cutoff laws are entanglement data. Recorded finding: Hagedorn level density, and explicitly "no CFT reading".
- Lead: none beyond the script; the Hagedorn observation was not developed.
- Related: L01-042, L01-048

### L01-048 The Phantasm must carry `Zhat^x = Gal(Q^ab/Q)`
- Source: `HANDOFF.md`:108-110
- Raised by: TJO
- Status at last mention: registered as conj:galois-graded-bond
- Content: the Galois requirement gives the trivial-versus-nontrivial character reading of the grading: the even sector is the trivial character, the odd sectors are the nontrivial ones.
- Lead: item 0a' below.
- Related: L01-049, L01-033

### L01-049 Item 0a': the `Gamma_0(N)` model space
- Source: `HANDOFF.md`:113-117
- Raised by: orchestrator, as the first item of the central programme
- Status at last mention: OPEN, not started; explicitly "the Gamma_0(N) scattering/character calculation above remains OPEN"
- Content: compute the scattering determinant of `Gamma_0(N)` (Dirichlet L-functions by character), the exit space `C^h`, and check that the Shor map acts on the bond as the level-`N` Galois symmetry with the `L(s,chi)` zeros in the `chi`-sectors. Numerics first at small `N`, then prover.
- Lead: if it works it identifies `K_S` with the BC bond by character decomposition, unblocking item 0b'.
- Related: L01-020, L01-033, L01-044, L01-048

### L01-050 Item 0d: the Mayer cusp tail
- Source: `HANDOFF.md`:125 (pointing to `notes/resonances/astra-freeassoc.md` section 3)
- Raised by: a codex free-association lane
- Status at last mention: "unchanged", i.e. raised and parked
- Content: listed as an open programme item with no further detail in this lane's files.
- Lead: none stated here.
- Related: L01-051, L01-052

### L01-051 Item 0e: Suzuki's prime-defined screw kernel
- Source: `HANDOFF.md`:126
- Raised by: a codex lane (section 16.3 of the same note)
- Status at last mention: "unchanged", parked
- Content: listed as an open programme item; Suzuki 2022's kernel form of Weil positivity is separately cited at `HANDOFF.md`:842.
- Lead: none stated here.
- Related: L01-050, L01-098

### L01-052 Item 0f: literature to read (Bonthonneau-Weich; Lewis-Zagier; Chang-Mayer)
- Source: `HANDOFF.md`:127
- Raised by: orchestrator
- Status at last mention: "unchanged", not fetched
- Content: three literature pointers kept on the programme list, presumably for cusp resonance theory and the transfer-operator approach to Maass forms.
- Lead: none stated; relevant to the H-CUSP-BRIDGE obstacle.
- Related: L01-069, L01-050

### L01-053 The zeta-spectral-triples sidequest (Connes-Consani-Moscovici) and `zst`
- Source: `HANDOFF.md`:129-186
- Raised by: TJO (asked for a careful reading and a plan for an arb/FLINT implementation)
- Status at last mention: MVP done (`zst/`), benchmark to `x = 50` certified, TJO asked to wind up
- Content: the algorithm uses a window `[lambda^{-1}, lambda]`, `2N+1` Fourier modes, a Weil form matrix of Loewner form `(b_n - b_m)/(n-m)`, and gets the spectrum as real zeros of `sum_j xi_j/(j-s)`. Findings: a typo in the paper's displayed constant `c(L)`; the secular function has several roots per pole interval so root isolation must use the `2N` count; the accuracy law `|z_1 - gamma_1| ~ 5e4 (1 - chi_4(lambda))`, about 5.5 digits per unit `lambda^2`; later `e^{-4 pi x}`, `N` saturating at `7.5 x`, error at height `gamma` growing like `10^{0.37 gamma}`.
- Lead: **the extensibility idea**: "input = abstract explicit-formula distribution (atoms, exponential-series kernels, trivial-divisor poles, identity shift) so Dirichlet/Hecke/GL(2), graph and curve transfer operators, Selberg compact and modular (H-CUSP-BRIDGE test), and the notebook's graded divisor formulation run through one pipeline." Next if pursued: M3 (general data model), the `(lambda,N)` accuracy map and the `x = 100` run (not completed, memory), then `det_reg -> Xi` and the prolate side (M5).
- Related: L01-054, L01-055, L01-069

### L01-054 MVP-2: the Ihara zeta of graphs as a test of what in CCM generalises
- Source: `HANDOFF.md`:158-176
- Raised by: TJO
- Status at last mention: built the same night (`ihz/`, G1-G3 done, `make check` green)
- Content: the linear algebra generalises verbatim (Toeplitz Weil form, cyclic-shift displacement, a new unitary key lemma `U^* T U = T`, circle conclusion = Caratheodory-Fejer = Connes-van Suijlekom `corcar` = Makhoul 1981, `eps` = Pisarenko noise floor, Cayley transform). The analytic content does not: the finite divisor is exact at the critical window `K = R+1` and degenerate above, with no second truncation, no archimedean transcendental term, no prolate/Hermite structure - "the missing step of CCM has no graph counterpart". What the graph adds: the chain run on a *false* RH (`eps_M` diverges like `-m rho^{2M}`, `xi_min` goes odd, kernel still exact); RH enters only as `eps -> 0`, i.e. Weil's criterion. Sign flipped for graphs (poles) versus CCM's sign for curves.
- Lead: next if pursued - the `Q-2` under-resolved law from the bench data (with TJO); the anti-palindromic search (`Q-3`); fuzz and mutation; an Opus REFUTE review of `lanes/theory.md` before registering any claim; then M3/G5 (shared data model with `zst`).
- Related: L01-053, L01-055, L01-098

### L01-055 Shard 08g: the windowed Weil form as a compression, and the extension disc
- Source: `HANDOFF.md`:30-42
- Raised by: TJO's question ("can one estimate `tr(A^l)`, `l > K`, better than the chain does?")
- Status at last mention: answered in shard 08g, 45 checks, **unreviewed**
- Content: the window form is an exact compression and the chain's implicit higher-trace model is the Pisarenko extension. The admissible next trace fills a disc (Levinson centre, determinant-ratio radius, boundary = singular windows with `K+1` atoms by Caratheodory-Fejer), so positivity alone cannot beat it. The counts add `N >= 0` and a Newton congruence mod `K+1`, which pin the next trace of `(1 2)(3 4 5)` one lag before the critical window but nothing for the Petersen graph. For zeta the mean of the higher traces is the pole, already exact, so "better estimators mean more primes".
- Lead: **proposed, not run**: use the per-window disc radius in `ihz`/`zst` as a rigorous ignorance measure against the observed `e^{-4 pi x}` convergence.
- Related: L01-053, L01-054, L01-008

### L01-056 The Selberg zeta as a graded transfer whose odd-block form is derived from the letters
- Source: `HANDOFF.md`:188-232
- Raised by: TJO asked for "the most consequential step toward a proof"; orchestrator recommended and executed
- Status at last mention: registered (shards 03e, 03f), Opus-reviewed (no BLOCKER/MAJOR), 9 proved
- Content: `Z_S` is the ring zeta of the stable two-term transverse complex (even `-X`, odd `-X+1`): `Z_S(s) = D_tow(s-1)/D_tow(s)`, retained divisor all odd, functional equation unconditional, RH/Ramanujan iff Selberg's `1/4`. The Ruelle zeta (full transverse forms) FAILS both, because its even band is shifted by one. Closed geodesics are fermionic because `dim E_s = 1`.
- Lead: the "first band derived from the letters" theorem - `Omega = lambda(1+lambda)` on `Res^0`, reality from Haar, the positive form as the ORTHOGONAL sum of branchwise pullbacks (the total pullback is degenerate), operator functional equation `J X J^{-1} = 1 - X`, and a Jordan block at Laplace eigenvalue exactly `1/4` so that full operator Hilbert-Polya needs the strict bound.
- Related: L01-057, L01-069, L01-016

### L01-057 The finite Hashimoto-lift theorem: letter-derived metric settles "Hermitian channel + lift => odd block unitary"
- Source: `HANDOFF.md`:211-215
- Raised by: orchestrator/prover in the Selberg-letters lane
- Status at last mention: registered (thm:hashimoto-lift-metric, thm:letters-derived-finite)
- Content: for graphs and graded quantum Hashimoto lifts, an inverse pushforward `F_mu`, a companion model, and a letter-derived metric `G_C = [[1, S/2],[S/2, q]]` with `C^* G C = q G`, positive iff the band condition is STRICT. Exact endpoint counterexamples: `K_3 x Q_3`, and a ten-letter Pauli channel.
- Lead: it settles one of the standing open items in the inverse-paired setting; the general (non-inverse-paired) version is still open.
- Related: L01-056, L01-077, L01-097

### L01-058 Selberg negatives: no doubled-bond CP realisation; K-type parity is not a flow grading
- Source: `HANDOFF.md`:216-219
- Raised by: prover + Opus review
- Status at last mention: proved negative (prop:selberg-no-cp-realisation; prop:ktype-not-flow-grading)
- Content: flat supertraces are negative distributions, so no doubled-bond CP realisation exists; K-type parity does not supercancel and obs:selberg-grading-choice was corrected. Also, the first-band operator form of the continuous Ihara-Bass is proved but the full-tower compression is not (prop:selberg-ladder-ihara).
- Lead: do not look for a Kraus/CP realisation of the Selberg graded transfer by doubling the bond.
- Related: L01-077, L01-056

### L01-059 The modular obstacle H-CUSP-BRIDGE: the `-3/4` versus `-1/4` centre mismatch
- Source: `HANDOFF.md`:220-232
- Raised by: orchestrator, sharpened by the prover and Opus review
- Status at last mention: OPEN (obs:modular-scattering-sector)
- Content: on `PSL_2(Z)` the Riemann zeros `rho/2` are Selberg zeros (FJS divisor theorem, byte-checked), but their first-band states push to Eisenstein Laurent coefficients outside `L^2`, so the Haar form is unavailable. "the orchestrator's `e^{t/2}` rescaling was the WRONG rate (that sector's centre is `-3/4` under RH; the Riemann model's `-1/4` belongs to `-conj(rho)/2`; not identified)". Truncated Maass-Selberg norms are positive throughout the strip. Selberg's `1/4` for `PSL_2(Z)` is known (Booker-Lee-Strombergsson, reported, not byte-checked).
- Lead: the missing object is "a non-compact flow realisation with finite-rank resonant data at `rho/2 - 1` and a positive modal pairing at the correct centre". Three next steps: (1) DFG-type resonance theory for the modular flow (Dyatlov-Guillarmou cusp resonances) with Eisenstein Laurent data as first-band states; (2) identify or refute the affine relation between the scattering sector `-3/4` and the Riemann graded generator `-1/4` of shard 04b; (3) a positive form on regular data for the Eisenstein sector (Lax-Phillips, weighted).
- Related: L01-056, L01-042, L01-052

### L01-060 The Ramanujan property for graded transfer channels - TJO's quest item
- Source: `HANDOFF.md`:234-251
- Raised by: TJO ("a rigorous definition of the Ramanujan property from the graded MPS picture that survives the continuum limit, with Harrow expanders as the test; and whether we only have quantum expanders for ungraded bond space")
- Status at last mention: registered (shards 02h, 03c, 03d), all rows sketched, unreviewed
- Content: **Answer: yes, every quantum expander in the literature is ungraded, its ring zeta has only poles, and the two closures coincide** (prop:no-ungraded-zeros). Zeros are the odd-sector (parity-coherence) eigenvalues under the periodic closure. The definition (def:graded-rh-fe-ramanujan) is placed on the divisor `nu = m_even - m_odd` of `1/sdet(1-uE)`: growth `q` = Perron root; a trivial set; RH = one-sided `|lambda| <= sqrt q`; FE = even similarity `J E J^{-1} = q E^{-1}`; Ramanujan = both; manifest = `E/sqrt q` unitary for a `Gamma_b`-even positive form.
- Lead: for infinite bonds the object is the divisor of correlation functions of regular data, not the `L^2` spectrum (obs:divisor-regular-data) - a decisive technical choice.
- Related: L01-061, L01-063, L01-088

### L01-061 The P-mode is structural, not trivial (orchestrator's own mid-session correction)
- Source: `HANDOFF.md`:252-254
- Raised by: orchestrator (Claude), correcting itself
- Status at last mention: registered (prop:p-mode)
- Content: `sum_s eps_s A_s A_s^+ = r_P . 1` gives `E(P) = r_P P`; `r_P = 1` for the 06h tensor (`H^0`), `-2` for the Pauli letters (inside the band, a pole pair on the circle), `-(q+1)` when all letters are odd.
- Lead: the P-mode must be included in the trivial-divisor bookkeeping rather than discarded.
- Related: L01-060, L01-064

### L01-062 The Pauli qubit channel is an elliptic curve over `F_5`
- Source: `HANDOFF.md`:255-262
- Raised by: orchestrator/prover in the graded-Ramanujan lane
- Status at last mention: registered and verified (prop:qubit-graded-zeta, `scripts/graded_ramanujan.py`, 79 checks in CI)
- Content: the letters `X, X, Y, Y, Z, Z` on `C^{1|1}` give `(1+2u+5u^2)/((1-u)(1-5u))`, which is the zeta function of `y^2 = x^3 + 4x + b` over `F_5`. Also verified: graded Harrow expanders exist, using index-two (Clifford) gradings, with `Ad P` intertwining, Harrow's bound sector by sector, and graded Ihara-Bass whose `(1-u^2)^{n_k(D-2)/2}` factors cancel for balanced gradings; odd edge eigenvalues on `|mu| = sqrt q` are zeros. Verified on `PGL_2(F_5)` and `PGL_2(F_13)` principal series.
- Lead: the smallest possible concrete instance of "a quantum channel whose zeta is a curve's zeta" - a template for building more.
- Related: L01-060, L01-084, L01-086

### L01-063 Harrow's continuum limit: Ramanujan = temperedness
- Source: `HANDOFF.md`:263-266
- Raised by: orchestrator
- Status at last mention: registered (obs:graded-continuous-harrow)
- Content: the continuum limit is the representation Lindbladian; Ramanujan becomes temperedness of `pi (x) conj pi` (gap `1/2`), with no discrete divisor. The graded `PGL_2(R)` version gives discrete series pairs, odd sector = archimedean ladder, and closed geodesics come out EVEN. The grading that makes Selberg zeros odd is instead Dyatlov-Zworski's form degree.
- Lead: which Selberg grading is the Phantasm's remains open (see L01-064).
- Related: L01-019, L01-056, L01-064

### L01-064 Open items left by the graded-Ramanujan lane
- Source: `HANDOFF.md`:276-282
- Raised by: orchestrator and the codex prover
- Status at last mention: OPEN
- Content: (a) a circle-type graded expander from a representation, i.e. an odd block that is `sqrt q`-unitary by a mechanism (Artin-Schreier is the prototype); (b) a Kraus realisation of the Artin-Schreier / Riemann / Selberg graded *spectral* transfers, which currently have no supplied Kraus realisation; (c) the relation between "Hermitian + lift" and "odd block unitary"; (d) the Repka `3/4` threshold versus Selberg `3/16` (**unverified, do not cite**); (e) which Selberg grading is the Phantasm's.
- Lead: next if pursued - an Opus REFUTE review of 02h/03c/03d against the prover's file; then the K-type-0-versus-2 grading of a `PSL_2(R)` representation channel as the candidate form-degree grading.
- Related: L01-057, L01-063, L01-077

### L01-065 Prover corrections in the graded-Ramanujan lane (what was wrong)
- Source: `HANDOFF.md`:267-275
- Raised by: codex prover `gpt-6-astra` (4 proved, 9 corrected, 1 refuted, 41 ledger rows)
- Status at last mention: applied
- Content: the LPS "genus 18/98" was the raw odd count - only the NET divisor survives; there is **NO odd-sector Alon-Boppana** because the letter `P` kills the odd sector (obs:odd-gap-no-alon-boppana); "band iff circle" holds only for the net divisor; trivial data must be a signed divisor with parities; the continuum needs two reference rates; the distinction "graded CP transfer" versus "graded spectral transfer" matters because Artin-Schreier / Riemann / Selberg have no supplied Kraus realisation; the `PSL_2(R)` type-zero bound `>= 1/2` is EQUIVALENT to temperedness; `PGL_2(R)` pairs need even `k >= 2`; shard 05's "nontrivial zero" should have read "pole".
- Lead: the absence of an odd-sector Alon-Boppana bound is a genuinely useful negative - the odd sector has no automatic lower obstruction.
- Related: L01-060, L01-064

### L01-066 Back to basics: grading a cycle odd induces zeros, with two more knobs
- Source: `HANDOFF.md`:284-299
- Raised by: TJO (restarted from the permutation `(1 2)(3 4 5)`)
- Status at last mention: registered (shard 03b, 46 checks in CI), unreviewed
- Content: the gas equals oscillators by unique factorisation; `zeta = Tr u^N Gamma(P)` on the bond Fock space. Grading a cycle odd induces zeros under the Ramond closure (`1/sdet`), at the odd cycle's eigenvalues, with holonomy placing them; the untwisted closure has none; the pole at 1 is eaten unless a holonomy is used - "rigidity/net multiplicity in miniature".
- Lead/negative: a fermionic prime contributes `1 - u^l` for every `l`, and making all primes fermionic gives `1/zeta`, i.e. **Moebius as fermion parity, with zeros on `Re s = 0`, NOT the critical line**. (Later amended: this is per finite factor only.)
- Related: L01-008, L01-043, L01-073

### L01-067 The physical dimension principle: ring norms see the letters only through the channel
- Source: `HANDOFF.md`:300-306
- Raised by: orchestrator
- Status at last mention: registered (obs:physical-dimension-principle, prop:parity-jump-uniform-shift)
- Content: the lower bound on the number of letters is the Kraus rank (canonical up to a unitary), and one letter means the channel itself. The sign lives only in even-odd coherences of the doubled bond: letters that *record* the bond parity kill the zeros (worked out at `n = 6`: one letter gives 1, one per cycle gives 13, one per point gives 5). Partial recording at rate `gamma` shifts every odd eigenvalue by `-2 gamma` and no even one.
- Lead: this is "the letter-level form of the uniform-rate statement, `2 gamma = 1/4` is the `e^{-t/4}`". A mechanism for producing the uniform rate from a physical process.
- Related: L01-066, L01-068, L01-042

### L01-068 Jump operators of the Riemann cMPS: prime jumps versus Galois jumps (TJO's question)
- Source: `HANDOFF.md`:307-318; amended at 361-363
- Raised by: TJO
- Status at last mention: registered (obs:jump-operator-guidance), with one clause later amended by the yolo audit
- Content: Galois jumps (character-diagonal unitaries) give character dephasing: they set the uniform rate but cannot produce frequencies, and as a full per-step average they are a character measurement and remove the zeros. Prime jumps act on all character sectors and carry the lengths (the record), but alone give a real spectrum and no zeros. So the grading must be transverse to the primes, and the frequencies `gamma_n` need an even-odd Hamiltonian (or non-normal coupling) that neither family supplies. **Amendment from shard 04g: inversion-asymmetric Galois rates DO produce frequencies.**
- Lead: the ansatz shape - "prime jumps + Galois dephasing at `2 gamma = 1/4` + even-odd Hamiltonian; RH = the dissipation on the even-odd coherences is pure dephasing". Next: test (e) in the finite covariant cones of shard 04d - does Galois covariance + a character-dephasing Kossakowski block + BC stationarity leave exactly an even-odd Hamiltonian free?
- Related: L01-067, L01-073, L01-080

### L01-069 The zeta conditions imposed factor by factor (shard 06h catalogue)
- Source: `HANDOFF.md`:320-343
- Raised by: TJO, as "the complementary strategy after the negative"
- Status at last mention: registered (shard 06h, 461 checks re-run, 26 in CI), unreviewed
- Content: the smallest example is the pair shift on `m^2` letters with the diagonal odd, giving `Z = (1-mu)/(1-m^2 u)`: one zero at `q^{-1/2}` by half entropy, a genuine gas, no functional equation. Ledger C1-C10 splits the conditions into automatic (positivity, rationality, sign structure) and constraints (integrality, genuine gas, FE, RH, unique fixed point = simple Perron root + whole-bond TP gauge + mixing, Galois/Artin, realisability, continuum embedding). The catalogue: four-letter TP elliptic tensors on `C^{1|1}` (affine, projective, supersingular with a real double zero); a Pauli family proving FE/RH/mixing are independent; Horner MPS for Dirichlet L over `F_2[x]` and `F_3[x]`; Gauss and Kloosterman sums; a graph cover with reciprocal Bass quadratics; cMPS half entropy and amplitude damping with the additive FE `Z(2-z) = Z(z)`.
- Lead: the stated limit - "finite bond implies rational `Z`, no atomic prime comb, periodic copies of finitely many divisor points". Next if pursued: **a bond-cutoff family of four-letter-type tensors whose divisor points accumulate (the only route to non-rational behaviour)**, or the Selberg/Lax-Phillips side where the infinite object exists.
- Related: L01-062, L01-070, L01-088

### L01-070 Orchestrator errors caught in the zeta-conditions lane
- Source: `HANDOFF.md`:336-338
- Raised by: the codex lane, correcting the orchestrator
- Status at last mention: corrected
- Content: inverse-closed letters alone give no functional equation (`diag(1,2)` is the counterexample); the swap L-function is not an Artin factor; "unique fixed point" is three conditions, not one; the duality matrix for the elliptic tensor was wrong twice before `Z`-conjugation on the even block.
- Lead: none; recorded so the same mistakes are not repeated.
- Related: L01-069

### L01-071 The yolo Lindbladian - TJO's request for a bold guess - NEGATIVE
- Source: `HANDOFF.md`:345-368
- Raised by: TJO ("a bold guess of the Riemann Lindbladian from the circumstantial evidence")
- Status at last mention: **pursued, negative** (shard 04g), reviewed only by codex lanes
- Content: the guess was bond `L^2(Zhat) (x) L^2(R_+^*)`, grading by the profinite Fourier mode, one prime jump `V_p` per prime at rate `1/p`, Galois dephasing at `1/4`, archimedean ladder plus dilation Hamiltonian, with the Ramanujan-sum sector as the `K_S` identification. What holds exactly: the `V_p` isometries and their Galois covariance; the Ramanujan-shell formulas; `<c_b>_beta -> 0` iff `b > 1`; `prod_p (1 - p^{-w} V_p)` has vacuum element `1/zeta(w+1/2)`; uniform Galois dephasing. What fails, with exact counterexamples: the grading is not invariant; vacuum-character coherences are not modes; the vacuum generating functions are shifted with no singularity in the strip at any cutoff; shell Gibbs weights are not stationary; rates `1/p` define no normal semigroup; the parity ring trace is not a trace at a prime cutoff; parity closure is not the `Q^x` quotient.
- Lead: bearing - phase-side prime jumps are side A with the Fourier side included; **the Ramanujan-sum sector plus prime jumps alone is ruled out**. Next if pursued: an Opus REFUTE review of 04g; a summable-rate or radial local model with a genuine bond cutoff before any metric question.
- Related: L01-068, L01-044, L01-049

### L01-072 The ring-norm-tensor campaign: Tier A (ordinary elliptic curve) answers all five wish-list items
- Source: `HANDOFF.md`:370-394
- Raised by: TJO ("an educated guess for the MPS tensor of the absolute simplest variety without an obvious Polya-Hilbert Hamiltonian", with a five-item wish list)
- Status at last mention: registered (shards 02g, 06c-06f), Opus REFUTE reviewed, conditional on cited assumptions
- Content: reading - in this notebook the obvious PH Hamiltonian is the quadratic Artin-Schreier unitary `E_g`, but that family is supersingular in every characteristic (proved), so Tier A is the *ordinary* elliptic curve. There the natural tensor is the lifted Frobenius as a toral endomorphism `M` of `C/Lambda`; `N_n = det(1-M^n) = |1 - pi^n|^2 = |O/(pi^n - 1)|` is literally a ring norm and a Lefschetz number; the ket bond is `Lambda^*(H^{1,0}) = C^{1|1}`, the double is `H^*(T^2)`, the grading is form degree, ket/bra is the Hodge decomposition, and the pairing is `H^2` with eigenvalue `q` = the degree. The PH unitary is `q^{-1/2} M^*` on harmonic one-forms, unitary because the lift is a conformal similarity of degree `q`; positivity is the degree form and Hasse's bound follows. Gauge = lattice basis, classes = ideal classes (Latimer-MacDuffee, Waterhouse), unitary gauge = Hodge basis.
- Lead: this is the cleanest "everything present" instance on the curve side; the physical state is a product state and the Fourier pullback is an injection whose only finite orbit is the zero mode.
- Related: L01-043, L01-073, L01-125

### L01-073 Tier B (genus two) forces fermionic letters; the drafted bound was false
- Source: `HANDOFF.md`:395-413
- Raised by: orchestrator (drafted), corrected by both the prover and the numerics lane independently
- Status at last mention: registered with corrections; several items still open
- Content: the morning's drafted bound `sum_odd |mu|^2 <= 2 Tr(E_++) Tr(E_--)` is **false** (because `Tr(A (x) conj A) = |Tr A|^2`). The genus bound `g <= 1` for bosonic letters without cancellation is proved instead by `|Tr M^n|^2 <= Tr S_+^n Tr S_-^n` for all `n` plus a Cesaro argument; the infinite-bond version forces fermionic jumps under explicit Hilbert-Schmidt hypotheses. For Tier B the literal geometric placement and the drafted vacuum ansatz are impossible; an explicit nine-letter tensor exists for `q+1 >= 4 sqrt q`; a two-even one-odd tensor for `y^2 = x^5 + x^3 + x^2 - 2` over `F_5` is certified by an exact rational contraction argument; the Jacobian is the bosonic product of two genus-one rings with the curve a rank-six non-product boundary inside it; Rosati positivity forces conjugation at every CM place and is the PH metric; CM type is a marking, not a gauge.
- Lead: open items - the universal three-letter tensor and its natural selection (conj:three-letter-universal); bosonic cancellation on larger bonds; whether the certified tensor's unitary similarity is an even gauge carrying the Hodge metric; the amplitude-locality conjecture (conj:amplitude-locality).
- Related: L01-072, L01-074, L01-084

### L01-074 Explicit MPS per genus 0-3, and the next rung (a variety with coefficients)
- Source: `HANDOFF.md`:414-424
- Raised by: orchestrator (shard 06g)
- Status at last mention: computed, unreviewed
- Content: one MPS per genus 0-3 written out (genus 3 over `F_37` from three brute-force counts); every odd mode has correlation length `2/log q`, "that is RH"; block Schmidt spectra from the doubled bond with entropy `<= 2 log D`, closed forms giving flat spectra (`log 8`, `log 12`); parent Hamiltonians with the periodic fermion ring selected by a parity-twisted boundary term.
- Lead: **the next rung** if TJO meant a Deligne-type variety: "the simplest is a curve with coefficients (an elliptic surface over `F_q(t)` with degree-2 L-function, a K3 with Picard number 20)." Important warning recorded: a surface's middle cohomology is EVEN, so its interesting eigenvalues are bosonic and the Ramanujan shape is the *graph* one (trivial `q^2`, nontrivial `|beta| = q`); the fermion enters as odd(base) (x) odd(fibre) = even.
- Related: L01-073, L01-113

### L01-075 The Weil numerator as a boson-fermion ring norm: Hasse's `N_n = deg(1-phi^n)` in MPS clothing
- Source: `HANDOFF.md`:517-536
- Raised by: TJO ("for elliptic curves the zeta has numerator and denominator; natural to realise via ring norms of an MPS with fermions and bosons")
- Status at last mention: discussion, not registered
- Content: the P-closed ring norm is `str E^n` on the doubled bond, and the untwisted closure is excluded by thm:no-ungraded-trace. The minimal bond `C^{1|1}` has even and odd doubled sectors of dimension 2 each, exactly `{1,q}` and `{alpha, conj alpha}`. Even a BOSONIC tensor `A_s = diag(a_s, c a_s)` with `sum |a_s|^2 = 1` and `|c|^2 = q` gives `||Psi_P||^2 = |1 - conj(c)^n|^2 = 1 + q^n - alpha^n - conj(alpha)^n`. Cauchy-Schwarz on the cross transfer gives the one-sided bound `|alpha| <= sqrt(1 . q)` for free with decoupled blocks, and the functional equation is the equality case.
- Lead: caveats and the concrete test - `alpha` is put in by hand (circular); "the real question is a tensor from the curve (test: **can the Artin-Schreier super-transfer be written as a `P(x) conj P` graded `E = sum A (x) conj A`?**)"; genus `>= 2` needs cancellations in the `(-,-)` block and presumably fermionic couplings, where Cauchy-Schwarz is no longer free. Wording note: add "with periodic closure" to cor:curve-counts-graded when next touched.
- Related: L01-043, L01-072, L01-125

### L01-076 The fermion parity of a cMPS ring, proved
- Source: `HANDOFF.md`:538-563
- Raised by: TJO, who was cautious about "the ring norm is a supertrace" and asked whether it had been proved (it had not)
- Status at last mention: registered (shards 02f, 04e, 04f; `scripts/cmps_parity_supertrace.py`, 89 checks in CI), unreviewed
- Content: for general data, `<Psi_B'|(-1)^F|Psi_B> = Tr[(B (x) conj B') e^{L T_eta}]` with `T_eta = Q (x) 1 + 1 (x) conj Q' + sum eta_a R_a (x) conj R'_a`, a signed sum of squares; the absence of any sign in the plain norm is a proved step, not a convention. With a bond grading `P`, the *physical* parity carries NO spectral information (`<(-1)^F> = +-1`). The supertrace lives on the doubled bond, `Gamma = P (x) conj P`, with `||Psi_P||^2 = str e^{LT}` and `||Psi_1||^2 = Tr e^{LT}`; `Psi_P` is the periodic (Ramond) fermion ring, `Psi_1` the antiperiodic one. Ring-length transforms give `str(z-T)^{-1} = d/dz log sdet(z-T)`, so the ring zeta `1/sdet(z-T)` has poles net even and zeros net odd.
- Lead: open - infinite bonds, and review.
- Related: L01-043, L01-075, L01-060

### L01-077 Ramanujan conditions written directly in the `Q, R` matrices of a boson-fermion cMPS
- Source: `HANDOFF.md`:565-618
- Raised by: TJO
- Status at last mention: unreviewed discussion export (`outputs/ramanujan-boson-fermion-cmps.md`)
- Content: the finite covariant-GKLS cone did NOT impose regular mixed-cMPS relations. For the standard regularity condition, `Q` is even, `R_b` even, `R_f` odd, with `R_alpha R_beta = (-1)^{p p} R_beta R_alpha` and in particular `R_f^2 = 0`. The observable-convention fermionic correlation transfer is `K_f(X) = Q^dag X + XQ + sum_b R_b^dag X R_b - sum_f R_f^dag X R_f`, intertwined with the ordinary (all-plus, CP) generator by `X -> PX`. For `A = K_f` restricted to the arithmetic sector `E`, the one-sided bound is `Re spec A <= -Delta`, and an additional reflection `lambda -> -2 Delta - conj(lambda)` makes it a line condition; in the Riemann convention `Delta = 1/4`. For a finite block, `A^dag G + G A = -2 Delta G` with `G > 0` is equivalent to the line spectrum AND diagonalisability.
- Lead: an obstruction found - the stationary-state Dirichlet identity vanishes at `X = R_f`, so a strict instantaneous coercivity bound in that metric cannot hold on a sector containing an `R_f` with nonzero stationary-state norm; a spectral gap or a different positive metric can still exist. Next: impose the regular graded `Q,R` algebra together with BC stationarity and arithmetic covariance; identify the sector `E` from the explicit formula / scattering comparison; seek the positive metric or the one-sided bound plus arithmetic duality. Warning recorded: the finite-GKLS counterexample must not be presented as a counterexample within the narrower regular mixed-cMPS class.
- Related: L01-080, L01-093, L01-041

### L01-078 The mixing-time hypothesis: Ramanujan is tightly related to mixing times of Lindbladians (TJO)
- Source: `HANDOFF.md`:471-515
- Raised by: TJO
- Status at last mention: partially explored, with a convergent negative
- Content: two papers were read from TeX. Becker-Zworski "Optimal relaxation for Witten Lindbladians in 1D": trace-norm decay at exactly the gap for a REGULAR class of inputs, sharp, with no uniform exponential decay on all trace class (a `1/t` example hidden in the untypeset tail of the source). Relevance judged suggestive but one-sided. Shang "A Simple Quantum Linear-System Solver via Dissipation": purely dissipative reset Lindbladian, worst-case mixing `O(kappa^2 log 1/eps)`, dimension-independent; relevance judged weak.
- Lead: see L01-079 for the negative it produced, and the four proposed next steps.
- Related: L01-079, L01-093

### L01-079 Convergent negative: `||Z(t)|| = 1` for all `t`, with or without RH
- Source: `HANDOFF.md`:497-515
- Raised by: two Opus readers independently
- Status at last mention: UNREVIEWED negative; "consistent with the recorded Riesz-basis dead route"
- Content: the argument is a reproducing-kernel bound `||Z_t|| >= e^{-eps t} - |S(x - i eps)|` together with `|S(x - i eps)| -> 0` as `x -> infinity` (mpmath at `eps = 0.2` gives 0.72, 0.60, 0.095, 0.027 at `x = 10, 100, 1000, 5000`). **Consequence: RH cannot be a WORST-CASE mixing-time statement for these channels** (there is no bounded `G` with `B^dag G + G B = -G/2` on all of `K_S`); any mixing form must restrict to regular data or a weighted norm - exactly the shape of Becker-Zworski's theorem.
- Lead: four proposed, none started - (1) review the argument and record it as a negative; (2) truncated-zero numerics: `sup_t e^{t/4} ||Z_t^{(N)}||`, Gram condition number, integrated Gramian versus `N`; (3) fetch Lubetzky-Peres "Cutoff on all Ramanujan graphs" (GAFA 2016) and ask for cutoff of Ramanujan quantum expanders (Weil-LPS); (4) identify the regular data class on which "all rates 1/4" is equivalent to uniform `e^{-t/4}` decay.
- Related: L01-078, L01-095, L01-041

### L01-080 The inverse problem: the BC state is the stationary state of an unknown Lindbladian
- Source: `HANDOFF.md`:426-469
- Raised by: TJO (clarifying the problem shape)
- Status at last mention: first finite constraint calculation done (shards 02e/04d), unreviewed
- Content: "The no-event generator and the jumps are BOTH unknown. The fixed-B scalar-reset positivity test is one ansatz, not the whole problem." Findings: no finite-dimensional unital representation of the full BC algebra retains its nontrivial phase observables (finite isometries are unitary, forcing `e(r) = I`). At odd prime `p` and the critical tracial extension `I/p`, the exact real span dimensions of GKLS cones are `(p-1)(p+1)^2` for Galois covariance, `2p-2` for full linear Weil covariance, `p+1` for Weyl+Galois, and `1` for Weyl+Weil. Full Weyl-translation covariance is an EXTRA assumption, not synonymous with carrying the symplectic structure. Full linear Weil covariance alone permits unequal odd decay rates: an explicit `p=7` conditional-Choi-positive perturbation has odd eigenvalues `-1-eps` and `-1+eps/2 +- i sqrt3 eps/2`, `eps = 1/196` - "No zero positions were fitted." Two-prime covariant CP couplings can vary while both one-prime dynamics remain fixed; CRT marginal compatibility does not select the coupling.
- Lead: next - an arithmetic representation or CP comparison map connecting the finite phase/Weil data and the full BC prime isometries to the scattering bond, specifying which symmetries commute with the dynamics and which act covariantly, and constraining the Kossakowski blocks and inter-prime couplings. Still open: prime powers, the real place, metaplectic compatibility, the critical operator-algebra limit, the physical cMPS.
- Related: L01-068, L01-049, L01-077

### L01-081 Ihara zeta functions of simplicial complexes (TJO's sidequest)
- Source: `HANDOFF.md`:632-691
- Raised by: TJO ("the zeros seem to carry surface-like qualities, so is there a natural Ihara-type result for simplicial complexes, and what is its quantum generalisation?")
- Status at last mention: done in one day, registered (shards 02d, 08d, 08e, 08f), Opus-reviewed 47/47 VALID
- Content: the literature result exists for *building quotients only* (Kang-Li, Fang-Li-Wang, Kang-Yu). No Ihara zeta for a general complex exists and four papers say so; Storm's hypergraph zeta is a graph zeta; the quantum side was empty. The object that "wants to exist" is the graded geodesic determinant with specified data (states, successors, algebraic lengths, transports; parity `k+1`). Numerics on `PGL_3(F_3)` (5616 vertices, LSV generators): the link is `PG(2,3)`, `chi = 29952`, NOT 3-colourable so Kang-Li's type hypothesis fails, yet the corrected identity holds exactly to `u^18`; all 5615 nontrivial vertex eigenvalues tempered; the 12-dimensional twist is a Ramanujan quantum expander of type `A~_2`.
- Lead: explicitly "None of this touches the Riemann side." Open: conj:vertex-collapse-characterisation (which complexes beyond buildings admit a vertex-level collapse). Possible follow-ups, not scheduled: the Knill-SDet / Ihara join; a voltage-quotient channel zeta for the Weil-LPS channels to compare with the `A~_2` case; `A~_3` numerics (`PGL_4(F_2)`, needing LSV `e > 1` for `q = 2`).
- Related: L01-082, L01-096

### L01-082 Prover corrections in the complex-zeta lane
- Source: `HANDOFF.md`:655-675
- Raised by: codex prover `astra`, all reviewed VALID
- Status at last mention: applied
- Content: the rule "add a vertex not closing a cell" gives outdegree `2q^2+q` on the `A~_2` building; Kang-Li's `L_E` needs link OPPOSITION, a building notion; the graded total is the completed vertex L-function `D_B/D_E = (1-u^3)^chi/det P_3`, not Kang-Li's `1/D_E`; a universal Bass-Schur identity holds for every complex with arbitrary weights (rational compression by one dimension) but the vertex-level polynomial identity is a *building phenomenon* (for the boundary of the 3-simplex, `Z = (1-u^4)^6` and no matrix polynomial works); on the building vertex side every chamber root cancels, so the reduced vertex L-function is a reciprocal polynomial with NO finite zeros and "fermionic zeros" means net odd multiplicity in a graded presentation, to be checked after cancellation; the `k`-cells / `H^{k-1}` dictionary is parity only; `Tr Ad(B_w) = |Tr B_w|^2` needs no pairing; the no-go's operative hypothesis is "honest trace", not positivity; chronological weights are not flat and the covariant twist on the full Cayley complex is pure gauge - the genuine Artin block is the voltage quotient with `det(1-uT) = prod_rho det(1-uT_rho)^{dim rho}`.
- Lead: Harrow transfer gives Ramanujan quantum expanders of type `A~_{d-1}` for every representation, with an exceptional space and an exact converse criterion.
- Related: L01-081, L01-038

### L01-083 Deligne's proof via graphs: the three ingredients a Hilbert-Polya approach must replace
- Source: `HANDOFF.md`:770-775; `notes/deligne-via-graphs.md`:106-108
- Raised by: orchestrator (expository note)
- Status at last mention: expository, recorded; feeds the "sign" requirement of the central priority
- Content: the three are products (eigenvalues multiply, trivial loss fixed), slicing over a curve (the core theorem is about a curve with matrix coefficients, i.e. a twisted Ihara zeta), and the sign (interesting eigenvalues are zeros, not poles). "Deligne exhibits no Hermitian form; Weil and Artin-Schreier do."
- Lead: see L01-111 through L01-119 for the note's own leads.
- Related: L01-111, L01-114, L01-119

### L01-084 Prior art: what is new and what is not in the quantum Ihara story
- Source: `HANDOFF.md`:777-793; `README.md`:122-125
- Raised by: orchestrator, as a literature check with byte-verified TeX quotes
- Status at last mention: settled
- Content: the Ad(U)-weighted Ihara zeta and its Bass formula are Matsuura-Ohta 2022 (arXiv:2204.06424); arbitrary-weight Bass for loopless graphs is Watanabe-Fukumizu 2011; twisted zetas go back to Sunada 1986. NOT found: any zeta of a quantum channel, "RH iff Ramanujan quantum expander", or the MPS/ring-norm reading. Exactly-Ramanujan channels from LPS via Harrow are in Iyer-Jain-Jordan-Somma arXiv:2602.15180 (SU(2) irreps); "the Weil instance is ours". Then proved: Ihara-Bass for the non-backtracking superoperator of an ARBITRARY Kraus family.
- Lead: convention recorded - `proved` requires a reviewer distinct from the author, and both being Claude models counts as a single declared family.
- Related: L01-021, L01-023, L01-096

### L01-085 The continuous (Selberg) dictionary and the flat-trace tower
- Source: `HANDOFF.md`:795-817
- Raised by: orchestrator; proved by the codex prover, Opus-reviewed 13/13 VALID
- Status at last mention: registered (shards 09b/09c)
- Content: the circle comb is blind to zeros (orbital trace only); the Lindbladian of the `sl_2` vector fields is `2 Omega = -2 Delta` on the K-invariant sector (the Casimir has the compact direction with a minus sign); Poincare Jacobian `4 sinh^2(k l/2)`; the flat trace corresponds to the tower `D(s) = prod_{j>=1} Z(s+j)` with `Lambda_fl = +D'/D`; tower zeros in bands `-1/2 - k +- i r_j`, and the first band is nonconstant on `Re s = -1/2` iff there is no eigenvalue in `(0, 1/4)`; Ruelle `= Z(s)/Z(s+1)`; the modular cusp term is a prime comb with dips `Lambda(n)/n` at `2 log n` plus an exact `+1/2` from the pole of zeta; `e^{-t/4} .` (channel prime measure) = cusp prime measure.
- Lead: open - conj:quantum-lindblad-gap (the continuous Harrow construction), and an operator-level continuous Ihara-Bass (the tower as a Laplacian determinant). Two review action items: (a) fetch a source so H-SZ and H-LAP become `cited` rather than `assumed`; (b) correct section 5 of `notes/riemann-channel-note.md`, whose prime weight `+Lambda(n) n^{-1/2}` is off by a factor `-2` and double-counts the `e^{-t/4}` damping.
- Related: L01-086, L01-108, L01-056

### L01-086 The continuous Harrow channel: assessed as "not hard, theorem-shaped"
- Source: `HANDOFF.md`:900-915
- Raised by: orchestrator (was conj:quantum-lindblad-gap)
- Status at last mention: assessed 2026-09-12 night, not executed
- Content: on each constituent `sigma` of `pi (x) conj pi` and diagonal K-type `m`, `-L = 2 lambda_sigma + m^2/2` with `lambda_sigma = s(1-s)`, so the gap is `min(1/2, 2 s(1-s))` over complementary-series constituents. For tempered `pi` the spherical part of `pi (x) conj pi` is tempered (Cowling-Haagerup-Howe) and the gap is exactly `1/2 = 2 . 1/4`, the continuous Ramanujan value. `e^{tL}` is a mixed-unitary channel averaged over the hypoelliptic heat kernel of `(1/2)(H^2+E^2)` (Nelson, Hoermander). Complementary series: Repka 1978 decides when `pi_s (x) pi_s` contains `pi_{2s-1}`, threshold `s > 3/4` **from memory, must be byte-checked**. The `SL_2(F_p)` half of the conjecture is void.
- Lead: to do - fetch Nelson/CHH/Repka TeX, restate as a theorem with the gap formula, run the codex prover, Opus refute. "The real difficulty is the lattice version (gap of `-2 Delta` on `Gamma\H` = `2 lambda_1`, Ramanujan iff Selberg `1/4`); a quantum (operator-level) lattice version is not yet formulated."
- Related: L01-063, L01-085, L01-064

### L01-087 Weil positivity for an arbitrary transfer operator, and the Kraus dichotomy
- Source: `HANDOFF.md`:819-847
- Raised by: TJO's question ("what does 'the reflection pairs the mode at rho with the mode at 1-conj rho, RH says every mode is its own partner' mean for an arbitrary Kraus family?")
- Status at last mention: registered (shards 08b/08c), proved by the codex prover with Opus refute review
- Content: (i) for any finite-dimensional `X`, positive definiteness of the rescaled trace sequence `r^{-l}(Tr X^l - trivial)` is exactly the one-sided bound `|mu| <= r`, with modes strictly inside the disc passing; (ii) if the retained spectrum is invariant under `J(mu) = r^2/conj mu`, the Weil form equals the mode-pairing form and positivity is equivalent to every mode being `J`-fixed, i.e. all on the circle; (iii) **the Kraus dichotomy**: any Ad-family has nonnegative ring traces and conjugation-closed spectrum (the adjoint pairing was never needed - two drafted claims were corrected by prover and numerics independently); inverse pairing `B_ibar = B_i^{-1}` gives the functional equation `mu -> (D-1)/mu` so its RH reads "every nontrivial eigenvalue of `Sigma` is real with `|alpha| <= 2 sqrt(D-1)`"; adjoint pairing gives HS-self-adjointness, i.e. reality for free (the Hilbert-Polya half); both together iff unitary, where the criterion is Hastings' bound alone; (iv) a Bochner version for Lindblad-type generators with Dyson-expansion ring norms; (v) a Hilbert-Polya inner product exists iff the operator is semisimple on the circle - **Weil positivity is blind to Jordan blocks**.
- Lead: prior art found (Huang 2019, Suzuki 2022, Weil/Li via Connes-Consani and Lagarias); not found - the arbitrary-operator statement, the separation of bound from duality, the Kraus dichotomy.
- Related: L01-097, L01-098, L01-041

### L01-088 Inverse-paired non-unitary Kraus families as the new class to study
- Source: `HANDOFF.md`:916-926
- Raised by: orchestrator (item 1a, sharpened by item 10)
- Status at last mention: proposed, cheap experiments not run
- Content: for adjoint-paired non-unitary families "Ramanujan" can only be the one-sided bound (there is no duality: prop:kraus-no-duality-example). The new class is `B_ibar = B_i^{-1}`: positive rings, a functional equation, and RH equivalent to `Sigma` having real spectrum in `[-2 sqrt(D-1), 2 sqrt(D-1)]` - "a PT-symmetric-type reality statement".
- Lead: three cheap experiments - `B_i = G U_i G^{-1}` (then `Sigma` is similar to Hermitian and reality is free); random invertible `B_i` (does reality fail generically? does the bound?); whether canonical form or the Bartholdi deformation (Matsuura-Ohta arXiv:2208.14032) singles out a duality for adjoint-paired families.
- Related: L01-087, L01-097, L01-064

### L01-089 Restate prop:ringnorm-trace (the distributional trace of the semigroup)
- Source: `HANDOFF.md`:927-930; and the note correction at 813-817
- Raised by: Opus reviewer
- Status at last mention: DONE in shard 04 (`Tr_dist Z(t) = 1 - 2 P_+ - e^{-t/2}/(e^t - 1)`, proved-conditional); the note still carries the old weight
- Content: section 5 of `notes/riemann-channel-note.md` has the prime weight `+Lambda(n) n^{-1/2}`, which is off by a factor `-2` against the note's own explicit formula and double-counts the `e^{-t/4}` damping. Notes are free-form and the shard is authoritative.
- Lead: fix section 5 of the note when next touched.
- Related: L01-085, L01-109

### L01-090 Tighten the "bridge" statement with a full innerness argument
- Source: `HANDOFF.md`:936-939
- Raised by: orchestrator (next step 3)
- Status at last mention: proposed, not done
- Content: the claim "Lax-Phillips = Bost-Connes at `beta = 1` + Sz.-Nagy-Foias" is stated at the level of the boundary phase; the innerness argument should be written in full (Phragmen-Lindeloef in `Im tau < 0`) rather than cited to Lax-Phillips.
- Lead: a self-contained proof of the repo's headline identification.
- Related: L01-038, L01-107

### L01-091 Repo discipline as a research instrument (lab book, four databases, gate, local CI)
- Source: `HANDOFF.md`:940-949; `README.md`:77-89
- Raised by: TJO (decided 2026-09-12 evening)
- Status at last mention: in force
- Content: `report.tex` with shards, four TSV databases (notation, definitions, claims, provenance), `scripts/labbook_check.py` and `scripts/ci_local.sh` via `make hooks`. "A statement is a claim only when it has a row in `db/claims.tsv`; `proved` needs a reviewer file; every quote needs a provenance row." Notes stay free-form but every note must be distilled by a shard, checked in both directions.
- Lead: this is the mechanism that keeps the ideation honest; it is why statuses can be cited at all.
- Related: L01-084

### L01-092 The regular fermionic cMPS four-mode sector (the 2026-09-19 main lead)
- Source: `HANDOFF.md`:13-21
- Raised by: a lane in the 2026-09-19 multi-agent review; saved under `notes/rh-strategy-2026-09-19/`
- Status at last mention: exploratory, saved, session stopped at TJO's request
- Content: "a regular fermionic cMPS with a faithful mixed stationary bond has a physical two-point function selecting a closed four-mode sector. Its quadratic fermion structure supplies observable closure; a separate reflection and coercivity condition enforce a common width. Perturbations distinguish these requirements." Explicitly: "This is a finite mechanism, not a Riemann construction or RH proof."
- Lead: the mechanism separates *closure* (from the quadratic fermion structure) from *common width* (from reflection + coercivity), which is exactly the separation the Weil-positivity work found between bound and duality.
- Related: L01-077, L01-087, L01-093

### L01-093 Selberg's `L^2` Laplace mechanism versus Riemann's cusp wave/scattering leakage
- Source: `HANDOFF.md`:18-21
- Raised by: the 2026-09-19 operator review
- Status at last mention: exploratory; an explicit candidate intertwiner recorded
- Content: the review separates the two mechanisms, records "an explicit candidate flow-to-wave intertwiner", and locates Uetake's 2007 modal/completeness theorem.
- Lead: the intertwiner and Uetake's completeness theorem are the concrete handles; completeness of the resonance modes is exactly what the Riesz-basis dead route (L01-095) failed to give.
- Related: L01-059, L01-095, L01-079

### L01-094 Recovery infrastructure as a research artefact
- Source: `HANDOFF.md`:23-28
- Raised by: orchestrator
- Status at last mention: in place
- Content: `scripts/research_checkpoint.py` writes verified atomic local archives in `.recovery/`, including the Git-ignored reference cache; `RECOVERY.md` gives offline restore instructions; new full sources cached at `refs/src/1712.07832/` and `refs/src/uetake-2007/` with download receipts and hashes committed.
- Lead: none mathematical.
- Related: L01-093

### L01-095 Dead route: bounded renorming of `K_S` (the Riesz-basis obstruction)
- Source: `HANDOFF.md`:693-698
- Raised by: orchestrator, recorded as a dead route
- Status at last mention: DEAD
- Content: the Gram condition number of the Cauchy-kernel eigenvectors grows from 10 to 700 across the 3000 zeros, so there is no bounded renorming making `Z(t)` a damping times a unitary.
- Lead: none; recorded so nobody retries it. Consistent with the `||Z_t|| = 1` negative.
- Related: L01-041, L01-079

### L01-096 The Weil-LPS channel as the first concrete Ramanujan object (TJO's go-ahead)
- Source: `HANDOFF.md`:858-888, 722-732; `transcript/transcript.md`:1227-1234, 1256, 1332-1348
- Raised by: orchestrator, proposed to TJO; TJO said "go ahead and totally compute the suggested object"
- Status at last mention: built and verified for ten `(p;q)` pairs (`scripts/weil_lps.py`), registered as HANDOFF item 5
- Content: Harrow's construction with `G = SL_2(F_p)`, `S` the LPS generators for a prime `q`, `pi` the Weil representation on `l^2(F_p)`: `Phi_q(rho) = (1/|S|) sum_s pi(s) rho pi(s)^dag`. Exactly Ramanujan (LPS + Deligne), commuting for different `q`, jointly diagonal with spectrum given by Hecke eigenvalues of weight-2 forms (Eichler-Shimura). Two adjustments were forced by the mathematics: `q` must be a square mod `p` (the intertwiner exists only for determinant one), and the channel must be taken on the even and odd Weil blocks separately because on the full space the parity operator is a second fixed point and Harrow's theorem needs irreducibility. Two bugs were caught by the built-in checks (quaternion enumeration parity, caught by `sigma(n)`; the Hecke relation failing by signs on `SL_2`, fixed by passing to `PSL_2`).
- Lead: remaining - identify the joint spectra with Hecke eigenvalues via LMFDB and Jacquet-Langlands; and **decide what "assemble over `p`" should mean, which is the DG-GLOBAL question in this guise**.
- Related: L01-020, L01-038, L01-120

### L01-097 The three known sources of Ramanujan-ness, and MSS as the one to watch
- Source: `HANDOFF.md`:858-877; `transcript/transcript.md`:1219-1223
- Raised by: orchestrator, in response to TJO's "RH is a Ramanujan property" steering
- Status at last mention: recorded as steering; MSS never attempted
- Content: exactly three routes are known - arithmetic (LPS via Deligne; every Riemann-relevant instance so far), probabilistic/asymptotic (Friedman for random regular graphs, Hastings for random unitaries: "nearly", with defect `eps -> 0`), and interlacing families (Marcus-Spielman-Srivastava: exactly Ramanujan bipartite graphs of every degree by real-rootedness of expected characteristic polynomials, no arithmetic input). "Real-rootedness of an expected characteristic polynomial is the same shape of statement as 'H is Hermitian', and the Montgomery-Odlyzko fact that the zeros look like eigenvalues of a random Hermitian matrix is the hint that `xi` might be an expected characteristic polynomial."
- Lead: two concrete strategies. (a) Since the zeros are symmetric under `beta <-> 1-beta`, "nearly Ramanujan with `eps -> 0` along an approximating family would be exact for zeta", so a sequence of finite Ramanujan channels converging to the Riemann channel is a genuine strategy, with all the difficulty in the convergence. (b) Look for `xi` as an expected characteristic polynomial (the MSS shape).
- Related: L01-022, L01-041, L01-087

### L01-098 The obstruction: prime dilations commute, and abelian Cayley graphs are never expanders
- Source: `HANDOFF.md`:873-877; `transcript/transcript.md`:1225; `notes/deligne-via-graphs.md`:182, 240
- Raised by: orchestrator; identified as the same obstruction on both sides of the dictionary
- Status at last mention: recorded as the central structural obstacle; deemed "not fatal"
- Content: no channel whose Kraus operators are commuting dilations on a plain space is Ramanujan. LPS shows how arithmetic examples get around it: the Hecke operators `T_q` also commute for different `q`, and expansion comes from the space being an arithmetic quotient; the joint spectrum of the commuting Ramanujan family is the Hecke eigenvalue system, and "Ramanujan for all `q` simultaneously" is Deligne. The same obstruction is *inside* Deligne's proof: commuting holonomies produce uncontrolled invariants and break Step 3 of the pointwise theorem.
- Lead: "Any lift of the prime dilations that hopes to be Ramanujan must break the commutativity by a quotient, as LPS does with the arithmetic lattice and as Deligne does with the shears of a generic slicing."
- Related: L01-037, L01-115, L01-117

### L01-099 Sorting the existing proofs by *where the unitarity comes from*
- Source: `README.md`:45-62
- Raised by: orchestrator (README working picture)
- Status at last mention: standing framing of the whole notebook
- Content: a table - Artin-Schreier transfer matrix (Parseval for additive characters, HP operator explicit); Weil for curves (Hodge index on `C x C`, HP operator via Rosati positivity); Deligne for varieties (positivity of even tensor powers, fixed loss paid by a base curve, roots as `k -> infinity`, no HP operator); LPS graphs (inherited from Deligne via Eichler-Shimura); random graphs and interlacing families (trace method / real-rootedness, no HP operator).
- Lead: "Where the Hermitian structure enters, or whether it must, is the question this notebook circles." This is the repository's stated master question.
- Related: L01-119, L01-097, L01-123

### L01-100 Zeta has the positivity and the sign; it lacks the product
- Source: `README.md`:56-62; `notes/deligne-via-graphs.md`:238
- Raised by: orchestrator
- Status at last mention: "the standard diagnosis, stated in the terms of this note"
- Content: Deligne's route needs a positivity, an operation under which eigenvalues multiply while the trivial loss stays fixed (products of varieties), and the sign putting the interesting eigenvalues in the numerator. Zeta has the positivity (`Lambda(n) >= 0`) and the sign; there is no `X x X` with zeta as its slice, so the multiply step has nothing to act on.
- Lead: find the missing product operation, or a substitute for it. (This is what the `F_1` hope of L01-006 was about.)
- Related: L01-006, L01-083, L01-116

### L01-101 Not established: any construction coupling the primes non-abelianly on the zeta side
- Source: `README.md`:72-75
- Raised by: orchestrator (README honesty list)
- Status at last mention: OPEN, stated as a standing gap
- Content: the README's "not established" list names RH itself, the Stinespring form of the compressed Lax-Phillips semigroup with prime dilations as jumps, and "any construction that couples the primes non-abelianly on the `zeta` side".
- Lead: this is the positive form of the abelian obstruction - a construction task, not just a no-go.
- Related: L01-098, L01-037, L01-038

### L01-102 "The cycle counts fluctuate no more than a random sequence would"
- Source: `notes/what-rh-has-become.md`:41-47
- Raised by: orchestrator, flagged in the note itself as "the single most useful sentence in the document"
- Status at last mention: standing slogan
- Content: `fix(sigma^n) = lambda_max^n + sum_{i>=2} lambda_i^n`, and RH says the fluctuation has size `sqrt(lambda_max^n)`, the size of the fluctuation of a sum of `lambda_max^n` independent coin tosses. "Every later version of RH is this sentence in a different costume."
- Lead: none; it is the reference point for translating any new formulation back to something checkable.
- Related: L01-011, L01-013

### L01-103 The two-level hierarchy: primitivity, spectral gap, Ramanujan
- Source: `notes/what-rh-has-become.md`:94-100, 141-147
- Raised by: orchestrator
- Status at last mention: standing dictionary, reused in the cMPS setting
- Content: for the transfer matrix `E` - a unique eigenvalue on the unit circle is primitivity (Perron-Frobenius), corresponding to `zeta(1+it) != 0` and the prime number theorem; all others inside a smaller circle is a spectral gap, corresponding to the zero-free region; all others on ONE circle of radius `e^{-1/xi}` with `xi = 2/h` is Ramanujan/RH.
- Lead: "RH for an MPS reads: all correlation lengths are equal, and equal to twice the inverse entropy rate"; the frequencies `theta_k` are unconstrained and there may be infinitely many.
- Related: L01-035, L01-013

### L01-104 The bond space is graded, not plainly bosonic (first statement)
- Source: `notes/what-rh-has-become.md`:118-120
- Raised by: orchestrator
- Status at last mention: this is the seed of the whole fermionic programme
- Content: "the total measure is still positive, because `Lambda(n) >= 0`, but the subleading sector of the bond space contributes negatively, so whatever the state is, its bond space is graded, not plainly bosonic."
- Lead: became the central-priority "fermionic zeros" consequence and the supertrace theorems.
- Related: L01-005, L01-043, L01-076

### L01-105 Proving RH here means exhibiting the state, and some arithmetic rigidity has to enter
- Source: `notes/what-rh-has-become.md`:173-178
- Raised by: orchestrator
- Status at last mention: standing diagnosis
- Content: what the new language settles is that RH is about the *sizes* of the subleading modes, not about the existence of the semigroup (which exists, Lax-Phillips). What it does not settle is a mechanism forcing the pairs to be degenerate. In positivity form: RH iff `F(u) = sum_rho e^{(rho-1/2)u}` is positive-definite on the dilation group iff its spectral measure is a positive measure, which by Bochner is the same as all `t_rho` real.
- Lead: "Proving it means exhibiting that state, or a Stinespring form of `Z(t)` with the prime dilations as Kraus operators, in a way that makes the positivity manifest ... the graph lesson says the Kraus structure alone will not do it; some arithmetic rigidity has to enter, playing the role weights play for curves."
- Related: L01-038, L01-018, L01-087

### L01-106 Erratum on words (entanglement Hamiltonian versus transfer generator)
- Source: `notes/what-rh-has-become.md`:180-182
- Raised by: TJO (the challenge), orchestrator (the fix)
- Status at last mention: applied to the notes and the worklog
- Content: an earlier draft and the founding conversation used "entanglement Hamiltonian" for `-log E`; the entanglement Hamiltonian is `-log rho_A`, built from the fixed points of `E`, and Hermitian by construction. The operator whose spectrum contains the zeros is the transfer generator, non-Hermitian in general.
- Lead: a caution about borrowing PEPS boundary-Hamiltonian language.
- Related: L01-041

### L01-107 The open Stinespring question as isolated by the main note
- Source: `notes/riemann-channel-note.md`:127-139
- Raised by: orchestrator
- Status at last mention: the repository's founding open question; next step 2 in the HANDOFF
- Content: the single-Kraus lift `Phi_t(X) = Z(t)^* X Z(t)` exists trivially (sub-unital, with the automorphic wave group as Stinespring dilation and the cusp as environment). A Holevo-form covariant Lindbladian with the von Mangoldt jump measure lives on the full regular representation, has symbol `zeta^t`, and is not the compressed object. "Whether a jump-type generator on `K_S` reproduces `Z(t)` is the open question this note isolates; its physical index would be the Stinespring environment."
- Lead: suggested as a blind codex lane (gpt-5.6-sol xhigh) with the note as its only input; "a negative answer with a reason is a result".
- Related: L01-038, L01-039, L01-040

### L01-108 The bridge recipe: Lax-Phillips = Bost-Connes at `beta = 1` + Sz.-Nagy-Foias
- Source: `notes/riemann-channel-note.md`:33-47, 89-93; `transcript/transcript.md`:1009-1014
- Raised by: orchestrator, verified numerically
- Status at last mention: established (numerically, residual `10^{-3}`); the innerness step still to be written in full
- Content: "Take the BC process at `beta = 1`, discard the divergent real part of its Levy exponent, keep the phase, use that unimodular function as the characteristic function of a contraction semigroup. The functional model of that phase has the zeta zeros as its spectrum." The real part of `psi_1` diverges (the BC phase transition), while the imaginary part converges conditionally at prime-number-theorem strength.
- Lead: see L01-090 (write the Phragmen-Lindeloef argument).
- Related: L01-038, L01-090, L01-039

### L01-109 The 3000-zero ring-norm test as the numerical anchor
- Source: `notes/riemann-channel-note.md`:105-125; `HANDOFF.md`:718-720
- Raised by: orchestrator
- Status at last mention: established (`scripts/ringnorm.py`); the note's weight later found off by `-2` (see L01-089)
- Content: with 3000 zeros and a Gaussian window, the zero sum matches every term of the Weil explicit formula to 0.20 on a scale of 147, with dips at `u = log n` of depth proportional to `Lambda(n)/sqrt n`, prime powers included. "The primes are the ring spectrum of the Riemann channel, the zeros are its transfer spectrum, and one identity, the explicit formula, links them."
- Lead: the dips' sign and depth later became the evidence forcing the fermionic grading (review item X3).
- Related: L01-043, L01-089

### L01-110 The Holevo semigroup is not a semigroup at the critical line
- Source: `notes/riemann-channel-note.md`:79-87
- Raised by: orchestrator
- Status at last mention: recorded constraint
- Content: the Holevo-form covariant semigroup with von Mangoldt jump measure is a genuine Markov semigroup for `sigma > 1` (Khinchin), has no zeros there, and "at `sigma = 1/2` it is not a semigroup at all (the symbol is unbounded)". The BC phase transition at `sigma = 1` is the finite/infinite-activity threshold of the jump measure.
- Lead: whatever object carries the zeros cannot be the naive analytic continuation of the jump semigroup - the compression is essential.
- Related: L01-039, L01-040, L01-107

### L01-111 "What do varieties have, that graphs lack, which makes every one of them Ramanujan?"
- Source: `notes/deligne-via-graphs.md`:104-108
- Raised by: orchestrator (the organising question of the note)
- Status at last mention: answered in three parts (product, slicing, sign); the answer is the note's content
- Content: "There is no theorem that a `(q+1)`-regular graph is Ramanujan; most are not." So the right question is not how to prove the bound but what varieties have. Varieties can be multiplied (eigenvalues multiply), sliced over a curve (becoming a curve with matrix coefficients), and their interesting eigenvalues enter with a minus sign. A graph has none of the three.
- Lead: each of the three is a design target for a Riemann construction.
- Related: L01-083, L01-100, L01-116

### L01-112 The engine: power up, dominate, take roots (and why the bound is `2 sqrt q`)
- Source: `notes/deligne-via-graphs.md`:110-126
- Raised by: orchestrator
- Status at last mention: expository, but the three moves are the reusable mechanism
- Content: on the infinite `(q+1)`-regular tree, closed walks of length `2k` from a root number `4^k q^k` times bounded and polynomial factors (Dyck paths times fresh-neighbour choices), so the spectral radius is `2 sqrt q`. Three moves: a nonnegative count dominates a power of an eigenvalue; the count is known up to a *fixed* loss; take the `2k`-th root and let `k -> infinity`. "The nontrivial content is entirely in move 2."
- Lead: any new proof strategy must supply move 2 - knowing the growth of the count with only a fixed loss.
- Related: L01-116, L01-117

### L01-113 Deligne's pointwise theorem written for graph twists, and the explicit counterexample
- Source: `notes/deligne-via-graphs.md`:128-174
- Raised by: orchestrator
- Status at last mention: expository, with a concrete graph counterexample
- Content: a twist assigns invertible matrices to directed edges with `rho(bar e) = rho(e)^{-1}`; the twisted zeta is `1/det(1-uT_rho)`, and the quantum Ihara zeta of the founding session is exactly this with a bouquet base and `rho = Ad(U_i)`. So **a quantum expander is a Ramanujan twist of a bouquet**. Deligne's hypotheses are (a) real traces, (b) an alternating pairing up to a scalar, (c) big monodromy. The counterexample showing the theorem is false for graphs: the bouquet of two loops with `rho(a) = [[2,1],[1,1]]`, `rho(b) = [[1,1],[1,2]]` satisfies (a), (b), (c) yet `rho(a)` has eigenvalue `(3+sqrt5)/2 > 1`, so it is not pure.
- Lead: what breaks is Step 3 - for a graph every eigenvalue of side B is a pole, so nothing forces the poles to sit at the trivial place.
- Related: L01-021, L01-116, L01-117

### L01-114 Big monodromy is not a miracle: Kazhdan-Margulis shears
- Source: `notes/deligne-via-graphs.md`:176-184
- Raised by: orchestrator
- Status at last mention: expository
- Content: the pairing supplies invariants for free (pairwise contractions), and big monodromy says these are the only ones. How it is verified geometrically: the holonomy around each bad slice is a shear (identity plus a rank-one nilpotent), all carried to one another by the group, and a theorem of Kazhdan and Margulis says a group generated by a single conjugacy class of shears acting without invariant subspaces is automatically as large as the pairing allows. "Big monodromy is not a miracle; it is the statement that the bad slices are all alike, which is true because they are generic."
- Lead: if one wants a non-abelian coupling of the primes, shears generated by a single conjugacy class are the template.
- Related: L01-098, L01-115

### L01-115 The abelian obstruction is literally inside Deligne's proof
- Source: `notes/deligne-via-graphs.md`:182, 240
- Raised by: orchestrator
- Status at last mention: recorded as the sharpest available diagnosis of the commuting-dilations problem
- Content: if all holonomies commute they have common eigenvectors and the tensor powers have far more invariants than the contractions (a common eigenvector with character `chi` becomes invariant in `rho^{(x)N}` as soon as `chi^N = 1`, carrying an unknown scalar), so the trivial poles sit at uncontrolled places and Step 3 gives nothing. "In your setting it is the observation from the founding session that commuting Kraus unitaries never give an expander: the adjoint action of an abelian group has as many invariants as it has joint eigenprojectors. The same obstruction, on both sides of the dictionary."
- Lead: break commutativity by a quotient.
- Related: L01-098, L01-037, L01-114

### L01-116 The sign is what makes the radius of convergence computable
- Source: `notes/deligne-via-graphs.md`:186-204
- Raised by: orchestrator
- Status at last mention: expository; identified as one of the three ingredients
- Content: for a curve with coefficients, `L = det(1-uF | interesting)/det(1-uF | invariant)`. The invariant block produces poles and is exactly what big monodromy computes; the interesting block produces *zeros*, and zeros do not obstruct convergence. "So the radius of convergence of `L_{2k}` is set by the invariant block alone." On the graph side positivity constrains only the sum of everything (the Perron bound); on the curve side the interesting eigenvalues are subtracted, so positivity bounds them by the trivial ones and tensor powers squeeze it to equality.
- Lead: honest summary - "an Euler product with nonnegative coefficients, whose only poles are at a known place, forces every local eigenvalue to lie inside that place, and even tensor powers make the bound exact."
- Related: L01-005, L01-043, L01-113

### L01-117 Slice, bound, multiply - and the single `sqrt q` loss paid by the base curve
- Source: `notes/deligne-via-graphs.md`:206-226
- Raised by: orchestrator
- Status at last mention: expository
- Content: slicing makes the middle block of `X` the interesting block of a base *curve with coefficients*; with pure coefficients the Euler product converges for `|u| < 1/(qc)` so the bound is `q^{(n+1)/2}` against the wanted `q^{n/2}` - "the loss is a single factor `sqrt q`, paid by the base being a curve, and independent of `n`". Then `X^k` has the products `alpha_1 ... alpha_k` among its middle eigenvalues and the loss is still one `sqrt q`, so `|alpha| <= q^{n/2} q^{1/2k} -> q^{n/2}`. "the surface `C x C` is where Weil's proof lived, and the products are not a convenience but the mechanism."
- Lead: the graph analogue of slicing is the Artin-Ihara factorisation over a covering, which the notebook already has - the missing piece is the product.
- Related: L01-100, L01-112, L01-123

### L01-118 Rankin-Selberg is the number-field shadow of the pointwise theorem
- Source: `notes/deligne-via-graphs.md`:239
- Raised by: orchestrator
- Status at last mention: raised once, not pursued
- Content: for a modular form, `L(f x conj f)` has nonnegative coefficients and a known pole, and dominating one local factor gives `|a_p| <= p^{(k-1)/2} . p^{1/2}` - the same fixed loss. Each symmetric-power L-function with known poles shaves the loss (Kim-Sarnak's `7/64` is the current state). "Knowing the poles of *all* the tensor-power L-functions is the analogue of big monodromy, and over number fields it is Langlands functoriality, unproved."
- Lead: this locates precisely what would have to be imported from the automorphic side; nobody in the notebook followed it up.
- Related: L01-116, L01-100

### L01-119 Ramanujan without Hermiticity is possible - the cleanest evidence for TJO's steering question
- Source: `notes/deligne-via-graphs.md`:228-241
- Raised by: orchestrator
- Status at last mention: recorded as the answer to the notebook's master question so far
- Content: Deligne's proof never exhibits a Hermitian structure. Weil's proof for curves does (the intersection form on `C x C` is definite by the Hodge index theorem, making `F/sqrt q` unitary for an explicit inner product). Grothendieck's plan was to prove a definite form in all dimensions (the standard conjectures) and deduce RH as Weil had; that plan is still open, and Deligne bypassed it. "So RH over finite fields is a theorem, but the inner product that would make Frobenius normal is, in dimension above one, not known to exist."
- Lead: "For the steering question of where Hermiticity enters, this is the cleanest evidence that it need not enter at all; what must enter is a positivity plus an operation under which eigenvalues multiply while the loss stays fixed."
- Related: L01-099, L01-018, L01-100

### L01-120 The Weil-LPS joint spectrum: structure visible, identification not done
- Source: `notes/weil-lps-channels.md`:64-77, 96
- Raised by: orchestrator
- Status at last mention: NOT done; needs LMFDB and Jacquet-Langlands bookkeeping
- Content: for `(13; 17, 29)` the even block has 19 distinct joint eigenvalue pairs, some integral, some in `Q(sqrt 17)`, some of higher degree; all inside the Ramanujan box. "The eigenvalues are algebraic integers by construction, since the Cayley adjacency matrix is an integer matrix, so that is not a test." What is visible is the structure the identification predicts: joint pairs, small-degree algebraic integers, and multiplicities equal to the multiplicity of the corresponding irreducible representation of `PSL_2(F_p)` in `W_+- (x) conj W_+-`.
- Lead: the identification with Hecke eigenvalues of weight-2 forms for the quaternion algebra ramified at `{2, infinity}`.
- Related: L01-096, L01-121

### L01-121 Not established for Weil-LPS: `p -> infinity` and assembling over all `p`
- Source: `notes/weil-lps-channels.md`:94-98
- Raised by: orchestrator
- Status at last mention: OPEN
- Content: "Any statement about `p -> infinity` or about assembling the `Phi_q` over all `p` into an object with the primes as rings; that is the DG-GLOBAL question of the parent repo in a new guise."
- Lead: this is the most direct route from the finite verified model to the infinite object; connects to the "converging family of Ramanujan channels" strategy.
- Related: L01-096, L01-097, L01-037

### L01-122 The honest last row: these channels are Ramanujan because of Deligne, not because they are channels
- Source: `notes/weil-lps-channels.md`:79-92
- Raised by: orchestrator
- Status at last mention: standing caveat
- Content: the dictionary table matches every ingredient (commuting Hecke channels for commuting prime dilations, `PSL_2(F_p)` as arithmetic quotient, the Weil representation, joint spectrum for zeros, Ramanujan for RH) except the last row: "source of the bound: unknown" versus "source of the bound: Deligne, via LPS". What the computation establishes is that the proposed object exists, is cheap, is self-checking, and lands on the parent campaign's Hilbert space.
- Lead: the search is for a *channel-internal* source of the bound.
- Related: L01-096, L01-018, L01-097

### L01-123 RH is unitarity: the Artin-Schreier transfer matrix with `E E^dag = q I`
- Source: `notes/artin-schreier-mps.md`:53-59; `HANDOFF.md`:734-743
- Raised by: TJO ("so can we find a matrix product state formulation of the weil conjectures this way")
- Status at last mention: registered (HANDOFF item 6), with the sign law later corrected by the prover
- Content: in a normal basis Frobenius is the cyclic shift, so an element of `F_{q^n}` is a ring of `n` sites. For quadratic Artin-Schreier `g(x) = sum_j a_j x^{1+q^j}`, the trace form in a self-dual normal basis is a translation-invariant quadratic spin model of range `J`, hence an MPS of bond dimension `q^J`. `E E^dag = q I` whenever `a_J != 0`, for a one-line reason: "the oldest spin in the bond couples linearly to the newest, so summing it out gives `q` times a delta". So rationality is finiteness of `E`, the functional equation is `E -> q E^{-dag}`, and RH is manifest. (Later correction in shard 06b: the founding `alpha = -lambda(E)` claim was FALSE in general, as was the orchestrator's conjugated replacement; the exact sign law is `S_n = (-1)^{n-1} det(S|ker P_g(S)) Tr E^n`.)
- Lead: "the first genuinely exact MPS instance of the Weil conjectures in the repo", and the prototype for a mechanism-supplied odd-block unitarity.
- Related: L01-064, L01-075, L01-124

### L01-124 Where the MPS formulation stops, and why that is the right place
- Source: `notes/artin-schreier-mps.md`:61-72
- Raised by: orchestrator
- Status at last mention: settled boundary
- Content: for cubic or higher digits, `Tr(x^3)` in normal-basis coordinates involves the multiplication structure constants, which are non-local and `n`-dependent. "The self-dual normal basis makes the *bilinear* trace form local, not the *trilinear* one." So exactly the sums Weil needed algebraic geometry for (cubic Gauss, Kloosterman) are the ones with no fixed local tensor. The uniform object beyond quadratic is Dwork's `p`-adic operator `alpha = psi_q . M_F` - "local weight then decimate by `q`", a coarse-graining tensor-network step with nuclear bond dimension. It gives rationality and the functional equation but **cannot deliver RH, because it sees the `p`-adic sizes of the eigenvalues (Newton polygon), not their complex absolute values**.
- Lead: "the Ramanujan bound is either manifest because the transfer matrix is a scaled unitary, or it comes from arithmetic input outside the transfer structure."
- Related: L01-123, L01-099

### L01-125 Open: a different `n`-uniform basis making cubic traces local
- Source: `notes/artin-schreier-mps.md`:78-82
- Raised by: orchestrator (the note's "Not established" list)
- Status at last mention: raised, explicitly never searched
- Content: three items - any fixed-local-tensor MPS for a non-quadratic Artin-Schreier curve or any genus `>= 1` curve not of this maximal type; "Whether a *different* basis of `F_{q^n}`, uniform in `n`, makes cubic traces local. **No candidate was found or searched for.**"; and a rigorous write-up of the unitarity argument as a lemma with the exact hypothesis `a_J != 0` and the even-`n` sign convention.
- Lead: the basis question is a concrete, self-contained search problem that would extend the exact MPS instance past the quadratic wall.
- Related: L01-123, L01-124, L01-072

## Small but possibly consequential

Items mentioned briefly and never followed up, each with one sentence on why it could matter.

1. **L01-012 (realisability of linear recurrences).** The question "which infinite permutations have rational `Z`" was reduced to an arithmetic condition on integer sequences (`sum_{d|n} mu(n/d) fix(sigma^d) = 0 mod n` with nonnegative quotient) and then dropped - it is the only place in the notebook where the *existence* of side B is a solved-in-principle arithmetic question.
2. **L01-029 (necklaces between Cuntz and Bost-Connes).** The remark that the MPS gas is the free version and BC the commutative version of one construction, "with necklaces sitting in between", was made once and never used, yet it names an intermediate algebra that would be the natural home for the sought object.
3. **L01-024 (character values `|Tr U_w|^2` over long words).** The RH question for a quantum expander was reduced to a distributional question about free-group characters, which is exactly what Hastings' proof controls - a possible non-arithmetic route to a Ramanujan bound.
4. **L01-027, lever 2 (change the constraint).** Non-backtracking is just one classical automaton on physical indices; the observation that Bass factorisation is the special property of the reversal-symmetric constraint suggests a whole family of unexplored zetas with different functional-equation structure.
5. **L01-055 (per-window disc radius as an ignorance measure).** Proposed but not run: use the shard-08g extension disc radius inside `ihz`/`zst` as a rigorous measure of what positivity alone cannot know, to be compared against the observed `e^{-4 pi x}` convergence.
6. **L01-069, final clause (bond-cutoff family with accumulating divisor points).** Identified as "the only route to non-rational behaviour" from the finite-tensor side, and never attempted - it is the bridge from the catalogue of toy tensors to an infinite object.
7. **L01-118 (Rankin-Selberg / symmetric-power L-functions).** The note identifies Langlands functoriality as the number-field analogue of big monodromy and Kim-Sarnak `7/64` as the current fixed loss; this is the only concrete statement in the lane of what would have to be imported from the automorphic side.
8. **L01-125 (an `n`-uniform basis making cubic traces local).** Explicitly "No candidate was found or searched for", yet it is a well-posed finite search that would push the exact MPS formulation of the Weil conjectures past the quadratic wall.

## Dead routes recorded

Routes explicitly declared dead, negative or ruled out in this lane's files.

- **Bose Fock space over `l^2(N)` with `h_0 = log n`** as the Riemann gas: gives `prod_n (1-n^{-beta})^{-1}`, not zeta, and the `n=1` mode condenses at every temperature. `transcript/transcript.md`:72.
- **Wick-rotating the Bost-Connes Hamiltonian to get Hilbert-Polya**: the spectrum of `H` is `{log n}` and no change of variable turns `log n` into `t_n`; the relation is Fourier duality. `transcript/transcript.md`:115.
- **Soule's zeta over `F_1` as a small RH example**: zeros at `0, ..., n`, all real, no critical line, "no RH content at all, because over `F_1` the Frobenius is trivial". `transcript/transcript.md`:183.
- **One infinite cycle (the shift on `Z`) as a test permutation**: no fixed points at any `n`, `Z(T) = 1`, "Nothing to study"; and infinite cycles never occur in the Frobenius setting. `transcript/transcript.md`:302.
- **"RH = all eigenvalues on the unit circle"** as a statement that survives to infinite permutations: false, since the replacing finite matrix is not unitary (`[2]` for `x -> x^2` on the closure of `F_2`). `transcript/transcript.md`:314-316.
- **Shor's algorithm as carrying RH content by itself**: `U_a` is a finite permutation whose zeta is trivially rational with RH automatic; its periods are governed by Dirichlet L-functions, not zeta. `transcript/transcript.md`:565, 570.
- **Plain cMPS as the continuum object**: the ring length becomes a free real parameter and the Euler product dissolves into `int dL/L`, so there is no discrete side A. `transcript/transcript.md`:725.
- **Commuting dilations / prime-by-prime ansaetze** (direct sums of circle rotations): spectrum on the imaginary axis, decay rate 0, no expansion; for finite prime sets the spectrum is only the poles of the partial Euler product, and "zeros exist only in the infinite product". `transcript/transcript.md`:860; `HANDOFF.md`:849-856.
- **Calling `-log E` the entanglement Hamiltonian**: the entanglement Hamiltonian is Hermitian by construction and blind to the subleading spectrum; the zeros live in the non-Hermitian transfer generator. `transcript/transcript.md`:1168-1172; `notes/what-rh-has-become.md`:180-182.
- **The Artin-Schreier founding sign claim `alpha = -lambda(E)`**: "FALSE in general; so was the orchestrator's conjugated replacement". `HANDOFF.md`:96-98.
- **The SHW rebound state being the vacuum**: the vacuum is absorbing (the renewal integral diverges), so it cannot be the rebound state. `HANDOFF.md`:92-94.
- **The yolo Lindbladian (Ramanujan-sum sector + prime jumps at rate `1/p`)**: NEGATIVE, with exact counterexamples - the grading is not invariant, vacuum-character coherences are not modes, shell Gibbs weights are not stationary, rates `1/p` define no normal semigroup, the parity ring trace is not a trace at a prime cutoff, parity closure is not the `Q^x` quotient. `HANDOFF.md`:345-366.
- **The Ruelle zeta (full transverse forms) as the Selberg graded transfer**: it FAILS both the functional equation and Ramanujan because its even band is shifted by one. `HANDOFF.md`:201-204.
- **A doubled-bond CP realisation of the Selberg graded transfer**: flat supertraces are negative distributions. `HANDOFF.md`:216-217 (prop:selberg-no-cp-realisation).
- **K-type parity as the flow grading**: it is not a flow grading and does not supercancel. `HANDOFF.md`:217-218 (prop:ktype-not-flow-grading).
- **The `e^{t/2}` rescaling for the modular scattering sector**: the WRONG rate; that sector's centre is `-3/4` under RH, not `-1/4`. `HANDOFF.md`:222-224.
- **The drafted odd-mode bound `sum_odd |mu|^2 <= 2 Tr(E_++) Tr(E_--)`**: false, because `Tr(A (x) conj A) = |Tr A|^2`; caught independently by the prover and the numerics lane. `HANDOFF.md`:395-397.
- **Tier B literal geometric placement and the drafted vacuum ansatz**: "impossible". `HANDOFF.md`:400-402.
- **Inverse-closed letters alone as a source of the functional equation**: `diag(1,2)` is a counterexample; and the swap L-function is not an Artin factor. `HANDOFF.md`:336-337.
- **An odd-sector Alon-Boppana bound**: does not exist - the letter `P` kills the odd sector. `HANDOFF.md`:270-271 (obs:odd-gap-no-alon-boppana).
- **"Fermionic primes give zeros on `Re s = 0`" as a global statement**: true per finite factor only; the global reading was amended. `HANDOFF.md`:361-363.
- **RH as a worst-case mixing-time statement**: `||Z(t)|| = 1` for all `t`, with or without RH, so there is no bounded `G` with `B^dag G + G B = -G/2` on all of `K_S`. `HANDOFF.md`:497-506 (unreviewed).
- **A bounded renorming of `K_S` (Riesz-basis obstruction)**: Gram condition number grows from 10 to 700 across the 3000 zeros. `HANDOFF.md`:697-698.
- **SPT protection as the mechanism**: "signs, not moduli" (obs:spt-protection-is-sign-data). `HANDOFF.md`:693-694, 845-846.
- **`PSL(2,Z)`-generator channels**: "expanders, not Ramanujan" for `p >= 11`; parked. `HANDOFF.md`:694-695, 846-847.
- **"GUE positions with equal widths is the fingerprint of scalar loss"**: false - one-port inverse design realises any equal-width poles; the information is in the couplings. `HANDOFF.md`:695-697.
- **A vertex-level polynomial Ihara identity for a general simplicial complex**: a building phenomenon only; for the boundary of the 3-simplex `Z = (1-u^4)^6` and no matrix polynomial works. Also: no Ihara zeta for a general complex exists, and four papers say so. `HANDOFF.md`:649-650, 662-664.
- **Adjoint-paired non-unitary Kraus families having a functional equation**: none exists (prop:kraus-no-duality-example), so "Ramanujan" can only be the one-sided bound there. `HANDOFF.md`:917-919.
- **Dwork's `p`-adic transfer operator as a route to RH**: it delivers rationality and the functional equation but "cannot deliver RH: it sees the `p`-adic sizes of the eigenvalues (Newton polygon), and RH is about their complex absolute values". `notes/artin-schreier-mps.md`:72.
- **A fixed local MPS tensor for non-quadratic Artin-Schreier curves in the shift basis**: the trilinear trace form is non-local and `n`-dependent. `notes/artin-schreier-mps.md`:63.
- **Deligne's pointwise theorem for graph twists**: false, with an explicit counterexample (bouquet of two loops, `rho(a) = [[2,1],[1,1]]`, `rho(b) = [[1,1],[1,2]]`) satisfying all three hypotheses yet not pure. `notes/deligne-via-graphs.md`:174.
- **Commuting holonomies / abelian monodromy in Deligne's argument**: uncontrolled invariants, Step 3 gives nothing - the same obstruction as commuting Kraus unitaries never giving an expander. `notes/deligne-via-graphs.md`:182.
- **Grothendieck's standard-conjectures route (a definite form in all dimensions)**: still open; Deligne bypassed it, and the inner product making Frobenius normal is not known to exist above dimension one. `notes/deligne-via-graphs.md`:230.
