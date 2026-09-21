# Positivity, arithmetic products, and RH: checkpointed lane

Status: COMPLETE, 2026-09-19. Owner: positivity_products subagent.

Scope: audit repo learnings on Deligne fixed-loss tensor amplification, Rosati arithmetic products, and Weil/Suzuki positivity. Deliver precise candidate reductions and falsification tests while marking RH-equivalent positivity as the unresolved target, not progress.

Durability: this file is updated on disk during the investigation. Existing repository sources are the default; every newly relied-on network result will be saved under this lane with its URL and retrieval time. No network results have yet been used.

Initial sources located: `HANDOFF.md`; `report/sections/06c_ring_norm_inputs.tex`, `06d_ring_norm_elliptic.tex`, `06e_ring_norm_bosonic_nogo.tex`, `06f_ring_norm_genus_two.tex`, `07_deligne_via_graphs.tex`, `08b_weil_positivity.tex`, `08c_weil_positivity_continuous.tex`; `notes/weil-positivity.md`; `notes/resonances/astra-freeassoc.md`; `notes/reviews/weil-positivity-2026-09-12.md`.

Initial reading: HANDOFF states the priority is a prime-defined, graded Riemann object with zeros as odd modes; finite prime-only detailed balance gives real relaxation spectra, while the zero-built vacuum Lindbladian has no arithmetic construction. The next positivity route explicitly listed is Suzuki's prime-defined screw kernel. Any proposed product must explain arithmetic generation and positivity, rather than insert the zeros spectrally.

## Checkpoint 1: established obstruction inventory

- The tensor-power engine needs nonnegative local coefficients AND an independently controlled pole set of the amplified global object. Ordinary graph transfer powers fail the latter: the interesting spectrum remains poles. See `report/sections/07_deligne_via_graphs.tex:132–160,195–208`.
- What kills the Deligne loss is not tensor powers alone: slicing any product over a one-dimensional base costs only one factor `sqrt(q)`, independently of tensor exponent. See `report/sections/07_deligne_via_graphs.tex:224–236`.
- Rosati positivity is the arithmetic proof of the Frobenius moduli. The constructed odd transfer already inputs those moduli; complete positivity of its MPS transfer is not an independent RH proof. The genus-two audit explicitly separates a spectral realization from the arithmetic Hodge metric. See `notes/ring-norm-tensor/astra-proofs.md:1013–1037`.
- Suzuki's existing local source is `refs/src/2206.03682/screwz_15.tex`; the repo already emphasizes that finite-interval positivity is insufficient and is even unconditional on sufficiently small intervals. Existing numerical Cholesky factors are a discovery aid only; an arithmetic recurrence with a sign-controlled extension law would be new useful structure. See `notes/resonances/astra-freeassoc.md:214–240,604–631`.

All statements above are repository audit findings; no external facts newly introduced and no network access used yet. Next: inspect exact Suzuki formula and derive interval-extension and amplified-loss tests with explicit hypotheses.

## Checkpoint 2: a precise obstruction to independent positive prime blocks

**New elementary deduction (proved here; no RH assumption).** For one prime power `n=p^k`, put `a=log(n)>0`, `w=Lambda(n)/sqrt(n)>0`, and `h_a(t)=(|t|-a)_+`. Its contribution to Suzuki's prime-defined `Psi` is `-w h_a(t)`, hence its contribution to the screw kernel is

`Delta K_a(t,u) = w[h_a(t-u)-h_a(t)-h_a(u)]`.

Choose `a/2 < A < a` and the two nodes `A,-A`. Then this contribution is the matrix

`w(2A-a) [[0,1],[1,0]]`,

with eigenvalues `+w(2A-a)` and `-w(2A-a)`. Thus each separate prime-power contribution is **indefinite at its first visibility on a symmetric interval**. This rules out the naive ansatz that the exact kernel is a fixed archimedean positive background plus a sum of independent positive prime-power Gram blocks. Positivity, if established arithmetically, must use correlated cross-prime/archimedean compensation, a nonlinear update, or a different representation. The deduction does NOT refute positivity of the total kernel.

