# Riemann versus Selberg: physical decay modes in cMPS

Final status: saved at user-requested shutdown; see the completion/status section below. Earlier checkpoint status lines are historical.
Status: working research note, continuously checkpointed. Owner: cmps_decay_comparison subagent. Started 2026-09-19.

## Scope and guardrails

Determine what fixes decay widths in Selberg's geometric realization and what a Riemann cMPS realization would still need to prove. Keep distinct: no-jump bond generator Q, physical completely positive transfer/Lindbladian L, observable or tilted transfer, and geometric flat-trace generator. Resonances need not be Hilbert-space eigenvectors; a common resonance width does not assert common physical norm decay for every state. A full Lindbladian supertrace is not automatically a prime orbit distribution.

## Checkpoint 0

Created before source inspection so the investigation survives interruption. Planned outputs: exact finite-bond calculation of the existing 2|2 toy, its perturbation sensitivity and observable residues; physical comparison; a concrete small theorem or no-go with explicit hypotheses.

## Checkpoint 1 — recovered facts and concrete perturbation target

The exact `2|2` example uses `R=X tensor |0><1|`, `H=diag(X/2,(X+Z)/2)`, `Q=-iH-R*R/2`. It has `R^2=0` **and** `{R,R*}=I`, so the single emission letter is itself a canonical fermionic annihilator on a twofold-degenerate Fock representation. The supplied two-point function uses the signed transfer `L_eta(X)=QX+XQ* - RXR*` and reportedly retains four slow poles after cancellation of four fast poles. I will independently test the cancellation and whether its exact widths survive parity/CAR-preserving perturbations.

The compact Selberg result is much more specific than generic dissipative positivity: first-band resonances satisfy `lambda(lambda+1)=-mu`, where `mu` is a self-adjoint Laplace eigenvalue; the extra bound `mu>=1/4` forces `Re lambda=-1/2`. The resonant state itself need not lie in L2, but its nonzero fibre pushforward is an L2 eigenfunction. Modular Riemann scattering poles instead push to non-L2 Eisenstein Laurent data, losing precisely this self-adjoint spectral inference. The natural cusp Gram gives a rank-one leakage identity, valid for off-line poles as well.

Sources already local: `03e_selberg_letters.tex`, `graded-channels.md` checkpoints 4–5, `cusp-bridge.md` checkpoints 3–6, and `cmps-renewal-bridge.md`. No new online dependency.

## Checkpoint 2 — the four-pole selection is structural; equal widths need an extra condition

**New exact deduction, independently checked symbolically.** Define four Majorana matrices

`w1=X tensor X`, `w2=X tensor Y`, `w3=Y tensor I`, `w4=X tensor Z`.

They satisfy `{wi,wj}=2 delta_ij I`, anticommute with the bond parity `P=Z tensor I`, and `R=(w1+i w2)/2`. For the whole four-parameter, CAR-preserving family

`H=diag(a X+b Z, c X+d Z)`

the signed Heisenberg transfer `L_eta^*(O)=Q*O+OQ-R*OR` preserves `W=span(w1,w2,w3,w4)`. In this basis, with columns giving images,

```
M = [ -1/2,  b+d,    a-c,    0   ]
    [ -b-d, -1/2,     0,    a+c  ]
    [ -a+c,   0,      0,   -b+d  ]
    [   0,  -a-c,    b-d,    0   ].
```

Since the physical output sink `R*` lies in W, its two-point resolvent can have only poles of this 4D matrix, irrespective of the stationary source. This explains the four-mode cancellation by **linear fermionic observable closure**, rather than an eigenvalue projector. The Hamiltonians in this family are quadratic in the Majoranas. This is physically meaningful structure.

However, write `y=z+1/4`. The centered characteristic polynomial has the exact shape

`det(zI-M)=y^4+alpha y^2-2bd y+beta`,

with `alpha=2(a^2+b^2+c^2+d^2)-1/8` and beta given in the saved script/output. If all four poles have real part -1/4, reality of M requires this polynomial to be even in y. Therefore **bd=0 is necessary**. Ordinary parity symmetry, CAR regularity, complete positivity and a faithful mixed stationary state do not enforce it.

The independent perturbation run shows:

- Base `a=c=d=1/2,b=0`: four visible widths exactly 1/4, four other odd residues numerically ~1e-31.
- Change only `b` to `1/100`: four poles remain selected, but visible widths split to approximately `0.246221280502464` and `0.253778719497537`. Stationary state remains faithful. The exact nonzero centered linear coefficient `-2bd=-1/100` proves the splitting is not numerical noise.
- Change a, c or d slightly while preserving b=0: the line persists locally, within a spectral inequality region.
- Add the allowed even interaction `0.01 P` to H: the Majorana closure breaks, and all eight odd poles become visible (the formerly hidden residues are ~4.6e-5 and 1.6e-4). This interaction leaves the original block-diagonal stationary state unchanged because `[P,sigma]=0`.

