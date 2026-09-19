# RH strategy lane: graded channels, cMPS and finite letters

Started: 2026-09-19. This file is the continuously saved checkpoint for agent `/root/graded_channels`.

## Scope and recovery status

Task: audit the repository's graded channels/cMPS, BC symmetry, Lindblad no-go and finite tensor lessons; identify a concrete obstruction or lemma and prioritized reductions toward RH. Files outside `notes/rh-strategy-2026-09-19/` will not be modified. All substantive deductions will be written here as they arise. External material, if needed, will be cached locally with source URLs and retrieval time.

Status: initial checkpoint saved before mathematical analysis. Next: inspect repository instructions/HANDOFF and assigned source shards. No new mathematical claims yet.

## Evidence and claim labels

- **Repository result:** theorem/claim already stated in repository; proof status will be audited where relevant.
- **Checked deduction:** direct reasoning supplied here from explicit assumptions.
- **Conjecture / proposed experiment:** not established, with success and failure criteria.
- **Circularity risk:** hypothesis already encoding desired RH conclusion, especially preassigned zero spectra.

## Checkpoint 1: structural lessons recovered

1. **Repository result, proved:** inverse-paired finite Hashimoto letters derive the companion metric `G=[[I,Sigma/2],[Sigma/2,qI]]` and `C* G C=qG`, but its positivity is equivalent to the *extra* strict band `|Sigma|<2 sqrt(q)`; endpoint roots have Jordan blocks. Thus constructing an invariant Hermitian form is not yet the RH step. Source: `report/sections/03f_selberg_letters_finite.tex:54-89`, labelled-input separation at lines 132-144.
2. **Repository result, counterexample checked by prior prover:** no universal odd-sector Alon–Boppana floor exists. `E=(Ad I+Ad P)/2` kills the odd block, and primitive bounded-degree examples also exist. Therefore "RH because odd relaxation is an extremal expander rate" is unsupported without a separate arithmetic normalization/duality condition. Source: `report/sections/03c_graded_ramanujan.tex:132-144`.
3. **Repository result, explicit algebra:** the parity jump `sqrt(gamma) P` adds `gamma(Ad P-I)`, shifting all odd rates by `-2 gamma` and leaving the even block alone. This preserves an already-uniform odd spectrum but does not force the rest of the dissipator to be scalar. Source: `report/sections/03b_graded_permutation.tex:218-240`.
4. **Repository caution:** actual doubled-bond cMPS supertrace is the parity-twisted closure norm, hence nonnegative; the formal graded spectral transfer and its trace distribution need not have a Kraus realization. Source: `report/sections/04e_cmps_parity_overlap.tex:12-34`. This calculation is marked sketched/unreviewed, unlike the reviewed abstract spectral no-go/realization statements.

Immediate proposed direction: formulate a letter-level *Dirichlet-form defect* for uniform odd dissipation. Test whether arithmetic symmetry constraints kill that defect, rather than assuming a positive metric from preassigned zeta zeros. Next checkpoint will audit the BC cone and the phase-side no-go and make the defect criterion precise.

## Checkpoint 2: a sharper obstruction to the naive prime-plus-parity ansatz

**Checked deduction (finite, bistochastic, fixed Hilbert–Schmidt metric).** Let `H=H_+ ⊕ H_-` with both summands nonzero, `P=diag(I,-I)`, and let `O={X:PXP=-X}` be the *whole* odd operator subspace. Suppose

`L(X)=-i[H0,X] + gamma(PXP-X) + D(X)`,

where `H0` is even, `D` is a GKLS dissipator with jumps `R_a`, `D(I)=0`, and `L` preserves `O`. If `L|_O+2 gamma I` is skew-adjoint in the Hilbert–Schmidt metric, then **all `R_a` are scalar and `D=0`**. Consequently one cannot add genuinely dissipative bistochastic prime noise to a parity jump already accounting for the entire desired decay rate while retaining a manifestly unitary shifted evolution on the full odd block in that metric.