Exact input formula: `refs/src/2206.03682/screwz_15.tex:95–116,178–188,248–265`; repo version `notes/resonances/astra-freeassoc.md:606–624`.

**Useful exact two-point diagnostic.** For the full even `Psi`, `Psi(0)=0`, the two-node matrix at `A,-A` has eigenvalues `Psi(2A)` and `4Psi(A)-Psi(2A)`. Any candidate sum-of-squares factorization must reproduce both. This makes the cancellation mechanism visible before large Gram matrices are built.

**Avoid a rediscovery.** Suzuki already proves `Psi(t)>=0` for every real `t` is equivalent to RH, and also `Psi(t)=O(1)` iff RH (`screwz_15.tex:400–425`). Merely replacing matrix positivity with this scalar positivity is not new progress.

## Checkpoint 3: exact fixed-loss amplification lemma and its missing input

**Elementary deduction, conditional reduction.** Let `Sigma` be the centered retained divisor (modes counted only after even/odd cancellation), invariant under `lambda -> -conj(lambda)`. For each integer `k>=1`, suppose an independently defined arithmetic product provides a scalar meromorphic response `R_k(z)` such that:

1. **Survival:** for every `lambda in Sigma`, `k lambda` is a genuine pole of `R_k` (nonzero net residue/divisor; an abstract tensor eigenvector alone is insufficient).
2. **Arithmetic growth control:** `R_k(z)` is the Laplace transform of locally integrable `r_k(t)` with `|r_k(t)| <= M_k(1+t)^{d_k} exp(epsilon_k t)`, where `M_k,d_k` may depend arbitrarily on `k` and `epsilon_k/k -> 0`.
3. The Laplace expression represents the same meromorphic continuation as the response in (1).

Then the Laplace integral is holomorphic for `Re z>epsilon_k`, so survival forces `k Re lambda<=epsilon_k`. Letting `k->infinity` gives `Re lambda<=0`; the reflection symmetry gives `Re lambda=0`. This proves RH **if** the original divisor is the centered Riemann divisor and all hypotheses are proved arithmetically.

This is a useful specification of the missing product, not evidence that it exists. A matrix coefficient may miss a mode, and a signed trace may cancel it; either breaks (1). Meromorphic resonances are not automatically Hilbert-space eigenvalues, so estimates on an unrelated `L^2` semigroup do not establish (2) for the needed response.

**Why ordinary tensoring does not help.** From `||T(t)||<=M exp(c t)` one only gets `||T(t)^tensor k||<=M^k exp(k c t)`, i.e. `epsilon_k=kc`. The amplification bound recovers `Re lambda<=c`, with no improvement. Constants `M_k` can be exponential or worse in `k` without ruining the lemma: only the coefficient of `t` must be sublinear in `k`. Thus testing the exponential loss, not the state-space dimension or prefactor, is the right early feasibility test.

Connection to repo: `report/sections/07_deligne_via_graphs.tex:137–151,224–236` contains the two finite-field fixed-loss arguments. The abstract response formulation above isolates the analogous analytic requirements without claiming a Riemann arithmetic product or hiding the cancellation problem.

## Checkpoint 4: stationary-increment Toeplitz form, with sparse arithmetic updates

**Elementary deduction.** Fix a mesh `h>0`, let `v_j` be formal kernel vectors for `K(jh,lh)`, and take differences `d_j=v_(j+1)-v_j`. Their formal Gram matrix is Toeplitz:

`<d_j,d_l> = c_h(j-l)`,

`c_h(m) = Psi((m+1)h)+Psi((m-1)h)-2Psi(mh)`.

On a finite consecutive grid containing `0`, `v_0=0`; cumulative summation reconstructs all remaining `v_j` from the increments. Thus the nonzero-node screw Gram matrix and this increment Toeplitz matrix are congruent by an invertible matrix. Their PSD conditions are exactly equivalent. Proving Toeplitz PSD for every finite size on a sequence of meshes tending to zero implies full kernel positivity by continuity; hence RH by Suzuki. This is a computationally useful equivalent formulation, not a proof.

