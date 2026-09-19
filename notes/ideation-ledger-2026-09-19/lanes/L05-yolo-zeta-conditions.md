# Lane L05: the yolo Lindbladian and the zeta-conditions catalogue

Two campaigns of the night of 2026-09-14. Campaign Y ("yolo Lindbladian") guessed a
phase-side Lindbladian for the Riemann zeros and had it audited; the audit came back
mostly negative, but with several exact positive by-products. Campaign Z
("zeta conditions") lined up the conditions a zeta should obey and imposed them factor
by factor on concrete graded MPS / cMPS tensors, producing thirteen buildable examples.

Attribution convention used below: the three brief files were written by the
orchestrator (Claude) as deliberately-slightly-too-strong drafts; the three report
files (`astra-*.md`) were written by the codex prover lane (astra / gpt-6-astra);
one passage is TJO verbatim.

## Coverage

| file | lines | read fully? | ideas found |
| --- | --- | --- | --- |
| notes/yolo-lindblad/astra-brief-A.md | 88 | yes | 14 (the guess + S1-S8 drafts + conventions) |
| notes/yolo-lindblad/astra-brief-B.md | 67 | yes | 6 (finite-model design, N1-N6, the "hunt" method, the unbuilt oscillator) |
| notes/yolo-lindblad/astra-finite-model.md | 403 | yes | 13 (numerical verdicts, exact resolvents, the repaired edge model) |
| notes/yolo-lindblad/astra-structure.md | 896 | yes | 34 (full audit: corrections, exact positives, OPEN items, ledger) |
| notes/yolo-lindblad/finite/report_template.md | 308 | yes | 0 new — byte-identical prose to `astra-finite-model.md` with `@@TABLE@@` placeholders; verified by diff. Only the rendering pipeline (seed `20260914`, `render_report.py`) is unique, and that is infrastructure, not an idea. |
| notes/zeta-conditions/astra-brief.md | 129 | yes | 20 (TJO's verbatim request, C1-C10 ledger, D1-D8 drafts, the explicitly-wanted tiny L-functions) |
| notes/zeta-conditions/astra-constructions.md | 1882 | yes (prose 1-377 in full; generated appendix 379-1882 scanned line by line for prose, matrices read as data) | 30 |
| notes/zeta-conditions/finite/README.md | 21 | yes | 1 (the "all-degree claims need proofs, a finite tally does not establish them" caveat) |
| notes/zeta-conditions/finite/results/evidence.md | 1504 | yes | 0 new — byte-identical to lines 379-1882 of `astra-constructions.md` (verified by diff); its 10 prose footnote bullets are folded into the entries below |

Total distinct entries: 84.

## Ideas and leads

---

### L05-001 The yolo guess itself: a phase-side Riemann Lindbladian
- Source: notes/yolo-lindblad/astra-brief-A.md:26-30; verdicts at notes/yolo-lindblad/astra-structure.md:7, 893-896; notes/yolo-lindblad/astra-finite-model.md:393-403
- Raised by: orchestrator (Claude), from TJO's central priority
- Status at last mention: pursued, negative (shard 04g "yolo Lindbladian: negative")
- Content: The guess is jumps `R_p = sqrt(lambda_p) V_p (x) T_{log p}` on `L2(Zhat) (x) L2(R_+^*)` with `lambda_p = 1/p`, where `V_p` is the prime-preimage isometry on the profinite phases and `T_{log p}` translates the archimedean line by `log p`; plus a Gamma-factor oscillator ladder and a Hamiltonian `D = x d/dx + 1/2`. The physical cMPS runs along the archimedean coordinate and "the letters are the primes". The ring norm with parity closure would be `Tr[Gamma_b e^{tT}]`. Every structural claim about it was either proved for the isometries alone or corrected.
- Lead: none survived as stated. The named replacements are L05-032 (annulus basis), L05-034 (radial local critical state) and L05-012 (the exact reciprocal-zeta multiset matrix element).
- Related: L05-002 … L05-050.

### L05-002 Prime jump = Galois away from p (S1)
- Source: notes/yolo-lindblad/astra-brief-A.md:34-37; notes/yolo-lindblad/astra-structure.md:45-78, 837-840; notes/yolo-lindblad/astra-finite-model.md:95-110
- Raised by: orchestrator (Claude); audited by codex prover
- Status at last mention: PROVED in part, CORRECTED in part
- Content: `V_p f(x) = sqrt(p) f(x/p) 1_{p Zhat}(x)` is an isometry with `V_p^* e_r = p^{-1/2} e_{pr}`, `V_p e_r = p^{-1/2} sum_{ps=r} e_s`, and it commutes with every Galois unitary `U_a`. The drafted claim that on a finite quotient `Z/b` coprime to `p` the jump *is* the Galois (Shor) map was corrected: it is `sqrt(p) V_p^*` restricted to that level that is the unitary permutation `r -> pr`, and `V_p` itself does not preserve the level at all (already `V_p e_0` has modes of denominator `p`).
- Lead: whenever a "prime jump = Galois unitary" shortcut is used anywhere in the programme, insert the `sqrt(p)` and check which direction is meant. If it worked unqualified, a whole prime-jump dynamics would be a group action and much easier.
- Related: L05-003, L05-005.

### L05-003 The Ramanujan shells as the Galois-fixed sector (S2)
- Source: notes/yolo-lindblad/astra-brief-A.md:38-41; notes/yolo-lindblad/astra-structure.md:80-113, 841-845
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED (all four drafted shell formulas)
- Content: `|b> = c_b / sqrt(phi(b))` with `c_b` the Ramanujan sum; the Galois-fixed subspace `G` is exactly the closed span of the `|b>` and reduces both `V_p` and `V_p^*`. The forward formula is `V_p|b> = p^{-1/2}|b> + sqrt((p-1)/p)|pb>` for `p` not dividing `b`, and `|pb>` otherwise; the backward one is `p^{-1/2}|b>` resp. `p^{-1/2} sqrt(phi(b)/phi(b/p))|b/p>`. The vacuum `|1>` is not invariant. The audit adds the case distinction the draft missed: the downward coefficient is `sqrt((p-1)/p)` when `p` exactly divides `b`, and one when `p^2 | b`.
- Lead: this is the one piece of the guess that is fully solid and reusable; any successor model can be built on the shell ladder.
- Related: L05-002, L05-031, L05-032.

### L05-004 "Even = span{e_0} = the Bost-Connes critical KMS state" as the grading
- Source: notes/yolo-lindblad/astra-brief-A.md:20-22; notes/yolo-lindblad/astra-structure.md:115-128, 846; notes/yolo-lindblad/astra-finite-model.md:289-297
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED (dead as drafted)
- Content: The brief graded the bond by "even = the constant function (the BC critical KMS state on the phases), odd = its complement". Two things break. First, the trivial Galois representation occurs on *all* of `G`, not just on `C e_0`, so "even = Galois-trivial" would be a different grading. Second and decisively, the generator does not commute with `Gamma_b`: eq. (2.4) shows `L_{p}(P_0)` produces odd cross terms `|1><p| + |p><1|` with coefficient `lambda_p sqrt(p-1)/p`, and distinct primes give distinct nonzero cross terms, so the failure persists for every nonempty positive-rate prime set. The finite model confirmed it numerically (largest grading commutator entry `0.707106781`).
- Lead: any successor must either pick a grading the prime jumps actually preserve, or supply a dynamics that does. Without an invariant odd sector the whole "RH = uniform decay of the odd sector" reading has nothing to act on.
- Related: L05-025, L05-030, L05-046.

### L05-005 Gauss vectors as scalar dephasing eigenmodes (S3)
- Source: notes/yolo-lindblad/astra-brief-A.md:42-51; notes/yolo-lindblad/astra-structure.md:130-182, 847-853; notes/yolo-lindblad/astra-finite-model.md:112-156
- Raised by: orchestrator (Claude)
- Status at last mention: half PROVED, the dynamical inference CORRECTED
- Content: `V_p^* ghat_chi = p^{-1/2} conj(chi(p)) ghat_chi` for `p` coprime to the modulus is exact, with no extra Gauss-sum normalisation. But the Lindblad recycling term uses `V_p f, V_p g`, not their backward images, so the coherence `|e_0><ghat_chi|` is not a scalar mode: the explicit counterexample is the nontrivial character mod 3 with `p = 2`, where `V_2 |v><g|` picks up a `|e_{1/2}><e_{1/6}|` coefficient absent from the original. The one-dimensional compression exists and has coefficient `sum_{p∤b} lambda_p (p^{-1} chi'(p) conj(chi(p)) - 1) - sum_{p|b} lambda_p` — note the *extra* `1/p` that the draft missed. Numerically the orthogonal residual is large (0.61 at beta=1, P=47), so it is not a truncation artefact.
- Lead: the extra `1/p` is the thing to explain or remove. If a modified jump gave the character rate `lambda_p(1 - chi(p))` without the `1/p`, the log-L identity L05-006 would become the actual spectrum.
- Related: L05-006, L05-007, L05-046.

### L05-006 The exact log-zeta minus log-L identity, prime powers and bad primes included
- Source: notes/yolo-lindblad/astra-structure.md:184-208, eqs (3.5)-(3.6), ledger 851-853
- Raised by: codex prover (proving a drafted S3 extension)
- Status at last mention: PROVED
- Content: With `A_beta(psi) = sum_p (psi(p)-1)/p^beta`, one has exactly `A_beta(psi) = log L(beta,psi) - log zeta(beta) + sum_p sum_{k>=2} (1 - psi(p)^k)/(k p^{k beta})`; every `p | b` contributes `-p^{-beta}` and there are no omitted bad-prime terms. For *genuine* Galois-unitary jumps (choose a unit `a_p == p mod b`) the good-prime part is real dephasing at exactly this rate. Also corrected: the notebook's blanket claim that character-diagonal unitary jumps "cannot produce frequencies" — asymmetric weights give imaginary parts `sum lambda_p Im psi(p)`; only inversion-symmetric weights force the scalar real.
- Lead: build the *Galois-unitary* dephasing model (jumps `U_{a_p}` at rates `lambda_p`) rather than the isometry model, and its coherence decay rates are literally `log L - log zeta` up to prime powers. Consequence: character sectors would carry L-function data by construction; the open part is the bad primes, where no such unit exists.
- Related: L05-005, L05-007, L05-046.

### L05-007 The Bost-Connes transfer eigenvalue is a prime-power compound Poisson generator
- Source: notes/yolo-lindblad/astra-structure.md:210-234, eqs (3.7)-(3.9), ledger 854-855; notes/yolo-lindblad/astra-finite-model.md:138-145
- Raised by: codex prover
- Status at last mention: PROVED
- Content: On the exact-denominator-`b` block, `zeta(beta)^{-1} sum_n n^{-beta} K_n` has eigenvalue `L(beta, conj chi)/zeta(beta)` on `ghat_chi`; its logarithm is `sum_p sum_{k>=1} (conj(chi)(p)^k - 1)/(k p^{k beta})`. So the BC transfer operator is *exactly* the exponent of a compound-Poisson generator with jump rates `p^{-k beta}/k` on prime powers, on the killed finite residue block. Equivalently each prime's exponent has the geometric law `(1-p^{-beta}) p^{-k beta}` and averaging its permutation gives the same product. Keeping only `k=1` gives L05-006, not this. For primitive `chi` the Gauss vector is a genuine eigenvector of the full transfer; for imprimitive it need not be (mod 6 counterexample given).
- Lead: this is a fully-specified arithmetic generator whose spectrum is `L/zeta` by construction — use it, rather than the phase isometries, as the starting point for a "transfer semigroup whose eigenvalues carry L-data". Consequence: it is a dissipative dynamics with L-functions as eigenvalues, with no zeros put in by hand. The open part is that its eigenvalues are `L(beta,·)/zeta(beta)` at *real* beta, not at the critical line.
- Related: L05-006, L05-005.

### L05-008 Critical vanishing of the Ramanujan expectation (S4)
- Source: notes/yolo-lindblad/astra-brief-A.md:52-55; notes/yolo-lindblad/astra-structure.md:236-256, 856; notes/yolo-lindblad/astra-finite-model.md:158-194
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED (exactly, by sympy rationals too)
- Content: `<c_b>_beta = zeta(beta)^{-1} sum_n n^{-beta} c_b(n) = sum_{d|b} mu(b/d) d^{1-beta} = b^{1-beta} prod_{p|b}(1 - p^{beta-1})`, which tends to 0 as `beta -> 1+` iff `b > 1`, and to 1 for `b = 1`. This is the sense in which the critical BC phase state "collapses onto the vacuum": every nontrivial Ramanujan shell observable has vanishing expectation at criticality.
- Lead: none stated beyond the correction L05-009. It is the cleanest "criticality selects the vacuum" statement in the campaign.
- Related: L05-009, L05-010.

### L05-009 "The critical state is the pure vector state of e_0 on C(Zhat)"
- Source: notes/yolo-lindblad/astra-brief-A.md:54-55; notes/yolo-lindblad/astra-structure.md:258-266, 857; notes/yolo-lindblad/astra-finite-model.md:174
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED (dead)
- Content: Haar *is* the vector state of `e_0`, and that vector state is pure on `B(L2)`, but its restriction to the commutative phase algebra `C(Zhat)` is Haar integration, not point evaluation, hence mixed. Explicit witness: `A = 2 Zhat` and its complement both have measure 1/2, and Haar is their nontrivial equal mixture; `omega(1_A) = 1/2 != omega(1_A)^2`.
- Lead: none. Recorded so nobody repeats "critical = pure".
- Related: L05-008, L05-010.

### L05-010 Weak-* convergence of the Gibbs phase states to Haar, on the whole algebra
- Source: notes/yolo-lindblad/astra-structure.md:267-268
- Raised by: codex prover (going beyond what was asked)
- Status at last mention: PROVED
- Content: The convergence of the Bost-Connes Gibbs phase states to Haar as `beta -> 1+` holds weak-* on the *entire* phase algebra `C(Zhat)`, not merely on Ramanujan sums. The proof: for a residue class mod `b`, write positive elements as `b(k+theta)`; the difference `sum_k (k+theta)^{-beta} - zeta(beta)` stays bounded for `1 < beta <= 2`, so normalised mass tends to `1/b`; locally constant functions converge to their Haar expectation, and they uniformly approximate continuous functions on a profinite compact space.
- Lead: this upgrade means a "critical KMS fixed point" statement can be made on the full phase algebra, not just on a convenient family of observables. Useful for the BC reframe priority.
- Related: L05-008, L05-034.

### L05-011 The central question: which generating function has 1/zeta in the denominator (S5)
- Source: notes/yolo-lindblad/astra-brief-A.md:56-64 ("This is the central question of the brief"); answers at notes/yolo-lindblad/astra-structure.md:270-353, 473-475; notes/yolo-lindblad/astra-finite-model.md:196-285
- Raised by: orchestrator (Claude)
- Status at last mention: pursued, negative for the guess; OPEN as a question (structure §5.8)
- Content: The brief asked for the exact operator statement — resolvent, Laplace transform in archimedean length, or ring norm — of the phase-side Lindbladian restricted to `G` that has `zeta(s)` in a denominator with poles exactly the nontrivial zeros, and anticipated the failure mode: "If the free (ordered-word) structure gives `1/(1 - sum_p lambda_p p^{-s} ...)` instead of `1/zeta`, say so and identify what restores the multiset (Euler product) structure". That is exactly what happened. The audit's §5.8 states plainly: "There is presently **no defined ring norm of the full guess**, and no proof that a resolvent or a length Laplace transform of its invariant dynamics on `G` has poles at the nontrivial zeta zeros."
- Lead: the three named candidate mechanisms for restoring the Euler product (commutation of the `V_p`, the stay term in S2, the parity closure) were each tested and each fails — see L05-013. What does restore it is an occupation-space trace or an explicit multiset product.
- Related: L05-012, L05-013, L05-014, L05-043.

### L05-012 The exact reciprocal-zeta matrix element of an inverse multiset sum
- Source: notes/yolo-lindblad/astra-structure.md:333-363, eqs (5.7)-(5.9), ledger 860
- Raised by: codex prover
- Status at last mention: PROVED (the single strongest positive of campaign Y)
- Content: Define `A(w) = sum_{n>=1} n^{-w} V_n = prod_p (I - p^{-w} V_p)^{-1}`, converging in operator norm for `Re w > 1`. Then `A(w)^{-1} = sum_n mu(n) n^{-w} V_n = prod_p (I - p^{-w} V_p)`, and since `<v, V_n v> = n^{-1/2}`, `<v, A(w)^{-1} v> = 1/zeta(w + 1/2)` exactly. This is an exact operator statement derived from the jumps themselves — but it is the matrix element of the inverse of a deliberately specified sum over *one copy of each integer*, not a resolvent or time-Laplace transform of any Lindbladian. A three-row table records which length weight gives which shift: `V_n` gives `zeta(s+1/2)`, `n^{-1/2} V_n` gives `zeta(s+1)`, `n^{-1} J_n` on the doubled vacuum gives `zeta(s+2)`. "Removing shifts to display `1/zeta(s)` requires explicitly changing the length weights."
- Lead: the missing steps are named precisely — extend the family in operator norm past `Re w > 1`, establish a closed generator, and make its poles generator eigenvalues. If those three were done, the reciprocal-zeta matrix element would become a spectral statement. Also: if the recorded length is `2 log p` rather than `log p`, replace `s` by `2s`; no factor of two is implicit.
- Related: L05-011, L05-013, L05-050.

### L05-013 Word multiplicities vs multiset multiplicities: the obstruction to the Euler product
- Source: notes/yolo-lindblad/astra-structure.md:365-383 eqs (5.10)-(5.11), 447-449, ledger 863-864; notes/yolo-lindblad/astra-finite-model.md:205, 219
- Raised by: codex prover
- Status at last mention: CORRECTED (a genuine, small, decisive obstruction)
- Content: Even though the `V_p` all commute, the ordered-word resolvent keeps multinomial multiplicities: `(I - u K_F(s))^{-1} = sum_n u^{Omega(n)} (Omega(n)!/prod k_p!) lambda(n) n^{-s} J_n`. The factor `Omega(n)!/prod k_p!` counts words with the same product — `pq` with `p != q` occurs *twice* in the length-two word sum but once in a multiset Euler product. The Poisson evolution likewise gives products of Poisson weights, not geometric weights. Neither the stay term of S2 nor a parity insertion changes this: "A parity insertion changes a trace functional; it does not replace `Omega(n)!/prod k_p!` by one."
- Lead: what does restore the Euler weights is stated: replace the word sum by `prod_p (I - z_p V_p)^{-1}`, or use an occupation-space trace with one coordinate `k_p` per prime. That is a *different construction*, not a consequence of commutation. Anyone hoping "commuting jumps give an Euler product" should stop here.
- Related: L05-012, L05-014, L05-043.

### L05-014 The exterior occupation parity: a second grading that gives 1/zeta as a signed trace
- Source: notes/yolo-lindblad/astra-structure.md:451-452
- Raised by: codex prover
- Status at last mention: PROVED, raised in passing, not pursued
- Content: Take one occupation coordinate `k_p >= 0` per prime with finite support; unique factorisation identifies the basis with integers `n` and the energy `sum k_p log p` is `log n`, so the thermal trace is `zeta(s)`. Restricting to occupancies 0 and 1 and giving each configuration the parity `(-1)^{sum k_p}` gives the absolutely convergent *signed* trace `sum mu(n) n^{-s} = prod_p (1-p^{-s}) = 1/zeta(s)`. Crucially: "This is an exterior occupation-space parity. It is different from the fixed doubled-bond parity in this brief."
- Lead: the programme has been using one grading (the doubled-bond parity `Gamma_b`) where the arithmetic wants another (exterior/fermionic occupation parity). Pursuing the second grading directly gives `1/zeta` as a supertrace with no boundary functional games. Consequence if it worked: the "zeros = odd sector" reading would get an honest fermionic realisation.
- Related: L05-013, L05-015, L05-071.

### L05-015 "All primes fermionic, zeros on Re s = 0"
- Source: notes/yolo-lindblad/astra-structure.md:454, ledger 866
- Raised by: an earlier shard of the notebook, quoted; corrected by codex prover
- Status at last mention: CORRECTED (dead as a global statement)
- Content: The shard's statement is correct about the *individual finite factors* `1 - p^{-s}` and finite products, whose zeros do have `Re s = 0`. It is not a statement about the zero or pole set of the analytically continued `1/zeta`: those factor zeros lie outside the half-plane where the infinite product converges, so no inference from finite factors to the continuation is available.
- Lead: none. Recorded so the fermionic-product picture is not over-read.
- Related: L05-014, L05-044.

### L05-016 Bernoulli continuation of zeta with no zero input
- Source: notes/yolo-lindblad/astra-structure.md:456-465, eq (5.17)
- Raised by: codex prover
- Status at last mention: PROVED (a tool, not a claim)
- Content: An explicit Euler-Maclaurin/Bernoulli continuation `zeta(s) = 1/(s-1) + 1/2 + sum_{r<=M} B_{2r}(0)/(2r)! (s)_{2r-1} - ((s)_{2M}/(2M)!) int_1^inf B_{2M}({x}) x^{-s-2M} dx`, holomorphic for `Re s > 1 - 2M`, meromorphic on the plane with only possible pole at 1. Written out because the campaign forbade importing anything about zeros.
- Lead: keep this as the standard "continuation without zeros" citation inside the notebook, so continuation steps never smuggle in zero data.
- Related: L05-017, L05-018.

### L05-017 Inside the strip, the Ramanujan series has no numerator cancellations
- Source: notes/yolo-lindblad/astra-structure.md:469
- Raised by: codex prover
- Status at last mention: PROVED; mentioned once, not followed up
- Content: For `sum_b c_b(n) b^{-s} = sigma_{1-s}(n)/zeta(s)`, the numerator for `n = prod p^{a_p}` is `prod_p (1 + p^{1-s} + ... + p^{a_p(1-s)})`, and a zero of a nonconstant geometric polynomial has its argument on the unit circle, so *all* numerator zeros have `Re s = 1`. Therefore inside the open critical strip `0 < Re s < 1` the poles of this scalar function are exactly the zeros of zeta, with their orders — proved without assuming any zero exists or where it lies.
- Lead: this is a clean, cancellation-free scalar carrier of the zeros. If any operator-theoretic object could be shown to *equal* `sigma_{1-s}(n)/zeta(s)` for one fixed `n`, its strip poles would be exactly the zeros. The campaign showed the prime-jump overlaps are not that object (L05-019), but the target is well-posed.
- Related: L05-012, L05-018, L05-019.

### L05-018 The global pole set is wrong without a completion
- Source: notes/yolo-lindblad/astra-structure.md:471, ledger 865
- Raised by: codex prover
- Status at last mention: CORRECTED (a constraint on all successors)
- Content: `sigma_{1-s}(n)/zeta(s)` also has a pole at `s = -2` (since `zeta(-2) = 0` while `sigma_3(n) > 0`), so "poles exactly the nontrivial zeros" is false globally for these functions. "Removing such poles requires an additional completion, not supplied by the prime jumps."
- Lead: the archimedean/Gamma factor is not decoration — it is what removes the trivial-zero poles. Any candidate must say where its completion comes from. Same point recurs in campaign Z (L05-084).
- Related: L05-017, L05-042, L05-084.

### L05-019 Shell values at 1 are not vacuum-to-shell jump overlaps
- Source: notes/yolo-lindblad/astra-structure.md:283-331, eqs (5.2)-(5.6), ledger 858-859
- Raised by: orchestrator drafted the identification; codex prover corrected it
- Status at last mention: CORRECTED (dead)
- Content: The draft hoped `c_b(1) = mu(b)` would be a vacuum-to-shell overlap of the dynamics, putting `1/zeta` in the numerator of a dynamical Dirichlet series. In fact `<b|V_n|1> = sqrt(phi(b)/n)[b|n] >= 0` — every overlap is nonnegative, e.g. `c_p(1) = -1` while `<p|V_p|1> = sqrt((p-1)/p) > 0` — and the exact overlap series is `sqrt(phi(b)) b^{-(s+1/2)} zeta(s+1/2)`, with zeta in the **numerator**. The true inverse relation is the Möbius inversion `c_b = sum_{d|b} mu(b/d) sqrt(d) V_d v`, an algebraic identity, not an evolution equation. Moreover point evaluation at the integer 1 is an unbounded functional even on `G` (the normalised unit-indicator over a finite prime set has norm one and value `prod (1-1/p)^{-1/2} -> infinity`), so the vector identity `C(s) = zeta(s)^{-1} sum_d d^{1/2-s} V_d v` cannot be evaluated at 1 by continuity.
- Lead: none as stated. The unboundedness of evaluation-at-1 is the structural reason the Ramanujan `1/zeta` cannot be a matrix element; a successor needs a *bounded* functional playing the role of "value at 1".
- Related: L05-011, L05-017.

### L05-020 At rates 1/p there is no normal cutoff limit at any positive time
- Source: notes/yolo-lindblad/astra-structure.md:15-27 (§0.1), 420-437 (§5.5), ledger 893
- Raised by: codex prover
- Status at last mention: CORRECTED (kills the guess as literally written)
- Content: With `lambda_p = 1/p`, `sum R_p^* R_p = (sum 1/p) I` has infinite quadratic form on every nonzero vector, so there is no densely defined no-jump operator. Worse, the natural finite-prime semigroups applied to `P_0` have **no trace-norm limit at any positive time**: every fixed shell diagonal entry obeys `<b|rho_F(t)|b> <= phi(b) exp[-t sum_{p in F, p∤b} (1-1/p)/p] -> 0`, and the vacuum survival is exactly `exp[-t sum_{p in F}(1-1/p)/p] -> 0`. Any trace-norm limit would be positive, trace one and have zero diagonal in a complete basis — a contradiction. Partial trace is trace-norm continuous, so adding a trace-preserving archimedean factor does not help.
- Lead: "Other limiting algebras or renormalizations require new definitions." Two are supplied: a summable-rate phase model, or the radial local model of L05-034.
- Related: L05-034, L05-048, L05-049.

### L05-021 The parity-closed ring trace is not an ordinary trace
- Source: notes/yolo-lindblad/astra-structure.md:439-445 (§5.6), ledger 894
- Raised by: codex prover
- Status at last mention: CORRECTED
- Content: On the infinite-dimensional doubled `G`, `L_F` is bounded so `e^{t L_F}` has bounded inverse `e^{-t L_F}` and therefore cannot be compact, let alone trace class; multiplying by the unitary `Gamma_b` cannot change that. So `Tr[Gamma_b e^{t L_F}]` is not an ordinary operator trace: "A finite prime cutoff alone is not a finite bond cutoff." A subtraction, distributional trace or other regularisation needs its own definition; parity supplies none.
- Lead: whatever "ring norm" means for an infinite bond has to be defined before it is computed. This is the same gap as L05-024 and L05-050.
- Related: L05-024, L05-049.

### L05-022 Prime periods as R_+ / p^Z from the idele-class stabiliser
- Source: notes/yolo-lindblad/astra-structure.md:505-515 (§6.3), ledger 871
- Raised by: orchestrator (S6 draft); proved elementarily by codex prover
- Status at last mention: PROVED
- Content: Let `x^(p)` be the adele-class point with component zero at `p` and one elsewhere. Its stabiliser in the idele class group is the image of `Q_p^x`; after quotienting the orbit by the compact norm kernel `K`, the norm coordinate is `R_+ / |Q_p^x|_p = R_+ / p^Z`, with logarithmic period `log p`. This is the precise sense in which prime periods `log p` occur. "Merely translating an auxiliary logarithmic line and inserting `Pi` performs none of these operations."
- Lead: the archimedean coordinate of the guess should be the norm coordinate of an *actual* adele-class orbit modulo the compact norm kernel, not a free line with `T_{log p}` on it. If that substitution were made honestly, the `log p` periods would be geometric rather than imposed.
- Related: L05-021, L05-023, L05-024.

### L05-023 Scope of the Connes 1999 trace formula citation
- Source: notes/yolo-lindblad/astra-structure.md:517-521 (§6.4), ledger 872
- Raised by: orchestrator asked for it, with "label anything from memory as UNVERIFIED-MEMORY"; codex prover verified it against the source
- Status at last mention: CORRECTED (scope narrowed); no UNVERIFIED-MEMORY remained
- Content: Connes's 1998 preprint (published 1999), *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, proves a local cutoff trace formula in §V Thm 3 and a finite-set-of-places formula in §VII Thm 4, using space and Fourier cutoffs and local principal-value terms; §VIII distinguishes the *global* trace-formula problem and its relation to RH. It does **not** provide an unconditional ordinary heat trace of anything like the proposed Lindbladian. arXiv: math/9811068, PDF pp. 2-3, 22, 31.
- Lead: none as a lead; recorded as the reference boundary — do not cite Connes 1999 as if the global formula were available.
- Related: L05-022, L05-024.

### L05-024 What an adelic identification would actually require (four missing ingredients)
- Source: notes/yolo-lindblad/astra-structure.md:523-525 (§6.5), ledger 873; repeated at 829
- Raised by: codex prover
- Status at last mention: OPEN
- Content: To identify a ring observable with the adelic orbit trace one needs (i) a specified quotient or correspondence, (ii) an intertwiner for the relevant actions, (iii) a test-function trace regularisation, and (iv) equality of the resulting distributions with all local normalisations. None is supplied by the guess, and "the geometric calculation of periods alone does not construct any of them."
- Lead: this is the concrete four-item checklist for the adelic route. Anyone reopening it should tick them in order.
- Related: L05-021, L05-022, L05-049.

### L05-025 A parity jump realises the -2gamma uniform decay exactly (S7)
- Source: notes/yolo-lindblad/astra-brief-A.md:71-76; notes/yolo-lindblad/astra-structure.md:529-544 (§7.1), ledger 875-876
- Raised by: orchestrator (Claude)
- Status at last mention: PROVED, but inapplicable to the unmodified guess
- Content: For `R = sqrt(gamma) Pi`, the dissipator is exactly `gamma(Gamma_b - I)`: zero on even operators, `-2gamma` on odd. So if a base generator preserves both sectors, adding it leaves the even part alone and subtracts `2gamma` from the odd spectrum. Likewise a finite abelian group of character-diagonal unitary jumps at total rate `gamma` damps every cross-character block at exactly rate `gamma` (eq. 7.2), verified numerically to `5.561e-17` over 13630 cross-character coherences. "This is why the computation does not apply to the unmodified prime guess" — there is no invariant sector to shift.
- Lead: choosing `2 gamma = 1/4` implements the critical-line rate in a *grading-preserving* model. The gap is that the model must first exist. See L05-030.
- Related: L05-004, L05-026, L05-030, L05-046.

### L05-026 Skew-adjointness, not formal skew-symmetry, is what forces a spectral line
- Source: notes/yolo-lindblad/astra-structure.md:546-558 (§7.2), ledger 874
- Raised by: codex prover
- Status at last mention: PROVED-CONDITIONAL (hypotheses H-INV, H-SA)
- Content: If the odd coherence space is invariant with a closed generator `T_odd = B - 2gamma`, and `B` is genuinely **skew-adjoint**, then `spec T_odd` lies on `Re = -2gamma` and `||e^{t T_odd} x|| = e^{-2gamma t}||x||`. The qualification is essential: on `L2(0,infty)`, `B = -d/dx` with domain `H^1_0` is closed and skew-*symmetric* but generates right shifts and its spectrum contains the whole left half-plane.
- Lead: every "the generator is anti-Hermitian so the spectrum is on a line" step anywhere in the programme must check domains, not just formal adjoints. That is the difference between an RH-shaped statement and nothing.
- Related: L05-025, L05-027, L05-028.

### L05-027 The exact finite-dimensional metric converse, and the Jordan obstruction
- Source: notes/yolo-lindblad/astra-structure.md:560-575 (§7.3), ledger 877
- Raised by: orchestrator asked for "the precise converse that would be needed"; codex prover supplied it
- Status at last mention: PROVED
- Content: For a finite matrix `T`: `T` is diagonalisable with every eigenvalue of real part `-2gamma` **iff** there is a positive-definite `M` with `B^* M + M B = 0`, `B = T + 2gamma`. The metric need not be the original Hilbert-Schmidt one. A spectral line alone is not enough: `T = -2gamma + [[i omega, 1],[0, i omega]]` has the right spectrum but a Jordan block, and its exponential has a term linear in `t`, impossible for any positive-definite metric.
- Lead: if the programme ever produces an odd generator with the right spectrum, the remaining work is exhibiting `M` — and diagonalisability must be checked separately.
- Related: L05-026, L05-028, L05-029.

### L05-028 The infinite-dimensional converse: Riesz basis, frequencies, maximal domain
- Source: notes/yolo-lindblad/astra-structure.md:577-589 (§7.4), ledger 878
- Raised by: codex prover
- Status at last mention: PROVED-CONDITIONAL (H-RIESZ, H-FREQ, H-DOM)
- Content: If normalised eigenvectors form a Riesz basis (uniform two-sided bounds `a, b`), eigenvalues are `-2gamma + i omega_j`, and the generator is the *maximal diagonal realisation* under the synthesis isomorphism, then `M = (S^{-1})^* S^{-1}` is bounded, positive, boundedly invertible, and the shifted generator is skew-adjoint in its metric. "A formal equality of quadratic forms on eigenvectors is not enough"; continuous spectrum would need a spectral representation instead of H-RIESZ.
- Lead: the Hilbert-Polya-shaped programme needs *uniform* Riesz bounds on the zero eigenvectors, and a domain statement. Those are the two hypotheses to attack next, not the eigenvalue list.
- Related: L05-027, L05-029.

### L05-029 The Gram condition number 10 -> 700 across 3000 zeros
- Source: notes/yolo-lindblad/astra-brief-A.md:76; notes/yolo-lindblad/astra-structure.md:591-597 (§7.5), ledger 879
- Raised by: earlier notebook observation, passed in by the orchestrator; analysed by codex prover under hypothesis H-GRAM
- Status at last mention: PROVED-CONDITIONAL — motivating, not decisive
- Content: For a Riesz basis, all Gram eigenvalues lie in `[a,b]`, so Gram condition numbers are uniformly bounded by `b/a`. The recorded growth from 10 to 700 is evidence that uniform bounds need investigation, "but two finite values do not prove divergence". If the numbers *do* diverge for normalised vectors, the candidate is not a Riesz basis and cannot be made an orthonormal eigenbasis by any bounded, boundedly invertible metric. Note the bookkeeping: the synthesis condition number is the square root of the Gram one (3.16 vs 26.46 here); other eigenvector scalings change finite optimisations but not the requirement of uniform bounds on *normalised* vectors.
- Lead: compute Gram condition numbers at 3000, 10000, 30000 zeros and fit the growth. Consequence either way: divergence kills the candidate Riesz basis (so kills that metric route to RH); boundedness would be strong positive evidence for it. This is a cheap, decisive numerical experiment that was flagged and not done.
- Related: L05-028, L05-030.

### L05-030 The forward RH implication and its missing premise
- Source: notes/yolo-lindblad/astra-structure.md:599-601 (§7.6), ledger 880
- Raised by: codex prover
- Status at last mention: OPEN
- Content: To get an RH implication one must (i) construct, *independently of zeros*, a grading-preserving generator; (ii) prove an arithmetic identification of its odd spectrum (or a determinant/trace identity), including multiplicities and possible cancellations; and then (iii) verify H-SA in the intended metric, or prove the bounded metric converse with its hypotheses. "S1-S6 do not establish the first step, and the supplied Gram observation does not establish the second."
- Lead: this three-step list is the cleanest statement in either campaign of what the whole programme still owes.
- Related: L05-004, L05-025, L05-028, L05-029.

### L05-031 Shell populations as a Markov chain b -> pb, and detailed balance (S8)
- Source: notes/yolo-lindblad/astra-brief-A.md:77-82; notes/yolo-lindblad/astra-structure.md:605-614 (§8.1), 627-653 (§8.3), ledger 881, 884-885; notes/yolo-lindblad/astra-finite-model.md:337-391
- Raised by: orchestrator (Claude)
- Status at last mention: CORRECTED twice over
- Content: Two separate errors. (a) The shell-diagonal algebra is not preserved: `J_p(|b><b|)` creates off-diagonal terms `sqrt(p-1)/p (|b><pb| + |pb><b|)`, and even the *pinched* chain has upward rate `lambda_p (p-1)/p` with a stay probability `1/p`, not the stated constant-rate chain. (b) The detailed-balance rate is backwards: with forward rate `u` and reverse `d`, the probability ratio on each edge is `u/d`, so Gibbs ratios `p^{-beta}` require `d = u p^beta`, not the drafted `u/p` — which would give ratio `p > 1` and no summable stationary law. And even with the corrected rates the quantum generator still creates coherences: the `(1,p)` entry of the shell Gibbs density has derivative `a c u w_0 (q-1)/(2q) != 0`. The finite model gives an exact rational counterexample on `B = {1,2}`, `p = 2`, `beta = 2`, with `L_db(rho_Gibbs)` having off-diagonal `27/160`.
- Lead: superseded by L05-047 (edge-resolved jumps do give the Gibbs fixed point) and L05-033 (the true reversible density is diagonal in *annuli*, not shells).
- Related: L05-032, L05-033, L05-047.

### L05-032 The annulus basis: the basis in which prime jumps really are occupation shifts
- Source: notes/yolo-lindblad/astra-structure.md:655-669 (§8.4), ledger 886
- Raised by: codex prover
- Status at last mention: PROVED (a genuine structural discovery, not asked for)
- Content: On the radial local space at `p`, the normalised annulus indicators `h_{p,k} = 1_{v_p(x)=k} / sqrt((1-1/p)p^{-k})` are an orthonormal basis, and `V_p h_{p,k} = h_{p,k+1}` exactly — a plain unilateral shift. The vacuum is *not* the occupation-zero vector but a geometric superposition `v_p = sqrt(1-1/p) sum_k p^{-k/2} h_{p,k}`. Consequently `G` is the incomplete Hilbert tensor product of the local radial spaces with reference vectors `v_p`, and a tensor product built on `h_{p,0}` instead is a genuinely *different* representation of the same infinitely many shifts — the reference overlaps `sqrt(1-1/p)` have vanishing product.
- Lead: this explains why the shell (`ell^2(N)` occupation) picture and the phase (Haar) picture keep disagreeing: "An abstract bijection between two countable orthonormal bases does not intertwine these infinitely many prime shifts and their selected vacua." Any future model must declare which reference vector it uses.
- Related: L05-033, L05-034, L05-035, L05-036.

### L05-033 The true one-prime reversible density, with a uniqueness proof
- Source: notes/yolo-lindblad/astra-structure.md:671-687 (§8.5)
- Raised by: codex prover
- Status at last mention: PROVED
- Content: With `S h_k = h_{k+1}` and `0 < q = u/d < 1`, the unique normal stationary density of `u D_S + d D_{S^*}` is `sigma_p = (1-q) sum_k q^k |h_{p,k}><h_{p,k}|`. Uniqueness includes coherences: for offset `r >= 1` the interior characteristic roots are 1 and `q`, compactness forces `x_j = C q^j`, and the boundary equation `d x_1 - (u + d/2) x_0 = 0` then forces `C = 0`. "This reversible state is diagonal in annuli, not in the Ramanujan shells."
- Lead: use annuli, not shells, as the diagonal basis of any reversible prime dynamics.
- Related: L05-032, L05-034.

### L05-034 The corrected critical reversible dynamics, whose valuation law IS Haar's
- Source: notes/yolo-lindblad/astra-structure.md:689-714 (§8.6), eqs (8.9)-(8.10), ledger 887
- Raised by: codex prover
- Status at last mention: PROVED (positive), with a sharp caveat
- Content: On the *radial local algebra* (norm closure of finite tensor products of local radial `B(G_p)`), take at each prime two jumps with `d_p = u_p p^beta`, and the product of the states (8.8). This is a well-defined strongly continuous dynamics without any summability of rates, because a local observable feels only finitely many radial generators. At `beta = 1`, `u_p = 1/p`, `d_p = 1` the stationary product state's valuation distribution is `prod_p ((1-1/p)p^{-k})_{k>=0}` — **exactly the valuation distribution of Haar measure on Zhat**. So on the radial multiplication algebra it agrees with the critical phase state. The caveat, also proved: this product state has **no normal extension to B(G) for any beta > 0** (the reference-projection expectations `a_p <= 1-1/p` have vanishing product while normality demands `Tr(rho P_F) -> 1`).
- Lead: this is the best replacement so far for the guess's "critical KMS fixed point": a precisely defined critical reversible dynamics that reproduces Haar. The next step is to ask what its *ring norm* or transfer spectrum is on this algebra, since its density is non-normal and so no naive trace is available. Consequence if it worked: a genuine algebraic critical fixed point for the BC reframe priority.
- Related: L05-010, L05-032, L05-036, L05-049.

### L05-035 The occupation Gibbs weight at beta = 1 is a semifinite weight, and a KMS obstruction
- Source: notes/yolo-lindblad/astra-structure.md:716-741 (§8.7), ledger 883, 888
- Raised by: orchestrator asked for the comparison with shard 04c; codex prover proved it
- Status at last mention: PROVED-CONDITIONAL (H-OCC, H-DB, H-RATES) and PROVED (KMS part)
- Content: In the occupation model `S_p |n> = |pn>` with `d_p = u_p p^beta`, `W_beta = diag(n^{-beta})` is stationary term by term. For `beta > 1` it normalises to a density; at `beta = 1` it defines instead a normal faithful semifinite *weight* `Phi_1(A) = sum_n (1/n)<n|A|n>` with `Phi_1(I) = infinity`, invariant under the Heisenberg semigroup (justified by monotone cutoffs, avoiding signed infinities). Separately, for the occupation energy `H|n> = (log n)|n>`, the KMS identity on matrix units forces `m^beta rho_mm = n^beta rho_nn`, so any normal beta-KMS density is a multiple of `W_beta` and cannot be normalised at `beta = 1`.
- Lead: at criticality the right object is a *weight*, not a state. That reframing should propagate to the rest of the programme.
- Related: L05-034, L05-036.

### L05-036 The completed occupation boundary: at beta = 1 infinitely many primes are occupied
- Source: notes/yolo-lindblad/astra-structure.md:743-756 (§8.8), ledger 889
- Raised by: orchestrator asked "what stationary object exists at beta=1 (a weight, a boundary condition at b -> infinity)"; codex prover answered
- Status at last mention: PROVED
- Content: `nu_beta = (x)_p (1-p^{-beta}) p^{-k beta}` is a genuine probability on `prod_p N_0` for every `beta > 0`. For `beta > 1` only finitely many coordinates are nonzero almost surely, and the mass on integer `n` is `n^{-beta}/zeta(beta)`. For `0 < beta <= 1` the divergence of `sum p^{-beta}` makes finite-support configurations have probability *zero*: the critical law is supported on configurations with infinitely many occupied primes. Uniqueness of the stationary law is proved without assuming independence (strict Jensen on `sqrt(1+h^2)` plus positivity of transition entries). "It is not an unspecified boundary condition at a single point called infinity."
- Lead: this is the concrete answer to "what is at `b -> infinity`". Consequence: the critical object lives on a *completed* configuration space (supernatural numbers / infinitely many occupied primes), which is where any critical transfer semigroup should be defined. Warning recorded: "The unnormalized occupation weight, the completed product probability, and Haar on the phase algebra must not be conflated, even though some restricted formulas agree."
- Related: L05-034, L05-035.

### L05-037 Forward phase dynamics converge to delta_0, not Haar; singular stationary states exist
- Source: notes/yolo-lindblad/astra-structure.md:616-625 (§8.2), 758-765 (§8.9), ledger 882, 890
- Raised by: codex prover
- Status at last mention: CORRECTED (dead route for "forward dynamics select the critical state")
- Content: For any finite or summable positive rates the forward jumps have **no** normal stationary density (valuation projections `E_{p,k}` satisfy `L^*(E_{p,k}) = lambda_p(E_{p,k-1} - E_{p,k})`, forcing all `a_k = 0`). Classically the Heisenberg action is random multiplication; every prime exponent tends to infinity, so every initial phase probability converges weak-* to `delta_0`, whose phase restriction is *not* Haar (`delta_0(c_b) = phi(b)`). Stationary *singular* states on `B(G)` do exist, by weak-* cluster points of time averages — an existence proof, not uniqueness, and no BC identification.
- Lead: "No uniquely selected normal critical KMS fixed point follows." A successor wanting Haar as the fixed point needs reverse jumps (L05-034), not forward ones.
- Related: L05-020, L05-034.

### L05-038 Vacuum coherences: projected decay, but conserved observables forbid full decay
- Source: notes/yolo-lindblad/astra-structure.md:767-806 (§8.10), eqs (8.13)-(8.17), ledger 891
- Raised by: orchestrator asked "whether the vacuum coherences |1><b| decay or are absorbing"; codex prover answered both ways
- Status at last mention: CORRECTED (the draft's dichotomy was false)
- Content: The projection back onto vacuum coherences does decay: `||P_0 e^{tL}(X_b) P_-||_1 <= exp[-t sum_p lambda_p(1 - p^{-1/2})]`. But the *full* operator cannot decay, because every `V_n` is a conserved Heisenberg observable (`J_p^*(V_n) = V_p^* V_p V_n = V_n`), giving `||e^{tL} X_b||_1 >= |<b|V_b|1>| = sqrt(phi(b)/b) > 0`. So information leaves the block rather than vanishing, and the vacuum population is not absorbing either (2.4 shows it emits immediately).
- Lead: the conserved family `{V_n}` is an unexploited structure — a commutative family of fixed Heisenberg observables of the forward dynamics, indexed by the integers. Worth asking what algebra it generates and what its joint spectrum is.
- Related: L05-012, L05-039, L05-040.

### L05-039 An abstract absorbing-vacuum channel built from any contraction semigroup
- Source: notes/yolo-lindblad/astra-structure.md:808-821 (§8.11), ledger 892
- Raised by: orchestrator asked to "Compare with the vacuum-decay Lindbladian of shard 04c"; codex prover built a zero-free comparison
- Status at last mention: PROVED-CONDITIONAL (H-CONTRACTION)
- Content: For *any* strongly continuous contraction semigroup `Z_t -> 0` on a Hilbert space `K`, the map `E_t(rho) = A_t rho A_t^* + Tr[(I - Z_t^* Z_t) rho_{--}] P_0` with `A_t = 1 (+) Z_t` is a CPTP semigroup on `C v (+) K` with `P_0` the unique stationary density and coherences `|v><g| -> |v><Z_t g|` decaying in trace norm. This reproduces the qualitative behaviour of shard 04c's vacuum-decay Lindbladian **without importing the zero-built model space**.
- Lead: use this as the template for any "absorbing critical vacuum" claim; it shows the behaviour is generic and therefore carries no arithmetic content by itself. "Substituting a semigroup already specified by zeta zeros would not solve the present brief."
- Related: L05-038, L05-040.

### L05-040 A single forward prime has a full spectral disk, not isolated real modes
- Source: notes/yolo-lindblad/astra-structure.md:413-418, ledger 862
- Raised by: codex prover (correcting an inherited identification)
- Status at last mention: CORRECTED
- Content: `spec L_{p} = {lambda_p(z-1) : |z| <= 1}` in Hilbert-Schmidt norm — a disk, not a discrete real set. The elementary proof uses the annulus operators `F_k = |h_k><h_k|`: they are HS-orthonormal with `J_p F_k = F_{k+1}`, a unilateral shift, so every `|z| < 1` is an eigenvalue of `J_p^*`. This does not contradict the real spectrum of the *different*, reversible occupation chain of shard 04c.
- Lead: recorded as a warning: the forward phase model and the reversible occupation model of 04c are not the same operator and must not be quoted interchangeably.
- Related: L05-032, L05-039.

### L05-041 The archimedean Hamiltonian D = x d/dx + 1/2 needs a measure and a factor of i
- Source: notes/yolo-lindblad/astra-brief-A.md:29; notes/yolo-lindblad/astra-structure.md:29-39 (§0.2), ledger 895
- Raised by: orchestrator; corrected by codex prover
- Status at last mention: CORRECTED (a bookkeeping fix, not fatal)
- Content: On `L2(R_+, dx)` the log transform `(Wf)(y) = e^{y/2} f(e^y)` takes the closure of `x d/dx + 1/2` to `d/dy` on `H^1(R)`, i.e. to multiplication by `i xi` — so `D^* = -D` and it is `H = -i D`, not `D`, that is self-adjoint. On multiplicative Haar `dx/x` the skew-adjoint generator is `x d/dx` without the `1/2`, and `T_u f(x) = f(e^{-u} x)`.
- Lead: fix the measure convention once, in the shared definitions, so the `1/2` shift is never accidentally doubled or dropped. It is exactly the sort of factor that would move a "critical line at 1/2" claim.
- Related: L05-001, L05-042.

### L05-042 The Gamma-factor oscillator ladder was never specified
- Source: notes/yolo-lindblad/astra-brief-A.md:27-28; notes/yolo-lindblad/astra-brief-B.md:32-33; notes/yolo-lindblad/astra-structure.md:41-43 (§0.3), ledger 896; notes/yolo-lindblad/astra-finite-model.md:54 ("No harmonic oscillator or archimedean Hamiltonian is added")
- Raised by: orchestrator (Claude)
- Status at last mention: raised, not pursued — OPEN in both lanes
- Content: The guess includes "the Gamma-factor (harmonic-oscillator) ladder on `L2(R_+^*)`" but never gives its jump operators, rates, grading, domains or trace prescription. The audit notes that "An oscillator heat trace and a Lindblad transfer trace are different objects", and that the cMPS parameter `t` and the auxiliary logarithmic coordinate must be distinguished until an identification is constructed. Crucially: any trace-preserving archimedean-only addition leaves the phase marginal unchanged, so it cannot cure the phase cutoff obstruction. Brief B offered an explicit implementation (`T_{log p} = exp(log p (a - a^+))` on `k = 0..K` levels, or a grid shift) which was not built.
- Lead: this is the completion factor (see L05-018: trivial-zero poles need a completion). It is the one piece of the guess never tested, and it is also the only piece that could supply the missing archimedean structure. Building the truncated-oscillator version from brief B:32-33 is a concrete unexecuted next step.
- Related: L05-018, L05-041, L05-050.

### L05-043 The zero hunt: exact vacuum resolvents, and where their poles actually are
- Source: notes/yolo-lindblad/astra-brief-B.md:45-52 (N4); notes/yolo-lindblad/astra-finite-model.md:196-285
- Raised by: orchestrator designed the hunt; codex prover executed it
- Status at last mention: pursued, clean negative
- Content: With `z = s + beta + 1`, the ordered-word vacuum resolvent is exactly `F(s) = 1/(1 - S_P(z))` where `S_P(z) = sum_{p<=P} p^{-z}`, and the multiset one is exactly `F_E(s) = zeta_P(s + beta + 1)` — a **shifted** partial zeta. Pole exclusion in the target rectangle is analytic, not a failed root search: the diagonal of `K(s)` at shell pair `(b,c)` is `sum_{p∤bc} p^{-z}`, bounded by `S_P(beta+1.3) < 1` uniformly in `P`, and triangularity then excludes every pole. Argument-principle windings on the rectangle boundary (steps 0.04 and 0.02, plus a 19x401 interior mesh, targets `b = 1,2,4,6,12,30,210`) give zero winding everywhere. No pole moves toward `s = 1`: `F(1)` creeps from 1.2049 to 1.2117 as `P` goes 5 to 47. "The shift by `beta+1` follows from the rate and the two vacuum amplitudes; it cannot be discarded."
- Lead: the shift `beta + 1` is the diagnosis — the rate `p^{-beta}` and the two vacuum amplitudes each contribute. A successor model wanting the pole at `s = 1` must have amplitudes that do not produce this shift.
- Related: L05-011, L05-012, L05-013, L05-044.

### L05-044 Warning: a shrinking ratio F/(1/zeta_P) is not evidence of a hidden 1/zeta factor
- Source: notes/yolo-lindblad/astra-finite-model.md:267-283
- Raised by: codex prover (correcting a tempting reading of its own table)
- Status at last mention: recorded as a methodological warning
- Content: The requested ratio is exactly `zeta_P(s)/(1 - S_P(s+beta+1))`, whose modulus at `1/2 + i gamma_1` falls from 0.224 (P=5) to 0.082 (P=47). That decrease is *not* extraction of a reciprocal-zeta factor: it multiplies a regular constructed `F` by a partial Euler product evaluated **outside** its half-plane of absolute convergence, and such products give no justified approximation to the continued `zeta(s)` in the strip.
- Lead: none; a guard against a very natural numerical self-deception in this programme. The same guard appears at L05-015.
- Related: L05-015, L05-043.

### L05-045 The continuous-time spectrum is a spread of real rates, not a vertical line
- Source: notes/yolo-lindblad/astra-brief-B.md:53-57 (N5); notes/yolo-lindblad/astra-finite-model.md:287-335
- Raised by: orchestrator asked "whether any structure (uniform real part, line) emerges"; codex prover answered
- Status at last mention: pursued, negative
- Content: The full finite doubled `T` is triangular with eigenvalues `-Lambda_P + sum_{p∤bc} p^{-beta-1}`, all real by construction (imaginary parts are exactly zero, not rounded). At `Bmax = 3072, beta = 1, P = 47` the odd compression's real parts spread over `[-1.643, -1.213]` with 397 distinct values. So the model gives real decay parameters with a *spread*, not relaxation frequencies on a line — and the chosen parity sector is not invariant anyway.
- Lead: frequencies must come from somewhere else (a Hamiltonian, or the archimedean factor). A purely dissipative commuting-jump phase model is spectrally real and cannot produce `i gamma_n`.
- Related: L05-004, L05-042, L05-046.

### L05-046 Galois dephasing: exact uniform shift, but no frequencies and no effect on the trivial sector
- Source: notes/yolo-lindblad/astra-brief-B.md:56-57; notes/yolo-lindblad/astra-finite-model.md:322-335
- Raised by: orchestrator; verified by codex prover
- Status at last mention: PROVED, and shown irrelevant to the hunt
- Content: Averaging `Ad(U_a)` over `a in (Z/120)^x` at total rate `gamma` gives exactly `0` on same-character coherences and `-gamma` on cross-character ones (max coefficient error `5.561e-17` over 770 + 13630 coherences). Character *equality* means equality as characters of the common group, not equality of modulus labels. The phase compressions preserve character sectors (leakage `4.036e-16`), so the shift is genuine — but it "cannot generate frequencies and cannot alter this Galois-trivial hunt", since the whole hunt lives in the Galois-trivial sector where all `U_a = I`.
- Lead: the dephasing mechanism is real but is orthogonal to where the zeta data is. Any RH-as-dephasing story needs the zeta data to live in a *non*-trivial character sector.
- Related: L05-006, L05-025, L05-045.

### L05-047 The repaired edge-resolved model that does have the Gibbs fixed point
- Source: notes/yolo-lindblad/astra-finite-model.md:377
- Raised by: codex prover (constructive repair, offered unprompted)
- Status at last mention: PROVED, but "they change the model"
- Content: Resolve each shell edge into its own jump `A_{p,b} = |pb><b|`, with rates `lambda_p p^{-beta}` upward and `lambda_p` downward. Then every edge obeys `w_{pb} = p^{-beta} w_b`, each separate dissipator preserves diagonal densities, and `b^{-beta}/Z_B` is verified stationary. Caveat recorded: with finitely many primes on a contiguous cutoff, disconnected components give additional stationary densities, so uniqueness is not asserted.
- Lead: if the programme wants shell Gibbs weights as a fixed point, this is the model that delivers them — at the cost of one jump per edge instead of one per prime, i.e. losing the "letters are primes" reading. That trade-off is worth an explicit decision.
- Related: L05-031, L05-033.

### L05-048 The divergence of sum 1/p is the real obstruction, and needs its own fix
- Source: notes/yolo-lindblad/astra-structure.md:25-27; notes/yolo-lindblad/astra-finite-model.md:335
- Raised by: codex prover
- Status at last mention: recorded constraint
- Content: At `beta = 1` the finite-cutoff statements do not define an unrestricted infinite-prime generator because `sum_p 1/p` diverges; "a domain or renormalization would need separate justification". The audit even reproves the divergence without prime asymptotics (if it converged, `prod (1-1/p)^{-1}` would be finite by `-log(1-u) <= 2u`, contradicting the harmonic partial sums).
- Lead: the critical rate `lambda_p = 1/p` is exactly the divergent one. Either renormalise (subtract `log log P`?), or move to the radial local algebra of L05-034 where summability is not needed. This is stated but no renormalisation was attempted.
- Related: L05-020, L05-034.

### L05-049 The audit's own "concrete next computations"
- Source: notes/yolo-lindblad/astra-structure.md:828-829
- Raised by: codex prover
- Status at last mention: OPEN (a to-do list, none done)
- Content: Four steps, in order. (1) *Select the algebra and the limiting dynamics* — either a summable-rate phase model or the radial local model of §8.6. (2) At a finite bond cutoff, explicitly record any changed isometry relations and test grading invariance, complete positivity, and the stationary density. (3) Compare the three actual generating functions — word resolvent, Poisson evolution, multiset inverse — using eqs (5.10)-(5.14) as exact controls, with the warning that "matching an arithmetic scalar after a changed functional must not be called a spectral realization". (4) An adelic route needs its quotient, intertwiner and regularised trace before one can ask for a metric making its odd generator skew-adjoint.
- Lead: this is the campaign's own hand-off list and no shard has taken it up.
- Related: L05-020, L05-024, L05-034, L05-050.

### L05-050 What remains undecided after the negative audit
- Source: notes/yolo-lindblad/astra-finite-model.md:403; notes/yolo-lindblad/astra-structure.md:473-475
- Raised by: codex prover
- Status at last mention: OPEN (explicitly the "what survived" line)
- Content: Verbatim: "An additional archimedean operator, different boundary functional, or justified infinite-domain construction remains undecided; none was inserted here." Those are exactly three live directions the negative result does *not* close: (i) an extra archimedean operator (the unbuilt Gamma ladder), (ii) a different boundary functional (a parity insertion changes the functional, not the multiplicities — so which functional?), (iii) a justified infinite-domain construction (the missing operator-norm continuation of `A(w)`).
- Lead: each of the three is a named, separable research task. (ii) in particular is cheap: enumerate candidate boundary functionals on the word expansion and see which produces multiset rather than word multiplicities.
- Related: L05-012, L05-013, L05-042, L05-049.

---

### L05-051 TJO's framing request for campaign Z
- Source: notes/zeta-conditions/astra-brief.md:15-18
- Raised by: TJO (verbatim)
- Status at last mention: executed (shard 06h registered)
- Content: Verbatim: "line up all the conditions we want a zeta to obey: functional equation, rh/ramanujan, unique fixed point etc etc and try to impose them factor by factor on the cMPS ring norm. I suppose it makes sense to include tiny L functions etc. ... I want to see completely concrete MPS/cMPS that any practitioner would understand that yield interesting zeta data." This is the origin of the whole condition ledger C1-C10 and the thirteen example scripts.
- Lead: the "factor by factor" method itself — impose one zeta condition at a time on an explicit tensor and see which force each other. The campaign's closing verdict on the method is at L05-083.
- Related: all of L05-052 … L05-084.

### L05-052 C1 — positivity is automatic, integrality is not
- Source: notes/zeta-conditions/astra-brief.md:36-37; notes/zeta-conditions/astra-constructions.md:21-29
- Raised by: orchestrator (Claude); sharpened by codex prover
- Status at last mention: settled
- Content: `N_n = Tr(Gamma E^n) = sum_{w} |Tr(Pi A_w)|^2 >= 0` automatically for a parity-closed (Ramond) ring; integrality is a separate arithmetic constraint. For cMPS `N(L) = Tr(Gamma exp(LT)) >= 0` automatically for every `L > 0`, but **integrality at arbitrary real lengths is not a useful requirement** — continuity would make an integer-valued function constant. The prover also insists on distinguishing three things that the programme keeps mixing: a physical ring **norm**, a ring **amplitude** `str F^n`, and an open-chain **sum of amplitudes**; a one-letter amplitude model with letter `F` has physical norm `|Tr(Pi F^n)|^2`, not `Tr(Pi F^n)`.
- Lead: the norm/amplitude/open-sum trichotomy is the single most-used correction in campaign Z; it recurs at L05-065, L05-068, L05-070.
- Related: L05-053, L05-065, L05-070.

### L05-053 C2 — a genuine bosonic gas, and its continuous-length version
- Source: notes/zeta-conditions/astra-brief.md:38; notes/zeta-conditions/astra-constructions.md:31-48
- Raised by: orchestrator; the continuum version and the no-go are the prover's
- Status at last mention: settled, with a new no-go
- Content: The lattice condition is `a_d = (1/d) sum_{e|d} mu(d/e) Tr(Gamma E^e) in Z_{>=0}`. Positivity of all ring norms does **not** imply it: the single letter `diag(1,-1)` with the same parity has `N = (4,0,4,0,4,0)` and `a_2 = -2`. For continuous `L` there is no intrinsic `a_d` at all; the prover formulates the right continuous condition as a locally finite positive prime measure `nu = sum_p m_p delta_{l_p}` with `N(L) dL = sum_{p,k} m_p l_p delta_{k l_p}(dL)` and `-d/dz log Z(z) = int e^{-zL} N(L) dL`. Then: **a nonzero finite-dimensional constant cMPS has analytic `N(L)` and cannot equal that atomic comb as a measure.**
- Lead: this is a clean no-go for "a finite cMPS is a prime gas". Any continuum prime gas needs either an infinite bond or a non-constant / singular generator. Sampling at interval `h` is an additional choice and generally gives nonintegral exponents.
- Related: L05-062, L05-082, L05-083.

### L05-054 C3 — rationality and degree bookkeeping; a cMPS zero mode is NOT invisible
- Source: notes/zeta-conditions/astra-brief.md:39-40; notes/zeta-conditions/astra-constructions.md:50-61
- Raised by: orchestrator; the cMPS asymmetry is the prover's correction
- Status at last mention: CORRECTED
- Content: `Z(u) = det(1-uE_-)/det(1-uE_+)` and `Zcal(z) = det(z-T_-)/det(z-T_+)`; net multiplicity `m_+(lambda) - m_-(lambda)` gives a pole (positive) or zero (negative). On the lattice, zero eigenvalues and nilpotent blocks are invisible to every positive power. **For cMPS a zero eigenvalue is not invisible**: it contributes a constant to `N(L)` and a factor `z` to the determinant, and the degree gap is `(D_+ - D_-)^2 = N(0) = |Tr Pi|^2`. "'Support' must never be used to discard a cMPS zero mode merely because it is zero."
- Lead: the identity `(D_+ - D_-)^2 = N(0) = |Tr Pi|^2` ties the superdimension of the bond to the vacuum norm — a small structural handle worth remembering when designing bonds.
- Related: L05-062, L05-078.

### L05-055 C4 — the functional equation as a net-divisor symmetry, and a bond duality J
- Source: notes/zeta-conditions/astra-brief.md:41-45; notes/zeta-conditions/astra-constructions.md:63-74
- Raised by: orchestrator; made exact by codex prover
- Status at last mention: settled
- Content: The exact condition is parity-preserving multiplicity invariance of the **reduced, nonzero net** spectrum under `lambda -> q/lambda`; then `Z(1/(qu)) = ± q^{chi/2} u^chi Z(u)` with `chi = d_+ - d_-` (`= 2-2g` in curve normal form), using `(sdet E)^2 = q^chi`. A sufficient *operator* equation is `J Gamma = Gamma J`, `J E J^{-1} = q E^{-1}` on an invariant invertible support — but spectral invariance alone need not provide such a `J` unless Jordan structures also match. For cMPS the natural symmetry is **additive**, `lambda -> kappa - lambda`, or `J T J^{-1} = kappa - T`, giving `Zcal(kappa - z) = (-1)^chi Zcal(z)`; "Multiplicative `lambda -> q/lambda` is not the natural symmetry of a generator."
- Lead: the multiplicative/additive distinction is the right way to carry the FE from lattice to continuum, and the FE cMPS example (L05-079) realises it concretely with `kappa = 2`.
- Related: L05-056, L05-079.

### L05-056 C4 correction — inverse-paired letters do NOT give the FE for a raw doubled sum
- Source: notes/zeta-conditions/astra-brief.md:91-93 (D4); notes/zeta-conditions/astra-constructions.md:76-78, 357
- Raised by: orchestrator drafted it from shard 08b; codex prover refuted it
- Status at last mention: CORRECTED with an exact counterexample (dead as stated)
- Content: The draft read shard 08b as saying that letters closed under `B -> B^{-1}` give the functional equation. They do for 08b's **non-backtracking / Hashimoto** construction after the specified trivial factors are removed — not for a general raw doubled sum. Counterexample: `B = diag(1,2)`, `B^{-1} = diag(1,1/2)` give even spectrum `{2, 17/4}` and odd spectrum `{5/2, 5/2}`; the even pair fixes `q = 17/2` and the odd pair fails it. Separately: an adjoint-closed Kraus family makes the **raw channel** Hilbert-Schmidt self-adjoint (hence real eigenvalues), but "Reality of coefficients, reality of eigenvalues, and a reciprocal FE are different assertions", and in the non-backtracking case it is `sum Ad(B_i)` that becomes self-adjoint, not the Hashimoto matrix.
- Lead: the *correct* inverse-pairing mechanism was then found — see L05-074 (the reversal/no-backtracking identity forcing `q = 3` in the Bass quadratics).
- Related: L05-074, L05-055.

### L05-057 C5 — RH/Ramanujan as a metric condition, plus a finite Weil criterion
- Source: notes/zeta-conditions/astra-brief.md:46-50; notes/zeta-conditions/astra-constructions.md:80-88
- Raised by: orchestrator; exact forms by codex prover
- Status at last mention: settled
- Content: Lattice: `|lambda|^2 = q` for every retained odd eigenvalue; a sufficient **visible mechanism** is a positive metric `M` with `E_-^† M E_- = q M`, which is also necessary if the retained odd matrix is semisimple. cMPS: replace the circle by `Re lambda = kappa/2`, with the metric condition `T_-^† M + M T_- = kappa M`. Separately, shard 08b's finite Weil criterion: set `nu_n = sum (lambda/sqrt q)^n`, `nu_{-n} = conj(nu_n)`, and require every finite Toeplitz matrix `(nu_{j-k})` to be positive semidefinite — this gives `|lambda| <= sqrt q`, and reciprocal closure upgrades it to equality. The prover also gives the **continuous-time Weil criterion**: use `nu(t) = sum exp((lambda - kappa/2)t)` for `t >= 0`, extend by conjugate reflection, and impose positive definiteness of every kernel matrix `(nu(t_j - t_k))`; then `Re lambda <= kappa/2`, with equality under additive reflection.
- Lead: the continuous-time Weil kernel condition is stated once and never used. It is exactly the object the cMPS side of the programme needs — a Weil positivity criterion for a *generator* rather than a transfer matrix.
- Related: L05-055, L05-079, L05-084.

### L05-058 A CPTP tensor with FE and a unique fixed point where RH fails
- Source: notes/zeta-conditions/astra-constructions.md:88, 302-317; evidence lines 1019-1031
- Raised by: codex prover (answering "give one where RH fails by a visible mechanism")
- Status at last mention: PROVED
- Content: `independence.py` prints an actual Kraus family with poles `{1, 1/16}` and odd eigenvalues `{8, 2}`: FE holds, a unique stationary state exists, RH fails. Its printed 2x2 Weil minor has a vector with quadratic value `-1`. The unequal moduli give unequal transfer decay lengths; replacing `{8,2}` by `{4,4}` restores RH via an odd block equal to `4 I`. "This is an actual Kraus variation, not a list of independently assigned roots."
- Lead: the takeaway for the whole programme is at the end of the report: "positivity of norms and an FE do not force RH: the explicit off-circle CPTP tensor disproves that shortcut." Any argument of the shape "positivity + FE => RH" is refuted by an explicit two-by-two example.
- Related: L05-057, L05-077, L05-084.

### L05-059 C6 — three requirements that the draft conflated
- Source: notes/zeta-conditions/astra-brief.md:51-53, 99-103 (D6); notes/zeta-conditions/astra-constructions.md:90-102, 359
- Raised by: orchestrator drafted; codex prover separated them
- Status at last mention: CORRECTED
- Content: "Unique fixed point" is three different things. (1) *Spectral pole*: the Perron eigenvalue `q > 0` of the even transfer is algebraically simple and uncancelled. (2) *A channel on the specified bond*: there is a strictly positive even `h` with `E^†(h) = q h`, so `B_s = q^{-1/2} h^{1/2} A_s h^{-1/2}` is TP; a **singular** `h` gives only a restriction, not a gauge on the whole bond. (3) *Stationarity / mixing*: a one-dimensional fixed space generated by a density matrix — and convergence additionally needs all other eigenvalues of modulus `< 1`, since uniqueness alone permits periodicity (a bit-flip channel is printed as witness). The stronger "even spectrum is exactly `{1, q}`" is named **C6projective**.
- Lead: whenever the notebook says "unique fixed point", say which of the three is meant. Also recorded: `H^0` is *not* a second decoupled block — in the TP curve tensors its eigenvalue 1 is a decaying population-difference eigenoperator.
- Related: L05-066, L05-077.

### L05-060 C7 — character factorisation is representation theory; calling it Artin needs a cover
- Source: notes/zeta-conditions/astra-brief.md:54-67; notes/zeta-conditions/astra-constructions.md:104-118
- Raised by: orchestrator; sharpened by codex prover
- Status at last mention: settled, with three warnings
- Content: With `U_g Pi = Pi U_g` and `U_g A_s U_g^{-1} = sum_t v_g(t,s) A_t`, `D_g = U_g (x) conj(U_g)` commutes with `E, Gamma`, and `N_n^chi = (1/dim chi) Tr(P_chi Gamma E^n)`, `L(u,chi) = 1/sdet(1 - u E_chi)`, `Z = prod_chi L^{dim chi}`. Three warnings: (a) to call the factors **Artin** one must identify an actual cover and its monodromy/Frobenius weights on primitive orbits — "A symmetry with fixed letters does not alone do this"; (b) a character factor need not be real or positive, and FE pairs `chi` with its contragredient so an individual complex character need not have a self-reciprocal divisor; (c) "even = trivial character, odd = nontrivial" is *additional geometric information*, not a theorem about all group actions — in the Ihara cover **every** physical norm mode is even, sign-character modes included.
- Lead: the notebook's "even = trivial, odd = nontrivial" pattern is geometric (Artin-Schreier cohomology) and must be re-derived, not assumed, for each new group action.
- Related: L05-069, L05-070, L05-074.

### L05-061 C8 — the minus sign lives in the mixed (+,-) coherences, not the odd ket population
- Source: notes/zeta-conditions/astra-brief.md:68; notes/zeta-conditions/astra-constructions.md:120-122
- Raised by: orchestrator; sharpened by codex prover
- Status at last mention: settled
- Content: Zeros have negative net **doubled** multiplicity and poles positive, automatically once homogeneous data and parity closure are fixed. The crucial point: "The mixed `(+,-)` and `(-,+)` coherences supply the minus sign, not the odd ket population." An untwisted closure uses the ordinary trace and has *no* finite determinant zeros; and separating letters by ket parity kills the lattice cross transfer and removes the zeros (as in shard 03b). In amplitude-only character examples the odd grading is a trace convention, not an established norm factorisation.
- Lead: consistent with shard 03b's "the sign lives in even-odd coherences". Any tensor designed so that letters do not move between parities will have no zeros at all — a useful design rule stated negatively.
- Related: L05-014, L05-062, L05-082.

### L05-062 C9/C10 — realisability, kinetic regularity, and when a lattice channel has a cMPS
- Source: notes/zeta-conditions/astra-brief.md:69-74; notes/zeta-conditions/astra-constructions.md:124-138
- Raised by: orchestrator; the exact tests are the prover's
- Status at last mention: settled, with two no-gos
- Content: C9: the finite test is a positive semidefinite Choi matrix for the channel plus parity covariance; factoring each parity block gives homogeneous Kraus letters. A **literal count state** additionally needs `Tr(Pi A_w) in {0,1}` — the curve tensors are only *weighted* norm realisations and their words do not label curve points one for one (already explicit in shard 06d). For cMPS, "regular" in the finite-kinetic-energy sense requires `R_a R_b = (-1)^{p_a p_b} R_b R_a`, so a fermionic species has `R_a^2 = 0`; a cMPS can be finite-norm and CPTP while failing kinetic regularity. C10: an exact cMPS embedding needs `E = exp(hT)` with Choi conditional positivity and the parity/regularity constraints — **a matrix logarithm is not enough, and a singular `E` cannot be such an exponential at positive time** (so the affine four-letter tensor, which has a zero eigenvalue, has no exact full-transfer embedding).
- Lead: "singular E has no exponential" is a small, sharp, reusable obstruction to continuum-ising lattice examples.
- Related: L05-063, L05-078, L05-079.

### L05-063 Poissonisation as the universal weak continuum construction
- Source: notes/zeta-conditions/astra-constructions.md:136
- Raised by: codex prover
- Status at last mention: PROVED, deliberately downplayed
- Content: For any lattice letters, take `Q = -c/2`, `R_s = A_s`, giving `T = E - c` and `N(L) = e^{-cL} sum_{n>=0} N_n L^n/n!` with `N_0 = (Tr Pi)^2`; it is TP if `sum A_s^† A_s = c`. "The `n=0` term and all zero modes matter. It normally changes the FE/RH and may fail kinetic regularity. No claim is made that the Horner characters or graph cover acquire an arithmetic continuum interpretation under this operation."
- Lead: a universal but lossy bridge from lattice to continuum. Worth knowing it always exists; worth not over-reading it.
- Related: L05-062, L05-069, L05-074.

### L05-064 What "incommensurable prime lengths" would actually mean
- Source: notes/zeta-conditions/astra-brief.md:74; notes/zeta-conditions/astra-constructions.md:138
- Raised by: orchestrator asked; codex prover defined it and closed the easy reading
- Status at last mention: settled negatively
- Content: Incommensurability means no common `h > 0` makes every `l_p/h` an integer. A constant finite-bond cMPS has continuously variable `L` but an analytic exponential-polynomial `N(L)`; "that fact does not create an atomic collection of incommensurable prime lengths." Nor do incommensurable Hamiltonian frequencies: those concern oscillations, not a proven Euler-prime length spectrum.
- Lead: the `log p` incommensurability that the Riemann programme wants cannot be manufactured by going continuous. It has to come from an infinite bond or from geometry (compare L05-022, where `log p` arises as an actual idele-class period).
- Related: L05-022, L05-053, L05-082.

### L05-065 E0: the pair shift, a zero by destructive interference with a subshift
- Source: notes/zeta-conditions/astra-brief.md:82-85 (D2); notes/zeta-conditions/astra-constructions.md:162-174, 355; evidence lines 7-105
- Raised by: orchestrator; built and corrected by codex prover
- Status at last mention: PROVED, interpretation CORRECTED
- Content: Four letters `(a,b) in {0,1}^2` with `A_{(a,b)} = diag(1, [a=b])` on `C^{1|1}`: the parity boundary cancels exactly the words all of whose pairs are diagonal, so `N_n = 4^n - 2^n` and `Z(u) = (1-2u)/(1-4u)`. Full even spectrum `{4,2}`, full odd `{2,2}`, one pair cancels, leaving one pole at `1/4` and one zero at `1/2`. RH-by-half-entropy: the odd coherence has half the exponential growth. Primitive binary necklaces sit inside primitive four-letter necklaces so every `a_d >= 0` — infinitely many surviving primes on a *finite* bond. Corrections: there is no FE; the `Z(A^1/F_4)/Z(A^1/F_2)` reading is an equality of rational functions in an identified degree variable, **not** an Artin quotient from the swap; and a simple Perron root does not make the displayed tensor a channel on the whole bond.
- Lead: this is the notebook's cleanest "a zero is destructive interference with a literal subshift" demonstration, and the model for D1's sub-system rule.
- Related: L05-066, L05-067, L05-076.

### L05-066 D1 — the sub-system rule, and what it actually needs
- Source: notes/zeta-conditions/astra-brief.md:78-81 (D1); notes/zeta-conditions/astra-constructions.md:354
- Raised by: orchestrator; conditioned by codex prover
- Status at last mention: PROVED-CONDITIONAL
- Content: The draft: if the odd sector is a sub-MPS of the even one, then `Psi_Pi = Psi_+ - Psi_-` is a sum of orthonormal words, `N_n = N_n^+ - N_n^-`, `a_d = a_d^+ - a_d^- >= 0`, and "the zeros of `Z` are the poles of the sub-system's zeta". The conditions that must be added: **unit-coefficient** word states (equal amplitudes alone does not give unit magnitude), and a repetition- and rotation-compatible subsystem so that primitive orbits form a genuine set difference. Weighted sub-sums give weighted norms. And "zeros = subsystem poles" holds only *before* net cancellation.
- Lead: this is the general recipe for manufacturing zeros from a subsystem. Worth stating as a lemma in the report shards, with the three hypotheses attached.
- Related: L05-065, L05-061.

### L05-067 The three curve rungs and the four-letter 1|1 elliptic tensors
- Source: notes/zeta-conditions/astra-brief.md:86-90 (D3); notes/zeta-conditions/astra-constructions.md:176-197, 356; evidence lines 106-304
- Raised by: orchestrator designed the ladder; codex prover built the tensors
- Status at last mention: PROVED, with an arithmetic-identification caveat
- Content: For `y^2 = x^3+x+1` over `F_5`: `a = 5+1-N_1 = -3`, `pi = (-3 + i sqrt 11)/2`. Four letters on `C^{1|1}` built from `t = (q+r)/2`, `h = (q-r)/2` with `r = 0` (affine) or `r = 1` (projective): two diagonal letters with Gram overlap `pi`, two parity-changing letters giving symmetric population transfer with eigenvalues `q, r`, and residual `t - q/t >= 0`. In both cases `sum A_s^† A_s = q`, so dividing by `sqrt q` gives an honest TP channel on the **whole** bond. `Z_aff = (1-pi u)(1-conj(pi) u)/(1-5u)`, `Z_proj` adds `(1-u)` and the FE. The two odd eigenvalues have modulus `sqrt 5` exactly because `pi conj(pi) = 5`, so their block over `sqrt 5` is unitary — RH by a visible mechanism. Important correction: the draft's plan of "deleting the product tensor's `H^0` block" does not give the affine rung; a different tensor is needed.
- Lead: this is the concrete answer to TJO's request — four letters on a bond of dimension `1|1` giving an elliptic curve zeta with FE, RH and a unique stationary state.
- Related: L05-068, L05-074, L05-077.

### L05-068 Ring-norm data do not determine the physical state
- Source: notes/zeta-conditions/astra-constructions.md:187-189
- Raised by: codex prover (an aside, not asked for)
- Status at last mention: PROVED; mentioned once
- Content: Three different tensors give *identical* ring norms and FE for the same elliptic curve: the four-letter `1|1` construction (maximally mixed unique stationary state, nonzero entanglement, transfer lengths `1/log 5` even and `2/log 5` odd); the shard 06g product letters `diag(1,pi)/sqrt 2` (zero entanglement, no full-bond TP gauge, rank-one left Perron eigenmatrix); and a two-letter damping representative (pure stationary vacuum). "Ring norm data do not determine these features" — even the stationary density matrix is not selected by the zeta.
- Lead: consequential for the whole programme. If the Phantasm is to be pinned down by zeta data alone, it cannot be: the zeta fixes the divisor, not the state, the entanglement, or the fixed point. Something beyond the zeta must select the physical realisation.
- Related: L05-067, L05-079, L05-083.

### L05-069 D5 corrected: the genuine tiny Z/2 Artin example (a voltage double cover)
- Source: notes/zeta-conditions/astra-brief.md:94-98 (D5); notes/zeta-conditions/astra-constructions.md:174, 199-210, 358; evidence lines 305-385
- Raised by: orchestrator drafted D5 and pre-emptively flagged it ("This is probably wrong because the pair shift is not a Z/2 cover"); codex prover confirmed and replaced it
- Status at last mention: CORRECTED with replacement
- Content: The drafted `L(u,sgn) = ((1-mu)/(1-m^2 u))^{1/2}` is wrong — half multiplicities (its `a_2 = 5/2`, printed in the evidence) already prevent a finite-dimensional trace interpretation. The diagnosis: three different objects were mixed — the trace of swap on the *entire* word space (`2^n`), the overlap of a single MPS state with its swapped copy (equal to its norm), and a deck-twisted path trace. The replacement is a directed base vertex with three loops of Z/2 voltages `0,1,1`; path matrix `C = 1 + 2X`; six matrix-unit letters on the two-sheeted cover, each closed word of amplitude one. Then `L(u,1) = 1/(1-3u)`, `L(u,sgn) = 1/(1+u)`, `Z_cover = L_1 L_sgn`. The sign logarithmic trace is `(-1)^n`, so **that individual Artin factor is not a norm**. A primitive base orbit with voltage `v` carries local factor `(1-chi(v)u^d)^{-1}` — the actual monodromy Euler product.
- Lead: voltage covers are the correct way to get Artin L-functions as MPS. Also recorded: "A group projector on each word space need not be compatible with repetition of prime orbits."
- Related: L05-060, L05-065, L05-074.

### L05-070 Horner Dirichlet MPS: tiny L-functions over F_2[x] and F_3[x]
- Source: notes/zeta-conditions/astra-brief.md:59-64 (C7b); notes/zeta-conditions/astra-constructions.md:212-260; evidence lines 386-601
- Raised by: orchestrator specified them; codex prover built them
- Status at last mention: built and PROVED, with the physical status corrected
- Content: Bond = the residue field `F_q[x]/M` including zero; letter `H_c` has entry one in row `xf + c mod M`, column `f` (the Horner step); start at the residue 1, read the `n` lower coefficients of a monic polynomial, close with the character row `(chi(f))_f` extended by `chi(0) = 0`. Then `b_n = chi^T (sum_c H_c)^n |1>` and `L(u,chi) = sum b_n u^n`. For `F_2`, `M = x^3+x+1`, `chi(x) = w = e^{2 pi i/7}`: `alpha = -(1+w+w^3)`, `L = (1-u)(1-alpha u)`, `|alpha|^2 = 2`, bond dimension 8. For `F_3`, `M = x^2+1`, `chi(1+x) = w = e^{2 pi i/8}`: `alpha = w^3+w^2-w = -sqrt 2 + i`, `L = 1 - alpha u`, `|alpha|^2 = 3`, bond dimension 9; characters with exponents 1,3,5,7 are odd with degree-one nontrivial L-functions, the nontrivial even ones have only `1-u`. Corrections: the *physical open norm* is the number of monics coprime to `M` (`q^n` below `deg M`, then `q^n - q^{n-deg M}`), **not** `b_n`; the amplitude presentations `diag(1,alpha)` and `[alpha]` reproduce the supertraces and superdeterminants but are not physical Ramond norms (the sequences are complex already at degree one); and the formal Möbius exponents printed are not the weighted degree-`d` prime sums.
- Lead: TJO asked for "tiny L functions" as MPS any practitioner would understand, and these are them. The open gap is that a *character-weighted* amplitude is not a norm, so these L-functions sit on side A (open chain) rather than side B (ring).
- Related: L05-071, L05-060, L05-052.

### L05-071 Side A to side B for the Horner automaton — and why closing it into a trace is wrong
- Source: notes/zeta-conditions/astra-brief.md:63-64; notes/zeta-conditions/astra-constructions.md:251-258
- Raised by: orchestrator asked to "explain the open-chain (sum over monic f, side A) versus ring (Frobenius orbits, side B) presentations and relate them"; codex prover answered with a correction
- Status at last mention: settled, and one route declared wrong
- Content: Unique factorisation of monic polynomials gives `L(u,chi) = prod_{P∤M}(1-chi(P)u^{deg P})^{-1}` and `N_n^chi = sum_{d|n} d sum_{deg P = d} chi(P)^{n/d}`. The prime polynomials are Frobenius orbits on the affine line away from the ramified modulus, and their weight repeats as `chi(P)^k`. "These are weighted orbit rings, **not** cyclic paths of the Horner residue automaton. Simply closing `H_c` into a trace is wrong: it imposes `f = x^n f + b`, a residue-automaton return condition." Verified against independent enumeration of irreducible monics through degree six, matching `N_n^chi = -1 - alpha^n` (F2) and `-alpha^n` (F3).
- Lead: this is the sharpest statement in either campaign of the side A / side B gap. The open-chain automaton computes the L-function; closing it into a ring gives the *wrong* orbits. Anyone hoping "side A automaton + trace = side B ring" should read this line.
- Related: L05-070, L05-060.

### L05-072 The Gauss sum sign convention
- Source: notes/zeta-conditions/astra-brief.md:65-66 (C7c); notes/zeta-conditions/astra-constructions.md:262-264; evidence lines 602-646
- Raised by: orchestrator asked for Gauss sums as degree-1 L-functions; codex prover fixed the sign
- Status at last mention: CORRECTED (a convention fix)
- Content: For the quadratic character over `F_3` with `psi(x) = e^{2 pi i x/3}`, `G = i sqrt 3`, also equal to the affine-line sum `sum_x psi(x^2)`; extensions obey `G_n = (-1)^{n-1} G^n` (Hasse-Davenport). So the standard convention `exp(sum G_n u^n/n)` gives `1 + Gu`, **not** `1 - Gu`; the latter is right only if `G` has been redefined as the Frobenius eigenvalue `-i sqrt 3`. No poles; zero at `u = i/sqrt 3`. "A single complex Gauss factor is not a positive norm or a bosonic prime gas."
- Lead: a small, easy-to-get-wrong sign that would silently flip a functional equation. Recorded so it is not rediscovered.
- Related: L05-073, L05-052.

### L05-073 Kloosterman: the requested q^n - Kl_n norm on a 1|1 bond does exist
- Source: notes/zeta-conditions/astra-brief.md:65-67 (C7c, "is there an MPS whose Ramond norm is q^n - Kl_n-type counts, and what is its bond?"); notes/zeta-conditions/astra-constructions.md:266-281; evidence lines 647-713
- Raised by: orchestrator asked the question; codex prover answered yes
- Status at last mention: PROVED (a direct positive answer to an open question in the brief)
- Content: Over `F_4` with the raw sum `S_n = sum_{x != 0} (-1)^{Tr(x + x^{-1})}`: `S_1 = 3`, `L_Kl(u) = 1 + 3u + 4u^2 = (1-pi u)(1-conj(pi)u)` with `pi = (-3 + i sqrt 7)/2`, `S_n = -(pi^n + conj(pi)^n)`. The elliptic curve `y^2 + xy = x^3 + 1` has affine count `4^n + S_n`. **So the requested norm of type `q^n - Kl_n` exists on bond `1|1`, with four explicitly printed affine letters**, provided `Kl_n` means the Frobenius power sum `-S_n`; with the raw convention the sign is plus. The affine norm zeta has one pole at `1/4` and two zeros; `|a| <= 2 sqrt q` follows from the computed conjugate pair with product `q`. Important: C1/C2 fail for the individual L-factor (its extension sums change sign), and only the **curve completion** restores a positive count and a genuine gas.
- Lead: exponential sums become physical ring norms only after completing to a curve. That pattern — "the L-factor alone is not a norm, the completion is" — repeats at L05-069 and L05-074 and is probably the general rule.
- Related: L05-067, L05-069, L05-074.

### L05-074 The graph cover Ihara Artin factor, and the correct inverse-pairing mechanism
- Source: notes/zeta-conditions/astra-brief.md:67 (C7d); notes/zeta-conditions/astra-constructions.md:283-300, 357; evidence lines 714-1018
- Raised by: orchestrator asked for "the Artin L-function of a small graph cover (Ihara), one example"; codex prover built it and used it to repair D4
- Status at last mention: PROVED, plus a derived new tensor
- Content: A rose with two undirected loops `a,b` oriented as `a,a^{-1},b,b^{-1}` with Z/2 voltages `0,0,1,1`; the cover has two vertices, a loop at each and two connecting edges. Eight row-letter matrices on bond dimension 8; a physical word is a closed non-backtracking directed-edge sequence with amplitude one — a literal count MPS, and its natural grading is **entirely even**. Fourier on the two sheets gives `L_1 = 1/((1-u^2)(1-u)(1-3u))`, `L_sgn = 1/((1-u^2)(1+3u^2))`, so every root is a **pole**; the sign factor's interesting poles are at `u = ± i/sqrt 3`. After removing one `(1-u^2)` per character the two Bass quadratics are `1-4u+3u^2` and `1+3u^2`, with reciprocal roots `{1,3}` and `{i sqrt 3, -i sqrt 3}`: **the reversal / no-backtracking identity forces the common product `q = 3` in these quadratics, and this is where inverse pairing really produces the FE.** The script then converts the reduced even/odd quadratics into a physical `1|1` graded elliptic norm tensor with `Z = (1+3u^2)/((1-u)(1-3u))` — a new graded norm realisation of a **ratio of reduced graph determinants**, not of the cover norm itself. Bond dimension two is the minimum possible for any nonzero doubled odd sector.
- Lead: this is the mechanism the programme wanted from shard 08b, now located correctly (Bass factors of a non-backtracking transfer, not a raw inverse-closed Kraus family). Also recorded: "the discarded Bass modes must be named, since the unmodified full divisor is not reciprocal at `q = 3`", and transposing the row-letters and dividing by `sqrt 3` gives a TP Kraus family directly.
- Related: L05-056, L05-060, L05-067, L05-073.

### L05-075 Every physical mode of the Ihara cover is even — the sign factor is not a norm
- Source: notes/zeta-conditions/astra-constructions.md:118, 155, 285, 300
- Raised by: codex prover
- Status at last mention: recorded, not followed up
- Content: In the graph cover the natural grading is entirely even, including the sign-character modes; the table row for `graph_artin` reads "all even" under C8. "Character projection of the graph trace is a linear amplitude operation; its sign trace takes negative values and is not itself the norm of the projected physical state."
- Lead: a counterexample to the notebook's hoped-for pattern "even = trivial character, odd = nontrivial characters". That pattern is specific to Artin-Schreier / hyperelliptic cohomology, not general. Small but it constrains the Galois-grading programme.
- Related: L05-060, L05-069, L05-074.

### L05-076 The supersingular curve with a real double zero and the Artin-Schreier involution as U = Pi
- Source: notes/zeta-conditions/astra-brief.md:88 (D3 last rung); notes/zeta-conditions/astra-constructions.md:191-197; evidence lines 248-304
- Raised by: orchestrator; built by codex prover
- Status at last mention: PROVED
- Content: `y^2 + y = x^3` over `F_4` gives `a = -4`, `pi = -2`, `Z = (1+2u)^2/((1-u)(1-4u))` — a **double zero at `u = -1/2` fixed by the reciprocal involution**, i.e. a zero on the real axis of the critical circle. The product letter is `diag(1,-2)`; a TP four-letter version is printed beside it. Exact enumeration through degree six checks the double-root sign. The Artin-Schreier involution acts trivially on `H^0, H^2` and by its sign character on `H^1`; **in the tensor this is exactly `U = Pi`, with odd physical letters changing sign**.
- Lead: the identification "Galois involution = bond parity operator" is the cleanest realisation in the notebook of "odd sector = nontrivial character". It is worth checking whether that identification generalises beyond Artin-Schreier.
- Related: L05-060, L05-067, L05-075.

### L05-077 Mutual independence of FE, RH and mixing — and the one impossible combination
- Source: notes/zeta-conditions/astra-brief.md:99-103 (D6); notes/zeta-conditions/astra-constructions.md:302-317, 359; evidence lines 1019-1366
- Raised by: orchestrator asked to "Decide whether 'unique fixed point' can be imposed independently of the FE and RH"; codex prover decided it
- Status at last mention: PROVED
- Content: Eight homogeneous Kraus families, all TP after division by four, on a `1|1` bond with even spectra `{16, r}` and odd `{x,y}`: TTT `(r=1, 4,4)` has FE+RH+mixing; TFT `(1, 8,2)` FE+mixing, no RH; FTT `(0, 4,4)` RH+mixing, no FE; FFT `(1, 3,3)` mixing only. The letters are scaled identity and Pauli matrices with positive coefficients `(16 ± r ± x ± y)/4` — physical letters, not a spectral ansatz. Tensoring with an idle all-even qubit gives the F-variants: FE and RH preserved, uniqueness destroyed, **no divisor point moved**. All Möbius exponents are nonnegative integers in every degree, proved by embedding disjoint full shifts. **The one impossibility:** if one insists on the exact *projective* curve normal form with real coefficients, RH already makes the odd multiset reciprocal and `{1,q}` supplies the even reciprocal pair, so `(C4 = N, C5 = Y, C6projective = Y)` cannot occur.
- Lead: the conditions the programme wants are genuinely independent — so RH is *not* going to fall out of FE plus a unique fixed point. That closes a whole class of hoped-for shortcuts. The exception (projective normal form) shows where a *stronger* pole condition does couple them.
- Related: L05-058, L05-059, L05-084.

### L05-078 The half-entropy cMPS and the exact 1|1 no-go
- Source: notes/zeta-conditions/astra-brief.md:104-107 (D7); notes/zeta-conditions/astra-constructions.md:319-337, 360; evidence lines 1367-1442
- Raised by: orchestrator asked for the continuum analogue of E0; codex prover built two and proved they cannot be merged
- Status at last mention: PROVED with a regularity qualification, plus a new no-go
- Content: Regular bosonic data `Q = I/2`, `R = diag(1,0)`, `Pi = diag(1,-1)` give `T = diag(2,1,1,1)`, `N(L) = e^{2L} - e^L`, `Zcal(z) = (z-1)/(z-2)` — exactly the requested half-exponent ratio. But it is not a Lindblad gauge on the full bond (its Perron left eigenmatrix has rank one) and a scalar growth shift cannot fix the unequal diagonal completeness defects. A finite-norm **normalised Lindblad** alternative exists (`R_f = [[0,1],[0,0]]`, `R_b = diag(1/2,-1/2)`, `Q = diag(-1/8,-5/8)`, `N(L) = 1 - e^{-L}`) but `R_f` and `R_b` do not commute so it fails the algebraic kinetic-regularity relation. **The no-go:** on homogeneous regular `1|1` data, each fermionic off-diagonal `R` is nilpotent, anticommutation forces all nonzero ones to have the same orientation, and any diagonal bosonic jump commuting with one of them is scalar and supplies no dephasing — so a normalised generator with a unique fixed point has even eigenvalues `{0,-gamma}` and odd `{-gamma/2 ± i omega}`, and **cannot** produce the half-difference `{0,-gamma}` even minus `{-gamma,-gamma}` odd for `gamma > 0`. "No unsupported higher-bond no-go is claimed."
- Lead: the explicit next question is whether the half-difference becomes possible on `C^{1|2}` or larger — the no-go is deliberately scoped to `1|1`. That connects to the memory item "genus >= 2 needs fermionic species (theorem + explicit C^{1|2} realisation)".
- Related: L05-062, L05-079, L05-065.

### L05-079 The FE cMPS: an amplitude-damping generator with additive FE, RH and a unique vacuum
- Source: notes/zeta-conditions/astra-brief.md:106-107; notes/zeta-conditions/astra-constructions.md:134, 339-348; evidence lines 1443-1503
- Raised by: orchestrator asked for "the cMPS with the FE (poles at 0 and lambda, zeros at lambda/2 ± i omega)"; codex prover built it
- Status at last mention: PROVED
- Content: One regular lowering fermion at rate two with Hamiltonian energy difference one. In the growth convention, even eigenvalues `{2,0}`, odd `{1±i}`, so `N(L) = 1 + e^{2L} - 2e^L cos L = |1 - e^{(1+i)L}|^2 >= 0`, `Zcal(z) = ((z-1)^2+1)/(z(z-2))`, and `Zcal(2-z) = Zcal(z)`. The jump is nilpotent so kinetic regularity holds; the odd damping is half the population decay and the frequency comes from the Hamiltonian; **the generator shifted by half the reflection constant is skew-adjoint on the odd two-dimensional sector** — exactly the S7 mechanism of campaign Y, realised concretely. Also: all three projective elliptic zeta *data* have such a cMPS counterpart with `gamma = log q`, `omega = arg pi`, one decay jump `sqrt(gamma)|0><1|`, shifting `Q` by `gamma/2` for growth.
- Lead: the honest caveat is the lead. "This ring vector has only its vacuum amplitude: a product containing a lowering jump is off-diagonal and has zero parity trace... the nontrivial zeta data sit in its length-dependent vacuum normalisation. It does not establish the proposed nontrivial Gibbs entanglement spectrum of the infinite Riemann programme." So the mechanism works but the state is trivial; making it nontrivial is the next step.
- Related: L05-026, L05-057, L05-068, L05-078.

### L05-080 The half-entropy row has RH without FE — and the centre is not canonical
- Source: notes/zeta-conditions/astra-constructions.md:156-160
- Raised by: codex prover
- Status at last mention: recorded, small
- Content: For the half-entropy row, `lambda_- = lambda_+/2` passes the central-line test **only against an explicitly prescribed target reflection** `lambda -> 2 - lambda`; the divisor itself does not obey that reflection. So it is C5 without C4, and there is no FE selecting the centre. Translating the spectrum by `-2` transports the target to `lambda -> -2 - lambda`: "half of a growth exponent is not invariant under arbitrary growth shifts."
- Lead: important guard for the whole "RH = uniform decay at half the rate" reading. Without an FE to fix the centre, "half" is convention-dependent, and a growth shift moves it.
- Related: L05-055, L05-057, L05-079.

### L05-081 D8 corrected — a finite bond can have infinitely many Euler primes
- Source: notes/zeta-conditions/astra-brief.md:108-112 (D8); notes/zeta-conditions/astra-constructions.md:361, 373
- Raised by: orchestrator drafted the no-go; codex prover split it
- Status at last mention: CORRECTED; the infinite arithmetic construction remains OPEN
- Content: The draft assumed a finite bond could not reach a Riemann-like object at all. The correction: a finite bond **can** produce infinitely many primitive necklaces and hence infinitely many Euler factors (E0 already does). What it cannot do is produce infinitely many distinct divisor points in the `u`-plane, a nonrational `Z(u)`, or an analytic finite-cMPS norm equal to the prime comb. Substituting `u = q^{-s}` gives infinitely many *periodic copies* of finitely many divisor points in the `s`-plane — "that is not Riemann's zero distribution". Also: the `06e`/`04b` trace-class no-go applies to **uncancelled negative spectral multiplicities**, not to graded physical norms — "The graded norm constructions here evade exactly that obstruction, by negative net coherence multiplicities."
- Lead: the no-go is narrower than believed, and the graded construction is precisely the evasion. What remains impossible for a finite bond is the *divisor* structure, not the Euler product.
- Related: L05-053, L05-065, L05-082, L05-083.

### L05-082 The uncompleted one-pole FE bookkeeping obstruction
- Source: notes/zeta-conditions/astra-constructions.md:371
- Raised by: codex prover
- Status at last mention: recorded, one paragraph, never followed up
- Content: "A single simple pole at `u = 1/q` is incompatible with the **uncompleted**, self-reciprocal curve-type FE for `q > 1`: reflection also requires a pole at `u = 1`. State whether the second pole is in the completion." The same bookkeeping applies to the generator poles at `0` and `kappa`. And: "Riemann's one-pole uncompleted function has archimedean/completion data absent from a bare finite ring determinant."
- Lead: Riemann's zeta has *one* pole; a self-reciprocal FE demands two. That mismatch is exactly what the completion (Gamma factor) absorbs, and it is a precise reason the archimedean factor cannot be optional. Ties directly to L05-018 and L05-042 in campaign Y.
- Related: L05-018, L05-042, L05-054, L05-084.

### L05-083 "What a practitioner can build tonight and what nobody can"
- Source: notes/zeta-conditions/astra-constructions.md:365-375
- Raised by: orchestrator asked for the section; codex prover wrote it
- Status at last mention: the campaign's closing verdict
- Content: Buildable tonight: E0 (a zero by destructive interference with a literal subshift); the four-letter elliptic tensors (adds RH, and FE on projective completion, with a unique stationary channel); Pauli reweighting to break RH while keeping FE and stationarity; an idle qubit to destroy uniqueness without moving any divisor point; the Horner tensors for tiny Dirichlet polynomials; the graph cover for an Artin decomposition whose nontrivial factors have poles; the amplitude-damping cMPS for an additive FE with uniform odd decay and a unique vacuum. What nobody can, factor by factor: "It does not make an infinite product converge, produce its continuation or archimedean factors, select a prescribed entanglement spectrum, or prove RH for an unidentified infinite object."
- Lead: the method's limits are now explicit. Everything local is reachable; convergence, continuation, the archimedean factor, and the entanglement spectrum are not.
- Related: L05-081, L05-084.

### L05-084 A precise sufficient checklist for a "tiny Riemann"
- Source: notes/zeta-conditions/astra-constructions.md:369
- Raised by: codex prover (answering D8's "state the minimal list of conditions")
- Status at last mention: stated, OPEN
- Content: Four items: (1) a convergent positive integer prime Euler product with infinitely many prime species; (2) a specified meromorphic continuation and completion with the intended pole divisor; (3) reciprocal / additive symmetry of the retained modes; (4) either the critical-circle/line condition itself, **or** Weil positive definiteness plus that symmetry. A unique channel fixed point is a further physical condition, not a replacement for the analytic requirements; growth and summability are needed in an infinite setting.
- Lead: this is the target specification for the Phantasm, stated without jargon. Item (4)'s "Weil positivity plus symmetry" is the only route in the list that does not presuppose knowing where the zeros are — worth prioritising, and it pairs with the unused continuous-time Weil kernel criterion at L05-057.
- Related: L05-053, L05-057, L05-077, L05-082, L05-083.

---

## Small but possibly consequential

1. **L05-014 (exterior occupation parity gives 1/zeta as a signed trace)** — one paragraph, never followed up, but it says the arithmetic wants a *different* grading from the one the programme has been using; pursuing it gives `1/zeta` with no boundary-functional gymnastics.
2. **L05-029 (Gram condition number 10 -> 700)** — a cheap numerical experiment (extend to 10k, 30k zeros) that would decisively kill or support the Riesz-basis route to a metric proof of RH; flagged twice and never run.
3. **L05-068 (ring-norm data do not determine the physical state)** — three tensors with identical zetas but different entanglement, stationary states and fixed points; if true in general, the zeta alone can never pin down the Phantasm and something else must select it.
4. **L05-071 ("closing the Horner automaton into a trace is wrong")** — the sharpest concrete statement anywhere of the side A / side B gap, with the exact wrong return condition `f = x^n f + b` written out.
5. **L05-057 (continuous-time Weil kernel criterion)** — stated once in the C5 paragraph and never used, yet it is exactly the generator-side Weil positivity condition the cMPS programme needs; and L05-084 names it as the only route that does not presuppose the zeros.
6. **L05-036 (the critical law is supported on infinitely many occupied primes)** — answers "what is at b -> infinity" precisely, and relocates the critical object to a completed configuration space; never used afterwards.
7. **L05-038 (the conserved family {V_n})** — the forward dynamics have a commutative family of fixed Heisenberg observables indexed by the integers; noticed only as an obstruction to decay, never explored as a structure.
8. **L05-082 (one pole vs two under a self-reciprocal FE)** — a one-paragraph bookkeeping remark that pins down exactly what the archimedean completion has to do, and why a bare finite ring determinant can never have Riemann's pole structure.

## Dead routes recorded

- **The phase-side Lindbladian at rates `lambda_p = 1/p` is not a normal Lindbladian at all**: infinite no-jump quadratic form, and no trace-norm limit of the finite-prime semigroups at any positive time — astra-structure.md:25, 420-437, ledger 893.
- **The doubled-bond grading (`even = span{e_0}`) is not preserved by the prime jumps**; there is no invariant even-odd restriction to carry a spectrum — astra-structure.md:115-128 (eq 2.4), ledger 846; astra-finite-model.md:289-297.
- **Gauss-vector coherences are not scalar Lindblad modes** (mod-3 / p=2 counterexample; the compression carries an extra `1/p` and a large orthogonal residual) — astra-structure.md:158-182, ledger 849-850; astra-finite-model.md:112-156.
- **`c_b(1) = mu(b)` is not a vacuum-to-shell jump overlap**; the true overlaps are nonnegative and put zeta in the *numerator* — astra-structure.md:283-302, ledger 859.
- **Commuting jumps do not restore the Euler product**; word/Poisson multiplicities `Omega(n)!/prod k_p!` survive, and neither the shell stay term nor the parity closure removes them — astra-structure.md:365-383, 447-449, ledger 863-864.
- **The guessed vacuum generating functions have no pole at `s = 1` and none at `1/2 + i gamma_n`**: exactly `1/(1 - S_P(s+beta+1))` and `zeta_P(s+beta+1)`, with analytic pole exclusion uniform in the prime cutoff — astra-finite-model.md:196-285.
- **A shrinking `F/(1/zeta_P)` ratio is not evidence of a hidden reciprocal-zeta factor** (partial Euler product evaluated outside its convergence half-plane) — astra-finite-model.md:283.
- **Parity closure does not implement the quotient by `Q^x`** — explicit two-dimensional counterexample `W_q = diag(1, e^{i theta v_p(q)})`, `Pi = diag(1,-1)` — astra-structure.md:491-503, ledger 870.
- **Connes 1999 does not supply an unconditional global periodic-orbit trace** for anything like this construction — astra-structure.md:517-521, ledger 872.
- **`Tr[Gamma_b e^{tL_F}]` is not an ordinary trace** on the infinite doubled bond, even with a finite prime cutoff — astra-structure.md:439-445, ledger 894.
- **Shell-diagonal Gibbs weights are not stationary** under the proposed forward+reverse jumps; and the drafted reverse rate was backwards (`d = u p^beta`, not `u/p`) — astra-structure.md:627-653, ledger 884-885; astra-finite-model.md:337-391 (exact rational counterexample).
- **Forward phase dynamics do not select Haar**: they converge weak-* to `delta_0`, whose phase restriction gives `delta_0(c_b) = phi(b)` — astra-structure.md:758-762, ledger 890.
- **Vacuum coherences neither decay fully nor are absorbing**: conserved observables `V_n` force `||e^{tL}X_b||_1 >= sqrt(phi(b)/b)` — astra-structure.md:793-806, ledger 891.
- **"Haar is the pure vector state of `e_0` on `C(Zhat)`"** is false — Haar is mixed on the commutative phase algebra — astra-structure.md:258-266, ledger 857.
- **"Character-diagonal unitary jumps cannot produce frequencies"** is false without an inversion-symmetry assumption on the weights — astra-structure.md:208, ledger 853.
- **"All primes fermionic, zeros on `Re s = 0`"** is true of the finite factors only, not of the continued infinite product — astra-structure.md:454, ledger 866.
- **"Poles exactly the nontrivial zeros" is globally false** for `sigma_{1-s}(n)/zeta(s)`: it also has a pole at `s = -2` — astra-structure.md:471, ledger 865.
- **A spectral line alone does not give anti-Hermiticity**: the Jordan block `-2gamma + [[i omega,1],[0,i omega]]` — astra-structure.md:570-575, ledger 877. And formal skew-symmetry does not constrain the spectrum: `-d/dx` on `L2(0,infty)` — astra-structure.md:556.
- **The forward phase prime does not have the real spectrum of the reversible 04c chain**: it has the full disk `lambda_p(z-1)`, `|z| <= 1` — astra-structure.md:413-418, ledger 862.
- **`D = x d/dx + 1/2` is not a Hamiltonian** as literally drafted; `-iD` with a fixed measure is — astra-structure.md:29-39, ledger 895.
- **Inverse-closed letters do not give the functional equation for a raw doubled transfer**: `B = diag(1,2)` counterexample (even pair fixes `q = 17/2`, odd pair fails it) — astra-constructions.md:76, 357.
- **The drafted `Z/2` L-function of the pair shift, `L(u,sgn) = ((1-mu)/(1-m^2u))^{1/2}`, is not an Artin factor**: half multiplicities (`a_2 = 5/2`) prevent any finite-dimensional trace interpretation; the pair shift is not a double cover — astra-constructions.md:174, 210, 358.
- **The `Z(A^1/F_4)/Z(A^1/F_2)` reading of E0 is not an Artin quotient**: it is an equality of rational functions in an identified degree variable — astra-constructions.md:172, 355.
- **Positivity of all ring norms does not give a bosonic gas**: `diag(1,-1)` has `N = (4,0,4,0,4,0)` and `a_2 = -2` — astra-constructions.md:39.
- **A nonzero finite-dimensional constant cMPS cannot be a prime gas**: its `N(L)` is analytic and cannot equal an atomic prime comb as a measure — astra-constructions.md:48.
- **Closing the Horner automaton into a trace is wrong**: it imposes the residue-automaton return condition `f = x^n f + b`, not Frobenius orbits — astra-constructions.md:258.
- **`Tr(Pi F^n)` is not a physical norm**: the norm of a one-letter amplitude model is `|Tr(Pi F^n)|^2`; character amplitudes and Möbius exponents of amplitude models are not prime counts — astra-constructions.md:19, 260; evidence.md:483-484, 599-600.
- **`exp(sum G_n u^n/n)` gives `1 + Gu`, not `1 - Gu`** for the standard Gauss sum convention — astra-constructions.md:264.
- **The individual Kloosterman L-factor is not a positive count / genuine gas** (its extension sums change sign); only the curve completion is — astra-constructions.md:281.
- **The individual Artin sign factor of the graph cover is not a norm** (its logarithmic trace is `(-1)^n`), and every physical mode of that cover is even — astra-constructions.md:210, 300.
- **"Even = trivial character, odd = nontrivial" is not a theorem about all group actions** — refuted by the Ihara cover — astra-constructions.md:118.
- **The 06g product letters `diag(1,pi)` are not TP-gaugeable on the whole bond** (rank-one left Perron eigenmatrix), and `H^0` is not a second decoupled even block — astra-constructions.md:102, 189; evidence.md:1441.
- **Positivity plus a functional equation does not force RH** — explicit CPTP counterexample with poles `{1,1/16}` and odd eigenvalues `{8,2}` — astra-constructions.md:88, 369.
- **A unique stationary state does not imply mixing** (a printed periodic channel has one stationary state and a nontrivial peripheral mode) — astra-constructions.md:96, 317.
- **On a `1|1` bond, kinetic regularity + full Lindblad normalisation + uniqueness + the exact half-entropy difference cannot all hold** — astra-constructions.md:337.
- **A matrix logarithm is not a cMPS embedding**, and a singular `E` has no exponential at positive time (so the affine four-letter tensor has no exact full-transfer embedding) — astra-constructions.md:132.
- **Integrality of `N(L)` at arbitrary real lengths is vacuous** (continuity would force the function constant); there is no intrinsic `a_d` for continuous `L` — astra-constructions.md:29, 41; evidence.md:1440, 1503.
- **A finite bond can never give a nonrational `Z(u)`, infinitely many distinct divisor points, or Riemann's zero distribution** under `u = q^{-s}` (only periodic copies of finitely many points) — astra-constructions.md:373.
- **A single simple pole is incompatible with an uncompleted self-reciprocal FE** for `q > 1` — astra-constructions.md:371.
