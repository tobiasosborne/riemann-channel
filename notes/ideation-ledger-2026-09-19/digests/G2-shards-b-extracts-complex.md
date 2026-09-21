# Digest G2: shards 05-11, source extracts, complex zeta / Ihara / BC symmetry

Merges three lanes: `L13-shards-05-11.md` (157 entries), `L11-source-extracts.md` (118),
`L08-complex-zeta-ihara-bc-symmetry.md` (81). Total 356 lane entries, all absorbed.

## Themes

1. **T1 The Weil--LPS finite model** --- the one exactly-Ramanujan quantum expander the notebook owns, and what it still owes (Hecke identification, assembly over primes).
2. **T2 Artin--Schreier curves as a supertrace transfer** --- sign law, Weil-representation unitary, the quadratic/cubic locality wall, the even-`n` sign.
3. **T3 Ring-norm tensors, genus by genus** --- TJO's five-item wish list, genus 1 lifted Frobenius, genus 2 nine/three-letter tensors, entanglement and parent Hamiltonians.
4. **T4 Why the bond must be graded** --- the bosonic no-goes at finite and infinite bond, and the exact hypothesis (trace, not positivity).
5. **T5 Every zeta condition imposed factor by factor** --- the C1--C10 ledger, tiny `L`-functions, explicit cMPS, and what a finite bond cannot reach.
6. **T6 Deligne via graphs: where Ramanujan-ness comes from** --- products, slicing, the minus sign, the abelian obstruction, and "positivity plus a multiplying operation" instead of Hermiticity.
7. **T7 The general quantum Ihara--Bass machine** --- Theorem 1 for arbitrary superoperators, unconditional side-A positivity, RH-iff-Hastings, and the open non-paired case.
8. **T8 Weil positivity, discrete and continuous** --- a bound without a duality, a circle with one, Jordan blocks, PT symmetry, Huang/Herglotz prior art and the converse gap.
9. **T9 A zeta of a simplicial complex: scope and construction** --- buildings only, the universal rational Bass--Schur compression, the tetrahedron obstruction, the vertex-collapse conjecture.
10. **T10 The graded presentation and "fermionic zeros"** --- the exact superdeterminant identity and every qualification that guts the naive reading.
11. **T11 Quantum twists of complexes** --- pure gauge vs voltage quotients, Artin bookkeeping, Harrow transfer, and the Ã2 numerics with their anomaly.
12. **T12 Higher-rank RH is a band, not a line** --- one-sided bounds, Kamber's `L_p` continuum, absent duality, and the surface-vs-curve two-expression shape.
13. **T13 Torsion and supertrace in the literature** --- one alternating-product shape in five categories, Knill vs Ihara, the fermionic proof of Bass, the three origin stories of the `chi` exponent.
14. **T14 Deninger, Connes and fermionic cMPS** --- the grading the arithmetic already forces, the Polya--Hilbert space "from its negative", and the novelty boundary.
15. **T15 The Weil window and its extension** --- the window as an exact compression, the extension disc, integrality, and why a better estimator for `zeta` means more primes.
16. **T16 Selberg, Lindbladians and the modular surface** --- transverse expansion as the missing ingredient, the Casimir Lindbladian, the tower, the cusp-as-prime-comb.
17. **T17 Prior art and novelty** --- what is claimed new, and how weak the negative searches are.
18. **T18 Bost--Connes symmetry generators** --- the GKLS cone at the critical state, the collapse under full symmetry, and the p=7 counterexample.
19. **T19 Bookkeeping, notation and reproducibility.**

---

## Items

### G2-T1-1 Hecke identification of the Weil--LPS joint spectra
- Absorbs: L13-001, L13-005, L11-059
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: The two commuting Weil--LPS channels `Phi_q^±` at a fixed odd prime `p` have a joint spectrum of small-degree algebraic integers; for `(p;q1,q2)=(13;17,29)` the even block has 19 distinct pairs `(a_17,a_29)`, some integral, one quadratic in `Q(sqrt 17)`. The conjecture is that these pairs are Hecke eigenvalues `a_q(f)` of weight-2 forms for the quaternion algebra ramified at `{2,infty}` with level determined by `p`, via Jacquet--Langlands. Four features were already checked numerically: algebraicity (not a test --- the Cayley matrix is integral by construction), multiplicities equal to the multiplicity of the corresponding irreducible of `PSL_2(F_p)` in `W^± ⊗ conj W^±`, and every pair inside the box `[-2sqrt q1, 2sqrt q1] x [-2sqrt q2, 2sqrt q2]`.
- Lead: run the LMFDB + Jacquet--Langlands lookup. Cheaper partial test first: verify the multiplicity prediction representation by representation, which needs no LMFDB. If the match holds, the finite model's spectrum *is* modular-form data and the Ramanujan property is derived from modularity rather than checked.
- Where: report/sections/05_weil_lps_channels.tex:225-264, :246-252; notes/extract/notation-and-definitions.md:303

### G2-T1-2 Assembling the Weil--LPS channels over all primes
- Absorbs: L13-002, L11-060
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: Nothing is known about `p -> infinity`, or about assembling the `Phi_q` over all `p` into a single object whose rings are the rational primes. The shard calls this "the parent repository's global question in a new guise" (the DG-GLOBAL question).
- Lead: build the direct integral / inductive limit over `p` and ask whether the assembled object has a zeta whose primes are the rational primes. This is the step that would turn a family of finite Ramanujan channels into something with a chance of seeing the actual zeros --- side A and side B joined.
- Where: report/sections/05_weil_lps_channels.tex:290-299; notes/extract/notation-and-definitions.md:304

### G2-T1-3 The exactly-Ramanujan claim, and the one unverified source near it
- Absorbs: L13-003, L13-138, L08-050
- Class: PARTIAL
- Raised by: orchestrator / paper
- What: `prop:weil-lps-exactly-ramanujan` is two lines --- Harrow's transfer inequality plus Lubotzky--Phillips--Sarnak, giving `(q+1)lambda_2(Phi_q^±) <= 2 sqrt q` in adjacency units. It is registered `sketched` only because LPS has no byte-verified local source in `refs/` and because irreducibility of the even/odd Weil blocks `W^±` plus the Step-4 projective-phase bookkeeping are verified numerically, not cited. The mechanism (Harrow 2008 + LPS) is known prior art; the *Weil-representation instance* is not, and Iyer--Jain--Jordan--Somma (Feb 2026) call explicit Ramanujan quantum expanders "a longstanding open problem". One source sits uncomfortably close: Ben-Aroya--Schwartz--Ta-Shma were read (publisher PDF only, no local TeX) as believing "their first construction has the potential of being improved to a quantum Ramanujan expander".
- Lead: fetch a quotable LPS source and prove or cite irreducibility of `W^±`; separately verify the Ben-Aroya--Schwartz--Ta-Shma remark, since if their construction reaches the bound the novelty claim needs adjusting. Noted coincidence: the Iyer et al. Appendix C example `p=5, D=6` uses the same norm-5 quaternions as `scripts/weil_lps.py`.
- Where: report/sections/05_weil_lps_channels.tex:101-128; report/sections/09_prior_art.tex:249-253; notes/prior-art-quantum-ihara.md:12,:83-96

### G2-T1-4 The honest row: these channels are Ramanujan because of Deligne
- Absorbs: L13-004, L11-076
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: The reading table maps commuting prime dilations to commuting Hecke channels, the Weil representation to `W^±` on `l^2(F_p)`, joint spectrum to Hecke eigenvalues, RH to `|eps| = sqrt q`. The last row is "source of the bound: unknown" versus "source of the bound: Deligne, via LPS". The channels are exactly Ramanujan *because Deligne proved the Weil conjectures*, not because they are channels. Sharpened further: the LPS Ramanujan property needs only the **curve** case (Eichler--Shimura transports Hecke eigenvalues to Frobenius eigenvalues of a modular curve), so Weil's theorem suffices; Deligne's method is needed only for higher weight.
- Lead: none --- this is the standing complaint that motivates every search for a channel-internal reason for the bound. Any claimed channel-theoretic explanation must add something beyond transporting Deligne.
- Where: report/sections/05_weil_lps_channels.tex:266-288; notes/extract/notation-and-definitions.md:305,:329

### G2-T1-5 The quantum Ihara zeta of the Weil--LPS channel has poles only
- Absorbs: L13-006
- Class: EXPLORED-registered
- Raised by: prover (correction applied 2026-09-15)
- What: For `(13,17)`, odd block, the edge superoperator on `M_6 ⊗ C^18` has `|eps| in {17, sqrt 17, 1}` with multiplicities `1, 70, 577`, satisfying Ihara--Bass to `1e-14`, so every nontrivial pole sits on the critical circle. The wording was corrected: the *ungraded* quantum Ihara zeta has poles only, no zeros --- the sign asymmetry of shard 07.
- Lead: for every other admissible pair the same conclusion follows from the quadratic `eps^2 - lambda eps + q = 0` without building the edge operator, so the expensive computation never has to be repeated.
- Where: report/sections/05_weil_lps_channels.tex:196-223

### G2-T1-6 The finite model of the Riemann channel exists and self-checks
- Absorbs: L13-007
- Class: EXPLORED-registered
- Raised by: TJO (founding session) / orchestrator
- What: The programme item was to build a finite object with every ingredient of the Riemann channel present and checkable: commuting dilations indexed by primes, an arithmetic quotient supplying expansion, and the Weil representation as the Hilbert space. Achieved; cheap to build; self-checks at every step; lands on the parent campaign's Hilbert space with the parent campaign's representation.
- Lead: none beyond G2-T1-1 and G2-T1-2.
- Where: report/sections/05_weil_lps_channels.tex:12-19, :266-288

### G2-T2-1 Dwork's p-adic operator is a coarse-graining tensor-network step --- and cannot give RH
- Absorbs: L13-008, L11-065
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: For non-quadratic `g` the Artin--Schreier trace form in the shift basis is non-local and `n`-dependent, so no fixed local tensor exists. The uniform transfer operator that *does* exist is Dwork's `alpha = psi_q ∘ M_F`, which has exactly the shape of a coarse-graining step ("local weight, then decimate by `q`"), with infinite but nuclear bond dimension and `L` as a Fredholm determinant, giving `S_n^x = (q^n-1) Tr(alpha^n)`. It delivers rationality and the functional equation but not RH, because the Newton polygon it computes is a statement about `p`-adic valuations, not complex absolute values --- which is why Deligne's proof lives in `l`-adic cohomology.
- Lead: dead for RH; still live as a template for "transfer operator with nuclear bond dimension" if the notebook ever wants an infinite-bond lattice model.
- Where: report/sections/06_artin_schreier_mps.tex:176-197; notes/extract/notation-and-definitions.md:314

### G2-T2-2 A basis uniform in `n` making cubic traces local --- never searched
- Absorbs: L13-009, L11-062, L11-063, L11-064
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: A self-dual normal basis makes the *bilinear* trace form local; it says nothing about the trilinear one, where `Tr(x^3) = sum_{ijk} c_{ijk} x_i x_j x_k` has `n`-dependent structure constants. The notebook records the quadratic/cubic dividing line as sharp *in the shift basis* --- but whether some other basis of `F_{q^n}`, uniform in `n`, restores locality was explicitly never examined ("no candidate was found or searched for"). Consequently no MPS with a fixed local tensor is known for any non-quadratic Artin--Schreier curve, or for any genus `>= 1` curve not of maximal type.
- Lead: search for such a basis. If one exists the MPS formulation of the Weil conjectures extends past degree three (past the supersingular boundary) and the "sharp dividing line" dissolves; side A would get a genuinely general tensor-network model.
- Where: report/sections/06_artin_schreier_mps.tex:199-207; notes/extract/notation-and-definitions.md:313,:316,:317

### G2-T2-3 The transfer unitary is a Weil-representation operator; the Weil bound is a character bound
- Absorbs: L13-012, L13-015, L13-016, L11-061, L11-086
- Class: EXPLORED-registered
- Raised by: prover
- What: `U_g = E_g / sqrt q` factors as a Fourier transform on the retiring register, quadratic phases, and a cyclic relabelling, and satisfies an exact Egorov relation for an explicit symplectic map `M_g`; hence `U_g = e^{i phi} W(M_g)`, and `|S_n(g)| <= q^J q^{n/2}` with equality **iff `M_g^n = 1`** --- so the maximal-curve saturation observed at `n=4` for `q=3, g=x^4` is exactly the finite order of a symplectic map. The fermionic sign of the count on an `n`-site ring is the sign of the Frobenius permutation, corrected on the fixed space by the radical sign. The literature backing is Gurevich--Hadani (Egorov determines `rho` up to a scalar), Thomas's character formula `|Tr rho(g)|^2 = |F|^{dim ker(g-1)}` --- literally the point count --- and Gross/Appleby for the stabiliser dictionary. Two loose ends: `asm:weil-implementer-exact` assumes a genuine (non-projective) centred lift `W` of `Sp(2J,F_q)`, which Gurevich--Hadani give only up to scalar; and the elementary unitarity lemma `EE^† = qI` when `a_J != 0` (the oldest spin appears only in the linear term, so summing over it gives `q delta`) has a one-line proof and `1e-15` numerics but was never written as a lemma.
- Lead: (i) discharge the centred-lift assumption from a source or fix the phase cocycle --- it de-conditionalises the whole symplectic story; (ii) write the `a_J != 0` unitarity lemma with its even-`n` sign convention, cheap and load-bearing; (iii) Howe's remark that the *modulus* alone follows from `rho ⊗ rho^*` being the natural action on `L^2(V)` is a shortcut around the full character formula and is unexploited.
- Where: report/sections/06b_artin_schreier_super.tex:150-208, :171-177; report/sections/06_artin_schreier_mps.tex:116-120; notes/extract/riemann-cmps-sources.md:633-787; notes/extract/notation-and-definitions.md:315

### G2-T2-4 The exact sign law, and two refuted universal laws
- Absorbs: L13-013, L13-017
- Class: EXPLORED-registered
- Raised by: numerics lane (failures), orchestrator (failed replacement), prover (the law)
- What: The founding session's `alpha_i = -lambda_i(E)` is false in general and the orchestrator's conjugated replacement fails too. The exact law is `S_n(g) = (-1)^{n-1} delta_n Tr E_g^n` with `delta_n = det(F|rad_n)`, equivalently `S_n = (1 - 2·1_{2h | n}) Tr E_g^n`: a periodic sign that flips exactly when `2h | n`. Endpoint criteria: the first drafted law holds for all `n` iff `P_g(-1) != 0`, the second iff `P_g(-eta(-1)) != 0`. Confirmed in 624 checks. Carried assumption: `asm:as-lpolynomial` (for `deg g = q^J+1` and every `a in F_q^x`, `L(ag,u)` is a polynomial of degree exactly `q^J` with constant term 1) --- root *sizes* are deliberately not assumed, which is what keeps the supersingularity theorem free of the Weil bound; alongside `asm:normal-basis`.
- Lead: cite or prove the polynomiality assumption. Otherwise settled.
- Where: report/sections/06b_artin_schreier_super.tex:12-19, :41-108, :63-69

### G2-T2-5 The count is a supertrace and the grading is by character sector --- but only for a geometric reason
- Absorbs: L13-014, L13-018, L13-065
- Class: EXPLORED-registered
- Raised by: prover, framed by orchestrator
- What: The projective curve has `N_n = str E^n` for a super-transfer matrix whose **even block is the trivial-character sector** and whose **odd block is the nontrivial characters**; it must be a supertrace, because `cor:curve-counts-graded` forbids a trace. The odd block has `FF^† = q` and its multiset is the `2g` Frobenius eigenvalues with no even--odd cancellation. This is the concrete template for "which physical letters carry the grading": characters, not geometry. The standing caution (from the 06h C7 row): a unitary `G`-action commuting with the closure and permuting letters splits `E = ⊕_chi 1 ⊗ E_chi` and `Z = prod L(u,chi)^{dim chi}`, but calling a factor an Artin `L`-function needs an actual cover with Frobenius weights on primitive orbits, and "even = trivial, odd = nontrivial" is **geometric input, not a theorem about group actions** --- the Ihara cover in the catalogue has every mode even. `asm:frobenius-semisimple` is used only for operator similarity, never for net spectra, a deliberate quarantine.
- Lead: none stated; but the caution is the gate any "the grading is the geometry" ansatz must pass.
- Where: report/sections/06b_artin_schreier_super.tex:133-148, :125-131; report/sections/06h_zeta_conditions.tex:51-56

### G2-T2-6 The even-`n` sign: two independent parity criteria, and a textbook-only gap
- Absorbs: L11-087, L11-088
- Class: PARTIAL
- Raised by: paper / extractor
- What: The statement the notebook wants --- the discriminant of a degree-`n` separable extension is a square iff the Galois group lies in `A_n`, hence for `F_{q^n}/F_q` with `q` odd it is a square iff `n` is odd (the Frobenius `n`-cycle has sign `(-1)^{n-1}`) --- was **not found verbatim in any arXiv TeX source**. What arXiv supplies instead (Auel--Biesel--Voight) is the other Stickelberger theorem `disc Z_K = 0,1 mod 4`, whose standard proof is exactly the even/odd permutation split `disc = (P-N)^2` with `P+N` the *permanent*. Independently, Arnault--Pickett--Vinatier (quoting Lempel--Weinberger) give: `F_{q^n}/F_q` has a self-dual normal basis iff `n` is odd, or `n = 2 mod 4` with `q` even.
- Lead: cite a textbook or write the two-line proof; state the two agreeing parity criteria as evidence that the even-`n` sign is structural, not a normalisation artefact. The `(P-N)^2` / permanent split is itself a bosonic/fermionic pair worth noting.
- Where: notes/extract/riemann-cmps-sources.md:788-850, :851-878

### G2-T3-1 TJO's five-item wish list, and the standing limitation of every answer
- Absorbs: L13-019, L13-052
- Class: PARTIAL
- Raised by: TJO
- What: For the simplest variety without an *obvious* Polya--Hilbert Hamiltonian, TJO asked for (1) a natural tensor determined by the variety; (2) the graded decomposition of the bond and why; (3) a theorem that the ring norms are the counts; (4) the PH operator; (5) the Ramanujan property --- all modulo gauge. Answered as a scorecard across 06c--06g: genus 0 and 1 are one-liners, genus 2 is a closed form above `q >= 16` and a certified decimal tensor below, and every genus `g` is the same closed form on `C^{1|g}` once `q+1 >= 2g sqrt q`. TJO's follow-up asked for the actual matrices, entanglement and parent Hamiltonians at each genus, and got them.
- Lead: item (1) is unanswered above genus 1, and the standing limitation is stated bluntly: "the only input at every genus is the `L`-polynomial" --- the construction consumes the answer.
- Where: report/sections/06c_ring_norm_inputs.tex:12-31; report/sections/06g_ring_norm_examples.tex:12-22