The arithmetic part becomes especially transparent. For one prime power with `a=log n>=h`, write `a/h=L+theta`, `L>=1`, `0<=theta<1`. Its contribution to `c_h(m)` vanishes except at

- `m=+/-L`: contribution `-w h(1-theta)`;
- `m=+/-(L+1)`: contribution `-w h theta`.

Coincident zero weights are omitted. Proof: the central second difference of a hinge is the triangular hat of width `2h` at its breakpoint; `h_a` has breakpoints at `+/-a`. Consequently each prime power gives at most four Toeplitz diagonals, with exact logarithmic weights, and its formal trigonometric polynomial is

`-2 w h[(1-theta)cos(L x)+theta cos((L+1)x)]`.

This supplies a focused discovery problem: derive a sign-controlled innovation/Schur recurrence for the **sum** of archimedean and sparse prime Toeplitz pieces. A decomposition assigning positive energies separately to these prime pieces is impossible by Checkpoint 2. The Toeplitz change of basis also exposes boundary terms cleanly and reduces repeated evaluations of `Psi` from quadratic to linear in grid size.

Caution: no convergence of an infinite prime trigonometric series is asserted. The formula is exact for each prime contribution and every finite matrix at its finite prime cutoff.

## Checkpoint 5: reproducible offline implementation and numerical sanity check

Created `positivity-products-check.py` in this directory, with atomic JSON checkpoints in `positivity-products-check.json`. It uses the prime formula, never zero ordinates; all prime powers through the required maximum difference are included. The script first validates the indefinite prime block and the sparse second-difference formula in exact rational arithmetic, then checks the total kernel/increment congruence and spectra at 40 and 70 decimal digits.

Numerical results for mesh `h=1/4`, nodes `[-A,A]` except the zero vector:

| A | nonzero nodes | min eigenvalue of K | min eigenvalue of increment Toeplitz matrix | final Schur pivot |
|---|---:|---:|---:|---:|
| 2 | 16 | 0.0210158467482652494 | 0.000747659951048785 | 0.0345767522234277915 |
| 4 | 32 | 0.0146176837661784046 | 0.000375484666271565 | 0.0273738285363350814 |

The values agree through the 32 digits printed at both precisions; the congruence residual is zero at the working arithmetic in these grids. These are **numerical sanity checks**, not interval certificates and not evidence of a new RH mechanism. The small positive increment eigenvalue also warns against seeking a mesh/interval-independent lower bound.

Run offline: `python3 notes/rh-strategy-2026-09-19/positivity-products-check.py`. Dependency already available in the environment: `mpmath 1.3.0`; exact initial checks use Python's standard-library `fractions`.

## Checkpoint 6: user steering — decay modes and the physical cMPS bridge

The user emphasizes that decay modes, represented naturally by a cMPS, are the crucial target. This changes the interpretation of the positivity search: seek arithmetic **output/exit energy identities for the amplitude decay modes**, not merely an abstract positive kernel.

**Finite-dimensional exact model.** Let `A` be the no-event amplitude generator carried by the vacuum/excited odd coherence, `C` the collection of physical exit amplitudes, and `G>0` a stored-energy form. A passive realization obeys

`A* G + G A = - C* C`.

For a stable observable pair `(C,A)`, the output Gram is

`G = integral_0^infinity exp(t A*) C* C exp(t A) dt`,

and the identity follows by differentiating the integrand. In a vacuum-decay Lindbladian this is precisely the norm lost into physical jump histories; the cMPS letters, including the free propagators between jumps, are the natural objects from which to calculate it. Source connection: `report/sections/08c_weil_positivity_continuous.tex:44–65` proves the Dyson history norm formula; the Riemann extension needs regularized resonant data, not an automatic finite-dimensional transplant.

For an eigenmode `A v=lambda v`, the exact identity gives

