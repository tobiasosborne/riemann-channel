# Cusp bridge and exact spectral centers — independent lane

Started 2026-09-19. Status: incremental checkpoint; this file is the durable record, not the final chat. No external sources newly used at this checkpoint. Source references below point to material already cached in this repository.

## Initial orientation

The current repository explicitly stops at **H-CUSP-BRIDGE**, rather than proving RH: modular scattering zeros are at `s = rho/2`, the corresponding proposed flow resonance is `lambda = rho/2 - 1`, and the compact Haar-pairing proof is unavailable because the Eisenstein Laurent coefficients are outside `L²` (HANDOFF.md, section “An infinite object…”, especially the final two bullets; exact line references to follow).

The compact construction is a useful structural prototype, but its positive branchwise form yields unitary centered flow **if and only if** the additional Selberg `1/4` coercivity holds; its full algebraic block further fails at a Jordan threshold (report/sections/03e_selberg_letters.tex:144–178). Therefore an existence claim for an appropriate positive metric alone is not evidence of a new mechanism.

The cusp prime-comb damping identity is explicitly only an identity of atomic measures and implies no operator identification or RH statement (report/sections/09c_selberg_tower_cusp.tex:122–138). Any proposed affine bridge must supply an intertwiner on regular/resonant data, not infer it from the prime weights.

## Work still running

1. Read the precise modular scattering and Riemann model formulas and their reviewed proofs.
2. Derive the exact affine map and its functional-equation pairing; separate arithmetic identities from operator statements.
3. Seek a concrete positive-pairing obstruction and a tractable test of cusp boundary renormalization.
4. Record sources, claim status, and ranked tests here.

## Checkpoint 2 — exact affine correspondence and a new testable obstruction

**Established repo facts (reviewed).** The detailed modular proof is `notes/selberg-letters/astra-proofs.md:339–393`; its hypotheses and missing H-CUSP-BRIDGE are explicit at 351–358. Its Maass–Selberg identity is 375–385. The Riemann model is only an assumed modal realization at `report/sections/04b_phantasm_forced.tex:246–265`; it is not an independently completed cusp identification.

**Checked deduction A (scalar affine maps, not an operator theorem).** Put `s = rho/2`, `lambda = s - 1`, and `b = -conj(rho)/2`. Then `b = -1 - conj(lambda)`. The Riemann functional-equation partner `rho' = 1-conj(rho)` has `lambda' = -1/2 - conj(rho)/2`, and therefore **`b = lambda' + 1/2`**. Thus, as multisets with multiplicities, the Riemann modal spectrum is the cusp-flow subset shifted by `+1/2`, after FE relabelling. This is stronger bookkeeping than just comparing centers, but supplies neither an intertwiner nor a bounded similarity. It also explains why the correct centers are `-3/4` and `-1/4`. The alternative same-label formula uses an adjoint/conjugate and reverses the sign; conflating these two maps is dangerous. Inputs: shard 03f:29–49 and shard 04b:249–252.

**New deduction B in progress (Maass–Selberg cross pairing).** For distinct scattering poles `s_i` with leading Laurent coefficients `e_i` and scalar constant-term coefficients `c_i`, the same bivariate Laurent-coefficient extraction as `astra-proofs.md:386–390` gives

`<Lambda^Y e_i, Lambda^Y e_j> = c_i conj(c_j) Y^(1-s_i-conj(s_j))/(1-s_i-conj(s_j))`

with the repository's linear-first convention. All denominators have positive real part because `Re(s_i), Re(s_j) < 1/2`. Consequently subtracting the full constant-term divergence entrywise leaves the **zero matrix**, rather than a positive resonance norm. A full proof and the normalized Cauchy-kernel Lyapunov identity will follow. This is a concrete obstruction to the naive finite-part renormalized Haar pairing, not a no-go for all nonlocal or weighted pairings.

## Checkpoint 3 — cross-pairing lemma proved