### G2-T3-2 The obvious Polya--Hilbert Hamiltonian exists only in the supersingular world
- Absorbs: L13-020, L13-025
- Class: EXPLORED-registered
- Raised by: prover (the orchestrator's drafted reason was insufficient)
- What: Every Frobenius eigenvalue of the smooth model of `y^q - y = g(x)` for quadratic `g` is `sqrt q` times a root of unity, in every characteristic including 2. So the one place the notebook had a manifestly unitary transfer matrix is supersingular throughout. The orchestrator's drafted reason ("the entries are roots of unity") failed on zero entries and the normalisation; the prover replaced it with finite order of `E_g / sqrt q` inside `Sp(2J, F_q)`. Carried as `asm:supersingular-newton`: all Newton slopes `1/2` iff all Frobenius eigenvalues are `sqrt q` times roots of unity.
- Lead: cite the Newton/spectral equivalence. Structurally the door is closed --- go to ordinary curves, which is what genus 1 does.
- Where: report/sections/06c_ring_norm_inputs.tex:132-162, :113-119

### G2-T3-3 The natural genus-one tensor is the lifted Frobenius on the flat torus
- Absorbs: L13-026, L13-024
- Class: EXPLORED-registered
- Raised by: prover
- What: With `M` the integral matrix of the lifted Frobenius, `#Fix(M^n) = det(1-M^n) = |1-pi^n|^2 = N_n`, all fixed points nondegenerate of index `+1`, so `N_n` is a Lefschetz number and also the index `|O/(pi^n-1)O|`, which by Lenstra *is* `E(F_{q^n})` as an `O`-module. The dynamical zeta of `(T^2, M)` is the Hasse--Weil zeta: gas side and transfer side carried by one dynamical system. Rests on `asm:deuring-lift` (an ordinary `E/F_q` with `End(E)=O` lifts to a number-field curve with good reduction, reduction an isomorphism on endomorphisms, complex model `C/Lambda` with `Lambda` a proper `O`-ideal).
- Lead: the honest gap is that "the bijection is noncanonical" --- primitive periodic orbits are only *equinumerous* with closed points, not canonically matched. A canonical matching would be a real Phantasm ingredient. Also: byte-cite Deuring 1941 or use the Serre--Tate form; it is the hinge of the whole genus-one construction.
- Where: report/sections/06d_ring_norm_elliptic.tex:19-45; report/sections/06c_ring_norm_inputs.tex:65-73

### G2-T3-4 Hodge doubling is the ket/bra doubling --- but the physical state has Schmidt rank one
- Absorbs: L13-027
- Class: EXPLORED-registered
- Raised by: prover
- What: The double of the Hodge ket bond is `H^*(T^2,C)` graded by form degree, with `E = diag(1, conj pi, pi, q)` and `Gamma = diag(1,-1,-1,1)`: `(+,+) = H^0`, the mixed lines are `H^{0,1}` and `H^{1,0}`, `(-,-) = H^2` with eigenvalue `q`. That answers wish-list item (2). The limitation: the fermionic modes are the odd-degree forms, but the *physical letters are bosonic*, the physical state has Schmidt rank one, and its configurations do not enumerate points.
- Lead: find a genus-1 tensor whose physical configurations *are* the points. None was found (see G2-T3-5 and G2-T5-7).
- Where: report/sections/06d_ring_norm_elliptic.tex:48-60

### G2-T3-5 The infinite-label Fourier tensor: honest but redundant
- Absorbs: L13-028
- Class: EXPLORED-negative
- Raised by: prover
- What: The pullback `U = M^*` on `L^2(T^2) ⊗ Lambda^*(C^2)` sends `e_k ⊗ omega` to `e_{M^T k} ⊗ Lambda^*(M^T) omega`; `k -> M^T k` is injective of index `q`, **not a permutation**, and its only finite orbit is `{0}`. The infinite-label tensor `A_k = |M^T k><k| ⊗ diag(1,pi)` has `P`-closed ring vector `(1-pi^n)|0,...,0>`: an honest but redundant physical index, since every closed ring except the vacuum mode vanishes.
- Lead: none. The diagnosis "the shift is not surjective" means this is *not* evidence that every variety's tensor is a permutation.
- Where: report/sections/06d_ring_norm_elliptic.tex:62-72; report/sections/06f_ring_norm_genus_two.tex:277-284

### G2-T3-6 The genus-one Polya--Hilbert unitary, and the missing phase branch
- Absorbs: L13-029
- Class: PARTIAL
- Raised by: prover (sharpened by review item m1)
- What: `U_PH = q^{-1/2} M^*|_{H^1}` is unitary iff `|pi|^2 = q`, and that is *derived* --- the lifted Frobenius is a conformal similarity whose oriented area ratio is its covering degree --- so the Ramanujan property at genus 1 needs no root-size input. The gap: the real PH model `K ⊗_Q R ≅ C` with `Re(x conj y)` is the real form of `H^1`, not the complex `H^1`, and "a self-adjoint logarithm needs a phase branch the curve does not specify".
- Lead: find the phase branch, or accept that the PH *operator* (as opposed to the unitary) is not determined by the curve. This is exactly the obstruction to answering wish-list item (4) canonically.
- Where: report/sections/06d_ring_norm_elliptic.tex:74-89

### G2-T3-7 Gauge is the lattice basis; ideal classes and CM types are markings, not gauge
- Absorbs: L13-030, L13-046
- Class: EXPLORED-registered
- Raised by: prover (review item m4)
- What: `M` changes by `GL_2(Z)` conjugacy under a change of lattice basis; its class is an ideal-lattice class of `Z[pi]` (Latimer--MacDuffee, all full ideal lattices, not only invertible ones), and the ordinary classification is Waterhouse's torsor. **Complex spectral data forget these classes**: all matrices in the isogeny class are `GL_2(C)`-conjugate. At genus two the same thing: the even gauge `G = diag(g_0, H)` fixes all ring norms and same-parity unitary rotations of letters fix `E` itself, but replacing a selected `pi_j` by `conj pi_j` changes the mixed-sector eigenvalues and is *not* an even gauge; a coupled solution with `N != 0` mixes the two coherences and its counts do not recover a marked half.
- Lead: the arithmetic (ideal class / CM type) is strictly finer than anything the ring norms see. If the Phantasm is to be arithmetic, its data must include a **marking**, not only a spectrum. This also constrains what "modulo gauge" in TJO's wish list can mean.
- Where: report/sections/06d_ring_norm_elliptic.tex:91-103; report/sections/06f_ring_norm_genus_two.tex:242-251

### G2-T3-8 Digits in base `pi`: a finite carry automaton that cannot count
- Absorbs: L13-031, L13-032
- Class: EXPLORED-negative
- Raised by: prover (correcting an orchestrator draft)
- What: With `D` a residue system of `O/pi O`, every class of `O/pi^n O` has a unique base-`pi` expansion; the cyclic map `D^n -> O/(pi^n-1)O` need not be onto (explicit counterexample `O = Z[i]`, `pi = 1+2i`, i.e. `y^2 = x^3+x` over `F_5`). Two words have the same image iff they admit integral cyclic carries `d_i - e_i = pi c_{i+1} - c_i` with `c_n = c_0`, which are unique and **bounded** by `max|d-e|/(sqrt q - 1)` --- the drafted "carries must be unbounded" was wrong, and the cyclic equivalence has a *finite* carry automaton. But no finite weighted adjacency matrix and no trace-class operator has power traces `N_n`, so no automaton with nonnegative transition counts counts the classes of `O/(pi^n-1)` by unweighted rings. A graded signed transfer (`diag(1,q)` even, `M` odd) has supertrace `N_n` but is not by itself a doubled-Kraus factorisation.
- Lead: none. It is the cleanest small no-go for "the points are the configurations".
- Where: report/sections/06d_ring_norm_elliptic.tex:105-118, :120-129

### G2-T3-9 The genus-two assumption bundle: CM type, polarised lift, Hodge adjunction, real closure
- Absorbs: L13-040, L13-041
- Class: PARTIAL
- Raised by: prover
- What: Two `assumed` rows carry the genus-two construction. `asm:cm-hodge-type`: for simple ordinary `A/F_q` of dimension `g`, `K = Q(pi)` is CM of degree `2g`, `End(A) ⊗ Q = K`, and `H^1(tilde A(C), C) = ⊕_phi C_phi` with `H^{1,0} = ⊕_{phi in Phi} C_phi` --- explicitly flagged, "the eigenspace statement is not quotable from the fetched TeX". `asm:cm-polarised-lift` bundles four separate items: (i) a polarisation lifts along the canonical lift and identifies Rosati adjunction with adjunction for the positive Hodge form, plus curve-in-Jacobian comparison facts; (ii) `H^*(A) = Lambda^* H^1(A)` with Frobenius acting by exterior powers; (iii) a finite real semialgebraic system with a real solution has a real algebraic solution; (iv) multiplicativity of Frobenius characteristic polynomials in exact sequences and preservation of ordinarity under base extension.
- Lead: split the bundle and discharge each. Item (iii) is what makes the three-letter feasibility statement ("then an algebraic solution exists") meaningful; item on the eigenspaces needs a quotable Shimura--Taniyama source.
- Where: report/sections/06f_ring_norm_genus_two.tex:52-61, :63-75

### G2-T3-10 Dead: the literal geometric placement and the vacuum ansatz at genus two
- Absorbs: L13-039
- Class: DEAD
- Raised by: orchestrator (drafted), prover (refuted)
- What: If the odd spectrum is the four Frobenius values and the even spectrum `{1,q,0,0,0}`, then the pure trace line `0 ⊕ 1_2` is not a `q`-eigenvector and the vacuum line is not invariant --- either would force all `c_f = 0` or all `d_f = 0` and contradict the genus bound. Both coupling directions must occur. The drafted ansatz `a_1=1, B_1=0, a_2=0, B_2=B` makes `M=0` and fails for every curve with `e_1 != 0`.
- Lead: none. It rules out the "put the cohomology where it geometrically belongs" strategy.
- Where: report/sections/06f_ring_norm_genus_two.tex:89-99

### G2-T3-11 The nine-letter closed-form tensor, its threshold, and base change
- Absorbs: L13-042, L13-051
- Class: EXPLORED-registered
- Raised by: prover
- What: For `q+1 >= 4 sqrt q` (every prime power `q >= 16`) an explicit nine-letter tensor on `C^{1|2}` has even spectrum `{1,q,0,0,0}`, odd block `diag(conj D, D)`, normal transfer, and `str E^n = N_n(C)` for every `n`. The even letters realise the depolarising map, the odd letters couple vacuum and trace, and neither eigenvector is the pure vacuum nor the pure polarisation line. It generalises to `C^{1|g}` with `w = (q+1)/2g`, `h = (q-1)/(2 sqrt g)` whenever `q+1 >= 2g sqrt q`. Below threshold, base change works: the `F_5` curve has `chi_F = z^4 - 3z^3 + 7z^2 - 15z + 25`, and over `F_25` the threshold is met with first six norms `31, 619, 15991, 390739, 9759526, 244128859`; both quartics are irreducible over `Q` so both Jacobians are simple and ordinarity is preserved. Rider: "the letters have no equation-local meaning and their number is not claimed minimal."
- Lead: find letters that *do* have equation-local meaning --- wish-list item (1) at genus `>= 2`. Base change is a general way into the closed-form regime but changes the field, so it does not answer the small-`q` question.
- Where: report/sections/06f_ring_norm_genus_two.tex:103-119, :121-129

### G2-T3-12 Three letters: a finite real feasibility problem, one certified curve, and a universal conjecture
- Absorbs: L13-043, L13-044
- Class: PARTIAL
- Raised by: prover / numerics lane
- What: Two even and one odd letter on `C^{1|2}` realise `N_n(C)` for all `n` iff two characteristic polynomials match (28 real unknowns), and then an algebraic solution exists. For `y^2 = x^5 + x^3 + x^2 - 2` over `F_5` an exact rational Newton--Kantorovich contraction certificate proves existence in a box of radius `1e-30`. Methodological warning recorded verbatim: "Least-squares residuals and four-digit printouts certify nothing." `conj:three-letter-universal` then asks (a) that every ordinary simple genus-two curve's three-letter problem be solvable, and (b) that some solution be selected *naturally* by the equation or the polarised CM data. Caveat: "failed smaller-alphabet searches prove no lower bound on the number of letters."
- Lead: part (b) is the prize --- it is wish-list item (1) at genus two, and a natural selection rule would make the tensor a functor of the curve rather than of its `L`-polynomial. Part (a) is a computer-assisted existence proof for one curve, not a formula.
- Where: report/sections/06f_ring_norm_genus_two.tex:131-156, :158-165

### G2-T3-13 Rosati positivity supplies the moduli and the Polya--Hilbert metric --- but the gauge question is open
- Absorbs: L13-045
- Class: PARTIAL
- Raised by: prover
- What: For a simple ordinary polarised abelian variety, Rosati acts as complex conjugation on each factor of `K ⊗ R ≅ prod_j C`, so `pi pi^† = q` gives `|phi_j(pi)|^2 = q` at every place and `q^{-1/2} tilde pi^*` is unitary on `H^{1,0}`: the root sizes come from *positivity*, with no use of the Weil conjectures. But in the nine-letter tensor the odd block is `sqrt q` times a unitary by construction, so RH is manifest only after the moduli are supplied, and the arithmetic proof of those moduli is Rosati (Hodge index on `C x C`), not complete positivity of a transfer. For the certified tensor, "whether that similarity is an even ket gauge carrying the arithmetic Hodge metric is not determined by the count equations."
- Lead: decide the gauge question for the certified `F_5` tensor. It would say whether the *count equations alone* can carry the arithmetic metric --- the crux of whether a transfer operator can prove RH.
- Where: report/sections/06f_ring_norm_genus_two.tex:224-240

### G2-T3-14 The genus-two ring norms are Hilbert norms of fermionic ring states
- Absorbs: L13-048
- Class: PARTIAL
- Raised by: prover / orchestrator
- What: Via `thm:cmps-twisted-supertrace` on the lattice, the supertraces of the nine-letter and certified tensors are the squared norms of physical periodic-fermion rings; an explicit Jordan--Wigner check confirms it for `n <= 5`. So "the count of a genus-two curve is literally the norm of a graded matrix product state with a three-dimensional bond and a fermionic letter."
- Lead: upgrade `thm:cmps-twisted-supertrace` from sketched; then item (3) of the wish list is a theorem at genus two.
- Where: report/sections/06f_ring_norm_genus_two.tex:197-206

### G2-T3-15 The curve sits inside the Jacobian as a non-product boundary
- Absorbs: L13-049
- Class: LEAD-unpursued
- Raised by: prover
- What: The tensor product of two elliptic norm tensors has ring norm `#J(F_{q^n})`; inside it the Frobenius-invariant graded subspace `S = C1 ⊕ H^1(J) ⊕ C omega` has `str F^n|_S = N_n(C)`. But the rank-six projector onto `S` is *not* of the form `B ⊗ conj B'` (a product range would have dimension `>= 9`): extracting the curve from the Jacobian ring needs a **non-product boundary**, which single fermionic rings avoid. Rider: "This does not say every boundary with the same scalar counts is that projector."
- Lead: "bosonic product of tori plus a non-product boundary" is an alternative architecture for higher genus that was never developed.
- Where: report/sections/06f_ring_norm_genus_two.tex:210-222

### G2-T3-16 Cut rank, basis dependence, and the restricted amplitude-locality conjecture
- Absorbs: L13-022, L13-023, L13-050
- Class: PARTIAL
- Raised by: prover (cut rank), orchestrator (conjecture, then self-corrected)
- What: For letters `A_s in M_D`, the flattening rank of `Tr(A_{s_1}...A_{s_n})` across two contiguous arcs is at most `D^2`, sharply, and at most `D^b` across a bipartition cutting `b` virtual edges; the orchestrator's drafted bound `D` is the *open-chain* bound. Numerically over `F_2` the quadratic `Tr(x^3)` has cut rank `<= 4` in a self-dual normal basis but grows (16 at `n=10`) in a plain normal basis, while the cubic `Tr(x^{1+2+4})` grows `2,4,8,16`: **cut rank is basis dependent**. `conj:amplitude-locality` survives only in restricted form --- with a self-dual normal-basis prescription for every `n` and trace-invisible Artin--Schreier coboundaries quotiented out, a fixed finite lattice tensor with amplitudes `psi(Tr g(x))` for all `n` exists only when the trace function has quadratic degree over the prime field. The broad slogan "fixed finite lattice tensors give only supersingular zetas" is **explicitly false** (the Hodge doubling tensor and the nine-letter tensor are finite ordinary norm tensors). Also recorded: "Infinitely many zeros and dilation time motivate an infinite-bond cMPS, but supply none of the domains, regularised trace, tensor factorisation or positivity it would need."
- Lead: prove or refute the restricted conjecture --- it would pin the exact boundary of the MPS formulation of the Weil conjectures. Separately, supplying those four analytic ingredients *is* the analytic core of the Phantasm.
- Where: report/sections/06c_ring_norm_inputs.tex:164-187, :189-198; report/sections/06f_ring_norm_genus_two.tex:286-294

### G2-T3-17 RH as a single odd correlation length; entanglement and parent Hamiltonians at each genus
- Absorbs: L13-053, L13-054, L13-055, L13-056, L13-057, L11-077, L11-093, L08-051
- Class: PARTIAL
- Raised by: orchestrator; the MPS hierarchy is the notebook's own
- What: For any graded tensor with net even spectrum `{1,q}` and odd spectrum the Frobenius eigenvalues, the even correlation length is `1/log q` and an odd mode `alpha_j` has `1/log(q/|alpha_j|)`. Hence **RH for the curve is exactly the statement that every odd (fermionic) mode has the same correlation length `2/log q`, twice the even one** (verified to `1e-6` in five examples). The general MPS hierarchy is the same statement: one eigenvalue on the unit circle = primitivity (PNT, `zeta(1+it) != 0`); all others strictly inside = spectral gap (zero-free region); all others on *one* circle of radius `e^{-1/xi}` with `xi = 2/h` = Ramanujan/RH --- "all correlation lengths equal, and equal to twice the inverse entropy rate". The supporting machinery: the reduced state of a contiguous `l`-site block in a `P`-closed ring of length `n` has at most `D^2` nonzero Schmidt weights, equal to the spectrum of `K G_X^T`, and the Jordan--Wigner reduced state has the same spectrum (the string is a parity sign); genus 0 is a cat state with GHZ-like doubly degenerate parent Hamiltonian, genus 1 is a **product state with zero entanglement** (the whole count in the normalisation), genus `>= 2` saturates a flat spectrum (`{1/4, 1/8^{x4}, 1/16^{x4}}` for nine letters over `F_25`; `{1/4, 1/12^{x6}, 1/36^{x9}}` at genus 3). The fermionic parent Hamiltonian is **one** local Hamiltonian with Ramond and Neveu--Schwarz boundary conditions: `Psi_P` is the ground state of the version whose wrapping terms are conjugated by site parities, `Psi_1` of the untwisted one. Measured gap pairs: 0.239/0.232 (certified genus-2 letters), 0.639/0.636 (nine letters). Genus 3 has sixteen letters and was never diagonalised. The cMPS fixed point *is* the entanglement spectrum (its eigenvalues are the squared Schmidt coefficients), which is the operator on the entropy side of `xi = 2/h`. The prior-art search found no hits for Ihara/zeta with matrix product state, transfer matrix or AKLT ("AKLT = `K_4`" is unclaimed).
- Lead: the sharpest physics lead in the group --- "every fermionic mode has correlation length exactly twice the bosonic one" is attackable with physics tools (Lieb--Robinson, area laws) and was written down once and never used. Cheap companions: diagonalise the genus-3 parent Hamiltonian to extend the gap data, and close the loop between `xi = 2/h` and the entanglement spectrum by direct computation. Standing warning: the genus-1 product state shows entanglement is *not* where the arithmetic lives in the current tensors; a tensor where it is would be new.
- Where: report/sections/06g_ring_norm_examples.tex:43-56, :60-80, :82-100, :104-125, :141-142; notes/extract/notation-and-definitions.md:271, :184-251; notes/prior-art-quantum-ihara.md:14

### G2-T3-18 The candidate Phantasm bond, and the trap in reading the functional equation as ket/bra exchange
- Absorbs: L13-047
- Class: LEAD-unpursued
- Raised by: orchestrator (deliberately labelled an observation, not a theorem)
- What: A plausible ket is `C ⊕ H_{>0}` with one odd mode per positive-height zero, the bra supplying the conjugates. Two problems are stated in the same breath. First, its `(-,-)` sector is far larger than the pole sector and nothing is said about what kills or regularises those modes. Second, ket/bra exchange is complex conjugation, whereas the functional equation also involves `rho -> 1-rho`, and the two coincide on each pair **only on the critical line** --- so reading the functional equation as ket/bra exchange would *assume RH*.
- Lead: find the regularisation of the `(-,-)` sector, and a symmetry implementing `rho -> 1-rho` without presupposing RH. This is the most direct Phantasm lead in the shard group.
- Where: report/sections/06f_ring_norm_genus_two.tex:255-263

### G2-T4-1 Bosonic species cannot pass genus one
- Absorbs: L13-034, L13-033, L13-035, L13-036
- Class: EXPLORED-registered
- Raised by: prover (the orchestrator's first attempt was refuted)
- What: With `s_±(n)` the word-trace sums, `|Tr M^n|^2 <= s_+(n) s_-(n)` for every `n`. If the nonzero even spectrum is exactly `{1,q}` with no cancellation and the odd spectrum is `2g` values of modulus `sqrt q`, writing the eigenvalues of `M` as `sqrt q beta_j` gives `|sum_j beta_j^n|^2 <= 1`, whose Cesaro mean tends to `sum_i m_i^2 >= g`, forcing `g <= 1`. This is the theorem that *forces* fermions past genus 1. The earlier drafted Hilbert--Schmidt/trace bound `sum_odd |mu|^2 <= 2 Tr E_{++} Tr E_{--}` is false (173 of 400 random instances violate it; its script computed `sum_s ||a_s||_HS^2` while calling it a trace). Bookkeeping: if a graded tensor on `C^{m|k}` has `str E^n = N_n` with net spectrum `{1,q}_+ - {alpha}_-` and `z_e, z_o` zero eigenvalues, then `(m-k)^2 - (z_e - z_o) = 2-2g` and `mk >= g`; **the minimal bond dimension is `min{m+k : mk >= g}`, not generally `g+1`; at genus two it is three.** Scope narrowing: odd letters add blocks between `(+,+)` and `(-,-)` and between the mixed sectors, and a cancelling multiset makes the inequality bound nothing, so fermionic letters are necessary on the *minimal* genus-two bond `C^{1|2}` (no room to cancel), not on every larger bond --- the failed bosonic `C^{2|2}` search is no certificate.
- Lead: for an unconditional "fermions are necessary", rule out cancelling multisets on larger bonds. Not done. Apply the `mk >= g` constraint before any numerical search at higher genus --- it is free.
- Where: report/sections/06e_ring_norm_bosonic_nogo.tex:41-66, :17-26, :68-77, :79-90

### G2-T4-2 The infinite-bond bosonic no-go, its analytic assumption, and the missing sufficiency
- Absorbs: L13-037, L13-021, L13-038
- Class: PARTIAL
- Raised by: prover; reviewer MAJ-2 on the assumption
- What: Under `asm:kraus-hs-setting` and `asm:zero-count-location`, if the odd eigenmodes at time `t` include `e^{t mu_rho}` over the nontrivial zeros, then `sum_rho e^{2t Re mu_rho} <= ||E_odd(t)||_HS^2 <= 2 ||S_+||_HS ||S_-||_HS < infinity`, impossible because the left side diverges. Hence no purely bosonic Kraus realisation of the Riemann semigroup exists and fermionic jumps are necessary in that setting. The assumption is heavy and carries the explicit rider "Not established for any Riemann cMPS": separable `H_±`; at each `t>0` a normal CP map with a countable bounded block-diagonal Kraus family `K_s = a_s ⊕ B_s` and weakly convergent expansion; blocks extending to bounded `S_±(t), M(t)` with `S_±` trace class; compression to finite bond subspaces agreeing with compression of the Kraus expansion; the odd semigroup having the zeros as eigenmodes with multiplicity. Caveat also recorded: the trace version `2 Tr S_+ Tr S_-` needs positivity of `S_±` on Hilbert--Schmidt space, which complete positivity alone does not give. And excluding the all-even Kraus class does **not** show that odd jumps *suffice*, that finitely many do, or that a distributional regularisation is a Hilbert norm.
- Lead: discharge (or refute) the analytic hypotheses for an actual Riemann cMPS --- this would become the notebook's strongest structural statement about the Phantasm. Separately, a *sufficiency* construction would give an actual fermionic cMPS whose ring norm is the Riemann count.
- Where: report/sections/06e_ring_norm_bosonic_nogo.tex:92-102; report/sections/06c_ring_norm_inputs.tex:121-130; report/sections/06f_ring_norm_genus_two.tex:265-272

### G2-T4-3 The grading is forced by the trace, not by positivity
- Absorbs: L11-089, L08-025, L08-026, L13-113
- Class: EXPLORED-registered
- Raised by: extractor (Lidskii argument), prover, reviewer adjudication
- What: If `X` is trace class then `Tr X^l = sum_j mu_j^l` with algebraic multiplicities; but a genus `>= 1` curve has `#X(F_{q^l}) = q^l + 1 - sum alpha_i^l` with `2g` terms of modulus `q^{1/2}` entering **negatively**, so the trace sequence cannot be realised without a grading. The same conclusion arrives independently on the complex side: since each single flow `T_k^E` has a nonnegative Kraus trace sequence, the zeros-as-odd-sector structure must come from the *alternating signs between different `k`*, not from any single flow. The hypothesis has to be stated carefully: positivity alone does **not** forbid a numerator --- `(1-u)/(1-2u)` has nonnegative Taylor coefficients and positive log-coefficients `(2^m-1)/m` yet a nonconstant reduced numerator. The reviewer adjudicated that the registered `thm:no-ungraded-trace` is a *residue-sign* argument that never uses positivity, so the operative hypothesis is "is an honest trace sequence", and the example is an instance (`N_m = 2^m - 1^m`), a sharpening rather than a contradiction. Similarly, a single finite transfer matrix contributes a reciprocal polynomial and so has no nonconstant reduced numerator; a numerator comes from net odd multiplicity between sectors. And Weil positivity applies to each retained *ordinary* block but "does not transfer automatically to an alternating product with negative spectral multiplicities".
- Lead: (i) write the Lidskii no-go as a short lemma --- it is the cleanest available *proof* that the grading is forced rather than aesthetic; (ii) fix the notebook's wording wherever it says "positive" instead of "is a trace sequence"; (iii) a **graded Weil positivity** (positivity for a supertrace sequence with negative multiplicities) is not established and is needed for any graded Phantasm.
- Where: notes/extract/riemann-cmps-sources.md:879-939; notes/complex-zeta/astra-proofs.md:641-680; report/sections/08e_complex_zeta_graded.tex:178-186

### G2-T5-1 TJO's factor-by-factor question and the ten-condition ledger
- Absorbs: L13-058, L13-059
- Class: PARTIAL
- Raised by: TJO
- What: TJO asked to line up every condition a zeta should obey (functional equation, RH/Ramanujan, unique fixed point, ...) and impose them factor by factor on the cMPS ring norm, including tiny `L`-functions, with completely concrete MPS/cMPS as the deliverable. Delivered by one codex lane (1882-line report, 13 scripts, 461 checks) plus 26 orchestrator re-derivations. The ten conditions as exact algebraic statements: C1 positivity automatic, integrality separate; C2 "genuine gas" (`a_d = (1/d) sum_{e|d} mu(d/e) N_e in Z_{>=0}`) **not** automatic; C3 rationality automatic, poles net even and zeros net odd; C4 FE as parity-preserving invariance under `lambda -> q/lambda`, visible mechanism `J Gamma = Gamma J`, `J E J^{-1} = q E^{-1}`, additive `lambda -> kappa - lambda` for cMPS; C5 RH as `|lambda|^2 = q` with a positive metric `M`, `E|_-^† M E|_- = qM`, necessary if semisimple; C6 **three** separate requirements (simple Perron root, a trace-preserving gauge on the whole bond, mixing); C7 Galois grading and Artin `L`-functions; C8 sign structure automatic; C9 physical realisability including cMPS kinetic regularity `R_a R_b = ± R_b R_a`, `R_f^2 = 0`; C10 exact lattice-in-cMPS embedding needs `E = e^{hT}` with Choi conditional positivity.
- Lead: each condition is now a testable algebraic property, so a search for a tensor satisfying all ten simultaneously is well posed --- **nobody ran that search**. And the whole shard is unreviewed by a second model family; every row is `sketched` or `numerical`. Getting it reviewed is the stated next step.
- Where: report/sections/06h_zeta_conditions.tex:12-19, :27-63

### G2-T5-2 Where the functional equation actually comes from
- Absorbs: L13-010, L13-060, L13-070
- Class: EXPLORED-registered
- Raised by: founding note (the involution), prover lane (the correction)
- What: For the quadratic Artin--Schreier transfer matrix, rationality of `Z` holds because `E` is finite, and the functional equation is the involution `E -> q E^{-†}`, which scaled unitarity `EE^† = qI` makes trivial --- the cleanest "FE = an involution on the transfer operator" statement in the book. But inverse-closed *letters* do **not** give the FE for the raw doubled transfer: explicit counterexample `B = diag(1,2)` with `B^{-1}` gives even spectrum `{2, 17/4}` and odd `{5/2, 5/2}`. The reciprocal quadratics arise in the *non-backtracking* construction, after the Bass factors are removed. The lane's correction ledger D1--D8 records four named items: inverse pairing alone gives no FE; the "swap" `L`-function was not an Artin factor; unique stationarity, gauge and mixing are three conditions not one; the affine rung needs its own tensor.
- Lead: none --- but this fixes where the FE actually lives, and the visible sufficient mechanism remains `J Gamma = Gamma J`, `J E J^{-1} = q E^{-1}`.
- Where: report/sections/06_artin_schreier_mps.tex:144-147; report/sections/06h_zeta_conditions.tex:39-43, :195-199

### G2-T5-3 E0: a zero as the removal of a full subshift
- Absorbs: L13-061
- Class: LEAD-unpursued
- Raised by: prover lane
- What: Letters `K_{(a,b)} = diag(1, [a=b])` on `C^{1|1}` give `N_n = m^{2n} - m^n`, `Z = (1-mu)/(1-m^2 u)`: one pole at `1/m^2`, one genuine **zero** at `1/m = q^{-1/2}` ("RH by half entropy"), a genuine gas, no FE, no whole-bond channel gauge. For `m=2` it equals `Z(A^1/F_4)/Z(A^1/F_2)` in an identified degree variable. Correction recorded: "the swap is a symmetry with fixed letters, not an Artin cover."
- Lead: the mechanism "a zero is the removal of a full subshift" is a candidate for how fermionic zeros should arise generally, and it has not been pushed anywhere.
- Where: report/sections/06h_zeta_conditions.tex:67-81

### G2-T5-4 Four-letter elliptic channels with FE, RH and mixing by visible mechanisms
- Absorbs: L13-062
- Class: EXPLORED-registered
- Raised by: prover lane
- What: Four explicit Kraus letters on `C^{1|1}` give `sum K_s^† K_s = q`, even spectrum `{q,r}`, odd `{pi, conj pi}`, Ramond norm `r + q^n - pi^n - conj pi^n` --- the affine (`r=0`) or projective (`r=1`) elliptic count. For `r=1` the FE comes from an explicit duality `J`, RH from `E|_-^† E|_- = q`, and the normalised channel is **mixing with the maximally mixed state as its unique fixed point**. This fixes condition C6, which the bare `diag(1,pi)` tensor fails, without changing `Z`.
- Lead: this is the notebook's best small "all conditions at once" object; testing whether the pattern extends to higher genus is the obvious next step and was not done.
- Where: report/sections/06h_zeta_conditions.tex:83-107

### G2-T5-5 FE, RH and mixing are mutually independent
- Absorbs: L13-063
- Class: EXPLORED-negative
- Raised by: prover lane
- What: With Pauli letters `sqrt(c_i) {1,Z,X,Y}` on `C^{1|1}` the even spectrum is `{16,r}` and the odd `{x,y}`, and four parameter choices realise (FE,RH,mixing) = (Y,Y,Y), (Y,N,Y), (N,Y,Y), (N,N,Y); tensoring with an idle even qubit keeps FE and RH and destroys uniqueness. The one excluded combination is (FE=N, RH=Y) with the exact projective pair `{1,q}`, since RH already makes the odd multiset reciprocal. **Positivity of norms plus FE does not force RH.**
- Lead: none --- it is a negative structural result constraining any attempt to derive RH from the other conditions.
- Where: report/sections/06h_zeta_conditions.tex:109-124

### G2-T5-6 Tiny `L`-functions as MPS: Horner, Gauss, Kloosterman, voltage cover
- Absorbs: L13-064
- Class: PARTIAL
- Raised by: prover lane (correcting two orchestrator drafts)
- What: (i) A Horner MPS on bond `F_q[x]/M` with letters `f -> xf + c` produces Dirichlet `L`-polynomials over `F_2` and `F_3` with `|lambda|^2 = q`; (ii) a Gauss factor `1 + iu sqrt 3`; (iii) a Kloosterman factor over `F_4` realised as the affine count of `y^2 + xy = x^3 + 1`; (iv) a `Z/2` voltage graph cover with an Artin decomposition. Two corrections: closing the Horner automaton into a trace imposes a return condition and *is wrong* (the ring presentation is the Euler product over prime polynomials); and the correct tiny `Z/2` Artin example is a directed voltage cover, not the drafted square root for the pair shift.
- Lead: the Horner construction is the notebook's only *open-chain* `L`-function MPS. Whether a genuine ring (trace) presentation of a Dirichlet `L`-function exists is left open.
- Where: report/sections/06h_zeta_conditions.tex:126-155

### G2-T5-7 A literal count state needs 0/1 word traces
- Absorbs: L13-066
- Class: LEAD-unpursued
- Raised by: prover lane (one clause in the C9 row)
- What: Choi positivity per parity block plus parity covariance gives homogeneous Kraus letters; but a *literal* count state (configurations = points) needs `Tr(Pi K_w) in {0,1}`, and "the curve tensors are weighted norms, not point enumerations".
- Lead: search for tensors with 0/1 word traces realising a curve count. This is the precise statement of the gap between the gas picture and every tensor the notebook actually built; the genus-0 example is the only place where "the configurations are the points".
- Where: report/sections/06h_zeta_conditions.tex:56-60; report/sections/06g_ring_norm_examples.tex:28-31

### G2-T5-8 The discrete-to-continuum passage is not free; two explicit cMPS
- Absorbs: L13-067, L13-068
- Class: PARTIAL
- Raised by: prover lane
- What: Exact embedding of a lattice channel in a cMPS needs `E = e^{hT}` with Choi conditional positivity; a singular `E` (the affine tensor) has none. Poissonisation `Q = -c/2`, `R_s = K_s` always exists but changes FE/RH. Two explicit cMPS were built: (i) `Q = 1/2`, `R = diag(1,0)` gives `N(L) = e^{2L} - e^L`; a normalised finite-norm alternative gives `N(L) = 1 - e^{-L}` but fails kinetic regularity, and "on homogeneous regular `C^{1|1}` data, regularity, Lindblad normalisation, uniqueness and the exact half difference cannot all hold". (ii) One lowering fermion `R = sqrt 2 |0><1|`, `H = diag(0,1)` gives ring zeta `((z-1)^2+1)/(z(z-2))` with additive FE `Z(2-z) = Z(z)` and both zeros on `Re z = 1`: FE, RH and a unique fixed point by one visible mechanism (odd damping is half the population decay; the frequency comes from `H`).
- Lead: recorded limitation --- "the ring vector has only its vacuum amplitude: the zeta data sit in the length-dependent vacuum normalisation, and no nontrivial entanglement spectrum is produced". Making a cMPS whose zeta data live in the *state*, not the normalisation, is the open task; any Phantasm starting from a lattice and wanting dilation time must face the embedding obstruction.
- Where: report/sections/06h_zeta_conditions.tex:60-62, :157-177

### G2-T5-9 What a finite bond cannot reach
- Absorbs: L13-069
- Class: EXPLORED-registered
- Raised by: prover lane
- What: A finite bond can have infinitely many Euler primes (E0 does) but cannot produce a nonrational `Z`, an atomic prime comb, or infinitely many distinct divisor points: `u = q^{-s}` gives periodic copies of finitely many points, not Riemann's zeros. Also: the bosonic no-go concerns plain power traces and graded norms evade it by negative net coherence multiplicities; a single simple pole at `1/q` is incompatible with the uncompleted self-reciprocal FE, so the completion must be declared. Factor by factor "does not make an infinite product converge, supply the continuation or the archimedean factor, select an entanglement spectrum, or prove RH for an unidentified infinite object."
- Lead: read the list as a **specification** for what an infinite-bond construction must add.
- Where: report/sections/06h_zeta_conditions.tex:179-199

### G2-T6-1 What varieties have that graphs lack: products and slicing
- Absorbs: L13-071, L13-073, L11-074
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: There is no theorem that a `(q+1)`-regular graph is Ramanujan --- most are not, the prism is a counterexample --- so the right question is what varieties have that graphs lack. Three things: varieties can be **multiplied**, **sliced** over a curve, and their interesting eigenvalues enter the count with a **minus sign**. A graph has none of the three. `zeta` sits on the *curve* side of the table (the zeros are subtracted from the prime count, and `Lambda(n) >= 0` is the right kind of positivity): the sign and the positivity are present, the product is absent, because there is no `X x X` with `zeta` as its slice, so Deligne's "multiply" step has nothing to act on.
- Lead: supply an operation on the Riemann channel under which eigenvalues multiply while the trivial loss stays fixed. If one existed, Deligne's engine (count, fixed loss, roots) would run on `zeta`.
- Where: report/sections/07_deligne_via_graphs.tex:92-99, :212-243, :279-284; notes/extract/notation-and-definitions.md:330-331

### G2-T6-2 The abelian obstruction: any Ramanujan lift must break the commutativity
- Absorbs: L13-072, L11-073
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: Commuting holonomies produce uncontrolled invariants in tensor powers, exactly as commuting Kraus unitaries never give an expander: a common eigenvector with eigenvalue `chi(w)` becomes invariant in `hol^{⊗N}` as soon as `chi^N = 1`, carrying an unknown scalar, so the trivial poles sit where the argument cannot control them. The same obstruction appears on both sides of the dictionary. Confirmed prime-side: the direct sum over `p` of rotations on circles of circumference `log p` has trace `sum_n Lambda(n) delta(s - log n)` and dynamical zeta equal to the Euler product --- it is pure side A, and for finite sets of primes its spectrum is just the poles of the partial Euler product. Direct sums and commuting dilations, prime by prime, cannot produce zeros.
- Lead: the design constraint is explicit --- "**any Ramanujan lift of the prime dilations must break the commutativity by a quotient**", as LPS does with the arithmetic lattice and Deligne does with the shears of a generic slicing. The prime dilations commute, so the lift cannot.
- Where: report/sections/07_deligne_via_graphs.tex:163-193; notes/extract/notation-and-definitions.md:349

### G2-T6-3 The sign: poles versus zeros, and why positivity bounds only one of them
- Absorbs: L13-074
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: Graph and curve match in every row of the dictionary except the sign of the error term, hence whether the interesting eigenvalues are poles or zeros. On the graph side positivity constrains the sum of everything, which is the Perron bound and no more; on the curve side the interesting eigenvalues are *subtracted*, so positivity bounds them above by the trivial ones and even tensor powers squeeze to equality. "The two-loop bouquet is not a curve because its walk counts cannot be written with the interesting part subtracted."
- Lead: none --- it is the reason the whole notebook wants graded (supertrace) objects: a minus sign in the count.
- Where: report/sections/07_deligne_via_graphs.tex:46-73, :195-210

### G2-T6-4 Deligne's purity step is false for graphs: the two-loop bouquet
- Absorbs: L13-075, L11-075
- Class: DEAD
- Raised by: orchestrator (worked counterexample)
- What: `hol(a) = [[2,1],[1,1]]`, `hol(b) = [[1,1],[1,2]]` satisfy (a) integral/real traces, (b) a determinant-1 alternating pairing with weight 1, and (c) big monodromy inside `SL_2(Z)` --- yet `hol(a)` has eigenvalue `(3+sqrt 5)/2 > 1`, so the twist is not pure. It breaks the third step, and must, since the theorem is false for graphs. Related: Deligne's proof never exhibits a Hermitian structure; Grothendieck's standard-conjectures plan is open; above dimension one the inner product making Frobenius normal is not known to exist.
- Lead: none --- it isolates exactly which hypothesis a channel-based approach would have to supply, and should be stated rather than re-derived.
- Where: report/sections/07_deligne_via_graphs.tex:153-161; notes/extract/notation-and-definitions.md:322, :319-329

### G2-T6-5 A quantum expander is a Ramanujan twist of a bouquet --- global versus pointwise eigenvalues
- Absorbs: L13-076
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: The quantum Ihara zeta is the Artin--Ihara `L`-function of a bouquet of `D` loops with `hol = Ad(U_i)` on the `i`-th loop; a quantum expander is a *Ramanujan twist of a bouquet*. Two kinds of side-B eigenvalue then live together: the **global** ones (eigenvalues of the twisted edge operator, poles of `L`) and the **pointwise** ones (eigenvalues of each `hol(gamma)`); "pure with constant `w`" means every pointwise eigenvalue of every prime cycle has modulus `w^{l(gamma)}`.
- Lead: the global/pointwise distinction has never been exploited for channels. A "pointwise purity" condition on `Ad(U_gamma)` is a strictly different requirement from the Ramanujan bound on `Sigma`, and nobody has asked which one the Phantasm needs.
- Where: report/sections/07_deligne_via_graphs.tex:114-131

### G2-T6-6 Ramanujan without Hermiticity: positivity plus an operation that multiplies eigenvalues
- Absorbs: L13-077, L11-069, L13-011
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: Deligne's proof exhibits no Hermitian structure --- no form, no operator, only positivity and a limit. Weil's proof for curves does (Hodge index on `C x C`), and Grothendieck's plan (standard conjectures) is still open. Both Deligne's route and the interlacing route (Marcus--Spielman--Srivastava) reach the spectral bound with **no Hilbert--Polya operator**; what they share is a positivity together with an operation under which eigenvalues multiply while the loss stays fixed (tensor powers for Deligne, interlacing for MSS). The standing dichotomy the whole notebook is trying to break is the same statement in the Artin--Schreier setting: "the Ramanujan bound is either manifest, because the transfer matrix is a scaled unitary, or it comes from arithmetic input that sits outside the transfer structure altogether."
- Lead: **stop looking for a Hermitian form; look for a positivity plus a multiplying operation.** The sharpest constructive suggestion in the group: tensor powers of a channel do multiply eigenvalues --- the question is what stays fixed.
- Where: report/sections/07_deligne_via_graphs.tex:245-256, :293-296; notes/extract/notation-and-definitions.md:332; report/sections/06_artin_schreier_mps.tex:209-211

### G2-T6-7 Rankin--Selberg, functoriality, and the three sources of Ramanujan-ness
- Absorbs: L13-078, L11-070, L11-068
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: For a modular form the Euler product of `L(f x conj f)` has nonnegative coefficients and a known pole, and dominating one local factor gives `|a_p| <= p^{(k-1)/2} · p^{1/2}` --- the same fixed loss; each symmetric-power `L`-function whose poles are known shaves it (Kim--Sarnak's `7/64` is the current state). "Knowing the poles of all the tensor-power `L`-functions is the analogue of big monodromy; over number fields that is Langlands functoriality, unproved." Against this, Ramanujan-ness has exactly three known sources: arithmetic (LPS via Deligne), probabilistic-asymptotic (Friedman, Hastings), interlacing families (MSS) --- and it is never a consequence of structure. The graph lesson says the Kraus structure alone will not force degeneracy of the decay rates: "some arithmetic rigidity has to enter, playing the role weights play for curves."
- Lead: any Phantasm must draw on one of the three sources or introduce a fourth; identifying the arithmetic input is the programme's central unanswered question, restated in channel language.
- Where: report/sections/07_deligne_via_graphs.tex:285-290; notes/extract/notation-and-definitions.md:268-269, :290

### G2-T7-1 Theorem 1: Ihara--Bass for an arbitrary family of superoperators
- Absorbs: L08-045, L11-071
- Class: EXPLORED-registered
- Raised by: orchestrator (proved, two Opus reviews VALID, plus numerics)
- What: For arbitrary `E_1..E_D in End(V)` with a fixed-point-free reversal `sigma`, `det_W(1-uT) = prod_{pairs} det_V(1 - u^2 E_ī E_i) · det_V(1 + D(u) - A(u))` with `A(u) = u sum_i E_i (1 - u^2 E_ī E_i)^{-1}` and `D(u) = u^2 sum_i E_ī E_i (1 - u^2 E_ī E_i)^{-1}`. No invertibility, positivity or unitarity is assumed. It is the bouquet analogue of Watanabe--Fukumizu's arbitrary-weight corollary (which is stated only for loopless graphs) and is the general machine used whenever a channel becomes a transfer matrix.
- Lead: none --- the machine works; the open questions are downstream (G2-T7-5).
- Where: notes/quantum-ihara-general.md:25-35, :55-96; notes/extract/notation-and-definitions.md:334-339

### G2-T7-2 Which factor carries the spectrum, and the `D=2` degeneration
- Absorbs: L13-082, L08-046
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: Under inverse pairing, `det_W(1-uT) = (1-u^2)^{N(D-2)/2} det_V(1 - u Sigma + (D-1)u^2)`. In general the poles of `zeta_T` lie among the roots of `det(1 + D - A)` together with `u^2 = 1/lambda` for nonzero `lambda in spec(E_ī E_i)`; the latter **may cancel**, and do in the unitary case (total cancellation at `D=2`, where `T = E_1 ⊕ E_2` because the only non-backtracking successor of `i` is `i`). Conversely a pole of the second factor is not a pole of `zeta_T` unless it survives multiplication by the first.
- Lead: the cancellation bookkeeping between the pair factor and the compressed factor is the *same phenomenon* as the chamber-factor cancellation on complexes (G2-T10-2), in the simplest possible setting --- nobody connected the two.
- Where: report/sections/08_quantum_ihara_general.tex:113-124; notes/quantum-ihara-general.md:47-53

### G2-T7-3 Side A is unconditionally positive: the primes are non-backtracking words
- Absorbs: L13-081, L08-048, L11-020, L11-090
- Class: EXPLORED-registered
- Raised by: orchestrator; literature corroboration from Aizenman--Warzel
- What: `Tr B^l = sum_gamma |Tr K_gamma|^2 >= 0` for *any* Kraus family, with no pairing hypothesis --- the proof uses only `Ad(A)Ad(B) = Ad(AB)` and `Tr Ad(A) = |Tr A|^2`. So `zeta` has nonnegative Taylor coefficients and an Euler product `prod_{[w]} det_V(1 - u^{|w|} Ad(A_w))^{-1}` over primitive cyclically non-backtracking classes, with real nonnegative multiplicities `|Tr A_w|^2`. Literature: the Bowen--Lanford/Ihara identity `det(1-uM) = prod_p [1 - u^{|p|} chi_M(p)]` holds for an **arbitrary non-backtracking flow matrix**, and Aizenman--Warzel say the reason the infinite Euler product collapses to a polynomial "is that the loop ensemble has a fermionic nature". Unused tool: Landau's theorem --- a Dirichlet series with nonnegative coefficients and abscissa of absolute convergence 0 does not extend holomorphically past it.
- Lead: (i) apply Landau to the unconditionally positive side-A series to pin the radius of convergence of `zeta_Phi` to a genuine singularity --- small and rigorous; (ii) check whether Theorem 1 is a special case of the arbitrary-flow-matrix identity, or whether operator weights genuinely break it. The standing task is to convert side-A positivity into a constraint on side B.
- Where: report/sections/08_quantum_ihara_general.tex:81-98; notes/quantum-ihara-general.md:41-45; notes/extract/cohomological-zeta-sources.md:1542-1592; notes/extract/riemann-cmps-sources.md:940-958

### G2-T7-4 RH for the quantum Ihara zeta is exactly Hastings' bound
- Absorbs: L13-079, L11-067
- Class: PARTIAL
- Raised by: orchestrator (founding session item 2)
- What: For unitary Kraus operators closed under adjoint, each eigenvalue `lambda` of `Sigma = D Phi` gets the quadratic `1 - lambda u + q u^2` with `eps eps' = q = D-1`; both roots have `|eps| = sqrt q` exactly when `|lambda| <= 2 sqrt q`. Hence every nontrivial pole of `zeta_q` lies on `|u| = q^{-1/2}` iff `D lambda_2 <= 2 sqrt(D-1)`, which is Hastings' bound. Ten arXiv metadata queries found no prior statement; the notebook records it as its own contribution, tagged `sketched` because it has had **no reviewer**.
- Lead: get it reviewed --- it is the load-bearing bridge between the zeta language and the channel language, and the whole "RH ⇔ Ramanujan channel" reading rests on it.
- Where: report/sections/08_quantum_ihara_general.tex:288-299; notes/extract/notation-and-definitions.md:343

### G2-T7-5 What replaces `mu mu' = D-1` when the weights are not inverse-paired
- Absorbs: L13-080, L08-047, L11-066
- Class: LEAD-unpursued
- Raised by: orchestrator (registered as `conj:kraus-ramanujan`)
- What: The arbitrary-Kraus Ihara--Bass gives the compression for *every* MPS transfer matrix, at the price of two `u`-dependent operators `A(u), D(u)` in place of the adjacency matrix and the degree. But it gives no Ramanujan reading by itself: without `E_ī E_i = 1` there is no quadratic relation pairing the eigenvalues of the edge operator with those of `Sigma`. Two concrete sub-questions: (a) what replaces the pairing; (b) whether MPS canonical form (`sum_k A_k^† A_k = 1`) buys anything.
- Lead: the HANDOFF proposes a cheap decisive experiment --- take random MPS tensors, measure the pole radii of `zeta_Phi`, and see empirically whether a Ramanujan-type circle survives. Canonical form is the obvious first hypothesis and has never been tested. This is the most direct open side-B question in the group.
- Where: report/sections/08_quantum_ihara_general.tex:275-286; notes/quantum-ihara-general.md:117; notes/extract/notation-and-definitions.md:340

### G2-T7-6 Provenance of the general identity: Watanabe--Fukumizu and Bordenave--Collins
- Absorbs: L13-083, L08-056, L08-052, L13-139
- Class: PARTIAL
- Raised by: round-1 provenance review, orchestrator, literature agent
- What: Watanabe--Fukumizu's corollary is stated for loopless graphs (their graphs are hypergraphs with two-element hyperedges), so a bouquet is not one of their graphs and their corollary does not apply to it; the notebook's theorem is the loop-admitting analogue, not an instance, and their scalar reduction "does not evaluate correctly there". The shape-matching to their right-hand side (after a push-through identity, a relabelling, and two conventions that wash out of `det(1-u·)` --- they compose prime cycles in reverse order and weight the target where `T` weights the source) is **checked numerically only**, in `notes/reviews/scratch_wf_mo_conventions.py`; the NeurIPS 2009 supplement with a hypergraph-free proof was never fetched. Bordenave--Collins have the *same* matrix-valued non-backtracking operator, introduced explicitly because "this extension is especially relevant in the context of quantum expanders", and their follow-up names the connection to Ihara--Bass identities --- "but as a resolvent identity rather than a determinant: no zeta and no Riemann hypothesis", and it is "an identity in its strongest form, i.e. between two operators". Their stated drawbacks: not self-adjoint, spectral correspondence only for `A_1 = M_n(C)`. Separately they record that a family of tensor-squared permutations is a nearly optimal quantum expander in Hastings' sense.
- Lead: three cheap jobs --- do the shape-matching **symbolically** (it would close the last provenance gap on the book's load-bearing theorem); fetch the NeurIPS supplement, which might cover the bouquet directly and change the novelty claim; and compare Theorem 1 with the "strongest form" operator identity. The tensor-squared permutation family is an unused source of near-Ramanujan channels.
- Where: report/sections/08_quantum_ihara_general.tex:219-239; report/sections/09_prior_art.tex:155-178; notes/prior-art-quantum-ihara.md:64, :66-75

### G2-T8-1 "Every mode is its own partner": the finite Weil theorem and its arithmetic anchor
- Absorbs: L13-084, L13-085, L11-105, L11-106
- Class: EXPLORED-registered
- Raised by: TJO (2026-09-12); prover; anchored on Connes and Connes--Consani
- What: The reflection `rho -> 1 - conj rho` pairs the mode of the Riemann channel at a zero with the mode at its mirror image; RH says every mode is its own partner, and Weil's criterion is the positivity of that pairing written on the primes. The finite theorem: for any operator, any trivial multiset and any critical radius, the rescaled trace sequence `nu_l = r^{-l}(Tr X^l - trivial)` is positive definite iff `|eps| <= r` on the retained multiset. **The point of the theorem is what it does not say: an eigenvalue inside the disc passes. Weil positivity alone is a spectral-gap statement, and the circle needs a second input.** The arithmetic anchor is Connes's Theorem 5 --- the asymptotic trace formula for `Trace(Q_Lambda U(h))` is equivalent to RH for all `L`-functions with Grossencharakter, the mechanism being `Delta_Lambda(f * f^*) >= 0`, positivity of type on the idele class group, with the two trivial terms `hat h(0) + hat h(1)` being the analogue of "trivial eigenvalues removed"; Connes's equivalence is in positive characteristic and the characteristic-zero case is conjectural. The citable clean form is Connes--Consani: `RH ⟺ sum_v W_v(g * conj g^♯) <= 0` for all `g in C_c^∞(R_+^x)` with `tilde g` vanishing on a finite set `F ⊇ {0,1}` disjoint from the zeros, `g^♯(x) = x^{-1} g(x^{-1})` --- with a recorded sign caveat (they write `<= 0` because the explicit formula puts zeros and places on opposite sides; the notebook's `>= 0` is the spectral side).
- Lead: prove the finite shadow cleanly and adopt one sign convention, stating which side the notebook's positivity lives on. The "second input" is the recurring theme: inverse pairing in the Kraus world, the functional equation in the arithmetic world.
- Where: report/sections/08b_weil_positivity.tex:13-24, :50-68; notes/extract/weil-positivity-sources.md:30-116, :117-181

### G2-T8-2 The inflow identity: a duality turns the Weil form into a mode-pairing form
- Absorbs: L13-086, L13-091, L13-090
- Class: EXPLORED-registered
- Raised by: prover (correcting an orchestrator draft on the continuous side)
- What: If the retained multiset is invariant under `J(eps) = r^2 / conj eps` then the Weil form **equals** the mode-pairing form, and positivity is equivalent to every mode being `J`-fixed, i.e. on the circle; a two-element orbit makes the form negative (Weil's off-line pair argument in finite form, proved by interpolating the test polynomial to vanish at every other retained value). Reciprocal symmetry without conjugation still gives the circle but the two forms can differ. Continuously: Weil positivity via Bochner is a half-plane bound `Re lambda <= a`; a mode off the line contributes a Lorentzian `2b/(b^2 + (x-omega)^2)`, a mode on the line a point mass; and if the multiset is invariant under `lambda -> 2a - conj lambda`, the autocorrelation of the rescaled trace equals `sum_lambda hat g(lambda) conj(hat g(2a - conj lambda))` --- Weil's form. Continuous side A is the Dyson expansion: for `L(x) = Kx + xK^† + sum_j R_j x R_j^†`, `Tr e^{t L}` is an absolutely convergent time-ordered integral of `|Tr(e^{(t-t_k)K} R_{j_k} ... R_{j_1} e^{t_1 K})|^2 >= 0`. **The free propagators between jumps were missing from the draft; without them the product is wrong for noncommuting `K` and `R_j`.**
- Lead: the continuous statement carries a one-line prescription worth keeping: "the content of RH in this language is the existence of a presentation in which the transfer generator is a scalar plus `i` times a Hermitian operator."
- Where: report/sections/08b_weil_positivity.tex:70-100; report/sections/08c_weil_positivity_continuous.tex:17-44, :46-68

### G2-T8-3 The Kraus dichotomy: inverse pairing buys the FE, adjoint pairing buys reality, both is unitarity
- Absorbs: L13-088, L13-095, L13-087, L13-089
- Class: EXPLORED-registered
- Raised by: prover / orchestrator
- What: Inverse pairing makes the retained edge multiset `J`-invariant for `r = sqrt q`; adjoint pairing makes `Sigma` Hilbert--Schmidt self-adjoint, hence real-spectrum; both at once forces every Kraus operator unitary (`Ad(B^†) = Ad(B)^{-1}` iff `B^† B = 1`; `B = 2` disproves "unitary up to a scalar"). In the unitary case Weil positivity is exactly Hastings' bound --- "the Ramanujan property is the statement that the rescaled ring norms form a positive definite sequence"; the trivial eigenvalue `D` always violates the band, so the trivial set must be enlarged (bookkeeping: a double root at `sigma = ±2 sqrt q` gives doubled copies of `±sqrt q`, and `sigma = ±D` gives extra `±1`s). Two negatives complete the picture. (i) The orchestrator's requested inverse-paired counterexample to conjugation closure **does not exist**: every `Ad`-type family has spectra closed under conjugation and nonnegative ring traces with no pairing hypothesis, so every Kraus-type family has a positive side A and a real-structured side B. (ii) For a general channel "every mode is its own partner" has no partner to refer to: for `n=2, D=4`, `B_1 = B_3 = diag(1,2)`, `B_2 = B_4 = 1`, the retained edge spectrum is invariant under `eps -> c/eps` for **no** nonzero `c`; the Weil form is still defined and its positivity is still the one-sided bound --- "the analogue of `Re rho <= 1/2` without the functional equation".
- Lead: the dichotomy is the constraint on any Phantasm transfer operator: reality of `spec(Sigma)` is the Hilbert--Polya half, the FE is the other half, and a Kraus family gets both only by being unitary. The escape is G2-T8-4.
- Where: report/sections/08b_weil_positivity.tex:133-175, :114-131, :177-188; report/sections/08c_weil_positivity_continuous.tex:234-251

### G2-T8-4 Weakened Hermiticity: inverse-paired non-unitary families as an unbroken PT symmetry
- Absorbs: L13-096, L11-115, L11-037
- Class: LEAD-unpursued
- Raised by: orchestrator; literature from Bender--Brody--Muller and from LLP via Parzanchevski
- What: Inverse-paired non-unitary families --- for instance `B_i = G U_i G^{-1}` with a common similarity `G`, which keeps `Sigma` similar to a self-adjoint operator --- have a genuine two-sided Ramanujan property with a positive side A, and their non-Hermitian `Sigma` with real spectrum is **the transfer-matrix version of an unbroken PT symmetry**. Reading the cited PT paper carefully: their `PT` is the *modified* reflection `(x,p) -> (x,-p)`, so `iH` is PT symmetric and a real spectrum of `H` requires **maximally broken** PT of `iH` --- the opposite of the usual slogan and easy to quote backwards; the paper also assumes a self-adjointness it does not prove. A third, independent candidate in the same slot: all geometric walks on quotients of a fixed building form a family of **almost-normal** digraphs, and for the geodesic edge walk on `Ã_d`-Ramanujan complexes they are *sharply* `(d+1)`-normal, and can be made `m`-periodic for any `m | (d+1)`.
- Lead: build the family `B_i = G U_i G^{-1}` --- it is the smallest class where the FE and reality coexist *without* unitarity, which is exactly what a Phantasm transfer operator would need, and it realises G2-T6-6's prescription (Ramanujan behaviour without Hermiticity). List PT symmetry, almost-normality and "positivity plus a multiplying operation" together as the three candidate substitutes for Hilbert--Polya self-adjointness, and test whether Kraus transfer operators are almost-normal.
- Where: report/sections/08c_weil_positivity_continuous.tex:253-257, :203-211; notes/extract/weil-positivity-sources.md:652-705; notes/extract/complex-zeta-sources.md:751-756

### G2-T8-5 Weil positivity is blind to Jordan blocks --- so a Hilbert--Polya realisation needs simple zeros
- Absorbs: L13-092, L08-035, L08-078
- Class: PARTIAL
- Raised by: prover, reproved finitely in the complex-zeta lane
- What: A Hilbert--Polya inner product exists iff the retained part is semisimple with all modes on the circle (or line). But `X = r [[1,1],[0,1]]` has `nu_l = 2` for all `l`, positive definite, yet is not unitarisable. So "all modes on the critical circle" is equivalent to Weil positivity, while "there is a Hilbert space in which the transfer operator is `r` times a unitary" is **strictly stronger --- by exactly the absence of Jordan blocks**. For the Riemann channel the distinction is the *multiplicity* of the zeros: a multiple zero of `S` gives a Jordan block of `Z_t`. The complex lane adds: positivity alone does not construct a Hilbert--Polya inner product for a nonsemisimple transfer matrix, repeated roots can make a companion matrix nonsemisimple, and logarithms require branch choices. What survives in higher rank is Weil-positivity-as-bound, the finite theorem applied block by block.
- Lead: **simplicity of the zeros is an extra requirement beyond RH for any Hilbert--Polya realisation, and nobody in the notebook tracks it.** Concretely: apply the block-by-block positivity certificate to the two isotypic blocks already built on the `PGL_3(F_3)` data and see what it actually looks like on a real graded example.
- Where: report/sections/08c_weil_positivity_continuous.tex:70-105; notes/complex-zeta/astra-proofs.md:947-962; notes/complex-zeta.md:225-228

### G2-T8-6 The zeta dictionary entry, and the four things the passage to `zeta` needs
- Absorbs: L13-093
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: For the compressed semigroup `Z_t` with modes `eta = -conj rho / 2` the critical real part is `a = -1/4`, the reflection becomes `eta -> -1/2 - conj eta`, and Weil's form is the autocorrelation of the centred trace distribution, whose full-line extension is `T_Z(-u) = e^{u/2} conj(T_Z(u))`. The trivial modes at `0` and `-1/2` and the Gamma-factor terms are *not* eigenmodes; they stay on the geometric side.
- Lead: four concrete items, none done: the completed-zeta data, a distributional trace realisation, the full explicit formula, and the infinite Weil converse, with Bochner--Schwartz in place of Bochner.
- Where: report/sections/08c_weil_positivity_continuous.tex:109-126

### G2-T8-7 Huang's Li-criterion for Ramanujan graphs --- the prior art, and the unfinished reconciliation
- Absorbs: L13-094, L11-109, L11-110, L11-114
- Class: PARTIAL
- Raised by: orchestrator; extractor's prior-art analysis
- What: With `Xi(u)` the Ihara zeta cleared of trivial poles and `d/du ln Xi(q^{-1/2}u) = sum_k h_{k+1} u^k`, Huang proves: `X` Ramanujan ⟺ `h_k >= 0` for all `k >= 1` ⟺ `h_k >= 0` for **infinitely many even `k`**; and `h_k = 2(n-1) + q^{k/2} + q^{-k/2} - q^{-k/2} N_k`, i.e. `q^{-k/2}` times (cycle count minus trivial part). In finite dimensions, for a conjugation-closed retained multiset, positive definiteness, boundedness, `|nu_l| <= nu_0`, and the termwise `Re nu_l <= nu_0` are all equivalent, and Huang's sequence is exactly `h_k = nu_0 - nu_k` with `nu_0 = 2(n-1)`. **But the overlap is not total**: Huang proves *termwise* nonnegativity, while the notebook claims positive-definiteness in the Herglotz/Toeplitz sense (every Toeplitz minor `>= 0`), and these are different conditions on a sequence --- neither implies the other in general. Huang's source has zero hits for "Herglotz", "Bochner", "Toeplitz", "positive definite". Full-text searches found *no* paper stating a Herglotz/Toeplitz criterion for the Ramanujan property or for an arbitrary transfer operator / Kraus channel --- the notebook's actual theorem.
- Lead: do the reconciliation explicitly --- state both conditions on the same sequence and prove or disprove either implication; it determines whether the notebook has a new theorem or a repackaging. Also exploit the "infinitely many even `k`" clause: a very weak hypothesis that might be far easier to verify for a channel and that nobody has used. The reason the Toeplitz machinery is preferred at all: "the Toeplitz form is what survives when the trace is a distribution and boundedness has no meaning."
- Where: report/sections/08c_weil_positivity_continuous.tex:221-232; notes/extract/weil-positivity-sources.md:381-517, :496-517, :835-887

### G2-T8-8 The converse gap: which test functions separate the zeros
- Absorbs: L11-107, L11-108, L11-113
- Class: LEAD-unpursued
- Raised by: paper (Lagarias, Suzuki, Voros/Coffey) + extractor
- What: The Weil scalar product is `<F,G>_{W(pi)} = sum_{rho} F(rho) conj G(1 - conj rho)`; RH ⟹ positive semidefinite because `rho = 1 - conj rho` iff `Re rho = 1/2`. Li's coefficients `lambda_n = sum_rho [1 - (1-1/rho)^n]` are a specialisation, and `<G_n, G_m> = lambda_n + lambda_{-m} - lambda_{n-m}` --- so the `lambda_n` are **not the diagonal** of the form but a combination of Gram entries. Critically: "one direction is elementary (RH ⟹ psd); the converse needs a test-function class rich enough to separate the zeros --- the source says so explicitly. **This is the same gap the notebook must close when it asserts 'iff'.**" On the continuous side Suzuki is prior art: RH ⟺ the Hermitian form built from `G_g(t,u) = g(t-u) - g(t) - g(-u) + g(0)` is non-negative definite for every `0 < a < infinity`, with the Nevanlinna/Pick/Herglotz class named, Weil positivity as `W(psi * tilde psi) >= 0`, and Li's criterion derived as the special case of testing against *triangular* functions. What Suzuki does not do: arbitrary finite-dimensional transfer operators, the discrete Toeplitz-sequence form, graphs, or Ramanujan.
- Lead: identify the test-function class (finite-dimensionally, the richness condition on `nu_l`) that makes the converse work --- the single most concrete open technical step in the positivity lane. Unexploited bonus: "Li = Weil tested against triangular functions" is a *recipe* for generating new criteria by choosing other test functions. Also a small unread thread: Voros credits Keiper, whose results "were almost never cited".
- Where: notes/extract/weil-positivity-sources.md:182-322, :310-322, :323-380, :706-834

### G2-T8-9 Herglotz hands over the unitary for free
- Absorbs: L11-112, L11-116
- Class: LEAD-unpursued
- Raised by: paper (Alpay--Colombo--Kimsey--Sabadini; Norvidas) + extractor
- What: A sequence is positive definite iff every block Toeplitz matrix `T_N >= 0` iff it is the moment sequence of a positive measure on `[0,2pi]`. Positivity forces `r(-n) = r(n)^*`, "so the notebook's `nu_{-l} = conj(nu_l)` is not an extra assumption but a consequence". And the representation `r(n) = C^* U^n C` with `U` unitary is "literally trace of a power of a unitary", the `|mu| = r` case of `Tr X^l`. Bochner's theorem is available in the continuous form (`f` positive definite iff the Fourier transform of a finite non-negative measure) and in the distributional Bochner--Schwartz upgrade in the same source.
- Lead: use `r(n) = C^* U^n C` as the **construction** of the Hilbert--Polya-like unitary --- Herglotz hands it over once positive-definiteness is established. This is the most direct available route from positivity to an operator, flagged in half a sentence and never taken. The distributional upgrade is what the continuous-time `Z(t)` statements will need, since the zero sum is a distribution not a function.
- Where: notes/extract/weil-positivity-sources.md:551-625, :615-620, :626-651

### G2-T8-10 Numerics caveat: finite-`L` positivity masks a mode just outside the circle
- Absorbs: L13-097
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: Positivity at a fixed finite `L` is weaker than the theorem --- a mode slightly outside the circle is masked by the positive contribution of the interior modes until `L` is large. The threshold radius approaches `max|eps|` from below like `L^{-3/2}` (relative gap `3e-2`, `5e-3`, `4.7e-4` at `L = 40, 160, 640`). Also recorded: `{X, Z, X^†, Z^†}` is an exact Ramanujan example with channel spectrum `{1,0,0,-1}`, exercising the `-1` branch of the trivial set.
- Lead: the `L^{-3/2}` rate is a quantitative statement about how much window one needs; it is the discrete cousin of the extension-disc radius (G2-T15-2).
- Where: report/sections/08c_weil_positivity_continuous.tex:278-282

### G2-T8-11 Two unused positivity constructions: the Sonin projection and the graph explicit formula
- Absorbs: L11-083, L11-117
- Class: LEAD-unpursued
- Raised by: paper (Connes--Consani) / extractor's not-found list
- What: Removing the absorption spectrum from "white light" gives the emission spectrum and resolves the Berry--Keating mismatch; there is "a single quantum cell" unaccounted for by the Berry--Keating cutoff, and the cutoff has a clean interpretation as the orthogonal projection `S` onto the **Sonin space** (functions vanishing with their Fourier transform on `[-1,1]`). The scaling action does not restrict to that subspace, but `Tr(rho(f) S)` is **positive definite by construction**, since on `f = g * g^*` it is `Tr(rho(g) S rho(g)^*)`. Separately, Horton--Stark--Terras and Stark--Terras I--III are journal-only and were never obtained; Terras's book is the reference for the **graph explicit formula**.
- Lead: "positive definite by construction" is precisely the mechanism the Weil-positivity lane wants, and the Sonin projection is a concrete finite-rank-like object nobody has used. And obtain the graph explicit formula: the notebook's whole side-A/side-B framing is a statement about an explicit formula, and the one case where it is elementary has never been written into the notebook.
- Where: notes/extract/riemann-cmps-sources.md:361-386; notes/extract/weil-positivity-sources.md:848-857

### G2-T9-1 TJO's founding question and the scope verdict: buildings only
- Absorbs: L13-098, L08-001, L08-003, L11-031, L13-101, L11-038, L11-039, L08-006
- Class: EXPLORED-negative
- Raised by: TJO (2026-09-13)
- What: TJO asked whether the Hashimoto operator, the Bass identity and "RH ⟺ Ramanujan" survive when a graph becomes a finite simplicial complex, and whether the answer grades by cell dimension into even and odd sectors, "with the odd sector supplying fermionic zeros the way 1-forms supply the numerator of a Ruelle zeta". Three sub-questions fell out: which flow, what `(1-u^2)^chi` really is, and what happens when edges carry channels. The verdict: an Ihara-type zeta with a Bass identity and an RH-iff-Ramanujan theorem exists **for finite quotients of affine buildings and nowhere else**; the shape is always `(1-u^n)^chi / (vertex-Hecke determinant)` = an alternating product of `det(I ∓ L u^j)` over facet dimensions. The two near misses both degenerate. Storm's hypergraph zeta has a Bass identity and an iff-Ramanujan theorem only because `zeta_H(u) = Z_{B_H}(sqrt u)` --- literally the Ihara zeta of the incidence bipartite graph in `sqrt u`, blind to simplicial structure beyond incidence (note the base `(1-u)`, not `(1-u^2)`, from the substitution), and its "modified hypergraph RH" first divides out `(1 + (r-1)q^{-s})^{n_2-n_1}`. The combinatorial Ruelle zeta of a triangulation is a polynomial vanishing to order `b_1(M)` at `z = (n+2)^{-1}`, a Fried-type torsion theorem --- "that point is not `q^{-1/2}`, and there is no spectral-gap statement".
- Lead: either restrict the complex-side ambitions to building quotients, or accept that the wanted object must be invented (G2-T9-11). Two cheap openings nobody took: whether the *quantum* twist of the incidence bipartite graph gives a useful channel object, and whether the notebook's own zeta likewise needs a trivial-factor quotient before RH can be stated --- record the shape of that correction.
- Where: report/sections/08d_complex_zeta.tex:12-17, :103-129; notes/complex-zeta.md:15-26, :60-63; notes/extract/complex-zeta-sources.md:16-32, :764-858

### G2-T9-2 Kang--Yu's all-rank identity states no RH
- Absorbs: L13-103, L08-004, L11-050
- Class: LEAD-unpursued
- Raised by: paper (Kang--Yu 2026)
- What: `(1-u^n)^chi L(Gamma, q^{(n-1)/2} u) = prod_k Z_k^eps(X,u)^{(-1)^{k+1}}`, an alternating product over facet dimension, each factor a reciprocal determinant of a successor operator on pointed `k`-facets with a parity sign. "The Euler factor is literally a torsion", the strategy inspired by Hoffman's reformulation of Bass's proof. Grepping the source for `Ramanujan` / `Riemann hypothesis` / `tempered` returns only a historical remark and three bibliography titles: **the source states no RH**, and in general rank it gives the determinant identity, not a list of prescribed circles.
- Lead: prove a general-rank RH for the Kang--Yu factors (or show it fails). That would be the first higher-rank RH-equals-Ramanujan theorem with an explicit alternating/graded presentation; it needs the Iwahori-spherical temperedness hypothesis plus LLP's branching hypotheses. A well-posed open problem the notebook noticed and did not attempt.
- Where: report/sections/08d_complex_zeta.tex:55-67; notes/complex-zeta/astra-proofs.md:183-193, :834-877; notes/extract/complex-zeta-sources.md:450-456

### G2-T9-3 "No zeta of a general complex" is a record of what was searched, not a theorem
- Absorbs: L13-102, L08-011, L08-075, L11-056, L11-049, L11-044
- Class: PARTIAL
- Raised by: four papers, assembled by the orchestrator; sharpened by the prover
- What: Deitmar--Hoffman (2004): "There is no Ihara-formula for higher rank up to date" --- and their own `PGL_3` identity is deliberately weak, `Z(u) = det(1 - u pi_1 + u^2 q pi_2 - u^3 q^3)^n / P(u)` for *some* `n` and *some* polynomial `P`. Lubotzky's 2018 ICM survey still calls it a direction of research "with the hope that also in this context the Ramanujaness of the complex can be expressed via the RH". Hong--Kwon (2024) name "the lack of a unified zeta function, as in higher dimensional buildings there are several possibilities to generalize Ihara's approach". Kang--Yu claim only the first identity uniform in `n`, and only for `PGL_n`. Six named search phrasings all returned nothing of the sought kind, and the prover's ledger row is blunt: "A literature search finding no general/quantum zeta proves nonexistence --- it does not."
- Lead: prove an actual impossibility theorem, or find the missing zeta. The lane has only obstructions to *specific prescribed shapes* (the cubic collapse, the Euler-factor-only fermion determinant). The honest position is that the general-complex Ihara zeta is an open construction problem and inventing it is a legitimate contribution independent of RH --- one endorsed at ICM level. Low-bar fallback: aim first for the Deitmar--Hoffman "weak identity" template (a determinant to an unspecified power over an unspecified polynomial) in the notebook's own setting.
- Where: report/sections/08d_complex_zeta.tex:131-146; notes/complex-zeta/astra-proofs.md:1118; notes/extract/complex-zeta-sources.md:1462-1480, :1106-1174, :1426-1445

### G2-T9-4 The universal Bass--Schur compression: what survives on *every* complex is rational
- Absorbs: L13-107, L08-015, L08-080
- Class: EXPLORED-registered
- Raised by: prover (answering "WRITE IT DOWN, it is the general-complex Bass identity"); reviewer VALID on all 13 test complexes
- What: For every finite abstract simplicial complex and every `k`, with `R_k` the first-vertex deletion, `S_k` the append map, `C_k` cyclic rotation and `F_k = C_k + R_{k+1}S_{k+1}`: `T_k = S_k R_k - F_k` and `det(I - zT_k) = det K_k(z) · det(I - z R_k K_k(z)^{-1} S_k)` with `K_k(z) = I + zF_k`. This is an explicit **rational** compression by one dimension, not a degree-`(d+1)` polynomial on vertices; at `d=1` it is Bass for every graph with no regularity assumption, trees and isolated vertices included by rational cancellation. The `d=2` total is `Z_ord = det K_2(-u) det M_2(-u) / [det K_1(u) det M_1(u)]`. A companion device: algebraic lengths `l(sigma)` can be converted to a transfer matrix linear in `u` by giving each state a chain of `l(sigma)` delay states of the **same parity**, weight 1 along the chain and the sign `s_k` on the exit arrow --- "the sign is inserted once per successor arrow, not at every delay tick", or the identity breaks.
- Lead: this is the object to build on for arbitrary complexes. Caveat recorded: "calling `M_1` a vertex determinant is valid only if its rational dependence on the full forbidden-transition matrix is stated", and nobody has asked what the poles of `M_k` mean spectrally. The delay-space trick is a general recipe for converting a zeta with unequal prime lengths into an ordinary linear transfer operator --- and the notebook's side-B objects have lengths `log p`, so whether it transfers is an untested question.
- Where: report/sections/08e_complex_zeta_graded.tex:44-66; notes/complex-zeta/astra-proofs.md:245-279, :376-390

### G2-T9-5 Finite cochain determinant cancellation holds for *any* degree `-1` map
- Absorbs: L13-108
- Class: LEAD-unpursued
- Raised by: prover (correcting an orchestrator draft)
- What: For a bounded cochain complex over `C(u)`, any degree `-1` map `h` and any `c`, `prod_i det(F_i | C^i)^{(-1)^i} = prod_i det(F_i | H^i)^{(-1)^i} = c^{sum(-1)^i dim C^i}`; **neither `h^2 = 0` nor `h = d^*` is required**. The exponent is the dimension count of the complex used, e.g. `sum(-1)^i (i+1) f_i` for pointed cochains --- already `chi = 1` against `0` on a single edge. "The draft's identification of the cochain product's exponent with `chi` was wrong."
- Lead: the freedom in `h` is completely unexploited. The theorem holds for *any* degree `-1` map, so there is a whole family of torsion identities nobody has looked at.
- Where: report/sections/08e_complex_zeta_graded.tex:19-42

### G2-T9-6 The tetrahedron obstruction and the vertex-collapse conjecture
- Absorbs: L13-109, L13-127, L08-012, L08-013, L08-014, L08-016
- Class: PARTIAL
- Raised by: orchestrator (asked for the universal identity), prover (refuted it), then registered as a conjecture
- What: On `X = ∂Δ^3`, `T_1 = 0` and `det(I + uT_2) = (1-u^4)^6`, and there is **no** matrix polynomial `P(u)` of any size or degree with `gzeta = (1-u^3)^chi / det P(u)`: that would force `det P = (1-u^3)^2/(1-u^4)^6`, which has poles at `u = -1, ±i`. The octahedron `K_{2,2,2}` gives the same phenomenon. So vertex collapse is a *building* phenomenon and dies on a four-vertex sphere. `conj:vertex-collapse-characterisation` then asks for a combinatorial characterisation of the complexes for which `B_X(u) = (1-u^{d+1})^chi / gzeta_ord(X,u)` is the determinant of `I - uA + sum_{j>=2} u^j Q_{j-1}` with `Q_{j-1}` built from local link data. Building quotients are sufficient; the tetrahedron gives a necessary polynomiality condition (`B_X` polynomial of degree at most `(d+1) f_0`, plus `[u] det = -Tr A`); and the orchestrator's expected answer, "links are generalised polygons of the same parameters", was refused as an assertion --- a link-parameter condition supplies neither a cyclic type structure nor an identified Bruhat--Tits universal cover, and even a recognition theorem would need a further argument transferring the Hecke/cochain data.
- Lead: **compute `B_X` over a census of small 2-complexes and look for the ones where it is polynomial of the right degree.** That is a finite, scriptable search for a non-building collapse, and nobody ran it. Finding one would be a genuinely new zeta and a much larger supply of exactly-solvable graded transfer operators than the building family.
- Where: report/sections/08e_complex_zeta_graded.tex:68-79; report/sections/08f_complex_zeta_quantum.tex:260-271; notes/complex-zeta/astra-proofs.md:328-347, :300-327

### G2-T9-7 The small exact test complexes, and the vanishing orders with no topological meaning
- Absorbs: L13-115, L08-038, L08-021, L08-076
- Class: EXPLORED-registered
- Raised by: prover / orchestrator; every entry recomputed by the reviewer
- What: `C_3` unfilled gives `(1-u^3)^{-2}`; the **filled** `Δ^2` gives total 1 --- "there is no forced `(1-u^3)` factor", the small surprise, so the `(1-u^{d+1})^chi` shape is not universal; `∂Δ^3` gives `(1-u^4)^6`; the optional clique-only fourth test, the octahedron `K_{2,2,2}` with `f = (6,12,8)`, gives `(1-u^6)^8/(1-u^4)^6` with reduced degrees 36 and 12, again with a pole at `u=-1` in the would-be vertex expression. On vanishing orders, `ord_{u_0} Z_pt = chi(X) - ord_{u_0} det P_n` at `u_0^n = 1`, which on a connected rank-three Ramanujan quotient is `chi - 1` at each cube root of unity; but for the ordered default there is **no formula at all**: `Z_ord(Δ^2) = 1` despite `chi = 1`, and `Z_ord(∂Δ^3)` has order **6** at `u=1` despite `chi = 2` and `b_1 = 0`. Trap flagged: the clique complex of `K_4` is the *filled* `Δ^3` with all flows zero, a different object from `∂Δ^3` --- "essential for interpreting a surface-like effect of the odd sector".
- Lead: these are the standing regression tests for any future graded-zeta code. Two open items: what the order-6 on `∂Δ^3` counts (six chamber 4-cycles?) might be a small structural theorem; and the brief's requested non-building tests were **substituted, not run** --- in particular a 7-vertex triangulated torus is the one test with `b_1 != 0`, the only case where a Betti number could show up in a vanishing order, and it has never been computed.
- Where: report/sections/08e_complex_zeta_graded.tex:201-211; notes/complex-zeta/astra-proofs.md:1012-1035, :448-465; notes/complex-zeta/astra-brief.md:29

### G2-T9-8 The recommended object: a graded geodesic determinant with specified data --- uniqueness unproved
- Absorbs: L13-114, L08-037
- Class: PARTIAL
- Raised by: prover, as the verdict of the whole brief
- What: Specify per degree `k` a state set `S_k`, a successor relation with multiplicities, a positive integer algebraic length `l_k(sigma)`, a step transport `U_{sigma tau}` on a fibre `V`, and give degree-`k` space parity `k+1`. Then `Z = sdet_W(I - ⊕_k (-1)^{k+1} T_k^U(u))^{-1}`. The definition is functorial under isomorphisms preserving states, lengths, successor incidences and transports --- but "it is not proved unique among possible choices of higher-dimensional geodesic". For a graph the default is Hashimoto's operator with only an even flow sector; for a building quotient it is the completed vertex product; Kang--Li's zeta is obtained by retaining only the edge factor.
- Lead: prove uniqueness, or exhibit a genuinely different higher-dimensional geodesic and compare the zetas. If some naturality axiom pinned the geodesic data down, "the zeta that wants to exist" would become a theorem rather than a recommendation.
- Where: report/sections/08e_complex_zeta_graded.tex:188-198; notes/complex-zeta/astra-proofs.md:985-1011

### G2-T9-9 Opposition, not non-incidence, is the building's successor rule
- Absorbs: L13-106, L08-071
- Class: EXPLORED-negative
- Raised by: prover (refuting an orchestrator draft); reviewer sharpening
- What: The unrestricted ordered-cell flow `T_1` is **not** the block sum `uL_E ⊕ u^2 L_E^t` even after replacing `u^2` by `u`: its outdegree is `2q^2 + q` against `q^2` for `L_E`, and its directed-colour classes are not invariant. "The `u^2` is an algebraic length, not a matrix square, and the `3!` orderings do not realise `L_B` once." Also refuted: the orchestrator's assertion that the total graded zeta equals Kang--Li's edge zeta --- it is the **completed vertex `L`-function**. The reviewer sharpened the negative: of the `2q^2 + q` unrestricted successors of a colour-1 directed edge, exactly `q^2` preserve the directed-edge colour and exactly `q^2 + q` flip it (verified exactly for `q = 2,3,5`), so **the colour-preserving part is precisely `L_E`** and the colour-flipping transitions are the entire discrepancy.
- Lead: any attempt to define a higher-dimensional Hashimoto operator by "don't backtrack" uses the wrong rule. But the reviewer's sharpening suggests a concrete unbuilt object: a **colour-graded** version of the ordered flow, block-triangular in the colour grading, interpolating between the ordered and building rules. Never written down.
- Where: report/sections/08d_complex_zeta.tex:291-320; notes/reviews/complex-zeta-2026-09-13.md:50, :589-593

### G2-T9-10 Alternatives on general complexes: the combinatorial Ruelle zeta, weighted complexes, size grading
- Absorbs: L08-007, L11-043, L11-040, L11-047
- Class: LEAD-unpursued
- Raised by: papers, recorded by the orchestrator/extractor
- What: On any triangulation of a compact oriented `n`-manifold, Benard--Chaubet--Dang--Schick count primitive closed geodesics in the `(n-1)`-skeleton (geodicity = LLP's condition), weight by `±1`, take the **direct** product (Selberg/Deitmar convention, no reciprocal), and get a polynomial of degree `|T^{(n-1)}|` vanishing to order `b_1(M)` at `z = (n+2)^{-1}`, with an `L^2` version whose leading coefficient is a Fuglede--Kadison determinant. It has **no** Ramanujan notion and **no** RH. Two other threads: Hong--Kwon treat a non-cocompact `PGL_3` lattice and "extend the definition to **weighted** complexes ... we define the edge zeta function for those and express it in terms of a determinant, analogous to the Bass--Ihara formula"; and a non-uniform Ihara--Bass exists with a prefactor `f_H(mu) = prod_k (1-mu)^{m_k(k-1)-n} (1+mu(k-1))^{m_k-n}` **graded by hyperedge size**, plus the observation that a `q`-dimensional cubical complex is a hypergraph on `(d-1)`- and `d`-cubes, plus a Bartholdi zeta for hypergraph coverings.
- Lead: this is the only object in the sweep that exists on an arbitrary complex *and* has a genuine numerator whose order is a Betti number --- ask whether a Ramanujan/spectral-radius notion can be attached to it at all. If yes, the notebook gets a zeta of an arbitrary complex; if no, the torsion-type and Ramanujan-type programmes are genuinely disjoint. Separately: check whether Hong--Kwon's weighted-complex proof accommodates *matrix* weights (one step from an operator-weighted Bass--Ihara, reusing existing machinery), and note that hyperedge size is a **second grading axis** distinct from parity.
- Where: notes/complex-zeta.md:63-67; notes/extract/complex-zeta-sources.md:998-1102, :859-927, :1241-1259

### G2-T9-11 The open object: a quantum (Kraus) zeta of a complex
- Absorbs: L11-026, L11-023, L11-024, L11-027, L11-028, L11-048, L11-035
- Class: LEAD-unpursued
- Raised by: extractor, after five named negative searches
- What: Five searches all return either quantum expanders (channels, no complexes) or Ramanujan complexes (complexes, no channels), never both. The two known quantum-flavoured zetas are the `Ad(U)`-weighted Ihara zeta of a **graph** (Matsuura--Ohta) and a density-matrix edge zeta of a **complete graph** (Bradshaw--LaBorde et al., whose authors call their eigenvalue--singularity correspondence "a variant of the Hilbert--Polya conjecture associated to this zeta function" --- but it is an ordinary edge zeta with `rho`-derived scalar weights, not Kraus-weighted and not on a complex). Material already fetched and never exploited: Szegedy-type quantum walks on simplicial complexes (verified: zero occurrences of "zeta" in the source, likewise its search sequel); First's Ramanujan-property paper (its eight `zeta` hits are all the Greek letter as a variable); Kamber's `L^p`-expander complexes; Lubotzky's high-dimensional-expander survey; the Ramanujan-digraph survey; and LLP, "where the higher-dimensional geodesic flow non-backtracking operator lives". That operator is the right shape: a `j`-dimensional geodesic flow on pairs (basepoint, `j`-cell), **multi-valued rather than a permutation**, geodicity enforced by "the next `(j+2)`-set is not a cell", reducing to non-backtracking at `j=1`, with digraph zeta `det(I - uA_Y)^{-1}` and Ramanujan complex ⟹ Ramanujan digraph ⟹ weak RH **for every affine building**. The LSV generators are recorded concretely: `b_u = 1 - r z^{-1}` with `r in F_{q^d}^x` of norm 1, one per `u in F_{q^d}^x / F_q^x`, quotient by a congruence subgroup giving `PGL_d(F_{q^e})`, 1-skeleton the Cayley graph on colour-`k` products, complex the clique complex, Hecke operators the colour-shift sums --- and no zeta is defined in those two papers.
- Lead: **define Kraus-weighted successor operators `T_k` on `k`-facets of a 2-complex and prove the alternating-product identity.** The concrete first move is to Kraus-weight LLP's branching operator, whose proof is "a simple combinatorial treatment" that may survive operator weights where representation-theoretic proofs would not; build an LSV complex numerically from the generators (the `scripts/weil_lps.py` machinery exists for the graph case); and attach a zeta to the existing quantum walk on a complex. Any of these would be a genuinely new object and the natural home for the grading.
- Where: notes/extract/cohomological-zeta-sources.md:1773-1804, :1681-1734, :1763-1772, :1824-1829; notes/extract/complex-zeta-sources.md:588-723, :1307-1425

### G2-T9-12 The strategic verdict: a testbed, not a Phantasm
- Absorbs: L08-077
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: "None of this touches the Riemann side directly. What it buys is a supply of exactly-solvable graded transfer operators with a Ramanujan property, and a sharp negative: there is no zeta of a general complex to build a Phantasm on."
- Lead: use the building family as a **testbed**. Every identity a real Phantasm must satisfy can be checked here first, exactly.
- Where: notes/complex-zeta.md:230-232

### G2-T10-1 The exact graded superdeterminant presentation
- Absorbs: L13-110, L08-017, L08-002
- Class: EXPLORED-registered
- Raised by: orchestrator (T3 of the brief), proved by the prover, reviewer VALID including the sign law
- What: `gzeta_ord = sdet(I - u Theta)^{-1}` exactly, with `W_+ = ⊕_{k odd} H_k`, `W_- = ⊕_{k even, k>=2} H_k`, `Theta = ⊕_k (-1)^{k+1} T_k`, and `log gzeta = sum_m (u^m/m) str(Theta^m) = sum_m (u^m/m) sum_k s_k^{m+1} Tr(T_k^m)`. The order at `u_0 != 0` is the odd minus the even algebraic multiplicity of `u_0^{-1}`. This is the exact graded presentation TJO wanted when he said "these zeros may be associated naturally with surface-like qualities" --- but the surviving form of that phrase is much weaker: "the surface-like feature that survives scrutiny is the possibility of an odd chamber contribution to a graded divisor. It is not an identification with surface cohomology or a universal Betti-number formula." Two drafted readings were refuted: "the zeros are exactly the odd eigenvalues" is false without the reciprocal, sign, multiplicity and cancellation qualifications; and the reviewer checked the sign law against the plausible wrong variant `s_k^m`, which fails.
- Lead: the caution is G2-T10-2. Keep the `s_k^{m+1}` sign law on record for anyone re-deriving it.
- Where: report/sections/08e_complex_zeta_graded.tex:82-105; notes/complex-zeta/astra-proofs.md:350-375, :985-1011

### G2-T10-2 "Fermionic zeros" names a net odd multiplicity that must be checked after cancellation
- Absorbs: L13-126, L08-018
- Class: EXPLORED-negative
- Raised by: prover, summarised by orchestrator
- What: "The odd sector is real as a graded *presentation* and unreal as a divisor." On the building vertex side `L_vertex(u) = D_B(u)/[(1-u^3)^chi D_E(u)] = 1/det P_3(u)` is a **reciprocal polynomial**, so it has no finite zeros: every apparent numerator zero cancels against an edge or Euler factor, and calling the chamber zeros uncancelled zeros of `L_vertex`, as the draft did, is wrong. The parallel with Ruelle and with Knill's supertrace is parity and alternating structure, "not an identification of spaces or weights". Extra twist recorded by the reviewer: in a *twisted* block the Euler factor is not even a power of `1-u^3`, so the cancellation bookkeeping changes block by block. Closing verdict: "None of this touches the Riemann side directly. It is a supply of exactly-solvable graded transfer operators with a Ramanujan property, not a channel whose zeta is `zeta(s)`."
- Lead: **any Phantasm claim of the form "the zeros are the odd modes" has to survive this cancellation test.** The sharp form of TJO's question --- find geodesic data where the odd sector survives cancellation --- is completely open.
- Where: report/sections/08f_complex_zeta_quantum.tex:238-245, :256-258; notes/complex-zeta/astra-proofs.md:391-400

### G2-T10-3 The cell-dimension ↔ cohomology dictionary is parity only, and one circle is not one parity sector
- Absorbs: L08-019, L13-122, L08-020
- Class: EXPLORED-negative
- Raised by: orchestrator (drafted the literal identification), prover (refuted it); numerics confirmed
- What: The substitution `i = k-1` matches the Grothendieck--Lefschetz exponents `(-1)^{i+1}` but **identifies no spaces and assigns no Weil weight**. A 3-cycle already disproves the literal reading: six ordered-edge states against one-dimensional ordinary `H^0`, and the graph also has nonzero `H^1`. "The word `H^0` only can describe the absence of an odd *flow* sector, not the ordinary cohomology of a graph." The spectral side kills the other tempting identification: tempered principal series give chamber roots `±q^{-1/2} alpha_i^{-1/2}` and edge roots `q^{-1} alpha_i^{-1}`; the tempered nonspherical type-(e) constituent gives one chamber root at `q^{-1/2}` and two at `q^{-1/4}`; Steinberg twists give the unit circle; one-dimensional constituents give *trivial* roots at `q^{-1}`. So **the circle `q^{-1/2}` is not "the odd sector", and a single constituent can contribute to two circles at once**; the `Ã2` numerics reproduce exactly the radii `{1, 3^{1/4}, 3^{1/2}}` for `L_B` and `{3, sqrt 3}` for `L_E` and nothing else.
- Lead: "None of these results constructs ordinary cohomology whose Frobenius is the cell flow." Constructing one is the open task --- it would be the actual Weil-cohomology analogue the Phantasm wants. Meanwhile the "weight-1, curve-like" sector exists only as a spectral factorisation, and anyone wanting a curve analogy must first make that factorisation canonical.
- Where: notes/complex-zeta/astra-proofs.md:401-418, :419-447; report/sections/08e_complex_zeta_graded.tex:107-127

### G2-T10-4 The total object needs a Berezinian; cell chirality and flow superparity are distinct gradings
- Absorbs: L13-111, L08-022, L08-023
- Class: EXPLORED-negative
- Raised by: orchestrator (asked for a single gamma-five Dirac operator), prover (delivered half)
- What: An explicit incidence matrix `D_k(z)` on `H_{k-1} ⊕ H_k ⊕ H_{k+1}` has two Schur evaluations giving both the flow determinant and the compressed form, and giving its auxiliary space parity `k+1` gives `sdet D_flow = gzeta^{-1}`. But "an ordinary Berezin integral gives `det D`, not a reciprocal or a superdeterminant merely because `D` has chiral blocks"; the construction uses separate auxiliary copies, so **cell chirality and flow superparity are distinct gradings** --- a `(k-1)`-cell used as an auxiliary variable in `D_k` has a different parity from the same cell as a flow state in `D_{k-1}`. "The draft's universal ordinary fermion determinant with flow parity equal to cell chirality does not exist." A related structural obstruction: the doubled cochain linearisation `B(u)` on `C ⊕ C[1] ⊕ C[1]` with blocks `(cI, d, delta; -delta, I, 0; -d, 0, I)` is even with Berezinian `c^{chi_pt}`, and it is needed *because* `(d+delta)^2 = d delta + delta d + delta^2` carries an extra degree-(-2) term (Kang--Yu state `delta_i ∘ delta_{i+1} != 0`), so the building "Laplacian" is not a square of a Dirac operator.
- Lead: construct geodesic data in which the two gradings **do** coincide --- that is precisely what would make "fermionic zeros" a statement about cells rather than an auxiliary bookkeeping device. And construct a genuine self-adjoint/gamma-five Dirac operator for building cochains: Matsuura--Ohta's stronger graph structure "cannot be imported without a separate construction", and that construction is what would make the Berezinian a physics object.
- Where: report/sections/08e_complex_zeta_graded.tex:130-152; notes/complex-zeta/astra-proofs.md:478-536, :547-600

### G2-T10-5 The plus sign in `det(I + uL_B)`
- Absorbs: L13-125
- Class: EXPLORED-registered
- Raised by: paper (Kang--Li), flagged by orchestrator
- What: The `PGL_3` Bass identity carries a **plus** sign on the chamber factor and a `u^2` on the transposed edge factor; the `Ã2` numerics confirm the plus sign is essential (using `det(I - uL_B)` first fails at `u^15`).
- Lead: the plus sign is a graded/parity sign in disguise and connects directly to the alternating-product reading of the torsion literature.
- Where: report/sections/08d_complex_zeta.tex:28-41

### G2-T11-1 Arbitrary channel weights preserve the compression --- and nothing else
- Absorbs: L13-112, L08-024, L08-029
- Class: EXPLORED-registered
- Raised by: orchestrator (T5 of the brief), proved by the prover, reviewer VALID
- What: Putting an arbitrary endomorphism on each directed edge preserves `T_k^E = S_k^E R_k - F_k^E` and the Schur factorisation **exactly**, "with no positivity, pairing, invertibility, or flatness hypothesis and no inverse of any `E_e`". And `Tr(T_k^E)^m = sum_{based closed walks} Tr_V(E_m ... E_1)`, which for `Ad`-weights is `sum |Tr(B_m ... B_1)|^2 >= 0` --- **adjoint pairing is not needed**, complete positivity of the step maps suffices. What is *not* preserved: for an invertible **flat** local system of rank `r`, `Z_{pt,E}(u) = (1-u^n)^{r chi}/det P_{n,E}(u)`, and there is no corresponding assertion for arbitrary nonflat Kraus weights. Adjoint pairing supplies neither flatness nor the cancellation --- a unitary, inverse-paired channel connection on a filled triangle (`B_01 = [[0,1],[1,0]]`, `B_12 = diag(1,-1)`, `B_02 = I`) has nonzero curvature.
- Lead: **open --- what the Euler/torsion factor becomes for non-flat channel weights.** That is the direct quantum analogue of the question the notebook cares about and the answer is simply not known. Also an open invitation in the prover's own words: "Any other successor rule with the same overlap admits the same construction, by letting `F` be the sum of its forbidden weighted transitions" --- the machinery is not tied to non-backtracking or to opposition. Unexploited: the pair factor `det_V(I - u^2 E_{(y,x)}E_{(x,y)})` for non-inverse-paired weights, which above dimension one does *not* remove the upper-face term.
- Where: report/sections/08e_complex_zeta_graded.tex:155-176; notes/complex-zeta/astra-proofs.md:603-668, :787-812

### G2-T11-2 The full-cover connection is pure gauge; use voltage quotients
- Absorbs: L13-116, L08-027, L08-072
- Class: EXPLORED-negative
- Raised by: prover (refuting an orchestrator draft); reviewer numerics
- What: On a Cayley complex the forward weights `E_{(g,gs)} = hol(s)` are generally **not flat** (a representation gives `rho(st) = rho(s)rho(t)` while flatness asks `rho(t)rho(s)`; on `Cay(Q_8, {±i,±j,±k})` 192 of 192 ordered 2-cells fail, and on the `Ã2` complex 39 of 52 chambers fail). The covariant convention `hol(s^{-1})` is **pure gauge**: `E_{(g,gs)} = F_{gs} F_g^{-1}` with `F_g = pi(g^{-1})`, so `det(I - uT_k^E) = det(I - uT_k)^{dim V}` and every closed straight walk of the full complex has identity holonomy. The minimal witness is the four-cycle with `G = Z/4`, separating the full twist `(1-u^4)^2` from the trivial-block determinant `(1-u)^2`. The genuine Artin object is the **voltage quotient** (13 states, 9 successors each, in the `PGL_3(F_3)` case). One unexplained numerical fact, flagged by the reviewer as "not a defect": on `Cay(Q_8, ...)` the *chronological* (totally non-flat) convention still gives `det(I - uT_1^{E,chrono}) = det(I - uT_1)^2` to `1.1e-15` (96x96 versus 48x48 eigenvalue multisets).
- Lead: design rule --- whenever the notebook wants a genuine twisted zeta it must use quotient voltages, not a connection on the cover. And: **is there a theorem behind the chronological coincidence?** A determinant identity holding for a totally non-flat representation connection would be a genuinely new fact and would widen the twisted-zeta class considerably; at present it is one numerical coincidence on one group.
- Where: report/sections/08f_complex_zeta_quantum.tex:20-31, :207-224; notes/complex-zeta/astra-proofs.md:681-738; notes/reviews/complex-zeta-2026-09-13.md:340

### G2-T11-3 Artin bookkeeping traps: `a_hol` not `d_hol`, and simplex stabilisers
- Absorbs: L13-117, L13-118, L08-028, L08-042
- Class: EXPLORED-registered
- Raised by: prover; confirmed numerically
- What: With a free action on states, `det(I - s_k T_k(u)) = prod_hol det(I - s_k T_{k,hol}(u))^{d_hol}`. But for `R = ⊕ a_hol hol` the Artin determinant has exponents `a_hol`, **not** `d_hol`: `R = pi ⊗ conj pi` need not embed in a single regular representation. "What always transfers is spectral support. An equivariant *matrix* identity restricts to every block; a scalar determinant equality need not." Euler-factor bookkeeping has the same trap: `gzeta_hol = F_hol/det(P_n|C_{0,hol})` with `prod_hol F_hol^{d_hol} = c^{chi(X)}`, and only if the action is free on **unpointed** simplices does this collapse to `F_hol = c^{d_hol chi/|G|}`; with simplex stabilisers the fractional power is not a rational determinant and must not be asserted. The `Ã2` numerics show it exactly: for the 12-dimensional `pi` the naive `c = chi · dim pi/|G| = 64` is right, while the whole anomaly sits in the trivial block, where `chi/|G| = 16/3` is replaced by `(1-u)^{13}(1-u^3)^1`. 24336 of 97344 triangles carry `Z/3` stabilisers.
- Lead: the global check `prod_hol F_hol^{d_hol} = c^chi` forces the remaining irreps to contribute `(1-u)^{-13}` in total, and **only two blocks were built, so that sum is not checked**. The numerics lane also never built the 144-dimensional `pi ⊗ conj pi` block (the `L_B` block would be 7488x7488, "judged not worth the time") and could not get full-space spectra without the character table of `PGL_3(F_3)` --- which is classical and available, so this is a bounded task that would close the Euler-factor audit.
- Where: report/sections/08f_complex_zeta_quantum.tex:33-44, :46-56; notes/complex-zeta/astra-proofs.md:749-786; notes/a2-complex-zeta/numerics.md:200-237

### G2-T11-4 Ramanujan complexes give Ramanujan quantum expanders for free --- and the channel adds nothing
- Absorbs: L13-119, L08-031, L08-041
- Class: EXPLORED-negative
- Raised by: prover (theorem), orchestrator (numerics), both recording the deflating rider
- What: Harrow-type transfer makes the vertex/colour channels `Phi_k(X) = |S_k|^{-1} sum_{s in S_k} pi(s) X pi(s)^†` commuting, normal, unital, trace-preserving, with `Phi_k^* = Phi_{n-k}` and common fixed space the commutant `pi(G)'`, and they satisfy the `Ã2` Ramanujan condition relative to the **exceptional** space. The 12-dimensional irrep of `PGL_3(F_3)` gives a genuine Ramanujan quantum expander of type `Ã2`: largest nontrivial `|13 mu| = 6.4817 < 3q = 9` and below Hastings' `2 sqrt(D-1) = 6.9282` at `D = 13`, with all 143 nontrivial joint eigenvalues inside the tempered deltoid. But **"it cannot fail"**: `Phi_1 = A_1^{(pi ⊗ conj pi)}/13`, so `13 spec(Phi_1)` is a sub-multiset of `spec(A_1)` on `C[G]` --- Ramanujan complex ⟹ Ramanujan quantum expander, automatically, and the channel adds no new spectral values.
- Lead: this is a limitation, not an achievement. If the quantum twist is ever to *do* something, the weights must not be of the form `pi ⊗ conj pi` on a Cayley complex --- they must be non-flat, non-representation weights, which is exactly the case where nothing is known (G2-T11-1).
- Where: report/sections/08f_complex_zeta_quantum.tex:59-73, :192-205, :248-252; notes/a2-complex-zeta/numerics.md:162-179

### G2-T11-5 The converse: coverage, and the exceptional space
- Absorbs: L13-120, L08-032, L08-030
- Class: EXPLORED-registered
- Raised by: orchestrator (expected the wrong criterion), prover (corrected it)
- What: Let `B_X` be the irreducibles having a nonexceptional joint eigenvalue outside the tempered spectrum. Then `R` is Ramanujan iff `B_X ∩ supp(R) = ∅`, and `X` is vertex-Ramanujan iff `B_X = ∅`; **coverage** of every nonexceptional irreducible by `pi ⊗ conj pi` is sufficient for the converse. Faithfulness is not: `Cay(Z/28, {±1,±3})` is 4-regular bipartite and not Ramanujan (`2cos(pi/14) + 2cos(3pi/14) = 3.5135 > 2 sqrt 3`), yet a faithful character has `pi ⊗ conj pi = 1` and a vacuous quantum condition --- for an irreducible `pi`, central elements act by scalars, so its adjoint representation can miss all irreducibles with nontrivial central character. Separately, the drafted "removing the channel fixed points removes all trivial modes" is false on a **partite** complex: if `X` has a nonconstant type character `chi` with `chi(s) = omega^k` on `S_k`, then for `pi = 1 ⊕ chi` the off-diagonal matrix units carry channel eigenvalues `omega^{±k}` --- not common fixed points --- yet their unnormalised first eigenvalue has modulus `q^2+q+1 > 3q`. One must remove the **exceptional space**.
- Lead: coverage is the right notion for transferring Ramanujan-ness back from a channel to a graph, and it has not been used elsewhere in the book; a quantum-expander certificate is only as strong as the support of `pi ⊗ conj pi`. Also outstanding: the reviewer notes that no such partite `X` was ever exhibited ("e.g. `PGL_3(F_q)` with `3 | q-1`"), so **the smallest 3-colourable Ramanujan complex is unbuilt** --- and it is the only setting where the exceptional-space correction bites.
- Where: report/sections/08f_complex_zeta_quantum.tex:75-86; notes/complex-zeta/astra-proofs.md:878-901, :825-833

### G2-T11-6 The `Ã2` anomaly: the identity holds where its hypothesis fails
- Absorbs: L13-123, L08-036, L08-040, L08-043
- Class: PARTIAL
- Raised by: numerics agent (the surprise), prover (the descent theorem)
- What: The smallest `Ã2` Ramanujan complex, the LSV Cayley complex of `PGL_3(F_3)` on 5616 vertices, is **not 3-colourable** (LSV's `r = ord(y/(1+y))` is 1 and the group is simple, so there is no epimorphism onto `Z/3`; for `q=3` no `e` repairs it since `3 | q^e - 1` is impossible), so Kang--Li's type-preservation hypothesis fails; and all 13 generators have order 3, so the 24336 triangles carry `Z/3` stabilisers and `G` is not free on unpointed 2-cells. **Yet the corrected identity holds exactly to `u^18`**, degree 308880 on both sides, with `chi` fitting at every order --- "two facts not anticipated in the brief". A type-preserving 3-fold cover was built alongside (`Gamma~ = Gamma(I) ∩ Gamma_1`, `Gamma/Gamma~ = PGL_3(F_3) x Z/3` by Goursat, `V = 16848`, `chi = 89856`), whose closed-walk counts are `3x` the base counts restricted to total colour shift 0, and on which `Tr(L_E^m) = Tr(L_B^m) = 0` unless `3 | m`. The prover then proved the descent: for `Gamma` torsion-free cocompact with descended cyclic type-difference data but not type-preserving, the pointed determinant identity descends from `Gamma_0 = Gamma ∩ ker tau`, using `chi(X_0) = |H| chi(X)` and the fact that characters of `H ⊂ Z/n` extend through `tau` and preserve temperedness. Types of *directed* edges are still globally defined via `S_1` vs `S_2`, which is all `L_E`, `L_B` need.
- Lead: a genuinely new little theorem produced by a numerical surprise --- and nobody has asked how far it widens the class (quotients with torsion? with simplex identifications?). Two further unexplored consequences: what else in the Kang--Li package survives without type preservation, and whether the `Z/3` colour grading of the trace sequence on the cover is the "letters" grading of the notebook's other lanes.
- Where: report/sections/08f_complex_zeta_quantum.tex:124-138, :150-165; notes/complex-zeta/astra-proofs.md:963-984; notes/a2-complex-zeta/numerics.md:34-54, :136-139

### G2-T11-7 The `Ã2` numerics: corrections, the degree audit, and a reusable technique
- Absorbs: L13-124, L08-039, L08-073, L08-044
- Class: EXPLORED-registered
- Raised by: numerics agent and prover; adjudicated by the reviewer
- What: The placement written in the orchestrator's brief, `(1-u^3)^chi det(cubic) det(I+L_B u) = det(I-L_E u) det(I-L_E^t u^2)`, fails at `u^3` (residual `-59904`) and fails the degree count (398736 against 219024); the correct cleared form is `det P_3 · det(I + uL_B) = (1-u^3)^chi det(I - uL_E) det(I - u^2 L_E^t)`. Using `det(I - uL_B)` first fails at `u^15`. The unrestricted ordered edge rule has outdegree `2q^2+q = 21` against `L_E`'s `q^2 = 9`; on all six orderings of a chamber, `det(I+uT_2) = det(I+uL_B)^2`. The predicted chamber eigenvalue radius `q^{3/4}` was stale (traceable to the non-tempered type-(d) row, absent on a Ramanujan quotient); the correct radii are `{1, q^{1/4}, q^{1/2}}`, observed as `1.316074 = 3^{1/4}`. Counts: `|G| = 5616`, `f_1 = 73008`, `f_2 = 97344`, `chi = 29952`; pointed edge space 146016, pointed chamber space 292032, all-ordered chamber space 584064. Technique worth keeping: the cubic `z^3 - (l/q)z^2 + (conj l/q)z - 1` is self-inversive, so all roots are unimodular iff both roots of `3z^2 - 2sz + conj s` lie in the closed disc --- stable to `2e-14`, unlike `np.roots` on the near-degenerate cubic, which gave spurious `1e-7` defects.
- Lead: the degree audit `3chi + 3f_1 = 3f_0 + 3f_2` is the cheapest sanity filter on any proposed placement of factors, and it is what killed the original one. Cohn's criterion is reusable for any future temperedness check.
- Where: report/sections/08f_complex_zeta_quantum.tex:150-177; notes/a2-complex-zeta/numerics.md:23-33, :63-68, :128-145; notes/complex-zeta/astra-proofs.md:1036-1058

### G2-T11-8 What the adversarial review explicitly did not check
- Absorbs: L08-074
- Class: PARTIAL
- Raised by: Opus reviewer
- What: Four items in an otherwise 47/47 VALID note. The `PGL_3(F_3)` complex was not rebuilt from the LSV generators (only the vertex link was); Kang--Yu's `thm:Phi-determinants` and the local factorisation `Phi_i = c W_i^{-1} J_i (I - s_i Sigma_i) J_i^{-1} Q_i^{-1}` were confirmed to exist at the cited addresses but **not verified line by line**; the global identity `prod_rho F_rho^{d_rho} = c^chi` was confirmed only on two isotypic blocks; the type-cover descent was checked only through order `u^18`.
- Lead: the first two are load-bearing, since everything conditional on Kang--Yu rests on an unverified technical proof.
- Where: notes/reviews/complex-zeta-2026-09-13.md:612

### G2-T12-1 Higher-rank RH is one-sided and the interior of the band is genuinely occupied
- Absorbs: L13-099, L08-005, L11-036, L11-032
- Class: EXPLORED-negative
- Raised by: papers (Lubetzky--Lubotzky--Parzanchevski; Kang--Li; Fang--Li--Wang), amplified by the prover
- What: For **every** building, a pole at `u = k^{-s}` has `|s| = 1` or `Re s <= 1/2`. The inequality is not an equality: poles with `|Re s| < 1/2` occur, already with `|Re s| = 0` in the graph case and with `0 < |Re s| < 1/2` in higher dimension --- LLP say so explicitly, and Parzanchevski states the digraph form, "a `k`-regular digraph `D` is Ramanujan if and only if every pole satisfies `Re s = 1` or `0 <= Re s <= 1/2`". Nor is RH a single-circle statement: for `PGL_3` Ramanujan is equivalent to the vertex cubic's nontrivial zeros on `|u| = q^{-1}`, **or** the chamber factor's on the **three** circles `1, q^{-1/2}, q^{-1/4}`, **or** the edge factor's on the **two** circles `q^{-1}, q^{-1/2}`; for `PGSp_4` the edge and chamber factors give only **bands** of moduli (`q^alpha`, `-2 <= alpha <= -1`).
- Lead: since the interior is occupied, no universal duality can close the bound, and what remains is Weil-positivity-as-bound block by block. Strategically: if the notebook's transfer operator is non-normal (as a channel generally is), expect a **band** rather than a line, and the "uniform decay" the programme seeks may have to be restated as a bound, not an equality --- which changes what "Ramanujan" must mean for the Phantasm.
- Where: report/sections/08d_complex_zeta.tex:81-89; notes/complex-zeta.md:53-59; notes/extract/complex-zeta-sources.md:106-135, :700-763

### G2-T12-2 Kamber's `L_p` criterion: a continuum of Ramanujan notions, with the bound inverted
- Absorbs: L13-100, L08-033, L08-079, L11-041, L11-042
- Class: LEAD-unpursued
- Raised by: paper (Kamber), corrections by the prover
- What: With one Bernstein--Lusztig operator per simple coweight, `zeta = 1/prod_i det(1 - h_{beta_i} u^{l(beta_i)})` --- at `n=1` exactly Hashimoto --- and `X` is an `L_p`-expander **iff** every eigenvalue satisfies `|theta| <= q^{l(beta_i)(p-1)/p}` or `|lambda| = q`; `p=2` is Ramanujan, larger `p` interpolates. This is the only if-and-only-if in higher rank, and it supplies the converse LLP could not get, for buildings of general type. Two corrections. The bound is on **eigenvalues**, so it *inverts* to a **lower** bound `|u| >= q^{-(p-1)/p}` on pole radii --- the source's own corollary calls an eigenvalue a "pole", and any downstream reading of it as an upper bound on `|u|` would be wrong. And in the variable `u = b^{-s}`, `|lambda| = b^{Re s}`, so peripheral means `Re s = 1`; the printed `|s| = 1` is not a well-defined invariant because `Im s` is only defined mod `2pi/log b`. Scope caveat: the abstract's "any complex" means any quotient of a building. Naming: Kamber's `L_2`-expander = Kang's "strongly Ramanujan" = First's "flag-Ramanujan"; Kang's *Riemann Hypothesis and strongly Ramanujan complexes from `GL_n`* (JNT 161 (2016) 281--297) is the most general RH result for `Ã_n` and is **not on arXiv** (searched via the arXiv API, two WebSearch passes, and the author's own publication list).
- Lead: the `L_p` family is a *continuum* of Ramanujan-type properties with an iff spectral criterion, and the notebook uses only the endpoint --- exactly the graded/tempered scale that "graded Harrow continuum = temperedness" wants. **Define `L_p`-expander for a quantum channel.** Separately, obtain Kang JNT 2016: it is the one paper with detailed pole locations by representation type.
- Where: report/sections/08d_complex_zeta.tex:91-101, :282-289; notes/complex-zeta/astra-proofs.md:902-924; notes/extract/complex-zeta-sources.md:930-997, :1449-1461

### G2-T12-3 No universal functional equation in higher rank
- Absorbs: L13-121, L08-034, L08-081
- Class: EXPLORED-negative
- Raised by: orchestrator (asked which factors have a duality), prover (answered)
- What: `p_a(u) = 1 - au + q conj(a) u^2 - q^3 u^3` satisfies `p_a(u) = -q^3 u^3 conj(p_a(1/(q^2 conj u)))`, so with `A_2 = A_1^*` the vertex zero multiset is invariant under `u -> q^{-2}/conj u` with fixed circle `|u| = q^{-1}` --- the precise single-circle Hilbert--Polya-style reading, valid *before* imposing Ramanujan. Principal-series edge and chamber parts inherit dualities at `q^{-2}` and `q^{-1}`. But the **full** edge and chamber factors do not: a tempered nonspherical (type-e) block has one root at radius `q^{-1/2}` and two at `q^{-1/4}`, so fixing both radii needs `c = q^{-1}` and `c = q^{-1/2}` at once, and exchanging them needs multiplicities `1 = 2`. No single `u -> c/u` or `u -> c/conj u` works. Worse outside type `Ã`: in type `C̃_2` the RH-equals-Ramanujan statement degrades from circles to **bands**.
- Lead: "Separate restricted circles can be given separate normalisations, but this is not a functional equation for the entire factor." A **multi-scale functional equation** (one normalisation per circle) has never been written down and is the only route left to a two-sided statement here. Also: nobody read the `C̃_2` paper --- if the degradation to bands is generic outside type `Ã`, that is a strong structural hint that "zeros on a line" is a type-`A` accident, directly relevant to whether the Phantasm should expect a line at all.
- Where: report/sections/08f_complex_zeta_quantum.tex:99-109; notes/complex-zeta/astra-proofs.md:925-946; notes/complex-zeta.md:43-44

### G2-T12-4 What is left in higher rank: Weil positivity as a bound
- Absorbs: L13-128
- Class: EXPLORED-registered
- Raised by: prover / orchestrator
- What: Since RH is one-sided, the interior genuinely occupied, and there is no universal duality, what one has in higher rank is Weil-positivity-as-bound: the finite theorem applied block by block to each retained ordinary block.
- Lead: a graded version with negative multiplicities is what would be needed (see G2-T4-3).
- Where: report/sections/08f_complex_zeta_quantum.tex:111-121, :252-256

### G2-T12-5 The hypothesis register: eight external theorems used but not reproved
- Absorbs: L13-105
- Class: PARTIAL
- Raised by: prover (register T8.3)
- What: Nine `assumed` rows, all byte-cited: pointed-facet successor conventions; LLP branching flows and the digraph bound; the Kang--Li rank-three identity and its four-way RH; the Kang--Yu pointed cochain identity and its **local** factorisation; the Iwahori-spherical constituent table; the LSV joint Hecke spectrum and explicit complexes; Iwahori-spherical temperedness (H-STRONG: "this can be strictly stronger than the vertex condition"); and Kamber's normalised criterion.
- Lead: H-STRONG is the interesting one --- if LLP's Ramanujan condition can be strictly stronger than the vertex condition, then "Ramanujan complex" is ambiguous and every claim using the phrase needs to say which one it means.
- Where: report/sections/08d_complex_zeta.tex:207-289

### G2-T12-6 Every determinant factor is a Langlands `L`-function --- and `chi` vanishes at `q = 1`
- Absorbs: L11-033, L11-034
- Class: LEAD-unpursued
- Raised by: paper (Kang--Li--Wang) + extractor's aside
- What: Each determinant in the `PGL_3` and `PGSp_4` identities is identified with a Langlands `L`-function of a representation `pi` of the dual group (minuscule `pi_1, pi_2`; spin and standard) and simultaneously with a zeta counting `pi`-geodesic walks or galleries --- a Rosetta stone. And `chi(B_Gamma) = (1/3)(q-1)^2(q+1)N_0` for `PGL_3`, `(q-1)^2(q^2+q+1)N_p` for `PGSp_4`: **both vanish at `q = 1`**, where the building identity degenerates to the apartment identity.
- Lead: (i) ask which representation of which dual group the notebook's channel factors would correspond to --- if the dictionary applies, "Ramanujan" becomes "tempered", a representation-theoretic condition rather than a spectral one. (ii) The `q -> 1` ("field with one element") limit is a **free structural handle nobody has used**: it kills the torsion factor and leaves a purely combinatorial identity, and might give an `F_un` reading of the `chi` exponent.
- Where: notes/extract/complex-zeta-sources.md:458-528, :500-508

### G2-T12-7 The two-expression structure: "surface versus curve"
- Absorbs: L11-015, L11-053, L11-054
- Class: LEAD-unpursued
- Raised by: paper (Kang--Li / Kang--Li--Wang) + extractor
- What: The same zeta has two closed forms --- a Hecke/vertex form with `(1-u^3)^chi` in the numerator and the vertex + chamber determinants in the denominator, and a Hashimoto/edge form with only edge determinants (note the **plus** sign in `det(I + L_B u)` and the `u^2` on the transposed edge factor). The authors say the shape "is reminiscent of the zeta functions attached to a surface and a curve over a finite field" and that the identity "is likely to be the prototype of complex zeta functions in general". Also recorded: `Z_-(Gamma,u) = det(1+L_B u)/det(1-L_E u^2)` and `Z(Gamma,u) = det(1+L_B u) det(1+L_B u^{1/2})/[det(1-L_E u) det(1-L_E u^2)]`, whence `(1-u^3)^chi/det(vertex cubic) = Z_1 Z_-` --- note the half-power `u^{1/2}`.
- Lead: treat higher facet dimension as the source of extra cohomological degrees placed in numerator or denominator by parity, and build the two-dimensional analogue for a channel. The notebook's Theorem 1 already has two forms (`1 - uM(u)` and `1 + D - A`) --- ask whether they line up with the vertex/edge dichotomy, and whether a third (chamber-like) form is missing. The "algebraic vs geometric" factorisation has never been attempted.
- Where: notes/extract/cohomological-zeta-sources.md:1123-1224; notes/extract/complex-zeta-sources.md:160-184, :175-184

### G2-T13-1 One shape, five categories: the zeta as an alternating product over a grading
- Absorbs: L11-001, L11-004, L11-022, L13-104, L08-008
- Class: LEAD-unpursued
- Raised by: papers (Deninger, Deitmar, Kang--Yu, Dyatlov--Zworski, Knill, Matsuura--Ohta), assembled by the extractor and the orchestrator
- What: Four instances of one shape in four different categories: `prod_{i=0}^2 (...)^{(-1)^{i+1}}` (arithmetic schemes), `prod_l Z_{sigma_l}(s + l|alpha|)^{(-1)^l}` (locally symmetric spaces), `prod_k Z_k^eps(X,u)^{(-1)^{k+1}}` (Bruhat--Tits buildings), `zeta_R = zeta_1/(zeta_0 zeta_2)` (Anosov flows). Deitmar proves that the geometric zeta of a locally symmetric space is a regularised determinant of `H + s` on the **virtual space** `⊕_p (-1)^p V_p`, and names the analogy himself: "a determinant formula similar to the determinant formula of Deligne expressing the Hasse--Weil zeta function as an alternating product of determinants of the Frobenius-action on étale cohomology". Dyatlov--Zworski give the cleanest instance of the picture the notebook wants: 1-forms (odd) in the numerator, 0- and 2-forms (even) in the denominator, so `m_R(0) = -chi(Sigma)`, the **even sectors contributing exactly 1 each (a one-dimensional vacuum) and the odd sector contributing `b_1`**. The notebook's own comparison is deliberately restricted: the parallel is "alternating determinant structure" only --- `sum (-1)^i Tr` is not `sum i(-1)^i dim`, and neither formula imports into the other. Four literatures compute the same shape and do not cite each other.
- Lead: **state the shape once, abstractly (a zeta as an alternating product over a grading), and ask what the notebook's category contributes as a fifth instance.** If the notebook can name the grading for channels, the analogy becomes a definition. Concretely: write the Riemann channel's zeta as `det(H+s | ⊕_p (-1)^p V_p)`, and use the Dyatlov--Zworski shape as the target --- a one-dimensional even sector (the fixed point / Perron eigenvalue) and an odd sector carrying the zeros, so that RH becomes a statement about the odd sector alone.
- Where: notes/extract/cohomological-zeta-sources.md:57-171, :172-284, :1650-1678; report/sections/08d_complex_zeta.tex:148-205; notes/complex-zeta/astra-proofs.md:466-475

### G2-T13-2 The divisor is the degree-weighted Euler number, not the plain supertrace
- Absorbs: L11-002, L11-013
- Class: EXPLORED-registered (a warning)
- Raised by: extractor, on Deitmar's vanishing-order theorem and Shen's torsion
- What: Deitmar's order of vanishing is `chi_1 = -sum_p p(-1)^p dim H^p`, the **higher** Euler number, and the quoted theorem's last sentence says the *ordinary* alternating sum `chi = sum_p (-1)^p dim H^p` **vanishes identically**. A naive supertrace bookkeeping would give zero. The same weight appears in analytic torsion, which is literally a supertrace of the form-degree **number operator**: `theta(s) = -Str[N^{Lambda(T^*Z)}(□^Z)^{-s}]`, `T(F) = exp(theta'(0)/2) = prod_i det(□|Omega^i)^{(-1)^i i/2}` --- and Milnor is credited with first noticing "a remarkable similarity between the Reidemeister torsion and the Weil zeta function". Deitmar's `chi_1`, Knill's `A(G)` and Shen's `theta(s)` are the same weighted supertrace.
- Lead: **whatever supertrace the notebook writes must carry the degree weight `p` (a number operator), not just the sign `(-1)^p`** --- otherwise the alternating count is identically zero and says nothing. Check that the three weights coincide. Note also that the degree-weighted insertion is precisely the one that makes the plain Euler sum vanish, which is what a numerator-carrying zeta would want; nobody asked what a degree-weighted flow supertrace would be on a complex.
- Where: notes/extract/cohomological-zeta-sources.md:118-146, :931-1005

### G2-T13-3 The alternating count is not perturbation-stable
- Absorbs: L11-006
- Class: EXPLORED-negative (a warning)
- Raised by: paper (Cekic--Delarue--Dyatlov--Paternain) + extractor
- What: In dimension 3 (5-dimensional sphere bundle) `m_R(0) = 4 - 2b_1` at the hyperbolic point but `4 - b_1` after a generic conformal perturbation --- the degree-1 contribution halves and the alternating sum jumps. "'The zeros are the odd cohomology' is a statement that can hold at a symmetric point and fail under perturbation, so any graded/supertrace realisation must be pinned by more than the alternating count."
- Lead: any notebook claim of that form needs a rigidity/stability argument, not just a degree count; otherwise it can be true at one channel and false at a nearby one.
- Where: notes/extract/cohomological-zeta-sources.md:391-492

### G2-T13-4 The special value is a torsion --- and the `L^2` route is blocked
- Absorbs: L11-005, L11-009, L11-010, L11-003
- Class: LEAD-unpursued
- Raised by: papers (Dang--Guillarmou--Rivière--Shen; Shen; Fried; Zhuang; Deitmar recording Moscovici--Stanton)
- What: `|zeta_{X,rho}(0)^{(-1)^{n_0}}| = tau_rho(M)`, the Ray--Singer/Reidemeister torsion, for acyclic unitary `rho`; Fried himself read this as "an analogue of the Lefschetz fixed point formula", and Shen proves the conjecture for all odd-dimensional closed locally symmetric reductive manifolds. A graph zeta that *is* a Reidemeister torsion already exists via knot diagrams: the twisted Alexander polynomial is a torsion of a knot exterior and is written as an Ihara-type zeta counting cycles on a knot diagram. But the `L^2` upgrade is blocked --- Zhuang states plainly: "We cannot get a zeta function formula like the twisted Alexander case since, unlike the determinant, there is no direct relationship between the `L^2`-torsion of a matrix and its entries." Historical pointer never followed: Deitmar records that the higher-rank case "seemed impenetrable until H. Moscovici and R. Stanton used supersymmetry arguments to compute traces of certain linear combinations of heat operators", which gave continuation of the Ruelle zeta for `SL_3(R)` and `SO(p,q)` with `pq` odd --- and Moscovici--Stanton itself was never fetched.
- Lead: identify the notebook's analogue of "the special value" (`u=1` for graphs, `s=0` here) and ask what torsion it computes for a Kraus channel --- if it is a torsion, the graded structure is *forced* rather than assumed. Also: see whether the knot-diagram construction runs with operator weights (a quantum twisted-Alexander/torsion); and fetch Moscovici--Stanton, whose supersymmetric heat-trace combination may be the closest existing template for a supersymmetric proof. Record the `L^2`/Fuglede--Kadison obstruction so nobody reaches for von Neumann determinants.
- Where: notes/extract/cohomological-zeta-sources.md:285-390, :742-770, :753-757, :147-159

### G2-T13-5 Knill's super pseudodeterminant never meets the Ihara zeta --- the unclaimed join
- Absorbs: L11-012, L11-021, L11-029, L08-009
- Class: LEAD-unpursued
- Raised by: extractor's negative searches; prover's refutation of a naive identification
- What: Knill proves `A(G) = prod_k Det(L_k)^{k(-1)^{k+1}} = SDet(D) = prod_k Det(D_k)^{(-1)^k}` and calls it, in his own words, the "**Fermionic**" version of the orientation-oblivious "**Bosonic**" pseudo-determinant; the combinatorial content is a generalised matrix-tree theorem, torsion = (rooted spanning trees on even simplices)/(rooted spanning trees on odd simplices), recovering Kirchhoff on triangle-free graphs. The extract calls it "the single most on-target source for the notebook's zeta = supertrace picture on the discrete side" --- and **Knill never mentions the Ihara zeta** (verified by grep). No source proves the Ihara/Hashimoto determinant identity by an explicit **supertrace** argument with a parity operator. And the tempting identification of `SDet` with the `u -> 1` limit of the trivial factor is false: on one edge the Ihara zeta is 1, Knill's squared torsion is 2, and `lim (1-u^2)^chi = 0` --- three different numbers. There is also no graph-literature statement that `(1-u^2)^chi` "is a Reidemeister torsion"; the nearest are Hoffman (cited second-hand) and Kang--Yu's derivation.
- Lead: **prove `Z_X(u)^{-1} = SDet(...)` for a finite graph.** The join is exactly "zeta is a supertrace" on a graph; it would be a publishable standalone result and would justify the notebook's central metaphor. Write the sentence "`(1-u^2)^chi` is a Reidemeister torsion" as a theorem. And note the one place a genuinely combinatorial "fermionic over bosonic" count appears --- the even/odd rooted-spanning-tree ratio --- which has never been given a transfer-operator reading.
- Where: notes/extract/cohomological-zeta-sources.md:866-930, :1624-1649, :1830-1836; notes/complex-zeta/astra-proofs.md:213-226

### G2-T13-6 The fermionic proof of Bass already exists: gamma-five, Witten index, sign-reversing involutions, `OSP(1|2)`
- Absorbs: L11-016, L11-017, L11-018, L11-019, L08-010
- Class: LEAD-unpursued
- Raised by: papers (Matsuura--Ohta; Foata--Zeilberger; Caracciolo--Sokal--Sportiello; Abdesselam)
- What: Matsuura--Ohta put a Grassmann field on vertices and two per oriented edge; the Berezin integral gives `det(D̸ + M)`, and two Schur decompositions give `(1-t^2)^{n_E - n_V} det Delta_{q,u}` (Ihara/Bass) and `det(I - qB_u)` (Hashimoto), whose equality **is** Bass's identity in Bartholdi-deformed form. `(1-t^2)^{-chi}` arises as `det(I_{n_E} - tJ) = (1-t^2)^{n_E}`, a fermionic determinant of the edge-reversal involution `J`, and the exponent `n_E - n_V` is the difference of the dimensions of the two blocks of a chiral, block-off-diagonal Dirac operator. The parity is **structural, not a sign in the measure**: all of `xi, psi, tilde psi` are ordinary Grassmann variables in the same Berezin measure, and the `Z_2` structure is that `D̸` is block off-diagonal with gamma-five hermiticity; the authors call the cycle-expansion signs "like the Witten index" and note that gamma-five hermiticity "allows us to construct the overlap fermion on the graph". The notebook's correction: the exponent `f_1 - f_0` is a reversal-pair count minus a vertex-denominator count, **not** `dim H_1 - dim H_0 = 2f_1 - f_0`. Combinatorially the same cancellation is Foata--Zeilberger's involution `pi -> pi'` with `deg pi + deg pi' = 0 mod 2` --- "the same cancellation that a Berezin integral performs automatically". And on the spanning-tree side, unrooted spanning forests are generated by a non-Gaussian Grassmann theory with an honest `OSP(1|2)` supersymmetry, mapping to the `N`-vector model at `N = -1` / the `sigma`-model on the unit supersphere in `R^{1|2}`, perturbatively asymptotically free in two dimensions, with all-minors and Hyperpfaffian-cactus generalisations.
- Lead: **redo the notebook's quantum Ihara--Bass as a Berezin integral over a chiral Dirac operator**, so the `chi` exponent comes out as an *index* rather than a bookkeeping count; generalise the gamma-five structure to complexes (explicitly flagged as needing "a separate construction"). Three smaller unpursued leads: read the cycle Möbius signs as a Witten index for the channel; exploit gamma-five hermiticity / **overlap fermions**, a lattice-QCD technology never applied to a zeta, which would give an exact chiral symmetry on the discrete side; and look for a sign-reversing involution on words in the `A_k, A_k^†`, which would give a weight-free combinatorial proof of the quantum identity. The extract also records the exact hole in the supersymmetry literature: "**not found: a paper joining the two into a single supersymmetric statement about `(1-u^2)^chi`**".
- Where: notes/extract/cohomological-zeta-sources.md:1227-1365, :1316-1352, :1366-1426, :1427-1541

### G2-T13-7 The `chi` exponent has three independent origin stories --- and an off-by-one
- Absorbs: L11-014, L11-007, L11-008, L11-051, L11-045, L11-046
- Class: PARTIAL
- Raised by: papers (Kang--Yu; Hoffman via Kang--Yu; Kang--Li--Wang; Deitmar--Kang) + extractor
- What: (i) **Torsion**: `prod_i det(Phi_i|C_i)^{(-1)^i} = prod_i det(Phi_i|H^i)^{(-1)^i} = (1-u^n)^{sum(-1)^i(i+1)V_i}`, giving `(1-u^n)^{chi(X)}`; for `n=2` this is exactly Ihara, so the numerator `(1-u^2)^chi` of the graph zeta **is** the determinant of a cochain automorphism over the whole (vertex, edge) complex. Kang--Yu say their proof "is inspired instead by Hoffman's reformulation of Bass's proof of the Ihara identity in terms of torsion of complexes". (ii) **Index**: the Matsuura--Ohta chiral-block difference. (iii) **Representation theory**: in Kang--Li--Wang's factor-by-factor bookkeeping over five types of unitary Iwahori-spherical representations, "the Steinberg multiplicity is what produces the Euler-characteristic exponent" --- the total number of Steinberg representations, with multiplicity, equals `3chi(X_Gamma) - 3`. Supporting bookkeeping: in `Z_X(u)^{-1} = (1-u^2)^{-chi} h_X(u)` both factors vanish at `u=1`, and the **tree number** sits in `h'_X(1) = -2chi(X)kappa(X)` (Kirchhoff), i.e. in the Laplacian/Hecke factor, while `(1-u^2)^chi` is the bookkeeping factor whose job is to cancel that zero. External justification for a negative exponent: Deitmar--Kang take Euler factors with a **positive** exponent against Ihara's convention and say "there is a deep reason for the sign in Selberg's paper ... It emerges that the exponent prescribed by the trace formula is an **Euler number**, in Selberg's original case the Euler number of a point". Warning: their own RH theorem gives `Z_{2,+}(-u)/Z_{1,+}(u^2) = (1-u^3)^{chi-1}P_1(u)/[(1-q^3u^3)P_2(u)]` --- the exponent is `chi − 1`, **not** `chi` --- and for a Ramanujan complex `P_1` has degree `N_1 - 3N_0 + 6`.
- Lead: **reconcile the three origin stories** --- it would be informative in itself, and it is the only way to know whether the `chi` exponent is universal. First reconcile the off-by-one: an unexplained `chi - 1` would break any universal supertrace bookkeeping. Concrete steps: run the Euler--Poincaré argument with the notebook's Kraus-weighted successor operators to get the quantum `chi` as a torsion; obtain Hoffman's paper (not on arXiv) and redo the quantum Ihara--Bass as a torsion computation rather than a Schur complement; and compute the analogue of `h'(1)` for the quantum Ihara zeta, asking what "the number of spanning trees" becomes for a Kraus family. Adopt the Deitmar--Kang convention and cite their sentence.
- Where: notes/extract/cohomological-zeta-sources.md:1008-1122, :566-697, :698-741; notes/extract/complex-zeta-sources.md:275-282, :1175-1240, :1218-1240

### G2-T13-8 A `±1` sign carried by the orbit rather than by the coefficient space
- Absorbs: L11-011
- Class: LEAD-unpursued
- Raised by: paper (Benard--Chaubet--Dang--Schick) + extractor, called "the strongest evidence that the graded picture survives discretisation"
- What: The combinatorial zeta `zeta_T(z) = prod_gamma (1 - eps_gamma z^{|gamma|})` weights each primitive closed geodesic in the `(n-1)`-skeleton by a **reversing index** `eps_gamma in {-1,1}`, the parity of how often orientations flip along the orbit --- "a `Z_2`-grading carried by the orbit, not by the coefficient space". The vanishing order at `z = (n+2)^{-1}` is `b_1(M)`.
- Lead: try a **per-orbit sign** in the notebook's Euler product (a sign on each cyclically non-backtracking word) instead of a graded bond space. If it reproduces the same divisor, the grading may be cheaper than a fermionic bond.
- Where: notes/extract/cohomological-zeta-sources.md:771-865

### G2-T13-9 Non-arXiv originals named but never obtained
- Absorbs: L11-030, L11-055, L08-053
- Class: LEAD-unpursued
- Raised by: extractor and orchestrator bibliographic bookkeeping
- What: None of D. Fried's five papers is on arXiv; Juhl's *Cohomological Theory of Dynamical Zeta Functions* (Progress in Math. 194) is not, and Deitmar credits Juhl's rank-one method as "the central idea" of his own higher-rank argument; Hashimoto 1989/90 ("the origin of the non-backtracking operator and of the bipartite factorisation used by Storm"), Bass 1992, Ihara 1966, Northshield 1998/1999, W.-C. W. Li's *Ramanujan hypergraphs*, Cartwright--Solé--Żuk, Cartwright--Steger (the source of the lattice used by LSV), Sunada 1986 (cited as the origin of the representation-twisted zeta), Stark--Terras I--III and Terras's book are all cited only second-hand. This violates the notebook's own "prefer TeX sources" rule: a byte-verified provenance for the twisted zeta is still missing.
- Lead: **Juhl's book is the single most relevant unread source** for "a cohomological theory of dynamical zeta functions"; Hashimoto 1989 is the second (everything on the bipartite/edge side descends from it). Both are concrete acquisition steps.
- Where: notes/extract/cohomological-zeta-sources.md:495-565, :1805-1845; notes/extract/complex-zeta-sources.md:1489-1498; notes/prior-art-quantum-ihara.md:124-131

### G2-T14-1 Deninger's grading is the notebook's `Z_2` grading
- Absorbs: L11-079, L11-080, L11-081, L11-092
- Class: LEAD-unpursued
- Raised by: paper (Deninger), called by the extractor "**the** citation for the notebook's `Z_2`-grading"
- What: `hat zeta_K(s) = prod_{i=0}^2 det_infty((s-Theta)/2pi | H^i_dyn)^{(-1)^{i+1}}`, with `H^0 = R` and `Theta = 0`, `H^1` infinite-dimensional **with spectrum the nontrivial zeros**, `H^2 ≅ R` with `Theta = id`, and `H^i = 0` for `i > 2`. The Lefschetz form is `sum_i (-1)^i Tr(phi^*|H^i) = 1 - sum_rho e^{t rho} + e^t` --- "the supertrace with the zeros entering with a minus sign" --- and the dictionary pairs finite places with closed orbits of length `log Np`. The generator `theta = lim_{t->0}(phi^{t*} - id)/t` on leafwise cohomology "plays a similar role as the Frobenius morphism on étale or crystalline cohomology"; the Ruelle zeta is `prod_i det_infty(s·id - theta | H^i_F(X))^{(-1)^{i+1}}` with `eps_gamma = sgn det(1 - T_x phi^{l(gamma)})`; and one dictionary line reads "Explicit formulas of analytic number theory ↔ transversal index theorem for `R`-action ... and Laplacian along the leaves". The programme is live, not a 1998 analogy: Deninger records that the conditions for periodic orbits to correspond to primes "were written down a long time ago ... but for too many years I had no idea how to construct natural `Q^{>0}`-spaces realizing these conditions", and the 2018 paper is where he does. Citation spine fixed: Deninger's Lefschetz equation, Connes's `⊖H` passage, and the fMPS supertrace + parity-insertion equations.
- Lead: **make the identification precise** --- the `Z_2`-grading of the notebook's operator is exactly Deninger's `(-1)^i`. Then read the 2018 construction and ask whether the constructed space admits a transfer-semigroup / channel description; that would be a direct bridge to side B. The "transversal index theorem" line is an unexplored suggestion for what the explicit formula becomes, and the notebook's Lindbladian generator is the natural candidate for `theta`.
- Where: notes/extract/riemann-cmps-sources.md:76-200, :181-199, :201-226, :1097-1107

### G2-T14-2 Connes: the Polya--Hilbert space appears from its negative
- Absorbs: L11-082
- Class: LEAD-unpursued
- Raised by: paper (Connes), called "the citation for 'the zeros are odd'"
- What: Connes identifies two mismatches with the Selberg trace formula, the first being "the overall **minus sign**", and resolves it: the analogue of the Polya--Hilbert space is `H^1_et`, which appears with a minus in the Lefschetz formula. Hence "(C) The Polya--Hilbert space `H` should appear from its negative `⊖H`" --- an **absorption** spectrum, not an emission spectrum. He adds that Berry--Keating's count is off precisely because of this.
- Lead: seek the notebook's transfer operator as a *negative* / odd sector. Concretely: look for the zeros as **missing lines in a continuum**, not as eigenvalues of a positive object.
- Where: notes/extract/riemann-cmps-sources.md:273-360

### G2-T14-3 The fermionic cMPS construction is not new --- only the arithmetic reading could be
- Absorbs: L11-084, L11-085, L11-094
- Class: EXPLORED-registered (a novelty downgrade)
- Raised by: extractor, on Bultinck et al., Verstraete--Cirac, Haegeman--Cirac--Osborne--Verstraete
- What: The graded contraction gives `C(|i> ⊗_g <j|) = (-1)^{|i|} delta_{ij}` --- "the famous supertrace"; to obtain the *normal* trace one must insert the fermion parity operator. Even-parity fMPS on a ring have coefficients `tr(P A^{i_1}...A^{i_N})` with the parity matrix `P`; odd-parity ones need an extra odd tensor `Y`. These are the two simple `Z_2`-graded algebras, with Majorana edge modes in the odd case (the Kitaev chain has `A^1 = Y`). The cMPS transfer operator `T = Q⊗1 + 1⊗conj Q + sum R_alpha ⊗ conj R_alpha` is a Lindbladian after gauge fixing, and the fermionic case is already in the literature with the **same** `Z_2`-graded bond structure: `P` diagonal, `Q` block diagonal, fermionic `R_alpha` block off-diagonal, `B` block-diagonal (even) or block-off-diagonal (odd), and `P T P = T`. Verdict: "The notebook's graded bond with a supertrace in PBC is therefore **not** new as a tensor-network construction; what is proposed as new is the arithmetic reading of it." Standing terminological guard: the entanglement Hamiltonian is `-log rho_A` and is Hermitian by construction, while the operator whose spectrum is supposed to contain the zeros is the **non-Hermitian transfer generator** --- the two must not be conflated.
- Lead: stop claiming the construction and claim only the reading; reuse the existing fermionic-cMPS calculus (it already has the `l_alpha = lP`, `r_alpha = Pr` eigenvector relations) rather than rebuilding it. Open choice: pick one of the two graded algebras (even `P`, odd `Y`) as the bond structure of the Riemann cMPS and see which reproduces the Deninger grading.
- Where: notes/extract/riemann-cmps-sources.md:387-512, :513-632, :625-632; notes/extract/notation-and-definitions.md:291

### G2-T14-4 Bost--Connes, and the open identification with the Phantasm constructions
- Absorbs: L11-091, L11-057, L11-058
- Class: LEAD-unpursued
- Raised by: paper (Bost--Connes via Connes--Marcolli) and the notebook's own open list
- What: Unique `KMS_beta` state for `0 < beta <= 1`; for `beta > 1` extreme states parameterised by embeddings `Q^ab -> C` with partition function `zeta(beta)`; at `beta = infinity` the Galois action factors through the abelianisation and class field theory intertwines. The dictionary table pairs "system at critical temperature (Riemann's `zeta` as partition function)" with "spectral realization (zeros of `zeta` as absorption spectrum)" and types `III_1 ↔ II_infty` --- with the honesty caveat that Connes--Marcolli label the system `III_1` in a table without proving or restating it there. Two of the notebook's own open items sit here: whether a **Holevo-form (jump-type) generator on `K_S` with jumps at the prime lengths `k log p`** reproduces the Lax--Phillips semigroup `Z(t)` (if it did, its physical index would be the Stinespring environment --- the primes would literally be the environment of a dilation); and the fact that the Phantasm constructions SP-PRIME and SP-BC-CONTROL are `beta > 1` objects whereas the Riemann-channel construction is a `beta = 1` phase compressed to a co-invariant subspace, with no identification made.
- Lead: construct the jump generator and compare its semigroup to `Z(t)` (HANDOFF suggests running it as a blind codex lane); and settle whether the `beta = 1` compression can be obtained as a limit of the `beta > 1` constructions. The `III_1 ↔ II_infty` type change across the critical temperature is a structural fact the notebook has never used --- it is a precise statement of what "compressing to a co-invariant subspace" costs.
- Where: notes/extract/riemann-cmps-sources.md:1018-1096; notes/extract/notation-and-definitions.md:286, :288

### G2-T15-1 The window is an exact compression; the implicit model of the higher traces is Pisarenko's
- Absorbs: L13-129, L13-130
- Class: EXPLORED-registered
- Raised by: TJO (2026-09-19), answered by the orchestrator
- What: TJO asked whether the Connes--Consani--Moscovici construction --- which seems to (1) assume a form for the traces, (2) collect data up to some lag, (3) model the higher traces, (4) read information off the minimal eigenvector by positivity and Toeplitz structure --- could be improved by a cleverer estimator of `Tr X^l` for `l > K`. First answer: in the CCM chain and its graph analogue the window quadratic form is the **exact** restriction of the full Weil form to test functions supported in the window --- no value is assigned to the traces beyond it. The perturbed operator's spectrum is exactly the roots of the kernel polynomial of `W_K - eps_K`, so the only model committed to is the **Pisarenko extension**: `K` atoms on the circle plus a white-noise floor `eps_K` at lag zero. "This is the minimal-support extension of the data, and it is the appropriate prior exactly because the true spectral measure is pure point."
- Lead: none further --- it identifies what the chain is implicitly assuming.
- Where: report/sections/08g_weil_window_extension.tex:12-22, :51-67

### G2-T15-2 The admissible next trace fills a disc, and nothing beats it
- Absorbs: L13-131
- Class: PARTIAL
- Raised by: orchestrator
- What: The admissible set for `nu_{K+1}` is a closed disc whose centre is the Levinson one-step predictor and whose radius is `det W_K / det W_{K-1}`, non-increasing in `K`; boundary points are exactly the singular windows with `K+1` atoms on the circle (Caratheodory--Fejer). If the retained measure has exactly `K+1` distinct atoms the true value lies on the boundary and every later trace is determined by the kernel recurrence. **No estimator of `nu_{K+1}` from `nu_0, ..., nu_K` and positivity alone can do better than the disc**; the centre is the minimax choice and the maximum-entropy (Burg) extension.
- Lead: the algebra is checked numerically to `1e-9` rather than carried out; completing it would raise the status above sketched.
- Where: report/sections/08g_weil_window_extension.tex:83-132

### G2-T15-3 Integrality adds information positivity cannot see --- but rescaling defeats it
- Absorbs: L13-132, L13-133
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: For an integer matrix `X` with `N_k = Tr X^k`, `N_{K+1} ≡ -sum_{i=1}^K c_i N_{K+1-i} (mod K+1)`: the traces up to lag `K` determine the next trace **modulo `K+1`**. Combined with the disc and with `N_{K+1} >= 0`, this can pin the next trace early --- for the permutation `(1 2)(3 4 5)` the three constraints pin it at `K=3`, one lag *before* the critical window. But for a `(q+1)`-regular graph the disc lives in the rescaled variable and has radius `q^{(K+1)/2} r_K` in count units, which exceeds one on every positive-definite window of the Petersen graph (35.5, 40.6, 49.4 at `K = 1,2,3`), "so integrality pins nothing; only the Ramanujan-side information (positivity) and the exact critical window remain".
- Lead: the arithmetic bonus is lost exactly when the critical radius is not 1 --- i.e. always in the interesting cases.
- Where: report/sections/08g_weil_window_extension.tex:139-152, :154-166

### G2-T15-4 For `zeta`, a better higher-trace estimator means more primes
- Absorbs: L13-134
- Class: EXPLORED-negative
- Raised by: orchestrator (explicitly "an argument, not a theorem")
- What: For `zeta` the traces are `Lambda(n)`. The *mean* of the traces beyond the window is the prime number theorem, which is exactly the pole term of the explicit formula and already enters the window form exactly; the higher powers `p^m > lambda^2` of known primes lie outside the support and are invisible; what is unknown beyond the window is the fluctuation `Lambda(n) - 1`, which by the explicit formula **is** the zeros. "A better estimator of the higher traces of `zeta` therefore means more primes, i.e. a larger window." The remaining freedom is the choice of extremal extension, and the content of Connes--Consani--Moscovici is the rate at which the Pisarenko atoms converge (about 5.4 digits per unit of `lambda^2`).
- Lead: this is the answer to TJO's question and it is negative in the cleanest way --- the estimator question is circular for `zeta`.
- Where: report/sections/08g_weil_window_extension.tex:166-177

### G2-T15-5 Two cheap computations proposed and not run
- Absorbs: L13-135
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: (a) In the `ihz` sidequest the disc radius `r_K` is one determinant ratio per window; combined with the congruence and nonnegativity it would show how far below the critical window a graph divisor is already forced. (b) For `zst`, the analogous quantity --- the Schur-complement radius of the window Loewner form as `lambda` grows --- "would bound rigorously what the primes beyond `lambda^2` can do to the form; comparing its decay in `lambda` with the observed `e^{-4pi lambda^2}` convergence of the first zero would say whether that convergence is explained by the shrinking envelope or by something specific to the arithmetic."
- Lead: exactly as stated; both are cheap and outstanding. **(b) is the more interesting: it would distinguish a generic approximation-theoretic effect from genuine arithmetic** --- a decisive experiment.
- Where: report/sections/08g_weil_window_extension.tex:198-207

### G2-T16-1 TJO's Lindblad question, and why the prime-circle picture cannot produce zeros
- Absorbs: L13-143, L13-144
- Class: EXPLORED-negative
- Raised by: TJO; answered by the prover
- What: TJO asked to replace channels by Lindblad generators: the simplest continuous instance is the generator of rotations on a circle of circumference `log p`, whose trace is a Poisson comb at multiples of `log p`, and the Selberg analogue should be a Lindbladian built from the vector fields on `PSL_2(R)` with the Laplacian as the small operator. Result for the naive construction: the direct sum over primes of circles gives the comb `sum_n Lambda(n) delta(t - log n)` as a *locally summed component trace*, but the smeared direct-sum operator is **never trace class** (the constant modes give a nonzero eigenvalue of infinite multiplicity) and the positive prime comb is not tempered; finite sets of primes see only Euler poles and **no zeros at all**. "**The missing ingredient is transverse expansion: a circle has no Poincaré map, so no Jacobian, so no resonances.**"
- Lead: the sharpest diagnosis in the group of why the naive "primes as circles" picture cannot produce zeros. **Any Phantasm needs a transverse direction.**
- Where: report/sections/09b_selberg_dictionary.tex:12-23, :161-186

### G2-T16-2 The Lindbladian of the `sl_2` vector fields is the Casimir --- but not a diffusion
- Absorbs: L13-145, L13-146, L11-104
- Class: PARTIAL
- Raised by: prover
- What: For real vector fields acting as derivations with jumps `L_j = -iX_j`, the dissipator on multiplication observables is `M_{(1/2) sum_j X_j^2 f}`. On the `K`-invariant sector `(1/2)(H^2 + E^2) = 2 Cas = -2 Delta`. But on all functions `(1/2)(H^2+E^2) = 2 Cas + (1/2)W^2`: **"the Casimir carries the compact direction with a minus sign and is not a diffusion Lindbladian on all of `L^2(Gamma\G)`"**; the two-jump Lindbladian preserves the `K`-invariant sector and equals `-2Delta` there. The continuous Harrow construction follows: for a unitary representation `pi` with `A_j = dpi(X_j)` and jumps `L_j = -iA_j`, the dissipator is `(1/2) sum_j B_j^2 rho` with `B_j rho = [A_j, rho]` the generators of `pi ⊗ conj pi` on Hilbert--Schmidt operators; for `sl_2` with the two non-compact jumps it is `2 Cas_{pi ⊗ conj pi} + (1/2)B_W^2`. "A channel from a representation becomes a Lindbladian from a representation, and its gap is a question about `pi ⊗ conj pi`." Bookkeeping gap on the geometry side: the statement "on right-`K`-invariant functions the Casimir equals `y^2(∂_x^2 + ∂_y^2)`" is *assembled* from two equations plus `∂_theta = e - f`; no source states the one-line reduction as a displayed sentence (the standard reference, Bump §2.2, is not on arXiv).
- Lead: the drift matters --- "squaring the projected tangent vectors alone would miss the drift and give the wrong operator". Extending beyond the `K`-invariant sector is unresolved. Derive the Casimir reduction in the lab book or acquire Bump §2.2.
- Where: report/sections/09b_selberg_dictionary.tex:188-218, :220-234; notes/extract/selberg-sources.md:302-306

### G2-T16-3 The gap conjecture for the representation Lindbladian
- Absorbs: L13-148, L13-149
- Class: LEAD-unpursued
- Raised by: orchestrator (registered open)
- What: For an irreducible unitary `pi` of `SL_2(R)`, or of `SL_2(F_p)`, the two-jump Lindbladian `2 Cas_{pi ⊗ conj pi} + (1/2)B_W^2` has a spectral gap governed by the decomposition of `pi ⊗ conj pi`; **for the Weil representation this is the continuous shadow of the Weil--LPS channels.** The smallest datum: for the three-dimensional `sl_2` irrep the Lindbladian spectrum is `{0, -4^{x3}, -12^{x5}} = -2j(j+1)`, so the gap is explicitly 4, and the quantum tensor identity holds to `7e-15`. Scaling in `dim pi` was not attempted.
- Lead: **compute the decomposition of `pi ⊗ conj pi` for the Weil representation and read off the gap.** That would give a continuous-time Ramanujan object matching the finite Weil--LPS model --- the dilation-time version of the finite model.
- Where: report/sections/09b_selberg_dictionary.tex:236-244; report/sections/09c_selberg_tower_cusp.tex:102-120

### G2-T16-4 The flat trace, the tower, and continuous Ramanujan as Selberg's 1/4
- Absorbs: L13-150, L13-151, L11-096, L11-099, L11-097
- Class: EXPLORED-registered
- Raised by: prover (correcting an orchestrator draft); conventions pinned from Dyatlov--Zworski and Dyatlov--Faure--Guillarmou
- What: The flat trace is `sum_gamma sum_k l_gamma e^{-lambda k l_gamma}/(4 sinh^2(k l_gamma/2))`, and the tower `D(lambda) = prod_{j>=1} Z_S(lambda + j)` converges absolutely without zeros, with **flat trace = +D'/D** (the sign was drafted as a minus and is a plus; and the graph counterpart of the tower is `det(1-uH)`, not the zeta). The tower comes from `1/(4 sinh^2(x/2)) = sum_m (m+1)e^{-(m+1)x}`: "**the Jacobian of the two transverse directions is what a graph does not have.**" The tower is entire with zeros at `lambda = -1/2 - k ± i r_j` and at `-N` with order `(2g-2)N^2 + 2`; the nonconstant first band is exactly the pole multiset in `-1 < Re lambda < 0`, and it lies on `Re = -1/2` iff every `r_j` (`j >= 1`) is real iff `Delta` has no eigenvalue in `(0, 1/4)`. **The constant mode must be removed, exactly as the constant adjacency mode is removed in the Ramanujan condition of a graph.** Supporting conventions from the literature: Guillemin's flat trace formula `tr^♭ e^{-itP}|_{C^∞(X;E^k_0)} = sum_gamma T_gamma^# tr(Λ^k P_gamma) delta(t - T_gamma)/|det(I - P_gamma)|`, with `P = -iV`, the sum over **all** orbits including repetitions, `P_gamma = dphi_{-T_gamma}` at negative time so `|mu| < 1` on `E_u`; and `zeta_S(s) = prod_gamma prod_{m>=0}(1 - e^{-(m+s)l_gamma})` with `zeta_R(s) = zeta_S(s)/zeta_S(s+1)` (attributed to Marklof, both products over primitive lengths, `m` the band index). Ruelle resonances come in **bands**: for a compact hyperbolic surface the resonances in `C \ (-1 - N_0/2)` are `lambda_{j,m} = -m - 1 + s_j`, one band per `m`, all translates of the Laplace spectrum.
- Lead: the `Λ^k` weight is the continuous form of the notebook's grading and the conversion is spelled out, so the formula can be transplanted directly. Two unused structures: the ratio-of-shifts `zeta_S(s)/zeta_S(s+1)` is the continuous analogue of the `mu mu' = q` pairing, and the shift `s -> s+1` is what the notebook's grading would have to produce; and "one band per `m`" is a structure the notebook's channel spectrum has never been tested for --- if a quantum transfer generator has band structure, "uniform decay" splits per band. The proposition itself makes no claim about operator realisations, only about the poles of the continued flat trace (see G2-T16-7).
- Where: report/sections/09c_selberg_tower_cusp.tex:17-42, :44-62; notes/extract/selberg-sources.md:15-56, :60-87, :88-104

### G2-T16-5 The cusp is the prime comb; the primes enter only as the scattering term
- Absorbs: L13-152, L13-154, L11-102, L11-103
- Class: EXPLORED-registered
- Raised by: prover (the identity), orchestrator (the dictionary); supporting sources on the scattering determinant
- What: The continuous-spectrum multiplier of the modular surface decomposes as `C = -P + A` where `P(t) = sum_n (Lambda(n)/n)[delta(t - 2 log n) + delta(t + 2 log n)]` and `A` is an explicit archimedean background with `A(t) = 1/2 - 1/(4 sinh(|t|/2))` away from 0. **"The prime atoms are dips"**; and the constant `1/2` is the pole of `zeta` at 1 (the ordinary boundary value differs from the Abel boundary distribution by `pi delta_0`), *not* a digamma term. Numerically confirmed with a Gaussian window to `3e-8`, the ratio `-2G/sqrt(2pi)` matching to six digits. The dictionary's closing row is the structural point: the dictionary maps edge space to `Gamma\PSL_2(R)`, the Hashimoto operator to the geodesic generator, the adjacency matrix to the Casimir, Ihara--Bass to the tower, and Ramanujan to "no eigenvalue in `(0,1/4)`" --- but **the primes of `zeta` enter only through the cusp of the modular surface, as the scattering term, not as closed geodesics.** Supporting literature: `phi(s) = sqrt pi Gamma(s-1/2)/Gamma(s) · zeta(2s-1)/zeta(2s)`, normalised by `phi(s)phi(1-s) = 1`, with **`phi(1/2) = -1`**, and it *is* the `y^{1-s}` coefficient of the Eisenstein constant term `xi(2s-1)/xi(2s)`; the continuous-spectrum term is `C = -(1/4pi)∫(phi'/phi)(1/2+ir)h(r^2+1/4)dr + (K_0/4)h(1/4)` with `K_0 = tr Phi(1/2)`, sitting on the **spectral** side (in the cocompact case `phi ≡ 1` and `C` disappears), and Booker--Platt give a fully explicit `PSL(2,Z)` version in an arithmetic normalisation where the `phi'/phi` integral is already folded into a `Lambda(n)/n` sum.
- Lead: the geodesic side and the prime side of the Selberg picture are **disjoint**, a serious obstacle to reading `zeta` as a Selberg-type transfer spectrum. Two small unpursued hints: `phi(1/2) = -1` is a `-1` at the central point, precisely the kind of sign the grading is trying to explain (check whether it is the same sign); and the fold of `phi'/phi` into a `Lambda(n)/n` sum is the prime side literally reappearing inside the continuous spectral term --- a structural hint for the cusp/environment story never followed up.
- Where: report/sections/09c_selberg_tower_cusp.tex:76-100, :142-172; notes/extract/selberg-sources.md:223-252, :253-294

### G2-T16-6 Correction: the "damped Riemann channel trace" claim
- Absorbs: L13-153
- Class: DEAD
- Raised by: prover, correcting the previous session's wording
- What: The sentence "the cusp term of the modular trace formula is the trace of the Riemann channel damped at rate `1/4`" is corrected: what is proved is that the *prime measure* written in the Riemann-channel note, damped at rate `1/4`, is the *prime part* of the cusp distribution --- an equality of prime atomic measures after subtracting the archimedean background and choosing positive weights. "It is not an equality of the full cusp distribution with a semigroup trace, nor of operators or spectra, and it implies nothing about the Riemann hypothesis." Also: **"the rate `1/4` is the uniform rate only under the Riemann hypothesis."**
- Lead: none --- an overclaim record.
- Where: report/sections/09c_selberg_tower_cusp.tex:122-138

### G2-T16-7 Open operator statements: continuous Ihara--Bass and a trace formula for `Z_t`
- Absorbs: L13-155, L13-156
- Class: LEAD-unpursued
- Raised by: orchestrator
- What: Four things are explicitly not established: a literal operator-theoretic compression from `Gamma\G` to the `K`-invariant sector turning the tower into a Laplacian determinant (its first-band operator form --- a quadratic intertwining through the fibre pushforward plus the horocyclic ladder --- is `prop:selberg-ladder-ihara` in the Selberg-letters shard, with the anisotropic-space realisation assumed there); a trace formula for the full compressed semigroup `Z_t` ("its own explicit formula has pole, archimedean and sign bookkeeping", and the full trace of `Z_t` is not established as a pure prime comb); any gap for the Lindbladian conjecture; and anything about RH or the `1/4` property of a given surface.
- Lead: write down the explicit formula for `Z_t` with all three bookkeeping terms. That is the prerequisite for any comparison with the Selberg trace formula and for the zeta-dictionary programme (G2-T8-6).
- Where: report/sections/09c_selberg_tower_cusp.tex:174-185, :135-138

### G2-T16-8 Assumptions and convention hazards in the Selberg lane
- Absorbs: L13-147, L11-100, L11-101, L11-098
- Class: PARTIAL
- Raised by: prover (assumptions), extractor (hazards)
- What: Six standard inputs are carried as `assumed` "because no local source quotes them in full": Fuchsian geometry; the Laplace spectrum of a compact hyperbolic surface; Selberg zeta entire with known divisor; closed realisations of flows and the heat semigroup; standard facts about `zeta` (including the `log^2` growth bound on `zeta'/zeta` near `Re = 1`); standard facts about `Gamma`. Three convention hazards. (i) The Poisson relation is only an **inclusion**, `Sing Supp Tr U(t) ⊂ Lsp(M,g)`, with "cancellations could take place if a length `L` is multiple"; the Selberg trace formula upgrades it to an equality for a compact hyperbolic surface, with `sqrt Delta` replaced by `sqrt(Delta - 1/4)` --- and the `-1/4` shift is **not** present in the general source. (ii) Laplacian sign conventions clash across sources: `Delta f_s = s(s-1) f_s` (the negative Laplacian, "the analyst-unfriendly one"), `Spec(Delta) = {s_j(1-s_j)}`, and `lambda_j = rho_j^2 + 1/4 >= 0` all appear in the same lane. (iii) The "band structure" and "Ruelle zeta = `Z(s)/Z(s+1)`" facts come from **different** papers, and the band-structure source never mentions Selberg or Ruelle zeta (verified: the string `zeta` does not occur in it).
- Lead: fetch quotable sources --- every claim depending on one prints `-conditional`. Fix **one** Laplacian sign convention before any Selberg computation, or risk an off-by-a-sign in the centring of the transfer spectrum (the same `-1/4` vs `-3/4` centring issue the Selberg-letters lane recorded). And do not put the two Dyatlov-school facts in one sentence without citing both papers.
- Where: report/sections/09b_selberg_dictionary.tex:28-84; notes/extract/selberg-sources.md:135-159, :161-222, :85-87, :296-306

### G2-T17-1 The prior-art verdict: no zeta has been attached to a quantum channel
- Absorbs: L13-136, L08-049, L11-072, L11-025
- Class: EXPLORED-registered
- Raised by: three literature agents, assembled by the orchestrator
- What: No source attaches a zeta function, or an analogue of RH, to a quantum channel; none states the poles-on-the-critical-circle iff Hastings-bound equivalence; none gives the MPS ring-norm reading or the identification of AKLT with `K_4`. Zero hits for any zeta/Ihara combined with channel, Kraus, CP-map or expander; Matsuura--Ohta contain none of the words Ramanujan, expander, Riemann hypothesis; Bordenave--Collins have the operator but no determinant and no zeta. What **is** known: (1) the `Ad(U)`-weighted Ihara--Bass formula (Matsuura--Ohta 2022; Watanabe--Fukumizu 2011 for loopless graphs; twisted zeta back to Sunada 1986 / Hashimoto 1989); (3) the trace formula / Artin--Ihara `L`-function reading; (4) the *mechanism* for exactly-Ramanujan channels from LPS (Harrow 2008 + LPS; Iyer--Jain--Jordan--Somma Feb 2026), but with no Weil-representation instance and no zeta; and the matrix-valued non-backtracking operator (Bordenave--Collins). Confirming the usage: the strongest explicit-Ramanujan-quantum-expander paper defines Ramanujan purely as `lambda <= 2 sqrt(D-1)/D` --- the Hastings/Alon--Boppana bound --- "and never a Riemann-hypothesis-for-a-zeta statement".
- Lead: present the RH-for-channels reading, the MPS/ring-norm dictionary and the Weil--LPS instance as this notebook's contribution. The spectral-gap half of "RH ⇔ Ramanujan channel" is free; only the zeta side is unclaimed.
- Where: report/sections/09_prior_art.tex:254-277; notes/prior-art-quantum-ihara.md:10,:22,:26; notes/extract/notation-and-definitions.md:344-348; notes/extract/cohomological-zeta-sources.md:1735-1772

### G2-T17-2 The search is metadata-only, so the absence claims are weak
- Absorbs: L13-137, L08-057
- Class: PARTIAL
- Raised by: orchestrator
- What: Ten arXiv metadata queries returned zero hits (listed verbatim in the shard: `"Ihara zeta" AND "quantum channel"`, `"zeta" AND "quantum expander"`, `"non-backtracking" AND "superoperator"`, `"AKLT" AND "zeta"`, ...), as did web/Scholar searches for "quantum Ihara zeta", Ihara zeta with noncommutative/quantum graphs (Weaver, Duan--Severini--Winter), Ihara zeta with MPS/tensor networks, and a MathOverflow search. **"arXiv search is metadata-only, so a formula inside a paper body would not surface, and the absence claims are weaker than its presence claims."**
- Lead: run a full-text search (Google Scholar full text, or a local full-text grep over the downloaded TeX in `refs/src`). The whole novelty claim rests on these negatives, so this is the obvious cheap insurance --- and it has never been done.
- Where: report/sections/09_prior_art.tex:279-293; notes/prior-art-quantum-ihara.md:135-137

### G2-T17-3 The object is not literally a Stark--Terras `L`-function
- Absorbs: L13-140, L08-054
- Class: EXPLORED-registered
- Raised by: orchestrator
- What: In Stark and Terras the representation is one of the Galois group of a covering of finite graphs, hence of a **finite** group, whereas `Ad(U_i)` for generic unitaries generates an **infinite** group. So the quantum Hashimoto object is not literally a Stark--Terras `L`-function, although the determinant formula is the same.
- Lead: the infinite-group case is exactly where the notebook's object departs from classical theory, and where the Artin-decomposition bookkeeping (`d_rho` versus `a_rho`, G2-T11-3) would have to be redone. Nobody asked what it becomes for an infinite image.
- Where: report/sections/09_prior_art.tex:237-243; notes/prior-art-quantum-ihara.md:113-122

### G2-T17-4 The quantum-walk line, and the unread open-quantum-random-walk extension
- Absorbs: L13-141, L08-055
- Class: LEAD-unpursued
- Raised by: a literature agent
- What: Konno and Komatsu--Konno--Sato build zetas from the **unitary evolution matrix of a quantum walk** (Grover walk) rather than from Kraus operators; the value of the line here is the Sunada pointer. One paper (arXiv:2104.10287) extends to **open quantum random walks on the torus by Fourier analysis** and was "not read in full".
- Lead: open quantum random walks are the closest published thing to a channel zeta, and this unread extension is the **single cheapest place where the "no quantum channel zeta exists" verdict could turn out to be wrong**. It is also the nearest neighbour to the notebook's own cMPS/Lindblad direction.
- Where: report/sections/09_prior_art.tex:245-249; notes/prior-art-quantum-ihara.md:105-111

### G2-T18-1 The Bost--Connes inverse problem, and the next target
- Absorbs: L08-058, L08-069
- Class: LEAD-unpursued
- Raised by: TJO; orchestrator's stated next step
- What: TJO asked for a Lindbladian with the BC state stationary, Galois symmetry and adelic symplectic structure. "The no-event generator and the jump map are both unknown. A fixed scattering generator with a chosen reset map is only one possible ansatz." The note does not construct the adelic bond, identify it with the scattering model, or prove RH; all its arguments are `sketched` and **unreviewed**. Its own stated next target: "an explicit representation or CP comparison map linking the finite phase/Weil data to a scattering bond, respecting the actual character action and the arithmetic boundary state. Only with that map can one impose the scattering odd-sector condition on the cone rather than fit an operator to known zeros."
- Lead: six named open sub-problems, each self-contained --- the `Gamma_0(N)` scattering/character calculation; prime powers; the real place; metaplectic compatibility; the critical operator-algebra limit; and identifying the standard BC time flow with the unknown cMPS transfer flow. Keep the methodological rule: build the map, don't fit an operator to known zeros.
- Where: notes/bc-symmetry-generators.md:3-9, :302-330

### G2-T18-2 The critical marginal is uniform and compatible, and has a unique Weil-invariant matrix extension
- Absorbs: L08-059, L08-062
- Class: PARTIAL
- Raised by: orchestrator
- What: `w_beta(0) = p^{-beta}`, `w_beta(x) = (1-p^{-beta})/(p-1)` for `x != 0`; at `beta = 1` the BC formula vanishes on every nontrivial finite-order phase at every level `N`, so the critical restriction is uniform on `Z/N` and the marginals are compatible under reduction, with diagonal extension `I/p`. Moreover the same residue probabilities have a **unique** Weil-invariant matrix extension `sigma_beta = aI + (r-a)P` with `r = p^{-beta}`, `a = (1-r)/(p-1)`, positive iff `beta >= log((p+1)/2)/log p`, parity-block eigenvalues `r` and `2a - r`; at criticality it is `I/p`, and full Weyl invariance forces `I/p`. This prevents a false no-go: failure of the *diagonal* extension to be symplectic-invariant does not exclude every extension. Noted: for `beta > 1` a symmetry-broken extremal state can belong to a stationary family, so uniqueness is the premise of the obstruction.
- Lead: compatibility under reduction is the hook for an adelic inverse-limit construction. "None of the coherent extensions has been identified with the full BC bond state" --- doing that identification is open.
- Where: notes/bc-symmetry-generators.md:40-64, :112-139

### G2-T18-3 No finite-dimensional representation of the full BC algebra retains the nontrivial phases
- Absorbs: L08-060
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: In finite dimension `mu_n^* mu_n = I` makes `mu_n` unitary, and `I = mu_n mu_n^* = (1/n) sum_k e(k/n)` is the spectral projection onto eigenvalue 1 of `e(1/n)`, so `e(1/n) = I` for every `n`. The critical phase state has `phi(e(1/n)) = 0` for `n > 1` and cannot be realised. "This excludes an exact finite representation, not finite restrictions, CP compressions, or asymptotic approximations."
- Lead: the three escape hatches are named in the last sentence and **none has been tried**: finite restrictions, CP compressions, asymptotic approximations.
- Where: notes/bc-symmetry-generators.md:66-80

### G2-T18-4 The stationary covariant GKLS cone --- and why state plus symmetry cannot select the dynamics
- Absorbs: L08-063, L08-064, L08-065, L08-070
- Class: EXPLORED-registered
- Raised by: orchestrator; presented as the note's concrete deliverable
- What: `C_U(sigma) = {L : L(X^*) = L(X)^*, Tr L(X) = 0, L(sigma) = 0, [L, Ad U_g] = 0, Q C_L Q >= 0}` with `C_L` the Choi matrix and `Q = I - |Omega><Omega|` --- linear equations plus one PSD constraint, necessary and sufficient; equivalently `L(X) = -i[H,X] + sum A_{ij}(F_i X F_j^* - {F_j^* F_i, X}/2)` with `A >= 0`, `H` in the commutant of `U`, `A` in the commutant of the induced representation on traceless operators, and unique once `Tr H = 0`. But every invariant faithful `sigma` has an **interior** feasible point `L_sigma(X) = sigma Tr X - X`, with conditional Choi matrix `Q(I ⊗ sigma)Q` strictly positive on `range Q`: because the cone has interior, small perturbations in every permitted direction stay GKLS, so positivity never shrinks the dimensions and **no amount of symmetry-plus-state will pin the generator down**. The dimension table at `sigma = I/p`: Galois torus `(p-1)(p+1)^2`; full Weil/`SL_2` `2p-2`; Weyl translations + Galois torus `p+1`; Weyl translations + full Weil **1** (orbit counts by BFS and independently by Burnside; these are dimensions of cones' spans, not claims that every coefficient in an orbit basis can be chosen nonnegative). Scope note on a tempting shortcut: the matrix test `-(B sigma + sigma B^*) >= 0` is necessary and sufficient only for a **fixed** finite no-event `B` with the scalar reset ansatz and positive exit flux; the cone allows `B`, `H` and all jump terms to vary, so failing that test is **not a no-go** for the larger inverse problem.
- Lead: extra arithmetic input is mandatory; the cone is the right object to impose it on. The useful regime is the Galois-torus-only row, which is large and unexplored.
- Where: notes/bc-symmetry-generators.md:143-178, :180-184, :188-207, :332-336

### G2-T18-5 Full affine symmetry removes the oscillatory modes --- and symmetry does not force equal odd decay rates
- Absorbs: L08-066, L08-067
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: All Weyl-covariant GKLS generators on `M_p` are `L(X) = sum_{v != 0} c_v(W_v X W_v^* - X)` with `c_v >= 0`; Galois covariance makes `c_v` constant on the `p+1` torus orbits and forces `c_v = c_{-v}`, so their Weyl eigenvalues are real and nonpositive, and full symplectic covariance gives exactly the depolarizer `L(X) = gamma(Tr(X)I/p - X)`. **Full affine symmetry in this model removes all oscillatory zero-like modes** --- a conditional obstruction to imposing those extra *commuting* symmetries, not to an adelic symplectic structure as such. And the hope that the prescribed symmetries force *equal* odd decay rates is refuted: `L = D - id + eps R_a` with `eps = 1/(4p^2)` and `R_a(W_v) = W_{av}`, `a` a primitive root, is CPTP with unique stationary state `I/p`, commutes with the entire Weil action and with parity, and at `p = 7` has odd-sector eigenvalues `-1-eps`, `-1+eps/2 ± i sqrt3 eps/2`, each of multiplicity 8. "All the prescribed finite state, linear symplectic and Galois symmetries coexist with unequal odd decay rates. No zeta zeros were used."
- Lead: the escape from the collapse is to make the symplectic structure act **non-commutingly** with the dynamics (covariance rather than commutation) --- explicitly left open. And one unexplained datum: in the tested *shear* classes at `p = 3,5,7` the odd real parts happen to coincide, and the note says those examples alone "do not refute an equal-rate statement" --- the coincidence is unexplained and might be a real phenomenon worth isolating.
- Where: notes/bc-symmetry-generators.md:215-238, :242-273

### G2-T18-6 Two prime levels: marginal compatibility does not select the coupling
- Absorbs: L08-068
- Class: EXPLORED-negative
- Raised by: orchestrator
- What: `L_c = (gamma_p - c)(D_p - id)⊗id + (gamma_q - c) id⊗(D_q - id) + c(D_p ⊗ D_q - id)` for `0 <= c <= min(gamma_p, gamma_q)` all have unique stationary state `I/(pq)`, full local Weyl and Weil covariance, and the **same** one-prime restrictions, while the joint traceless sector decays at `gamma_p + gamma_q - c`. Under CRT these are compatible prime-residue models. "The statement concerns two prime levels only; an infinite consistent, conservative adelic system has not been constructed."
- Lead: construct the infinite adelic system, or prove it cannot be conservative. The one-parameter family `c` is exactly the freedom an arithmetic constraint would have to fix.
- Where: notes/bc-symmetry-generators.md:277-300

### G2-T18-7 Parity as a local arithmetic grading --- is it the Phantasm's grading?
- Absorbs: L08-061
- Class: LEAD-unpursued
- Raised by: orchestrator (explicitly not pursued)
- What: Parity `P|x> = |-x>` implements the central symplectic element `-I` and also `U_{-1}`, so the local models already preserve even and odd operator sectors of dimensions `(p^2+1)/2` and `(p^2-1)/2`. "Identifying this local grading with the Phantasm's grading is still additional work."
- Lead: this is the **only arithmetically natural `Z_2` grading on the BC side anywhere in the group**. If it *is* the Phantasm's grading, the odd sector of the graded superdeterminant and the odd sector of the BC Lindbladian are the same object; if not, it should be ruled out. Nobody has tried either.
- Where: notes/bc-symmetry-generators.md:106-110

### G2-T19-1 The reproducibility discipline and its one exposed gap
- Absorbs: L13-157
- Class: EXPLORED-registered
- Raised by: orchestrator (infrastructure, in force)
- What: One row per evidence script, its captured output under `outputs/`, and the claims it backs; scripts run from the repository root with only numpy/scipy/mpmath/sympy; random data seeded; local CI re-running the fast scripts and diffing against captured output; every quote byte-checked at `<id>:<file>:<line>`; a `proved` claim names its review file and the gate checks for `VERDICT <id>: VALID`. No mathematical ideas of its own.
- Lead: the one substantive gap it exposes is that "proved" in this book means author `!=` reviewer **inside one model family** for the campaigns where only one family was declared.
- Where: report/sections/11_reproducibility_map.tex:1-66; report/sections/08_quantum_ihara_general.tex:18-22

### G2-T19-2 Sixteen notation ambiguities, four of them substantive
- Absorbs: L11-095
- Class: LEAD-unpursued
- Raised by: extractor
- What: Sixteen genuine clashes, several mathematical rather than typographic: (1) channel normalisation `Phi` vs `D Phi` vs `Sigma`; (2) Ramanujan units --- `lambda_2` of a channel vs `(q+1)lambda_2` vs Hastings' `lambda_H` vs `2 sqrt q`, and one table "mixes both units in one row"; (3) `q` vs `D-1`, which coincide in the LPS story and not in general; (11) whether canonical form of an MPS is the spectral condition or `sum_k A_k^† A_k = 1`; (12) which object "Riemann channel" denotes --- "**No note gives a one-sentence definition --- one must be written**"; (13) "Bost--Connes system" is never defined in the notes, only used.
- Lead: items (2), (3), (11), (12) can change statements, not only symbols. Decide them before the report shard.
- Where: notes/extract/notation-and-definitions.md:354-372

### G2-T19-3 Unreproduced founding-session numerics
- Absorbs: L11-078
- Class: LEAD-unpursued
- Raised by: extractor
- What: The 4-symbol cyclic-rule shift has small-matrix eigenvalues `2, 1±i, 0` and satisfies the RH analogue; the golden-mean shift has `phi, -1/phi` and does not. The `K_4` and prism numbers are likewise labelled "from the founding session" with **no script in the repository**.
- Lead: write the three-line script and register the results. Cheap; it is the notebook's simplest RH-fails example and is currently unreproducible.
- Where: notes/extract/notation-and-definitions.md:261, :263-264

### G2-T19-4 Citation hazards recorded
- Absorbs: L11-111, L11-052, L11-118, L13-142
- Class: EXPLORED-registered
- Raised by: extractor and orchestrator
- What: Four operational rules. (i) **Do not cite `lambda_H = 2 sqrt(D-1)/D` as a proved bound** --- Hastings shows `|lambda_2| -> lambda_H` *in probability* for random unitaries as `N -> infinity`; the rigorously proved bound is the weaker `lambda_loose(D) = sqrt(lambda_H)`. (ii) `refs/src/0809.1401/` holds the latest-version tarball carrying the **Kang--Li** title and author list, not Kang--Li--Wang, and is not byte-identical to `0804.2305`; the arXiv abs page reports the Kang--Li--Wang title for all three versions --- **quote Kang--Li--Wang from `0809.1401v1` only**. (iii) `math-ph/0404030`, the identifier guessed for Voros, serves an unrelated paper on `k`-decomposability of positive maps; it was fetched, identified as wrong, deleted and removed from the ID list (Voros is `math/0506326`; his earlier note `math/0404213` was not fetched). Also recorded as file hazards: Voros's file is latin-1 and GNU grep exits 1 on it without matching, and Coffey's main LaTeX file is named `lambda2.txt`. (iv) arXiv:2309.15873 was attributed to Kudo and Li by a literature agent; the TeX header gives Mason Eyler and Jaiung Jun, and every citation was corrected on 2026-09-12.
- Lead: none mathematical; guards for the provenance database.
- Where: notes/extract/weil-positivity-sources.md:518-550, :10-16; notes/extract/complex-zeta-sources.md:195-207; report/sections/09_prior_art.tex:295-300

---

## Top leads in this group

1. **G2-T6-6** --- "stop looking for a Hermitian form; look for positivity plus an operation under which eigenvalues multiply at fixed loss". The single most consequential steering statement across all three lanes, and no one has tried to realise it.
2. **G2-T8-4** --- the concrete family `B_i = G U_i G^{-1}`: the smallest class where the functional equation and real spectrum coexist *without* unitarity, i.e. G2-T6-6 made concrete. One paragraph, never built. *(small but consequential)*
3. **G2-T7-5** --- what replaces `mu mu' = D-1` for non-inverse-paired weights, and whether MPS canonical form buys anything. The most direct open side-B question; the decisive experiment (random MPS, measure pole radii) is cheap. *(small but consequential)*
4. **G2-T3-18** --- the candidate Phantasm bond `C ⊕ H_{>0}`, and the trap that reading the functional equation as ket/bra exchange assumes RH. Needs a symmetry implementing `rho -> 1-rho` that does not presuppose the answer.
5. **G2-T16-1** --- "the missing ingredient is transverse expansion: a circle has no Poincaré map, so no Jacobian, so no resonances". The cleanest statement of what any Phantasm must supply.
6. **G2-T3-17** --- RH for a curve as "every fermionic mode has correlation length exactly twice the bosonic one". A physics statement attackable with physics tools, written once and never used. *(small but consequential)*
7. **G2-T15-5(b)** --- the unrun `zst` Schur-complement-radius computation: it would decide whether the observed `e^{-4pi lambda^2}` convergence of the first zero is generic approximation theory or genuine arithmetic. Cheap and decisive. *(small but consequential)*
8. **G2-T8-9** --- Herglotz gives `r(n) = C^* U^n C`: a *constructive* route from positive-definiteness to the actual unitary the programme wants, flagged in half a sentence and never taken. *(small but consequential)*
9. **G2-T13-5** --- prove `Z_X(u)^{-1} = SDet(...)` for a finite graph. Knill and the Ihara literature compute the same shape and do not cite each other; the join is a publishable standalone result and would justify the notebook's central metaphor. *(small but consequential)*
10. **G2-T8-7 / G2-T8-8** --- reconcile Huang's termwise criterion with Toeplitz positive-definiteness, and close Lagarias's converse gap. This determines whether the notebook has a new theorem or a repackaging; Huang's "infinitely many even `k`" clause is an unexploited weakening. *(small but consequential)*
11. **G2-T9-11** --- define Kraus-weighted successor operators on the facets of a 2-complex (Kraus-weight LLP's branching operator) and prove the alternating-product identity. The object appears to be genuinely open and is the natural home for the grading.
12. **G2-T9-6** --- compute `B_X(u) = (1-u^{d+1})^chi / Z_ord` over a census of small 2-complexes and look for a non-building vertex collapse. A bounded, scriptable search that was never run. *(small but consequential)*
13. **G2-T16-3** --- compute the decomposition of `pi ⊗ conj pi` for the Weil representation and read off the Lindbladian gap: the dilation-time version of the finite Weil--LPS model.
14. **G2-T1-1 / G2-T1-2** --- the LMFDB + Jacquet--Langlands identification of the joint spectra, and the assembly of the Weil--LPS channels over all primes. The first makes the finite model arithmetic; the second is the only route in this group from a family of finite models to the actual zeros.
15. **G2-T13-6** --- redo the quantum Ihara--Bass as a Berezin integral over a chiral Dirac operator so the `chi` exponent becomes an index; and the never-applied overlap-fermion / gamma-five technology that would give an exact chiral symmetry on the discrete side. *(small but consequential)*

Runners-up worth keeping visible: **G2-T11-2** (a non-flat connection reproducing the pure-gauge determinant to `1.1e-15` --- theorem or coincidence?), **G2-T11-6** (the `Ã2` identity holding where its hypothesis fails), **G2-T17-4** (the unread open-quantum-random-walk paper, the cheapest place the novelty verdict could break), **G2-T12-6** (the free `q -> 1` degeneration), **G2-T18-7** (the `(p^2±1)/2` parity grading on the BC side), **G2-T9-5** (torsion cancellation for *any* degree `-1` map --- an unexplored family of Bass-type identities), **G2-T9-9** (the never-written colour-graded flow interpolating between the ordered and building rules), **G2-T8-5** (simplicity of the zeros as an extra hypothesis nobody tracks).

## Dead routes (consolidated)

**Curves, tensors, letters**
- `alpha_i = -lambda_i(E)` uniformly in `n` for Artin--Schreier curves: false; holds iff `P_g(-1) != 0` (G2-T2-4; 06b:80-92).
- The conjugated replacement law `S_n = -(-eta(-1))^n conj(Tr E^n)`: also false; holds iff `P_g(-eta(-1)) != 0` (G2-T2-4).
- "The entries are roots of unity" as the reason the transfer unitary has finite order: insufficient (zero entries, normalisation) --- 06c:159-162 (G2-T3-2).
- Cut-rank bound `D` across a ring cut: that is the open-chain bound; the ring bound is `D^2` --- 06c:168-170 (G2-T3-16).
- "Fixed finite lattice tensors give only supersingular zetas": explicitly false --- 06f:286-290 (G2-T3-16).
- "Carries must be unbounded" in base-`pi` digits: wrong; cyclic carries are bounded --- 06d:126-128 (G2-T3-8).
- Counting elliptic-curve points by a nonnegative-weight automaton or any finite weighted adjacency matrix / trace-class operator: impossible --- 06d:120-128 (G2-T3-8).
- The drafted HS/trace bound `sum_odd |mu|^2 <= 2 Tr E_{++} Tr E_{--}`: false, 173/400 random violations --- 06e:17-26 (G2-T4-1).
- The trace version `2 Tr S_+ Tr S_-` of the infinite-bond bound: needs positivity of `S_±` on HS space, which complete positivity does not give --- 06e:100-102 (G2-T4-2).
- The literal geometric placement of genus-two cohomology and the vacuum ansatz `a_1=1,B_1=0,a_2=0,B_2=B`: both impossible --- 06f:89-99 (G2-T3-10).
- Reading the functional equation as ket/bra exchange: would assume RH --- 06f:259-263 (G2-T3-18).
- Cubic and higher Artin--Schreier traces in the shift basis: non-local, so no fixed local tensor there (only in that basis) --- notation-and-definitions.md:313 (G2-T2-2).
- Dwork's transfer operator for RH: it sees `p`-adic sizes, not complex absolute values --- notation-and-definitions.md:314 (G2-T2-1).
- The infinite-label Fourier tensor at genus 1: honest but redundant, every closed ring but the vacuum vanishes --- 06d:62-72 (G2-T3-5).
- "Nonnegative coefficients forbid a numerator": false, `(1-u)/(1-2u)`; the operative hypothesis is "is an honest trace sequence" --- astra-proofs.md:669-680 (G2-T4-3).

**Zeta conditions**
- "Inverse-closed letters give the functional equation for the raw doubled transfer": false, counterexample `B = diag(1,2)` --- 06h:40-43 (G2-T5-2).
- Closing the Horner automaton into a trace to present a Dirichlet `L`-function as a ring norm: wrong (imposes a return condition) --- 06h:135-138 (G2-T5-6).
- The drafted square-root `Z/2` Artin factor for the pair shift: not an Artin factor; the correct example is a directed voltage cover --- 06h:74-76, :146-149 (G2-T5-3, G2-T5-6).
- Treating unique stationarity, whole-bond gauge and mixing as one condition: they are three --- 06h:195-199 (G2-T5-2).

**Deligne / graphs / channels**
- Deligne's pointwise (purity) theorem for graphs: false; the two-loop bouquet satisfies (a),(b),(c) and is not pure --- 07:153-161 (G2-T6-4).
- Commuting Kraus unitaries or commuting holonomies as a source of expansion: never gives an expander --- 07:174-188 (G2-T6-2).
- Prime-by-prime ansätze (direct sums of circle rotations, commuting dilations) to see the zeros: pure side A --- notation-and-definitions.md:349 (G2-T6-2).
- Looking for an `X x X` with `zeta` as its slice: there is none, so Deligne's "multiply" step has nothing to act on --- notation-and-definitions.md:330 (G2-T6-1).
- An inverse-paired Kraus counterexample to conjugation closure: none exists --- 08b:127-131 (G2-T8-3).
- The Dyson-expansion draft without free propagators between jumps: wrong for noncommuting `K` and `R_j` --- 08c:61-63 (G2-T8-2).
- Kraus structure alone forcing degeneracy of decay rates: it will not; arithmetic rigidity must enter --- notation-and-definitions.md:290 (G2-T6-7).

**Complexes and the graded reading**
- "The total graded zeta equals Kang--Li's `Z`": refuted; it is the completed vertex `L`-function --- 08d:310-320, astra-proofs.md:105-118 (G2-T9-9).
- The unrestricted ordered-cell flow as the building's edge successor: outdegree `2q^2+q` against `q^2`, colour classes not invariant --- 08d:302-308 (G2-T9-9).
- The ordered flow as `k!` copies of the Kang--Yu / LLP flow: opposition is strictly stronger than non-incidence --- astra-proofs.md:119-130 (G2-T9-9).
- Identifying the cochain product's Euler exponent with `chi`: it is `sum(-1)^i(i+1)f_i`; and the ordered-cochain exponent is `sum(-1)^i(i+1)! f_i`, already wrong on one edge --- 08e:40-41, astra-proofs.md:157-182 (G2-T9-5).
- A universal cubic vertex Bass identity on every 2-complex: refuted by `∂Δ^3` (poles at `u=-1, ±i`) --- 08e:68-79 (G2-T9-6).
- "No polynomial multiplier could clear the rational total": too broad; `p(u) = (1-u^4)^6` clears it on `∂Δ^3`; the surviving obstruction is Euler-factor-only --- astra-proofs.md:1059-1070 (G2-T9-6).
- "Links are generalised polygons of the same parameters" as the collapse class: refused; no cyclic type structure, no identified universal cover --- astra-proofs.md:328-341 (G2-T9-6).
- "The zeros are exactly the odd eigenvalues": false without the reciprocal, sign, multiplicity and cancellation qualifications --- 08e:91-93 (G2-T10-1).
- Calling the chamber zeros uncancelled zeros of the vertex `L`-function: wrong, they all cancel --- 08e:96-105 (G2-T10-2).
- `k`-cells literally realising `H^{k-1}` with Weil weight `k-1`: only the parity exponents match --- astra-proofs.md:401-447 (G2-T10-3).
- One pure fermion determinant giving the total supertrace with flow parity equal to cell chirality: does not exist; the total is a Berezinian --- 08e:141-152 (G2-T10-4).
- The building "Laplacian" as `(d+delta)^2`: `delta^2 != 0`, so a degree-(-2) term appears --- astra-proofs.md:597-599 (G2-T10-4).
- Knill's super pseudodeterminant as the `u -> 1` limit of the zeta or the Euler factor: one edge gives three different numbers (1, 2, 0) --- astra-proofs.md:213-226 (G2-T13-5).
- "The full representation twist is a representation block": refuted by the four-cycle with `G = Z/4`; the covariant weights are pure gauge --- 08f:20-31 (G2-T11-2).
- `E_{(g,gs)} = rho(s)` as a flat connection: it is not, in the chronological convention; 192 of 192 ordered 2-cells fail on `Cay(Q_8, ...)` --- astra-proofs.md:697-700 (G2-T11-2).
- `R = pi ⊗ conj pi` embedding in a single regular representation: only spectral support transfers --- astra-proofs.md:726-729 (G2-T11-3).
- Asserting a fractional Euler exponent `c^{d_hol chi/|G|}` when simplex stabilisers exist: not a rational determinant; measured `(1-u)^{13}(1-u^3)^1` where `16/3` was predicted --- 08f:53-56 (G2-T11-3).
- A scalar global determinant identity restricting automatically to every irreducible: it does not --- astra-proofs.md:442-447 (G2-T11-3).
- Removing only the channel fixed points in the Harrow-type transfer: type characters survive and violate the tempered bound; remove the exceptional space --- 08f:70-72 (G2-T11-5).
- One faithful `pi` detecting Ramanujan: false on `Cay(Z/28, {±1,±3})` --- astra-proofs.md:878-901 (G2-T11-5).
- The pole placement in the orchestrator's `Ã2` brief: fails at `u^3` and on the degree count; `det(I-uL_B)` for `det(I+uL_B)` fails at `u^15`; the chamber radius prediction `q^{3/4}` was stale --- 08f:160-164, numerics.md:128-145 (G2-T11-7).
- Assuming a non-type-preserving Cayley quotient satisfies the type-preserving theorem: a separate descent argument is required --- astra-proofs.md:965-984 (G2-T11-6).
- "LLP's condition is an invariant `|s| = 1`": `Im s` is defined only mod `2pi/log b` --- astra-proofs.md:906-924 (G2-T12-2).
- Reading Kamber's bound as an upper bound on pole radii: it inverts to `|u| >= q^{-(p-1)/p}` --- astra-proofs.md:902-924 (G2-T12-2).
- Assuming higher-rank RH has a duality: the type-(e) chamber block has radii `q^{-1/2}` (x1) and `q^{-1/4}` (x2); no `u -> c/u` or `c/conj u` works --- astra-proofs.md:925-946 (G2-T12-3).
- Expecting factor-by-factor RH from the all-rank Kang--Yu identity: that paper states no RH --- astra-proofs.md:183-193 (G2-T9-2).
- Arbitrary Kraus weights preserving the building Euler/Hecke formula: they preserve only the Schur identity; the cochain cancellation needs an invertible **flat** local system --- astra-proofs.md:787-812 (G2-T11-1).
- The `L^2`/Fuglede--Kadison route to a zeta formula: "no direct relationship between the `L^2`-torsion of a matrix and its entries" --- cohomological-zeta-sources.md:753-757 (G2-T13-4).
- A single cohomological degree as a topological invariant: only the alternating combination is --- cohomological-zeta-sources.md:846-851 (G2-T13-4).
- A naive plain (unweighted) alternating Euler characteristic as the divisor: it vanishes identically in Deitmar's setting --- cohomological-zeta-sources.md:143-146 (G2-T13-2).
- "The zeros are the odd cohomology" as a stable statement: the alternating count jumps from `4-2b_1` to `4-b_1` under a generic conformal perturbation --- cohomological-zeta-sources.md:481-492 (G2-T13-3).
- Treating the hypergraph zeta as a new object: `zeta_H(u) = Z_{B_H}(sqrt u)` --- complex-zeta-sources.md:840-858 (G2-T9-1).
- Expecting a Ramanujan notion from the combinatorial Ruelle zeta of a triangulation: its distinguished point `(n+2)^{-1}` is not `q^{-1/2}` and there is no spectral-gap statement --- complex-zeta-sources.md:1097-1102 (G2-T9-10).
- Looking for a Bartholdi zeta of a simplicial complex: the generalisation exists for graphs and hypergraphs only --- complex-zeta-sources.md:1482-1485 (G2-T9-10).
- Treating the "not found" literature verdicts as nonexistence proofs: arXiv search is metadata-only --- astra-proofs.md:1118, prior-art:137 (G2-T9-3, G2-T17-2).
- Expecting a quantum walk on a complex, a Ramanujan-quantum-expander paper, or First's Ramanujan-property paper to carry a zeta: verified zero occurrences in all three --- cohomological-zeta-sources.md:1715-1724, :1755-1762, :1824-1829 (G2-T9-11, G2-T17-1).
- Claiming the fermionic-cMPS graded bond as a novel construction: it is already in Haegeman--Cirac--Osborne--Verstraete --- riemann-cmps-sources.md:625-632 (G2-T14-3).
- Identifying Huang's termwise criterion with Toeplitz positive-definiteness: different conditions, neither implying the other --- weil-positivity-sources.md:500-513 (G2-T8-7).

**Selberg / Lindblad / BC**
- "The Poisson trace of the direct sum" over prime circles: the smeared operator is never trace class and the comb is not tempered --- 09b:161-186 (G2-T16-1).
- Squaring the projected tangent vectors to get the Selberg Lindbladian: misses the drift --- 09b:213-218 (G2-T16-2).
- The Casimir as a diffusion Lindbladian on all of `L^2(Gamma\G)`: it carries the compact direction with a minus sign --- 09b:205-209 (G2-T16-2).
- The drafted minus sign in the flat-trace/tower relation: it is a plus; and the graph counterpart of the tower is `det(1-uH)`, not the zeta --- 09c:39-42 (G2-T16-4).
- "The cusp term of the modular trace formula is the trace of the Riemann channel damped at rate 1/4": corrected to a statement about prime measures only --- 09c:132-138 (G2-T16-6).
- An exact finite-dimensional unital `*`-representation of the full BC algebra retaining the nontrivial phases: impossible (`mu_n mu_n^* = I` forces `e(1/n) = I`) --- bc-symmetry-generators.md:66-80 (G2-T18-3).
- Imposing Weyl-translation plus full Weil covariance on the BC Lindbladian: the cone collapses to the depolarizer --- bc-symmetry-generators.md:215-238 (G2-T18-5).
- Hoping the prescribed symmetries force equal odd decay rates: refuted at `p = 7` --- bc-symmetry-generators.md:242-273 (G2-T18-5).
- Selecting the adelic coupling by marginal compatibility alone: the family `L_c` has identical one-prime restrictions --- bc-symmetry-generators.md:277-300 (G2-T18-6).
- Using `-(B sigma + sigma B^*) >= 0` as a no-go: it binds only a fixed no-event `B` with the scalar reset ansatz --- bc-symmetry-generators.md:332-336 (G2-T18-4).

**Window extension**
- Beating the extension disc: no estimator of the next trace from the traces up to lag `K` and positivity alone can do better --- 08g:104-107 (G2-T15-2).
- Using integrality to pin the next trace of a `q`-regular graph: defeated by rescaling; the disc radius exceeds one in count units --- 08g:161-166 (G2-T15-3).

## Bookkeeping issues

- **Shard 06h is entirely unreviewed by a second model family**; every row is `sketched` or `numerical` (report/sections/06h_zeta_conditions.tex:19) --- G2-T5-1.
- **`obs:rh-iff-ramanujan-channel` is tagged `sketched` because it has had no reviewer**, and it is the load-bearing bridge between zeta language and channel language (08:288-299) --- G2-T7-4.
- **The Watanabe--Fukumizu shape-matching for Theorem 1 is checked numerically only** (`notes/reviews/scratch_wf_mo_conventions.py`); no local source covers arbitrary weights on a bouquet, and their corollary does not apply to loops (08:219-239) --- G2-T7-6.
- **Novelty downgrade**: the graded/fermionic cMPS bond structure is already in the literature; only the arithmetic reading can be claimed (riemann-cmps-sources.md:625-632) --- G2-T14-3.
- **Novelty hazard**: Ben-Aroya--Schwartz--Ta-Shma's remark about improving to a quantum Ramanujan expander was read from a publisher PDF with no byte-verified local TeX (09:249-253) --- G2-T1-3.
- **Citation hazard**: do not cite `lambda_H = 2 sqrt(D-1)/D` as a proved bound; Hastings proves only `sqrt(lambda_H)` rigorously (weil-positivity-sources.md:546-550) --- G2-T19-4.
- **Citation hazard**: `refs/src/0809.1401/` carries the Kang--Li title, not Kang--Li--Wang --- quote Kang--Li--Wang from `0809.1401v1` only (complex-zeta-sources.md:195-207) --- G2-T19-4.
- **Corrected misattributions**: `math-ph/0404030` is not Voros (deleted from `refs/src/`); arXiv:2309.15873 is Eyler--Jun, not Kudo--Li (corrected 2026-09-12) --- G2-T19-4.
- **Unverified proof steps flagged by the reviewer**: Kang--Yu's `thm:Phi-determinants` and the local factorisation were confirmed to exist at the cited addresses but not checked line by line; everything conditional on Kang--Yu rests on them (reviews/complex-zeta-2026-09-13.md:612) --- G2-T11-8.
- **Incomplete audits**: the global Euler-factor identity `prod_rho F_rho^{d_rho} = c^chi` was confirmed on two isotypic blocks only; the `Ã2` descent was checked only to `u^18`; the `pi ⊗ conj pi` 144-dimensional block was never built --- G2-T11-3, G2-T11-8.
- **Assumption registers not discharged**: eight external theorems in the complex lane (08d:207-289); six standard Selberg inputs (09b:28-84); `asm:weil-implementer-exact`, `asm:as-lpolynomial`, `asm:deuring-lift`, `asm:cm-hodge-type` (whose eigenspace statement is "not quotable from the fetched TeX"), `asm:cm-polarised-lift`, `asm:kraus-hs-setting` ("not established for any Riemann cMPS") --- G2-T12-5, G2-T16-8, G2-T2-3, G2-T2-4, G2-T3-3, G2-T3-9, G2-T4-2.
- **Wrong statement corrected in the framing**: the slogan "no bosonic (positive) ring norm can produce a zeta with a numerator" is false as worded; the hypothesis is "is a trace sequence" (astra-proofs.md:669-680, review:321-330) --- G2-T4-3.
- **Claimed "iff" carries a known gap**: the Weil-criterion converse needs a test-function class rich enough to separate the zeros; the source says so explicitly and the notebook inherits the gap (weil-positivity-sources.md:310-322) --- G2-T8-8.
- **Definition missing**: no note gives a one-sentence definition of "the Riemann channel"; "Bost--Connes system" is used but never defined; Ramanujan units are mixed within a single table row (notation-and-definitions.md:354-372) --- G2-T19-2.
- **Unreproducible numerics**: the founding-session shift/`K_4`/prism numbers have no script in the repository (notation-and-definitions.md:261-264) --- G2-T19-3.
- **"Proved" means author != reviewer inside one model family** for campaigns where only one family was declared (08:18-22) --- G2-T19-1.
- **Prior-art absence claims rest on metadata-only searches**; no full-text search has ever been run (09:279-293) --- G2-T17-2.
- **Requested tests substituted**: the brief's non-building targets (4-simplex boundary, 7-vertex triangulated torus) were replaced by `∂Δ^3` and the octahedron; the `b_1 != 0` case was never computed (astra-brief.md:29) --- G2-T9-7.
- **Terminological guard**: the entanglement Hamiltonian `-log rho_A` is Hermitian by construction and must not be conflated with the non-Hermitian transfer generator (notation-and-definitions.md:291) --- G2-T14-3.

## Audit

Total lane entries in the three files: **356** (L13: 157; L11: 118; L08: 81).
Absorbed: **356**. None omitted.
Digest items: **139** across 19 themes.

Per-lane check: L13-001 … L13-157 all appear exactly once in an "Absorbs" list; L11-001 … L11-118 likewise; L08-001 … L08-081 likewise. Each lane's "Small but possibly consequential" entries were re-used by ID (they name existing entries, not new ones) and are surfaced in the Top-leads section; each lane's "Dead routes recorded" bullets restate entries already absorbed above and are consolidated, with digest-item back-references, in the Dead routes section.