Proof, saved immediately while checking: for a bistochastic GKLS dissipator,

`-Re Tr(X* D(X)) = (1/2) sum_a ||[R_a*,X]||_HS^2`.

This follows by expanding both sides and using `sum R_a R_a*=sum R_a* R_a`. The Hamiltonian commutator is skew, and the parity jump is `-2 gamma I` on `O`, so the hypothesis forces every commutator on the right to vanish for every odd `X`. The commutant of all off-diagonal block matrices is `C I`: test separately arbitrary `|u_+><v_-|` and their reverses to eliminate the off-diagonal blocks of `R_a*` and force the two diagonal blocks to the same scalar. Thus the residual dissipator is zero. No zeta data enter this argument.

**Limits of this obstruction:** it is not a general RH no-go. It does not exclude (i) a nontracial invariant state and a different metric, (ii) a proper odd resonance subspace rather than the entire coherence space, (iii) an invariant positive form not equal to the HS form, or (iv) sharing the target decay rate between parity dephasing and other noises. Equal real parts of eigenvalues alone do not imply HS skew-adjointness. The latter distinction is precisely why this is an obstruction to a *manifest positive-form mechanism*, not to arbitrary spectral fitting.

**Repository evidence motivating the assumptions:** shard 04d's BC cone contains explicit generators with full Weil/Galois/parity covariance, unique tracial stationary density and unequal odd rates (`04d_bc_symmetry_generators.tex:161-182`); imposing all Weyl covariance collapses to pure depolarization and kills oscillations (`:143-157`). Neither symmetry route independently supplies a viable uniform oscillatory block.

Next: validate the identity and obstruction with a small deterministic matrix experiment, derive a constructive tight-frame variant, and write regulator-safe success criteria.

## Checkpoint 3: validated defect identity and a constructive alternative

`graded_channels_checks.py` now independently checks the Dirichlet identity for paired nonnormal even/odd jumps in dimensions `(1|1),(1|2),(2|2),(2|3)` and computes the full odd commutant to have complex dimension one in all four cases. Results are saved in `graded_channels_checks.json`. The first run completed all mathematical assertions but encountered a NumPy integer JSON-serialization error at export; casting that count to a Python integer fixed output, and the full run passes. This is numerical support; the proof above is elementary exact algebra.

**Checked deduction: tight-frame form of the positive-metric problem.** For a parity-covariant bistochastic GKLS generator define

`C_O X = ([R_1*,X],...,[R_m*,X])`, for `X` in the odd subspace `O`.

Then the Hermitian part of the restricted generator is `-(1/2) C_O* C_O`. Hence

`L|_O + c I is HS-skew-adjoint  <=>  C_O* C_O = 2 c I_O`.

Thus the useful letter problem is a **tight-frame identity for commutators**, not merely parity covariance. It makes uniform decay a quadratic identity among arithmetic letters which can be checked without knowing eigenvalues. `R=sqrt(gamma)P` supplies `4 gamma I_O`; with desired `c=1/4`, it exhausts the budget when `gamma=1/8`, explaining the obstruction above. Other noises may instead share the budget.

**Concrete finite witness, not a Riemann model.** On `C^(1|1)`, take grading `P=Z`, arbitrary real `omega != 0`, Hamiltonian `H0=(omega/2)Z`, and jumps `sqrt(1/8)X, sqrt(1/8)Y`. The even generator spectrum is `{0,-1/2}`, the odd block is `-1/4 I` plus a skew-Hermitian rotation with eigenvalues `±i omega`, and the stationary density is uniquely `I/2`. Its supertrace is

`1+e^(-t/2)-2e^(-t/4) cos(omega t) = |1-e^((-1/4+i omega)t)|^2`.

