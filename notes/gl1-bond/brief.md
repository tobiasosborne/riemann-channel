# Brief: the adelic symplectic space as the bond. The GL_1 bond of a function field is the class group, its state is the theta functional, and the cusps of the tree quotient are that bond

Author of the brief and of the proofs (`proofs.md`): `claude:fable-5.1`. Numerics lane: `claude:opus`, blind from
this brief. Review lane: `claude:opus`, REFUTE protocol. Date 2026-09-21.

## Why this round

TJO's question: is it consistent to take the symplectic space over the adeles (`A (+) A` with the rational
Lagrangian `Q (+) Q`, Heisenberg--Weyl representation on `L^2(A)`, Weil representation of `SL_2(Q)`, theta
functional `Theta(f) = sum_{q in Q} f(q)`) as the **bond** (auxiliary) system of the cMPS, not as the bulk?
The notebook's results say the bulk cannot be the adeles: a physical state that is a product over places is
the Bost--Connes side A, bond dimension one, blind to the zeros (`prop:normal-kms-gibbs`, `obs:prime-by-prime-blind`).
This round makes the bond reading concrete in the one setting where everything is finite and RH is known, a
function field `K` of genus `g` over `F_q`, and then states the `Q` case (Riemann's theta) in the same words.
The claims below are elementary function-field facts assembled in the notebook's dictionary; their value is
the identification, not their novelty. The reader will run numerics against every displayed formula.

Conventions: `K` the function field of a smooth projective curve `C/F_q` of genus `g` with at least one
rational point `P_0`; `Pic(K)` the divisor class group, `deg: Pic -> Z`, `Pic^n` its fibres, `h = |Pic^0(F_q)|`
the class number; `h^0(D) = dim_{F_q} L(D)`, `L(D) = {f in K^x : div f + D >= 0} cup {0}`; `Z(T) = zeta_K(s)` with
`T = q^{-s}`, `Z(T) = P(T)/((1-T)(1-qT))`, `P(T) = prod_{i=1}^{2g}(1 - alpha_i T)`, `N_k = 1 + q^k - sum alpha_i^k`.
For the affine ring `R = O(C \ P_0)`, `Pic(R) = Pic^0(K)` when `P_0` is rational. D2: `q = 2`, `y^2+y = x^3+x+1`,
`h = 1`; D3: `q = 3`, `y^2 = x^3+x+1`, `h = 4` (shard 04k, `def:elliptic-cavity`).

## B1. The class-group bond and its ring norms

(a) `Z(T) = sum_{n >= 0} a_n T^n` with `a_n = #{effective divisors of degree n} = sum_{[D] in Pic^n} (q^{h^0(D)} - 1)/(q - 1)`.
(b) Riemann--Roch (`h^0(D) - h^0(K_C - D) = n + 1 - g`, `n = deg D`) gives `a_n = h (q^{n+1-g} - 1)/(q-1)` for
`n > 2g - 2`: the "generic" part, geometric in `q^n` and `1`; the deviations are supported on `n <= 2g-2` and come
from the special classes (`h^1(D) != 0`), i.e. from the theta divisor of the Jacobian.
(c) In the tensor-network reading: bond `l^2(Pic^0) (x) l^2(Z)` (class times degree), the transfer step is the
degree shift, the ring norm at length `n` is `a_n`, and the two eigenvalues `q, 1` of the generic part are the
Perron pair (the pole), while the finitely many special degrees carry the zeros. `Z(T)` is the ring-norm
generating function of this bond; `P(T) = (1-T)(1-qT) Z(T)` is its odd part in the sense of
`thm:scattering-superdeterminant`.
(d) Genus one: `Z(T) = 1 + h T/((1-T)(1-qT))`, `P(T) = (1-T)(1-qT) + hT = 1 - (q+1-h)T + qT^2`, so `h = P(1) = N_1`
and the Frobenius eigenvalues are determined by the class number alone. D2: `P = 1 - 2T + 2T^2`; D3: `P = 1 + 3T^2`
(checked symbolically before writing this brief). In general `h = P(1) = det(1 - Fr | H^1)`: **the bond dimension
of the class-group bond is the zeta numerator at `T = 1`**.

## B2. The theta functional is the state on the bond; Poisson summation is Riemann--Roch

(a) For an idele `x` with divisor `D = div(x)` and `f = 1_{O_A}` (the product of the local unit balls),
`Theta(x f) = sum_{a in K} 1_{O_A}(x a) = #L(D) = q^{h^0(D)}`: the theta functional evaluated on the idele class
of `D` is `q^{h^0(D)}`, a function on `Pic(K)`; the bond state is `[D] -> q^{h^0(D)}`.
(b) Tate's zeta integral over the ideles, `zeta(f, s) = int_{A^x} f(x)|x|^s d^x x` with `f = 1_{O_A}`, equals
`(q-1)^{-1} sum_{[D]} (q^{h^0(D)} - 1) q^{-s deg D}` up to the volume normalisation, i.e. `Z(T)` of B1(a); the
poles at `T = 1` and `T = 1/q` come from the two constant terms of the theta functional (the term `a = 0` and its
Fourier image), and the functional equation `Z(1/(qT)) = q^{1-g} T^{2-2g} Z(T)` is Poisson summation on `A/K`
applied to `f`, which for this `f` is exactly Riemann--Roch (`h^0(D) - h^0(K_C - D) = deg D + 1 - g`).
(c) Hence: the automorphism of the Heisenberg--Weyl system (the Weyl element, the adelic Fourier transform)
acts on the bond state as `[D] -> [K_C - D]` together with the degree reflection `n -> 2g-2-n`; on `Pic^{g-1}` it
is the involution fixing the theta divisor. The "pole even, zeros odd" grading of the notebook is the split
of the bond state into its generic Riemann--Roch part (even: `q^{n+1-g}` and `1`, the constant terms) and the
special part (odd, supported on the theta divisor).

## B3. The cusps of the tree quotient are the class-group bond

(a) The cusps of `GL_2(R) \ T` are in bijection with `Pic(R) = Pic^0(K)` (Serre, Trees II.2; `cit:lorscheid-cusp-count`
gives `h deg x` for a removed place `x`): D2 has one cusp, D3 has four. So the hedgehog's spikes **are** the
units-invariant part `l^2(Pic^0)` of the GL_1 adelic bond, and H-CLASS (`obs:h-class`: the equal-depth-cut
scattering matrix is a `Pic`-group matrix diagonalised by the class characters) is the statement that the
GL_2 scattering matrix is the Fourier transform on the GL_1 bond.
(b) The class characters `chi` of `Pic^0` diagonalise the degree-shift transfer of B1(c); the `chi`-channel has
ring-norm generating function `L(T, chi) = sum_{[D]} chi([D]) (q^{h^0(D)}-1)/(q-1) T^{deg D}` (for `chi != 1` this is
the Hecke `L`-function of `chi`, a polynomial of degree `2g - 2`), which at genus one is `1`: the three monomial
channels of D3 (`thm:d3-channels`) are the three nontrivial class characters seeing no zeros, and the zeta
channel is the trivial character. This is `prop:character-channel-graded-bond` at the level of `Pic^0` instead
of `(F_q[T]/N)^x`.
(c) Consequently, at genus one the class-group bond has dimension `h = P(1)` while the Hasse--Weil sector has
dimension `4` (two Frobenius eigenvalues, each with two square roots); they coincide for D3 (`h = 4`) and not for
D2 (`h = 1`). The "one exit per zero mode" of `thm:arithmetic-metric` is therefore NOT "one cusp per class" in
general; the coincidence at D3 is the accident `P(1) = 4 = 4g`.

## B4. The case of Q: Riemann's theta on the dilation bond

(a) `Pic(Z)` is trivial and the units are `{+-1}`, so the units-invariant GL_1 bond over `Q` is `L^2(R_+^x, d^x x)`
alone (one cusp, `h = 1`), and the theta functional on `x f_infty (x) 1_{Zhat}` with `f_infty(t) = e^{-pi t^2}` is
Jacobi's `theta(x) = sum_{n in Z} e^{-pi n^2 x}`: the bond state is `theta`, a function on the dilation line.
(b) Its constant terms are `1` (the term `n = 0`) and `x^{-1/2}` (the Fourier image, `theta(1/x) = x^{1/2} theta(x)`):
the even sector, the pole pair `s = 0, 1`, exchanged by the automorphism; the odd part `theta(x) - 1 - x^{-1/2}`
has Mellin transform `int_0^infty (theta(x) - 1 - x^{-1/2}) x^{s/2} d^x x = 2 xi(s)/(s(s-1))` for all `s` (Riemann),
where `xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)`: the zeros of `zeta` are the zeros of the Mellin transform of the odd
part of the bond state.
(c) So the `Q` case of "adelic symplectic space as bond" is Riemann's 1859 setup read as a cMPS: bond `L^2(R_+^x)`,
no-event dynamics the dilation, bond state `theta`, automorphism `x -> 1/x` (the Weyl element of `SL_2(Q)` acting
through the Weil representation, i.e. the Fourier transform on `A/Q`), even sector the two constant terms, odd
sector the rest. The notebook's Riemann channel (`prop:functional-model-modes`: one mode per zero on
`K_S = H^2 ominus S H^2`, `S(tau) = xi(1-2i tau)/xi(1+2i tau)`) is the compression of this dilation to the model
space of the automorphism's symbol; whether the dilation-cyclic subspace of the odd part of `theta`, with the
outgoing half `x > 1` removed, is unitarily that model space is **H-THETA**, stated here as a hypothesis for the
next round, not claimed.