Thus **mode selection is robust within the quadratic class; uniform widths require a symmetry plus a band inequality; generic parity-even interactions destroy the selection itself**. The toy is a useful finite Selberg-like mechanism, not evidence that CAR alone enforces RH.

Offline artifact: `riemann_vs_selberg_cmps_check.py` with incrementally written JSON of the drift, exact polynomial and all residues. No web query required because the facts used are direct finite-matrix algebra and the cached cMPS primary source.

## Checkpoint 3 — exact symmetry and coercivity, rather than width fitting

For `b=0`, put `N=M+I/4`. The following involution is derived directly from the letters, with no diagonalization:

```
J = [0 0 -1 0; 0 0 0 1; -1 0 0 0; 0 1 0 0],
J^2=I,  J N J=-N.
```

This gives the centered reflection symmetry. It still permits eigenvalues off the imaginary axis, exactly as a functional equation permits off-line zeros.

The full elementary criterion is explicit. With b=0,

`alpha=2(a^2+c^2+d^2)-1/8`,

`beta=(a^2-c^2-d^2)^2+(-a^2-c^2+d^2)/8+1/256`.

All four modes have width 1/4 precisely when `alpha>=0`, `beta>=0`, and `alpha^2-4beta>=0`; these say that both roots of `u^2+alpha u+beta` are real and nonpositive. Strict inequalities give four nonzero distinct imaginary centered roots. Endpoint Jordan behavior must be checked separately if an operator unitarizing metric is claimed.

There is a useful explicit self-adjoint reduction. Write q=1/4 and use the two eigenspaces of J. Then `N=[[0,A],[B,0]]` and

`AB=[[q^2-(a-c)^2-d^2, 2d(a-q)], [2d(a+q), q^2-(a+c)^2-d^2]]`.

For `a>q`, `AB` is self-adjoint in the positive metric `G=diag(a+q,a-q)`. After the corresponding change of coordinates, **minus** this quadratic operator is the real symmetric matrix

```
S = [(a-c)^2+d^2-q^2,  -2d sqrt(a^2-q^2);
     -2d sqrt(a^2-q^2), (a+c)^2+d^2-q^2].
```

Thus a letter-derived symmetry gives a quadratic spectral relation, and the independent inequality `S>=0` yields uniform modal widths. This is a literal finite physical analogue of Selberg's `lambda(lambda+1)=-Delta` followed by `Delta>=1/4`.

For the original toy, S has eigenvalues `11/16 +/- sqrt(7)/4`, both positive. A weak-drive example `a=c=1/20,b=0,d=1/2` retains the four physical output poles but has widths approximately `0.0060754` and `0.4939246`: its reflection symmetry survives while its spectral inequality fails. This is a concrete counterexample to inferring uniform decay from the symmetry alone.

## Checkpoint 4 — exact robustness checks completed

The independent script now computes both output resolvents in exact rational arithmetic. At the base point it reproduces

`F(z)=8z(z^2+z+1)/[5(8z^4+8z^3+14z^2+6z+1)]`.

For the parity-even perturbation `H -> H+P/100`, the same faithful stationary density is exactly stationary, but the reduced output denominator has degree **eight**, with numerator and denominator coprime. Thus the loss of four-mode selection is exact, despite unchanged CAR emission letter, grading, canonical cMPS gauge and stationary density. Numeric residue size is only illustrative; denominator degree and coprimality prove visibility.

The script also asserts the Majorana CAR, invariant four-dimensional signed-adjoint space, exact involution, and positive-metric quadratic symmetrization. Source conventions are directly checked against `refs/src/1211.3935/calculus.tex:309-313,378-403`: kinetic regularity is R squared zero; the physical norm uses the plus-sign transfer, whereas a fermionic field two-point function uses the signed transfer between insertions. These two transfers must not be conflated. The signed transfer is not itself being asserted to be a physical CPTP evolution; it is the required fermionic correlation propagation inside a physical cMPS.

## Compact theorem and proof

**Finite physical decay-selection theorem (proved here).** On the bond `C^(2|2)`, let `P=Z tensor I`, `R=X tensor |0><1|`, `H=diag(aX+bZ,cX+dZ)` with real parameters, and `Q=-iH-R*R/2`. For any stationary density sigma, the physical fermionic output response

`F(z)=tr[R* (z-L_eta)^(-1)(R sigma)]`

