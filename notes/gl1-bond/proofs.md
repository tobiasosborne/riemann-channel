# Proofs: the class-group bond, the theta functional as bond state, the cusps as the GL_1 bond

Author: `claude:fable-5.1`. Brief: `notes/gl1-bond/brief.md` (B1--B5). Numerics lane (blind):
`notes/gl1-bond/numerics.md`, `scripts/gl1_bond.py`. Review: `notes/reviews/gl1-bond-2026-09-21.md`.
Conventions as in the brief. Standard facts are named with a source; the repository holds TeX sources
for none of Rosen, Weil, Serre or Tate, so every citation below is "not byte-cited". The value of the
round is the identification with the notebook's objects, not the theorems.

## B1. The class-group bond

**Proposition B1.** Let `K` be the function field of a smooth projective curve `C/F_q` of genus `g` with a
rational point `P_0`.
(a) `Z(T) = sum_{D >= 0} T^{deg D} = sum_n a_n T^n` with `a_n = sum_{[D] in Pic^n} (q^{h^0(D)} - 1)/(q - 1)`.
(b) For `n > 2g - 2`, `a_n = h (q^{n+1-g} - 1)/(q - 1)`, `h = |Pic^0(F_q)|`.
(c) `a_0 = 1`, and for `g = 1`, `Z(T) = 1 + hT/((1-T)(1-qT))`, `P(T) = 1 - (q+1-h)T + qT^2`, `h = P(1) = N_1`.
(d) In general `h = P(1)`.

*Proof.* (a) The effective divisors linearly equivalent to `D` are the divisors `div(f) + D` with
`f in L(D) \ {0}`, and `f, f'` give the same divisor iff `f' = c f`, `c in F_q^x`; so their number is
`(q^{h^0(D)} - 1)/(q-1)`, and summing over the classes of degree `n` counts every effective divisor of degree `n`
once. The Euler product `Z(T) = prod_P (1 - T^{deg P})^{-1}` is the same sum organised by closed points.
(b) `Pic^n` is a torsor for `Pic^0` (translate by `nP_0`), so it has `h` elements. For `deg D = n > 2g-2`,
`deg(K_C - D) < 0` gives `h^0(K_C - D) = 0` and Riemann--Roch gives `h^0(D) = n + 1 - g`. (c) `a_0` counts the
zero divisor only. At `g = 1`, `2g - 2 = 0`, so (b) applies for `n >= 1` with `h^0(D) = n`, and
`Z(T) = 1 + h sum_{n>=1} (q^n - 1)/(q-1) T^n = 1 + (h/(q-1)) [qT/(1-qT) - T/(1-T)] = 1 + hT/((1-T)(1-qT))`.
Multiplying by `(1-T)(1-qT)` gives `P(T) = 1 - (q+1)T + qT^2 + hT`. Then `P(1) = h`, and
`N_1 = 1 + q - (alpha_+ + alpha_-) = 1 + q - (q + 1 - h) = h`. For D2 (`q = 2, h = 1`): `1 - 2T + 2T^2`; for D3
(`q = 3, h = 4`): `1 + 3T^2`; both agree with `def:elliptic-cavity`. (d) `P(1) = det(1 - Fr | H^1) = |J(F_q)|`
(Weil; the `F_q`-points of the Jacobian are the fixed points of Frobenius, counted by the Lefschetz formula on
`H^1` of the Jacobian, whose `H^1` is that of the curve), and `J(F_q) = Pic^0(C)(F_q)` when a rational point
exists. Not byte-cited. QED.

*Reading.* The bond `l^2(Pic^0) (x) l^2(Z)` with the degree shift as transfer has ring norms `a_n`; the generic
part of (b) has the two eigenvalues `q` and `1`, which are the even (Perron, pole) part of
`thm:scattering-superdeterminant`, and the finitely many degrees `n <= 2g-2` where `h^0(D)` exceeds
`n + 1 - g` carry `P(T)`, the `H^1` factor of `sdet(1 - wE_S)` in the variable `w = T^2` (the remaining odd factors
`(1-qw)(1-q^2w)` are the twisted `H^0` and `H^2`; numerics F4). At genus one the bond dimension `h` is the zeta numerator at `T = 1`.