## B5. What is and is not gained for RH

(a) Gained: the bond is identified (B1--B4) with objects whose ring norms are exact (`a_n`, `q^{h^0(D)}`, `theta`),
the grading is the constant-term/special split, and the automorphism is Poisson summation. All of this is
side-B bookkeeping of known theorems.
(b) Not gained: the metric. On the class-group bond at genus one the Frobenius roots are fixed by `h` (B1(d)) and
their common modulus `sqrt q` is Hasse's theorem; nothing in B1--B4 forces it. On `K_HW` the unitarising metrics
form the cone of `thm:arithmetic-metric` and the symmetric ray is fixed by the Klein group, but at genus one any
Frobenius-normal metric on `H^1 (x) C` is diagonal in the eigenbasis and the reality and bipartite symmetries
fix its ratios, so "the symmetric ray is the Hodge metric" is vacuous at genus one and can only be tested at
genus two. The Kraus dichotomy (`obs:kraus-dichotomy`) stands: the automorphism gives the functional equation,
not the circle.

## What the numerics lane must do (blind; do not read `proofs.md`)

Write `scripts/gl1_bond.py` (deterministic, seed `20260921`, stdlib + numpy + sympy, under `60 s`, a single
`check(cond, msg)` helper, tally `CHECKS: <passed> passed, <failed> failed`, no timestamps) and
`notes/gl1-bond/numerics.md` (ledger rows D1, D2, ..., each with the claim tested, what was computed, the
result, VERIFIED/FAILED/PARTIAL, and the line of the assertion; then "Findings against the brief"; then
"Conventions used"; then the tally). Capture stdout to `outputs/gl1_bond.txt`.