has its poles contained in the spectrum of the explicit 4x4 matrix M in Checkpoint 2. This is a regular fermionic cMPS with `R^2=0` and canonical gauge. If `b=0`, its candidate output divisor has the reflection `lambda -> -1/2-lambda`. All four candidate eigenvalues lie on `Re lambda=-1/4` exactly under the three non-strict polynomial inequalities in Checkpoint 3. For `a>1/4`, the stronger strict condition `S>0` from that checkpoint is an explicit letter-defined sufficient condition for centered imaginary eigenvalues. At the base point all four poles are visible, simple, and have width 1/4; the stationary density is faithful and unique.

**Proof.** Direct CAR multiplication gives the four invariant signed-Heisenberg images and M. Since `R*=(w1-iw2)/2` belongs to that invariant space, move the propagator to the sink in the trace pairing; the output is a matrix coefficient of the restricted four-dimensional semigroup. Its resolvent has no other poles. Compute `J(M+I/4)J=-(M+I/4)` when b=0. The resulting characteristic polynomial is `y^4+alpha y^2+beta`, so its roots y are imaginary precisely when the two roots in y squared are real and nonpositive, giving the three inequalities. Diagonalizing J, not M, gives the two blocks A,B; `G AB=(AB)^T G` for `G=diag(a+1/4,a-1/4)>0`, and its negative is similar to S. Therefore `S>0` makes the eigenvalues of N squared negative. At the base point direct exact contraction gives the coprime four-pole response above; the exact stationary density and its positive characteristic roots are recorded in `graded-channels.md` checkpoint 5 and independently satisfy stationarity in this lane's script. Uniqueness follows from the exact simple zero of the full generator established there. QED.

**Two exact limitations, proved by perturbation.** Within the same family a nonzero bd adds the centered odd coefficient `-2bd y`, excluding a common width for all four candidate eigenvalues. At `a=c=d=1/2,b=1/100`, all four have nonzero numerical residues; the exact width obstruction itself uses no numerics. At `a=c=1/20,b=0,d=1/2`, the exact discriminant is `-2399/10000`, so reflection survives and common width fails. Finally, adding `P/100` preserves the stationary density and all basic cMPS/parity/CAR requirements but yields an exactly coprime output denominator of degree eight. The additional four modes cannot be dismissed as unphysical solely from grading.

This theorem is a finite mechanism and counterexample family, not an arithmetic RH theorem.

## Precisely why the Riemann and Selberg decay stories differ

| Question | Compact/discrete Selberg band | Riemann sector in modular scattering | Physical cMPS contribution |
|---|---|---|---|
| What propagates? | Geodesic drift on an anisotropic distribution space; stable transverse grading provides the determinant | Outgoing cusp resonance data, mapped formally to a contraction/model space | Q propagates no-emission amplitudes; L propagates density matrices; L_eta propagates fermionic two-point insertions |
| Why is there a decay center? | Stable/unstable hyperbolic exponents enter the quadratic relation and transverse Jacobians; constant-curvature normalization yields center -1/2 | Poles `s=rho/2` would give flow center -3/4 under RH; shifted contraction modes have center -1/4 | A symmetry of a visible amplitude block can derive a center, as J does in the toy |
| What controls the width? | `lambda(lambda+1)=-mu`, with real L2 Laplace eigenvalue mu; `mu>=1/4` places roots on the line | Eisenstein resonant coefficients are outside L2, so self-adjointness of the Laplacian does not constrain their continued poles this way; positive cusp norm instead includes boundary leakage | A letter-derived quadratic observable closure can yield a self-adjoint reduced operator; a separate coercivity estimate would fix widths |
| Is positivity enough? | Positivity of Delta only gives real branch or vertical line; the 1/4 lower bound is extra | Positive Cauchy Gram and passive rank-one exit exist throughout the zero strip, including hypothetical off-line locations | CP, CAR regularity, mixing and faithful sigma all hold in the width-splitting counterexample |
| Does every mode contribute? | The precise stable complex and its determinant choose a retained divisor | Scattering/flow/model-space maps and multiplicities must be proved; a spectral shift alone is insufficient | Physical insertion selects an observable subspace; the toy shows exact cancellation by Majorana closure |

The flow's Liouville measure is preserved; resonance decay describes relaxation of correlations of regular data, not loss of the L2 norm under the full transport group. Hyperbolicity is therefore not itself a literal Lindblad emission process. The cusp adds an outgoing scattering boundary and a non-self-adjoint resonance problem. Its positive boundary-energy identity is a natural passive-system/cMPS starting point, but does not make all escape widths equal.

