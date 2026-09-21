# Lane L14: codex astra rollouts of 2026-09-12 (drafts and messages not in the final files)

Scope note. Four codex `gpt-6-astra` prover sessions of 2026-09-12 were read line by line from
the extracted transcripts in the session scratchpad. Each session produced exactly one repo file.
Other lanes ledger those final files; this lane records only what lives in the transcript and not
in the final file: cut draft passages, ideas stated in chat messages, abandoned scratch
experiments, and the orchestrator's own drafted statements in the briefs (many of which the prover
found false — the brief's original wording exists nowhere else in the repo).

Method. Every `apply_patch` body and every `cat >> ... <<EOF` heredoc in the four transcripts was
unescaped and its `+` lines diffed line by line against the final repo file, and every `-` line
(text the prover deleted from an earlier draft) was checked against the final file for survival.
Transcript line numbers below are the line numbers of the four `.txt` transcripts.

## Coverage

| transcript | lines | read fully? | final repo file | items found |
|---|---|---|---|---|
| `2026-09-12T12-54-39.txt` (Selberg dictionary) | 235 | yes, every line; the 3 patch bodies at 123/130/133 are truncated by the extractor at exactly 20 000 chars, so the tails of those writes are not visible | `notes/selberg/astra-proofs.md` (805 lines) | 10 (L14-001..010). Of 757 visible draft `+` lines, **0** are absent from the final file; 15 `-` lines were replaced, all by expanded final text (checked fragment by fragment). Yield is therefore brief-level and message-level only. |
| `2026-09-12T17-21-49.txt` (Weil positivity) | 167 | yes, every line; patch bodies at 124/130 truncated at 20 000 chars | `notes/weil-positivity/astra-proofs.md` (986 lines) | 11 (L14-011..021). Of 677 visible draft `+` lines, **6** are absent from the final file — the only genuine cut of material in the whole lane (L14-011, L14-012). |
| `2026-09-12T19-12-16.txt` (resonances free-association) | 158 | yes, every line; the single patch body at 149 truncated at 20 000 chars, so only ~206 of the final 646 lines were visible as draft | `notes/resonances/astra-freeassoc.md` (646 lines) | 8 (L14-022..029). Of the 206 visible draft lines, 0 absent and 0 removed: the file was written in one pass and not revised. Yield is the eight seeds in the brief plus four chat messages and two scratch scripts. |
| `2026-09-12T21-42-08.txt` (riemann-cmps / the Phantasm) | 224 | yes, every line; patch/heredoc bodies at 139/147/155/167/176/195 truncated at 20 000 chars | `notes/riemann-cmps/astra-proofs.md` (1356 lines) | 13 (L14-030..042). Of 1319 visible draft lines, 4 absent (3 of them heredoc terminators, 1 a re-typeset formula); 13 `-` lines replaced, all surviving in edited form. Yield is brief-level plus five chat messages and two scratch scripts. |

Total entries: **42**.

## Ideas and leads