This has the correct two reference rates, mixed stationary state, and additive functional equation at the finite rational-zeta level, from balanced population-exchange letters. It demonstrates an escape from the all-parity damping ansatz. The check script uses the arbitrary frequency `sqrt(2)`, never a known zeta ordinate.

**Material limitation:** these two odd Pauli jumps violate cMPS kinetic regularity (`R_X^2 != 0`). Unitary remixing to raising/lowering jumps makes each square zero but their mutual anticommutator nonzero. Therefore this is valid graded GKLS/finite-norm cMPS data, not a finite-kinetic-energy fermionic cMPS. The repository already warns that kinetic regularity is independent (`report/sections/06h_zeta_conditions.tex:57-62,157-172`). No RH inference follows from this toy, and its arbitrary frequency shows why the trace-identification problem remains indispensable.

## Checkpoint 4: user steering toward physically natural decay modes

The parent relayed the user's emphasis that decay modes and their physically natural cMPS realization are the crucial objective. A small, **kinetically regular**, nonabsorbing cMPS has now been built and checked locally; it is a better next test than the Pauli two-jump toy.

Bond `C^(2|2) = C^2_(parity) tensor C^2_(internal)`, with

- `P=Z tensor I`;
- one physical fermion jump `R=X tensor |0><1|`;
- even Hamiltonian `H=diag(X/2,(X+Z)/2)`;
- `Q=-iH-R*R/2`.

The emitted fermion resets the internal two-level system while flipping bond parity. The even Hamiltonian repopulates the emitting level inside each parity sector. Thus the jump returns to active internal states rather than an absorbing external vacuum. There is only one fermion field and `R^2=0`, so the finite-kinetic-energy CAR regularity condition is satisfied. All matrices are specified before any spectral computation and use no zeta zeros.

**Numerical results:** `regular_cmps_decay_check.py` and `.json` are saved. The stationary density is unique and faithful, with four Schmidt weights approximately `0.0145898, 0.0381966, 0.2618034, 0.6854102` and entropy `0.796154` nats. The generator is parity covariant, trace preserving, mixing, and its parity-closed ring supertraces are nonnegative at all six tested lengths. Its odd modes split into *two* vertical bands at real parts `-1/4` and `-3/4`; both bands oscillate at frequencies numerically `(sqrt(7)±2)/4`. The full odd block is therefore not a one-rate model. The slow band gives a tangible candidate for the **proper physical decay subspace** the user has in mind; the fast band must be classified/cancelled by an actual trace identity, never simply discarded to fit RH. Exact characteristic-polynomial and stationary-state checks are next.

## Checkpoint 5: exact physical correlation selects the slow band

The exact calculation is saved in `regular_cmps_decay_exact.py` and `.txt`. It proves that the odd characteristic polynomial factors into the coprime quartics

`p_s(z)=z^4+z^3+(7/4)z^2+(3/4)z+1/8`,

`p_f(z)=z^4+3z^3+(19/4)z^2+(15/4)z+9/8`.

Their roots are respectively `-1/4 ± i(sqrt(7)±2)/4` and `-3/4 ± i(sqrt(7)±2)/4`. The even characteristic polynomial is

`z(z+1)(2z+1)^2(z^2+z+2)(4z^2+4z+5)/16`.

The exact stationary density is block diagonal, with blocks

`[[1/5,i/10],[-i/10,1/10]]` and `[[3/5,1/5+i/10],[1/5-i/10,1/10]]`.

Its characteristic polynomial is `(100x^2-70x+1)(100x^2-30x+1)/10000`, whose four roots are strictly positive. The generator has a simple zero and all other modes decay, proving uniqueness and mixing without a numerical tolerance. The first exact stationarity print used unsimplified SymPy matrix equality and printed `False`; simplifying its entries gives identically zero, now asserted by the saved executable script.

**Further checked deduction:** for the parity-twisted transfer `L_eta(X)=QX+XQ* - R X R*`, the source/sink resolvent is exactly