**Lemma (conditional only on the repo's Maass–Selberg identity; independent deduction).** Let `s_1,...,s_N` be distinct modular scattering poles with `0 < Re(s_i) < 1/2`, and use only their leading Laurent eigenstates. Switch to the conventional matrix inner product antilinear in its first argument. Divide the `i`th truncated state by `c_i Y^(1/2-s_i)`. Its Gram matrix is exactly

`K_ij = 1 / (1-conj(s_i)-s_j)`.

Proof: extract the leading Laurent coefficient in each parameter from `astra-proofs.md:378–381`. Only the product of the two scattering coefficients survives. The other terms have a pole in at most one parameter. The normalized formula follows. Set `a_i=1/2-s_i`. Then

`K_ij = integral_0^infinity exp(-conj(a_i)t) exp(-a_j t) dt`.

This is strictly positive definite for distinct `s_i`: any null vector would give a finite exponential sum vanishing identically, and its first `N` derivatives at zero give an invertible Vandermonde system. Thus this positive pairing exists for arbitrary distinct parameters in the whole strip; it does not select RH.

For the proposed cusp-flow generator `A=diag(s_i-1)` the exact identity is

`A* K + K A = -K - 11*`,

so at the RH center

`(A+3/4 I)* K + K (A+3/4 I) = (1/2) K - 11*`.

For `N >= 2` the right-hand side **cannot vanish**, because `K` has rank `N` and `11*` has rank one. In particular, the natural normalized cusp Gram pairing cannot make the centered flow unitary, **even if every pole satisfies RH**. For `N=1` it vanishes exactly at `Re(s_1)=1/4`.

The shift `C=A+1/2 I` satisfies `C* K+K C=-11*`: this is exactly a finite one-exit dissipativity identity. It is a promising structural match to the scalar model's one-channel dissipation, but is not yet an intertwiner with the whole model space.

A second consequence: subtracting the entire constant-term divergence from each unnormalized cross pairing yields zero identically, so the straightforward Hadamard finite part of this particular pairing cannot supply a positive norm on these leading states. Different pairings, subleading Laurent data, or nonlocal boundary terms are not ruled out.

**External source checkpoint.** A live search located the primary Bonthonneau–Weich paper, *Ruelle–Pollicott resonances for manifolds with hyperbolic cusps*, arXiv:1712.07832; the full result is saved immediately in `cusp-bridge-web-search.json`, with source URLs and retrieval timestamp. Its abstract proves a cusp resonance construction, not the needed first-band/Eisenstein positive-pairing statement. Full source retrieval is in progress under `cusp-bridge-sources/1712.07832/`.

## Checkpoint 4 — a source closes only one bridge component; an old sign needs repair

**Newly checked primary source.** Bonthonneau–Weich, DOI 10.4171/JEMS/1103, full PDF https://ems.press/content/serial-article-files/32642, browsed 2026-09-19 and immediately saved in `cusp-bridge-web-primary.json`. Theorem 1 (PDF p. 2, extracted lines 71–75) gives the globally meromorphic flow resolvent from compactly supported smooth functions to distributions, with finite-rank residues. Corollary 1 (PDF p. 3, lines 92–102) explicitly treats cofinite Fuchsian orbifolds with a torsion-free finite-index normal subgroup; its footnote names `PSL(2,Z)` and `Gamma(2)` (lines 122–123). Thus the finite-rank modular resolvent component of H-CUSP-BRIDGE already has a verified primary theorem. The source says the identification with discretized transfer spectra / first band remains future work (p. 3, lines 109–125). It therefore does **not** supply the needed multiplicity-preserving Eisenstein first-band map or positivity. Parent is archiving the complete TeX/PDF; my ordinary shell fetch failed DNS, with failure metadata saved under `cusp-bridge-sources/1712.07832/retrieval.json`.

**Checked local inconsistency (not an RH issue).** Shard `report/sections/04_riemann_channel.tex:71–75` writes `Z(t)* k_lambda = exp(-it conj(lambda)) k_lambda` for `lambda=gamma/2-i beta/2`, then claims this scalar decays. Direct substitution gives real exponent **`+beta t/2`**, so the displayed formula cannot be right for a contraction. The same error appears in `notes/riemann-channel-note.md:59–64`. For the stated lower-half-plane Hardy space and compression `Z(t)=P_K exp(it x)|K`, the correct kernel eigenformula is `Z(t) k_lambda = exp(it conj(lambda)) k_lambda`, giving generator eigenvalue `-beta/2+i gamma/2 = -conj(rho)/2`, consistent with the later assumption in shard 04b:249–252. The elementary Hardy proof and an executable sign check will be recorded next. Existing shards were not edited in this lane.

## Checkpoint 5 — a finite Gram-level bridge and sign proof

**Checked deduction C (exact finite Gram-level bridge).** Keep the preceding finite leading-state span and `C=diag(s_i-1/2)`. Define lower-half-plane points `tau_i=i conj(C_i)=Im(s_i)-i(1/2-Re(s_i))`. These are zeros of the repo's inner symbol by the functional equation: their zeta labels are `rho'_i=1-conj(2s_i)`. With boundary measure `dx/(2 pi)`, the Hardy kernels `k_i(x)=1/(x-conj(tau_i))` have Gram matrix

`<k_i,k_j> = i/(conj(tau_j)-tau_i) = -1/(conj(C_i)+C_j) = K_ij`.

The first equality follows by closing the rational integral in the upper half-plane; its residue is at `conj(tau_j)`. Thus sending each normalized truncated Laurent state to `k_i` gives an **explicit isometry of finite modal spans** and intertwines the diagonal shifted action `C` with the model semigroup restricted to those kernels. This is an unconditional finite Gram identity given the repo's Eisenstein and inner-symbol inputs, even for hypothetical off-line zeros.

The limitation is essential: on the left we have *assigned* the first-band eigenvalue `s_i-1` to an Eisenstein residue; we have not constructed an actual flow resonant state with that eigenvalue, nor shown that truncation intertwines a flow. The isometry is not a bounded map between a specified anisotropic flow space and `K_S`, does not address generalized Laurent/Jordan chains, and does not establish completeness of all kernels in `K_S`. It settles useful algebraic normalization, not H-CUSP-BRIDGE and not RH.

**Hardy-sign proof.** In `H²(C_-)`, multiplication by `exp(-it z)` is contractive for `t>=0`; its adjoint is `P_- exp(it x)`. Reproducing kernels are eigenvectors of this adjoint, with eigenvalue `conj(exp(-it lambda))=exp(it conj(lambda))`. Because a kernel at a zero of `S` belongs to `K_S`, the additional projection onto `K_S` leaves it unchanged. Hence the correct formula for the defined compression is `Z(t) k_lambda = exp(it conj(lambda)) k_lambda`. Taking `lambda=gamma/2-i beta/2` gives decay `exp(-beta t/2)` and frequency `+gamma/2`, in agreement with 04b's generator `-conj(rho)/2`. The erroneous formula in shard 04 instead gives growth and uses the wrong adjoint.

**Numerical check, not proof and not RH evidence.** `cusp_bridge_diagnostic.py` and its generated `cusp_bridge_diagnostic.json` check the exact Lyapunov identities, positive Cauchy Gram matrices, Hardy Gram equality, FE affine relabeling, and truncation normalization on synthetic on-line and off-line FE-paired parameters. All assertions pass. Three-mode on-line centered defect norm is about 2.2544; it is not zero under RH. The old and corrected scalar moduli at `beta=1/2,t=1` are respectively `exp(1/4)` and `exp(-1/4)`. The exact proofs above, not floating-point positivity, establish the claims.

## Checkpoint 6 — physical decay modes and a finite cMPS realization

The user's steering emphasizes that the decay modes are crucial and cMPS is the natural physical setting. The Gram obstruction above should therefore be read as guidance about the **physical norm**, not as a reason to discard cMPS or the decay interpretation.

**Checked deduction D (finite dissipative realization).** Let `R=K^(1/2)`, `B=R C R^(-1)`, and `j=1* R^(-1)` (a one-row exit map). The one-exit identity gives

`B*+B = -j* j`, hence `B=-i H - (1/2) j* j`, `H=(i/2)(B-B*)=H*`.

On the bond `C|vac> + C^N`, use Hamiltonian `0+H` and the single jump `L=|vac> j`, with `L|vac>=0`. The cMPS/no-event letter is `Q=0+B`. These satisfy **`Q+Q*+L*L=0`**, the finite trace-preserving cMPS/Lindblad gauge. The vacuum-to-mode coherences inherit exactly the decay eigenvalues `s_i-1/2`, the Riemann model values after FE relabeling. This is an exact finite construction from the cusp Gram identity. It realizes decay modes as cMPS bond coherences, in the same shape as the repo's vacuum-decay channel (`report/sections/04c_phantasm_channels.tex`, vacuum-decay theorem).

Its limitation: it takes a finite selection of scattering poles as input, has an absorbing pure vacuum, and neither derives the poles from local prime-defined letters nor produces the desired mixed BC critical stationary state. It is an admissible finite physical model, not a proof mechanism yet.

**Why nonnormality is necessary, not a defect.** If `N>=2` and the selected poles lie on `Re(s)=1/4`, all eigenvalues of `B` have decay rate `1/4`, while `B+B*` has rank-one negative part. Were `B` normal, its Hermitian part would be `-(1/2)I`, which has rank `N`, contradiction. Thus the one-exit system with uniform modal widths must be nonnormal. Individual eigenmodes have one lifetime; arbitrary coherent superpositions need not have a single exponential survival norm. Demanding centered unitarity in the *physical* Hardy/cusp norm would wrongly exclude this physically natural possibility. A separate arithmetic positive form could orthogonalize the modes; proving that form from non-spectral data remains the RH-sized step.

## Ranked next tests and success/failure criteria

1. **Extend the cusp Gram/exit identity from leading modes to generalized Laurent data.** Start with a synthetic double scattering pole and take all bivariate Laurent coefficients of Maass–Selberg, including logarithmic cusp terms. Compute the resulting confluent Cauchy matrix and its dissipative generator, then compare with repeated-zero Hardy kernel derivatives. Success: an explicit positive Gram identity and a matching Jordan chain, preserving algebraic multiplicity. Failure: an unavoidable extra boundary term or mismatch in chain length; this would isolate a real obstruction. This is the quickest useful theorem, and it avoids silently assuming zero simplicity. A positive centered unitary form on the full Jordan chain would require semisimplicity and is stronger than RH alone; the dissipative cMPS realization can accommodate Jordan blocks.

2. **Construct the actual noncompact first-band pushforward on regular data.** Use the now-cached Bonthonneau–Weich theorem (`refs/src/1712.07832/preprint.tex:143–164`) for the resolvent; start with one scattering pole and match its distributional state to the Eisenstein Laurent coefficient through the Poisson transform. Success: finite-rank Riesz range, wavefront/cusp-growth conditions, and a nonzero multiplicity-preserving pushforward at `lambda=s-1`, with the sign of `X` explicitly fixed. Failure: proof that the pole occurs only in a related determinant or different flow sector, or a failed domain/Poisson condition. It would then be inappropriate to import compact DFG positivity. BW explicitly leaves the discretized-transfer/first-band identification to further work at `preprint.tex:172`.

3. **Derive the cMPS exit map before solving for zeros.** Seek `j` and `H` from a cusp boundary/Schur-complement or Mayer-tail construction, then compare its finite approximants against the Cauchy Gram realization. Success: analytic formulas from modular branches or prime input, convergence on a fixed domain, and the exact scalar scattering determinant including all elementary factors. Failure: `j` or `H` is fitted from a supplied list of zero locations, or cutoffs change the divisor uncontrollably. The matrix construction above is an exact normalization target and debugging oracle for this test; it is not by itself the desired letters-first derivation.

4. **Test mixed-state reinsertion while preserving the coherence decay sector.** In the finite Gram realization, try an SHW-style rebound density on the modal bond and compute which coherence sectors survive. Success: a stated symmetry/invariant subspace preserving the original decay generator while yielding a nontrivial stationary density, with any extra even population modes tracked. Failure: rebounding alters every zero mode, or the stationary state remains absorbing and pure. The known vacuum construction already has trivial canonical stationary entanglement (`report/sections/04c_phantasm_channels.tex:97–109`), so merely repeating it cannot meet the BC/cMPS objective. No finite approximation can by itself furnish the infinite critical KMS state.

## Source and recovery register

- **Complete primary source now archived by parent:** `refs/src/1712.07832/preprint.tex` and source archive. Checked exact local lines 143–164 (resolvent/orbifold) and 172 (first-band connection left open). Parent's receipt is `notes/rh-strategy-2026-09-19/cusp-source-download.json`. This supersedes the earlier shell-download failure as the current availability status; the failure receipt is retained for recovery provenance.
- Existing primary inputs used locally: `refs/src/1607.08053/main.tex:370–401,592–601` and `refs/src/1108.5659/main.tex:2037–2049,2071–2079`.
- Newly browsed evidence immediately cached: `cusp-bridge-web-search.json` and `cusp-bridge-web-primary.json`, each with URL and retrieval time. The latter is a cached extracted excerpt, not a complete PDF; the parent archive supplies the complete source.
- Reproducible offline diagnostic: `python3 notes/rh-strategy-2026-09-19/cusp_bridge_diagnostic.py`. It writes `cusp_bridge_diagnostic.json`. The final version additionally verifies the physical cMPS gauge and Hamiltonian/exit decomposition for both on-line and off-line synthetic parameters.
- No existing theorem/status shards were edited. The old kernel sign/adjoint issue is recorded here for a separate reviewed correction.

## Claim-status ledger

| Item | Status | What it establishes / does not establish |
|---|---|---|
| Compact Selberg branchwise metric | Reviewed repo result, conditional on listed analytic inputs and extra band bound | A prototype; bound is not derived from letters |
| Scattering pole `rho/2`, non-L² residue | Reviewed repo result using cached divisor/Eisenstein inputs | Actual arithmetic sector; ordinary Haar norm fails |
| BW modular flow resolvent | Checked primary theorem | Existence and finite-rank poles, not their required zeta identification |
| FE spectral shift `C=A+1/2` | Checked scalar deduction | Correct rates and multisets; no flow intertwiner |
| Cross Gram / rank-one Lyapunov formula | New checked deduction from Maass–Selberg | Exact positive dissipative modal pairing throughout strip |
| Naive finite-part pairing is zero | New checked obstruction | Rules out one specific renormalization, not all positive constructions |
| Finite Hardy Gram isometry | New checked deduction, leading states only | Modal normalization bridge; no anisotropic-domain/completeness theorem |
| cMPS vacuum-exit letters | New explicit realization plus existing vacuum theorem | Exact finite physical decay model; poles supplied, stationary state pure |
| Uniform widths with one exit imply nonnormality | New checked finite lemma | Supports cMPS decay interpretation; excludes physical-norm centered unitarity |
| Positive centered metric from arithmetic input | Open / RH-equivalent after spectral identification, plus semisimplicity if full blocks included | The unresolved arithmetic mechanism |
| Diagnostic outputs | Numerical checks | Algebra/sign debugging only; no evidence for RH |

Status: lane report ready for cross-review. It records no proof of RH and no unconditional uniform-width claim.
