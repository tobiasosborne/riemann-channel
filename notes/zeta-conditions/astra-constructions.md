# Zeta conditions on concrete MPS and cMPS tensors

Constructive notebook, 14 September 2026. Conventions: `02g`, `02f`, `04f`, `03b`; arithmetic inputs are finite-field equations and character tables. The scripts never read a list of zeta zeros. Elliptic parameters are derived from a base-field point count, and extension counts check the result independently. This is a construction and correction report, not a proof of a Riemann hypothesis for an unknown object.

**The buildable answer:** four letters on a bond of dimension `1|1` realise the affine and projective elliptic examples, with an actual trace-preserving normalisation on the full bond. An amplitude-damping cMPS gives the additive functional equation, two odd modes on the central line, and one stationary state. Horner MPS of bond dimensions eight and nine compute the requested Dirichlet polynomials. Their character amplitudes are not positive ring norms. The half-entropy cMPS exists, but its regularity and Lindblad requirements need the distinction below.

All explicit matrices, count sequences through six, Möbius exponents, and check tallies are printed in the generated catalogue at the end of this report. Matrix entries there are exact numbers; `I` means the imaginary unit in expressions, decimal complex values use Python's `j`, and identity matrices are printed entry by entry. `w` is a specified root of unity, not an unknown parameter. Individual scripts print their own tallies and exit unsuccessfully on failure. Reproduce everything with:

```bash
python3 notes/zeta-conditions/finite/run_all.py
```

Only NumPy, SymPy and SciPy are needed. Everything is deterministic; there is no random sampling or seed to choose. Exact identities and finite numerical tests are distinguished below. Finite checks of prime counts do not prove positivity in every degree: the orbit arguments supply that proof for the count examples.

## 1. The condition ledger

Write `E=Σ A_s⊗conj(A_s)`, `Γ=Π⊗conj(Π)`, and `E_±=E|Γ=±1`. Each letter is homogeneous, `Π A_s Π=η_s A_s`. Write `T=Q⊗1+1⊗conj(Q)+Σ R_a⊗conj(R_a)`, with `ΠQΠ=Q`, `ΠR_aΠ=η_a R_a`. The underlying channel convention is `𝓔(X)=Σ A_s X A_s†` and the generator is `𝓣(X)=QX+XQ†+ΣR_aXR_a†`.

The three quantities to keep distinct are a physical ring **norm**, a ring **amplitude** `str F^n`, and an open-chain **sum of amplitudes**. A one-letter amplitude model with letter `F` and boundary `Π` has physical norm `|Tr(ΠF^n)|²`, not `Tr(ΠF^n)`. An arbitrary graded Frobenius matrix does not establish a Kraus realisation.

### C1. Positivity and integrality

For lattice data the exact condition is

\[
N_n=\operatorname{Tr}(\Gamma E^n)=\sum_{w\in S^n}|\operatorname{Tr}(\Pi A_w)|^2\in\mathbb Z_{\ge0},\quad n\ge1.
\]

Positivity and reality are automatic; integrality is a separate arithmetic constraint. For cMPS replace the sum by the sum over species and the integrals over ordered particle positions, including the vacuum. Thus `N(L)=Tr(Γ exp(LT))≥0` automatically for every `L>0`. Integrality at arbitrary real lengths is not a useful nonconstant requirement: continuity would make an integer-valued function constant. Positivity is not automatic for a character amplitude or an arbitrarily prescribed supermatrix.

### C2. A genuine bosonic gas

The exact lattice condition on the letters is

\[
a_d=\frac1d\sum_{e\mid d}\mu(d/e)\operatorname{Tr}(\Gamma E^e)\in\mathbb Z_{\ge0}\quad(d\ge1).
\]

These are exponents in the unweighted product `∏(1-u^d)^(-a_d)`. If only real nonnegative exponents are wanted, drop the integer requirement, but they no longer count prime species. Positivity of all ring norms does not imply C2. The single letter `diag(1,-1)` with the same parity has `N=(4,0,4,0,4,0)` and `a_2=-2`; see `e0_pair_shift.py`.

There is no intrinsic `a_d` for a continuous `L`. A precise continuous prime-gas condition would be a locally finite positive prime measure `ν=Σ_p m_p δ_{ℓ_p}`, `m_p∈Z_≥0`, with positive lengths, suitable exponential summability, and

\[
N(L)\,dL=\sum_{p,k\ge1}m_p\ell_p\,\delta_{k\ell_p}(dL),\qquad
-\partial_z\log Z(z)=\int_0^\infty e^{-zL}N(L)\,dL.
\]

A nonzero finite-dimensional, constant cMPS has analytic `N(L)` and cannot equal this atomic comb as a measure. One can instead choose a sampling interval `h` and impose the lattice condition on `Tr(Γ exp(nhT))`; this is an additional choice and generally gives nonintegral exponents. The rational cMPS ring determinant alone is not an Euler gas over discrete prime lengths.

### C3. Rationality and degree bookkeeping

Automatic for finite homogeneous data:

\[
Z(u)=\frac{\det(1-uE_-)}{\det(1-uE_+)},\qquad
\mathcal Z(z)=\frac{\det(z-T_-)}{\det(z-T_+)}.
\]

A nonzero eigenvalue `λ` with net multiplicity `m_+(λ)-m_-(λ)` contributes a pole of that order at `u=1/λ`; negative multiplicity means a zero. Lattice zero eigenvalues and nilpotent zero blocks are invisible to every positive power. Before cancellation, lattice degrees are at most `D_+²+D_-²` downstairs and `2D_+D_-` upstairs; count only nonzero eigenvalues for the actual polynomial degrees.

For cMPS, a zero eigenvalue is **not** invisible: it contributes a constant to `N(L)` and a factor `z` to the determinant. Before and after equal cancellations, denominator degree minus numerator degree is `(D_+-D_-)²`. This is also `N(0)=|Tr Π|²`. Jordan blocks do not affect either trace sequence or determinant; they can affect dynamics and metric unitarity. “Support” must never be used to discard a cMPS zero mode merely because it is zero.

### C4. Functional equation

On the reduced, nonzero lattice spectrum require parity-preserving multiplicities under `λ↦q/λ`. Equivalently, the **net** signed divisor has this invariance; a symmetry of the full unreduced spectrum is sufficient but stronger. If `χ=d_+-d_-` on that reduced spectrum, then

\[
Z(1/(qu))=(-1)^\chi\frac{q^\chi}{\operatorname{sdet}E}\,u^\chi Z(u)
=\pm q^{\chi/2}u^\chi Z(u).
\]

The last step uses `(sdet E)²=q^χ`. For the curve normal form `χ=2-2g`. A concrete sufficient operator equation is `JΓ=ΓJ`, `JEJ^{-1}=qE^{-1}` on an invariant invertible support. Spectral invariance alone need not provide such a `J` unless the Jordan structures also match. The Hodge matrix `J` for the product elliptic tensor is printed and verified in `curve_projective.py`.

For cMPS the corresponding symmetry is **additive**: `λ↦κ-λ` with parity and multiplicities preserved, or `JTJ^{-1}=κ1-T`. It gives `𝒵(κ-z)=(-1)^χ𝒵(z)`. The FE example has `κ=2`; in Lindblad normalisation its centre shifts and the reflection is `λ↦-2-λ`. Multiplicative `λ↦q/λ` is not the natural symmetry of a generator.

**Correction to the reading of `08b`:** inverse-paired letters give reciprocal quadratic roots for its non-backtracking/Hashimoto construction, after the specified trivial factors are removed. They do not do so for a general raw doubled sum. `B=diag(1,2)` and `B^{-1}=diag(1,1/2)` have even spectrum `{2,17/4}` and odd spectrum `{5/2,5/2}`. The even pair fixes `q=17/2`; the odd pair fails it. This is tested in `e0_pair_shift.py`. The graph construction below exhibits the actual inverse-pairing mechanism.

Conjugation closure is automatic for a physical transfer: adjoint of a bond operator is an antilinear symmetry, separately in each doubled parity. An adjoint-closed Kraus family makes the **raw** channel Hilbert–Schmidt self-adjoint, hence its eigenvalues real. In the non-backtracking construction it is the sum `Σ Ad(B_i)` that becomes self-adjoint, not necessarily the Hashimoto matrix. Reality of coefficients, reality of eigenvalues, and a reciprocal FE are different assertions.

### C5. RH / Ramanujan

Fix which modes are trivial **before** testing. For curves, the exact condition is `|λ|²=q` for every retained odd eigenvalue. A sufficient, visible mechanism is a positive metric `M` with `E_-† M E_-=qM`. It is also necessary if the retained odd matrix is semisimple. For graph non-backtracking transfers the analogous condition concerns the retained nontrivial **even** modes, with the Bass factors and Perron partners specified. A generic stochastic adjacency matrix obeys a different Ramanujan inequality; it should not be silently substituted for this circle condition.

For cMPS, replace the circle by `Re λ=κ/2`. A metric sufficient condition is `T_-†M+MT_-=κM`. In the normalised FE example `κ=-2`, so all odd modes decay at rate one. Existence of that metric includes semisimplicity and is stronger than a bare statement about the eigenvalues.

The finite Weil criterion of `08b` supplies another exact condition: for the retained spectrum set `ν_n=Σ(λ/√q)^n`, `ν_{-n}=conj(ν_n)`, and require every finite Toeplitz matrix `(ν_{j-k})` to be positive semidefinite. This gives `|λ|≤√q`. Reciprocal closure then gives equality. In continuous time use `ν(t)=Σ exp((λ-κ/2)t)` for `t≥0`, extend by conjugate reflection, and impose positive definiteness of every kernel matrix `(ν(t_j-t_k))`. The generator bound is `Re λ≤κ/2`; additive reflection makes it equality. This is a condition on the retained sector, not positivity of the whole Ramond norm.

`independence.py` has an explicit CPTP family with poles `{1,1/16}` and odd eigenvalues `{8,2}`: FE and a unique stationary state hold, while RH fails. Its printed two-by-two Weil minor has a printed vector with quadratic value minus one. The unequal moduli give unequal transfer decay lengths. Replacing them by `{4,4}` gives RH by an odd block equal to four times the identity. This is an actual Kraus variation, not a list of independently assigned roots.

### C6. A unique fixed point, mixing, and the pole

Three requirements were conflated in the draft:

1. **Spectral pole:** the Perron eigenvalue `q>0` of the even transfer is algebraically simple and uncancelled.
2. **A channel on the specified bond:** there is a strictly positive even matrix `h` with `𝓔†(h)=qh`. Then `B_s=q^{-1/2}h^{1/2}A_sh^{-1/2}` satisfies `ΣB_s†B_s=1`. A singular `h` permits a restriction, not a gauge on the entire original bond.
3. **Stationarity / mixing:** the normalised channel has a one-dimensional fixed space generated by a density matrix. Convergence to it further requires every other eigenvalue to have modulus less than one. Uniqueness alone permits periodicity. `independence.py` prints a bit-flip channel with one stationary state and a second peripheral eigenvalue.

On the even algebra these are literal finite-dimensional spectral and linear equations; if the user wants uniqueness on the entire matrix algebra, also exclude fixed odd coherences. The main channel examples do. The brief additionally permits only the other nonzero even eigenvalue `1`, or its absence. The four basic independence examples obey that restriction. Requiring the full projective even pair `{1,q}` is a stronger divisor constraint, denoted C6projective here. More general ergodic channels can have additional subleading even modes.

For cMPS impose `Q=-iH-½ΣR_a†R_a`, `H=H†`, and `ker 𝓣=Cρ_*` with `ρ_*≥0`, `Trρ_*=1`, and exclude other imaginary-axis eigenvalues if convergence is intended. After a growth shift `T=𝓛+κ1`, the stationary mode is the simple pole at `z=κ`. A pure stationary state is allowed; it does not give a prescribed mixed entanglement spectrum.

The product elliptic tensor `diag(1,π)` has a simple Perron root, but its left Perron eigenmatrix is rank one. Dividing its letters by `√q` is not a TP normalisation on both bond lines. The four-letter construction below fixes this without changing the ring zeta. Its `H^0` eigenvalue `1` is a decaying eigenoperator of the channel after division by `q`, not a second decoupled stationary block.

### C7. Galois grading and character factors

An exact lattice covariance is `U_gΠ=ΠU_g` and `U_g A_s U_g^{-1}=Σ_t v_g(t,s)A_t` for unitary physical representations `v_g`. Then `D_g=U_g⊗conj(U_g)` commutes with `E,Γ`. Decompose the doubled space as `⊕_χ V_χ⊗M_χ`, with `E=⊕1⊗E_χ`, `Γ=⊕1⊗Γ_χ`. Define

\[
N_n^\chi=\operatorname{str}_{M_\chi}E_\chi^n
=\frac1{\dim\chi}\operatorname{Tr}(P_\chi\Gamma E^n),\quad
P_\chi=\frac{\dim\chi}{|G|}\sum_g\overline{\chi(g)}D_g.
\]

Then `N_n=Σ dimχ N_n^χ`, `L(u,χ)=1/sdet(1-uE_χ)`, and `Z=∏ L(u,χ)^{dimχ}`. For cMPS impose in addition `U_gQU_g^{-1}=Q` and the analogous unitary species covariance for `R`; replace powers by exponentials and determinants by `sdet(z-T_χ)`.

This is representation-theoretic factorisation. To call it an **Artin** L-function also identify an actual cover and its monodromy/Frobenius weights on primitive orbits. A symmetry with fixed letters does not alone do this. Nor must a character factor be real or positive. FE normally pairs `χ` with its contragredient; an individual complex character need not have a self-reciprocal divisor.

“Even = trivial, odd = nontrivial” is additional geometric information, realised on the elliptic hyperelliptic/Artin–Schreier cohomology and its doubled tensor. It is not a theorem about all group actions: in the Ihara cover every physical norm mode is even, including the sign-character modes. The bond multiplication action on the Horner automaton does not commute with its summed transfer; the script explicitly checks this. Its character boundary must not be called an equivariant Frobenius eigenspace.

### C8. Sign structure

Automatic once the homogeneous physical data and parity closure have been fixed: zeros have negative **net doubled** multiplicity and poles positive multiplicity. The mixed `(+,-)` and `(-,+)` coherences supply the minus sign, not the odd ket population. In cMPS use exactly the same doubled grading. An untwisted closure uses the ordinary trace and has no finite determinant zeros. Separating letters by ket parity kills their lattice cross transfer and removes the zeros, as in `03b`. In amplitude-only character examples the odd grading is a trace convention, not an established norm factorisation.

### C9. Physical realisability and regularity

For a proposed lattice transfer the exact finite test is a positive semidefinite Choi matrix for `𝓔`, together with parity covariance; factoring each parity block of that Choi matrix gives homogeneous Kraus letters. The displayed tensors already supply such a factorisation. Orthonormal physical words always define the Hilbert norm, but a literal **count state** additionally needs `Tr(Π A_w)∈{0,1}` (or unit-modulus phases on selected words). The curve tensors are weighted norm realisations; their words do not label curve points one for one. The product tensor is especially transparent: `(1-π^n)φ^{⊗n}`. This limitation is already explicit in `06d`.

For finite cMPS, bounded matrices and the stated parity relations suffice for a finite Fock norm on a finite ring. If “regular” also means the usual finite-kinetic-energy condition, require `R_aR_b=(-1)^{p_ap_b}R_bR_a`; in particular a fermionic species has `R_a²=0`. Lindblad normalisation is the C6 equation, independent of finite-norm existence. The half-entropy alternatives below explicitly label which meaning holds. A cMPS can be finite-norm and CPTP while failing kinetic regularity.

### C10. Continuum and quantised length

An exact cMPS embedding of a particular lattice channel asks for a generator of the above Kraus/Lindblad form with `E=exp(hT)` (up to the declared growth factor). Taking a matrix logarithm is insufficient: its Choi conditional positivity and the jump parity/regularity constraints must hold. Singular `E` cannot be such an exponential at positive time. The affine four-letter tensor has a zero eigenvalue and hence has no exact full-transfer embedding.

All three projective elliptic **zeta data** have a cMPS counterpart with `γ=log q`, `ω=arg π`, one decay jump `√γ |0><1|`, and normalised Hamiltonian with energy difference `ω`; shift `Q` by `γ/2` to restore growth. Its spectrum is `{γ,0}` even and `{γ/2±iω}` odd; sampling at `L=n` gives the same counts. This realises the data, not necessarily the particular four-letter channel. `cmps_fe.py` is the concrete numerical choice `γ=2,ω=1`. The two-letter damping variant in `curve_projective.py` is a discrete representative of this semigroup type.

A universal weaker construction is Poissonisation: take `Q=-c1/2`, `R_s=A_s`, giving `T=E-c1` and `N(L)=e^{-cL}Σ_{n≥0}N_n L^n/n!`, with `N_0=(TrΠ)²`. It is TP if `ΣA_s†A_s=c1`. The `n=0` term and all zero modes matter. It normally changes the FE/RH and may fail kinetic regularity. No claim is made that the Horner characters or graph cover acquire an arithmetic continuum interpretation under this operation.

Incommensurable prime lengths mean that no common `h>0` makes every `ℓ_p/h` an integer. Constant finite-bond cMPS has continuously variable `L` but an analytic exponential-polynomial norm; that fact does not create an atomic collection of incommensurable prime lengths. Incommensurable Hamiltonian frequencies concern oscillations, not a proven Euler-prime length spectrum.

## 2. The concrete catalogue and its mechanisms

The full matrices and numerical tables are at the end, organised by the script names in this section. The following table records all ten conditions for the primary object in each row. `Y` is an exact property, `N` is a failure, `—` means the condition has no intrinsic meaning for that object, `A` means amplitude/character data only, and `R` means after the specifically stated reduction. C1 for lattice rows includes integrality. C6 means a mixing TP channel on the specified bond; the stronger projective pole condition is discussed separately. C9 `W` is a weighted physical norm, `P` is a literal count state, and `K` flags the kinetic-regularity distinction.

| Object / script | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 |
|---|---|---|---|---|---|---|---|---|---|---|
| E0 / `e0_pair_shift` | Y | Y | Y | N | Y | N | symmetry, not Artin | Y | P | half-entropy analogue, different parameters |
| affine elliptic / `curve_affine` | Y | Y | Y | N | Y | Y | hyperelliptic character | Y | W | no exact exponential of displayed E |
| projective elliptic / `curve_projective` four letters | Y | Y | Y | Y | Y | Y | hyperelliptic character | Y | W | same-data damping cMPS |
| supersingular / `curve_supersingular` four letters | Y | Y | Y | Y | Y | Y | Artin–Schreier character | Y | W | same-data damping cMPS |
| directed double cover / `z2_shift_cover` total | Y | Y | Y | N | — | Y | Artin Y | Y | P | Poissonisation only asserted |
| Dirichlet F2 / `dirichlet_f2`, individual L | N | N | Y | N, dual-character FE | Y after trivial root | — | Dirichlet Y | A | open MPS; ring A | no arithmetic continuum claimed |
| Dirichlet F3 / `dirichlet_f3`, individual L | N | N | Y | N, dual-character FE | Y | — | Dirichlet Y | A | open MPS; ring A | no arithmetic continuum claimed |
| Gauss / `gauss`, individual L | N | N | Y | N, dual factor | Y | — | additive/multiplicative character | A | open MPS; ring A | — |
| Kloosterman affine norm / `kloosterman` | Y | Y | Y | N | Y | Y | Artin–Schreier character | Y | W | singular E; projective completion has analogue |
| Ihara cover total / `graph_artin` | Y | Y | Y | R | R | Y | Artin Y | all even | P | Poissonisation only asserted |
| half entropy regular / `cmps_half` | Y | — | Y | N | Y at prescribed κ=2 | N | parity only | Y | W, kinetic regular | continuous L |
| half entropy TP alternative / `cmps_half` | Y | — | Y | N | Y at transported κ=-2 | Y | parity only | Y | W, K fails | continuous L |
| FE cMPS / `cmps_fe` | Y | — | Y | Y | Y | Y | parity only | Y | W, kinetic regular | continuous L |

For the half-entropy row, `λ_-=λ_+/2` passes the central-line test with the explicitly prescribed target reflection `λ↦2-λ`. The divisor does not obey that reflection. Thus this is C5 without C4, and there is no FE selecting that centre. Translating its spectrum by minus two transports this target to `λ↦-2-λ`; half of a growth exponent is not invariant under arbitrary growth shifts.

### E0: remove a full subshift

Take the four pair letters `(0,0),(0,1),(1,0),(1,1)` and `A_(a,b)=diag(1,[a=b])`. The parity boundary cancels exactly the words all of whose pairs are diagonal. Thus

\[
N_n=4^n-2^n,\qquad Z(u)=\frac{1-2u}{1-4u}.
\]