## B2. The theta functional on the bond; Poisson summation is Riemann--Roch

**Proposition B2.** Let `O_A = prod_v O_v` and `f = 1_{O_A}`. For an idele `x` with divisor `D = div(x) = sum_v v(x_v) v`:
(a) `Theta(x f) = sum_{a in K} 1_{O_A}(x a) = q^{h^0(D)}`.
(b) With `d^x x` normalised by `vol(prod_v O_v^x) = 1`, for `Re s > 1` (elsewhere by continuation),
`int_{A^x/K^x} (Theta(x f) - 1) |x|^s d^x x = (q-1)^{-1} sum_{[D] in Pic} (q^{h^0(D)} - 1) q^{-s deg D} = Z(q^{-s})`,
and `int_{A^x} f(x)|x|^s d^x x = sum_{D >= 0} q^{-s deg D} = Z(q^{-s})` as well.
(c) The functional equation `Z(1/(qT)) = q^{1-g} T^{2-2g} Z(T)` is Poisson summation on `A/K` for `f`, and for this
`f` Poisson summation is Riemann--Roch `h^0(D) - h^0(K_C - D) = deg D + 1 - g`. On `Pic^{g-1}` the map
`[D] -> [K_C - D]` preserves the theta divisor `W_{g-1} = {[D] : h^0(D) > 0}`; its fixed locus is the set of theta
characteristics `{[D] : 2[D] = [K_C]}`, a `Pic^0[2]`-torsor (possibly empty over `F_q`) of order at most `2^{2g}`,
which is larger than `W_0` at genus one (two classes for D3, one for D2) and finite against the
`(g-1)`-dimensional `W_{g-1}` for `g >= 2` (review).

*Proof.* (a) `x a in O_A` iff `v(x_v) + v(a) >= 0` for every place, i.e. `div(a) + D >= 0`, i.e. `a in L(D)`;
this set has `q^{h^0(D)}` elements (including `a = 0`). (b) The map `A^x/K^x -> Pic(K)`, `x -> [div x]`, is
surjective with fibres the cosets of `(prod_v O_v^x) K^x / K^x ~ prod_v O_v^x / F_q^x`, of volume `1/(q-1)`;
`|x| = q^{-deg div(x)}` and `Theta(x f) - 1 = q^{h^0(D)} - 1` are constant on fibres, so the integral is
`(q-1)^{-1} sum_{[D]} (q^{h^0(D)} - 1) q^{-s deg D} = sum_n a_n q^{-sn}` by B1(a). The second integral is over the
ideles with `div(x) >= 0`, whose fibres over the effective divisors have volume `1`. (c) Tate's thesis for
function fields (Weil, *Basic number theory*, VII; Rosen, ch. 6 and 7): the global functional equation of
`zeta(f, s)` follows from `sum_{a in K} f(x a) = |x|^{-1} sum_{a in K} \hat f(a/x)` (Poisson on `A/K`, `A/K`
compact and self-dual), and for `f = 1_{O_A}`, with the additive character attached to a global differential `omega` (so that the
self-dual measure gives `vol(O_A) = q^{1-g}`; this choice, not Poisson, is where Serre duality enters),

    hat f = q^{1-g} 1_{O_A(K_C)},   O_A(K_C) = {a : div(a) + div(omega) >= 0 locally},

so that Poisson at `x` reads `q^{h^0(D)} = q^{deg D + 1 - g} q^{h^0(K_C - D)}`,
which is Riemann--Roch. Substituting in (b) gives the functional equation of `Z`. Symmetry of the theta divisor:
for `deg D = g-1`, Riemann--Roch gives `h^0(D) = h^0(K_C - D)`. Not byte-cited. QED.

*Reading.* The bond state is `[D] -> q^{h^0(D)}` on `Pic`; the automorphism (Weyl element of `SL_2(K)` in the
Weil representation, the adelic Fourier transform) acts on it as `D -> K_C - D` with `n -> 2g-2-n`, and the
"pole even, zeros odd" split of the notebook is the split into the generic Riemann--Roch part and the special
part supported on the theta divisor. The two poles of `Z` are the two constant terms, `a = 0` and its Fourier
image, exchanged by the automorphism.

## B3. The cusps of the tree quotient are the class-group bond

