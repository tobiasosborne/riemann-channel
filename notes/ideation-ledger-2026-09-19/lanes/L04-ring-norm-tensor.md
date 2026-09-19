# Lane L04: the ring-norm-tensor campaign

Scope: the 2026-09-14 "ring-norm-tensor" campaign — curve point counts realised as
parity-twisted ring norms (supertraces) of graded MPS tensors; ordinary elliptic curve
(Tier A), ordinary genus two (Tier B), the bosonic no-go, and what it all suggests for
the Phantasm. Lanes: TJO (question), orchestrator `claude:fable-5.1` (brief + prior
numerics), prover `codex:gpt-6-astra` (proofs), numerics `claude:opus-5`, adversarial
reviewer `claude:opus-5`.

## Coverage

| file | lines | read fully? | ideas found |
|---|---|---|---|
| `notes/ring-norm-tensor/astra-brief.md` | 27 | yes | 16 entries cite it (001–005, 007, 009, 011, 014–016, 018, 021, 027–029, 031–032, 044, 048–051) |
| `notes/ring-norm-tensor/astra-proofs.md` | 1184 | yes | 47 entries cite it (the bulk of the ledger) |
| `notes/ring-norm-tensor/numerics.md` | 377 | yes | 18 entries cite it (008, 010, 019, 020, 023, 030, 032–036, 043, 060, …) |
| `notes/ring-norm-tensor/sources.md` | 666 | yes | 7 entries cite it (053, 055, 056, 057, 058, plus provenance notes in 045, 016) |
| `notes/reviews/ring-norm-tensor-2026-09-14.md` | 792 | yes | 16 entries cite it (008, 023–026, 036, 038, 042, 043, 045, 052–059) |

No file was empty of ideas.

---

## Ideas and leads

### L04-001 The campaign question: an MPS tensor for the simplest variety with no obvious Polya–Hilbert Hamiltonian
- Source: `notes/ring-norm-tensor/astra-brief.md`:5 (the whole "THE QUESTION (TJO, 2026-09-14)" paragraph)
- Raised by: TJO
- Status at last mention: partially explored — items (1),(2),(3) answered for Tier A and (with caveats) Tier B; (4) answered as a unitary not a Hamiltonian; (5) answered only by putting the eigenvalues in by hand
- Content: TJO asked for "an educated guess, with proofs where possible, for the matrix product state (MPS) tensor of the absolute simplest variety that does not have an obvious Polya--Hilbert (PH) Hamiltonian", with a five-item wish list: (1) a natural MPS tensor determined by the variety data; (2) a prescription for which bond modes are bosonic and which fermionic, and why; (3) a theorem that ring norms give the correct counts so the ring zeta matches the expected zeta; (4) an identification of the PH operator; (5) the Ramanujan property for the MPS. "Obvious PH Hamiltonian" was defined in the notebook to mean the quadratic Artin–Schreier transfer matrix.
- Lead: the five items are the scorecard for every later entry; the open half is (1) "natural" and (5) "structural" — a tensor exists, but nothing in the campaign makes RH fall out of the tensor rather than being inserted through the eigenvalues. If a tensor could be written from the *equation* of the curve and RH read off from complete positivity, that would be the Phantasm for varieties.
- Related: L04-012, L04-034, L04-037, L04-042, L04-045, L04-046

### L04-002 The two-tier plan: ordinary elliptic as theorem, ordinary genus two as educated guess
- Source: `astra-brief.md`:5; `astra-proofs.md`:7 (summary of conclusions), 1184 (RESULT line)
- Raised by: TJO / orchestrator
- Status at last mention: executed; Tier A complete, Tier B complete only for one curve plus a large-field family
- Content: "The simplest variety outside that class is an ORDINARY elliptic curve over F_q; the first case where fermionic physical species are forced is genus 2." Tier A was to be all theorems; Tier B an educated guess "to be made as rigorous as you can". Outcome: Tier A is an exact finite graded MPS theorem; Tier B has a certified tensor for one F_5 curve and an explicit algebraic family for every q >= 16.
- Lead: the missing middle is genus two over small fields (q < 16) other than the single certified example, and genus >= 3. Stated as open at `astra-proofs.md`:1182.
- Related: L04-037, L04-041, L04-042

### L04-003 Gauge freedom of a graded MPS tensor as a design constraint
- Source: `astra-brief.md`:5, :15 (T1(f)), :21 (T4(d)); `astra-proofs.md`:398–419 (T1.7), 1041–1060 (T4.8); `numerics.md`:146–150
- Raised by: TJO ("Remember the gauge freedom of MPS tensors")
- Status at last mention: settled for what gauge *is*; the useful consequence (which structural ansatzes are genuine restrictions) was extracted numerically
- Content: even gauge is `A_s -> G A_s G^{-1}` with `G = diag(g_0, H)`, acting by `B_s -> H B_s H^{-1}`, `c_f -> g_0 c_f H^{-1}`, `d_f -> H d_f g_0^{-1}`; it conjugates `E` by `G (x) conj G` and leaves every ring norm invariant. The numerics lane drew the practical corollary: "so `B_1=0` (a vacuum species) and `all B_s diagonal` are genuine restrictions, not gauge choices."
- Lead: use gauge-invariant coordinates (the Gram matrix of the physical coefficient vectors, `spec M`, `spec N`) when hunting for a closed form, since individual entries move along gauge orbits *and* along a genuine moduli direction.
- Related: L04-034, L04-035, L04-047

### L04-004 Point counts as ring norms: N_n = N_{K/Q}(1 - pi^n) = |O/(pi^n - 1)O|
- Source: `astra-brief.md`:15 (T1(a)); `astra-proofs.md`:241–276 (Theorem T1.1); `numerics.md`:72–93 (N2)
- Raised by: TJO / orchestrator
- Status at last mention: registered and proved (T1.1, conditional on H-DEURING, H-DEG, H-FROB, H-LEF; the point-group reading on H-LENSTRA); numerically confirmed for three curves at n = 1,2,3
- Content: for an ordinary elliptic curve, `#E(F_{q^n})` is literally the index of the principal ideal `(1 - pi^n)` in the endomorphism order O — "the count is literally the norm of the ideal". This is the campaign's side-A anchor: the gas of primes as ring norms. Under Lenstra, `E(F_{q^n}) = O/(pi^n - 1)O` as an O-module.
- Lead: this is the only place in the campaign where the count is an honest arithmetic *norm* rather than a supertrace fitted to it. The lead never followed: is there a Riemann-side ring whose ideal norms are the zero-counting data?
- Related: L04-021, L04-022

### L04-005 Where the "obvious" PH Hamiltonian lives and why it stops: the quadratic Artin–Schreier family is supersingular
- Source: `astra-brief.md`:13 (T0(a)); `astra-proofs.md`:89–112 (T0.1); `numerics.md`:253–272 (N4(a))
- Raised by: orchestrator, from shard 06b
- Status at last mention: proved (T0.1, conditional on H-AS-WEIL/H-AS-FILTER/H-AS-SUPER); 11/11 numerical cases agree
- Content: for `y^q - y = g(x)` with `g = sum_j a_j x^{1+q^j}`, the normalized transfer `E_g/sqrt q` equals a root-of-unity phase times `W(M_g)` for `M_g` in the finite group `Sp(2J, F_q)`, so it has finite order; every Frobenius eigenvalue is `sqrt q` times a root of unity and the curve is supersingular. Numerically the orders of `lambda/sqrt q` are 1..36 across `q in {3,5,7}`, `J <= 2`.
- Lead: this is the *boundary* of the easy case. Everything the campaign did afterwards was an attempt to cross it. Corrected sub-point: the phase is not a root of unity "because the entries are roots of unity" (there are zero entries and a `q^{-1/2}`); the Fourier–phase–permutation determinant calculation is the proof (`astra-proofs.md`:109, ledger item 2 at :1107).
- Related: L04-006, L04-009, L04-051

