# Brief for the prover: the Ihara square complex with a cusp. Horizontal cohomology of Gamma_1(N)[1/p] \ (H x T_p) is Eichler–Shimura, the Eisenstein classes are the radical of the cup pairing and the exit sector, the level-N scattering matrix is a diagonal matrix of GL_1 theta-channel edge quotients (H-ARITH over Q), and the level-N Riemann channel is a direct sum of character channels with one exit per class character

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/deninger-cusp/astra-proofs.md` (create
it; overwrite if present) and, if you want scratch computations, python files under
`notes/deninger-cusp/checks/`. Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy,
scipy is installed (mpmath has Dirichlet L-series; there is no PARI). Read first:

1. `notes/deninger-lps/src/lps-deninger-worked-example.md` (a cocompact finite model from a separate Codex
   conversation: horizontal cohomology 721-dimensional, transverse `T_17`, Bass doubling, even poles `1, 17`)
   and `notes/deninger-lps/src/manuscript.txt` (Theorem 5.2, Definition 6.1, Theorem 6.2, Proposition 9.3: the
   Bass companion of an eigenvalue `lambda` with `|lambda| > 2 sqrt q` violates positivity; Section 9–10).
2. The notebook's cusp work: `report/sections/04i*`, `04j*` (a finite graph with a cusp), `04k_elliptic_cavity_scattering.tex`
   (`thm:multi-exit-scattering`: `h` rays, `S(z) = -Q(z)^{-1} Q(1/z)`, `det S = (-1)^h p/ptilde`),
   `04l_elliptic_cavity_channel.tex` (`thm:h-exit-model`, `def:h-exit-renewal-channel`, `thm:arithmetic-metric`),
   `04m*`, `04n_graded_toys_network.tex`, `04o_graded_toys_exits.tex` (`obs:level-tower-correction`: for
   `Gamma_0(N)`, `N` squarefree, trivial character, every scattering entry is a rational function of `p^{-s}`
   times `xi(2s-1)/xi(2s)` and the `L`-ratios enter only for `Gamma_1(N)`; `asm:h-arith-gamma1` over `F_q[T]`;
   `prop:character-channel-graded-bond`; `conj:galois-graded-bond`), `04p_gl1_bond.tex`
   (`prop:cusps-are-class-group-bond`: cusps = `Pic`, H-CLASS = the scattering matrix is a group matrix
   block-diagonalised by the Fourier transform on the class group in `2 x 2` blocks on inverse pairs of
   characters), `04q_h_theta.tex`, `04r_h_theta_channels.tex` (`prop:siegel-constant-term`: the constant term of
   the level-one completed Eisenstein series is `(1/2)[Lambda(2s) y^s + Lambda(2s-1) y^{1-s}]`, two GL_1 theta
   channels exchanged by `F(t) -> t^{-1} F(1/t)`; the scattering coefficient `Lambda(2s-1)/Lambda(2s)`; Uetake's
   reduced causal factor; `thm:symbol-edge-quotient`), `09b_selberg_dictionary.tex`, `09c_selberg_tower_cusp.tex`.
3. `notes/h-theta/astra-proofs.md` (conventions, binding). Sources in `refs/src`: Uetake 2007
   (`refs/src/uetake-2007/`), Burnol; Huxley 1984 ("Scattering matrices for congruence subgroups") and Hejhal
   (Selberg trace formula II, Chapter 11) are NOT in the repo: state what you use from them precisely and mark
   "not byte-cited". Quote repo sources by file and line.

Be explicit. Classical theory (Eichler–Shimura, Manin–Drinfeld, Huxley's scattering matrices, Ihara's
lattice `SL_2(Z[1/p])` in `SL_2(R) x SL_2(Q_p)`) may be used if each input is stated precisely as a cited
theorem. A blind numerics lane will test every displayed formula (Dirichlet `L`-values with mpmath, small
levels `N = 5, 7, 11, 13`) and a hostile reviewer will try to refute every claim. Label every claim PROVED,
REFUTED, SHARPENED or OPEN. Keep a correction ledger for this brief. Do not pad.

## 0. Why this round

The cocompact LPS model has no cusp, hence no exit and no scattering matrix; the notebook's programme is
built on cusps as exits (the Riemann channel is the cusp of the modular surface; the cusps of a curve over
`F_q` are its class group, the GL_1 bond). The author of this brief (`claude:fable-5.1`) believes the
non-cocompact analogue of the LPS square complex is Ihara's quotient `Gamma[1/p] \ (H x T_{p+1})`, whose
horizontal (archimedean) cohomology is the `H^1` of the open modular curve, whose transverse transport is
`T_p`, and in which Deninger's package holds on the cuspidal part (Eichler–Shimura + Petersson) while the
Eisenstein classes are exactly (i) the radical of the cup pairing, (ii) the Bass-doubled "even poles" that
Proposition 9.3 excludes from positivity, and (iii) the notebook's exit sector, whose transfer function is the
level-`N` scattering matrix; and that this scattering matrix is, in the class-character basis, a diagonal
matrix of GL_1 theta-channel edge quotients (one per Dirichlet character), which settles the H-ARITH question
of shards 04o/04p over `Q`. Prove, refute or sharpen.

## 1. The Ihara square complex with a cusp

**D1 (structure and horizontal cohomology).** Let `p` be a prime not dividing `N`, `Gamma = Gamma_1(N)`,
`Gamma[1/p]` its `Z[1/p]`-points (or the corresponding subgroup of `SL_2(Z[1/p])`), acting on `H x T_{p+1}`
(Ihara: `SL_2(Z[1/p])` is a lattice in `SL_2(R) x SL_2(Q_p)`; state the theorem, not byte-cited). Prove:
(a) the quotient `Gamma[1/p] \ (H x T_{p+1})` is the "Hecke square complex": its horizontal slice is the open
modular curve `Y_1(N) = Gamma_1(N) \ H`, its vertical edges are the `p+1` branches of the Hecke correspondence
`T_p`, and its "squares" are the commutation of `T_p` with the horizontal identifications (the
`Gamma_0(p)`-level cover `Y_1(N) n Gamma_0(p)` is the edge space); (b) the horizontal (leafwise) cohomology is
`H^1(Y_1(N); R)`, which by Eichler–Shimura and Manin–Drinfeld splits `T_p`-equivariantly as
`S_2(Gamma_1(N)) (+) conj(S_2(Gamma_1(N))) (+) Eis`, with `dim Eis = (number of cusps of Gamma_1(N)) - 1` and
`T_p = p + 1` on `Eis` (for `p` prime to `N`; for the general Eisenstein eigenvalue with characters give the
formula `chi_1(p) + p chi_2(p)`); (c) the transverse transport (the square-induced map on horizontal edge
fields restricted to the horizontal cohomology, as in the LPS example) is `T_p`. Make (c) an honest theorem
with the exact combinatorial definition of the transport on `Y_1(N)`'s cochains (a triangulation or the de
Rham version with the pull-back/push-forward along the correspondence), or state it as the standard
description of `T_p` on `H^1` via the correspondence and mark what is definition and what is theorem.

**D2 (Deninger's package on the cuspidal part; the Eisenstein classes are the radical and the even poles).**
Prove: (a) with `A = T_p` on `H^1_cusp := S_2 (+) conj S_2` (as a real vector space) and `q = p`, the Bass doubling
`F = [[T_p, -p],[1, 0]]` is Frobenius at `p` on the etale `H^1` of `X_1(N)` (Eichler–Shimura relation), the
cup pairing of `X_1(N)` (Poincaré) is a `T_p`-similitude `Omega` with multiplier... (careful: on the single
copy `H^1` the cup product is `T_p`-*adjoint-symmetric*, `<T_p x, y> = <x, T_p^* y>` with `T_p^* = w T_p w`; say
exactly which of `Omega_B` (the Bass doubled pairing) and the Poincaré pairing satisfies `A^T Omega A = q Omega`
and how they are related; this is where Proposition 9.3's "Omega_B is not the face pairing" must be resolved
in the arithmetic case: the author expects the Poincaré pairing on `H^1(X_1(N))`, restricted to the
`Frob_p`-doubled eigenspaces, IS `Omega_B` up to the Eichler–Shimura normalisation); the Petersson metric is a
positive `G` with `F^T G F = p G`; Theorem 5.2 (iv) is `|alpha_p| = sqrt p`, the Ramanujan–Petersson bound,
which for weight two is Eichler–Shimura–Igusa (no Deligne). (b) On `Eis`, `T_p = p + 1 > 2 sqrt p`, so the Bass
companion has eigenvalues `1` and `p`, off the critical circle: by Proposition 9.3 no positive invariant metric
exists there; and `Eis` is exactly the radical of the cup pairing on `H^1(Y_1(N))` (the pairing
`H^1_c x H^1 -> H^2_c` degenerates on the image of the boundary; the Eisenstein classes are not compactly
supported): so in the Ihara square complex with cusps, **the radical of the face pairing = the Eisenstein
sector = the Bass-doubled even poles = the exit sector**. Prove this four-fold identity with precise
hypotheses (which `H^1`: of `Y`, of `X`, compactly supported, Borel–Moore; the mixed Hodge structure with
weights 1 and 2; the weight-2 part is `Eis`). (c) State what it means for the notebook: the Eisenstein classes
(the constant terms, one per cusp minus one) carry the exit; the cusp forms carry the odd, positive, critical
sector; the finite LPS model has no radical because it has no cusp; and the archimedean gamma factor and the
`T log T` zero count (absent in the finite model, as its author notes) enter through the continuous spectrum
attached to the same Eisenstein sector.

## 2. The level-N scattering matrix as a matrix of GL_1 theta-channel edge quotients (H-ARITH over Q)

**D3 (Huxley's structure, transcribed as edge quotients).** For `Gamma_1(N)` (equivalently `Gamma_0(N)` with all
nebentypus characters), the scattering matrix `Phi(s)` of the Eisenstein series at the cusps is, after the
Fourier transform on the "class group" of cusps (the cusps of `Gamma_1(N)` are indexed by pairs `(d, a)` with
`d | N`, `a in (Z/gcd(d, N/d))^x` up to the sign, i.e. by a finite abelian group extension; state the exact
parametrisation, Huxley 1984 not byte-cited), block-diagonal with blocks indexed by pairs of primitive
Dirichlet characters `(chi_1, chi_2)` with `chi_1 chi_2 = nebentypus`, and the entries are finite Euler
products at the primes dividing `N` times the ratio `Lambda(2s - 1, chi_1 conj(chi_2)) / Lambda(2s, chi_1 conj(chi_2))`
of completed Dirichlet `L`-functions (with the Gauss sum and the conductor power). Prove or transcribe precisely
(the notebook needs the *structure*: which characters, what the finite factors look like, what the
determinant is); at least give the complete statement for `N = ell` prime and trivial nebentypus
(`obs:level-tower-correction`: no `L`-ratios) and for `N = ell` prime with a nontrivial even character `chi`
mod `ell` (two cusps `0, infinity`; scattering matrix `2 x 2`; entries in terms of `Lambda(2s-1, chi)/Lambda(2s, chi)`
and `Lambda(2s-1, conj chi)/Lambda(2s, conj chi)` and the Gauss sum `tau(chi)`), fully explicit, with the
functional equation `Phi(s) Phi(1-s) = I` checked, and the residue at `s = 1`.

**D4 (the character channel is two twisted GL_1 theta channels; the twisted Siegel theta).** Generalise
`prop:siegel-constant-term` to a primitive character `chi` mod `N`: define the twisted Siegel theta
`Theta_{z, chi}(t) = sum_{(m,n)} chi(n) e^{-pi t |m z + n|^2 / y}`-type (choose the twist that makes the
Eisenstein series of character `chi` its Mellin transform: `E(z, s, chi)` with `chi` on the lower-left entry or
on the `n`; state the standard choice) and prove that its constant term in `x` is a sum of two GL_1 twisted theta
channels `theta_chi(t/y)`-type and `sqrt(y/t) theta_{conj chi}(t y)`-type (with the Gauss sum), exchanged by the
weighted involution `F(t) -> t^{-1} F(1/t)` composed with `chi -> conj(chi)` (Poisson for `theta_chi` is the
functional equation of `L(s, chi)`, with the Gauss sum and the parity of `chi`; even `chi` only for the weight-0
Eisenstein series; say what happens for odd `chi`), whose Mellin transforms are `Lambda(2s, chi) y^s` and
`(tau(chi)/sqrt N-type factor) Lambda(2s - 1, conj chi) y^{1-s}`; hence the `chi`-channel of the scattering
matrix is the ratio of the two edge transforms of the odd part of `theta_chi` (the analogue of
`thm:symbol-edge-quotient`, with `E_chi(tau) = xi(1 - 2 i tau, chi)`-type Hermite–Biehler and
`Theta_chi = E_chi^# / E_chi`... careful: for `chi != conj chi` the ratio is `E_{conj chi}^# / E_chi`, a ratio of
two different functions; work out whether the `chi`-channel symbol is inner and pure Blaschke (zeros of
`L(s, chi)` in the strip, with the functional equation pairing `chi` with `conj chi`, so the model space pairs
the `chi` and `conj chi` channels: `prop:cusps-are-class-group-bond`(a)'s `2 x 2` blocks). Test numerically for
`N = 5`, `chi` the character of order 4 (odd) or order 2 (even, `chi = (./5)`), and `N = 7, 13` with an even
character: give the numerics lane the formulas and expected values at two points.

**D5 (the level-N Riemann channel is a direct sum of character channels with one exit each).** With D3–D4 and
the notebook's `h`-exit model (`thm:h-exit-model`: `Theta = eta S B_bd`, `K = H^2(C^h) (-) Theta H^2(C^h)`, `Z`,
exit map `J` with `I - Z^* Z = J^* J`, rank `J <= h`), prove: the model space of the level-`N` cusp cavity is
`K_N = (+)_{chi} K_{Theta_chi}` (one scalar or `2 x 2`-block channel per character, the `2 x 2` blocks for
`chi != conj chi` being the inverse-pair blocks), the exit map has rank exactly `h = number of cusps` (one exit
per class character, NOT one per zero mode: `prop:kernels-not-riesz`'s lesson at level `N`), the modes of the
`chi`-channel are the jets of the zeros of `L(s, chi)` cut to the outgoing half and damped by `y^{-1/4}`
(as in `thm:model-space-jets`), the diamond operators act on the `chi`-channel by `chi` (so
`asm:h-arith-gamma1` holds over `Q` with the finite factors of D3), and the graded divisor of the level-`N`
channel is the union over `chi` of the zero sets of `L(s, chi)` (with the even sector = the poles, which occur
only for `chi = 1`, i.e. only the trivial character channel has an even sector: the Eisenstein classes of D2
with `T_p = p + 1` versus `chi_1(p) + p chi_2(p)`; reconcile). Then the Deninger reading: on the level-`N`
channel the functional-equation pairing `Omega` pairs the `chi`-channel with the `conj chi`-channel (the
`2 x 2` blocks of `prop:cusps-are-class-group-bond`), a positive compatible metric on the spectral side exists
iff GRH for all `chi` mod `N` with simple zeros (transcribe the finite criterion, Theorem 5.2 (iv)), and, as in
the level-one case, no bounded such metric exists on `K_N` (Riesz failure; state and prove or cite the
level-one argument from the sibling lane's claim, marked as such: "`prop:kernels-not-riesz` generalises to
`L(s, chi)` because the zero density is again `T log T`").

## 3. Consequences

**D6.** One structured page: what D1–D5 change in the notebook's programme. In particular: (a) H-ARITH
(`obs:graded-toys-next`, `asm:h-arith-gamma1`, `conj:galois-graded-bond`) over `Q`: settled or not, and what
remains over `F_q[T]` (the function-field version of D3–D4 for `Gamma_1(N) < GL_2(F_q[T])`, `N` a cubic:
which parts transfer verbatim, which need the `infinity`-factor); (b) the cusp count `h` and the exit rank
against the finite cavities of 04k/04l (there `h` rays, `det S = (-1)^h p / ptilde`); (c) the relation between
the LPS cocompact model (no radical, no exit, positivity on everything) and the cusp model (radical = exit):
Deninger's `H^1` for `Spec Z` "has a cusp" (the archimedean place; the poles of `xi`) — say in two sentences
whether the notebook should read the pole sector of `xi` as the Eisenstein radical of an arithmetic square
complex, marked as observation.

## 4. Output format

`notes/deninger-cusp/astra-proofs.md` with: a ledger table (D1–D6, verdicts); full proofs with hierarchical
steps where long; every external theorem stated precisely with author and year, marked "not byte-cited";
repo sources quoted by file and line; a section "Numerical checks for the blind lane" (explicit: the `2 x 2`
scattering matrix for `N = 5` with the order-2 and order-4 characters at `s = 0.7 + 0.3 i` and its functional
equation; the twisted theta constant term at `y = 1.3, t = 0.7`; the residue at `s = 1`; the modes of the
`chi`-channel at the first two zeros of `L(s, chi)` for `chi = (./5)`; the Eisenstein `T_p` eigenvalue on `Eis`
for `N = 11, p = 2, 3`); a section "Corrections to the brief"; and a closing "What this changes in the notebook"
with, per claim, the status to register and the one-sentence statement.

## 6. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/deninger-cusp/progress.txt` with the
claim you are working on, updated whenever you move to the next claim.
