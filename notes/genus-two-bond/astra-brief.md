# Brief for the prover: the class-group bond at genus two. The class-field cover as the bond's H^1, the Frobenius channel in blocks indexed by class characters, the Rosati (Hodge) metric against the symmetric ray: the first non-vacuous metric test; and the two GL_1 cusps folded by the automorphism

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/genus-two-bond/astra-proofs.md` (create
it; overwrite if present) and, if you want scratch computations, python files under
`notes/genus-two-bond/checks/`. Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy,
scipy is installed (no PARI; point counts over `F_5`, `F_25`, `F_125`, `F_625` by brute force in python are
fine and expected). Read first:

1. `report/sections/04p_gl1_bond.tex` (the class-group bond `l^2(Pic^0) (x) l^2(Z)` with the degree shift;
   `prop:class-group-bond`: `Z(T) = sum a_n T^n`, `a_n = sum_{Pic^n} (q^{h^0(D)} - 1)/(q - 1)`, special degrees
   `n <= 2g - 2` carry `P(T)`, `h = P(1)`; `prop:theta-functional-bond-state`; `prop:cusps-are-class-group-bond`:
   cusps = `Pic^0`, class characters `chi`, `L(T, chi)` of degree `2g - 2` for `chi != 1`; `obs:gl1-bond-no-metric`:
   at genus one the metric question is vacuous, "the first genuine test is genus two"; `num:gl1-bond`),
   `notes/gl1-bond/proofs.md`, `scripts/gl1_bond.py`.
2. `report/sections/06f_ring_norm_genus_two.tex` (genus two in the ring-norm campaign: the curve
   `C: y^2 = x^5 + x^3 + x^2 - 2` over `F_5`, `chi_F = z^4 - 3z^3 + 7z^2 - 15z + 25`; `cit:rosati-positive`,
   `cit:cm-lift-frobenius`, `asm:cm-hodge-type`, `asm:cm-polarised-lift`; `thm:rosati-ph-genus-two`: the Rosati
   involution is complex conjugation at every CM place, `q^{-1/2} pi^*` is unitary on `H^{1,0}` and on
   `H^1(J~, C)` with their Hodge metrics, "the PH models agree up to positive weights and the CM type";
   `prop:cm-type-gauge`; `obs:phantasm-bond-candidate`), `notes/ring-norm-tensor/astra-proofs.md` (your
   predecessor's ledger on that round).
3. `report/sections/04l_elliptic_cavity_channel.tex` (`thm:arithmetic-metric`: on `K_HW` of D2 the cone of
   metrics with `Z^* H Z = r^2 H` is diagonal in the eigenbasis, parity and the real structure leave a
   single ray, the symmetric ray; the Lax–Phillips energy metric is outside the cone),
   `report/sections/04o_graded_toys_exits.tex` (`thm:frobenius-channel-expander`: `Z' = rU`, one exit per
   mode, `U^2 ~ (Frob/sqrt q) (x) 1_2`, all relaxation moduli `q^{-1/2}`), `report/sections/04k_elliptic_cavity_scattering.tex`
   (the D2, D3 curves and H-CLASS).