`-Re(lambda) = ||C v||^2 / (2 <v,Gv>)`.

Thus **uniform decay is uniform exit energy per stored modal energy**. An arithmetic proof of

`||C v||^2 = 2 kappa <v,Gv>`

for every retained resonant eigenmode would force the critical decay width `-Re(lambda)=kappa`. This is a precise modal target that does not require Hilbert–Schmidt normality of `A`. It also does not assert simplicity of zeros. The difficult input is an arithmetic construction of `C,G` and the equality for the actual Riemann resonant modes; defining them from already-centered real zero frequencies would be circular.

A stronger, easier-to-state identity `C*C = 2 kappa G` on the whole retained state space yields `A*G+GA=-2 kappa G`. It permits nonnormality in the original coordinates but gives metric skew-adjointness after centering. In finite dimension it therefore also excludes Jordan blocks. Because Weil positivity is blind to Jordan blocks, this full identity is stronger than divisor RH; keep the modal version separate.

**Why generic exit positivity is insufficient.** The cusp lane reports, for `A=diag(s_i-1)` and `G_ij=1/(1-conj(s_i)-s_j)`, the identity `A*G+GA=-G-11*`. Its modal width is

`-Re(s_i-1)=1/2 + |1|^2/(2 G_ii)`.

So the positive exit Gram records a mode-dependent extra escape term; it exists throughout the allowed strip. It does not force equal widths. The next physical calculation should therefore isolate a prime-defined mechanism that fixes the exit-to-storage ratio, or compensates that extra escape via correlated return amplitudes, rather than re-prove positivity of this Gram.

### Concrete bridge from the prime kernel to integrated cMPS amplitudes

Use the repo's Riemann no-event normalization `A` with modes `-conj(rho)/2`, and put `B=2A+1/2`; its formal centered modes are `1/2-conj(rho)`. For an arithmetic input boundary vector/distribution `b`, define integrated vectors

`V(t) = integral_0^t exp(r B) b dr`.

A candidate physical construction should establish the exact identity

`<V(t),V(u)>_G = Psi(t)+Psi(u)-Psi(t-u)`.

It must establish this from the physical letters and prime/archimedean data, including the mixed `t,u` correlations; agreement only at `t=u` or only at finitely many times is insufficient. If it did, the right side would be a Gram kernel and Suzuki would imply RH. This is therefore an exact **bridge specification**, not a proved new criterion. Its advantage is that it says which cMPS observable to calculate.

Under RH the familiar mode components are `(exp(i gamma t)-1)/(i gamma)`, matching Suzuki's Eq_109, but those components must not be used as the construction. The input `b` may be a distribution rather than a Hilbert vector because infinitely many unit-weight modes are involved; it is the time-integrated vectors `V(t)` that must have finite norm. This is precisely why the integrated prime kernel is a better finite-energy target than an unsmeared trace at zero.

The Toeplitz quantities in Checkpoint 4 are now the Gram entries of finite time-bin amplitudes `V((j+1)h)-V(jh)`. Their Schur complements are the energy of the next output amplitude after projecting onto previously observed amplitudes. That is a physical interpretation of the sought arithmetic recurrence. Prime-power contributions to this energy are not independent PSD channels (Checkpoint 2); interference among physical histories and the archimedean sector is essential in this representation.

## Checkpoint 7: an architecture test forced by the prime kinks

**Elementary deduction.** The prime formula implies, at each prime-power time `a=log(p^k)>0`,

`Psi'(a+) - Psi'(a-) = -log(p)/sqrt(p^k)`.

All archimedean terms are smooth for positive time, and only this hinge turns on at `a`. Therefore the exact integrated covariance has genuine first-derivative kinks; on the diagonal the jump in the derivative of `K(t,t)=2Psi(t)` is `-2log(p)/sqrt(p^k)`.