The full even spectrum is `{4,2}`, the full odd spectrum is `{2,2}`. One even/odd pair cancels, leaving one pole at `1/4` and one zero at `1/2`. The odd coherence has half the exponential growth of the dominant even mode. Its transfer length is `1/log 2`; the interpretation as a state correlation length requires a nonzero observable overlap.

Primitive binary necklaces form a subset of primitive four-letter necklaces, so every `a_d` is a nonnegative integer. There are infinitely many surviving primes; rationality does not rule that out. At `m=2` the displayed rational function is indeed the ratio of the two affine-line zetas over F4 and F2, with their degree variables identified. That equality is not an Artin factorisation of a degree-two cover. The swap has fixed letters; its representation on a word Hilbert space is not the Frobenius action on all extension fields.

The MPS itself is swap invariant. Its overlap with the swapped state equals its norm, not the trace of swap on the entire word space. The latter trace is `2^n`. These two meanings of a twisted count were mixed in D5.

### Three curve rungs on a `1|1` bond

For `y²=x³+x+1` over F5, direct enumeration gives `a=5+1-N_1=-3`; define `π=(-3+i√11)/2`. Both the affine and projective four-letter tensors are printed in full. Their construction uses `t=(q+r)/2`, `h=(q-r)/2`, with `r=0` for the affine curve and `r=1` for the projective curve: the two diagonal letters have Gram overlap `π`, and two separate parity-changing letters create the symmetric population transfer with eigenvalues `q,r`. The residual diagonal-letter square is `t-q/t≥0`. In each case `ΣA_s†A_s=q1`, so dividing letters by `√q` gives an honest TP channel.

The even spectra are `{5,0}` and `{5,1}`; the odd spectrum is `{π,conjπ}` in both. Hence

\[
Z_{\rm aff}(u)=\frac{(1-\pi u)(1-\bar\pi u)}{1-5u},\qquad
Z_{\rm proj}(u)=\frac{(1-\pi u)(1-\bar\pi u)}{(1-u)(1-5u)}.
\]

The affine tensor is an actual physical norm realisation, not subtraction of an unphysical boundary amplitude. Its zero even eigenvalue disappears from the lattice determinant. Adding the projective `H^0` restores the reciprocal pole pair and FE. The two odd eigenvalues have modulus `√5` by the exact identity `πconjπ=5`; their block divided by `√5` is unitary. The even stationary state of the four-letter channel is maximally mixed and unique. Its nonstationary even length is `1/log 5` in the projective case; the odd transfer length is `2/log 5`. The affine even subleading mode vanishes after one step. These are transfer-mode lengths, not a guarantee about every physical correlator.

The report also prints the `06g` product letters `diag(1,π)/√2`, twice. They have exactly the same ring norms and FE, but zero entanglement and no full-bond TP gauge. The four-letter tensors have a different transfer eigenbasis and a different physical state. Ring norm data do not determine these features. The two-letter damping representative has a pure stationary vacuum and again the same norm data, showing that even the stationary density matrix is not selected by the zeta.

For `y²+y=x³` over F4, the base-field enumeration gives `a=-4`, so `π=-2` and

\[
Z(u)=\frac{(1+2u)^2}{(1-u)(1-4u)}.
\]

There is a double zero at `u=-1/2`, fixed by the reciprocal involution. The product letter is `diag(1,-2)`; the TP four-letter version is printed beside it. The exact extension-field enumeration through degree six checks the double-root sign. The Artin–Schreier involution acts trivially on `H^0,H^2` and by its sign character on `H^1`. In the tensor this is `U=Π`, with odd physical letters changing sign. For all three curve rungs the gas consists of closed points, so the all-degree positivity of `a_d` comes from geometry. The words of these weighted MPS are not those closed points.

### Correct tiny Z/2 Artin example

Use a directed base vertex with three distinguishable loops of voltages `0,1,1` in Z/2. The cover has two vertices, with path matrix `C=1+2X`, `X` the sheet swap. Six matrix-unit letters record the directed lifted edges, making each closed word have amplitude one. The channel normalises by division of letters by `√3` and is mixing.

The character restrictions are the scalar amplitude letters `[3]` and `[-1]`. Thus

\[
L(u,1)=\frac1{1-3u},\quad L(u,\mathrm{sgn})=\frac1{1+u},\quad
Z_{\rm cover}=\frac1{(1-3u)(1+u)}.
\]

The sign logarithmic trace is `(-1)^n`, so this individual Artin factor is not a norm. A primitive base orbit with voltage `v` carries local factor `(1-χ(v)u^d)^(-1)`. This is the actual monodromy Euler product. Contrast the draft square root for the pair shift: its proposed `a_2=5/2` and half net multiplicities already prevent a finite-dimensional trace interpretation of that particular factor. A group projector on each word space need not be compatible with repetition of prime orbits.

### Horner Dirichlet MPS over F2 and F3

The bond is the residue field, including zero. Its ordered basis has index `j=Σ a_i q^i`, representing `Σa_i x^i`. The letter `H_c` has entry one in row `xf+c mod M`, column `f`, and zero elsewhere. Start at the basis vector for the constant residue one, read the `n` lower coefficients of a monic polynomial in descending order, and close with the linear row `(χ(f))_f`, extended by `χ(0)=0`. Every letter, the initial vector and the character row are printed in full in the generated catalogue.

Then

\[
\Psi_n=\sum_{c_1\ldots c_n}\chi(x^n+c_1x^{n-1}+\cdots+c_n)|c_1\ldots c_n\rangle,
\quad b_n=\langle\mathbf1|\Psi_n\rangle=\chi^{\mathsf T}(\sum_cH_c)^n|1\rangle,
\quad L(u,\chi)=\sum_{n\ge0}b_nu^n.
\]

The notation `χ^T` means the displayed linear row; its ket dual would be conjugated. The physical open norm is the number of monics coprime to `M`, equal to `q^n` below `deg M` and `q^n-q^{n-deg M}` thereafter. It is not `b_n` or the logarithmic sequence `N_n^χ`.

For F2, `M=x³+x+1`, take generator `x` of F8× and `χ(x)=w=exp(2πi/7)`. The result derived from the Horner coefficients is

\[
\alpha=-(1+w+w^3),\qquad
L(u,\chi)=1+(w+w^3)u-(1+w+w^3)u^2=(1-u)(1-\alpha u),\quad |\alpha|^2=2.
\]

All six nontrivial characters are even because F2× is trivial. The script checks the modulus identity for every conjugate character by exact reduction modulo the cyclotomic polynomial. The root at `u=1` is a trivial factor; the nontrivial zero is `1/α`.

For F3, `M=x²+1`, take generator `1+x` of F9× and `χ(1+x)=w=exp(2πi/8)`. Here

\[
\alpha=w^3+w^2-w=-\sqrt2+i,\qquad L(u,\chi)=1-\alpha u,\quad |\alpha|^2=3.
\]