4. Sources under `refs/src` for function-field class field theory if present (search for `lorscheid`,
   `apw`, `takahashi`); otherwise state the standard facts (Artin reciprocity for function fields, the
   Hilbert class field of a curve with a rational point, Weil's `L(T, chi)` for unramified class characters)
   precisely, marked "not byte-cited".

Be explicit and computational: every group, character and polynomial below is finite and must be displayed.
A numerics lane will recompute everything from the curve equation, and a hostile reviewer will try to refute
every claim. Label every claim PROVED, REFUTED, SHARPENED or OPEN. Keep a correction ledger for this brief.
Do not pad.

## 0. Why this round

At genus one the class-group bond fixes the Frobenius roots by `h` alone and every Frobenius-normal metric
is the same ray (`obs:gl1-bond-no-metric`). Genus two is the first case where (i) the special degrees carry a
non-trivial `P(T)`, (ii) the class characters carry `L`-functions with zeros of their own, (iii) the
Frobenius-normal metrics on `H^1 (x) C` form a cone with a free ratio, and (iv) the Rosati (Hodge) metric of a
polarised CM lift is a *specific* point of that cone. The author of this brief (`claude:fable-5.1`) wants the
test done on the concrete curve of shard 06f. A sibling lane today tests the same question at "genus 721" on
the LPS square complex (Petersson versus the symmetric ray); this lane is the function-field twin.

## 1. The class-group bond of `C: y^2 = x^5 + x^3 + x^2 - 2` over `F_5`

**E1 (the finite data).** Compute and display: `N_1, N_2, N_3, N_4` (points over `F_{5^k}`, with the point(s)
at infinity of the smooth model: `deg 5` model has one rational point at infinity; check), `P(T)` from the
counts and confirm `chi_F = z^4 - 3z^3 + 7z^2 - 15z + 25` of shard 06f (so `P(T) = 1 - 3T + 7T^2 - 15T^3 + 25T^4`);
`h = P(1) = 15 = #Pic^0(F_5)`; the group structure of `Pic^0(F_5)` (cyclic of order 15 or `Z/3 x Z/5`, the same
group; exhibit a generator as a divisor class); the effective divisor classes of degrees `0, 1, 2 = 2g - 2` with
their `h^0` (the theta divisor: which classes of degree `g - 1 = 1` are effective; how many of the 15 classes in
each degree are effective and with what `h^0`); `a_0, a_1, a_2` from `prop:class-group-bond`(a) and the check
that `Z(T) = P(T)/((1-T)(1-5T))` reproduces them and that `a_n` for `n >= 3` is the Perron pair
`h(5^{n-1} - 1)/4`. Choose a rational point `P_0` of degree one and fix the identification `Pic^n = Pic^0` by it.

**E2 (the class characters and their `L`-functions).** For each of the 14 nontrivial characters `chi` of
`Pic^0(F_5)` (extended by `chi(P_0) = 1`), compute `L(T, chi) = sum_{[D]} chi([D]) (5^{h^0(D)} - 1)/4 T^{deg D}`
as in `prop:cusps-are-class-group-bond`(b): a polynomial of degree `2g - 2 = 2`; display all 14, their two
roots, check `|root|^{-1} = sqrt 5` (Weil for the class-field cover) and the functional equation
`L(T, chi) = chi-dependent-constant * 5 T^2 L(1/(5T), conj chi)`. Prove: the maximal unramified abelian cover
`C'` of `C` in which `P_0` splits completely has Galois group `Pic^0(F_5)` (Artin reciprocity, not byte-cited),
genus `g' = 1 + 15(g - 1) = 16`, and `P_{C'}(T) = P(T) prod_{chi != 1} L(T, chi)` (degree `4 + 14 * 2 = 32 = 2g'`).
So: **the class-group bond's Fourier decomposition is the character decomposition of `H^1(C')`**, the
trivial character carrying `H^1(C)`. State this as a theorem with the exact hypotheses (a rational point;
`chi` unramified; the sign/constant in the functional equation).

## 2. The Frobenius channel on the class-group bond and the metric test

**E3 (the Frobenius channel in blocks).** With `thm:frobenius-channel-expander`'s model (`Z' = rU`, one exit per
mode, `r = q^{-1/4}`), the Frobenius channel of the bond is `U = Frob/sqrt 5` on `H^1(C') (x) C`, block-diagonal
over the characters: the trivial block `H^1(C)` (4 modes, the roots of `P`), and 14 blocks of 2 modes (the
roots of `L(T, chi)`), each block unitary in *some* metric iff its roots have modulus `sqrt 5` (Weil). Prove
that the cone of Frobenius-normal metrics on `H^1(C) (x) C` (metrics `H` with `U^* H U = H` in the sense of
`thm:arithmetic-metric`, `Z^* H Z = r^2 H`) is, for distinct roots (check they are distinct for this curve),
the diagonal positive weights `(h_1, h_1', h_2, h_2')` in the eigenbasis of `Frob`, with the real structure
(`Frob` is real on `H^1(C, Q_l)` or on `H^1` of a lift) forcing `h_j = h_j'` on conjugate pairs: two free
scalars, one modulo scale. Same for each `chi`-block with the pair `(chi, conj chi)` (the real structure
pairs the `chi` block with the `conj chi` block: say exactly what "real" means there).