**Proposition B3.** Let `R = O(C \ P_0)` with `deg P_0 = 1`, `T` the Bruhat--Tits tree at `P_0`, `Gamma = GL_2(R)`.
(a) The cusps of `Gamma \ T` are in bijection with `Pic(R) ~ Pic^0(K)`; D2 has one, D3 four.
(b) For a character `chi` of `Pic^0`, extended to `Pic` by `chi(P_0) = 1`, put
`L(T, chi) = sum_{[D]} chi([D]) (q^{h^0(D)} - 1)/(q-1) T^{deg D}`. Then `L(T, chi) = sum_{D >= 0} chi([D]) T^{deg D}
= prod_P (1 - chi([P]) T^{deg P})^{-1}`, the Hecke `L`-function of the unramified character `chi`; for `chi != 1`
it is a polynomial of degree `2g - 2`, and at genus one it equals `1`.
(c) At genus one, `dim l^2(Pic^0) = h = P(1)` and `dim K_HW = 4`; these coincide iff `h = 4` (D3), not for D2.

*Proof.* (a) The ends of `T` are `P^1(K_{P_0})`, the cusps of the quotient are the `Gamma`-orbits of the
`K`-rational ends `P^1(K)`, and a `K`-line `L subset K^2` gives the rank-one projective `R`-module `L cap R^2`;
two lines are in the same `GL_2(R)`-orbit iff these modules are isomorphic, and every rank-one projective
module arises, so the cusps are `Pic(R)` (Serre, *Trees*, II.2, the section `def:elliptic-cavity` cites as II.2.4.4; not checkable here). The count is
byte-cited in the repository: `cit:lorscheid-cusp-count` (`1012.3513:hecke.tex:992`, `#cusps = h_X d_x`) and
`cit:apw-cusps-pic-no-funnels` (`2603.26443:final_draft.tex:892`, cusps in bijection with `Pic(R)`). APW's
lattice is `PGL_2(R)`, and the Steinitz argument above is for `GL_2(R)`; the two counts agree by the sources,
not by the argument given (review).
`Pic(R) = Pic(C)/<[P_0]>`, and subtracting a multiple of the degree-one class `[P_0]` normalises each class to
degree zero uniquely, so `Pic(R) ~ Pic^0(K)`. `h = 1` for D2 and `h = 4` for D3 (`def:elliptic-cavity`), matching
the one cusp and the four cusps. (b) By the count of B1(a), `sum_{D >= 0, [D] = c} T^{deg D} = (q^{h^0(c)}-1)/(q-1) T^{deg c}`,
so the first equality is a regrouping and the Euler product follows from unique factorisation of effective
divisors into closed points, `chi` being multiplicative on classes. For `chi != 1` the `L`-function is the
numerator of the zeta function of the unramified abelian cover attached to `chi` divided by that of `C`, a
polynomial of degree `2g - 2` (Rosen, ch. 9; Weil). At `g = 1` this degree is `0`; directly: for `n >= 1`,
`h^0(D) = n` depends only on the degree, and `sum_{[D] in Pic^n} chi([D]) = 0` because `Pic^n` is a `Pic^0`-torsor
and `chi != 1`, while for `n = 0` only `[D] = 0` contributes `1`. Not byte-cited except as stated. (c) `dim l^2(Pic^0) = h` is B1; `dim K_HW = 4` is the count of nonzero
resonances of D2 and D3, `prop:d2-spectrum-frobenius` and `prop:d3-spectrum`, which rest on `asm:h-diag` (the
transcribed stabiliser data) and on H-LP for the model-space reading; so (c) is conditional on `asm:h-diag`
(review). QED.

*Reading.* The four cusps of D3 are `Pic^0 = Z/4`; H-CLASS (`obs:h-class`, `prop:d3-group-matrix`) says the
equal-depth-cut scattering matrix is a `Pic`-group matrix times the inversion pairing `P_inv`; the class
characters block-diagonalise it, with a `2 x 2` block on each inverse pair `{chi, bar chi}` of eigenvalues
`+- (hat f(chi) hat f(bar chi))^{1/2}`, so the Fourier transform on the GL_1 bond `l^2(Pic^0)` is the change of
basis, not the diagonalisation. With `L(T, chi) = 1` for `chi != 1` this reproduces the channels
`{zeta, 1, 1, -1}` of `thm:d3-channels` exactly, the `-1` coming from the inversion pairing and not from a
character value: the three monomial channels are not in bijection with the three nontrivial characters
(review; `thm:d3-height-diagonalisation` already says the congruence does not name the characters). What the
characters do say is that no channel other than `chi = 1` carries a zero at genus one. The coincidence `h = 4 = 4g` at
D3 is not "one cusp per zero mode" (`thm:arithmetic-metric` needs one exit per mode on `K_HW`, and D2 has one
cusp for four modes).