`tr[R* (z-L_eta)^(-1)(R sigma)] = 8z(z^2+z+1) / [5(8z^4+8z^3+14z^2+6z+1)]`.

The fast quartic cancels completely, and the numerator is coprime to the remaining slow quartic. Thus a natural emitted-fermion correlation sees **exactly the four slow modes**, all of width `1/4`, despite a faithful mixed stationary bond and eight odd transfer modes. This was not imposed as a projector or fitted from spectral data. The physical two-point prescription is verified against the repository's cached primary source, Haegeman–Cirac–Osborne–Verstraete `refs/src/1211.3935/calculus.tex:380-403`, which inserts the fermionic-sign transfer between `R` and `R*`; the orientation with creation at the left endpoint gives the displayed trace expression in the canonical `l=I,r=sigma` gauge. Finite kinetic regularity is at that source's lines 309–313.

**Interpretation and remaining arithmetic gap:** this is a physically natural *observable decay subspace*, selected by the actual field insertion rather than by deleting unwanted eigenvalues. It is an encouraging finite mechanism for the user's intuition. It does not identify the four frequencies with Riemann zeros, does not make the whole ring zeta a Riemann zeta, and does not show that the band selection persists under arithmetic enlargement. The next lemma to seek is an input/output intertwining identity for prime-defined letters, with a controllable/observable odd subquotient whose entire pole divisor matches the zeta zeros.

**Exact input/output strengthening:** the source-generated Krylov space `span{L_eta^k(R sigma)}` and the sink-observable space each have dimension four. Let `A=L_eta|_odd`, `K=A+I/4`, and use the four columns `v,Kv,K^2v,K^3v` with `v=R sigma`. On that Krylov basis,

`K_comp=[[0,0,0,-9/256],[1,0,0,0],[0,1,0,-11/8],[0,0,1,0]]`.

The explicit rational metric

`G=[[10496/27,0,-32/3,0],[0,32/3,0,-1],[-32/3,0,1,0],[0,-1,0,1]]`

is positive definite and satisfies `K_comp* G+G K_comp=0`, checked exactly using principal minors. This metric is constructed on a space generated by physical letters and field insertion; no eigenvectors or zeta frequencies are assigned. It is not the original physical Hilbert–Schmidt norm, in accord with the distinction emphasized by the cusp lane. The entire construction is still a finite toy. A relation selecting a uniform-width observable subspace, rather than uniformity of all odd coherences, is now a concrete testable mechanism.

## Prioritized next work, with falsifiable acceptance criteria

### 1. Generalize the regular cMPS observable-subspace mechanism (highest priority)

Start from the explicit one-fermion `2|2` toy above and deform its *letters*, not its eigenvalues: `R=X tensor lowering` and `H=diag(H_+,H_-)`, then permit arithmetic finite-level character actions on the internal index. Impose parity, `R^2=0`, canonical gauge, and a faithful stationary bond before seeking uniform widths. Form the physical insertion-generated Krylov space and its observable quotient using the parity-twisted transfer appropriate to the fermion two-point function. Derive its polynomial/intertwining relations directly from the letters.

**Minimal missing identity:** for independently specified local/arithmetic letters, there must be a positive form `G` on the *observable* odd realization with `A_obs*G+G A_obs=-(1/2)G`, and an input/output divisor identity tying precisely these poles (including their algebraic multiplicities) to the Riemann zeros under `b=-conj(rho)/2`. The toy supplies the former in finite dimension but supplies no arithmetic divisor identity. Prime-dependent coefficients may not be fitted to known zero positions.

**Success:** symbolic relations selecting the slow subspace survive a nontrivial family/enlargement, the physical correlation couples to all retained modes, stationarity stays faithful, and the extra fast/population poles are accounted for in the identified correlation or graded determinant. **Failure:** the four-mode cancellation is destroyed by every meaningful arithmetic extension, positivity uses fitted eigenvalues, or a trace/divisor assertion silently suppresses poles visible to required insertions. The immediate experiment is parameter classification of this `2|2` family and exact residues, not an expensive search over guessed zeta ordinates.

