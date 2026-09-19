# RH through physical decay modes — checkpointed synthesis

Status: synthesis of five agent reviews and parent calculations, 2026-09-19. No RH proof. New deductions are research notes, not registered proved claims. Reports were written continuously; independent cross-checks and limitations are retained in each lane.

## The main research target

Construct prime-defined, graded cMPS letters and a physical field correlation whose observable decay modes are exactly the Riemann zero divisor. Derive their common width from those letters, with a stationary arithmetic bond and a controlled infinite limit. The current repo separately supplies pieces of this picture, not the complete construction.

An essential distinction now supported by an exact finite model: the relevant object may be the **observable odd subquotient**, determined by field insertions and their reachable/observable spaces, rather than the full odd transfer spectrum. A regular fermionic cMPS with a faithful mixed stationary bond can naturally select one decay band in a two-point function. See `graded-channels.md`, Checkpoint 5. The second cMPS review independently identifies the mechanism as closure of linear Majorana observables under a quadratic generator, and tests its limits under perturbations.

## Why the Selberg and Riemann decay modes differ

| Feature | Laplace-derived Selberg first band | Riemann scattering sector |
|---|---|---|
| Arithmetic/spectral parameter | Laplace eigenvalue `mu=s(1-s)` | zeta zero `rho`, scattering pole `s=rho/2` |
| Flow parameter in repo convention | `lambda=s-1` | candidate first-band parameter `lambda=rho/2-1` |
| Desired flow decay line | `Re lambda=-1/2`, if nontrivial `mu>=1/4` | `Re lambda=-3/4`, under RH |
| Riemann functional-model normalization | not this operator | `b=-conj(rho)/2`, desired `Re b=-1/4` |
| Positive spectral input | fibre pushforward to self-adjoint L2 Laplacian | outgoing Eisenstein data outside L2; ordinary spectral theorem unavailable |
| Extra proof input | spectral bound `mu>=1/4`; strictness for a full positive operator metric at the Jordan endpoint | arithmetic constraint forcing equal scattering widths; passivity alone allows unequal widths |

The scalar shifts are not a constructed intertwiner of the geodesic-flow, wave-scattering and cMPS operators. Functional-equation relabelling gives the Riemann modal spectrum as the proposed cusp subset shifted by `+1/2`; domain, residue and generalized-mode identification remain separate work.

Even if RH holds, at `s=1/4+i gamma/2` the scattering Laplace parameter is

`mu=s(1-s)=3/16+gamma^2/4+i gamma/4`.

For nonzero `gamma` it is nonreal. Thus the Riemann scattering modes cannot simply be turned into ordinary self-adjoint Laplace eigenfunctions by proving the Selberg gap. This is the clearest algebraic expression of the difference. The boundary term in integration by parts survives at the cusp and balances this imaginary part. Exact source and domain details are in `riemann-vs-selberg-operators.md`.

## Concrete deductions already obtained

- The normalized leading Eisenstein Gram matrix is `K_ij=1/(1-conj(s_i)-s_j)`. It is positive throughout the strip. For `C=diag(s_i-1/2)`, `C* K+K C=-11*`, yielding a finite one-exit cMPS realization. The physical Gram does not enforce equal widths; equal widths with one exit require nonnormality when more than one mode is present. See `cusp-bridge.md`.
- A stationary mixed reset can be tested directly: with no-jump generator `B`, exit `E=-(B+B*)` and target state `sigma`, measure/prepare renewal is possible exactly when `-(B sigma+sigma B*)>=0`. Reinsertion changes the physical transfer spectrum, so preserving no-jump modes is insufficient. See `cmps-renewal-bridge.md`.
- Uniform modal width is an equality of exit energy per stored modal energy. Full centered unitarity in the physical norm is stronger and can wrongly exclude valid decay models. See `positivity-products.md`, Checkpoint 6.
- Individual prime-power additions to Suzuki's exact covariance are indefinite. The required prime-defined positive correlation cannot be built as a simple sum of independent positive prime blocks. Time-bin increments instead expose a sparse Toeplitz/Schur-complement problem. See `positivity-products.md`.

## A physical cMPS mechanism, independently dissected

Use a graded four-dimensional bond, `P=Z tensor I`, one fermionic emission letter

`R=X tensor |0><1|`, `H=diag(aX+bZ,cX+dZ)`, `Q=-iH-R*R/2`.

Here `R^2=0`, `{R,R*}=I`, and `Q+Q*+R*R=0`. Thus the example satisfies the single-species fermionic regularity and canonical cMPS relations. At `a=c=d=1/2,b=0`, it has a unique faithful stationary bond density. Its physical fermion two-point resolvent is exactly

`8z(z^2+z+1) / [5(8z^4+8z^3+14z^2+6z+1)]`.

All four poles have real part `-1/4`; their imaginary parts are `+/- (sqrt(7)+/-2)/4`. The full odd transfer also has a faster band of width `3/4`, but the actual field insertions do not observe that band. No zeta zeros or spectral projectors were supplied. The calculation uses the parity-signed transfer dictated by the fermionic field ordering, not an arbitrary ordinary Lindblad two-point expression.