### L04-006 Supersingularity of the quadratic family over arbitrary finite fields, by Gauss sums and a finite-valued recurrence
- Source: `astra-proofs.md`:113–145 (Proposition T0.2), 1106 (ledger item 1)
- Raised by: codex prover (extending the brief's odd-prime scope)
- Status at last mention: proved-here, conditional only on H-FROB; reviewer verdict VALID after the m2/m3 fixes
- Content: the normalized Frobenius power sums of the quadratic family take values in a *finite* set independent of n (quadratic Gauss sums have modulus 0 or `p^{(m+d)/2}` with a phase in `{+-1, +-i}`), and a power-sum sequence of finitely many nonzero complex numbers which lives in a finite set is eventually periodic; Vandermonde then forces `(alpha_i/sqrt q)^h = 1`. "No RH modulus premise was used." This covers characteristic two without claiming a genuine symplectic implementer there.
- Lead: the technique — finite value set + fixed linear recurrence + Vandermonde — is a general "spectrum is roots of unity" detector and could be pointed at any other family whose exponential sums are computable. Not tried elsewhere.
- Related: L04-005

### L04-007 The ring cut-rank bound is D^2, not D
- Source: `astra-brief.md`:13 (drafted as "at most D"); `astra-proofs.md`:146–165 (Proposition T0.3), 1109 (ledger item 4); `notes/reviews/ring-norm-tensor-2026-09-14.md`:416–420 (C20), :463
- Raised by: orchestrator (drafted wrong); corrected by codex prover
- Status at last mention: dead as drafted; corrected version proved-here and shown sharp
- Content: a contiguous bipartition of a *ring* cuts two virtual edges, so the flattening rank is at most `D^2`, and the bound is attained (matrix-unit alphabet at n = 2; also a unit-modulus example `A_0 = |0>(<0|+<1|)`, `A_1 = |1>(<0|-<1|)` whose ring amplitude is `(-1)^{sum_i s_i s_{i+1}}` and whose 2|2 cut at n = 4 has rank 4). General bipartition: `D^b` with b the number of cut edges.
- Lead: none stated beyond "use D^2 when reasoning about rings".
- Related: L04-008

### L04-008 The binary cut-rank experiment and the boundedness question — resolved by the self-dual normal basis
- Source: `astra-brief.md`:13; `astra-proofs.md`:166–236 (Proposition T0.4), 1110 (ledger item 5); `numerics.md`:274–322 (N4(b)), :376; review:33–71 (MAJ-1), :422–424 (C21), :466–468, :756–765 (post-fix)
- Raised by: orchestrator (asked "stating whether it is bounded"); answered "open here" by the prover; closed by the numerics lane and the reviewer
- Status at last mention: pursued, positive — bounded by 4 in a self-dual normal basis; the prover's growing table `2,4,8,16,8,4,2` was basis artefact. Registered in shard `num:cut-rank-binary`.
- Content: for `q = 2`, `Tr(x^3) = Tr(x·x^2) = sum_{i,j} x_i x_j c_{j+1-i}` with `c_k = Tr(beta^{1+2^k})`; self-duality is exactly `c_k = delta_{k,0}`, so the form is the cyclic nearest-neighbour `sum_i x_i x_{i-1}` and a contiguous cut sees only two boundary bonds, giving cut rank `<= 4 = D^2` for *every* n. Verified for n = 3,5,6,7,9,10,11. Self-dual normal bases of `F_{q^n}/F_q` exist only for n odd, or n = 2 mod 4 with q even (no such basis at n = 4, 8 over F_2).
- Lead: the dichotomy the campaign wanted now has a provable half (quadratic bounded, cubic growing), which "makes a dichotomy plausible" — the concrete next step is to prove the other half, i.e. Conjecture T0.C.
- Related: L04-009, L04-010, L04-005

### L04-009 Conjecture T0.C: restricted amplitude locality
- Source: `astra-brief.md`:13 ("state the CONJECTURE (label it, do not claim it)"); `astra-proofs.md`:237, 1111 (ledger item 6), 1182; review:470–473, :761–765
- Raised by: TJO/orchestrator; sharpened by codex prover
- Status at last mention: open, explicitly labelled so
- Content: "After specifying a normal-basis prescription for every n and quotienting the polynomial data by trace-invisible Artin--Schreier coboundaries, a fixed finite tensor with the particular amplitudes psi(Tr g(x)) for every n can exist only if those trace functions have quadratic degree (allowing lower degree) over the prime field." Necessity only. Three caveats the prover insisted on: the basis prescription matters (now fixed to self-dual), "quadratic" means degree of a *function* not of a polynomial, and a coboundary `h^q - h` can give a nonquadratic polynomial with the same amplitudes. The conjecture says nothing against the finite ordinary-elliptic *norm* tensor.
- Lead: prove it, or find a nonquadratic trace function with bounded cut rank in the self-dual basis. If true it is the sharp statement of "equation-local tensors only see Gauss sums" and tells the Phantasm that a Riemann tensor cannot be equation-local.
- Related: L04-008, L04-051

### L04-010 The cubic amplitude's cut rank grows — the other half of the dichotomy
- Source: `numerics.md`:283–313 (tables for q = 2 and q = 3), :376
- Raised by: numerics lane (Opus)
- Status at last mention: computed, positive evidence; not proved
- Content: in the self-dual normal basis the cubic amplitude `Tr(x^{1+q+q^2})` has cut rank `2,4,8,16` at n = 3,5,7,9 for q = 2 and `1,9,27` at n = 3,5,7 for q = 3 — roughly doubling (tripling) every two sites — while the quadratic stays at `<= 4` (resp. `<= 9`). "So no fixed finite lattice tensor reproduces the cubic amplitude."
- Lead: extend the table to larger n and to other non-quadratic trace forms; a proved growth rate would be most of T0.C's necessity half.
- Related: L04-008, L04-009

### L04-011 The single toral dynamical system realises both the gas side and the transfer side
- Source: `astra-brief.md`:15 (T1(b)); `astra-proofs.md`:277–299 (Theorem T1.2), 1112 (ledger item 7); `numerics.md`:50–70 (N1)
- Raised by: TJO/orchestrator
- Status at last mention: proved; orbit correspondence corrected to non-canonical
- Content: `(T^2, M)` with `M` the integer matrix of `pi` has `exp(sum_n #Fix(M^n) u^n/n) = (1 - au + qu^2)/((1-u)(1-qu)) = Z(E,u)`, and by Mobius inversion it has exactly as many primitive closed orbits of each length as E has closed points of each degree. So the Euler product (gas) and the Lefschetz trace (transfer) are two readings of one system. Correction (ledger 7): equal orbit counts give a length-preserving bijection *after choices*, "not a canonical arithmetic correspondence supplied by the zeta identity".
- Lead: the Phantasm wants exactly this — one dynamical system whose orbits are the primes and whose cohomology carries the zeros. The break is recorded at L04-050: no analogous lifted Riemann dynamics is known.
- Related: L04-050, L04-004

### L04-012 The elliptic answer: A_s = a_s diag(1, pi) on C^{1|1}, doubled bond = H^*(T^2)
- Source: `astra-brief.md`:3(i), :15 (T1(c)); `astra-proofs.md`:300–332 (Theorem T1.3); `numerics.md`:63–68
- Raised by: orchestrator (from the morning's numerics), proved by codex prover
- Status at last mention: registered and proved; the cleanest result of Tier A
- Content: ket bond `V = Lambda^*(H^{1,0}) = C (+) C dz = C^{1|1}`, `P = diag(1,-1)`; all tensors even; the doubled bond is `diag(1, conj pi, pi, q)` with `Gamma = diag(1,-1,-1,1)`, i.e. exactly `H^0, H^{0,1}, H^{1,0}, H^2` of the torus with parity = total form degree. Every word gives `Tr(P A_{s_1}...A_{s_n}) = (1 - pi^n) prod a_{s_i}`, so `||Psi_P(n)||^2 = |1 - pi^n|^2 = N_n`; untwisted it is `|1 + pi^n|^2`. A singleton alphabet already suffices. Answers wish-list items (1),(2),(3) for Tier A: the modes are fermionic exactly when they are odd-degree forms, and the count is a supertrace because it is a Lefschetz number.
- Lead: the prescription "bond = Lambda^* of the holomorphic half, parity = form degree, bra = the antiholomorphic half" is the campaign's one *natural* tensor rule. Genus two breaks it (L04-029).
- Related: L04-013, L04-029, L04-044

### L04-013 Bond-odd versus physically fermionic; the state does not enumerate points
- Source: `astra-proofs.md`:329, 1116 (ledger item 11)
- Raised by: codex prover (clarifying the brief)
- Status at last mention: recorded as a correction/clarification; no further work
- Content: "The odd-degree bond/cohomology modes are fermionic in the grading. The physical letters of this tensor are even. These are different uses of 'fermionic.'" And: the physical vector has Schmidt rank one — "its norm realizes the counts, but its basis configurations do not enumerate the points of the curve."
- Lead: none stated. But it is the gap between a *norm* realisation and a *state* realisation: a tensor whose basis configurations enumerate rational points would be a much stronger object, and nothing in the campaign produced one.
- Related: L04-015, L04-012

### L04-014 The Koopman/Fourier picture: an injection with one finite orbit, and a flat (not trace-class) Lefschetz trace
- Source: `astra-brief.md`:15 (T1(d), drafted as "a permutation"); `astra-proofs.md`:333–355 (Theorem T1.4), 1113–1114 (ledger items 8, 9); `numerics.md`:53–55, :333
- Raised by: orchestrator (drafted); corrected by codex prover; box-checked numerically
- Status at last mention: proved, with the drafted word "permutation" declared wrong
- Content: `U(e_k (x) omega) = e_{M^T k} (x) Lambda^*(M^T) omega`; `M^T` on `Z^2` is injective of index q, **not** a permutation (Haar pullback is an isometry but not surjective). Its only finite orbit is `{0}`, since `ker(M^{nT} - 1) = 0` over Q. The Fourier-diagonal flat supertrace `sum_{k fixed} str Lambda^*(M^{nT}) = det(1 - M^{nT}) = N_n` is contributed by `k = 0` alone, and is a distributional Lefschetz trace, not an ordinary Hilbert-space trace. Numerics checked directly that the box `[-50,50]^2` has no periodic point but 0 for periods <= 12.
- Lead: "the count lives in the boundary (bond) alone" — i.e. for a variety the physical index carries no counting information at all. If the Riemann analogue has the same shape, the whole content sits in the bond and the physical alphabet is decorative.
- Related: L04-015, L04-050

### L04-015 An honest but redundant infinite-label Fourier tensor
- Source: `astra-proofs.md`:356–372 (Proposition T1.5), 1114 (ledger item 9)
- Raised by: codex prover (answering "say explicitly what this does and does not give as an MPS tensor with physical index")
- Status at last mention: proved-here, and explicitly declared to add nothing
- Content: `A_k = |M^T k><k| (x) F` with `F = diag(1, pi)` and `k` in `Z^2` is a genuine lattice tensor on `l^2(Z^2) (x) V`; all ring amplitudes vanish unless every physical label is 0, and the survivor is `1 - pi^n`, so the ring vector is `(1 - pi^n)|0,...,0>` with norm `N_n`. "This construction adds no pointwise arithmetic information to the singleton tensor in T1.3. It does not realize the exponential-sum amplitudes of T0.C."
- Lead: none stated. Recorded as a dead end for "MPS with physical index".
- Related: L04-013, L04-014

### L04-016 The PH operator for an elliptic curve: RH as a conformal similarity of the flat torus
- Source: `astra-brief.md`:15 (T1(e)); `astra-proofs.md`:374–397 (Theorem T1.6), 1118 (ledger item 13); `sources.md`:585–638 (Hodge positivity provenance)
- Raised by: TJO/orchestrator
- Status at last mention: proved, conditional on H-DEURING, H-DEG, H-FROB; reviewer VALID
- Content: the PH Hilbert space is `H^1(T^2, C)` with the Hodge metric and the PH unitary is `U_PH = q^{-1/2} M^* | H^1`; it is unitary because the lifted Frobenius `z -> pi z` is a conformal similarity of ratio `|pi|`, whose oriented area ratio `|pi|^2` is the covering degree q. Positivity enters as the positive definite degree form `deg(m + n pi) = m^2 + a mn + q n^2`, whose determinant `q - a^2/4 > 0` gives `a^2 < 4q` — Hasse's discriminant argument, derived rather than assumed.
- Lead: reviewer m1 asks for H-DEG to be split into H-DEG-GEO (lattice geometry) and H-DEG-ARITH (`deg Frob = q`, preserved under good reduction) so that "RH for E is forced by its degree" becomes a theorem of the file rather than a restatement of its hypothesis. Applied in shard `thm:elliptic-ph-unitary`; one polish line still open (review:752–754).
- Related: L04-045, L04-053

### L04-017 A self-adjoint PH Hamiltonian needs a phase branch the curve does not supply
- Source: `astra-proofs.md`:394 (remark after T1.6), 1035 (T4.7 `<1>5`), 1117 (ledger item 12)
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "If a self-adjoint 'Hamiltonian' rather than a unitary is required, choose a spectral logarithm `H_PH` with `e^{i H_PH} = U_PH`. Its phases are defined modulo `2 pi`; the curve does not specify that branch."
- Lead: this is a real obstruction to the *Hilbert* half of Polya–Hilbert for varieties: the arithmetic gives a unitary, and promoting it to a Hamiltonian needs extra data. For the Riemann case the branch would be the height itself — worth asking what on the finite-field side plays the role of the height.
- Related: L04-016, L04-045

### L04-018 Integral ideal classes are not complex MPS gauge orbits
- Source: `astra-brief.md`:15 (T1(f)); `astra-proofs.md`:398–419 (Proposition T1.7), 1119 (ledger item 14); `numerics.md`:66–68
- Raised by: TJO ("remember the gauge freedom"); corrected by codex prover
- Status at last mention: proved; the drafted identification "gauge orbits = isomorphism classes of curves" is dead
- Content: `GL_2(Z)` conjugacy of the integral matrix is the ideal-lattice class (Latimer–MacDuffee, with *all* full ideal lattices for a nonmaximal order, not only invertible ones); Waterhouse strata the isogeny class by endomorphism order. But over C all matrices in the isogeny class are `GL_2(C)`-conjugate, so "complex spectral data forget these ideal classes", and the T1.3 tensor is already identical throughout the isogeny class. Also: the cohomological matrix is `M^T` on the *dual* lattice, and exchanging the two Hodge embeddings is not an even ket gauge.
- Lead: an arithmetically faithful tensor would need integral structure kept, not just the spectrum — an unexplored direction (a "Z-form" of the MPS tensor whose gauge group is `GL_2(Z)`).
- Related: L04-003, L04-047, L04-054

### L04-019 The condition number of the Hodge basis as a quantitative "amount of gauge needed"
- Source: `numerics.md`:42–48 (table column `cond(V)`), :66–68
- Raised by: numerics lane (Opus)
- Status at last mention: computed once, never used again
- Content: for each of five curves the condition number of `V = [v_pi, v_barpi]` is tabulated (2.32 … 3.51): "it is O(1) but never 1 — the integral basis is never the Hodge-orthonormal one, which is exactly T1(f)'s point that the unitary gauge is a complex, not an integral, change of basis."
- Lead: `cond(V)` is a computable invariant of the isogeny class measuring how far the arithmetic basis is from the Ramanujan/unitary basis. Nobody asked what it is as a function of the discriminant, or whether it has arithmetic meaning.
- Related: L04-018, L04-003

### L04-020 Lenstra's O-module structure — verified, but only for conductor-1 orders
- Source: `astra-brief.md`:9 (H-LENSTRA); `astra-proofs.md`:266 (scope caveat: "No canonical choice of these isomorphisms, compatible for all n, is part of this input"), 1154; `numerics.md`:72–93 (N2); `sources.md`:261–302
- Raised by: orchestrator; scope-limited by prover and numerics lane
- Status at last mention: consistent; untested outside conductor 1
- Content: `E(F_{q^n}) = O/(pi^n - 1)O` as O-modules, checked by brute-force group structure against Smith normal form for three curves at n = 1,2,3. But: "For all five curves `disc(Z[pi])` is already a fundamental discriminant (conductor f = 1), so `Z[pi] = O_K = End(E)`."
- Lead: two untried things — (a) a curve with conductor f > 1, where `Z[pi] != O`, to see whether the tensor construction cares; (b) the *compatible-for-all-n* choice of isomorphisms, which Lenstra does not supply and which a genuine ring/transfer picture would need.
- Related: L04-004, L04-021

### L04-021 pi-adic digits, cyclic carries, and the failure of surjectivity
- Source: `astra-brief.md`:17 (T2); `astra-proofs.md`:422–447 (Proposition T2.1), 467 (Correction), 1120–1121 (ledger items 15, 16); review:510–514 (C/verdict), :168–174 (m6)
- Raised by: TJO/orchestrator ("Optional but valuable")
- Status at last mention: proved-here, with the brief's expected reason corrected
- Content: every class in `O/pi^n O` has a unique digit expansion `sum d_i pi^i`; two words agree in the *cyclic* quotient `O/(pi^n - 1)` exactly when integral cyclic carries exist, and those carries are **bounded**: `|c_i| <= C_D/(|pi| - 1)`. So the cyclic equivalence relation *is* recognised by a finite automaton. Surjectivity nonetheless fails: for `O = Z[i]`, `pi = 1 + 2i` (the curve `y^2 = x^3 + x` over F_5), `O/(pi - 1) = O/(2i)` has four classes but the digits `{0, +-1, +-2}` hit only two; and `|1 - pi^2|^2 = 32 > 25`, so no five-digit alphabet can surject at n = 2.
- Lead: the honest question left open — what *does* the carry automaton compute, and is there a weighted/graded version of it whose ring trace is `N_n`? See L04-022.
- Related: L04-022, L04-004

### L04-022 No ungraded finite or trace-class automaton counts N_n; a graded 2|2 transfer does
- Source: `astra-brief.md`:17; `astra-proofs.md`:448–470 (Proposition T2.2), 465 (`<1>3`), 1122 (ledger item 17)
- Raised by: orchestrator (via `thm:no-ungraded-trace`); executed by codex prover
- Status at last mention: pursued, negative for the ungraded case; the graded replacement is recorded but flagged as not yet a norm tensor
- Content: a residue argument on `sum_n Tr(B^n) u^n` shows no finite matrix and (by Lidskii) no trace-class operator has power traces `N_n`. But "A finite **graded weighted** transfer does suffice: on an abstract 2|2 transfer space take `diag(1,q)` even and the integral Frobenius matrix M odd. Its supertrace is `N_n`." Crucial caveat (ledger 17): "A supermatrix alone is also not a proof of a doubled-Kraus factorization" — being a *supertrace* is cheap; being a *ring norm* `sum A (x) conj A` is the real content.
- Lead: find the missing bridge — a carry automaton with signs whose signed ring count is `N_n` *and* which factors as `sum_s A_s (x) conj(A_s)`. Nothing was attempted.
- Related: L04-021, L04-012

### L04-023 The drafted Hilbert–Schmidt/trace bound for the bosonic no-go is FALSE
- Source: `astra-brief.md`:19 (T3(a) as drafted); `astra-proofs.md`:473–518 (Theorem T3.1), 514 (`<1>5` counterexample), 516 (the script mislabelling), 1123–1124 (ledger items 18, 19); `numerics.md`:218–239 (b'), :337, :357; review:252–273 (C1–C3), :436
- Raised by: orchestrator (drafted); refuted independently by the numerics lane and the codex prover; confirmed by the reviewer
- Status at last mention: dead route, with an exact one-line counterexample
- Content: the drafted chain ended `<= 2 Tr(E_{++}) Tr(E_{--})`, but `Tr(sum_s A_s (x) conj A_s) = sum_s |Tr A_s|^2`, **not** `sum_s ||A_s||_HS^2`. Counterexample: one species, m = k = 2, `a = B = diag(1,-1)`; both traces are 0 so the drafted right side is 0, while `sum_odd |mu|^2 = 8`. On 400 random purely bosonic `C^{1|2}` instances the drafted bound failed 173 times. The supplied numerical script `weil_ring_norm_check.py` computed `tpp`/`tmm` as sums of squared Frobenius norms while its comments called them block traces — exactly the mislabelling.
- Lead: the reviewer's C2 verdict: "the correction is right and is not an over-correction". The repaired bound `sum_odd |mu|^2 <= 2 tau_+ tau_-` holds on all 400.
- Related: L04-024, L04-028

### L04-024 The repaired bosonic genus bound: word traces, Cauchy–Schwarz at every n, and a Cesaro average
- Source: `astra-proofs.md`:520–538 (Lemma T3.2), 540–563 (Theorem T3.3), 1125 (ledger item 20); review:275–292 (C4–C6), :527–534
- Raised by: codex prover (replacing the broken argument)
- Status at last mention: registered and proved-here; reviewer calls it "the load-bearing repair"
- Content: with `a_w`, `B_w` the length-n words, `Tr S_+^n = sum_w |Tr a_w|^2 >= 0`, `Tr M^n = sum_w Tr(a_w) conj(Tr B_w)`, so `|Tr M^n|^2 <= Tr S_+^n · Tr S_-^n` for every n by Cauchy–Schwarz. With even spectrum `{1,q}` and no cancellation each block carries exactly one of `1,q`, so `|sum_j beta_j^n|^2 <= 1` with `|beta_j| = 1`; the Cesaro mean of the left side tends to `sum_i m_i^2 >= g`, whence `g <= 1`.
- Lead: this is the campaign's cleanest structural theorem and the reason fermions are forced at genus two. It is stated for finite bonds with no cancellation; the two escapes are L04-027 (cancellation) and L04-028 (infinite bond).
- Related: L04-023, L04-027, L04-028

### L04-025 What equality really forces: word-trace vectors, not matrix proportionality — and nilpotent transients are invisible
- Source: `astra-proofs.md`:557–561 (T3.3 `<1>5` and the following remark), 1126 (ledger item 21); review:294–301 (C7)
- Raised by: orchestrator (drafted "M normal and B_s = c a_s"); corrected by codex prover
- Status at last mention: drafted version dead; corrected version proved
- Content: two explicit counterexamples: (a) m=1, k=3, `B_0 = pi (+) 0_2`, `B_1 = 0 (+) e_12` with `a_1 = 0` but `B_1 != 0`; (b) m=1, k=2, `B_0 = [[pi, b],[0,0]]` with `b != 0`, giving a non-normal M with the correct elliptic spectra (`||[M,M^*]|| = 2.32`). "Nilpotent transient data are invisible to these traces."
- Lead: this is a free-parameter direction nobody exploited. Nilpotent transients cost bond dimension but no counting constraint — could they be used to hide the extra structure a *natural* genus-two tensor would need?
- Related: L04-026, L04-035

### L04-026 The Euler-characteristic bookkeeping and the true minimal bond
- Source: `astra-brief.md`:19 (T3(c)); `astra-proofs.md`:565–587 (Proposition T3.4), 1127 (ledger item 22); `numerics.md`:340; review:536–540
- Raised by: orchestrator (drafted "minimal bond C^{1|g}"); corrected by codex prover
- Status at last mention: proved-here
- Content: `(m-k)^2 - (z_e - z_o) = 2 - 2g`, the Euler characteristic. Necessarily `mk >= g`. If the odd dimension is exactly 2g then `mk = g`, there are no odd zero modes and no cancellation, and the even zero primary subspace has dimension `m^2 + k^2 - 2` (so `g^2 - 1` nilpotents on `C^{1|g}`). Correction: `C^{1|g}` is natural only if the even ket is *stipulated* to be a single vacuum line; the true minimum of `m + k` subject to `mk >= g` is not `g + 1` (at g = 4, `2|2` has dimension 4 and beats `1|4`'s 5). Genus two does need bond dimension 3.
- Lead: for genus >= 4 the natural-looking `1|g` bond is *not* minimal; nobody looked at whether the `m|k` bonds with `m, k > 1` have a cohomological meaning (a non-vacuum even sector).
- Related: L04-029, L04-037

### L04-027 Even–odd cancellation as the remaining escape from the bosonic bound
- Source: `astra-brief.md`:19 (T3(d), "say whether it excludes anything"); `astra-proofs.md`:589–612 (Proposition T3.5), 610, 1128 (ledger item 23), 1182; `numerics.md`:166–167 (B3, B4 fail); review:542–545
- Raised by: orchestrator; answered "does not exclude anything" by codex prover
- Status at last mention: open — explicitly on the open list
- Content: with cancellation the constraints become `s_+(n) + s_-(n) = 1 + q^n + sum_x x^n` and `|Tr M^n|^2 <= s_+(n) s_-(n)`; "These do not imply a genus bound independent of X." So fermionic species are proved necessary **only on the minimal genus-two bond 1|2**, which has no room for cancellation. "The unsuccessful bosonic 2|2 search is not a nonexistence certificate."
- Lead: either construct a purely bosonic genus-two tensor on a larger bond with cancelling spectrum, or prove none exists. This decides whether "fermions are forced" is a theorem or an artefact of minimality — and the same question is the crux for the Riemann case.
- Related: L04-024, L04-028, L04-060

### L04-028 The infinite-bond bosonic no-go for the Riemann cMPS, with the honest constant
- Source: `astra-brief.md`:19 (T3(e)), :23 (T5(ii)); `astra-proofs.md`:87 (H-KRAUS-HS), 614–643 (Theorem T3.6), 641, 1074–1080 (Observation T5.2), 1130 (ledger item 25), 1182; review:547–552, :612–614
- Raised by: orchestrator (drafted with `2 Tr S_+ Tr S_-`); repaired by codex prover
- Status at last mention: conditional-on H-KRAUS-HS and H-ZERO; existence still open
- Content: if the zeros are the odd modes of a cMPS transfer semigroup with an all-even (bosonic) Kraus decomposition, then `sum_rho e^{2t Re mu_rho} <= ||E_o(t)||_HS^2 <= 2 ||S_+(t)||_HS ||S_-(t)||_HS < infinity`, while the left side diverges (infinitely many zeros, real parts in a bounded interval). Hence fermionic jump operators are forced *in that analytic setting*. The drafted `2 Tr S_+ Tr S_-` is only valid if `S_+-` are additionally positive self-adjoint on the Hilbert–Schmidt spaces — "Complete positivity of the underlying Kraus map alone does not imply that extra property."
- Lead: the two ways out are explicitly named: "an infinite-bond construction could instead fail the trace-class/CP-extension assumptions." Establishing H-KRAUS-HS for a proposed Riemann cMPS, or constructing a fermionic one, "is not done here". This is the campaign's main transfer of a finite-field lesson to the Phantasm.
- Related: L04-024, L04-027, L04-048, L04-051

### L04-029 The genus-two ket space C (+) H^{1,0} is the exterior algebra *truncated* after degree one
- Source: `astra-brief.md`:21 (T4 proposal); `astra-proofs.md`:645–651, 1131 (ledger item 26)
- Raised by: orchestrator (proposal); qualified by codex prover
- Status at last mention: partially explored — the vector-space identification is valid, the naive spectral placement is not
- Content: `V = C (+) H^{1,0}(J~) = C^{1|2}`; its double has even dimension 5 and odd 4. "Unlike the elliptic case, it is the exterior algebra **truncated after degree one**. ... it is not already the cohomology of the curve." The three excess even dimensions are the traceless part of `End(H^{1,0})`, and "Spectra do not locate these modes canonically."
- Lead: the natural-tensor rule of L04-012 does not extend. Either find the right ket space for genus two (not a truncated exterior algebra), or accept that the genus-two tensor is a fitted object. Unresolved.
- Related: L04-012, L04-031, L04-044

### L04-030 The genus-two block equations, with rank N <= number of odd species
- Source: `astra-brief.md`:21 (T4(a), block formulas); `astra-proofs.md`:652–686 (Lemma T4.1); `numerics.md`:116–130; review:304–310 (C8)
- Raised by: orchestrator; index conventions fixed by numerics and prover
- Status at last mention: proved-here, verified to 1.7e-16 by two independent builds
- Content: `E_o = [[M, N],[conj N, conj M]]` with `M = sum_s a_s conj(B_s)` (even species only) and `N = sum_f conj(d_f) c_f` (odd species only); `E_e = [[t, u],[v, W]]` with `t = sum|a_s|^2`, `u = sum_f c_f (x) conj c_f`, `v = sum_f d_f (x) conj d_f`, `W = sum_s B_s (x) conj B_s`. Detail the brief left implicit (numerics:127): `N_{ji} = sum_f conj((d_f)_j)(c_f)_i`, so **rank N <= number of odd species**.
- Lead: the rank bound is what kills one-fermion ansatzes (L04-032, L04-033) — a cheap counting tool for screening ansatzes before any optimisation.
- Related: L04-032, L04-033

### L04-031 The literal geometric placement of the genus-two eigenvectors is impossible
- Source: `astra-proofs.md`:688–708 (Proposition T4.2), 706, 1131 (ledger item 26); review:394–404 (C18), :559–562
- Raised by: orchestrator (proposed `q` on the polarisation trace line, vacuum line carrying 1); refuted by codex prover
- Status at last mention: dead as proposed
- Content: if `0 (+) I_2` were the `q`-eigenvector then `sum_f ||c_f||^2 = 0`, so all `c_f = 0` and `N = 0`; if the vacuum line were invariant then all `d_f = 0`. In either case deleting all odd species leaves the *same* spectra, producing a purely bosonic genus-two tensor without cancellation — contradicting T3.3. "This also shows that both directions of fermionic coupling must occur somewhere in any such realization." The surviving even eigenvectors must *mix* vacuum and polarisation trace.
- Lead: the mixing is explicit in T4.3 (`(sqrt2, I_2)` and `(-sqrt2, I_2)`); nobody asked whether that mixing has a geometric meaning.
- Related: L04-029, L04-037

### L04-032 The suggested genus-two ansatz (a_1 = 1, B_1 = 0, a_2 = 0) is dead on arrival
- Source: `astra-brief.md`:21 ("A suggested ansatz"); `astra-proofs.md`:704 (T4.2 `<1>3`), 1132 (ledger item 27); `numerics.md`:154 (S1), :169–176, :343, :359–361; review:401–404
- Raised by: orchestrator (suggested); refuted independently by numerics and prover
- Status at last mention: dead, unconditionally, with a proof
- Content: `a_1 = 1, B_1 = 0, a_2 = 0` force `M = sum_s a_s conj(B_s) = 0`; then `E_o = [[0, N],[conj N, 0]]` is similar to `-E_o` via `diag(I,-I)`, so its spectrum is symmetric under `z -> -z` and its trace is 0. The Frobenius multiset of the test curve is not negation-closed (`min_{j,k} |alpha_j + alpha_k| = 0.791288 > 0`) and has trace 3. "So **no** tensor of that shape can work, for any curve whose `{alpha_j}` is not closed under negation — i.e. for every ordinary curve with `e_1 != 0`." With one odd species, `N` has rank <= 1 so `E_o` has rank <= 2 in a four-dimensional sector.
- Lead: none — this is a clean refutation. Record so nobody re-tries a "vacuum species" first.
- Related: L04-030, L04-033

### L04-033 A vacuum species is compatible with two fermionic species, never with one
- Source: `numerics.md`:154–184 (ansatz table S1–S9), :344–345, :362–365
- Raised by: numerics lane (Opus)
- Status at last mention: pursued; positive for 3 even + 2 odd (S9, cost 1.8e-25), negative for every single-fermion variant
- Content: every ansatz with `a_1 = 1, B_1 = 0` and a single odd species fails, with 2 or 3 even species and every structured `B_2` tried. "They all stall in the same place: `t = sum_s |a_s|^2 -> q = 5` and `spec M -> {conj pi_1, conj pi_2}`, i.e. the optimiser is dragged to the Hodge-natural M and then cannot repair the even sector, because `t + Tr W` must be `1 + q = 6` while t alone has already reached 5."
- Lead: "The species count is not a free parameter of the construction — it interacts with the structure imposed." The concrete unexplored question: is there a *theorem* behind the numerical stalling (vacuum species + one fermion impossible for every ordinary genus-two curve)?
- Related: L04-030, L04-032, L04-034, L04-036

### L04-034 The CM-diagonal ansatz — the campaign's most promising shape for a closed form
- Source: `numerics.md`:186–216, :346–347, :366–369
- Raised by: numerics lane (Opus) — "New positive result"
- Status at last mention: pursued, positive with two odd species (D22, cost 5.1e-26); negative with one (D21, D31); never taken further
- Content: take every even tensor simultaneously diagonal, `A_s = diag(a_s, b_{s,1}, b_{s,2})` — "the direct generalisation of the genus-1 tensor `A_s = diag(a_s, alpha a_s)`" — with odd species unrestricted. With two odd species it solves exactly (even spectrum `{1,5,0,0,0}`, odd spectrum exactly the four `alpha_j`). "In that ansatz the whole even sector is encoded in the 3x3 Gram matrix of `(a, b_1, b_2)` in the species index, and `M = diag(<b_1,a>, <b_2,a>)` is diagonal." Labelled "the most promising shape for a closed form".
- Lead: this is the clearest unfinished lead in the lane. The prover never worked on it (T4.3 and T4.5a use different shapes). The next step: solve the CM-diagonal equations symbolically — the unknowns reduce to a 3x3 Gram matrix plus two rank-one odd couplings, which is small enough for exact algebra.
- Related: L04-012, L04-035, L04-041

### L04-035 The solution set is a positive-dimensional variety; a closed form needs an extra principle
- Source: `numerics.md`:137–143, :193–216, :348; `astra-proofs.md`:765, 972, 818
- Raised by: numerics lane (Opus); echoed by codex prover
- Status at last mention: recorded as the campaign's central negative finding for Tier B
- Content: three independent restarts of the free 2-even-1-odd ansatz reach cost < 1e-25 with `t = 3.5380, 3.3681, 4.0115` and "completely different `spec M` and `c·d`". "**The solution set is a positive-dimensional family that is not a single gauge orbit**, so no individual entry ... can be read off." Attempts to recognise entries (moduli, phases relative to `pi_j`, ratios to `sqrt q`, `u_{ii} v_{ii}`, `|N_{ii}|`, `N_{12} N_{21}`) "produced **no** stable pattern tied to q". Honest summary: "the campaign's hoped-for closed form is not there ... Any closed-form tensor will have to be singled out by an extra principle (Hodge metric / Rosati positivity / a normalisation of the physical index), not by the counts alone."
- Lead: the three candidate extra principles are named and none was tried. Imposing Hodge-metric normality, or Rosati self-adjointness, as an *extra equation* on the feasibility system of L04-040 is the obvious experiment.
- Related: L04-034, L04-040, L04-041, L04-046

### L04-036 M is not the Hodge Frobenius in any small-q solution: the cohomological branch is a saddle
- Source: `numerics.md`:203–210, :370–375; review:212–225 (m10), :447
- Raised by: numerics lane (Opus) — "Surprise 5"; scope-reconciled by the reviewer
- Status at last mention: recorded; the apparent conflict with T4.3 resolved as a scope difference
- Content: in every genus-two solution found at q = 5, `M != diag(conj pi_1, conj pi_2)` and `|m_i|^2 != q` (e.g. 1.028, 1.378 against q = 5); "the four Frobenius eigenvalues are produced by the interplay of M (rank 2) and N (rank 2), not by M alone." The `M = conj D, N = 0` picture from cohomology "is a saddle that every failing search is attracted to ... and no solution reaches. Whatever makes RH manifest for this tensor, it is not the odd block being `sqrt q` times a unitary by construction." Reviewer m10: no contradiction with T4.3, because T4.3 needs `q + 1 >= 4 sqrt q` (fails at q = 5: 6 < 8.944) and 5 even + 4 odd letters.
- Lead: the reviewer asks that the lab book record explicitly that the `M = conj D, N = 0` branch is "provably available for q >= 16 and numerically unreachable at q = 5 with few species". The unexplored question: is there a *threshold in species count* at small q above which the cohomological branch reappears?
- Related: L04-033, L04-035, L04-037, L04-045

### L04-037 The nine-letter closed-form genus-two tensor for q + 1 >= 4 sqrt q, and its C^{1|g} extension
- Source: `astra-proofs.md`:710–769 (Theorem T4.3), 767 (the `C^{1|g}` sentence), 1134 (ledger item 29); review:312–338 (C9–C12), :564–568
- Raised by: codex prover (replacing the drafted three-species theorem)
- Status at last mention: registered and proved (shard `thm:nine-letter-tensor`); reviewer VALID, rebuilt independently at nine values of q
- Content: with `t = (q+1)/2`, `w = (q+1)/4`, `h = (q-1)/(2 sqrt 2)`, `B_0 = D/sqrt t` (`D = diag(pi_1, pi_2)`), `R = w I_4 - b_0 b_0^*` and `S = R^{1/2}` in closed form, five even and four odd letters give even spectrum `{1, q, 0, 0, 0}` and odd block exactly `diag(conj D, D)`; the full transfer is *normal*. The three zero modes are exactly the traceless 2x2 operators, killed in one step. Condition (4.3) `q + 1 >= 4 sqrt q` holds for every prime power `q >= 16`. Extension: on `C^{1|g}`, `t = (q+1)/2`, `w = (q+1)/(2g)`, `h = (q-1)/(2 sqrt g)`, `g^2 + 1` even and `2g` odd letters, whenever `q + 1 >= 2g sqrt q` (verified for g = 3).
- Lead: honest gap stated by the prover: "no equation-local geometric meaning for its nine letters has been established" and "Physical species number is not claimed minimal." Two concrete next steps: (a) small-q genus two beyond the certified example; (b) a geometric reading of the nine letters.
- Related: L04-038, L04-039, L04-041, L04-042

### L04-038 The field-size threshold is exactly the Weil lower bound, and the split is ansatz-optimal
- Source: review:324–330 (C11), :439; `astra-proofs.md`:710–714
- Raised by: Opus reviewer ("Two favourable structural facts the author did not state")
- Status at last mention: raised, not yet written into the file
- Content: (i) `q + 1 >= 2g sqrt q` is *exactly* `q + 1 - 2g sqrt q >= 0`, i.e. nonnegativity of the Weil **lower** bound on `N_1`. (ii) the symmetric split `t = wg = (q+1)/2` is optimal for the ansatz: the even 2x2 block is `[[t, h sqrt g],[h sqrt g, wg]]` with `t + wg = q+1` and `t·wg - h^2 g = q`, and positivity of R is `t(q + 1 - t) >= g^2 q`, maximised at `t = (q+1)/2` giving `(q+1)^2 >= 4 g^2 q`. "So (4.3) is the best this construction can do, not an artefact of a lazy choice. Worth recording."
- Lead: the coincidence with the Weil lower bound is suggestive and unexplained — if `N_1 = 0` the construction dies, which hints that the obstruction is about the curve *having* points rather than about the method. Worth chasing.
- Related: L04-037, L04-041

### L04-039 Base change to reach the large-field regime
- Source: `astra-proofs.md`:771–794 (Proposition T4.4), 792; review:340–346 (C13)
- Raised by: codex prover
- Status at last mention: proved-here; used as the bridge from the supplied F_5 curve into T4.3's scope
- Content: the supplied genus-two curve over `F_{25}` has `chi_{F^2}(z) = z^4 + 5z^3 + 9z^2 + 125z + 625`, so `q = 25 >= 16` and T4.3 applies exactly. Simplicity and ordinarity survive: both quartics reduce mod 2 to `Phi_5`, irreducible over F_2; Newton slopes are unchanged under finite base extension.
- Lead: base change as a *general* trick — every ordinary curve reaches `q >= 16` after a finite extension, so T4.3 gives a tensor for `N_{nm}` for a fixed m. The unanswered question: can the `F_{q^m}` tensor be descended to one for `N_n` over `F_q`?
- Related: L04-037, L04-041

### L04-040 The genus-two problem as an exact real feasibility system, with algebraicity for free
- Source: `astra-brief.md`:21 ("if you find that no tensor with entries algebraic over Q(pi_1,pi_2) exists ... say so"); `astra-proofs.md`:796–820 (Proposition T4.5), 1135 (ledger item 30); review:573–576
- Raised by: orchestrator (the algebraicity question); reformulated by codex prover
- Status at last mention: proved-here (equivalence); algebraicity conditional on H-RCF
- Content: for two even and one odd species the existence question is exactly the real polynomial system `det(z I_5 - E_e) = z^3(z-1)(z-q)`, `det(z I_4 - E_o) = chi_F(z)` in 28 real unknowns. By real-closed-field transfer, if any complex solution exists then an algebraic one does — "Thus one cannot legitimately claim that 'only transcendental tensor entries work' for this fixed finite species class." Also the sharp methodological point: a least-squares residual of 4e-24 plus four-decimal printed matrices "do not certify (4.9)".
- Lead: 28 unknowns and 9 equations is within reach of Groebner/cylindrical decomposition with the CM structure imposed; nobody tried symbolic elimination. That, not optimisation, is the route to L04-041.
- Related: L04-035, L04-041, L04-042

### L04-041 Conjecture T4.C: a universal three-species genus-two tensor, and the selection problem
- Source: `astra-proofs.md`:822, 1133 (ledger item 28), 1182; review:701–704
- Raised by: orchestrator (drafted as a theorem to prove); demoted to a conjecture by codex prover
- Status at last mention: open
- Content: "For every ordinary simple genus-two curve, (4.9) has a solution with two even letters and one odd letter." Proved for the supplied F_5 curve only (T4.5a). A *second*, separate open requirement: "Whether those entries can be selected naturally from the equation or the polarized CM data is a further unresolved requirement."
- Lead: the two halves should be attacked separately — existence for all ordinary genus-two data (a real-algebraic-geometry question), and natural selection (a geometric question). The CM-diagonal ansatz of L04-034 is the best current handle on the second.
- Related: L04-034, L04-035, L04-040, L04-042

### L04-042 The certified exact three-letter tensor for the F_5 curve (rational contraction certificate)
- Source: `astra-proofs.md`:824–974 (Theorem T4.5a), 972, 1133; review:348–392 (C14–C17), :578–584
- Raised by: codex prover
- Status at last mention: registered and proved (shard `thm:f5-certified-tensor`); reviewer: "This is the strongest result in the file and it holds up completely"
- Content: two even and one odd tensor on `C^{1|2}` with `chi_e(z) = z^3(z-1)(z-5)` and `chi_o(z) = z^4 - 3z^3 + 7z^2 - 15z + 25`, hence `||Psi_P(n)||^2 = N_n(C)` for *every* n. Existence is proved by a Krawczyk-style rational contraction: nine active coordinates, radius `10^{-30}`, exact rational `f(y_0)` and Jacobian, verified `||B||_inf < 2`, `||B f(y_0)||_inf < 10^{-70}`, `||I - BJ||_inf < 10^{-50}`, uniform Hessian bound `H = 10^16`. Independently re-run by the reviewer (`B norm 1.49913`, `eta 1.01e-90`, `eps 3.52e-58`), and the explicit Jordan–Wigner Fock vector gives `31, 117, 619, 3318` for n = 2..5.
- Lead: the prover's own limits: the certificate "does not give the frozen entries a natural geometric meaning, identify a canonical physical alphabet, or settle a universal three-species formula". Also: it proves existence with three letters but "does not prove that three letters are the minimum possible". The certificate technique itself generalises — it could certify a whole family if applied to a parametrised system.
- Related: L04-040, L04-041, L04-043

### L04-043 Numerical diagnostics for a triple zero mode: use the characteristic polynomial, not the eigenvalues
- Source: `numerics.md`:111–114; review:184–195 (m7)
- Raised by: numerics lane; re-raised as a fix request by the reviewer
- Status at last mention: recorded as a fix to apply; not blocking
- Content: the three nilpotent even modes show up as eigenvalues of modulus ~6e-5, "the **cube root** of the least-squares residual — the signature of a genuine 3x3 nilpotent Jordan block, not of sloppy convergence. A naive 1e-5 threshold misreads this as five nonzero eigenvalues." The reviewer notes the certified T4.5a tensor shows the same `~1e-5` "zeros" in double precision, so the file's own criticism of the supplied search would otherwise read as applying to its own certificate; the right diagnostic is `chi_e = [1,-6,5,0,0,0]` to 1e-10.
- Lead: adopt "characteristic polynomial / Newton power sums" as the standard acceptance test for every future tensor search in the notebook.
- Related: L04-042, L04-040

### L04-044 The Jacobian product tensor, and why extracting the curve needs a non-product boundary
- Source: `astra-brief.md`:3(v), :21 (T4(b)); `astra-proofs.md`:977–1009 (Proposition T4.6), 1136–1137 (ledger items 31, 32); `numerics.md`:241–249 (N3(d)); review:586–593
- Raised by: orchestrator; proved with corrections by codex prover
- Status at last mention: proved-here
- Content: the tensor product of g elliptic bonds with singleton tensors `diag(1, pi_j)` has `||Psi||^2 = prod_j |1 - pi_j^n|^2 = #J(F_{q^n})`, its double being `H^*(J) = Lambda^* H^1(J)`. Inside it sits a Frobenius-invariant graded subspace `S = C1 (+) H^1(J) (+) C omega` (`omega = e_1^f_1 + e_2^f_2`, `F omega = q omega`) with `str F^n|_S = N_n(C)`. But the rank-six projector onto S is **not** of the form `B (x) conj B'`: the five listed vectors force each factor to have dimension >= 3, so a product range would have dimension >= 9 > 6. Corrections: `i^*` is restriction, not a subalgebra inclusion, and for a principally polarised abelian surface `int_J theta^2 = 2`, so `i^* theta = 2[pt]` and the *line*, not its unscaled generator, is `H^2(C)`.
- Lead: a non-product boundary is a real structure — an entangled boundary condition on a ring. Nobody asked what physical operation on the ring it is, or whether the Riemann case needs one.
- Related: L04-029, L04-012

### L04-045 Rosati positivity derives the Ramanujan property — the one place in the campaign where RH is proved rather than assumed
- Source: `astra-brief.md`:21 (T4(c)); `astra-proofs.md`:1011–1039 (Theorem T4.7), 1138 (ledger item 33); review:595–601, :699–701
- Raised by: orchestrator; proved by codex prover
- Status at last mention: proved-here (the placewise involution and modulus implication), conditional on H-CM, H-ROSATI, H-CM-POL
- Content: Rosati is an R-algebra involution of `K (x) R = C^g`; positivity forbids it from permuting distinct primitive idempotents (`Tr(e_j e_k) = 0`) and from being the identity on a factor (`(i e_j)(i e_j)^dagger = -e_j` has trace -2), so it is complex conjugation at each place; applying the embeddings to `pi pi^dagger = q` gives `|phi_j(pi)|^2 = q` at *every* place. Crucially: "Total degree in dimension two would only give `|pi_1|^2 |pi_2|^2 = q^2`; it does not supply the two separate equalities."
- Lead: the reviewer singles this out: "this is the one place in the file where RH is *derived* rather than assumed ... unlike T1.6 it does not have the conclusion inside its hypotheses." The Phantasm lead: find the Riemann-side analogue of a *positive involution on a commutative algebra*, whose positivity forces conjugation place by place.
- Related: L04-046, L04-016, L04-055

### L04-046 Where RH would have to enter the tensor, and why it does not
- Source: `astra-proofs.md`:1037 (T4.7 closing paragraph), 1138; `numerics.md`:370–375
- Raised by: TJO/orchestrator ("Be honest: ... say where it would have to enter the tensor"); answered by codex prover
- Status at last mention: honest negative; open
- Content: "For the tensor of T4.3, the odd transfer is already `diag(conj D, D)`; hence it is `sqrt q` times a unitary **by construction**. RH is made manifest *after* the Frobenius eigenvalues and their moduli have been supplied. The structural arithmetic proof of those moduli is Rosati positivity, not complete positivity of an arbitrary MPS transfer." For curves the corresponding positivity is the Hodge index theorem on `C x C`; "no separate tensor derivation of that positivity is established here." For the certified T4.5a tensor the odd roots are distinct so it is *similar* to `sqrt 5` times a unitary, but "Its polynomial equations do not specify the arithmetic Hodge metric or show that this similarity is induced by an even ket gauge. That missing metric identification is distinct from the now-proved count identity."
- Lead: the sharpest unfinished question in the lane — is there a *metric* on the bond, determined by the curve, in which a counting tensor is automatically normal with odd block `sqrt q` times unitary? That would be RH from complete positivity.
- Related: L04-045, L04-035, L04-036

### L04-047 The CM type is arithmetic marking, not gauge
- Source: `astra-brief.md`:21 (T4(d)); `astra-proofs.md`:1041–1060 (Proposition T4.8), 1139 (ledger item 34); review:603–606
- Raised by: orchestrator; sharpened by codex prover
- Status at last mention: proved-here
- Content: even bond gauge cannot change `spec M` (the scalar `g_0` cancels from the mixed sector), so replacing a selected `pi_j` by `conj pi_j` is not a gauge transformation. "Changing the whole CM type exchanges the holomorphic and antiholomorphic assignments; changing only part of the type exchanges the corresponding lines, not necessarily the entire mixed sectors." And: "For a general solution of (4.9) with `N != 0`, the odd eigenmodes can mix the two coherences. Counts alone do not recover a marked CM-type half from that tensor." Same-parity unitary rotations of the physical letters leave E exactly invariant — a separate, useful freedom.
- Lead: the CM type is extra data a *natural* tensor would have to encode. Since the counts cannot see it, any selection principle (L04-035) must come from the metric.
- Related: L04-035, L04-046, L04-003

### L04-048 The candidate bond for zeta: C (+) one odd mode per positive-height zero
- Source: `astra-brief.md`:23 (T5(i)); `astra-proofs.md`:1064–1072 (Observation T5.1), 1140 (ledger item 35); review:608–610
- Raised by: TJO/orchestrator
- Status at last mention: open, explicitly an observation not a construction
- Content: "A plausible ket space is `C (+) H_{>0}`, where `H_{>0}` has one odd mode per positive-height nontrivial zero, with multiplicity. The bra would supply conjugate modes." Two named problems: (a) "Its `(-,-)` sector is much larger than the desired pole sector; what kills, cancels, or regularizes those modes remains unspecified. Archimedean/trivial-zero modes require their own bookkeeping." (b) ket/bra exchange is complex conjugation, while the functional equation is `rho -> 1 - rho`; these agree only on the critical line, so "Treating the full functional equation as automatic ket/bra exchange would put RH into the interpretation. An additional duality is needed before that inference is available."
- Lead: find the extra duality. Also: the `(-,-)` sector problem is concrete — in the elliptic case `(-,-)` carried exactly `H^2` with eigenvalue q, so the question is what plays the role of `H^2` for zeta.
- Related: L04-012, L04-027, L04-050

### L04-049 Fermionic jumps are necessary but nothing says they suffice
- Source: `astra-brief.md`:23 (T5(ii)); `astra-proofs.md`:1074–1080 (Observation T5.2)
- Raised by: orchestrator; qualified by codex prover
- Status at last mention: conditional obstruction only; existence open
- Content: "T3.6 excludes the all-even Kraus class in that analytic setting. Thus a realization retaining those assumptions needs odd jumps. It does not follow that odd jumps suffice, that their number is finite, or that a distributional regularization is an ordinary Hilbert norm. The finite-bond theorem H-TWIST supplies none of these infinite-dimensional assertions."
- Lead: three separate missing pieces named — sufficiency, finiteness of the number of odd jumps, and whether the regularized object is a Hilbert norm at all.
- Related: L04-028, L04-052

### L04-050 No lifted Riemann dynamics, no positive metric — the substantive break in the analogy
- Source: `astra-brief.md`:23 (T5(iii)); `astra-proofs.md`:1082–1090 (Observation T5.3); review:616–617
- Raised by: TJO/orchestrator; sharpened by codex prover
- Status at last mention: sketched comparison; the proposed Riemann lift is open
- Content: for an ordinary elliptic curve the lifted Frobenius gives an injective Fourier shift whose only finite cycle is the zero label, and the flat Lefschetz supertrace sits in that fibre. But this does not generalise into a principle: "even in this example the shift is not surjective, and for an abelian surface the full torus counts the Jacobian, not the curve." And: "No analogous lifted Riemann dynamics, positive Hodge/Rosati metric, or physical-label construction is established. That missing dynamics and positivity, rather than the formal notation for a supertrace, is the substantive break in the analogy."
- Lead: the two things to look for are named precisely — a lifted dynamics (a space with a map whose Lefschetz data are the zeta zeros) and a positive metric on its `H^1`. This is the Phantasm restated in finite-field language.
- Related: L04-011, L04-014, L04-045, L04-048

### L04-051 The locality dichotomy must be restricted; infinite-bond cMPS as the research target
- Source: `astra-brief.md`:23 (T5(iv)); `astra-proofs.md`:1092–1100 (Observation T5.4), 1141 (ledger item 36); review:619–621
- Raised by: orchestrator (drafted as a dichotomy); refuted in its literal form by codex prover
- Status at last mention: dead as drafted; the restricted version is Conjecture T0.C
- Content: "The literal claim 'fixed finite lattice tensors give only supersingular zetas' is false: T1.3 gives ordinary elliptic counts with a fixed two-dimensional bond, and T4.3 gives ordinary genus-two examples with a fixed three-dimensional bond." What survives is only the equation-local amplitude conjecture T0.C. Dwork's infinite-dimensional arithmetic transfer is "one established framework in the background; no theorem here makes it necessary for every ordinary norm realization or identifies it with a Hilbert-space MPS bond." Positive part: "Infinitely many distinct zeta zeros themselves motivate an infinite spectral space. Dilation time motivates a continuous formulation. Together they make an infinite-bond cMPS a reasonable research target, but neither supplies the missing analytic domains, regularized trace, tensor factorization, or positivity."
- Lead: four concrete conjectural requirements are itemised (analytic domains, regularized trace, tensor factorization, positivity) — a checklist for any proposed Riemann cMPS.
- Related: L04-009, L04-028, L04-048

### L04-052 Split H-TWIST into its unconditional algebraic half and its sketched physical half
- Source: review:73–103 (MAJ-2), :434, :628, :767–782 (post-fix); `astra-proofs.md`:47–52 (H-TWIST as stated), 1162
- Raised by: Opus reviewer
- Status at last mention: applied in the shards (`def:graded-lattice-tensor` + `cor:genus-two-physical-norm`); one strengthening still available
- Content: `||Psi_P(n)||^2 = str_Gamma E^n = sum_w |Tr(P A_w)|^2` glues two things. The second equality is unconditional and two lines long. The first — the Hilbert norm of the physical periodic-fermion ring — is `thm:cmps-twisted-supertrace` in shard 04f, where *every* theorem carries `claimstatus sketched-conditional`. Splitting it makes T4.3 and T4.5a unconditional matrix theorems modulo H-FROB, with only their physical reading inheriting the sketched status. The reviewer verified both halves numerically (algebraic half to 1e-10 for a mixed 1|2 tensor; physical half against the Jordan–Wigner Fock vector to 5e-13).
- Lead: the remaining strengthening (review:774–782): the shards still hedge the algebraic identity to "all-even letters", but it is **unconditional including odd letters**, since `E^n = sum_w A_w (x) conj A_w` by ordinary Kronecker multiplicativity and no statistics sign is inserted. "The shards are therefore conservative, not wrong; the hedge can be dropped."
- Related: L04-042, L04-022

### L04-053 Split H-DEG so that "RH for E is forced by its degree" becomes a theorem
- Source: review:109–124 (m1), :747–754 (post-fix); `sources.md`:162–200, :649
- Raised by: Opus reviewer, backed by the sources lane
- Status at last mention: applied in `thm:elliptic-ph-unitary`; one polish line open
- Content: H-DEG as quoted from the brief ends "...**so `|pi|^2 = deg(Frobenius) = q`**", and that final clause *is* RH for elliptic curves, making T1.6 look circular. Fix: split into H-DEG-GEO (`[Lambda : pi Lambda] = |pi|^2 = N_{K/Q}(pi)`, pure lattice geometry) and H-DEG-ARITH (`deg Frob = q`, preserved under good reduction). The sources lane already needed three separate quotes for H-DEG, and "the split matches the quotes one-for-one".
- Lead: remaining polish — say explicitly that the clause used from `cit:hasse-degree-bound` is `d = deg(pi) = q`, **not** `c^2 <= 4d`, "a half-sentence saying so would make the non-circularity self-evident to a reader who sees Hasse's bound sitting in the same citedfact."
- Related: L04-016

### L04-054 H-WAT needs a j-invariant / quadratic-twist gloss
- Source: review:148–156 (m4), :742–745 (post-fix); `sources.md`:355–428, :653
- Raised by: sources lane, escalated by the reviewer
- Status at last mention: applied in `prop:integral-marking-gauge`
- Content: the quotable source indexes `Ell_O(k)` by **j-invariants**, not F_q-isomorphism classes, and those differ by quadratic twists; also it is a `cl(O)`-torsor, so the bijection is not canonical without a base point. "No arXiv source states H-WAT as a single proposition; cite Waterhouse 1969 §7 directly for the sharp form."
- Lead: none beyond the citation fix.
- Related: L04-018

### L04-055 H-CM's eigenspace clause is not quotable from arXiv — the one provenance hole under T4.7
- Source: review:158–166 (m5); `sources.md`:430–488, :654
- Raised by: sources lane; escalated by the reviewer
- Status at last mention: raised, fix requested (mark `assumed (named-not-quoted)`), not confirmed applied
- Content: the clause actually used — `H^1(A~(C),C) = (+)_phi C_phi` with `H^{1,0} = (+)_{phi in Phi} C_phi` and `pi~` acting on `C_phi` by `phi(pi)` — "is NOT quotable from arXiv — assumed (Shimura–Taniyama; Lang, *Complex Multiplication*, Ch. 1)". T4.7 `<1>3`–`<1>4` and T4.6 `<1>2` rest on it. The reviewer stresses this is provenance, not a gap in the argument.
- Lead: mark H-CM `assumed (named-not-quoted)` in the provenance table "before promoting T4.7 past conditional-on".
- Related: L04-045, L04-044

### L04-056 H-SCHUR has no arXiv source; prove it instead
- Source: `sources.md`:557–577, :656; `astra-proofs.md`:501 (proved in T3.1 `<1>2`); review:523–525
- Raised by: sources lane; acted on by the codex prover
- Status at last mention: closed — the prover proved it from Schur triangularisation, "which closes the sources lane's 'no arXiv source' gap"
- Content: exhaustive arXiv searching for a quotable statement of `sum |mu_i|^2 <= ||M||_HS^2` with the normality equality case found nothing; the lane recommended proving it in one line, which T3.1 does.
- Lead: a general policy hint for the notebook — when no byte-verifiable source exists, prove rather than cite.
- Related: L04-023

### L04-057 Three further provenance gaps left as "assumed"
- Source: `sources.md`:148–160 (Deuring), :252–259 (general Lefschetz), :627–638 (general Hodge inner product), :648, :650, :658
- Raised by: sources lane (Opus)
- Status at last mention: recorded as assumed; no follow-up
- Content: (a) no arXiv source states Deuring's 1941 lifting theorem in its own form — the campaign uses the Serre–Tate canonical lift plus Deligne's equivalence instead; cite Deuring 1941 or Lang, *Elliptic Functions* Ch. 13 §5. (b) the general manifold Lefschetz fixed-point theorem is not stated in the toral source; cite Dold VII.6. (c) the general Hodge-star `L^2` inner product on k-forms is not stated; the source gives only the second Riemann bilinear relation (positive definiteness of `i int omega ^ conj omega` on `H^{1,0}`); cite Griffiths–Harris Ch. 0 §6 or Warner Ch. 6 if the general case is needed.
- Lead: none; bookkeeping so the notebook knows which citations are named-but-not-quoted.
- Related: L04-016, L04-011

### L04-058 Caveat on a very recent preprint used only for attribution
- Source: `sources.md`:359–363
- Raised by: sources lane (Opus)
- Status at last mention: recorded
- Content: arXiv 2605.07626 (el Baraka–Ezzouak, 2026) is cited only for joint attribution of the order stratification to Deuring 1941 + Waterhouse 1969. "**Caveat**: this is a very recent, unrefereed preprint whose front matter contains typographic errors; use it only for attribution, never as the authority for a proof."
- Lead: none; a standing warning.
- Related: L04-054

### L04-059 Small fixes and scope repairs flagged by the reviewer
- Source: review:126–146 (m2, m3), :168–174 (m6), :197–202 (m8), :204–210 (m9), :732–740 (post-fix)
- Raised by: Opus reviewer
- Status at last mention: m2, m3 applied; m6, m8, m9 recorded as minor and not blocking
- Content: m2 — T0.2's hypotheses say `J >= 1` while its statement and proof cover `J = 0`; change to `J >= 0`. m3 — the displayed radical operator is right only because `b, a_j` lie in F_q and are fixed by `x -> x^q`; say so. m6 — T2.1 `<1>2`'s "the same congruence argument applies at each step" is too terse; the clean route is the cyclic shift `(pi^n - 1) c_i = sum_j (d_{i+j} - e_{i+j}) pi^j`, reduced mod pi, giving integrality uniformly in i. m8 — at the boundary `w = nu` the four `B_ell` are generically nonzero but linearly dependent, not zero. m9 — the certificate runs in 0.17 s not 55 s; the displayed `kappa` uses the looser `||B|| < 2`; T0.1's title understates its supersingularity conclusion.
- Lead: none beyond applying them.
- Related: L04-006, L04-021, L04-037

### L04-060 The catalogue of failed genus-two ansatzes
- Source: `astra-brief.md`:3 (prior numerics: "one even plus one odd and one even plus two odd species failed; purely bosonic C^{1|2} fails; purely bosonic C^{2|2} (cancellation allowed) was not found"); `numerics.md`:152–167 (table S1–S9, D21, D31, B3, B4), :343–348; `astra-proofs.md`:813 ("Failures of the one-even search variants likewise do not prove their nonexistence"), 1133
- Raised by: orchestrator (prior numerics) and numerics lane; scope-limited by codex prover
- Status at last mention: recorded as searches, explicitly **not** as nonexistence proofs
- Content: fourteen ansatzes tried with 5–10 random restarts and bounds +-4: S1–S8 (vacuum variants), D21, D31 (CM-diagonal with one odd), B3, B4 (purely bosonic with 3 and 4 even species) all failed at costs `4e-2` to `7e0`; only S9 (3 even + 2 odd, vacuum) and D22 (2 even + 2 odd, CM-diagonal) solved. The prover's standing caveat: "Failed smaller-species searches prove no lower bound on species count."
- Lead: only S1 has an unconditional refutation (L04-032). Everything else is a failed search and could be re-tried with a better parametrisation — in particular B3/B4 bear directly on the open cancellation question L04-027.
- Related: L04-027, L04-032, L04-033, L04-034

---

## Small but possibly consequential

1. **L04-034 (CM-diagonal ansatz)** — the only ansatz called "the most promising shape for a closed form", solved numerically, and then never touched again by the prover; its unknowns reduce to a 3x3 Gram matrix, small enough for exact algebra.
2. **L04-038 (threshold = Weil lower bound)** — the reviewer noticed that `q + 1 >= 2g sqrt q` is exactly `N_1 >= 0` by the Weil lower bound; an unexplained coincidence that might say the construction fails precisely when the curve has no points.
3. **L04-019 (condition number of the Hodge basis)** — a computable number measuring how far the arithmetic basis is from the Ramanujan basis; tabulated once, never interpreted.
4. **L04-025 (nilpotent transients are invisible to all the trace constraints)** — free parameters that cost bond dimension but satisfy no counting equation; a possible hiding place for the extra structure a natural tensor needs.
5. **L04-017 (a PH Hamiltonian needs a phase branch the curve does not supply)** — a genuine obstruction to the Hilbert half of Polya–Hilbert for varieties, mentioned twice in passing and never pursued.
6. **L04-022 (a graded 2|2 supermatrix has supertrace N_n but is not shown to be a ring norm)** — the gap between "signed transfer" and "doubled-Kraus factorisation" is exactly the gap the Phantasm has to close.
7. **L04-044 (the curve projector is not a product `B (x) conj B'`)** — an entangled boundary condition on a ring, with no physical interpretation attempted.
8. **L04-039 (base change into the q >= 16 regime)** — every ordinary curve reaches T4.3's scope after a finite extension; whether the extension tensor descends was never asked.

## Dead routes recorded

- **The drafted bosonic bound `sum_odd |mu|^2 <= 2 Tr(E_{++}) Tr(E_{--})` is FALSE.** One-species counterexample `a = B = diag(1,-1)` on `C^{2|2}`: right side 0, left side 8. `astra-proofs.md`:495, :514; `numerics.md`:218–239; review:258–264. (The genus bound itself survives via the repaired word-trace argument, L04-024.)
- **The drafted genus-two ansatz `a_1 = 1, B_1 = 0, a_2 = 0` cannot work for any ordinary curve with nonzero Frobenius trace** — it forces `M = 0` and a negation-symmetric odd spectrum. `astra-proofs.md`:704; `numerics.md`:169–176; review:401–404.
- **A vacuum species together with a single fermionic species fails for the test curve**, with 2 or 3 bosonic species and every structured `B_2` tried (numerically, not proved). `numerics.md`:178–184, :344.
- **The CM-diagonal ansatz with one odd species fails** (D21, D31). `numerics.md`:163–164, :347.
- **Purely bosonic genus-two on `C^{1|2}` fails** (B3 with 3 even species, B4 with 4 even species). `numerics.md`:166–167. Proved impossible without cancellation by T3.3; *not* proved on larger bonds (`astra-proofs.md`:610).
- **The cut-rank bound "at most D" for a ring is wrong**; it is `D^2` for a contiguous cut and the bound is sharp. `astra-proofs.md`:150, :158–160, :1109.
- **"The permutation `k -> M^T k` of `Z^2`" is not a permutation** — `M^T` is injective of index q; Koopman pullback is an isometry but not a unitary surjection. `astra-proofs.md`:180, :1113.
- **"Fixed finite lattice tensors give only supersingular zeta functions" is false**, refuted by the campaign's own T1.3 (ordinary elliptic, bond `C^{1|1}`) and T4.3 (ordinary genus two, bond `C^{1|2}`). `astra-proofs.md`:1096, :1141; review:619–621.
- **The failure of a finite carry automaton is NOT unboundedness of cyclic carries** — in this expanding complex base the carries are bounded by `C_D/(sqrt q - 1)`; the failure is that recognising equality of digit words is not counting quotient classes with weight one. `astra-proofs.md`:467, :1121.
- **The digit map `D^n -> O/(pi^n - 1)` need not be onto**, for cardinality reasons and otherwise: `O = Z[i]`, `pi = 1 + 2i`, digits `{0, +-1, +-2}` hit 2 of 4 classes at n = 1, and `|1 - pi^2|^2 = 32 > 25` at n = 2. `astra-proofs.md`:285 (T2.1 `<1>4`), :1120.
- **Do not double the cohomology twice** — the ket exterior *half* doubles to full cohomology; using full cohomology as the ket and then taking a norm squares the wrong object. `astra-proofs.md`:1115.
- **`0 (+) I_2` (the polarisation trace line) cannot be the `q`-eigenvector, and the vacuum line cannot be invariant**, on the minimal genus-two bond — either would let the odd species be deleted, contradicting the bosonic no-go. `astra-proofs.md`:698–702, :1131.
- **"Only transcendental tensor entries work" is not a legitimate conclusion** — by real-closed-field transfer, if a complex solution of the feasibility system exists then an algebraic one does. `astra-proofs.md`:811, :1135.
- **Small least-squares residuals and four-decimal printed matrices are not certificates** — "Fitting many positive powers is compatible with small unwanted eigenvalues and with poorly conditioned nilpotent limits." `astra-proofs.md`:813.
- **Equality in the genus-one case does not give matrix proportionality or normality** — only proportionality of word-trace vectors at every length; two explicit counterexamples with nilpotent transients and a non-normal M. `astra-proofs.md`:557–561, :1126.
- **The minimum bond for genus g is not `C^{1|g}` in general** — the condition is `mk >= g` and at g = 4 the bond `2|2` (dimension 4) beats `1|4` (dimension 5). `astra-proofs.md`:571–573, :1127.
- **Bra/ket conjugation does not implement the functional equation** — `conj(rho) = 1 - rho` only on the critical line, so identifying the two "would put RH into the interpretation". `astra-proofs.md`:1070, :1140.
- **The growing cut ranks `2,4,8,16,8,4,2` at n = 8 are basis noise**, not evidence of unboundedness; in a self-dual normal basis the quadratic amplitude has cut rank `<= 4` for every n. review:33–71; `numerics.md`:315–322; `astra-proofs.md`:1110 (ledger item 5, to be reworded).
- **Integral ideal classes (Latimer–MacDuffee / Waterhouse) are not complex MPS gauge orbits** — complex tensors forget the ideal class entirely. `astra-proofs.md`:1119.
- **The root-of-unity phase of the Artin–Schreier transfer does not follow from "the entries are roots of unity"** (there are zero entries and a `q^{-1/2}`); the Fourier–phase–permutation determinant argument is needed. `astra-proofs.md`:109, :1107.