## B4. The case of Q: Riemann's theta on the dilation bond

**Proposition B4.** (a) `A^x = Q^x . R_+^x . Zhat^x` with `Q^x cap (R_+^x Zhat^x) = {1}`, so
`A^x / (Q^x Zhat^x) ~ R_+^x`: the units-invariant GL_1 bond over `Q` is `L^2(R_+^x, d^x x)`, one cusp.
(b) For `x in R_+^x` at the real place and `f = e^{-pi t^2} (x) 1_{Zhat}`, `Theta(x f) = sum_{n in Z} e^{-pi n^2 x^2} = theta(x^2)`,
`theta(y) := sum_n e^{-pi n^2 y}`, with `theta(1/y) = y^{1/2} theta(y)`.
(c) For `0 < Re s < 1`,
`int_0^infty (theta(y) - 1 - y^{-1/2}) y^{s/2} d^x y = 2 pi^{-s/2} Gamma(s/2) zeta(s) = 4 xi(s)/(s(s-1))`,
with `xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)` (the notebook's `\cxi`). The integral diverges outside the
strip. Hence the zeros of `zeta` in the strip are the zeros of the Mellin transform of the odd part
`theta - 1 - y^{-1/2}` of the bond state.

*Proof.* (a) A positive rational that is a `p`-adic unit for every `p` is `1`; every idele is `q . (r, u)` with
`q in Q^x` the signed product of the prime powers `p^{v_p(x_p)}`, `r in R_+^x`, `u in Zhat^x` (class number one and
`Z^x = {+-1}`). (b) `1_{Zhat}(a) = 1` iff `a in Z`, and `x` acts at the real place. (c) Let `psi(y) = (theta(y)-1)/2`.
For `Re s > 1`, `int_0^infty psi(y) y^{s/2} d^x y = pi^{-s/2} Gamma(s/2) zeta(s) =: Lambda(s)` termwise. Riemann's
splitting at `y = 1` with `psi(1/y) = y^{1/2} psi(y) + (y^{1/2} - 1)/2` gives, for all `s`,
`Lambda(s) = int_1^infty psi(y)(y^{s/2} + y^{(1-s)/2}) d^x y - 1/s - 1/(1-s)`. Now compute
`I(s) = int_0^infty (psi(y) - y^{-1/2}/2) y^{s/2} d^x y` in the strip: on `(1, infty)`, `psi y^{s/2}` converges and
`-(1/2) int_1^infty y^{(s-1)/2} d^x y = -1/(1-s)` needs `Re s < 1`; on `(0, 1)`, `psi(y) - y^{-1/2}/2 = y^{-1/2} psi(1/y) - 1/2`,
and `int_0^1 y^{-1/2} psi(1/y) y^{s/2} d^x y = int_1^infty psi(u) u^{(1-s)/2} d^x u` while `-(1/2) int_0^1 y^{s/2} d^x y = -1/s`
needs `Re s > 0`. Adding, `I(s) = Lambda(s)`, and `theta - 1 - y^{-1/2} = 2(psi - y^{-1/2}/2)` gives the factor `2`.
With the notebook's `xi`, `Lambda = 2 xi/(s(s-1))`. Outside the strip one of the two elementary integrals
diverges. QED.

*Corrections to the brief.* B4(b) of the brief wrote `2 xi(s)/(s(s-1))` and "for all `s`"; the correct statement
is `4 xi(s)/(s(s-1))` in the notebook's normalisation of `xi`, valid in the strip `0 < Re s < 1` only. The numerics
specification's test points `s = 2, 3` are outside the strip and must be replaced by points in it (the zeros
`1/2 + i gamma_n` are inside). Recorded in the ledger below.