### 2. Mixed renewal from the cusp exit, with an observable-sector preservation test

Use the parent's exact finite inverse criterion: given stable dissipative `B`, exit `E=-(B+B*)`, and target cutoff state `sigma`, a scalar reset preserving it exists precisely when `M=-(B sigma+sigma B*)>=0`; then `Omega=M/tr(E sigma)`. Build the physical GKLS/cMPS transfer and recompute the *observable* decay spectrum. The rank-one exit embedding with an external reference vacuum preserves `B` as coherences but has pure stationary entanglement; a mixed reset must be tested on a genuine internal source/sink realization rather than assumed to preserve `B`.

**Success:** an explicit invariant or observable subquotient has an intertwiner with the arithmetic decay generator after reset, a nontrivial stationary density, the correct fermionic insertion, and all extra population modes tracked. **Failure:** physical source/sink poles move, the proposed cMPS violates kinetic regularity, or the bond remains absorbing. A finite cutoff's Gibbs weights are a target to check; no normal density at criticality can simply be assumed on the original BC `l^2(N)` bond (`04c_phantasm_channels.tex:123-131,162-169`).

### 3. Test arithmetic covariance against the commutator-frame defect

In the existing finite BC covariance cone for primes `p=3,5,7`, impose the linear stationary/covariance constraints and examine the Hermitian part on a specified candidate observable coherence space. For a tracial model with a *fixed* metric, `C_O* C_O=2cI` is linear in the Kossakowski matrix; Choi positivity makes this a concrete semidefinite feasibility problem. The full-odd obstruction above is a screening test when a parity jump already spends the entire rate budget. For nontracial or nonnormal models, use the appropriate weighted form and do not import the HS no-go.

**Success:** a symmetry/letter identity forces the defect to vanish on the observable subspace while permitting nontrivial frequencies and faithful stationarity, with exact rational/algebraic certificates. **Failure:** the existing covariant perturbations retain free nonuniform decay parameters (`04d:161-182`), or extra Weyl symmetry kills the oscillatory modes (`04d:143-157`). Full covariance plus stationarity alone has already failed, so merely rerunning that ansatz is not useful.

### 4. Prove a regulator statement for correlations and modal forms

Separate bond dimension, arithmetic level/prime cutoff, continuum spacing, and critical-temperature limits. Each approximant must specify its regular source/sink spaces and physical observable transfer. Check local uniform convergence of the correlation resolvent on contours isolating poles, convergence of residues and their ranks, and controlled noncancellation; then separately check persistence of the positive metric on the intended domain. A finite correlation's scalar pole order alone does not certify geometric/algebraic modal multiplicities (`03d_graded_ramanujan_continuum.tex:78-97`).

**Success:** a common-domain resolvent/intertwining theorem and a nondegenerate limiting form, or a fully specified weaker modal completion sufficient for the divisor, with all limit orders justified. **Failure:** metrics degenerate, modes escape, reference/trivial factors are inconsistent, or divergent prime rates are assumed to produce a normal semigroup. The repository's `1/p` prime-jump cutoff loses mass (`04g_phase_side_lindbladian.tex:121-135`). Our finite companion test gives a second exact warning: `C_n=[[2-1/n,1],[-1,0]]` has positive invariant `G_n=[[1,1-1/(2n)],[1-1/(2n),1]]`, but `lambda_min(G_n)=1/(2n)->0`; the limiting companion has a nonzero Jordan nilpotent and admits no positive invariant metric. Finite positivity alone does not survive a regulator removal in the needed sense.

## Cross-review of the other lanes