### L14-001 The flat-trace Laplace transform has the opposite sign from the drafted one
- Source: `2026-09-12T12-54-39.txt:81` (brief T4(ii)) and `:111` (prover's message), and "the corrected form is in `notes/selberg/astra-proofs.md` line 332; the brief's own wording is transcript-only".
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted "Lambda(sigma) = -(d/d sigma) log D(sigma) with D(sigma) = prod_{j>=1} Z(sigma+j)". The prover's first message back says plainly "the flat-trace transform is $D'/D$". So the Laplace transform of the Guillemin flat trace is $+\partial_\sigma\log D(\sigma)$, equivalently $-\partial_\sigma\log(D^{-1})$. The minus sign proposed for that particular $D$ is false.
- Lead: whenever the notebook writes a "continuous Ihara--Bass" in the form (transfer resolvent) = (minus log-derivative of a determinant), check which of $D$ or $D^{-1}$ plays the role of $\det(1-uT)$; getting this backwards inverts the whole zeros/poles dictionary.
- Related: L14-002.

### L14-002 The graph analogue of the Selberg tower is det(1-uT), not its inverse
- Source: `2026-09-12T12-54-39.txt:81` (brief T4(v)), correction at `notes/selberg/astra-proofs.md:510`.
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted "the graph analogue of D is 1/det(1-uT)". The prover shows the graph log-derivative has *exactly the same sign* as $\partial_\sigma \log D(\sigma)$, so the correct analogue is $\det(1-uT)$ itself. The orchestrator's inverse-determinant analogy is the drafted error; this matters because "the Ihara zeta is $1/\det(1-uT)$" then wrongly suggests the Selberg tower should also appear inverted.
- Lead: rewrite the side-A/side-B dictionary entry so that "Selberg tower $D$" ↔ "$\det(1-uT)$" and "Ihara zeta" ↔ "$D^{-1}$"; the tower $\prod_{j\ge1}Z(\sigma+j)$ is present on the hyperbolic side and *absent* on the graph side because the tree is one-dimensional (no transverse Jacobian).
- Related: L14-001.

### L14-003 "All first-band resonances on Re sigma = -1/2 iff every r_j is real" is false with j = 0 included
- Source: `2026-09-12T12-54-39.txt:81` (brief T4(iv)) and `:111`; correction at `notes/selberg/astra-proofs.md:461`.
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted the criterion with $j\ge0$, i.e. including $\lambda_0=0$. With $j=0$ the alleged first band contains $0$ and $-1$ and so cannot lie on $\operatorname{Re}\sigma=-1/2$; the statement is false on *every* compact connected surface. The corrected property is the absence of **nonconstant** complementary-series parameters. The prover's message calls this "exclude the constant Laplace eigenfunction".
- Lead: this is the exact continuous analogue of removing the constant adjacency mode (and, when present, the bipartite extremal mode) in the graph Ramanujan condition — so any "Ramanujan = RH" statement in the notebook must carry the same trivial-mode deletion on both sides of the dictionary. Worth checking the same omission wherever the notebook writes "all modes decay at rate 1/4".
- Related: L14-010.

### L14-004 The modular cusp term is a negative prime comb with a +1/2 boundary constant
- Source: `2026-09-12T12-54-39.txt:83` (brief T5), `:111`, `:115`, and the mpmath check at `:119`.
- Raised by: orchestrator brief (drafted positive), prover (corrected)
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted $C(t) = \sum_{n\ge2}(\Lambda(n)/n)[\delta(t-2\log n)+\delta(t+2\log n)] + A(t)$ with positive weights, and asked only for "the convention (positive weights = peaks of C, or dips)". The prover reports "the stated scattering multiplier gives negative prime peaks", i.e. the prime atoms are *dips*, and then finds a further term the brief did not anticipate: "The $r=0$ calculation adds a $+\tfrac12$ constant to the archimedean distribution", coming from $q(1+2ir)+q(1-2ir)$ differing from its right-Abel boundary distribution by $+\pi\delta_0(r)$ in the $r$ variable. The numerical check at line 119 evaluates $m(0)=\gamma-\log\pi-2\log 2$.
- Lead: any comparison of "the prime comb" between the modular trace formula and the Riemann channel must carry both the sign and the $+1/2$; the damping-by-$e^{-t/4}$ statement the brief wanted is then an identity of *defined prime measures*, not of operator traces.
- Related: L14-005.

### L14-005 The "compressed-semigroup trace is a pure prime comb" claim of the notebook needed qualification
- Source: `2026-09-12T12-54-39.txt:115` (message only).
- Raised by: codex prover
- Status at last mention: stated in a message only (the qualification survives in the final file's ledger, but this sentence is the clearest statement of it)
- Content: "The notebook's claim that the full compressed-semigroup trace is a pure prime comb also needs qualification: I can prove the requested damping identity for the stated prime measures, but that alone does not establish an identity of full operator traces." This is the first place in the 09-12 campaign where the gap between "the prime measures match after damping" and "the operator traces are equal" is named.
- Lead: to close it one needs a genuine trace-class statement for $Z(t)$ (which the later riemann-cmps session shows is impossible: an infinite eigenvalue list precludes compactness), or a regularised trace with a stated regularisation. Consequence if closed: the cusp term of the modular trace formula would literally *be* the damped Riemann channel, not merely share its prime weights.
- Related: L14-004, L14-042.

### L14-006 Omega = -Delta exactly, so the two-jump Lindbladian is -2 Delta
- Source: `2026-09-12T12-54-39.txt:126` (message), constant stated nowhere else in the transcript.
- Raised by: codex prover
- Status at last mention: stated in a message only; the constant is used in the final file
- Content: The brief (line 77) asked for "$\Omega f = c\,y^2(F_{xx}+F_{yy})$ with $c$ an explicit constant you determine (compute it; do not guess)". The answer: on right-$K$-invariant functions $\Omega = -\Delta$ with the notebook's positive Laplacian $\Delta=-y^2(\partial_x^2+\partial_y^2)$, hence $c=+1$, and the Lindbladian built from the two non-compact jumps $L_1=-iH$, $L_2=-iE$ is $\tfrac12(H^2+E^2) = 2\Omega = -2\Delta$ on that sector.
- Lead: this fixes the time normalisation of the "Selberg Lindbladian": a Lindblad time $t$ corresponds to hyperbolic Laplacian time $2t$. Any later attempt to match the Lindblad relaxation rate to the spectral gap $1/4$ must carry the factor 2.
- Related: L14-007.

### L14-007 The tensor Lindbladian is 2 Omega_{pi ⊗ bar-pi} + B_W^2/2, not the Casimir
- Source: `2026-09-12T12-54-39.txt:77` (brief T2(c)) and the draft patch body `2026-09-12T12-54-39_L0123` ("the precise Casimir qualification"); final at `notes/selberg/astra-proofs.md:786`.
- Raised by: orchestrator brief (drafted loosely), prover (sharpened)
- Status at last mention: corrected in final
- Content: The brief asked the prover to "record as a remark (not a theorem) that its spectral gap is governed by the decomposition of $\pi\otimes\bar\pi$ into irreducibles". The prover declines to make that a gap statement and instead proves the exact operator identity: the Lindbladian equals $2\Omega_{\pi\otimes\bar\pi} + B_W^2/2$, with $B_W\rho = 0$ only on the diagonal-$K$-invariant sector. On that sector $\langle\rho,\mathcal L\rho\rangle_{\rm HS} = -\tfrac12\sum_j\lVert[A_j,\rho]\rVert^2_{\rm HS}\le 0$.
- Lead: a spectral gap for this Lindbladian is **not** obtained from the Casimir alone; the $B_W^2/2$ term must be controlled, and the invariant-domain question (is it a core?) is left open. Consequence if closed: a genuine "quantum Selberg gap" statement.
- Related: L14-006.

### L14-008 A circle translation generator is not a Lindbladian: the prime-circle flow is not dissipative
- Source: draft `2026-09-12T12-54-39_L0147` (a `-` line of the fourth patch) and final at `notes/selberg/astra-proofs.md:99` and `:784`.
- Raised by: codex prover
- Status at last mention: corrected in final (the draft sentence survives, embedded in a longer proof)
- Content: "In particular a first-order translation generator is anti-self-adjoint and is not a dissipative sum-of-squares generator merely because it generates a flow." And at line 784: "Calling that generator a dissipative Lindbladian without an additional construction confuses it with a sum of squares."
- Lead: a standing caution for the whole programme. The "circle flows over primes" object of the worklog has an anti-self-adjoint generator; if the Phantasm is to be a Lindbladian, the dissipation must be *constructed* (as the cusp/exit term is in the Riemann channel), not inherited from the flow.
- Related: L14-009.

### L14-009 The finite-prime spectrum also misses the continued zeta's zeros, and this needs the zero-free line
- Source: draft `2026-09-12T12-54-39_L0147` versus final `notes/selberg/astra-proofs.md:87` and `:99`.
- Raised by: codex prover
- Status at last mention: strengthened between drafts (the draft made only the weaker claim)
- Content: The earlier draft said only "The finite Euler product has no zeros anywhere in $\mathbb C$" and "No zeta zero is produced by that finite construction." The final version adds a genuinely new claim: $\operatorname{spec}(A_S)$, which is the set $\bigcup_{p\in S}(2\pi i/\log p)\mathbb Z$ sitting on the imaginary axis, is *disjoint from the zero set of the continued Riemann zeta*. The proof uses $\zeta(iv)=\chi(iv)\zeta(1-iv)\ne0$ for real $v\ne0$ (zero-free line plus the gamma quotient), and $\zeta(0)=-1/2$ at $v=0$.
- Lead: this is the sharpest available form of "the prime circles are blind to the zeros" — not merely "the finite product has no zeros" but "the whole finite-prime spectrum avoids the continued zeta's zeros, and that avoidance is exactly the zero-free line". Any construction that hopes to produce zeros from prime circles must therefore break either the finiteness or the unitarity.
- Related: L14-008.

### L14-010 The drafted trivial-zero multiplicities of the Selberg zeta were among the corrected items
- Source: `2026-09-12T12-54-39.txt:71` (the brief's conventions) and the final RESULT line's list of corrections ("zero multiplicities").
- Raised by: orchestrator brief
- Status at last mention: corrected in final
- Content: The brief stated as convention "trivial zeros at $s=-k$ with multiplicity $(2g-2)(2k+1)$ for genus $g$". This appears in the prover's final list of corrected drafted items ("trace interpretation, determinant sign and graph inverse, constant-mode first band, zero multiplicities, scattering prime sign and boundary constant, and full-channel-trace claim are corrected explicitly").
- Lead: check the multiplicity convention before importing the Selberg trivial zeros into the tower $D(\sigma)=\prod_{j\ge1}Z(\sigma+j)$, since the tower multiplies them.
- Related: L14-003.

### L14-011 CUT: the explicit contour proof that the Lorentzian is the Fourier transform of an exponential of unit mass
- Source: `2026-09-12T17-21-49.txt:124` and `:130` (draft), deleted by the patch at `:143`; **absent from `notes/weil-positivity/astra-proofs.md`**.
- Raised by: codex prover
- Status at last mention: cut from final
- Content: The first two drafts of the Weil file carried a full contour computation of $\int_{\mathbb R} e^{ixt}/(x^2+b^2)\,dx$: for $t>0$ close in the upper half-plane, bound the arc by $\pi R/(R^2-b^2)$ since $|e^{ixt}|\le1$, pick up the pole at $ib$ with residue $e^{-bt}/(2ib)$ giving $\pi e^{-bt}/b$; for $t<0$ close clockwise for $\pi e^{bt}/b$; at $t=0$ the arctangent integral gives $\pi/b$; then shift $x=\xi-\omega$. The point of the calculation was to show the inverse transform of the Lorentzian $2b/(b^2+(\xi-\omega)^2)$ **has mass 1**, i.e. that each off-line mode contributes a genuine probability measure.
- Lead: restore this if the continuous Weil form is ever to be normalised as a spectral *measure* rather than a distribution — the unit mass is what makes "each mode of width $b$ contributes one Lorentzian of weight one" literally true.
- Related: L14-012.

### L14-012 CUT: the named time-ordered Dyson matrix A_{j_1..j_k}, including the empty word A_∅ = e^{tK}
- Source: `2026-09-12T17-21-49.txt:124` and `:130` (draft), deleted at `:143`; **absent from the final file**.
- Raised by: codex prover
- Status at last mention: cut from final
- Content: The draft introduced explicit notation for the continuous ring word: for $k\ge1$ and $0<t_1<\cdots<t_k<t$,
  $A_{j_1\ldots j_k} = e^{(t-t_k)K}R_{j_k}e^{(t_k-t_{k-1})K}R_{j_{k-1}}\cdots e^{(t_2-t_1)K}R_{j_1}e^{t_1K}$,
  with the degenerate cases spelled out: $e^{(t-t_1)K}R_{j_1}e^{t_1K}$ for $k=1$, and $A_\varnothing=e^{tK}$ for $k=0$. It also said "No trace preservation is assumed."
- Lead: this named object is the continuous analogue of the non-backtracking word $A_w$ whose $|\operatorname{Tr}A_w|^2$ is the discrete ring norm. Having a name for it (and for the empty word) is what would let one write a *continuous Ihara--Bass* by words rather than by determinants. The final file proves the theorem but drops the notation, so the word-level picture is not available in the repo.
- Related: L14-011, L14-018.

### L14-013 "Both pairings iff a nonzero scalar multiple of a unitary" is false; it forces actual unitarity
- Source: `2026-09-12T17-21-49.txt:81` (brief T3(c)) and `:114` (message).
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted "(c) BOTH pairings hold simultaneously iff every $B_i$ is a nonzero scalar multiple of a unitary (prove: $\operatorname{Ad}(B^\dagger)=\operatorname{Ad}(B)^{-1}$ iff $B^\dagger B$ is a scalar)". The prover: "simultaneous adjoint and inverse pairing requires actual unitaries". The counterexample is as cheap as $B=2I$. Scalar $B^\dagger B$ characterises only a *projective* equality, with an explicit factor $\kappa$.
- Lead: consequential for the Kraus dichotomy slogan. "Inverse pairing buys the functional equation, adjoint pairing buys reality, unitarity buys both" is right only if "unitarity" means $B^\dagger B=I$ on the nose. Scaled unitaries change the transfer operator, its critical radius $r$, its trivial roots $S_0$, and the channel normalisation — so a family of unequal scales need not preserve the quadratic duality at all.
- Related: L14-014, L14-015.

### L14-014 The requested inverse-paired Kraus counterexample cannot exist: every Kraus family is conjugation-symmetric
- Source: `2026-09-12T17-21-49.txt:81` (brief T3(b)) and `:114` (message).
- Raised by: orchestrator brief (asked for it), prover (proved impossible)
- Status at last mention: dead (the brief asked for an object that does not exist)
- Content: The brief said "Answer precisely (it is iff $\operatorname{spec}(\Sigma)$ is closed under conjugation; give a 1x1 or 2x2 counterexample where it is not)". The prover: "Every Kraus family has conjugation symmetry, so the requested inverse-paired Kraus counterexample cannot exist." The antiunitary involution $C(v\otimes|i\rangle)=v^\dagger\otimes|i\rangle$ commutes with $T$ for *every* Kraus family, adjoint-paired or not — strengthening what the brief asked (it had asked for it only in the adjoint-paired case). A counterexample exists only in the strictly larger non-Kraus superoperator class.
- Lead: "adjoint pairing buys reality" is too weak a slogan — *any* Kraus presentation already buys reality. The real content of adjoint pairing is the nonnegative ring count $\operatorname{Tr}T^\ell=\sum_w|\operatorname{Tr}B_w|^2$, not the conjugation symmetry. This changes which hypothesis is load-bearing in the RH analogy.
- Related: L14-013, L14-015.

### L14-015 An abandoned first attempt at the counterexample: weighted scalar non-backtracking matrices
- Source: `2026-09-12T17-21-49.txt:117` (a sympy exec, before the message at `:121`); **the experiment is absent from the final file**, which carries a different example.
- Raised by: codex prover
- Status at last mention: raised, not pursued (superseded)
- Content: The first attempt built a $4\times4$ non-backtracking matrix directly from *scalar weights*: reversal `rev=[2,3,0,1]`, weights $(a,1,a,1)$ for $a\in\{1,2,4\}$, $T_{ji}=0$ if $j=\bar i$ and $=w_i$ otherwise, then factored its characteristic polynomial. This is a superoperator family that is **not** of Kraus form — exactly the class where L14-014 says the counterexample does live. It was dropped in favour of the genuine $n=2$, $D=4$ Kraus family $B=\{\operatorname{diag}(2i,1),I,\operatorname{diag}(-i/2,1),I\}$ with $\Sigma=\sum_i \bar B_i\otimes B_i$ (exec at `:148`).
- Lead: the scalar-weight non-backtracking matrix is the cheapest laboratory for "inverse pairing without Kraus". If one wants to see the functional equation *without* positivity of ring counts, this is the two-line model to use. Nothing in the repo records it.
- Related: L14-014.

### L14-016 The notebook's xi has no poles at 0 and 1, so the "two trivial modes" of Z do not exist
- Source: `2026-09-12T17-21-49.txt:87` (brief T6) and `:121` (message).
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted "identify ... $S$ (the two trivial modes coming from the poles of $\xi$ at $s=0$ and $s=1$, and where the archimedean Gamma-factor terms sit)". The prover: "the notebook's completed $\xi$ has no poles at $0,1$, and its displayed explicit formula includes pole and Gamma terms alongside negative prime atoms". The $\xi$ used in the repo is entire; the poles at $0,1$ belong to the explicit-formula side $\Lambda_\zeta$, not to the mode list. For the zero-mode semigroup one must take $S=\varnothing$; $\{0,-1/2\}$ can be removed only after an explicitly artificial spectral augmentation.
- Lead: the "trivial set $S$" of the Weil-form machinery has no natural arithmetic occupants here. Any attempt to make the Riemann channel's Weil form two-sided by deleting a trivial set has to *invent* that set, which is a strike against the construction.
- Related: L14-020, L14-039.

### L14-017 mu -> r^2/mu is not a linear map, and W = M needs conjugation symmetry on top of it
- Source: `2026-09-12T17-21-49.txt:79` (brief T2(c)).
- Raised by: orchestrator brief
- Status at last mention: corrected in final
- Content: The brief called $\mu\mapsto r^2/\mu$ "the linear map ... (the 'functional equation')". It is a holomorphic reciprocal map, not linear. More substantively: the circle criterion (b) needs only this reciprocal symmetry, but the identity $W(c)=M(c)$ — Weil form equals mode pairing — additionally needs conjugation symmetry of the retained multiset. The final file gives a reciprocal-only example with $W\ne M$.
- Lead: the two halves of "RH = Weil positivity" split cleanly: the *bound* needs only the functional equation, the *inflow identity* needs reality too. In the notebook's Kraus language that is exactly "inverse pairing gives the bound, adjoint pairing gives the identity".
- Related: L14-014.

### L14-018 The drafted Dyson product omitted the free propagators between jumps and is false for noncommuting K, R_j
- Source: `2026-09-12T17-21-49.txt:83` (brief T4(c)).
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted the continuous ring norm as $\sum_k\sum_{j_1..j_k}\int |\operatorname{Tr}(e^{(t-t_k)K}R_{j_k}\ldots R_{j_1}e^{t_1K})|^2$, which, read literally, has the $R$'s adjacent with no $e^{(t_{i+1}-t_i)K}$ between them. That product is false for noncommuting $K$ and $R_j$. The corrected statement needs the full time-ordered product (see the cut notation in L14-012), plus the $k=0$ term, a finite jump-list hypothesis, and absolute convergence.
- Lead: the "continuous ring norm" is genuinely a *time-ordered* word, not a word in the $R_j$ alone — which is what makes the continuous case harder than the discrete non-backtracking count, where words are unordered letters.
- Related: L14-012.

### L14-019 The drafted superoperator trace was over the wrong space (n^4 instead of n^2)
- Source: `2026-09-12T17-21-49.txt:83` (brief T4(c)).
- Raised by: orchestrator brief
- Status at last mention: dead (typo-level but load-bearing), corrected in final
- Content: The brief wrote $\operatorname{Tr}_{M_n\otimes M_n^*}e^{t\mathcal L}$. But $M_n\otimes M_n^*$ has dimension $n^4$ and is the space of *superoperators*; $e^{t\mathcal L}$ acts on the $n^2$-dimensional state space. The intended trace is $\operatorname{Tr}_{M_n}$, equivalently a trace on $\mathbb C^n\otimes\overline{\mathbb C^n}$.
- Lead: none stated; recorded because the same confusion would quadruple every dimension count in a cMPS bond-space estimate.
- Related: -

### L14-020 "Every zeta function has side A = a nonnegative count of rings" is not true of arbitrary superoperators
- Source: `2026-09-12T17-21-49.txt:71` (the brief's opening framing) and the final ledger's last row.
- Raised by: orchestrator brief
- Status at last mention: corrected in final (recorded as an overreach of the programme's framing)
- Content: The brief opens "In the notebook every zeta function has side A (a nonnegative count of rings, e.g. $\operatorname{Tr}T^\ell = \sum_w|\operatorname{Tr}A_w|^2$)". The prover's ledger records: nonnegative ring traces hold in the stated Kraus settings only; they are *not* a property of arbitrary superoperators, and they are distinct from Weil positive-definiteness even when available. Crucially, the one-sided theorems themselves need no positive ring-count premise at all.
- Lead: this decouples two things the programme had been bundling. Positivity of ring counts (side A) and Weil positive-definiteness of the rescaled trace sequence are logically independent; the RH-relevant one is the latter. Worth checking whether the "ring gas" picture is doing any work in the main line of argument, or is only motivation.
- Related: L14-014, L14-042.

### L14-021 An n = 1 example could not have satisfied the brief's own premise
- Source: `2026-09-12T17-21-49.txt:81` (brief T3(e)), final ledger row for T3(e).
- Raised by: orchestrator brief
- Status at last mention: dead (the brief asked for something logically impossible)
- Content: The brief asked for "an explicit small example ($n=1$ or 2, $D=4$)" of an adjoint-paired family that is *not* unitary-up-to-scalar. But every nonzero $1\times1$ matrix is a scalar multiple of a unitary, so no $n=1$ example can satisfy the premise. Only $n=2$ works.
- Lead: none stated.
- Related: L14-013, L14-015.

### L14-022 Seed S2's inference is wrong: a tuned one-port realises equal widths at irregular positions
- Source: `2026-09-12T19-12-16.txt:77` (seed S2), `:131` and `:146` (messages), scratch exec at `:134`; the conclusion survives in `notes/resonances/astra-freeassoc.md` but the seed's original inference is transcript-only.
- Raised by: orchestrator brief (seed), prover (refuted)
- Status at last mention: dead (false inference), corrected in final
- Content: Seed S2 argued: rank-one coupling to a lattice gives equal widths trivially; for GUE-like positions it gives Porter--Thomas widths generically; therefore "GUE positions with equal widths" is the *fingerprint* of a chaotic Hermitian $H$ with **scalar** loss, not of "cavity plus one lead". The prover built the inverse design explicitly — prescribe poles $a=(-2,-0.7,0.4,1.8)$ at common width $w=1/4$, form $P=\prod(z-(a_k-iw))$, take $U=\operatorname{Re}P$, $V=\operatorname{Im}P$, read the closed energies $h$ as the roots of $U$ and the coupling squares as $2V(h)/U'(h)$, set $H_{\rm eff}=\operatorname{diag}(h)-\tfrac i2 jj^{\mathsf T}$ — and recovers the prescribed poles exactly. So equal widths at *arbitrary irregular* positions are realisable by one passive channel with specially tuned couplings.
- Lead: the special information in RH, read this way, sits in the **couplings**, not in the loss operator. Consequence: any argument of the form "equal widths ⟹ the loss is scalar ⟹ the generator is normal-plus-constant" is invalid, and the programme cannot get Hermiticity for free from RH.
- Related: L14-026, L14-027.

### L14-023 Seed S4's monodromy claim is false: positive canonical-system energy does not make transfer matrices elliptic
- Source: `2026-09-12T19-12-16.txt:79` (seed S4), `:131` (message), scratch exec at `:134`; correction at `notes/resonances/astra-freeassoc.md:226-234`.
- Raised by: orchestrator brief (seed), prover (refuted with an exact example)
- Status at last mention: dead (false statement), corrected in final
- Content: Seed S4 asserted "positivity of the Hamiltonian (mass density) is what makes a J-unitary monodromy similar to a unitary (Krein space: eigenvalue pairs $\mu, 1/\bar\mu$ collapse to the circle exactly when the form is definite)". The prover's two-slab counterexample: $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\mathsf H_1=\operatorname{diag}(4,1/4)$, $\mathsf H_2=\operatorname{diag}(1/4,4)$, both positive with $\det\mathsf H=1$, transfer $T_i=-J\mathsf H_i$ (quarter-period slabs); the monodromy $T_2T_1$ has eigenvalues $\operatorname{diag}(-16,-1/16)$, manifestly off the unit circle. Periodic positive media have forbidden bands.
- Lead: the relevant positivity must belong to the **spectral operator or its boundary response** (the Weyl/Herglotz function), not to a spatial monodromy. The Kraus analogy "inverse pairing = J-unitary, positive $\mathsf H$ = the missing adjoint pairing" is therefore only valid with that distinction made.
- Related: L14-029.

### L14-024 The local Euler phase factors are unimodular but not individually inner in the channel half-plane
- Source: `2026-09-12T19-12-16.txt:80` (seed S5), `:152` (message), scratch exec at `:134`.
- Raised by: orchestrator brief (seed), prover (refuted)
- Status at last mention: corrected in final
- Content: Seed S5 drafted "$S(\tau)$ is an Euler product of local unimodular factors $S_p$, each an inner function whose zeros lie on $\operatorname{Im}\tau=-1/2$". The prover's check evaluates, for $p=2$, $L=\log p$, $\tau=-iy$ with $y\in\{0.25,0.49,0.51\}$: the local factor $R=(1-q/p)/(1-p^{-1}/q)$ with $q=e^{-2i\tau L}$, against the genuine disk Blaschke factor $b=(q-1/p)/(1-q/p)$. The moduli disagree: $R$ is unimodular on the real line but not an inner function of the lower half-plane.
- Lead: this kills the cheapest route to "factorised scattering": one cannot write $S$ as a product of local *inner* factors and read off zeros factor by factor. If one wants a Thouless/Furstenberg reading of the explicit formula, the factors must be replaced by $2\times2$ matrices whose boundary determinant carries the phase — i.e. one is thrown back onto a genuinely noncommuting chain.
- Related: L14-023, L14-028.

### L14-025 The completed channel delay differs from the physical cusp delay by a rational term
- Source: `2026-09-12T19-12-16.txt:152` (message); the consequence is at `notes/resonances/astra-freeassoc.md:270`.
- Raised by: codex prover
- Status at last mention: corrected in final
- Content: "the completed channel delay differs from the physical cusp delay by a rational term". Consequence: positivity of the completed model delay is *not* an unconditional positivity assertion for every convention of physical cusp delay; in the Selberg-file convention $q_\phi=2m$, whose Fourier transform carries the prime dips, the archimedean part and the pole boundary constant, and none of those may be discarded when comparing signs.
- Lead: Wigner time delay is convention-sensitive at the level of a rational function. Any "physical observable sensitive to equal widths" built from the delay must first fix which delay.
- Related: L14-004, L14-026.

### L14-026 The exit-Gram conditioning grows: an equivalent inner product on K_S may not exist
- Source: `2026-09-12T19-12-16.txt:134` (scratch exec) and `:146` (message); numbers at `notes/resonances/astra-freeassoc.md:99`.
- Raised by: codex prover
- Status at last mention: raised, not pursued further
- Content: Assigning width $1/4$ to the cached zeta ordinates and forming the Cauchy/exit Gram matrix $G_{mn} = 2w/(2w - i(a_n-a_m))$ with $w=1/4$: the condition number is about **9.88** for the first 24 ordinates and about **701** for the last 24 of a 3000-ordinate cache; the largest neighbouring overlap grows from about 0.570 to 0.939. The message draws the inference: "a useful Hermitian bond space may require more than an equivalent inner product on the existing model space".
- Lead: concrete and cheap — push the window to higher height and larger size and see whether the condition number is unbounded. If it is, a *bounded* metric change on $K_S$ is ruled out and any Hilbert--Polya inner product must live on a different completion or a different bond space. That would be a genuine structural negative result about the Riemann channel.
- Related: L14-022, L14-042.

### L14-027 Nothing here forbids superradiance; seed S6's implicit hope is unsupported
- Source: `2026-09-12T19-12-16.txt:81` (seed S6); answered at `notes/resonances/astra-freeassoc.md:101` and `:321`.
- Raised by: orchestrator brief (question), prover (answered negatively)
- Status at last mention: dead (the hoped-for mechanism does not exist)
- Content: Seed S6 asked "superradiance in one-channel systems segregates widths (one broad, many narrow), the opposite of uniform; **what forbids superradiance here?**" The answer is: nothing. Nothing about having one exit generically forbids strong-coupling superradiant segregation. Further, GUE-like zero spacing does not establish that a physical cusp cavity belongs to a time-reversal-broken ensemble, and supplies no prohibition of superradiance; and Hecke commutativity alone does not prove Poisson statistics for arithmetic Laplace spectra.
- Lead: if a superradiance-prohibition is wanted it must come from arithmetic (an identity about the coupling vector $j$), not from the one-channel structure. Concretely: sweep the opening strength in a closed Hermitian model and watch for width splitting, as the final file's check 16.2 proposes.
- Related: L14-022.

### L14-028 Seed S8's question — is there a Ramanujan property for a lead / for continuous spectrum? — was not answered
- Source: `2026-09-12T19-12-16.txt:83` (seed S8); the final file ranks the corresponding mechanism 5th with "currently acting on the wrong spectral sector".
- Raised by: orchestrator brief
- Status at last mention: raised, not pursued
- Content: The seed asked: the Weil--LPS channels are exactly Ramanujan because of Deligne, and "the analogue of the cusp there is absent (compact). What is the compact-vs-cusp dichotomy in expander language: is there a notion of 'Ramanujan for the continuous spectrum / for a lead'?" The final note does not define such a notion; it observes only that Hecke/Ramanujan rigidity is the strongest arithmetic input available but acts on the discrete (Laplace) sector, whereas the zeros are scattering poles.
- Lead: define "Ramanujan for a lead" — e.g. a uniform bound on the resonance widths of an open graph/quotient in terms of the degree — and test it on the Weil--LPS channels with one vertex opened. Consequence if it worked: a finite, checkable toy version of the exact statement RH is asking for.
- Related: L14-027.

### L14-029 The prime screw kernel: an unconditional positivity test that does not input the zeros
- Source: `2026-09-12T19-12-16.txt:138` (scratch exec); the resulting check is `16.3` in the final file, but the script itself is transcript-only.
- Raised by: codex prover
- Status at last mention: raised; the script exists only in the transcript
- Content: The check builds Suzuki's screw function from the primes alone,
  $\Psi(t) = 8(\cosh(t/2)-1) - \sum_{n}(\log p/\sqrt n)(t-\log n)_+ + t\cdot\tfrac12(\psi(1/4)-\log\pi) + \tfrac14\big(C - e^{-t/2}\Phi(e^{-2t},2,1/4)\big)$ with $C=\pi^2+8G$ ($G$ = Catalan's constant), forms the kernel $K_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(|t_i-t_j|)$ on a grid $t_k=k/8$, and compares its eigenvalues with the Gram matrix $K_z = 2\operatorname{Re}(ff^*)$, $f_{k}= (e^{it_k\gamma}-1)/\gamma$, built from 3000 cached ordinates. It also checks the delay identity $4\operatorname{Re}(\xi'/\xi)(1+2ix)$ against the sum of Poisson kernels at width $1/4$.
- Lead: this is the notebook's one *prime-side* positivity test whose failure would be evidence against RH rather than an artefact. Worth turning into a committed script with controlled truncation and cancellation error — the final file itself cautions that "a failed Cholesky step at floating-point precision is not a negative Weil vector until truncation and cancellation errors are controlled".
- Related: L14-023, L14-026.

### L14-030 The drafted Artin--Schreier sign law is false; the counterexample is q=3, g = 2x^2 + x^4, n = 1
- Source: `2026-09-12T21-42-08.txt:91` (brief T7(b)), `:117`, `:129`, `:171` (messages), scratch execs at `:125`, `:134`, `:159`.
- Raised by: orchestrator brief (drafted from 40 brute-force cases), prover (refuted and replaced)
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted, from numerics, "$S_n(g) = -(-\eta(-1))^n \overline{\operatorname{Tr}E_g^n} = -(-\eta(-1))^n\operatorname{Tr}(E_{-g}^n)$ for all $n\ge1$, equivalently $S_n(g)=(-1)^{n+1}\eta(-1)^{d_n}\operatorname{Tr}E_g^n$". The prover found the counterexample *before writing anything*: for $q=3$, $g=2x^2+x^4$ (i.e. $a=(2,1)$), $n=1$, the exponential sum is $S_1=3$ whereas the drafted formula gives $-3$. A second exact counterexample is $(q,a,n)=(5,(1,1),2)$. The corrected law is $S_n = (-1)^{n-1}\det(S\,\vert\,\ker P(S))\operatorname{Tr}E_g^n$, i.e. the correction is the determinant of the cyclic shift **on the radical** of the quadratic form, not the universal $\eta(-1)^{d_n}$; equivalently the periodic sign $1-2\cdot\mathbf 1_{2h\mid n}$ where $h$ is the $q$-power ceiling of the multiplicity of $z+1$ in $P$. Verified by 628 exact finite-field checks (the script at `:159` diagonalises the trace form over $\mathbb F_q$ for $q\in\{3,5,7\}$ and $n$ up to 9).
- Lead: the "fermionic sign" of the ring count is *not* simply the sign of the Frobenius permutation corrected by $\eta(-1)$; it is a determinant on a degenerate direction. Anywhere the notebook says "the sign is the Frobenius permutation sign", the radical term has to be carried.
- Related: L14-031, L14-032, L14-035.

### L14-031 The drafted failure class "q | n" is wrong: the exact criterion is P(-eta(-1)) != 0
- Source: `2026-09-12T21-42-08.txt:91` (brief T7(b)) and `:173` (message).
- Raised by: orchestrator brief
- Status at last mention: dead (false localisation of the failure), corrected in final
- Content: The brief guessed "if the drafted law fails for some class of $n$ (e.g. $q\mid n$), say so". In fact failure is not confined to characteristic-divisible extension degrees: the exact necessary and sufficient condition for the drafted law to hold for the *whole* sequence is $P(-\eta(-1))\ne0$, where $P(z)=\sum_j a_j(z^j+z^{-j})/2$. For the corresponding $L$-polynomial claim $L(g,T)=\det(1+TE_g)$ the condition is $\sum_j(-1)^j a_j\ne0$, i.e. $P(-1)\ne0$.
- Lead: a clean coefficient criterion on the Artin--Schreier polynomial that decides whether the transfer matrix *is* the Frobenius up to sign. Cheap to test on any family; tells you in advance which curves the MPS picture describes exactly.
- Related: L14-030, L14-036.

### L14-032 The rebound/renewal fixed-point equation is false: the vacuum is absorbing and the integral diverges
- Source: `2026-09-12T21-42-08.txt:87` (brief T5(e)) and `:131` (message).
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted "this is reinsertion at the rebound state $\Omega=|{\rm vac}\rangle\langle{\rm vac}|$ in the enlarged space, and the fixed-point equation $\rho_\infty\propto\int_0^\infty Z(t)\Omega Z(t)^*dt$ is solved by $\Omega$ itself". The prover: "it has the stated pure fixed state, but inserting that absorbing state into the proposed renewal integral makes the integral diverge". Precisely: $\Omega$ lies outside the original $K_S$, and in the enlarged space the integral equals $T\Omega$ up to cutoff $T$. The vacuum is **absorbing**, not a finite-holding-time renewal state.
- Lead: this is a real obstruction to the SHW renewal reading of the Riemann channel. The reinsertion state cannot be the vacuum; it must be some other state with finite mean holding time, and *which* state it is remains undetermined (the final resonance note ranks this mechanism 7th precisely because "its reinsertion state is undetermined"). Finding an arithmetically natural reinsertion state is the concrete next step.
- Related: L14-040, L14-042.

### L14-033 Infinite-parity rigidity under positivity alone: left open, and the obstruction is named
- Source: `2026-09-12T21-42-08.txt:81` (brief T2(c)) and `:150` (message).
- Raised by: orchestrator brief (proposed a Landau route), prover (could not close it)
- Status at last mention: open
- Content: The brief proposed closing the infinite case by applying Landau's theorem to the diffuse part of the signed Radon measure $f=\text{supertrace}-\text{comb}$, or to $\text{supertrace}+\text{comb}$. The prover: "The unrestricted infinite case remains unresolved; the file identifies the missing control over atomic contributions." The obstruction is precise: flipping infinitely many parities can produce **negative prime atoms** in $\mu-\text{comb}$, and the proposed positive-measure argument needs those atoms separated from the diffuse part. What *is* proved: the finite-flip theorem (extended to arbitrary flips of trivial-zero parities provided only finitely many nontrivial zeros are flipped), and a theorem under the stronger domination hypothesis $\mu\ge\text{comb}$.
- Lead: the missing step is a separation of the atomic and diffuse parts of a signed measure whose Laplace transform is $2\sum_{\rho\in F}m_\rho/(s-\rho)+\ldots$. If closed, positivity of the supertrace would force **all** the parities, i.e. the Phantasm's grading would be fully determined by positivity rather than assumed.
- Related: L14-039.

### L14-034 The Artin--Schreier module keeps a redundant register at J = 0
- Source: draft `2026-09-12T21-42-08_L0147` / patch at `:191`; the correction is in the final file but the module itself was never fixed.
- Raised by: codex prover
- Status at last mention: corrected in the note, but the code defect stands
- Content: For $J=0$ the minimal transfer matrix is the scalar quadratic Gauss sum $E_g=\sum_x\psi(a_0x^2)$, and $E_0=q$. `scripts/artin_schreier_mps.py` instead retains a redundant $q$-state register: its positive-power traces agree with the scalar, but it carries extra **zero eigenvalues**, so it is not the claimed one-dimensional scaled unitary. Similarly $\operatorname{Tr}E_0^n=q^n$ for all $n$ but the nonzero spectrum of $E_0$ is just $\{q\}$ with $q^J-1$ invisible zero eigenvalues for $J\ge1$.
- Lead: concrete code fix. Also a general caution: positive-power traces are blind to zero eigenvalues and nilpotent blocks, so any "the transfer matrix *is* the Frobenius" claim proved by traces gives equality of net multisets only, never operator similarity (that needs semisimplicity, H-FROB-SS).
- Related: L14-035, L14-041.

### L14-035 The drafted universal odd block of the super-transfer matrix is false
- Source: `2026-09-12T21-42-08.txt:91` (brief T7(d)); final ledger.
- Raised by: orchestrator brief
- Status at last mention: dead (false statement), corrected in final
- Content: The brief drafted the graded matrix $\mathbb E := [E_0\oplus(1)]_{\rm even}\oplus[-\eta(-1)\bigoplus_{a\in\mathbb F_q^*}E_{ag}]_{\rm odd}$ with $\operatorname{str}\mathbb E^n=N_n=\#C(\mathbb F_{q^n})$. It is false: at $q=3$, $g=2x^2+x^4$ its claimed supertrace is $-2$ while the actual projective count is $10$. The fix replaces each character block by $F_{ag}$ from the corrected spectral recipe; the simple block survives only under the endpoint condition $P(-\eta(-1))\ne0$.
- Lead: the "super-transfer matrix" of the finite-field prototype — the concrete model for the Phantasm's grading — does not have the naive form. Any attempt to lift the grading from $\mathbb F_q$ to $\zeta$ must lift the *corrected* block.
- Related: L14-030, L14-031, L14-036.

### L14-036 The replacement L-polynomial construction: roots-of-unity rotations, verified exactly at q=3, a=(1,1), h=3
- Source: `2026-09-12T21-42-08.txt:173` (message), exact sympy check at `:204`, draft text at `_L0214`.
- Raised by: codex prover
- Status at last mention: stated and verified; the exact symbolic check is transcript-only in this form
- Content: When the endpoint condition fails, the message describes "a finite spectral construction using roots-of-unity rotations and the supplied polynomiality hypothesis". The exact check: for $q=3$, $a=(1,1)$, $h=3$, with $E$ the $3\times3$ matrix $E_{xa}=\omega^{(x^2+ax)\bmod 3}$, $\omega=e^{2\pi i/3}$, $D=\det(I-TE)$ and $L=1-i\sqrt3\,T+\tfrac{-3+3i\sqrt3}{2}T^2+\tfrac{9+3i\sqrt3}{2}T^3$, sympy verifies $[L(g,T)D_g(T)]^3=\det(I-T^6E_g^6)$ identically.
- Lead: the $h$-th root construction is what replaces $L=\det(1+TE)$ in the degenerate case. Worth committing as a script: it is the only worked example of the corrected recipe.
- Related: L14-031, L14-035.

### L14-037 The exact symplectic matrix of the Artin--Schreier transfer, checked over 105 Weyl labels
- Source: draft text at `_L0214` / `_L0218`, patch at `:191`.
- Raised by: codex prover
- Status at last mention: corrected in final (the check is reported there; the phrasing of the check differs)
- Content: The transfer matrix $E_g/\sqrt q$ is a Clifford operation implementing an explicit symplectic $M_g\in Sp(2J,\mathbb F_q)$, given by formula (7.13). A bounded Python check verified the symplectic identity and centred Weyl covariance for $(q,a)=(3,(0,1)),(3,(2,1)),(3,(0,1,1)),(5,(1,1)),(5,(1,2,1))$: every Weyl label in the three $q=3$ cases and the position/momentum basis labels in the two $q=5$ cases, **105 covariance comparisons**, maximum entrywise residual $7.56\times10^{-16}$. The brief's H-WEIL-REP, with "up to a phase" covariance, was also corrected: arbitrary label-dependent phases allow Weyl displacements and so do not characterise a Weil implementer up to scalar; the covariance must be *centred* and exact.
- Lead: $d_n=\dim\ker(M_g^n-I)$ and the Weil bound is saturated exactly when $M_g^n=I$. That makes the saturation question a finite group-order question in $Sp(2J,\mathbb F_q)$ — fully computable.
- Related: L14-030, L14-034.

### L14-038 H-MM1 was handed over as an assumption but had to be proved, on a specified weighted space
- Source: `2026-09-12T21-42-08.txt:75` (brief hypothesis list: "H-MM1 ... take as given") and `:152` (message), draft at `_L0214`.
- Raised by: orchestrator brief (as a given), prover (proved it and qualified it)
- Status at last mention: corrected in final
- Content: The brief listed H-MM1 (the birth--death generator on $\mathbb N$ with constant rates $\lambda<\mu$ has spectrum $\{0\}\cup[-(\sqrt\lambda+\sqrt\mu)^2,-(\sqrt\lambda-\sqrt\mu)^2]$) as a fact to assume. The prover proves it: detailed balance $\pi_k\lambda=\pi_{k+1}\mu$ makes the backward generator self-adjoint in $L^2(\pi)$; conjugating by $f_k\mapsto\sqrt{\pi_k}f_k$ gives off-diagonal $a=\sqrt{\lambda\mu}$ and diagonal $-(\lambda+\mu)$; the sine transform gives the band; the boundary equation $x=-\lambda+az$ forces $z=\sqrt{\lambda/\mu}$, $x=0$ (the constant function), and the resolvent recurrence excludes everything else. Crucially the infinite prime-chain spectrum is then the **closure of the union of finite Minkowski sums** of the bands on a *specified stationary weighted space* — neither the closure nor the choice of space can be omitted.
- Lead: "the prime chain's spectrum is a union of real intervals and contains no trace of the zeros" is only true on that weighted space; on unweighted or unbounded closures nothing is asserted. Anyone arguing "the zeros are not in the Bost--Connes chain" must pin the space.
- Related: L14-042.

### L14-039 Positivity does not fix the ladder's parity
- Source: `2026-09-12T21-42-08.txt:85` (brief T4(b)), final ledger.
- Raised by: orchestrator brief (noticed), prover (confirmed and sharpened)
- Status at last mention: raised; stands as a genuine indeterminacy
- Content: The brief already noted "the ladder's parity is not fixed by positivity", giving both variants: over $\mathbb C\oplus K_S$ alone the supertrace is $2P_+ + e^{-t/2}/(e^t-1)$, and with the ladder counted even it is $2P_+ + 2e^{-t/2}/(e^t-1)$, both positive. The prover confirms and adds: exact trace equality forces the *net graded spectral datum*, but positivity alone fixes neither the ladder nor (for now) the infinite parity assignment.
- Lead: if the Phantasm is to be an actual physical object, something other than positivity must decide whether the archimedean ladder $-(k+1/2)$, $k\ge1$, is bosonic or fermionic. That is a concrete, sharply posed question — and the answer would be a real structural datum about the archimedean place.
- Related: L14-033.

### L14-040 The vacuum-decay Lindbladian doubles the zero list, so it is not the T4 graded datum
- Source: `2026-09-12T21-42-08.txt:87` (brief T5(d)), final ledger.
- Raised by: orchestrator brief (drafted single-copy), prover (corrected to doubled)
- Status at last mention: dead as drafted, corrected in final
- Content: The brief drafted "each zero appears once as an odd mode $-\bar\rho/2$ and once as its conjugate". Since the zero multiset is already conjugation-invariant, the combined formal odd list has multiplicity $2m_\rho$ at each zero-mode value — twice T4's single-copy datum. So the concretely-constructed vacuum-decay channel does **not** realise the forced Phantasm spectrum; it realises its double.
- Lead: a structural mismatch between the one object that exists (the absorbing-vacuum CPTP semigroup) and the one object that is forced (the graded datum with supertrace $2P_+$). Resolving it — a square root, a real structure, a further grading — is a well-posed next step.
- Related: L14-032, L14-042.

### L14-041 The population block's formal trace |Tr Z|^2 is not a form factor
- Source: `2026-09-12T21-42-08.txt:87` (brief T5(d)), final ledger.
- Raised by: orchestrator brief (drafted, with a self-imposed caution), prover (declined to prove it)
- Status at last mention: raised, not pursued
- Content: The brief drafted that the even population block carries the pair sums $-(\bar\rho_n+\rho_m)/2$ "whose formal trace is $|\operatorname{Tr}Z(t)|^2$, i.e. the form factor $\sum_{n,m}e^{-(\bar\rho_n+\rho_m)t/2}$ of the zeros (state as a remark; no claim about pair correlation is to be proved)". The prover records: only a formal expression or a finite-cutoff equality is available, because the pair spectral list violates the finite-order condition (G2) and a product of two distributional traces is undefined. No form-factor or pair-correlation limit is claimed.
- Lead: if the Montgomery pair correlation is ever to appear inside this framework it will have to be as a regularised population trace with a stated regularisation, since the naive product does not exist. Worth knowing before anyone builds a pair-correlation argument on this block.
- Related: L14-040.

### L14-042 The harness ate the file; it was recovered by replaying apply_patch calls out of the codex rollout log
- Source: `2026-09-12T12-54-39.txt:161` (the orchestrator's second prompt) through `:232`.
- Raised by: orchestrator brief / codex prover
- Status at last mention: resolved; infrastructure lesson
- Content: After the first session finished, the orchestrator reported: "The file `notes/selberg/astra-proofs.md` you created was accidentally overwritten by the harness with your final chat message (it now has 2 lines)." Rather than rewriting from memory, the prover located its own rollout JSONL at `~/.codex/sessions/2026/09/12/rollout-2026-09-12T12-54-39-....jsonl`, extracted the five `custom_tool_call` entries whose input starts `text(await tools.apply_patch(`, JSON-decoded each patch, deleted the corrupted file, and replayed the patches through the `apply_patch` binary in order — restoring the file byte-for-byte.
- Lead: this is a reusable recovery procedure for any lost codex output, and it is the reason this lane's transcripts contain complete patch bodies at all. It also explains the truncation pattern (the extractor caps lines at 20 000 chars). Worth writing into the env-quirks notes.
- Related: -

## Small but possibly consequential

1. **L14-014** — "adjoint pairing buys reality" is too weak: *every* Kraus family is conjugation-symmetric, so reality is free and the real content of adjoint pairing is the nonnegative ring count.
2. **L14-013** — the Kraus dichotomy's "both pairings" case needs $B^\dagger B = I$ exactly; a scale as innocent as $B=2I$ changes the transfer operator, its critical radius and its trivial roots.
3. **L14-026** — the exit-Gram condition number rising from ~9.88 to ~701 across the zero cache is the only quantitative evidence in the campaign against a bounded metric change on $K_S$; one more run at higher height would settle it.
4. **L14-002** — the inverse-determinant slip means the Ihara/Selberg dictionary was, as drafted, upside down; worth re-checking every place in the report that pairs a tower with a determinant.
5. **L14-009** — "the prime circles are blind to the zeros" is really the statement that the zero-free line keeps $\zeta$'s zeros off the imaginary axis; the blindness *is* a known theorem in disguise.
6. **L14-034** — positive-power traces are blind to zero eigenvalues and nilpotents, so every "the transfer matrix is the Frobenius" claim in the notebook is a net-multiset claim, not an operator claim, unless semisimplicity is added.
7. **L14-039** — nothing yet decides whether the archimedean ladder is even or odd; a physical Phantasm must answer this, and the question is sharply posed.
8. **L14-012** — the cut name $A_{j_1\ldots j_k}$ (with $A_\varnothing = e^{tK}$) is the continuous ring word; without it the repo has the theorem but not the combinatorial object, which is what a continuous Ihara--Bass would need.

## Dead routes recorded

| Drafted statement (transcript line) | Verdict and correction |
|---|---|
| "$\Lambda(\sigma) = -(d/d\sigma)\log D(\sigma)$" — `12-54-39:81` | False sign. The flat-trace transform is $+\partial_\sigma\log D = -\partial_\sigma\log(D^{-1})$ (`12-54-39:111`). |
| "the graph analogue of $D$ is $1/\det(1-uT)$" — `12-54-39:81` | False. The analogue is $\det(1-uT)$ itself; the graph log-derivative has the same sign as $\partial_\sigma\log D$. |
| "all resonances of the first band lie on $\operatorname{Re}\sigma=-1/2$ iff every $r_j$ is real ($j\ge0$)" — `12-54-39:81` | False on every compact connected surface: with $j=0$ the band contains $0$ and $-1$. Corrected to "no **nonconstant** complementary-series parameter" (`12-54-39:111`). |
| "$C(t)=\sum\Lambda(n)/n\,[\delta(t\mp2\log n)]+A(t)$" with positive prime weights — `12-54-39:83` | Sign is negative (prime *dips*), and a $+1/2$ archimedean boundary constant is missing, coming from the $r=0$ Abel boundary $+\pi\delta_0(r)$ (`12-54-39:111`, `:115`). |
| Selberg trivial zeros at $s=-k$ with multiplicity $(2g-2)(2k+1)$ — `12-54-39:71` | Listed among the corrected drafted items ("zero multiplicities") in the final RESULT line. |
| "both pairings iff every $B_i$ is a nonzero scalar multiple of a unitary; $\operatorname{Ad}(B^\dagger)=\operatorname{Ad}(B)^{-1}$ iff $B^\dagger B$ scalar" — `17-21-49:81` | False for exact matrix and exact superoperator pairing. Correct condition: $B^\dagger B=I$. Disproved by $B=2I$ (`17-21-49:114`). |
| "give a 1x1 or 2x2 counterexample where $\operatorname{spec}(T)\setminus S_0$ is not conjugation-closed (Kraus case)" — `17-21-49:81` | No such example exists: every Kraus family has the antiunitary $C(v\otimes\lvert i\rangle)=v^\dagger\otimes\lvert i\rangle$ commuting with $T$. Counterexamples exist only among non-Kraus superoperators (`17-21-49:114`). |
| "$n=1$ or 2, $D=4$" example of an adjoint-paired non-scalar-unitary family — `17-21-49:81` | $n=1$ is impossible: every nonzero scalar is a scalar multiple of a unitary. |
| "$\mu\mapsto r^2/\mu$, the linear map (the functional equation)" — `17-21-49:79` | Not linear; a holomorphic reciprocal map. Also, $W=M$ needs conjugation symmetry in addition to reciprocal symmetry. |
| Dyson product $\ldots R_{j_k}\ldots R_{j_1}\ldots$ without free propagators between jumps — `17-21-49:83` | False for noncommuting $K,R_j$; the full time-ordered product with $e^{(t_{i+1}-t_i)K}$ between every pair of jumps is required. |
| $\operatorname{Tr}_{M_n\otimes M_n^*}e^{t\mathcal L}$ — `17-21-49:83` | Wrong space: that is the $n^4$-dimensional superoperator space. The intended trace is $\operatorname{Tr}_{M_n}$. |
| "$S$ = the two trivial modes from the poles of $\xi$ at $s=0,1$" — `17-21-49:87` | The notebook's $\xi$ is entire; those poles belong to $\Lambda_\zeta$ on the explicit-formula side. Take $S=\varnothing$ (`17-21-49:121`). |
| "every zeta function has side A, a nonnegative count of rings" as a universal premise — `17-21-49:71` | Holds in the stated Kraus settings only; not a property of arbitrary superoperators, and distinct from Weil positive-definiteness even when it holds. |
| Seed S2: "GUE positions with equal widths is the fingerprint of chaotic Hermitian $H$ with scalar loss, not of cavity plus one lead" — `19-12-16:77` | False inference. A tuned one-port realises equal widths at arbitrary irregular pole positions; the special information sits in the couplings (`19-12-16:131`, exec `:134`). |
| Seed S4: "positivity of the Hamiltonian is what makes a J-unitary monodromy similar to a unitary" — `19-12-16:79` | False. Two positive slabs $\operatorname{diag}(4,1/4)$, $\operatorname{diag}(1/4,4)$ give monodromy eigenvalues $\operatorname{diag}(-16,-1/16)$. Positive periodic media have forbidden bands (`19-12-16:131`). |
| Seed S5: "each local Euler factor $S_p$ is an inner function whose zeros lie on $\operatorname{Im}\tau=-1/2$" — `19-12-16:80` | Unimodular on the real line but **not** individually inner in the channel half-plane; checked numerically at $p=2$, $y=0.25,0.49,0.51$ against the true Blaschke factor (`19-12-16:152`). |
| Seed S6: "what forbids superradiance here?" — `19-12-16:81` | Nothing does. Neither one exit nor GUE-like spacing prohibits superradiant width segregation (`notes/resonances/astra-freeassoc.md:101`, `:321`). |
| "$S_n(g)=-(-\eta(-1))^n\overline{\operatorname{Tr}E_g^n}$, equivalently $(-1)^{n+1}\eta(-1)^{d_n}\operatorname{Tr}E_g^n$" — `21-42-08:91` | False. Counterexamples $(q,a,n)=(3,(2,1),1)$ (where $S_1=3$ but the law gives $-3$) and $(5,(1,1),2)$. Correct law: $S_n=(-1)^{n-1}\det(S\vert\ker P(S))\operatorname{Tr}E_g^n$, the determinant of the shift on the **radical**; equivalently the periodic sign $1-2\cdot\mathbf 1_{2h\mid n}$ (`21-42-08:117`, `:129`, `:171`). |
| "failure, if any, is confined to $q\mid n$" — `21-42-08:91` | False localisation. The exact criterion for the whole sequence is $P(-\eta(-1))\ne0$; for $L=\det(1+TE_g)$ it is $P(-1)\ne0$, i.e. $\sum_j(-1)^ja_j\ne0$ (`21-42-08:173`). |
| Super-transfer $\mathbb E=[E_0\oplus(1)]\oplus[-\eta(-1)\bigoplus_a E_{ag}]$ with $\operatorname{str}\mathbb E^n=N_n$ — `21-42-08:91` | False: at $q=3$, $g=2x^2+x^4$ its claimed supertrace is $-2$ while the projective count is $10$. Each character block must be replaced by the corrected $F_{ag}$. |
| "$\rho_\infty\propto\int_0^\infty Z(t)\Omega Z(t)^*dt$ is solved by $\Omega$ itself" — `21-42-08:87` | False. $\Omega$ is outside $K_S$ and absorbing; the integral equals $T\Omega$ up to cutoff and diverges (`21-42-08:131`). |
| "each zero appears once as an odd mode plus once as its conjugate" — `21-42-08:87` | The zero multiset is already conjugation-invariant, so the odd list has multiplicity $2m_\rho$: the vacuum-decay model realises the **double** of the forced graded datum. |
| "the formal population trace is $\lvert\operatorname{Tr}Z(t)\rvert^2$, the form factor" — `21-42-08:87` | Only formal or finite-cutoff: the pair spectral list violates (G2) and a product of distributional traces is undefined. No pair-correlation statement follows. |
| T2(c): close the infinite-parity case by Landau on the diffuse part — `21-42-08:81` | Not provable under positivity alone; negative prime atoms of $\mu-\text{comb}$ block it. Proved only under the added domination $\mu\ge\text{comb}$; the unrestricted case is left **open** (`21-42-08:150`). |
| "H-MM1 ... take as given" — `21-42-08:75` | Not merely given: proved here, and the infinite prime-chain spectrum is the *closure* of the union of finite Minkowski sums on a *specified* stationary weighted space, not a bare union. |
| H-WEIL-REP's "up to a phase" Weyl covariance — `21-42-08:75` | Too weak: arbitrary label-dependent phases admit Weyl displacements and do not characterise a Weil implementer up to scalar. Centred exact covariance is required. |
| "$\alpha_i=-\lambda_i(E_g)$ uniformly in $n$" (notebook `prop:as-transfer-matrix`, flagged by the brief itself) — `21-42-08:69` | Confirmed false in general; holds only under the endpoint condition. The brief flagged it, and T7 supplies the replacement. |
