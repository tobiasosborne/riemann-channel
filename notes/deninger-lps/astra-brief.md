# Brief for the prover: the LPS square complex (13, 17; level 5) as a Deninger finite model. Horizontal cohomology is the H^1 of the 13-graph, the transverse transport is the Hecke operator T_17, the Bass doubling is Frobenius at 17, the positive pairing is Petersson (Eichler–Shimura + Jacquet–Langlands); the same object as the notebook's graded Weil–LPS channel

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/deninger-lps/astra-proofs.md` (create it;
overwrite if present) and, if you want scratch computations, python files under `notes/deninger-lps/checks/`.
Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy, scipy is installed. Read first:

1. `notes/deninger-lps/src/lps-deninger-worked-example.md`: an explicit finite model (produced in a separate
   Codex conversation on Deninger's programme; its data files are NOT in this repo, only the text). Vertex
   set `PGL_2(F_5)` (120), horizontal generators `S_13` (14), vertical generators `S_17` (18), 840 + 1080
   edges, 7560 squares from the 252 reordering rules `ab = +-b'a'`; total Betti numbers `(1, 0, 5759)`;
   horizontal cohomology `K = ker D^t` of dimension 721; transverse transport `T_1` on horizontal edge fields
   through the squares, `T_1 D = D T_0` with `T_0 = A_17`; `chi_T = chi_{T_1}(x)(x - 18)/chi_{A_17}(x)`, fully
   factored in its Section 13 (eigenvalues `+-7, -1, +-3, 4, 5, +-6, 2, -2, ...` with multiplicities `4, 4, 8,
   ...`); certified `||T|| < 8 < 2 sqrt(17)`; Bass doubling `F_1 = [[T, -17 I],[I, 0]]` on `K (+) K`, pairing
   `Omega`, metric `G = [[I, -T/2],[-T/2, 17 I]] > 0`, quarter-turn `J`, the suspension Hamiltonian, the graded
   Euler product with the `(1-u^2)^{5760}` correction.
2. `notes/deninger-lps/src/manuscript.txt` (same conversation's general note, text of the PDF/TeX beside it):
   Definition 5.1, Theorem 5.2 (an invariant positive polarization exists iff the normalised dynamics is
   semisimple with unit-modulus spectrum; the certificate `A^T G A = q G`), Proposition 5.3, Definition 6.1 and
   Theorem 6.2 (the Deninger-type finite package), Theorem 7.1 (conformal torus maps `q = a^2 + b^2`),
   Theorem 8.1 (reciprocal bouquets on two tori), Section 9 (obstructions), Proposition 9.3 (Bass doubling:
   positivity iff `||T|| < 2 sqrt q`; `Omega_B` is not the face pairing), Section 10 ("the specific LPS
   face-to-pairing construction remains open in this work"; the total `H^1 = 0` versus horizontal 721).
3. The notebook's own LPS work: `notes/weil-lps-channels.md` and `scripts/weil_lps.py`,
   `scripts/weil_lps_hashimoto.py` (Weil-representation channels on `l^2(F_p)` with LPS generators of norm
   `q`; for `(p; q) = (13; 17)` the odd-block edge superoperator on `M_6 (x) C^18`), `notes/ramanujan-graded/`
   and `report/sections/02h_definitions_graded_ramanujan.tex` (`def:graded-transfer-channel`,
   `def:graded-hashimoto`, `def:index-two-grading`), `report/sections/05*` (graded Ramanujan shards: search
   `thm:graded-harrow`, `thm:graded-qihara-bass`, `cor:graded-band-circle`), `report/sections/04l_elliptic_cavity_channel.tex`
   (`thm:arithmetic-metric`: the cone of `q^{-1/4} Z`-unitary metrics and its symmetric ray),
   `report/sections/04p_gl1_bond.tex` (`obs:gl1-bond-no-metric`: at genus one the metric question is vacuous;
   "the first genuine test is genus two"), `report/sections/08c_weil_positivity_continuous.tex`
   (`obs:kraus-dichotomy`), `notes/deligne-via-graphs.md`.

Be explicit and elementary where possible, but this lane is allowed to use the standard theory of
automorphic forms on definite quaternion algebras, strong approximation, the Jacquet–Langlands correspondence
and Eichler–Shimura, as long as every such input is stated precisely as a cited theorem (author, year, and
the exact statement used; the sources are not in `refs/src`, so mark them "not byte-cited"). A blind numerics
lane will test every finite statement (it can rebuild the complex from the quaternion sets in the worked
example) and a hostile reviewer will try to refute every claim. Label every claim PROVED, REFUTED, SHARPENED
or OPEN. Keep a correction ledger for this brief. Do not pad.

## 0. Why this round

The worked example realises Deninger's finite package (odd spectrum on the critical circle, even poles,
functional equation, positive pairing, compatible star, self-adjoint Hamiltonian, trace formula) but its own
author left open "the face-derived identification" of the pairing and did not say *what* the 721-dimensional
space and the operator `T` are. The author of this brief (`claude:fable-5.1`) believes they are classical
objects, and that naming them (i) supplies the missing identification arithmetically, (ii) shows the
positivity certificate is exactly the Ramanujan–Petersson bound (Eichler–Shimura for weight two), (iii)
identifies the finite model with the notebook's own graded Weil–LPS channel for the same primes, and (iv) makes
the metric question of `obs:gl1-bond-no-metric` non-vacuous at "genus" 721. Prove, refute or sharpen the
following.

## 1. The complex

**B1 (structure).** The complex `X` of the worked example is the Cayley 2-complex of `PGL_2(F_5)` with respect
to `S_13 u S_17` and the 252 Mozes relations. Prove: `X = Gamma(5) \ (T_14 x T_18)` where `Gamma < PGL_2(Q)`
(equivalently the unit group of the Hamilton quaternions over `Z[1/221]` modulo centre, `13 = 17 = 1 mod 4`) is
the lattice acting simply transitively on the vertices of the product of the two trees (Mozes 1995; Rattaggi
2004, `arXiv:math/0411547`; Burger–Mozes), and `Gamma(5)` is the kernel of reduction modulo 5 (both 13 and 17
are nonsquares mod 5, hence the image is `PGL_2(F_5)` and both colour graphs are bipartite). Identify the
7560 squares with the `Gamma(5)`-orbits of the squares of `T_14 x T_18` (one square per `(a, b)`, four
representatives). Say what the quotient of the *full* product by the *full* lattice `Gamma` is (one vertex,
`7 + 9` loops, 63 squares: the standard presentation) and why the total `H^1(X; Q) = 0` (Garland-type
vanishing for cocompact lattices in products of trees, or a direct argument; the worked example only proves
`b_1 = 0` by a rank computation).

**B2 (horizontal cohomology is the first homology of the 13-graph).** `K = ker D^t` (721-dimensional
antisymmetric horizontal edge fields orthogonal to gradients) is `H_1(X^{13,5}; R)` of the LPS graph
`X^{13,5} = Gamma(5) \ T_14` (`b_1 = 840 - 120 + 1 = 721`), i.e. the horizontal cohomology of the square
complex is the ordinary first cohomology of one colour graph. Prove it and identify the transverse transport:
`T_1` (defined by "compare a horizontal edge with its opposite edge in each incident square, signs retained")
restricted to `K` is the Hecke operator `T_17` acting on `H^1(X^{13,5})` through the correspondence
`X^{13,5} <- Gamma(5) n Gamma_17-stuff -> X^{13,5}` induced by the vertical edges. Make this precise: for
`f` a function on directed horizontal edges, `(T_1 f)(g, a) = sum_{b in S_17} f(g phi(b'), a')` with
`ab = +- b' a'`, and `T_17` on the tree quotient is the sum over the 18 neighbours in the 17-direction of
the *transported* edge; the transport is well defined because the square relation is the commutation of the
two Hecke correspondences on the product of trees. State it as: the squares are the Hecke commutation
`T_13 T_17 = T_17 T_13`, lifted to edges.

**B3 (the spectrum of `T` is a Hecke polynomial at 17).** Prove: in adelic terms, functions on
`PGL_2(F_5)` are automorphic forms on the definite quaternion algebra `B` ramified at `{2, infinity}` (the
Hamilton quaternions) of level `K(5)` (principal congruence at 5, maximal elsewhere), by strong
approximation and class number one of the maximal order; `A_13 = T_13`, `A_17 = T_17`. Functions on directed
horizontal edges are forms of Iwahori level at 13; the old part (image of the two degeneracy maps from vertex
functions) has dimension `2 * 120 - 2 = 238` (the two-dimensional kernel spanned by the constants and the
bipartite sign, i.e. the two one-dimensional automorphic representations), the new part has dimension
`1680 - 238 = 1442 = 2 * 721`, and the edge-reversal involution splits it into `K (+) K'`, each 721-dimensional,
with `T_17` acting the same way on both (the reversal commutes with `T_17`). The eigenvalues of `T = T_1|_K`
are therefore the Hecke eigenvalues `a_17(pi)` of the automorphic representations `pi` of `B^x` with `pi_13`
special (Steinberg twisted by an unramified character) and `pi_5^{K(5)} != 0`, each with multiplicity
`dim pi_5^{K(5)}` (times the multiplicity of `pi` in the discrete spectrum, which is one). By
Jacquet–Langlands these are the weight-two newforms on `GL_2/Q` whose local components are discrete series at
2 and special at 13 with the level-5 condition; `|a_17| <= 2 sqrt 17` is Eichler–Shimura–Igusa (weight two
needs no Deligne). Check the worked example's factorisation against this: which eigenvalues in Section 13
are integers (rational newforms, e.g. elliptic curves of conductor `2^e * 13 * 5^2`-type over Q with split
multiplicative reduction at 13; `a_17 in {+-7, -1, +-3, 4, 5, +-6, +-2, 3}` are all of the form `17 + 1 - #E(F_17)`
for some curve `E/F_17`) and whether the multiplicities `4, 8, 6, 12, 15, 18, 17, 20, 44, 77, ...` are
consistent with sums of `dim pi_5^{K(5)}` (the dimensions of irreducible representations of `PGL_2(F_5)`
are `1, 1, 4, 4, 5, 5, 6, 6` and `GL_2(F_5)/centre`-representations appear in the regular representation
with multiplicity equal to their dimension). You need not identify each newform; give the structural
theorem and one or two verified instances (e.g. the eigenvalue `-7` or `7`, or the multiplicity-77 eigenvalue
`-2`, which must be `a_17` of a newform or several newforms whose level-5 local representation has
`K(5)`-fixed space of the stated total dimension; a consistency count over all 721 is sufficient:
`sum_a m_a = 721`).

**B4 (the Deninger package is Eichler–Shimura + Petersson).** Prove: (a) on each `a_17`-eigenline of `K`, the
Bass companion `F_1` has the two eigenvalues `alpha, beta` with `alpha + beta = a_17`, `alpha beta = 17`, the
Satake parameters at 17 of `pi` (equivalently the eigenvalues of Frobenius at 17 on the two-dimensional
Galois representation attached to the newform); so `(K (+) K, F_1) = (+)_pi V_pi (Frob_17) (x) (multiplicity)`
as a linear dynamical system, i.e. the Bass doubling of the horizontal cohomology is the etale `H^1` of the
corresponding modular curve (the 13-new, discrete-series-at-2 part, at level 5), with Frobenius at 17.
(b) The pairing `Omega_B` on `K (+) K` corresponds to the Poincaré (cup) pairing on that `H^1`, and the
metric `G` to the Hodge (Petersson) metric, up to the per-eigenform scalings of (c). Hence the "face-derived
identification" that the general note leaves open is supplied by the modular curve of the Jacquet–Langlands
correspondent, not by the squares of `X`: the surface whose cup product is `Omega` is archimedean (the
modular curve), and the total `H^1(X) = 0` is the reason the squares cannot supply it. State this as a theorem
with the exact hypotheses, or refute it. (c) `thm:arithmetic-metric` at "genus 721": the cone of positive
metrics `H` on `K (+) K (x) C` with `F_1^* H F_1 = 17 H` is diagonal in the `F_1`-eigenbasis; the real structure
(complex conjugation on `K (+) K`) forces the weights of `alpha` and `conj(alpha) = beta` to be equal; so the
cone has one free positive scalar per eigenform (per distinct `a_17` and per copy), and both `G` (the worked
example's) and the Petersson metric are points of it; compute the ratio `G / Petersson` per eigenform if you
can (it is a normalisation of the Eichler–Shimura map; if the ratio is constant across eigenforms, say so
and prove it; if it is `<f, f>_Petersson`-dependent, say so). This is the first non-vacuous instance of the
"symmetric ray is the Hodge metric" question of `obs:gl1-bond-no-metric`: settle whether the symmetric ray
(all weights equal in the exit normalisation of `thm:arithmetic-metric`) coincides with Petersson.

## 2. The same object as the notebook's graded Weil–LPS channel

**B5.** The notebook's `(p; q) = (13; 17)` channel is `Phi(rho) = (1/18) sum_{alpha in S_17} W(g_alpha) rho W(g_alpha)^*`
with `W` the Weil representation of `SL_2(F_13)` on `l^2(F_13)`, split into even and odd blocks `M_7`, `M_6`, and
its Hashimoto (non-backtracking) edge superoperator on `M_6 (x) C^18` (`scripts/weil_lps_hashimoto.py`). Prove the
dictionary: (a) `Phi` is the Hecke operator `T_17` acting on `End(pi_13^{+-})`-isotypic vectors of the space of
automorphic forms on the same quaternion algebra `B` at level `K(13)` (principal congruence at 13) — i.e. the
notebook's channel is the level-13 counterpart, and the worked example's `T` the level-5 counterpart, of the same
Hecke operator at 17; both spectra are `a_17` of newforms for `B^x`, selected by different local conditions at
the level prime (Weil-representation isotypic at 13 versus `K(5)`-fixed at 5 with Steinberg at 13). (b) The
notebook's Harrow containment ("every channel eigenvalue times `q + 1` lies in the Cayley spectrum") and the
worked example's `chi_T | chi_{T_1}` are the same statement (old/new decomposition). (c) The graded quantum
Ihara zeta of the notebook (`thm:graded-qihara-bass`, `cor:graded-band-circle`) and the worked example's
`Z(u) = det_K(I - uT + 17u^2)/((1-u)(1-17u))` are both Bass doublings of `T_17` on a "13-new" space, hence
products of local Hecke polynomials `1 - a_17(pi) u + 17 u^2` over the selected `pi`, and their "Ramanujan
property" is the same Eichler–Shimura statement. State the exact relation (which `pi` appear in each, with
multiplicities), and whether either zeta *is* a factor of the other after a change of level. If the Weil
representation at 13 selects precisely the Steinberg-at-13 forms (the odd Weil representation of
`SL_2(F_13)` restricted from the special representation of `GL_2(Q_13)`, or the cuspidal ones: decide), say so.

**B6 (is the finite model a graded transfer channel?).** In `def:graded-transfer-channel` a graded transfer
channel is a Kraus family with a parity; its graded divisor gives zeros (odd) and poles (even). The worked
example's model is a linear dynamical system `F_0 = 1, F_1, F_2 = 17` on `R (+) (K (+) K) (+) R`, not a Kraus
family. Prove or refute: there is a graded transfer channel (a completely positive map on a graded matrix
algebra with homogeneous Kraus operators) whose sector restrictions have `Tr E_0^n - Tr E_1^n = N_n :=
1 + 17^n - Tr F_1^n` for all `n`; if yes, construct it (the natural candidate: the classical Markov transfer
on directed 17-edges with the sign transport, i.e. the signed non-backtracking operator `B_e` of the worked
example's Section 8 as a permutation-type Kraus family, plus the vertex walk `B_v`, with the `(1-u^2)^{5760}`
correction as a designated trivial divisor); if no, say exactly which axiom fails (the "graded CP transfer
versus graded spectral transfer" distinction of `notes/ramanujan-graded`). Either way, say whether the
notebook's Weil–LPS channel (which IS a Kraus family) realises the level-13 counterpart as a genuine graded
CP transfer, so that the Deninger finite package has a quantum-channel instance with the positivity
certificate `G` given by the Hilbert–Schmidt metric (Harrow: the channel is self-adjoint, so the metric is
free; check whether that is the symmetric ray).

## 3. Consequences for the notebook's programme

**B7.** Write, as a short structured section, what the identification changes: (a) "positivity of the
companion metric is precisely the Ramanujan constraint" (worked example, Section 9; Proposition 9.3) becomes
"Deninger's positive Hodge structure on the finite model is the Petersson metric on the modular curve, and
its existence is Eichler–Shimura + Igusa/Deligne"; the finite model does not produce positivity from the
squares, it inherits it from an archimedean surface; (b) what is the analogue for the notebook's arithmetic
targets (the GL_1 bond of shard 04p, the Riemann channel `K_S` of 04q/04r) of the pair (13-graph, T_17): the
author's guess is (the dilation direction `R_+^x`, the Hecke/Frobenius at one prime `p` acting on the model
space) with the squares being the commutation of the dilations by `log p` and `log q`; say whether Deninger's
"foliated space" for `Spec Z` is the `GL_1` version of this square complex (the two-prime solenoid
`R_+^x / p^Z q^Z`), and what replaces the finite-dimensionality that made everything work here. Two paragraphs
at most; mark speculation as such.

## 4. Output format

`notes/deninger-lps/astra-proofs.md` with: a ledger table (B1–B7, verdicts); full proofs with hierarchical steps
where long; every external theorem stated precisely with author and year, marked "not byte-cited"; a section
"Numerical checks for the blind lane" (explicit finite statements the numerics lane can verify after rebuilding
the complex from the quaternion sets: dimensions, the old/new split, `T_1 D = D T_0`, that `T_1` commutes with the
edge reversal, the eigenvalue multiplicities against the representation dimensions of `PGL_2(F_5)`, the ratio
`G / Petersson` if computable from a finite formula, the Hecke relation `T_17^2 - 17 = T_{17^2}` on `K`); a
section "Corrections to the brief"; and a closing "What this changes in the notebook" with, per claim, the
status to register and the one-sentence statement.

## 6. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/deninger-lps/progress.txt` with the
claim you are working on, updated whenever you move to the next claim.
