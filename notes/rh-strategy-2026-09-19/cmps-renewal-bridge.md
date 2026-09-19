# A concrete cMPS target: mixed renewal with visible decay modes

Status: parent working checkpoint, 2026-09-19; new elementary finite-dimensional deductions, not a proof of RH or a registered lab-book theorem. This note responds to the user's steering that decay modes and their physically natural cMPS realization are central.

## Why cMPS fits the question

In canonical finite-dimensional cMPS, local letters satisfy `Q+Q*+sum R_a*R_a=0`, and the transfer generator is

`L(X)=Q X+X Q*+sum R_a X R_a*`.

A stationary density supplies the bond Schmidt weights. Relaxation modes of this transfer generator govern bond correlations along cMPS space (dilation time in the arithmetic proposal). Identifying an actual fermionic output correlation requires the correct parity insertion; this note does not assume that every odd bond observable is already a physical local field insertion. The repo's exact fixed-point and vacuum results are in `report/sections/04c_phantasm_channels.tex:35–111`; general overlap/parity bookkeeping is in shards 04e–04f.

The crucial distinction is between no-jump modes of `Q`, physical transfer modes of `L`, and poles visible to specified correlation insertions. A physical construction must say which of these carries the zeta divisor and prove that the modes are observable. The absorbing-vacuum construction does this for odd coherences but has trivial stationary entanglement; arbitrary mixed reinsertion need not preserve those modes.

## Finite inverse renewal criterion (proved here)

Let `B` be a finite matrix with all eigenvalues in the open left half-plane and

`E=-(B+B*) >= 0`.

For a reset density `Omega>=0`, `tr Omega=1`, define

`L_Omega(X)=B X+X B*+Omega tr(E X)`.

The reset map is completely positive (measure `E`, prepare `Omega`), and the generator is trace preserving. Explicit letters are obtained from decompositions `Omega=sum_a w_a |v_a><v_a|` and `E=sum_b e_b |u_b><u_b|`:

`R_ab=sqrt(w_a e_b)|v_a><u_b|`, `Q=B`.

These obey the canonical cMPS relation exactly. For a target density `sigma`, write `r=tr(E sigma)` and `M=-(B sigma+sigma B*)`.

**Claim.** If `r>0`, this reset construction has `L_Omega(sigma)=0` for some reset density if and only if `M>=0`; the required reset is uniquely `Omega=M/r`.

Proof: stationarity is exactly `M=r Omega`. Also `tr M=tr(E sigma)=r`, so positivity of `M` is both necessary and sufficient. For a faithful target density, nonzero `E` implies `r>0`. Stability excludes `E=0`.

Conversely, for any reset density, the renewal integral

`W=integral_0^infinity exp(tB) Omega exp(tB*) dt`

is finite and positive; `B W+W B*=-Omega`, so `tr(E W)=1`. Therefore `sigma=W/tr W` is stationary. Stability makes the Lyapunov map invertible. Any stationary operator satisfies `X=tr(E X) W`, so this normalized stationary density is unique; faithfulness requires further controllability hypotheses. This uniqueness strengthening was independently checked by the graded-channel lane.

**What this gives the RH programme.** Once an arithmetic no-jump generator and a proposed BC cutoff state are specified independently, positivity of the explicit matrix `M` is a falsifiable compatibility condition. The reset cannot be chosen freely while retaining that state. This criterion does not prove any uniform decay rate and does not identify the transfer eigenvalues with those of `B`.

## Grading obstruction to the most literal one-exit reset

Assume both parity sectors are nonzero, `B` commutes with parity `P`, and `E=-(B+B*)` has rank one. Since `E` commutes with `P`, its range lies wholly in one parity sector. On the other sector, `B+B*=0`; because `B` is block diagonal, that entire sector evolves unitarily. Thus `B` cannot be stable on the whole graded bond.

This elementary obstruction does not rule out the user's cMPS picture. It rules out simultaneously demanding a stable full no-jump bond, a nontrivial even/odd grading and a single homogeneous exit of rank one. More exits, a reference sector with different dynamics, an operator/coherence grading, or a restricted resonance realization can change the problem. Each must retain the physical transfer and arithmetic correspondence explicitly.

## Next checkpoint

Run a small finite example to verify the reset criterion and show exactly how mixed reinsertion changes the transfer modes; have the graded-channel lane check the algebra. Then use this as a construction specification, not as an assertion that a general scalar scattering realization is already an arithmetic cMPS.

## Executable check and its implication

`cmps_renewal_check.py` and its JSON output verify the canonical letters, renewal flux, target-state inverse criterion and unique faithful stationary examples for `B=-iX-diag(1,0)/2`. Its no-jump modes are `-1/4 ± i sqrt(15)/4`. Resetting to `I/2` gives physical transfer modes `{0,-1/2,-1/2±2i}`; resetting to `diag(1,0)` gives `{0,-1/2,-1/4±i sqrt(63)/4}`. The same no-jump object therefore leads to different physical decay modes after reinsertion. All residuals are below `3e-16`.

For target `sigma=diag(p,1-p)`, the required reset numerator has determinant `-(1-2p)^2`. Every biased diagonal target fails positivity; the uniform target succeeds. This is an exact algebraic example of the compatibility constraint, not a numerical conjecture.

Independent cross-review: the graded-channel lane checked both the renewal criterion and rank-one graded-exit obstruction; it supplied the uniqueness strengthening included above. None of these statements identifies a Riemann divisor.