Characters with exponents `1,3,5,7` are odd and have degree-one nontrivial L-functions; the nontrivial even characters instead have only the factor `1-u`. This is the parity of a Dirichlet character on constants, distinct from a physical fermion parity. The standard polynomial degree and unitary-normalisation conventions are reviewed in [Roditty-Gershon, §3](https://link.springer.com/article/10.1007/s40993-016-0066-2). The particular coefficients and root-size identities here are computed directly, without using Weil's theorem as a numerical input.

For either example, the completed degree-one factor `L*(u,χ)=1-αu` satisfies

\[
L^*(1/(qu),\chi)=-\frac{\alpha}{qu}L^*(u,\bar\chi),
\]

since `αconjα=q`. This is a dual-character FE, not C4 for the individual complex factor. Pairing `χ` with `barχ` restores reciprocal and conjugation symmetry. The original F2 factor also has its specified trivial root.

**Side A to side B.** Unique factorisation of monic polynomials gives

\[
L(u,\chi)=\prod_{P\nmid M}(1-\chi(P)u^{\deg P})^{-1},\qquad
N_n^\chi=\sum_{d\mid n}d\sum_{\deg P=d}\chi(P)^{n/d}.
\]

The prime polynomials are Frobenius orbits on the affine line away from the ramified modulus. Their multiplicative weight is repeated as `χ(P)^k`. These are weighted orbit rings, not cyclic paths of the Horner residue automaton. The scripts enumerate irreducible monic polynomials independently through degree six and compare this formula with `N_n^χ=-1-α^n` (F2) or `-α^n` (F3). Simply closing `H_c` into a trace is wrong: it imposes `f=x^n f+b`, a residue-automaton return condition.

For a compressed **amplitude** presentation take the printed all-odd letter `diag(1,α)` over F2 and `[α]` over F3. Their supertraces produce those logarithmic sequences, and their superdeterminants give the L-functions. They are not physical Ramond norm realisations: the displayed sequences are already complex at degree one. The Möbius exponents printed for these factors are the formal exponents in `∏(1-u^d)^(-a_d)`; they are not the weighted degree-d prime sums because repetitions raise the character value to a power.

### Gauss and Kloosterman factors, with signs fixed

For the quadratic character over F3 and `ψ(x)=exp(2πix/3)`, the standard Gauss sum is `G=i√3`. It also equals the affine-line sum `Σ_x ψ(x²)`. Its extensions using norm and trace have `G_n=(-1)^{n-1}G^n`. Consequently the standard convention `exp(Σ G_nu^n/n)` gives **`1+Gu`**, not `1-Gu`. The latter notation is correct if the letter `G` has been redefined as the Frobenius eigenvalue `-i√3`. This polynomial has no poles and its zero is `u=i/√3`. `gauss.py` prints the three scalar affine-line letters, indexed by `x=0,1,2`, and the one-dimensional all-odd amplitude matrix. It checks both forms of the Gauss sum directly in the extension fields. The lifting convention is the classical Hasse–Davenport relation; see the finite-field discussion in [Iwaniec–Kowalski, exponential sums](https://people.math.ethz.ch/~kowalske/ik-ant-exp-sums.pdf). A single complex Gauss factor is not a positive norm or a bosonic prime gas.

For Kloosterman use F4 and the **raw** sum

\[
S_n=\sum_{x\in\mathbb F_{4^n}^{\times}}(-1)^{\operatorname{Tr}_{\mathbb F_{4^n}/\mathbb F_2}(x+x^{-1})}.
\]

`kloosterman.py` obtains `S_1=3` and derives

\[
L_{\rm Kl}(u)=1+3u+4u^2=(1-\pi u)(1-\bar\pi u),\quad
\pi=(-3+i\sqrt7)/2,\quad S_n=-(\pi^n+\bar\pi^n).
\]

This exponential-sum L-function is on the punctured affine line `G_m`; `x^{-1}` is not defined at zero. The elliptic curve `y²+xy=x³+1` has affine count `4^n+S_n`: at `x=0` it has one point, and for `x≠0`, division by `x²` gives a trace condition with `Tr(x+x^{-2})=Tr(x+x^{-1})`. Its smooth completion adds one point. Thus the requested **norm of type `q^n-Kl_n` exists on bond `1|1`**, with the four explicitly printed affine letters, if `Kl_n` denotes the Frobenius power sum `-S_n`. With the raw exponential-sum convention the correct sign is plus. Replacing `+S_n` by `-S_n` would give a different sequence and a different zeta.

The affine norm zeta has one pole at `1/4` and two zeros `1/π,1/conjπ`; the L-factor itself has these zeros and no poles. The bound `|a|≤2√q` follows here from the explicitly computed conjugate pair with product `q`. The raw sums are also the logarithmic coefficients of `L_Kl`, so C1/C2 for that individual L-factor fail (its extension sums change sign). The curve completion restores a positive count and a genuine gas. This distinction is checked, not inferred from an assumed physical interpretation of an exponential sum.

### A graph-cover Ihara factor and the correct inverse-pairing mechanism

Take a rose with two undirected loops `a,b`, oriented as `a,a^{-1},b,b^{-1}`. The Z/2 voltages are `0,0,1,1`. The cover has two vertices, a loop at each and two edges between the vertices. `graph_artin.py` prints the base and sign Hashimoto matrices, the eight-dimensional cover matrix, the deck permutation, and eight full row-letter matrices on bond dimension eight. They are a count MPS: a physical word is a closed non-backtracking directed-edge sequence, and its amplitude is one. The natural grading is entirely even.

Fourier decomposition on the two sheets gives

\[
L_1=\frac1{(1-u^2)(1-u)(1-3u)},\quad
L_{\rm sgn}=\frac1{(1-u^2)(1+3u^2)},\quad Z_{\rm cover}=L_1L_{\rm sgn}.
\]

These are the usual graph Artin determinants; the cover factorisation and the Bass correction are described in [Terras, Artin L-functions of graphs](https://mathweb.ucsd.edu/~aterras/zeta%20stroll.pdf). Here they are verified directly from the printed matrices. Every root is a **pole**: in particular the sign factor's interesting poles are at `u=±i/√3`. The full cover has poles `1/3`, `1` with multiplicity three, `-1` with multiplicity two, and `±i/√3`.

After removing one `(1-u²)` factor per character, the two Bass quadratics are `1-4u+3u²` and `1+3u²`. Their reciprocal roots are `{1,3}` and `{i√3,-i√3}`. The reversal/no-backtracking identity forces the common product `q=3` in these quadratics: this is where inverse pairing produces FE. The two-letter orientation inverses are combinatorial inverses, not a false statement about the inverse of a raw Kraus sum. The retained nontrivial even modes satisfy the graph RH; the discarded Bass modes must be named, since the unmodified full divisor is not reciprocal at `q=3`.

The script also converts these **reduced** even/odd quadratics into a physical `1|1` elliptic norm tensor with `Z=(1+3u²)/((1-u)(1-3u))`. It prints all four letters. This is a new graded norm realisation of a **ratio** of reduced graph determinants, not the graph cover norm. It exhibits the requested even pair and odd reciprocal pair by a valid visible mechanism. Bond dimension two is the minimum possible for any nonzero doubled odd sector. A raw inverse-closed Kraus family by itself is insufficient, as the earlier counterexample proves.

The cover count channel has one stationary state and all other eigenvalues below the Perron modulus. To see a TP Kraus family directly, transpose every displayed row-letter and divide by `√3`; their completeness follows from every row having three entries. Transposition preserves the untwisted closed-word norm by reversing word order. The nontrivial transfer lengths are `2/log 3` for the retained complex modes and `1/log 3` for the subleading unit modes. Character projection of the graph trace is a linear amplitude operation; its sign trace takes negative values and is not itself the norm of the projected physical state.

### Independence, using actual channels

`independence.py` prints eight homogeneous Kraus families, all TP after division by four. The basic bond is `1|1`; their even spectra are `{16,r}` and odd spectra `{x,y}`. The four entries are:

| Base tag | r | x,y | FE C4 | RH C5 | mixing C6 |
|---|---:|---|---|---|---|
| TTT | 1 | 4,4 | Y | Y | Y |
| TFT | 1 | 8,2 | Y | N | Y |
| FTT | 0 | 4,4 | N | Y | Y |
| FFT | 1 | 3,3 | N | N | Y |

The displayed matrices are scaled identity and Pauli matrices with positive coefficients. Their squared coefficients are `(16+r+x+y)/4`, `(16+r-x-y)/4`, `(16-r+x-y)/4`, `(16-r-x+y)/4`. They are physical letters, not a spectral ansatz whose positivity is unchecked. The eigenvalues are then derived from their channel action.

Tensor every letter with an idle, all-even qubit to obtain tags TTF, TFF, FTF, FFF. This multiplies every doubled multiplicity by four and gives a stationary matrix algebra. FE and RH are preserved, while the fixed point ceases to be unique. All enlarged matrices are also printed in full. Each example has `N_n=k(16^n+r^n-x^n-y^n)`, with `k=1` or four; its exact `Z`, `N_1..6`, and `a_1..6` are in the appendix. All their Möbius exponents are nonnegative integers in every degree: embed the disjoint x- and y-letter full shifts in the 16-letter shift, and add an independent r-letter shift; multiply orbit multiplicities by k.

This proves mutual independence of C4, C5 and **mixing-channel C6** while retaining the brief's permitted even spectrum `{q,1}` or `{q}` on support in the unique-state rows. FTT removes the H0 pole, using an even zero eigenvalue. There is a deliberate limit if one instead insists on the exact **projective** curve normal form with real coefficients: RH already makes the odd multiset reciprocal, and `{1,q}` supplies the even reciprocal pair. Thus `(C4=N,C5=Y,C6projective=Y)` is impossible. FTT/FTF avoid precisely that stronger hypothesis. Moreover, simple stationarity without mixing is strictly weaker: the printed periodic channel has a unique stationary state and a nontrivial peripheral mode.

### Two cMPS constructions and a regularity correction

**Half entropy.** `cmps_half.py` first uses the regular bosonic data `Q=1/2` times the two-dimensional identity, `R=diag(1,0)`, `Π=diag(1,-1)`. It prints the matrices and `T=diag(2,1,1,1)`. Consequently

\[
N(L)=e^{2L}-e^L,\qquad \mathcal Z(z)=\frac{z-1}{z-2}.
\]

There is one net even pole at two and one net odd zero at one after a cancellation. This has precisely the requested exponent ratio. The two bond branches differ by whether they emit the common physical species; their vacuum amplitudes cancel. The original tensor is not a Lindblad gauge on the full bond, and a scalar growth shift cannot fix its unequal diagonal completeness defects.

The same script supplies a finite-norm **normalised Lindblad** alternative with a lowering fermion and a diagonal bosonic dephaser. Its exact matrices are printed: `R_f=[[0,1],[0,0]]`, `R_b=diag(1/2,-1/2)`, `Q=diag(-1/8,-5/8)`. Its even eigenvalues are `0,-1`, odd eigenvalues `-1,-1`, stationary state the pure vacuum, and

\[
N(L)=1-e^{-L},\qquad\mathcal Z(z)=\frac{z+1}{z}.
\]

Adding the identity to this Q restores the previous growth exponents. However, the bosonic and fermionic R matrices do not commute, so these data fail the standard algebraic kinetic-regularity relation. This failure is not a claim that this particular nonminimal ring state has infinite kinetic energy; it is a failure of the regular-matrix ansatz. It is still a well-defined finite Fock-norm cMPS in the conventions of `02f`, which explicitly did not impose that extra relation.

There is a small exact obstruction if **all** the demands are imposed on `1|1`. For homogeneous regular data, each fermionic off-diagonal R is nilpotent. Anticommutation of two such jumps forces all nonzero ones to have the same lowering or raising orientation. Every diagonal bosonic jump commuting with one of them is scalar and supplies no dephasing. A normalised generator with a unique fixed point therefore has even eigenvalues `{0,-γ}` and odd eigenvalues `{-γ/2±iω}`. It cannot produce the half-difference `{0,-γ}` even minus `{-γ,-γ}` odd for `γ>0`. If there is no fermionic jump, the two parity populations are separately stationary. Thus on this bond regularity, full Lindblad normalisation, uniqueness and the exact half-difference cannot all hold. No unsupported higher-bond no-go is claimed.

**Functional equation.** `cmps_fe.py` takes one regular lowering fermion with rate two and Hamiltonian energy difference one. Its normalised data and the growth-shifted Q are printed in full. In the growth convention the even eigenvalues are `{2,0}` and odd eigenvalues `{1+i,1-i}`, so

\[
N(L)=1+e^{2L}-2e^L\cos L=|1-e^{(1+i)L}|^2\ge0,\qquad
\mathcal Z(z)=\frac{(z-1)^2+1}{z(z-2)},\qquad\mathcal Z(2-z)=\mathcal Z(z).
\]

In the normalised convention the poles are `0,-2`, zeros `-1±i`, and the unique stationary state is the vacuum. The jump is nilpotent, so kinetic regularity holds. The odd damping is half the population decay and its frequency comes from the Hamiltonian. The generator shifted by half the reflection constant is skew-adjoint on the odd two-dimensional sector. This is a concrete FE/RH/fixed-point mechanism. It does not assign a precomputed zeta-zero list to a Hamiltonian.

This ring vector has only its vacuum amplitude: a product containing a lowering jump is off-diagonal and has zero parity trace. Thus it is a perfectly honest but physically simple cMPS; the nontrivial zeta data sit in its length-dependent vacuum normalisation. It does not establish the proposed nontrivial Gibbs entanglement spectrum of the infinite Riemann programme. Both cMPS scripts print `N(L)` at integer lengths through six. Prime counts are marked undefined rather than invented for a continuous length variable.

## 3. Correction ledger for D1–D8

| Draft | Verdict | Exact correction / scope |
|---|---|---|
| D1: sub-system rule | **PROVED-CONDITIONAL** | For unit-coefficient word states with a repetition- and rotation-compatible subsystem, the difference is the indicator of the complement, its norm is the difference of counts, and its primitive orbits form a set difference. Equal amplitudes alone do not say the coefficients have unit magnitude, or identify compatible primitive orbits. Weighted sub-sums generally give weighted norms. The zeros of the ratio may cancel against poles; “zeros = subsystem poles” is only before net cancellation. |
| D2: E0 | **PROVED, interpretation corrected** | The four diagonal letters give exactly the stated formula, genuine gas and circle radius. There is no FE. The F4/F2 zeta ratio is an equality of rational functions in an identified degree variable, not an Artin quotient from the swap. A simple Perron eigenvalue here does not make the displayed tensor a channel on the whole bond. |
| D3: ladder | **PROVED-CONDITIONAL for arithmetic identification; explicit tensors constructed** | The affine rung needs a different tensor, not just deletion of the product tensor's H0 block. The four-letter construction does it. All stated curve sequences follow from the elliptic Frobenius recurrence; the independent point enumerations are finite checks. The standard all-degree point-count recurrence and closed-point interpretation give all-degree C1/C2. The product letters match norms but do not enumerate points as words. |
| D4: inverse pairing | **CORRECTED with counterexample** | Inverse closure does not imply FE for the raw doubled transfer. The `diag(1,2)` counterexample is exact. The non-backtracking construction with its Bass factors gives the reciprocal quadratics; the graph example and its separate `1|1` graded norm realisation exhibit the corrected mechanism. No nonexistent general raw-letter theorem is used. |
| D5: swap L-function | **CORRECTED with counterexample and replacement** | The proposed square root is not an Artin factor of that pair shift, and has half multiplicities. A free voltage cover gives the explicit factors `1/(1-3u)` and `1/(1+u)`. Deck-twisted path traces, traces on the whole word representation, and overlaps of a single MPS state are different objects. |
| D6: fixed point selects poles | **CORRECTED** | Simple Perron root, faithful TP gauge, unique stationary state, and mixing are separate conditions. Unique stationarity does not exclude peripheral periodic modes. H0 need not be a second decoupled block; it is a decaying population-difference mode in the TP curve tensors. All eight FE/RH/mixing combinations exist with the permitted presence/absence of H0; one combination is impossible under the extra exact-projective pole condition. |
| D7: cMPS E0 and FE | **PROVED with a regularity qualification** | The half-difference has a regular bosonic unnormalised construction and a finite-norm TP construction that fails kinetic regularity. On homogeneous `1|1` data, regularity plus TP plus uniqueness rules out that exact difference. The separate FE example satisfies all three and has two poles/two zeros. |
| D8: tiny Riemann | **CORRECTED; infinite arithmetic construction remains OPEN** | Finite bond can have infinitely many Euler primes, as E0 does. It cannot give infinitely many distinct divisor points in the u-plane, or an analytic finite-cMPS norm equal to the prime comb. The trace-class plain-trace no-go applies to uncancelled negative spectral multiplicities, not to graded physical norms. A full infinite-bond Riemann cMPS is not constructed here. |

The inherited all-degree elliptic recurrence is the standard `N_n=1+q^n-s_n`, `s_n=a s_{n-1}-q s_{n-2}`, `s_0=2,s_1=a`, as used in `06d` and `06g`. The scripts derive `a` from the actual curve equation. They do not turn six checked values into a purported proof for all n. Norm identities and channel normalisations are direct matrix identities for every n or L.

## 4. What a practitioner can build tonight and what nobody can

Build E0 to see a zero created by destructive interference with a literal subshift. Build the four-letter elliptic tensors to add RH and, on projective completion, FE; they also give a unique stationary channel. Change the Pauli weights to break RH while keeping FE and stationarity. Add an idle qubit to destroy uniqueness without moving any divisor points. Build the Horner tensors to compute tiny Dirichlet polynomials with actual coefficient letters and character boundaries. Build the graph cover to see an Artin decomposition whose nontrivial factors have poles. Build the amplitude-damping cMPS to see an additive FE, a uniform odd decay rate, and a unique vacuum.

A precise sufficient checklist for a “tiny Riemann” is: a convergent positive integer prime Euler product with infinitely many prime species; a specified meromorphic continuation and completion with the intended pole divisor; reciprocal/additive symmetry of the retained modes; and either the critical-circle/line condition itself, or Weil positive definiteness plus that symmetry. A unique channel fixed point is a further physical condition, not a replacement for the analytic requirements. Growth and summability are needed in an infinite setting. In particular, positivity of norms and an FE do not force RH: the explicit off-circle CPTP tensor disproves that shortcut.

A single simple pole at `u=1/q` is incompatible with the **uncompleted**, self-reciprocal curve-type FE for `q>1`: reflection also requires a pole at `u=1`. State whether the second pole is in the completion. The same bookkeeping applies to the generator poles at zero and κ. Riemann's one-pole uncompleted function has archimedean/completion data absent from a bare finite ring determinant.

No finite bond can produce a nonrational zeta in u, or a finite-cMPS norm equal to a nonzero atomic prime comb. It **can** produce infinitely many primitive necklaces and hence infinitely many Euler factors. Substituting `u=q^{-s}` produces infinitely many periodic copies of finitely many divisor points in the s-plane; that is not Riemann's zero distribution. The no-go in `06e`/`04b` says no finite matrix or trace-class operator has a curve's uncancelled genus-positive counts as a **plain power trace**. The graded norm constructions here evade exactly that obstruction, by negative net coherence multiplicities.

“Factor by factor” constructs and tests local spectra, characters, primes, normalisations and dualities. It does not make an infinite product converge, produce its continuation or archimedean factors, select a prescribed entanglement spectrum, or prove RH for an unidentified infinite object. The constructions above are finite models with stated mechanisms and stated limits; the infinite arithmetic identification remains open.

<!-- GENERATED EVIDENCE BELOW -->

## Reproducible matrix and number catalogue

Generated by `finite/run_all.py`. Every matrix entry below is an exact number (including radicals and the specified roots of unity); decimals are labelled. A repeated letter is a distinct orthonormal physical species. Matrix rows are printed in full, in row-major order.

**Verification: 461 passed checks; 0 failed scripts; 13 example scripts.**

### `e0_pair_shift.py` — 26 checks

Run: `python3 notes/zeta-conditions/finite/e0_pair_shift.py`.

- **Z**: `(2*u - 1)/(4*u - 1)`
- **C2_counterexample_Z**: `(u + 1)**2/(u - 1)**2`
- **weighted_subset_Z**: `(u - 4)/(2*(u - 2))`
- **inverse_counterexample_Z**: `(5*u - 2)**2/((2*u - 1)*(17*u - 4))`

| Sequence | Entries in order |
|---|---|
| N_1..6 | `2`, `12`, `56`, `240`, `992`, `4032` |
| a_1..6 | `2`, `5`, `18`, `57`, `198`, `661` |
| C2_counterexample_N | `4`, `0`, `4`, `0`, `4`, `0` |
| C2_counterexample_a | `4`, `-2`, `0`, `0`, `0`, `0` |
| fake_swap_N | `1`, `6`, `28`, `120`, `496`, `2016` |
| fake_swap_a | `1`, `5/2`, `9`, `57/2`, `99`, `661/2` |
| weighted_subset_N | `1/4`, `3/16`, `7/64`, `15/256`, `31/1024`, `63/4096` |
| weighted_subset_a | `1/4`, `-1/32`, `-3/64`, `-33/1024`, `-45/1024`, `-43/8192` |
| inverse_counterexample_N | `5/4`, `153/16`, `3425/64`, `67617/256`, `1252625/1024`, `22399713/4096` |
| inverse_counterexample_a | `5/4`, `133/32`, `1115/64`, `65169/1024`, `250269/1024`, `7382155/8192` |

**A_00** (2 × 2):
```text
[1, 0]
[0, 1]
```

**A_01** (2 × 2):
```text
[1, 0]
[0, 0]
```

**A_10** (2 × 2):
```text
[1, 0]
[0, 0]
```

**A_11** (2 × 2):
```text
[1, 0]
[0, 1]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**E_d** (4 × 4):
```text
[4, 0, 0, 0]
[0, 2, 0, 0]
[0, 0, 2, 0]
[0, 0, 0, 2]
```

**counterexample_C2_A** (2 × 2):
```text
[1, 0]
[0, -1]
```

**inverse_B** (2 × 2):
```text
[1, 0]
[0, 2]
```

**inverse_Binv** (2 × 2):
```text
[1, 0]
[0, 1/2]
```

**inverse_E_d** (4 × 4):
```text
[2, 0, 0, 0]
[0, 5/2, 0, 0]
[0, 0, 5/2, 0]
[0, 0, 0, 17/4]
```

**weighted_subset_A_0** (2 × 2):
```text
[1/2, 0]
[0, 1/2]
```

**weighted_subset_A_1** (2 × 2):
```text
[1/2, 0]
[0, 0]
```


### `curve_affine.py` — 26 checks

Run: `python3 notes/zeta-conditions/finite/curve_affine.py`.

- **Z**: `-(5*u**2 + 3*u + 1)/(5*u - 1)`
- **pi from N1**: `-3/2 + sqrt(11)*I/2`

| Sequence | Entries in order |
|---|---|
| N_1..6 | `8`, `26`, `107`, `674`, `3068`, `15551` |
| a_1..6 | `8`, `9`, `33`, `162`, `612`, `2571` |

**A_0** (2 × 2):
```text
[sqrt(10)/2, 0]
[0, sqrt(10)*(-3 + sqrt(11)*I)/10]
```

**A_1** (2 × 2):
```text
[0, 0]
[0, sqrt(2)/2]
```

**A_2** (2 × 2):
```text
[0, sqrt(10)/2]
[0, 0]
```

**A_3** (2 × 2):
```text
[0, 0]
[sqrt(10)/2, 0]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**E_d** (4 × 4):
```text
[5/2, 0, 0, 5/2]
[0, -3/2 - sqrt(11)*I/2, 0, 0]
[0, 0, -3/2 + sqrt(11)*I/2, 0]
[5/2, 0, 0, 5/2]
```


### `curve_projective.py` — 46 checks

Run: `python3 notes/zeta-conditions/finite/curve_projective.py`.

- **Z**: `(5*u**2 + 3*u + 1)/((u - 1)*(5*u - 1))`
- **pi from N1**: `-3/2 + sqrt(11)*I/2`

| Sequence | Entries in order |
|---|---|
| N_1..6 | `9`, `27`, `108`, `675`, `3069`, `15552` |
| a_1..6 | `9`, `9`, `33`, `162`, `612`, `2571` |

**A_0** (2 × 2):
```text
[sqrt(3), 0]
[0, sqrt(3)*(-3 + sqrt(11)*I)/6]
```

**A_1** (2 × 2):
```text
[0, 0]
[0, 2*sqrt(3)/3]
```

**A_2** (2 × 2):
```text
[0, sqrt(2)]
[0, 0]
```

**A_3** (2 × 2):
```text
[0, 0]
[sqrt(2), 0]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**E_d** (4 × 4):
```text
[3, 0, 0, 2]
[0, -3/2 - sqrt(11)*I/2, 0, 0]
[0, 0, -3/2 + sqrt(11)*I/2, 0]
[2, 0, 0, 3]
```

**product_A_0** (2 × 2):
```text
[sqrt(2)/2, 0]
[0, sqrt(2)*(-3 + sqrt(11)*I)/4]
```

**product_A_1** (2 × 2):
```text
[sqrt(2)/2, 0]
[0, sqrt(2)*(-3 + sqrt(11)*I)/4]
```

**product_E_d** (4 × 4):
```text
[1, 0, 0, 0]
[0, -3/2 - sqrt(11)*I/2, 0, 0]
[0, 0, -3/2 + sqrt(11)*I/2, 0]
[0, 0, 0, 5]
```

**Hodge_J** (4 × 4):
```text
[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 1, 0, 0]
[1, 0, 0, 0]
```

**damping_A_0** (2 × 2):
```text
[-3/2 + sqrt(11)*I/2, 0]
[0, 1]
```

**damping_A_1** (2 × 2):
```text
[0, 2]
[0, 0]
```


### `curve_supersingular.py` — 34 checks

Run: `python3 notes/zeta-conditions/finite/curve_supersingular.py`.

- **Z**: `(2*u + 1)**2/((u - 1)*(4*u - 1))`
- **pi from N1**: `-2`

| Sequence | Entries in order |
|---|---|
| N_1..6 | `9`, `9`, `81`, `225`, `1089`, `3969` |
| a_1..6 | `9`, `0`, `24`, `54`, `216`, `648` |

**A_0** (2 × 2):
```text
[sqrt(10)/2, 0]
[0, -2*sqrt(10)/5]
```

**A_1** (2 × 2):
```text
[0, 0]
[0, 3*sqrt(10)/10]
```

**A_2** (2 × 2):
```text
[0, sqrt(6)/2]
[0, 0]
```

**A_3** (2 × 2):
```text
[0, 0]
[sqrt(6)/2, 0]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**E_d** (4 × 4):
```text
[5/2, 0, 0, 3/2]
[0, -2, 0, 0]
[0, 0, -2, 0]
[3/2, 0, 0, 5/2]
```

**product_A** (2 × 2):
```text
[1, 0]
[0, -2]
```


### `z2_shift_cover.py` — 31 checks

Run: `python3 notes/zeta-conditions/finite/z2_shift_cover.py`.

- **Z_cover**: `1/((1 - 3*u)*(u + 1))`
- **L_trivial**: `1/(1 - 3*u)`
- **L_sign**: `1/(u + 1)`

| Sequence | Entries in order |
|---|---|
| N_1..6 | `2`, `10`, `26`, `82`, `242`, `730` |
| a_1..6 | `2`, `4`, `8`, `18`, `48`, `116` |
| deck_twisted_traces | `4`, `8`, `28`, `80`, `244`, `728` |
| N_sign_1..6 | `-1`, `1`, `-1`, `1`, `-1`, `1` |
| a_sign_1..6 | `-1`, `1`, `0`, `0`, `0`, `0` |

**A_0** (2 × 2):
```text
[1, 0]
[0, 0]
```

**A_1** (2 × 2):
```text
[0, 0]
[1, 0]
```

**A_2** (2 × 2):
```text
[0, 0]
[1, 0]
```

**A_3** (2 × 2):
```text
[0, 0]
[0, 1]
```

**A_4** (2 × 2):
```text
[0, 1]
[0, 0]
```

**A_5** (2 × 2):
```text
[0, 1]
[0, 0]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, 1]
```

**deck_X** (2 × 2):
```text
[0, 1]
[1, 0]
```

**path_C** (2 × 2):
```text
[1, 2]
[2, 1]
```

**Artin_trivial_amplitude_letter** (1 × 1):
```text
[3]
```

**Artin_sign_amplitude_letter** (1 × 1):
```text
[-1]
```


### `dirichlet_f2.py` — 23 checks

Run: `python3 notes/zeta-conditions/finite/dirichlet_f2.py`.

- **L**: `-(u - 1)*(u*w**3 + u*w + u + 1)`
- **alpha**: `-w**3 - w - 1`
- **alpha_decimal**: `(-0.7225209339563143-1.2157152215855884j)`
- **w**: `exp(2*pi*i/7)`
- **primitive_generator_digits**: `[0, 1, 0]`
- **odd_character_k**: `1`

| Sequence | Entries in order |
|---|---|
| L_monic_coefficients_0..6 | `1`, `w**3 + w`, `-w**3 - w - 1`, `0`, `0`, `0`, `0` |
| log_N_1..6_exact | `w**3 + w`, `w**5 - w**4 - w**3 - w - 1`, `3*w**4 + w**3 + w**2`, `-3*w**5 - 3*w**4 - 2*w**3 - 4`, `w**5 - 5*w**2 + w`, `5*w**5 + 5*w**3 + 5*w**2 - 2*w - 1` |
| log_N_1..6_decimal | `(-0.27747906604368566+1.2157152215855884j)`, `(-0.044073000010209806-1.7567593946498548j)`, `(-3.8263964055659905+0.10716043394670804j)`, `(1.17240714138104+3.3586674756630295j)`, `(1.5135735376839907-5.067735990622914j)`, `(-8.977033282792704+0.6057557306517314j)` |
| formal_a_1..6_exact | `w**3 + w`, `w**5/2 - w**4/2 - w**3 - w - 1/2`, `w**4 + w**2/3 - w/3`, `-w**5 - w**4/2 - w**3/4 + w/4 - 3/4`, `w**5/5 - w**3/5 - w**2`, `2*w**5/3 - w**4/3 + w**3 + 2*w**2/3` |
| formal_a_1..6_decimal | `(-0.27747906604368566+1.2157152215855884j)`, `(0.1167030330167379-1.4862373081177207j)`, `(-1.182972446507435-0.3695182625462934j)`, `(0.3041200353478124+1.2788567175782202j)`, `(0.3582105207455353-1.2566902424416995j)`, `(-0.8973404905433657+0.5785116521567444j)` |
| physical_open_norm_1..6 | `2`, `4`, `7`, `14`, `28`, `56` |

**H_0** (8 × 8):
```text
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
```

**H_1** (8 × 8):
```text
[0, 0, 0, 0, 0, 1, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
```

**Pi_open** (8 × 8):
```text
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
```

**right_boundary_e1** (8 × 1):
```text
[0]
[1]
[0]
[0]
[0]
[0]
[0]
[0]
```

**left_character_row** (1 × 8):
```text
[0, 1, w, w**3, w**2, w**6, w**4, w**5]
```

**multiplication_by_generator** (8 × 8):
```text
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
```

**amplitude_F_odd** (2 × 2):
```text
[1, 0]
[0, -w**3 - w - 1]
```

**Pi_amplitude** (2 × 2):
```text
[-1, 0]
[0, -1]
```

- The formal a_d are Mobius exponents, not the character sums over degree-d primes.
- The displayed character row is linear; a bra ket for it uses the conjugate ket.

### `dirichlet_f3.py` — 24 checks

Run: `python3 notes/zeta-conditions/finite/dirichlet_f3.py`.

- **L**: `-u*w**3 - u*w**2 + u*w + 1`
- **alpha**: `w**3 + w**2 - w`
- **alpha_decimal**: `(-1.414213562373094+1j)`
- **w**: `exp(2*pi*i/8)`
- **primitive_generator_digits**: `[1, 1]`
- **odd_character_k**: `1`

| Sequence | Entries in order |
|---|---|
| L_monic_coefficients_0..6 | `1`, `-w**3 - w**2 + w`, `0`, `0`, `0`, `0`, `0` |
| log_N_1..6_exact | `-w**3 - w**2 + w`, `2*w**3 + 2*w - 1`, `w**3 - 5*w**2 - w`, `4*w**3 + 4*w + 7`, `11*w**3 - w**2 - 11*w`, `-10*w**3 - 10*w + 23` |
| log_N_1..6_decimal | `(1.414213562373094-1j)`, `(-0.9999999999999991+2.8284271247461916j)`, `(-1.4142135623730958-5j)`, `(7+5.656854249492383j)`, `(-15.556349186104043-0.9999999999999973j)`, `(23-14.142135623730951j)` |
| formal_a_1..6_exact | `-w**3 - w**2 + w`, `3*w**3/2 + w**2/2 + w/2 - 1/2`, `2*w**3/3 - 4*w**2/3 - 2*w/3`, `w**3/2 + w/2 + 2`, `12*w**3/5 - 12*w/5`, `-7*w**3/3 + 2*w**2/3 - 5*w/3 + 4` |
| formal_a_1..6_decimal | `(1.414213562373094-1j)`, `(-1.207106781186548+1.9142135623730958j)`, `(-0.9428090415820636-1.333333333333334j)`, `(2+0.7071067811865479j)`, `(-3.3941125496954285+5.873123168353978e-16j)`, `(4.471404520791033-2.1617604580795238j)` |
| physical_open_norm_1..6 | `3`, `8`, `24`, `72`, `216`, `648` |

**H_0** (9 × 9):
```text
[1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 0, 0]
```

**H_1** (9 × 9):
```text
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
```

**H_2** (9 × 9):
```text
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0]
```

**Pi_open** (9 × 9):
```text
[1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
```

**right_boundary_e1** (9 × 1):
```text
[0]
[1]
[0]
[0]
[0]
[0]
[0]
[0]
[0]
```

**left_character_row** (1 × 9):
```text
[0, 1, w**4, w**6, w, w**7, w**2, w**3, w**5]
```

**multiplication_by_generator** (9 × 9):
```text
[1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0]
```

**amplitude_F_odd** (1 × 1):
```text
[w*(w**2 + w - 1)]
```

**Pi_amplitude** (1 × 1):
```text
[-1]
```

- The formal a_d are Mobius exponents, not the character sums over degree-d primes.
- The displayed character row is linear; a bra ket for it uses the conjugate ket.

### `gauss.py` — 14 checks

Run: `python3 notes/zeta-conditions/finite/gauss.py`.

- **G_standard_sum**: `sqrt(3)*I`
- **L_standard**: `sqrt(3)*I*u + 1`
- **L_if_G_means_Frobenius_alpha**: `sqrt(3)*I*u + 1`
- **physical_open_norm_degree_n**: `3**n`

| Sequence | Entries in order |
|---|---|
| log_N_1..6 | `sqrt(3)*I`, `3`, `-3*sqrt(3)*I`, `-9`, `9*sqrt(3)*I`, `27` |
| formal_a_1..6 | `sqrt(3)*I`, `3/2 - sqrt(3)*I/2`, `-4*sqrt(3)*I/3`, `-3`, `8*sqrt(3)*I/5`, `4 + 2*sqrt(3)*I/3` |

**open_A_0** (1 × 1):
```text
[1]
```

**open_A_1** (1 × 1):
```text
[-1/2 + sqrt(3)*I/2]
```

**open_A_2** (1 × 1):
```text
[-1/2 + sqrt(3)*I/2]
```

**open_boundary** (1 × 1):
```text
[1]
```

**amplitude_F** (1 × 1):
```text
[-sqrt(3)*I]
```

**Pi_amplitude** (1 × 1):
```text
[-1]
```


### `kloosterman.py` — 24 checks

Run: `python3 notes/zeta-conditions/finite/kloosterman.py`.

- **L_Kl**: `4*u**2 + 3*u + 1`
- **Z_affine**: `-(4*u**2 + 3*u + 1)/(4*u - 1)`
- **pi from Kl1**: `-3/2 + sqrt(7)*I/2`

| Sequence | Entries in order |
|---|---|
| raw_Kl_1..6 | `3`, `-1`, `-9`, `31`, `-57`, `47` |
| N_1..6 | `7`, `15`, `55`, `287`, `967`, `4143` |
| a_1..6 | `7`, `4`, `16`, `68`, `192`, `680` |
| L_log_N_1..6 | `3`, `-1`, `-9`, `31`, `-57`, `47` |
| L_formal_a_1..6 | `3`, `-2`, `-4`, `8`, `-12`, `10` |

**A_0** (2 × 2):
```text
[sqrt(2), 0]
[0, sqrt(2)*(-3 + sqrt(7)*I)/4]
```

**A_1** (2 × 2):
```text
[0, 0]
[0, 0]
```

**A_2** (2 × 2):
```text
[0, sqrt(2)]
[0, 0]
```

**A_3** (2 × 2):
```text
[0, 0]
[sqrt(2), 0]
```

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**E_d** (4 × 4):
```text
[2, 0, 0, 2]
[0, -3/2 - sqrt(7)*I/2, 0, 0]
[0, 0, -3/2 + sqrt(7)*I/2, 0]
[2, 0, 0, 2]
```

**amplitude_F** (2 × 2):
```text
[0, -4]
[1, -3]
```

**Pi_amplitude** (2 × 2):
```text
[-1, 0]
[0, -1]
```


### `graph_artin.py` — 46 checks

Run: `python3 notes/zeta-conditions/finite/graph_artin.py`.

- **Z_cover**: `1/((u - 1)**3*(u + 1)**2*(3*u - 1)*(3*u**2 + 1))`
- **L_trivial**: `-1/((u - 1)**2*(u + 1)*(3*u - 1))`
- **L_sign**: `-1/((u - 1)*(u + 1)*(3*u**2 + 1))`
- **Z_curve**: `(3*u**2 + 1)/((u - 1)*(3*u - 1))`

| Sequence | Entries in order |
|---|---|
| N_cover_1..6 | `4`, `8`, `28`, `104`, `244`, `680` |
| a_cover_1..6 | `4`, `2`, `8`, `24`, `48`, `108` |
| N_sign_1..6 | `0`, `-4`, `0`, `20`, `0`, `-52` |
| a_sign_1..6 | `0`, `-2`, `0`, `6`, `0`, `-8` |
| N_curve_1..6 | `4`, `16`, `28`, `64`, `244`, `784` |
| a_curve_1..6 | `4`, `6`, `8`, `12`, `48`, `124` |

**cover_A_0** (8 × 8):
```text
[1, 0, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_1** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_2** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_3** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_4** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_5** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_6** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_A_7** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 1, 0, 0, 0, 0]
```

**Pi_cover** (8 × 8):
```text
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
```

**cover_TP_A_0** (8 × 8):
```text
[sqrt(3)/3, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[sqrt(3)/3, 0, 0, 0, 0, 0, 0, 0]
[sqrt(3)/3, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_TP_A_1** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, sqrt(3)/3, 0, 0, 0, 0, 0, 0]
[0, sqrt(3)/3, 0, 0, 0, 0, 0, 0]
[0, sqrt(3)/3, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_TP_A_2** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, sqrt(3)/3, 0, 0, 0, 0, 0]
[0, 0, sqrt(3)/3, 0, 0, 0, 0, 0]
[0, 0, sqrt(3)/3, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_TP_A_3** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, sqrt(3)/3, 0, 0, 0, 0]
[0, 0, 0, sqrt(3)/3, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, sqrt(3)/3, 0, 0, 0, 0]
```

**cover_TP_A_4** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, sqrt(3)/3, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, sqrt(3)/3, 0, 0, 0]
[0, 0, 0, 0, sqrt(3)/3, 0, 0, 0]
```

**cover_TP_A_5** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, sqrt(3)/3, 0, 0]
[0, 0, 0, 0, 0, sqrt(3)/3, 0, 0]
[0, 0, 0, 0, 0, sqrt(3)/3, 0, 0]
```

**cover_TP_A_6** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, sqrt(3)/3, 0]
[0, 0, 0, 0, 0, 0, sqrt(3)/3, 0]
[0, 0, 0, 0, 0, 0, sqrt(3)/3, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**cover_TP_A_7** (8 × 8):
```text
[0, 0, 0, 0, 0, 0, 0, sqrt(3)/3]
[0, 0, 0, 0, 0, 0, 0, sqrt(3)/3]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, sqrt(3)/3]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

**H_base** (4 × 4):
```text
[1, 0, 1, 1]
[0, 1, 1, 1]
[1, 1, 1, 0]
[1, 1, 0, 1]
```

**H_sign** (4 × 4):
```text
[1, 0, 1, 1]
[0, 1, 1, 1]
[-1, -1, -1, 0]
[-1, -1, 0, -1]
```

**H_cover** (8 × 8):
```text
[1, 0, 1, 1, 0, 0, 0, 0]
[0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 1, 1, 0, 1]
[0, 0, 0, 0, 1, 0, 1, 1]
[0, 0, 0, 0, 0, 1, 1, 1]
[1, 1, 1, 0, 0, 0, 0, 0]
[1, 1, 0, 1, 0, 0, 0, 0]
```

**deck** (8 × 8):
```text
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
```

**Bass_even** (2 × 2):
```text
[0, -3]
[1, 4]
```

**Bass_odd** (2 × 2):
```text
[0, -3]
[1, 0]
```

**curve_A_0** (2 × 2):
```text
[sqrt(2), 0]
[0, sqrt(6)*I/2]
```

**curve_A_1** (2 × 2):
```text
[0, 0]
[0, sqrt(2)/2]
```

**curve_A_2** (2 × 2):
```text
[0, 1]
[0, 0]
```

**curve_A_3** (2 × 2):
```text
[0, 0]
[1, 0]
```

**Pi_curve** (2 × 2):
```text
[1, 0]
[0, -1]
```


### `independence.py` — 131 checks

Run: `python3 notes/zeta-conditions/finite/independence.py`.

- **TTT_Z**: `(4*u - 1)**2/((u - 1)*(16*u - 1))`
- **TTF_Z**: `(4*u - 1)**8/((u - 1)**4*(16*u - 1)**4)`
- **TFT_Z**: `(2*u - 1)*(8*u - 1)/((u - 1)*(16*u - 1))`
- **TFF_Z**: `(2*u - 1)**4*(8*u - 1)**4/((u - 1)**4*(16*u - 1)**4)`
- **FTT_Z**: `-(4*u - 1)**2/(16*u - 1)`
- **FTF_Z**: `(4*u - 1)**8/(16*u - 1)**4`
- **FFT_Z**: `(3*u - 1)**2/((u - 1)*(16*u - 1))`
- **FFF_Z**: `(3*u - 1)**8/((u - 1)**4*(16*u - 1)**4)`
- **periodic_Z**: `-1/((2*u - 1)*(2*u + 1))`

| Sequence | Entries in order |
|---|---|
| TTT_N_1..6 | `9`, `225`, `3969`, `65025`, `1046529`, `16769025` |
| TTT_a_1..6 | `9`, `108`, `1320`, `16200`, `209304`, `2794140` |
| TTF_N_1..6 | `36`, `900`, `15876`, `260100`, `4186116`, `67076100` |
| TTF_a_1..6 | `36`, `432`, `5280`, `64800`, `837216`, `11176560` |
| TFT_N_1..6 | `7`, `189`, `3577`, `61425`, `1015777`, `16515009` |
| TFT_a_1..6 | `7`, `91`, `1190`, `15309`, `203154`, `2751875` |
| TFF_N_1..6 | `28`, `756`, `14308`, `245700`, `4063108`, `66060036` |
| TFF_a_1..6 | `28`, `364`, `4760`, `61236`, `812616`, `11007500` |
| FTT_N_1..6 | `8`, `224`, `3968`, `65024`, `1046528`, `16769024` |
| FTT_a_1..6 | `8`, `108`, `1320`, `16200`, `209304`, `2794140` |
| FTF_N_1..6 | `32`, `896`, `15872`, `260096`, `4186112`, `67076096` |
| FTF_a_1..6 | `32`, `432`, `5280`, `64800`, `837216`, `11176560` |
| FFT_N_1..6 | `11`, `239`, `4043`, `65375`, `1048091`, `16775759` |
| FFT_a_1..6 | `11`, `114`, `1344`, `16284`, `209616`, `2795248` |
| FFF_N_1..6 | `44`, `956`, `16172`, `261500`, `4192364`, `67103036` |
| FFF_a_1..6 | `44`, `456`, `5376`, `65136`, `838464`, `11180992` |
| periodic_N_1..6 | `0`, `8`, `0`, `32`, `0`, `128` |
| periodic_a_1..6 | `0`, `4`, `0`, `6`, `0`, `20` |

**TTT_A_0** (2 × 2):
```text
[5/2, 0]
[0, 5/2]
```

**TTT_A_1** (2 × 2):
```text
[3/2, 0]
[0, -3/2]
```

**TTT_A_2** (2 × 2):
```text
[0, sqrt(15)/2]
[sqrt(15)/2, 0]
```

**TTT_A_3** (2 × 2):
```text
[0, -sqrt(15)*I/2]
[sqrt(15)*I/2, 0]
```

**TTT_Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**TTF_A_0** (4 × 4):
```text
[5/2, 0, 0, 0]
[0, 5/2, 0, 0]
[0, 0, 5/2, 0]
[0, 0, 0, 5/2]
```

**TTF_A_1** (4 × 4):
```text
[3/2, 0, 0, 0]
[0, 3/2, 0, 0]
[0, 0, -3/2, 0]
[0, 0, 0, -3/2]
```

**TTF_A_2** (4 × 4):
```text
[0, 0, sqrt(15)/2, 0]
[0, 0, 0, sqrt(15)/2]
[sqrt(15)/2, 0, 0, 0]
[0, sqrt(15)/2, 0, 0]
```

**TTF_A_3** (4 × 4):
```text
[0, 0, -sqrt(15)*I/2, 0]
[0, 0, 0, -sqrt(15)*I/2]
[sqrt(15)*I/2, 0, 0, 0]
[0, sqrt(15)*I/2, 0, 0]
```

**TTF_Pi** (4 × 4):
```text
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, -1, 0]
[0, 0, 0, -1]
```

**TFT_A_0** (2 × 2):
```text
[3*sqrt(3)/2, 0]
[0, 3*sqrt(3)/2]
```

**TFT_A_1** (2 × 2):
```text
[sqrt(7)/2, 0]
[0, -sqrt(7)/2]
```

**TFT_A_2** (2 × 2):
```text
[0, sqrt(21)/2]
[sqrt(21)/2, 0]
```

**TFT_A_3** (2 × 2):
```text
[0, -3*I/2]
[3*I/2, 0]
```

**TFT_Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**TFF_A_0** (4 × 4):
```text
[3*sqrt(3)/2, 0, 0, 0]
[0, 3*sqrt(3)/2, 0, 0]
[0, 0, 3*sqrt(3)/2, 0]
[0, 0, 0, 3*sqrt(3)/2]
```

**TFF_A_1** (4 × 4):
```text
[sqrt(7)/2, 0, 0, 0]
[0, sqrt(7)/2, 0, 0]
[0, 0, -sqrt(7)/2, 0]
[0, 0, 0, -sqrt(7)/2]
```

**TFF_A_2** (4 × 4):
```text
[0, 0, sqrt(21)/2, 0]
[0, 0, 0, sqrt(21)/2]
[sqrt(21)/2, 0, 0, 0]
[0, sqrt(21)/2, 0, 0]
```

**TFF_A_3** (4 × 4):
```text
[0, 0, -3*I/2, 0]
[0, 0, 0, -3*I/2]
[3*I/2, 0, 0, 0]
[0, 3*I/2, 0, 0]
```

**TFF_Pi** (4 × 4):
```text
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, -1, 0]
[0, 0, 0, -1]
```

**FTT_A_0** (2 × 2):
```text
[sqrt(6), 0]
[0, sqrt(6)]
```

**FTT_A_1** (2 × 2):
```text
[sqrt(2), 0]
[0, -sqrt(2)]
```

**FTT_A_2** (2 × 2):
```text
[0, 2]
[2, 0]
```

**FTT_A_3** (2 × 2):
```text
[0, -2*I]
[2*I, 0]
```

**FTT_Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**FTF_A_0** (4 × 4):
```text
[sqrt(6), 0, 0, 0]
[0, sqrt(6), 0, 0]
[0, 0, sqrt(6), 0]
[0, 0, 0, sqrt(6)]
```

**FTF_A_1** (4 × 4):
```text
[sqrt(2), 0, 0, 0]
[0, sqrt(2), 0, 0]
[0, 0, -sqrt(2), 0]
[0, 0, 0, -sqrt(2)]
```

**FTF_A_2** (4 × 4):
```text
[0, 0, 2, 0]
[0, 0, 0, 2]
[2, 0, 0, 0]
[0, 2, 0, 0]
```

**FTF_A_3** (4 × 4):
```text
[0, 0, -2*I, 0]
[0, 0, 0, -2*I]
[2*I, 0, 0, 0]
[0, 2*I, 0, 0]
```

**FTF_Pi** (4 × 4):
```text
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, -1, 0]
[0, 0, 0, -1]
```

**FFT_A_0** (2 × 2):
```text
[sqrt(23)/2, 0]
[0, sqrt(23)/2]
```

**FFT_A_1** (2 × 2):
```text
[sqrt(11)/2, 0]
[0, -sqrt(11)/2]
```

**FFT_A_2** (2 × 2):
```text
[0, sqrt(15)/2]
[sqrt(15)/2, 0]
```

**FFT_A_3** (2 × 2):
```text
[0, -sqrt(15)*I/2]
[sqrt(15)*I/2, 0]
```

**FFT_Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**FFF_A_0** (4 × 4):
```text
[sqrt(23)/2, 0, 0, 0]
[0, sqrt(23)/2, 0, 0]
[0, 0, sqrt(23)/2, 0]
[0, 0, 0, sqrt(23)/2]
```

**FFF_A_1** (4 × 4):
```text
[sqrt(11)/2, 0, 0, 0]
[0, sqrt(11)/2, 0, 0]
[0, 0, -sqrt(11)/2, 0]
[0, 0, 0, -sqrt(11)/2]
```

**FFF_A_2** (4 × 4):
```text
[0, 0, sqrt(15)/2, 0]
[0, 0, 0, sqrt(15)/2]
[sqrt(15)/2, 0, 0, 0]
[0, sqrt(15)/2, 0, 0]
```

**FFF_A_3** (4 × 4):
```text
[0, 0, -sqrt(15)*I/2, 0]
[0, 0, 0, -sqrt(15)*I/2]
[sqrt(15)*I/2, 0, 0, 0]
[0, sqrt(15)*I/2, 0, 0]
```

**FFF_Pi** (4 × 4):
```text
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, -1, 0]
[0, 0, 0, -1]
```

**periodic_A_0** (2 × 2):
```text
[0, sqrt(2)]
[0, 0]
```

**periodic_A_1** (2 × 2):
```text
[0, 0]
[sqrt(2), 0]
```

**periodic_Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**TFT_Weil_minor** (2 × 2):
```text
[2, 5/2]
[5/2, 2]
```

**TFT_Weil_witness** (2 × 1):
```text
[1]
[-1]
```

- Tags give (C4, C5, C6 ergodic channel). FT has only the pole at 1/16: the even zero mode is invisible to positive powers.
- Every A/4 family is CPTP; the idle qubit yields a stationary matrix algebra, not just a duplicated trace.

### `cmps_half.py` — 18 checks

Run: `python3 notes/zeta-conditions/finite/cmps_half.py`.

- **N_regular**: `exp(2L)-exp(L)`
- **Z_regular**: `(z - 1)/(z - 2)`
- **N_Lindblad**: `1-exp(-L)`
- **Z_Lindblad**: `(z + 1)/z`
- **shift_to_positive_exponents**: `Q_Lindblad + I gives T_Lindblad + 2I`

| Sequence | Entries in order |
|---|---|
| N_L=1..6 | `4.670774270471606`, `47.209093934213584`, `383.34325656954746`, `2926.3598370085842`, `21878.05263570414`, `162351.3626255112` |
| N_exact_L=1..6 | `-E + exp(2)`, `-exp(2) + exp(4)`, `-exp(3) + exp(6)`, `-exp(4) + exp(8)`, `-exp(5) + exp(10)`, `-exp(6) + exp(12)` |

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**Q_regular** (2 × 2):
```text
[1/2, 0]
[0, 1/2]
```

**R_regular** (2 × 2):
```text
[1, 0]
[0, 0]
```

**T_regular** (4 × 4):
```text
[2, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
```

**Q_Lindblad** (2 × 2):
```text
[-1/8, 0]
[0, -5/8]
```

**R_fermion** (2 × 2):
```text
[0, 1]
[0, 0]
```

**R_boson** (2 × 2):
```text
[1/2, 0]
[0, -1/2]
```

**T_Lindblad** (4 × 4):
```text
[0, 0, 0, 1]
[0, -1, 0, 0]
[0, 0, -1, 0]
[0, 0, 0, -1]
```

**H_Lindblad** (2 × 2):
```text
[0, 0]
[0, 0]
```

- No intrinsic integer-degree prime counts in continuous length.
- Regular bosonic tensor is not TP gaugeable on the whole bond; its Perron left eigenmatrix has rank one.

### `cmps_fe.py` — 18 checks

Run: `python3 notes/zeta-conditions/finite/cmps_fe.py`.

- **N**: `1+exp(2L)-2exp(L)cos(L)`
- **Z_growth**: `((z - 1)**2 + 1)/(z*(z - 2))`
- **Z_normalized**: `((z + 1)**2 + 1)/(z*(z + 2))`

| Sequence | Entries in order |
|---|---|
| N_L=1..6 | `5.451668219098879`, `61.748014674422954`, `444.19785518102907`, `3053.333452001966`, `21943.267392681642`, `161981.07073842204` |
| N_exact_L=1..6 | `-2*E*cos(1) + 1 + exp(2)`, `1 - 2*exp(2)*cos(2) + exp(4)`, `1 - 2*exp(3)*cos(3) + exp(6)`, `1 - 2*exp(4)*cos(4) + exp(8)`, `-2*exp(5)*cos(5) + 1 + exp(10)`, `-2*exp(6)*cos(6) + 1 + exp(12)` |

**Pi** (2 × 2):
```text
[1, 0]
[0, -1]
```

**H** (2 × 2):
```text
[0, 0]
[0, 1]
```

**R** (2 × 2):
```text
[0, sqrt(2)]
[0, 0]
```

**Q_normalized** (2 × 2):
```text
[0, 0]
[0, -1 - I]
```

**Q_growth** (2 × 2):
```text
[1, 0]
[0, -I]
```

**T_normalized** (4 × 4):
```text
[0, 0, 0, 2]
[0, -1 + I, 0, 0]
[0, 0, -1 - I, 0]
[0, 0, 0, -2]
```

**T_growth** (4 × 4):
```text
[2, 0, 0, 2]
[0, 1 + I, 0, 0]
[0, 0, 1 - I, 0]
[0, 0, 0, 0]
```

- Odd decay rates are 1, even nonstationary decay rate 2; normalized correlation lengths 1 and 1/2.
- Continuous length has no intrinsic a_d. Sampling at L=n gives formal Mobius exponents, generally nonintegral.