**Parent `cmps-renewal-bridge.md`, finite inverse criterion: VALID.** The measure/prepare map is CP, `sum R_ab*R_ab=E`, and `M>=0` with `Omega=M/r` is exactly stationarity. The finite stable Lyapunov equation gives a useful strengthening: every stationary matrix satisfies `X=tr(EX)W`, so the normalized stationary density is unique for every reset `Omega`; faithfulness, rather than uniqueness, needs an additional reachability assumption. This strengthening was sent to the parent. The model is finite-norm cMPS data automatically; kinetic regularity of multiple fermionic jumps is a further constraint and is not automatic.

**Parent grading obstruction: VALID under its exact assumptions.** A parity-even rank-one `E` lies in one parity sector; the other sector of parity-even `B` is skew-Hermitian, excluding stability on the entire bond. This is not an obstruction to the reference-vacuum embedding or to a proper observable coherence space. It matches the premise distinctions in our full-odd HS obstruction.

**`cusp-bridge.md`, Checkpoint 5 Gram/sign calculation: VALID on the finite leading-mode span.** With `tau_i=i conj(C_i)`, the Hardy inner product `i/(conj(tau_j)-tau_i)` is `-1/(conj(C_i)+C_j)`, and `exp(it conj(tau_i))=exp(t C_i)`. The finite isometry has the claimed sign and decay. The stated limits (assigned leading modal data; no actual cusp-flow intertwiner/completeness/Jordan theorem) are essential and correctly retained.

**`cusp-bridge.md`, Checkpoint 6 cMPS realization and nonnormality: VALID.** `B=K^(1/2) C K^(-1/2)` gives `B+B*=-j*j`; `H=(i/2)(B-B*)` is Hermitian with `B=-iH-j*j/2`. The absorbing-vacuum embedding realizes `B` and its conjugate as coherences, not the complete physical generator. If all `N>=2` modal widths are `1/4`, normality would give a full-rank negative Hermitian part, contradicting rank-one exit. Hence demanding uniform physical-norm decay for every superposition is too strong. This supports the cMPS relaxation interpretation and clarifies why a second metric or proper observable subspace is a plausible arithmetic mechanism.

## Recovery register and final status

All work in this lane is saved in this directory. No existing report shard, claims database, or status file was changed. No new network access was needed: the cited cMPS primary paper and all mathematical audit sources were already local. The scripts use only local NumPy/SciPy/SymPy and no input zero lists.

- Narrative/proofs/checkpoints: `graded-channels.md`.
- Dirichlet, tight-frame, Pauli and regulator checks: `graded_channels_checks.py` with `graded_channels_checks.json` (all checks pass).
- Regular cMPS numerical construction: `regular_cmps_decay_check.py` with `.json` (all checks pass).
- Exact stationary state, decay factors, field-correlation cancellation, reachable subspace and positive metric: `regular_cmps_decay_exact.py` with `.txt` (all assertions pass).
- Source identity manifest: `graded-channels-source-manifest.json` (SHA-256 and sizes of used local material).

No proof of RH is claimed. The strongest new positive result is a completely explicit regular fermionic cMPS with mixed stationary entanglement whose physical two-point function selects an observable four-mode decay space on one vertical line, with a positive metric obtained on a letter-generated Krylov basis. The strongest new obstruction isolates when a full-odd, tracial, pure-parity-damping ansatz leaves no room for additional dissipative prime letters.

Final executable audit: after parent review, the exact script now asserts the complete displayed two-point rational identity, denominator degree four, coprimality with its derivative (simple poles), numerator/denominator coprimality, rank-four Krylov basis, exact centered intertwining, metric skew-adjoint identity and all four positive leading principal minors. All assertions pass. This replaces a previously informational printed pole-count statement with explicit acceptance checks.

Audit implementation correction: SymPy's integer-polynomial gcd retains the common constant factor `5` in the denominator and its derivative. The simplicity assertion therefore checks gcd *degree zero* rather than equality to the literal constant `1`. With that normalization fixed, the full exact script completes successfully; this was a check-normalization issue, not a repeated pole.