**E4 (the Rosati metric is a specific point; the symmetric ray is another; are they the same?).** Under
`asm:cm-hodge-type` and `asm:cm-polarised-lift` (shard 06f), take the CM field `K = Q(pi)` (quartic CM field:
compute it from `chi_F`; its real quadratic subfield; whether `O_K`-maximal-order questions matter), the CM
type `Phi = {phi_1, phi_2}` selected by the lift, and the principal polarisation. Prove: the Hodge metric on
`H^1(J~, C) = C^{Phi} (+) C^{conj Phi}` in the `pi`-eigenbasis is `diag(c_1, c_2, c_1, c_2)` with
`c_j = c(phi_j) > 0` determined by the polarisation `E(x, y) = Tr_{K/Q}(xi x conj(y))` with `xi in K` totally
imaginary (`phi_j(xi)` purely imaginary with a sign fixed by the CM type), i.e. `c_j = |phi_j(xi)|` up to a
common factor, once the eigenvectors are normalised by the lattice (the CM ideal class of the canonical lift).
Then the **test**: is `c_1 = c_2` in the normalisation in which the symmetric ray of `thm:arithmetic-metric`
is defined? Since the class-group bond has no cavity exit, propose the canonical normalisation from the bond
itself: the components of the theta bond state `Omega_theta = sum_D q^{h^0(D)} |D>` (or of its special-degree
part) along the Frobenius eigenvectors, or the Gauss-sum/`L`-value normalisation of the character blocks
(`L(T, chi)` at `T = 1` or at `T = q^{-1/2}`). Work out at least one canonical normalisation and compute the
ratio `c_1/c_2` (or the analogous ratio of the Rosati weights in it) as an exact algebraic number in `K` (or
its real subfield); if it is `1`, the symmetric ray IS the Hodge metric at genus two for this curve; if not,
display the number and say what it measures. If the CM lift's ideal class cannot be pinned down by pure
thought, say exactly which finite computation (in `K`) would pin it and give the two candidate answers. Do
not assume `asm:weil-curves`; if you need Weil's theorem for the curve (roots of modulus `sqrt 5`) it is
verified numerically in E1 and E2 for this curve.

**E5 (the exit).** For the Frobenius channel on the trivial block with the one-exit-per-mode model
(`J' = sqrt(1 - r^2) 1`), the exit is not arithmetic. The bond has one distinguished vector, the theta
bond state, and one distinguished direction, the degree shift. Prove or refute: the degree shift on
`l^2(Pic^0) (x) l^2(Z)` compressed to the special degrees `n <= 2g - 2` and cut at `n > 2g - 2` (the Perron
tail as the "outgoing half") is a finite contraction whose characteristic function has `P(T)` (or its
reciprocal) as determinant, i.e. the class-group bond's own cut realises `H^1` as a model space with a single
exit (the degree shift into the Perron tail), in the spirit of `thm:h-exit-model`, and whether its modal Gram
matrix (in the `l^2(Pic^0)` metric, which IS canonical) is Frobenius-normal, i.e. whether the *bond metric*
`l^2(Pic^0)` itself induces a point of the cone of E3, and which point (compare with E4). This is the genus-two
version of the D2/D3 hedgehog with the cusps as the class group (`prop:cusps-are-class-group-bond`), computed
on the bond alone. If the cut is not a contraction, say why and what the correct object is.

## 3. The two GL_1 cusps (ideation, marked as such; one page at most)

**E6.** The GL_1 bond `L^2(R_+^x)` has two ends `y -> 0` and `y -> infinity`, exchanged by the Poisson
automorphism `y -> 1/y`; the modular surface has one cusp, whose Eisenstein constant term is the pair of GL_1
theta channels (`prop:siegel-constant-term`, 04r), exchanged by the weighted involution. At genus two over
`F_q` the same folding is the pair `(chi, conj chi)` of class characters versus the single cusp per class. Say
whether "the automorphism folds the two GL_1 cusps into the one GL_2 cusp" is a theorem the notebook already
has (name the claim) or an open identification, and what the function-field version at genus two adds (the
`2 x 2` blocks of H-CLASS on inverse character pairs as the fold). Mark speculation.

## 4. Output format

`notes/genus-two-bond/astra-proofs.md` with: a ledger table (E1–E6, verdicts); full proofs with hierarchical
steps where long; every external theorem stated precisely with author and year, marked "not byte-cited";
repo sources quoted by file and line; a section "Numerical checks for the blind lane" (explicit: the point
counts; `Pic^0` structure and a generator; the 14 `L(T, chi)`; the `pi`-eigenbasis and the Rosati weights
`c_1, c_2` with the normalisation; the modal Gram of E5); a section "Corrections to the brief"; and a closing
"What this changes in the notebook" with, per claim, the status to register and the one-sentence statement.

## 5. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/genus-two-bond/progress.txt` with
the claim you are working on, updated whenever you move to the next claim.