Concretely, for both curves (D2: `y^2 + y = x^3 + x + 1` over `F_2`; D3: `y^2 = x^3 + x + 1` over `F_3`):
1. Enumerate the closed points of degree `<= 6` by grouping `C(F_{q^k})` into Frobenius orbits (build `F_{q^k}`
   as `F_q[t]/(irreducible)`), including the point at infinity; count effective divisors `a_n` for `n <= 6` from
   the closed points; check `a_n` against the coefficients of `Z(T) = P(T)/((1-T)(1-qT))` with the `P` of shard 04k.
2. Compute `Pic^0(F_q)` explicitly as the group of `F_q`-points of the elliptic curve (group law), verify `h = 1`
   and `h = 4` (and that D3's group is `Z/4`), and verify B1(d): `P(T) = 1 - (q+1-h)T + qT^2`, `h = P(1) = N_1`.
3. For a set of divisors `D` of degrees `0..4` (sums of the closed points found), compute `h^0(D)` by linear
   algebra over `F_q` (Riemann--Roch spaces via explicit function bases; for an elliptic curve `L(nP_0)` has the
   basis `1, x, y, x^2, xy, ...` and a general `D` can be reduced to `nP_0` plus a translation by the group law:
   use `h^0(D) = h^0(D - div(f))` and the fact that on an elliptic curve `h^0(D) = deg D` for `deg D >= 1` and
   `h^0(D) = 1` iff `D ~ 0` for `deg D = 0`); verify `a_n = sum_{[D] in Pic^n}(q^{h^0(D)}-1)/(q-1)` for `n = 0..4` by
   summing over the `h` classes of each degree.
4. Verify Riemann--Roch numerically on those divisors (`h^0(D) - h^0(-D) = deg D` at genus one, `K_C = 0`) and the
   functional equation `Z(1/(qT)) = T^0 Z(T)` at `g = 1` symbolically.
5. For D3 compute the four class characters of `Z/4` and the `L`-polynomials `L(T, chi)` of B3(b) from the
   `h^0` data of step 3 (sum over classes with `chi`), verifying `L(T, chi) = 1` for `chi != 1` and `Z(T)` for
   `chi = 1`; report the same for D2 (only the trivial character).
6. Jacobi theta: verify numerically (mpmath, 30 digits) that `int_0^infty (theta(x) - 1 - x^{-1/2}) x^{s/2} d^x x = 2 xi(s)/(s(s-1))`
   at `s = 2, 3, 1/2 + 14.134725 i, 1/2 + 21.022040 i` (the last two should be numerically zero to the precision
   of the zero) and `theta(1/x) = sqrt x theta(x)` at `x = 1/3, 1, 7`.
7. The cusp count: state (do not derive) the cusp numbers `1` and `4` from shard 04k and check them against `h`.

Report every discrepancy as a finding.