*Reading.* Riemann's argument is the `Q` case of "adelic symplectic space as bond": bond `L^2(R_+^x)`, no-event
dynamics the dilation, bond state `theta`, automorphism `y -> 1/y` (the Weyl element acting through the Weil
representation, i.e. Fourier on `A/Q`), even sector the two constant terms `1` (the pole `s = 0`) and
`y^{-1/2}` (the pole `s = 1`), in the variable `y = |x|^2`; in the idele variable `x` the same identity reads
`int_0^infty (theta(x^2) - 1 - x^{-1}) x^s d^x x = Lambda(s) = 2 xi(s)/(s(s-1))`, half the constant of (c) because
`d^x y = 2 d^x x` (review; so the brief's constant was right for the idele variable and wrong for `y`),
odd sector `theta - 1 - y^{-1/2}`. **H-THETA** (hypothesis, not claimed): the compression of the dilation
semigroup to the dilation-cyclic subspace of the odd part of `theta`, with the outgoing half `y > 1` removed, is
unitarily equivalent to the Riemann channel of `prop:functional-model-modes` on `K_S = H^2 ominus S H^2`.

## B5. What is and is not gained

The identifications B1--B4 are exact and elementary; they place the bond, its state, its grading and its
automorphism. They do not place the metric. At genus one the Frobenius roots are fixed by `h` alone (B1(c))
and their common modulus `sqrt q` is Hasse's theorem, which nothing on the bond forces. On `K_HW`, any
metric in which `q^{1/4} Z` is unitary is diagonal in the eigenbasis of `Z` (`thm:arithmetic-metric`; not
"Frobenius-normal": Frobenius has doubled eigenvalues on `K_HW` and its normal metrics form an eight-dimensional
cone, review), and the reality and bipartite symmetries fix the ratios; on `H^1 (x) C` itself, when the two
Frobenius eigenvalues are distinct, every Frobenius-normal metric is diagonal in the eigenbasis and reality fixes
the ratio; so "the symmetric ray is the Hodge metric" carries no content at genus one (it fails to be even
well-posed at square `q` with `h = 1`, where `P` has a double root); the first genuine test is genus two, where two Klein orbits can have different moduli
(`lem:funnel-first-order`). The Kraus dichotomy (`obs:kraus-dichotomy`) stands: the automorphism gives the
functional equation, adjoint pairing gives reality, and the circle needs unitarity of the dynamics itself in a
canonical metric.

## Correction ledger against the brief

| # | claim | correction |
|---|---|---|
| 1 | B4(b) | the Mellin identity holds for `0 < Re s < 1` only, and equals `4 xi(s)/(s(s-1))` with the notebook's `xi`; the brief's `2 xi(s)/(s(s-1))` and "for all `s`" are wrong |
| 2 | numerics spec, item 6 | the test points `s = 2, 3` lie outside the strip; the integral diverges there |
| 4 | B4(a) | the lattice sum with `f_infty = e^{-pi t^2}` is `theta(x^2)`, as stated in B4(b) here; the brief's display wrote `theta(x)` (numerics F3) |
| 5 | B1(c), B2(c) | `P` is the `H^1` factor of the superdeterminant in `w = T^2`, not the whole odd part (F4); the involution preserves the theta divisor, its fixed locus is the 2-torsion coset (F5) |
| 6 | review | B2(c) fixed locus = theta characteristics, not "larger"; B2(b) range `Re s > 1`; B2(c) `hat f` displayed with the differential-attached character; B3(a) cusp count byte-cited via Lorscheid and APW, `PGL_2` vs `GL_2`; B3(c) conditional on `asm:h-diag`; B3 reading: block-diagonalisation with `2 x 2` inverse-pair blocks, the `-1` from the pairing; B4 reading: pole pairing and the variable `y = |x|^2`, idele-variable constant `Lambda(s)`; B5: unitarising metrics of `Z`, distinct eigenvalues on `H^1` |
| 3 | B2(b) | `Theta(xf)` in B2(a) is a function of the divisor class only through `h^0`; the Tate integral over `A^x` (not modulo `K^x`) gives `Z` directly with fibre volume `1`, the version over `A^x/K^x` needs the fibre volume `1/(q-1)` and the subtraction of the constant term `a = 0` |