For a bounded generator `B` on a Hilbert space and a Hilbert vector `b`, `V(t)=integral_0^t exp(rB)b dr` is entire as a Hilbert-valued function and its diagonal norm is real analytic on the real line. Consequently **no such bounded-generator, finite-energy-boundary realization can equal the exact Suzuki covariance**. This includes every fixed finite-dimensional, time-homogeneous cMPS amplitude model of this form. An exact physical candidate needs an unbounded generator/distributional boundary, explicit delay propagation at prime lengths, or another mechanism genuinely producing these singularities. A finite approximation is still useful, but equality to the whole prime kernel cannot be claimed.

This gives a cheap stopping test before testing global positivity: calculate the jump at `log 2`. If the proposed exact prime-history model is analytic there, its bridge identity is impossible. A smoothed comparison must specify the smoothing on both sides and control its removal.

## Ranked next tests, with success and stopping conditions

1. **Arithmetic cMPS time-bin covariance and exit ratio.** Input: a candidate whose jump/free-history letters and boundary distributions are specified from primes/archimedean data without zero ordinates. Output: the first nontrivial mixed covariance `K(t,u)` around the `log 2` and `log 3` ridges, together with its passive energy balance and modal exit/storage ratio. Required hypotheses: a defined domain and positive physical norm, controlled history sums, correct Riemann time normalization `B=2A+1/2`. Success is an identity or structural recurrence reproducing the prime kink and mixed terms, not a fitted matrix. Stop that ansatz if it is analytic at `log 2`, assigns an independent positive block to each prime, or produces the density-operator pair-difference spectrum in place of the amplitude modes. Only pursue uniform width after the actual arithmetic bridge is verified.

2. **Nonlinear innovations for the prime-defined Toeplitz matrices.** Input: exact finite prime cutoffs, the sparse four-diagonal prime updates from Checkpoint 4, and the full archimedean piece. Output: an arithmetic formula for each next Schur pivot `d-k* K^{-1}k`, or the generalized PSD Schur condition if the prior block is singular. Required hypotheses: certified entry error bounds for any claimed sign; every support/grid size in a proved recurrence, not just sampled grids. Success is a sign mechanism derived from arithmetic/history interference. Stop numerical enlargement when it produces only more positive matrices without a recurrence; a putative negative vector must be interval-certified and converted to a smooth test before interpreting it as mathematical failure. Current script is exploratory high precision, not that certification.

3. **Product loss and spectral survival audit.** Input: a proposed arithmetic product/slicing operation acting on the actual retained amplitude divisor. Output: an explicit table for `k=1,2,3` of surviving scaled poles, even/odd cancellation, growth exponents `epsilon_k`, and the claimed general law. Required hypotheses are exactly Checkpoint 3. Success is a mechanism suggesting/proving `epsilon_k=o(k)` while retaining every target pole. Stop if all available bounds are `epsilon_k=k epsilon_1`, if the pole is erased by a supertrace, or if a tensor product counts a different object without an arithmetic projection. The genus-two Jacobian/curve projector warning is concrete evidence that this last failure is easy (`06f_ring_norm_genus_two.tex:213–221`).

## Completion and recovery

Status: COMPLETE for this ideation/audit lane, 2026-09-19. No RH proof is claimed. New proved-here results are the independent-prime-block obstruction, the sparse increment Toeplitz algebra, the conditional fixed-loss lemma, the finite passive modal width identity, and the bounded-generator kink obstruction. The global positivity, arithmetic cMPS bridge, uniform modal exit ratio, and arithmetic product remain open targets. Numerical evidence is separated above.

Files: this report; `positivity-products-check.py`; `positivity-products-check.json`; `positivity-products-sources.sha256`. The computation was completed at both precisions with atomically written outputs. Every substantive result was written to this report before being sent in chat.

Network provenance: **no web results used and no new download required**. Suzuki's primary TeX, the reviewed local proofs, and the report shards were already on disk; source hashes below identify the exact local inputs. The parent is preparing whole-repository snapshots including `refs/src`, so recovery does not require a live network. The script itself runs offline with Python 3 and mpmath 1.3.0.