The explanation is structural: `R` and `R*` lie in the four-dimensional linear Majorana space, and the signed Heisenberg transfer preserves that space for the whole quadratic family. This is **physical observable closure**.

Uniform width is a separate statement. On this observable space let M be the drift and `N=M+I/4`. For `b=0` an explicit letter-derived involution satisfies `JNJ=-N`. In its two eigenspaces N is off diagonal. For `a>1/4`, its square reduces, in a positive metric, to minus the real symmetric matrix

`S=[[ (a-c)^2+d^2-1/16, -2d sqrt(a^2-1/16) ],`
`   [ -2d sqrt(a^2-1/16), (a+c)^2+d^2-1/16 ]]`.

The independent inequality **S>=0** forces the common width. In the original model its eigenvalues are `11/16 +/- sqrt(7)/4`, both positive. This gives a literal finite physical analogue of Selberg's quadratic relation followed by its Laplace spectral bound.

Two perturbations delimit the result:

- Setting `b=0.01` preserves CAR, CP, faithful stationarity and four-mode selection, but splits the widths to approximately `0.24622128` and `0.25377872`. Its centered characteristic polynomial has a nonzero linear term `-2bd y`, so the failure is exact.
- Adding `0.01 P` to the Hamiltonian preserves grading and the stationary state, but is a quartic fermion interaction. It breaks the linear observable closure and makes all eight odd poles visible.

A weak-drive case retains the reflection but violates the band inequality, also producing unequal widths. Hence the relevant recipe has three distinct requirements: **observable closure, reflection symmetry, and independent coercivity**. cMPS supplies a natural setting for all three; none may be silently inferred from the other two. Details, exact proofs and numerical residue tests are in `graded-channels.md` and `riemann-vs-selberg-cmps.md`.

## The wave model already has a stronger literature foundation

[Uetake (2007)](https://www.impan.pl/en/publishing-house/journals-and-series/annales-polonici-mathematici/all/92/2/85177/the-lax-8211-phillips-infinitesimal-generator-and-the-scattering-matrix-for-automorphic-functions), Theorems 4.2 and 4.4, supplies a factored modular Lax–Phillips generator with the zeta zeros as eigenvalues of `-2A_c`, including algebraic multiplicity and dense generalized-mode span. This substantially narrows the repo's older missing modal-realization input. It does not prove RH, a cMPS stationary arithmetic state, or the geodesic-to-wave intertwiner. Its full publisher PDF is cached at `refs/src/uetake-2007/paper.pdf`; no TeX source was located.

The half shift is explained by the actual wave equation: `u_tt=(1/4-Delta)u`. For Laplace parameter `s(1-s)` the decaying scattering branch has exponent `q=s-1/2`, whereas geodesic first-band bookkeeping has `lambda=s-1`. Thus `q=lambda+1/2` is a change of generator, not a change of time units. With `r=log y` and `u_0=y^(1/2)v(r,t)`, the cusp zero-mode wave equation becomes `v_tt=v_rr`: these are escape modes down the cusp.

A precise candidate map is now available. If the Poisson pushforward P satisfies `Delta P=-P(A^2+A)`, set `C=A+1/2` and `T u=(Pu,PCu)`. The first-order wave generator `W=[[0,I],[1/4-Delta,0]]` obeys `WT=TC` algebraically. What remains is its domain, outgoing quotient and residue/Jordan justification on the cusp. Bonthonneau–Weich's general cusp resolvent construction is cached in `refs/src/1712.07832/preprint.tex`; it does not by itself establish this correspondence.

Two repository corrections are recorded without changing registered claims: shard 04's old Hardy kernel exponential has the wrong sign for decay; and the entire-xi scattering symbol differs from the raw Eisenstein coefficient by the rational factor `(2i tau-1)/(2i tau+1)`. Both matter when constructing an operator rather than matching its nontrivial scalar pole set.

## Ranked next tasks

1. Develop a prime-defined analogue of the demonstrated fermionic observable closure. Derive its reflection and a quadratic positive operator from the letters; prove the required coercivity, without assigning the zero spectrum. The four-dimensional toy is the first controlled test case.
2. Complete the cusp/scattering-to-physical-transfer dictionary, including boundary conditions, rational scattering normalization, residues and Jordan chains.
3. Match the resulting integrated two-point function to the prime-defined Suzuki covariance, with exact cutoff limits. Positivity of that kernel is RH-equivalent; the new content must be the independently constructed letters/history identity.
4. Pursue Deligne-style tensor amplification only after identifying a product whose global growth loss is sublinear in tensor degree and whose relevant poles survive cancellation.

## Recovery

All lane reports, calculation scripts and outputs are in this directory. Original source archives and newly retrieved papers are retained in `refs/src/`; new receipts are here. `RECOVERY.md` explains atomic, checksummed snapshots in `.recovery/`, including otherwise Git-ignored references. See `.recovery/LATEST-full.json` for the latest full snapshot and `.recovery/LATEST-session.json` for the latest session checkpoint. Offline extraction and deliberate-corruption rejection are tested; receipts are in this directory. These are local disk backups, not off-site storage.