For the normalized cusp Gram K and shifted amplitude C, the relation `C*K+KC=-11*` makes this distinction quantitative. A finite modal eigenvector has width `|1*v|^2/(2 v*K v)`: leakage positivity gives a sign, while equal width requires an independently fixed exit/storage ratio. Even if widths are equal, rank-one leakage in dimension greater than one forces nonnormality in the physical metric. It would be incorrect to require every coherent superposition to have the same exponential survival norm. This is why a physical cMPS realization can be useful without requiring the raw physical transfer to become unitary after rescaling.

The Selberg flat supertrace is a signed orbit distribution of a single-copy geometric complex. The full doubled-bond Lindbladian supertrace is a different object and, in the finite physical setting, a parity-closed ring norm. Neither the toy's physical correlation nor its full ring norm has been identified with the Riemann explicit formula.

## Mixed stationarity, critical BC state, and what they can supply

A faithful mixed finite bond is compatible with the useful decay selection: the original toy explicitly exhibits it. It is also compatible with unequal widths: b=1/100 proves that. The inverse renewal criterion in `cmps-renewal-bridge.md` makes the remaining stationarity constraint concrete: for a desired sigma and amplitude B, `-(B sigma+sigma B*)>=0` is required for a measure-and-prepare reset to realize that sigma. Changing the reset generally changes transfer and observable poles; amplitude poles do not automatically survive reinsertion.

The critical BC state is not a normal density on the standard `B(l2(N))` representation (`04c_phantasm_channels.tex:123-132`); treating it as a finite trace-one matrix would suppress a real limit problem. A proposed type-III/GNS formulation must replace the finite Schmidt-density argument with a specified state, positive covariance/GNS form, domains for its evolution and convergence of local physical correlations. The word “nonnormal” here concerns normality of a state as a functional; it is distinct from nonnormality of the finite decay matrix. Neither property by itself derives reflection symmetry, observable closure or the coercivity estimate. No assertion about an unverified type classification is needed for the finite result.

## Exact next arithmetic lemma to pursue

The concrete target is now an **arithmetic observable quadratic reduction**, rather than “find a Lindbladian with the zeros as eigenvalues.” Start with prime/modular-branch-defined finite cutoff letters and a specified output field, with no zero ordinates in their definitions. Prove the following before increasing the cutoff:

1. A finite generating family of odd observables closes under the correctly signed Heisenberg transfer. Supply the intertwiner and boundary source/sink explicitly. In the toy this family is the four Majoranas, and the intertwiner is their inclusion in the bond algebra.
2. A letter symmetry yields `J(A+kappa)J=-(A+kappa)`, with the Riemann normalization kappa=1/4. Supply J from arithmetic symmetries, not by matching already computed eigenvalues.
3. The square of the centered observable generator reduces, in a positive independently defined form, to minus an arithmetic self-adjoint operator S. State the exact analogue of `S>=0` and seek a sum-of-squares or boundary-flux identity proving it. The toy's 2x2 S is the complete model calculation for this step.
4. Prove that the selected output's meromorphic response has the desired zeta/scattering pole divisor, including nonzero residues or a jointly observable family of insertions. Distinguish genuine cancellation from an omitted mode. This identification has to include the elementary archimedean factors and correct affine normalization.
5. For an infinite/critical construction, pass these identities to regular-data correlations on fixed domains, with controlled meromorphic convergence and algebraic multiplicities. Uniform finite matrices or a fitted finite zero list are insufficient.

The smallest immediate arithmetic experiment is to derive the signed Heisenberg image of the first proposed prime/cusp output letter and its first two commutators, and calculate the component outside its proposed generating family. Nonzero uncontrolled components identify the interaction terms analogous to P/100, which spoil observable selection. If closure exists, compute the centered involution defect and the quadratic form before any large spectral numerics. This distinguishes a potential Selberg-style mechanism from a realization that merely packages already-known scattering data.

## Completion and durable recovery

Status: **COMPLETE**, 2026-09-19. All substantive results were checkpointed to this note before final reporting. The new finite theorem, perturbation counterexamples and exact verification scripts contain no RH assumption. The arithmetic reduction and infinite critical-state realization remain open.

Owned artifacts: this note; `riemann_vs_selberg_cmps_check.py`; its `.json` and `.txt` outputs; `riemann-vs-selberg-cmps-sources.sha256`. Run offline with Python 3, SymPy and NumPy:

`python3 notes/rh-strategy-2026-09-19/riemann_vs_selberg_cmps_check.py`

No new internet source was required. Primary cMPS TeX and the reviewed Selberg/scattering sources were already cached locally. The source hash manifest identifies the inputs; parent-managed repository recovery snapshots cover the note and scripts. Existing report/status files were not changed by this lane.
