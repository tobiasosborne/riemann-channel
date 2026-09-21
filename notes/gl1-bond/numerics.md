# GL_1 bond -- numerics lane

**Lane.** Blind numerics lane, author line `claude:opus`.
**Brief.** `notes/gl1-bond/brief.md` (author `claude:fable-5.1`), claims **B1--B5**, and in particular
the specification in its final section *"What the numerics lane must do"*, steps 1--7.
**Protocol.** BLIND to the prover: `notes/gl1-bond/proofs.md` exists in the repository and was **not
opened**. The only other repository files read were `report/sections/04k_elliptic_cavity_scattering.tex`
(for `def:elliptic-cavity`: the two curves, their `P(T)`, their Weil numbers, their cusp numbers and
`Pic(R)`), `report/sections/04n_graded_toys_network.tex` (for `thm:scattering-superdeterminant`) and
`scripts/graded_toys.py` (for its finite-field / polynomial coding conventions only -- nothing is
imported; every field, every curve and the whole group law are re-implemented in this lane's script).

**Script.** `scripts/gl1_bond.py` (python3 + numpy + sympy + mpmath, deterministic, seed `20260921`,
no timestamps, no addresses, runtime ~5 s).
**Output.** `outputs/gl1_bond.txt`, produced by
`python3 scripts/gl1_bond.py > outputs/gl1_bond.txt 2>&1` from the repository root; two consecutive
runs are byte-identical.
**Assertions.** Every claim goes through the single helper `check(cond, msg)`, which counts, prints one
line `ok  [L<line>]  <msg>` or `FAIL [L<line>]  <msg>`, and never aborts. No tolerance was loosened to
make anything pass: the seven failing checks are the brief's own formulas, asserted as written.

Ledger rows below are labelled **D01, D02, ...** (two digits) so that they are never confused with the
two **curves**, which the brief calls **D2** (`y^2+y = x^3+x+1` over `F_2`) and **D3**
(`y^2 = x^3+x+1` over `F_3`). "Assertion line" is the line of `scripts/gl1_bond.py` printed inside the
`[L....]` tag of the corresponding output lines.

---

## Ledger

| Row | Claim tested | What was computed | Result | Status | Assertion line(s) |
|---|---|---|---|---|---|
| D01 | 04k `def:elliptic-cavity` / B1(d): `P(T) = prod(1-alpha_i T)`, `|alpha_i| = sqrt q`, `N_1 = 1+q-sum alpha_i` | `C(F_q)` enumerated point by point from the Weierstrass equation (infinity included) for both curves; `P` and the `alpha_i` taken from 04k and multiplied out in sympy | `N_1 = 1` (D2), `4` (D3); `P_D2 = 1-2T+2T^2`, `P_D3 = 1+3T^2`; `alpha = 1 +- i` resp. `+- i sqrt 3`, both of modulus `sqrt q` | VERIFIED | 421, 424, 427 |
| D02 | Conventions: `N_k = 1 + q^k - sum alpha_i^k` | `C(F_{q^k})` enumerated for `k = 1..6` over `F_{q^k} = F_q[t]/(m_k)` built here | D2 `[1,5,13,25,41,65]`, D3 `[4,16,28,64,244,784]`, equal to the prediction for every `k` | VERIFIED | 438 |
| D03 | step 1: closed points as Frobenius orbits; `sum_{d|k} d b_d = N_k` | orbits of `x -> x^q` on `C(F_{q^k})`, `k <= 6`, grouped; Mobius inversion cross-check | `b_d(D2) = [1,2,4,5,8,8]`, `b_d(D3) = [4,6,8,12,48,124]`; both identities exact; `P_0 = O` is a degree-one closed point | VERIFIED | 477, 481, 483 |
| D04 | **B1(a)**: `Z(T) = sum a_n T^n`, `a_n = #{effective divisors of degree n}` | product `prod_P (1-T^{deg P})^{-1}` over the enumerated closed points, truncated at `T^6`, against the Taylor coefficients of `P(T)/((1-T)(1-qT))` | D2 `[1,1,3,7,15,31,63]`, D3 `[1,4,16,52,160,484,1456]`, exact agreement `n = 0..6` | VERIFIED | 500 |
| D05 | **B1(b)**: `a_n = h(q^{n+1-g}-1)/(q-1)` for `n > 2g-2`; deviations only on `n <= 2g-2` | the same `a_n` against the closed form, `g = 1` | holds for every `n >= 1`; the single deviation is `a_0 = 1` against the formula's `0` | VERIFIED | 510, 513 |
| D06 | **B1(c)**: the generic part has the two eigenvalues `q` and `1` (the Perron pair) | the recursion `a_{n+1} = (q+1)a_n - q a_{n-1}` for `n >= 2`, and the explicit two-mode form `a_n = A q^n + B`, `A = h/(q-1)`, `B = -A` | recursion exact; `A q^0 + B = 0 != a_0 = 1`, so the whole "special" content sits at `n = 0 = 2g-2` | VERIFIED | 519, 525 |
| D07 | step 2 / implementation: the general-Weierstrass group law (char 2 included) | closure, identity, inverses, commutativity and full associativity over `F_q`; every point on the curve and 60 seeded random associativity triples over `F_{q^3}` | all identities hold for both curves | VERIFIED | 542, 548, 553, 564 |
| D08 | step 2 / **B1(d)**, **B3(a)**: `Pic^0(K) = E(F_q)`, `h = 1` and `h = 4`, D3's group is `Z/4` | the group `E(F_q)` and the order of every element | D2: `{O}`, `h = 1`. D3: orders `[1,2,4,4]`, so cyclic `Z/4`, `h = 4`; a discrete log to a chosen generator is a bijection onto `Z/4` | VERIFIED | 579, 583, 594, 599 |
| D09 | **B1(d)**: `P(T) = (1-T)(1-qT)+hT = 1-(q+1-h)T+qT^2`, `Z(T) = 1 + hT/((1-T)(1-qT))`, `h = P(1) = N_1` | sympy, exactly, from the computed `h` | all three identities exact for both curves | VERIFIED | 604, 607, 609 |
| D10 | step 3: `h^0(nP_0)` by **explicit linear algebra**, basis `1, x, y, x^2, xy, x^3, ...` | rank over `F_{q^6}` of the value matrix of `{x^i y^j : j <= 1, 2i+3j <= n}` at all affine points of `C(F_{q^6})` (64 for D2, 783 for D3), `n = 0..4` | ranks `= #monomials = [1,1,2,3,4]`; `h^0 = deg` for `deg >= 1`, `h^0(0) = 1`; independence is *proved* (a nonzero element has at most `n` zeros) | VERIFIED | 687, 693 |
| D11 | **B2(a)**: `Theta(x f) = #L(D) = q^{h^0(D)}` | all `q^{dim}` `F_q`-combinations of the basis enumerated and separated by their values, `n = 0..4` | exactly `q^{h^0}` distinct functions in every case (`2,2,4,8,16` and `3,3,9,27,81`) | VERIFIED | 712 |
| D12 | the class map (needed for steps 3 and 5): `Tr(P) = sum` over the Frobenius orbit is `F_q`-rational and is the class of `P - (deg P) P_0` | group law over `F_{q^d}` applied to every closed point of degree `d <= 4`, then tested for rationality of both coordinates | rational in every case for both curves; on degree-one points `Tr` is the identity and `Tr(P_0) = O` | VERIFIED | 744, 748 |
| D13 | step 3: `h^0` from raw counting, and the theta divisor at `g = 1` | all effective divisors of degree `<= 4` enumerated as multisets of closed points (27 for D2, 233 for D3) and sorted into classes by `D12` | every class of `Pic^n` (`n = 1..4`) holds exactly `(q^n-1)/(q-1)` effective divisors; in degree 0 only the trivial class holds one; hence the enumeration-based `h^0` is `deg D` resp. `1/0` | VERIFIED | 776, 801, 807 |
| D14 | **B1(a)** at the level of classes: `a_n = sum_{[D] in Pic^n}(q^{h^0(D)}-1)/(q-1)` | that sum over the `h` classes with `h^0` read off the enumeration, `n = 0..4`; and the two `h^0` routes (enumeration vs Riemann--Roch consequence) compared on all 260 effective divisors | identity exact for both curves; the two routes agree everywhere | VERIFIED | 843, 852 |
| D15 | step 4: Riemann--Roch `h^0(D)-h^0(K_C-D) = deg D + 1 - g`, `g = 1`, `K_C = 0` | 72 (D2) and 74 (D3) seeded **signed** divisors of degree `0..4` with multiplicities in `-2..2`, both `h^0` routes | `h^0(D)-h^0(-D) = deg D` in every case, including with `h^0` taken from raw counting only | VERIFIED | 885, 889 |
| D16 | **B2(b)** / step 4: `Z(1/(qT)) = q^{1-g} T^{2-2g} Z(T)`; poles of `Z` | sympy, exactly, for both curves at `g = 1`, plus a genus-0 control (`q = 2`, `P = 1`) where the prefactor `2T^2` is nontrivial | holds exactly; at `g = 1` the prefactor is `1`, so `Z(1/(qT)) = Z(T)`; `P(1) != 0` and `P(1/q) != 0`, so the only poles are the simple ones at `T = 1, 1/q` | VERIFIED | 903, 906, 911, 918 |
| D17 | **B2(c)**: the Weyl automorphism acts as `[D] -> [K_C-D]` with `n -> 2g-2-n`; "on `Pic^{g-1}` it is the involution fixing the theta divisor" | the map `[D] -> [-D]` on `E(F_q)`; its fixed locus; the theta divisor of `Pic^0` from D13 | involution: yes; it fixes the theta divisor `{O}`: yes; but its fixed locus is the 2-torsion, **2 classes** for curve D3 against the theta divisor's 1 | PARTIAL | 928, 931, 934 |
| D18 | **B3(b)**: `L(T,chi) = sum chi([D])(q^{h^0}-1)/(q-1) T^{deg D}`; `= 1` for `chi != 1` at `g = 1`; `= Z(T)` for `chi = 1` | the four characters of `Pic^0 = Z/4` (D3) and the single character (D2) summed against the enumerated per-class counts, `n = 0..4` | `L(T,1) = Z(T)` exactly; each of the three nontrivial characters gives constant term 1 and coefficients 0 in degrees 1..4, i.e. `L = 1`, a polynomial of degree `2g-2 = 0`; the mechanism (orthogonality x constant per-class count) also checked | VERIFIED | 1003, 1014, 1020, 1024, 1029 |
| D19 | step 7 / **B3(a)**: cusp numbers `1` and `4` (STATED from 04k) against `h`; Lorscheid's `h deg x` | the stated cusp numbers compared with the computed `h`, with `deg P_0 = 1` | `1 = h(D2)`, `4 = h(D3)`; `h * deg x` gives the same | VERIFIED | 1040, 1044 |
| D20 | **B3(c)**: `dim K_HW = 4` vs `h`; coincidence for D3, not D2; `4 = 4g` | comparison of the computed `h` with 4 | D2 `h = 1 != 4`; D3 `h = 4 = 4`; and `4 = 4g` at `g = 1`, so the stated accident is arithmetically consistent | VERIFIED | 1052, 1056 |
| D21 | **B1(c)** via `thm:scattering-superdeterminant`: `P(T) = (1-T)(1-qT)Z(T)` "is its odd part" | `sdet(1-wE_S)` from the even spectrum `{1,q,q alpha_i}` and odd spectrum `{alpha_i,q,q^2}`, in sympy; compared with `(1-w)P(qw)/((1-q^2w)P(w))` and with `Z(qw)/Z(w)` | the superdeterminant identity and its equality with `zeta_K(2s-1)/zeta_K(2s)` are exact; but the **full odd factor is `P(w)(1-qw)(1-q^2w)`**, and the variable is `w = T^2` | PARTIAL | 949, 954, 959 |
| D22 | **B4(b)**: `theta(1/x) = sqrt x theta(x)` at `x = 1/3, 1, 7` | both sides summed directly (no functional equation used), mpmath, 40 working digits | deviations `0, 0, 9.2e-41` | VERIFIED | 1096 |
| D23 | **B4(b)** inside `0 < Re s < 1`: `int_0^oo (theta(x)-1-x^{-1/2}) x^{s/2} d^x x = 2 xi(s)/(s(s-1))` | the integral at `s = 1/2, 0.3, 0.7+0.2i`, theta-tails by tanh-sinh quadrature and the two elementary tails in exact closed form (`2/s`, `-2/(s-1)`, both verified) | the integral equals **`2 xi(s)`** to `< 1e-40`; the brief's right-hand side is off by `|I| ~ 8` against `|brief| ~ 32-55`; the ratio `I/(2 xi/(s(s-1)))` is **exactly `s(s-1)`** | FAILED (brief's constant) | 1125, 1134, 1145, **1148**, 1152 |
| D24 | **B4(b)**: "for all `s`", and step 6's test points `s = 2, 3` | the tail `int_A^{2A}` of the integrand for `A = 10, 100, 1000` at `s = 2, 3`, and its exact elementary value | the tail **grows** like `-2 x^{(s-1)/2}`: the integral **diverges** for `Re s >= 1`; it converges only on `0 < Re s < 1` | PARTIAL | 1164, 1175 |
| D25 | **B4(b)** at `s = 2, 3` (after analytic continuation) | the continued expression at `s = 2, 3`, against `2 xi(s)` and against the brief's `2 xi(s)/(s(s-1))` | equals `2 xi(s)` to `0` and `5.7e-42` (`2 xi(2) = pi/3` exactly); the brief's form is off by the factors `2` and `6` | FAILED (brief's constant) | 1185, **1189**, 1192 |
| D26 | step 6: at `s = 1/2 + 14.134725 i` and `1/2 + 21.022040 i` the transform is "numerically zero to the precision of the zero" | the same integral at the two truncated zeros; `xi` at the full-precision zeros | `|I| = 3.9e-12` and `5.8e-14` against `|I| ~ 8` elsewhere in the strip, consistent with `|2 xi'| |t - t_true|`; `I = 2 xi(s)` to `1e-44`; the full-precision zeros give `|xi| < 1e-23` | VERIFIED | 1201, 1206, 1210 |
| D27 | **B4(b)**, independent discrimination of the two candidate right-hand sides | the residue of the transform at `s = 1` and `s = 0` by `eps`-scaling | **simple** poles with residues `+2` and `-2`, exactly those of `2 xi(s)`; `2 xi(s)/(s(s-1))` would have **double** poles there | VERIFIED | 1219 |
| D28 | **B4(a)**: the theta functional on `x f_oo (x) 1_{Zhat}` with `f_oo(t) = e^{-pi t^2}` "is `theta(x) = sum e^{-pi n^2 x}`" | the lattice sum `sum_{n in Z} f_oo(xn)` at `x = 1.7, 0.6` against `theta(x^2)` and against `theta(x)` | the sum equals **`theta(x^2)`** to `1e-40`; against `theta(x)` it is off by `9.4e-3` resp. `3.6e-1` | FAILED (normalisation) | 1231, **1235** |
| D29 | **B5(b)**: "the Frobenius roots are fixed by `h` ... nothing in B1--B4 forces `sqrt q`" | for the genus-one shape `P = 1-(q+1-h)T+qT^2`, the equal-modulus property against the Hasse interval, `q = 2,3,4,5` and all `h` in range; explicit witness `q = 2, h = 6` | equal modulus holds exactly on `|h-(q+1)| <= 2 sqrt q`; the witness gives `alpha = -1, -2`, moduli `1, 2 != sqrt 2` | VERIFIED (supports B5(b)) | 624, 630 |
| D30 | **B5(b)**: at genus one "any Frobenius-normal metric is diagonal in the eigenbasis ... vacuous" | distinctness of the two `alpha_i`, and the commutant of `diag(alpha_1, alpha_2)` solved symbolically | eigenvalues distinct for both curves; the commutant is exactly the 2-dimensional diagonal algebra, so only one ratio is free | VERIFIED (supports B5(b)) | 968, 976 |
| D31 | **B4(b)**: the two constant terms `1` and `x^{-1/2}` are the pair exchanged by `x -> 1/x` | `u(x) = theta(x)-1-x^{-1/2}` against `x^{-1/2} u(1/x)` at `x = 1/4, 5/2` | equal to `< 1e-28`: the odd part transforms with the same sign rule, so the even/odd split of B4(b) is internally consistent | VERIFIED | 1245 |

---

## Findings against the brief

Five places where the brief's formula, constant or claim does not hold as stated. Three are hard
numerical failures (F1--F3) and two are imprecisions that a reader would take as stated (F4, F5).
The corrected form is given in each case. Everything else in B1--B5 that this lane could reach came
out exactly as the brief writes it, including the parts of B5 that say what is *not* gained (D29, D30).

**F1 (hard failure). B4(b): the constant in the Mellin identity is wrong by `s(s-1)`.**
The brief displays
`int_0^oo (theta(x) - 1 - x^{-1/2}) x^{s/2} d^x x = 2 xi(s)/(s(s-1))`.
The correct identity is
> **`int_0^oo (theta(x) - 1 - x^{-1/2}) x^{s/2} d^x x = 2 xi(s)`**, with `xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)`.

Measured at `s = 1/2`, `0.3`, `0.7+0.2i` the integral equals `2 xi(s)` to better than `1e-40`
(rows D23, lines 1145), while the brief's right-hand side is wrong by exactly the factor `s(s-1)`:
the ratio `I(s)/(2 xi(s)/(s(s-1)))` is `-0.25`, `-0.21`, `-0.25+0.08i`, i.e. `s(s-1)` to `1e-30`
(line 1152). After continuation the same holds at the brief's own test points, `2 xi(2) = pi/3`
against the brief's `pi/6`, and `2 xi(3) = 0.38262659603...` against the brief's `0.06377109934...`
(D25, line 1189). Two independent confirmations that `2 xi(s)` and not `2 xi(s)/(s(s-1))` is right:
(i) the transform has **simple** poles at `s = 0, 1` with residues `-2, +2`, exactly those of `2 xi`,
whereas `2 xi(s)/(s(s-1))` has **double** poles there (D27, line 1219); (ii) the derivation
`I(s) = 2[xi(s) - 1/(s(s-1))] + (-2/s + 2/(s-1)) = 2 xi(s)`, the two elementary tails cancelling the
`1/(s(s-1))` of Riemann's formula -- which is presumably where the spurious factor came from.
*The qualitative claim of B4(b) survives intact*: the zeros of `zeta` are exactly the zeros of the
Mellin transform of the odd part of the bond state (D26), because the spurious factor is nonvanishing
there. Only the constant is wrong.

**F2 (hard failure, same display). B4(b): "for all `s`" is false for the integral as written; and the
brief's step 6 asks for it to be tested at two points where it diverges.**
The integrand behaves like `-x^{(s-3)/2}` at infinity, so the integral converges **only on the strip
`0 < Re s < 1`**; at `s = 2` and `s = 3` -- the first two test points of step 6 -- the tail
`int_A^{2A}` grows as `2.62, 8.28, 26.20` resp. `10, 100, 1000` for `A = 10, 100, 1000`, exactly the
elementary `-2 x^{(s-1)/2}` (D24, lines 1164, 1175). Corrected form:
> the identity holds **for `0 < Re s < 1` as a convergent integral, and for all `s` by analytic
> continuation**, the continuation being effected by replacing the two elementary tails
> `int_1^oo u^{-s/2-1} du` and `int_1^oo x^{(s-1)/2-1} dx` by their closed forms `2/s` and `-2/(s-1)`.

**F3 (hard failure). B4(a): the archimedean normalisation is off by a square.**
The brief says the theta functional on `x f_oo (x) 1_{Zhat}` with `f_oo(t) = e^{-pi t^2}` "is Jacobi's
`theta(x) = sum_{n in Z} e^{-pi n^2 x}`". The actual lattice sum is
`sum_{n in Z} f_oo(xn) = sum_{n in Z} e^{-pi n^2 x^2} = theta(x^2)`, verified to `1e-40` at
`x = 1.7, 0.6` while the brief's `theta(x)` is off by `9.4e-3` resp. `3.6e-1` (D28, line 1235).
Corrected form: with `f_oo(t) = e^{-pi t^2}` and `theta` in the brief's own normalisation
`theta(y) = sum e^{-pi n^2 y}`,
> **the bond state is `x -> theta(x^2)`** on the dilation line (equivalently: read the brief's `x` as
> the *idele norm* `|x|` only after replacing `theta(x)` by `theta(x^2)`; the functional equation then
> reads `theta(x^{-2}) = x theta(x^2)`, and the two constant terms of B4(b) become `1` and `x^{-1}`).

This is a bookkeeping slip, not a structural one -- B4(b) and B4(c) are self-consistent in the variable
`y = x^2` -- but the two displays of B4 are written in two different variables as they stand.

**F4 (imprecision). B1(c): "`P(T) = (1-T)(1-qT) Z(T)` is its odd part in the sense of
`thm:scattering-superdeterminant`."**
Two things are not right as stated. (i) In `sdet(1-wE_S)` the odd spectrum is
`{alpha_i, q, q^2}`, so the full odd factor is `P(w)(1-qw)(1-q^2 w)`, and even after the two lines with
eigenvalue `q` cancel against the even side it is `P(w)(1-q^2 w)`, not `P(w)` (D21, line 959, exact in
sympy). (ii) The superdeterminant lives in `w = q^{-2s} = T^2`, not in `T`. Corrected form:
> `P` is the **`H^1` (odd) factor** of `sdet(1-wE_S)` in the variable `w = T^2`; the remaining odd
> factors `(1-qw)(1-q^2 w)` are `H^0` twisted and `H^2` twisted.

The identity the sentence is pointing at *is* exact and was verified:
`zeta_K(2s-1)/zeta_K(2s) = sdet(1-wE_S) = (1-w)P(qw)/((1-q^2 w)P(w))` (D21, lines 949, 954).

**F5 (imprecision). B2(c): "on `Pic^{g-1}` it is the involution fixing the theta divisor."**
The involution `[D] -> [K_C - D]` does fix the theta divisor, but the phrase reads as a
characterisation and is not one: at genus one the theta divisor of `Pic^{g-1} = Pic^0` is the single
principal class, while the fixed locus of the involution is the whole 2-torsion -- **two** classes for
curve D3, one for curve D2 (D17, line 934). Corrected form:
> the involution `[D] -> [K_C - D]` of `Pic^{g-1}` **preserves** the theta divisor; its fixed locus is
> the `K_C`-translated 2-torsion coset and is in general strictly larger.

**Non-findings worth recording** (checked, and the brief is right): B1(a),(b),(d) exactly, including
`h = P(1) = N_1` and the single deviation at `n = 0 = 2g-2`; B2(a) `Theta(xf) = q^{h^0(D)}` by explicit
count; B2(b) the functional equation with its `q^{1-g}T^{2-2g}` prefactor (also checked at `g = 0`,
where the prefactor is nontrivial, so it is not an artefact of `g = 1`); B3(a) `#cusps = h` for both
curves and Lorscheid's `h deg x`; B3(b) `L(T,chi) = 1` for the three nontrivial class characters of D3
and `Z(T)` for the trivial one; B3(c) the `h = 4 = dim K_HW` coincidence at D3 and its failure at D2;
B5(b) both of its negative claims, which this lane could make precise and confirm (D29: the genus-one
`h -> P(T)` map forces equal moduli exactly on the Hasse interval and not otherwise, with the explicit
counterexample `q = 2, h = 6`, `alpha = -1, -2`; D30: the commutant of Frobenius on `H^1 (x) C` at
genus one is the diagonal algebra, so the symmetric-ray statement is vacuous there).

---

## Conventions used

1. **Curves and coefficients.** Both curves are handled in the general Weierstrass form
   `y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6`: curve D2 is `(0,0,1,1,1)` over `F_2`, curve D3
   is `(0,0,0,1,1)` over `F_3`. The group law is the general one (Silverman III.2.3), implemented in
   this script, so no short-Weierstrass shortcut is used for curve D2 in characteristic 2. `P_0` is the
   point at infinity `O = (0:1:0)`, `F_q`-rational, the identity of the group; `R = O(C \ P_0)`.
2. **Finite fields.** `q` is prime for both curves, so `F_q = F_p`. `F_{q^k} = F_q[t]/(m_k)` with `m_k`
   the lexicographically first monic irreducible of degree `k` (coefficients low-to-high as base-`q`
   digits), found by trial division against the irreducibles of degree `<= k/2`; the coding convention
   for polynomials follows `scripts/graded_toys.py` but nothing is imported. `F_q` sits in `F_{q^k}` as
   the constants, which is how `E(F_q) <= E(F_{q^k})`. Frobenius is `a -> a^q` coordinatewise.
3. **Closed points and divisors.** A closed point of degree `k` is a Frobenius orbit of size exactly
   `k` in `C(F_{q^k})` (the orbit of `O` has size 1). An effective divisor of degree `n` is a multiset
   of closed points whose degrees sum to `n`, enumerated exhaustively for `n <= 4` and counted by the
   Euler product `prod_P (1-T^{deg P})^{-1}` for `n <= 6`.
4. **Divisor classes.** For a closed point `P` of degree `d` the trace `Tr(P)` (sum of the orbit in
   `E(F_{q^d})`) is used as the class of `P - d P_0` in `Pic^0(K) = E(F_q)`; its `F_q`-rationality is
   **checked**, not assumed (D12). The class of `sum m_i P_i` in `Pic^0` after subtracting `(deg D) P_0`
   is `sum m_i Tr(P_i)`.
5. **`h^0` -- three routes, declared.**
   (i) *Riemann--Roch consequence*, as the brief explicitly permits: at genus one `h^0(D) = deg D` for
   `deg D >= 1`, `h^0(D) = 0` for `deg D < 0`, and for `deg D = 0`, `h^0(D) = 1` iff `D` is principal,
   decided by the group law (`sum m_i = 0` and `sum m_i Tr(P_i) = O`). **This lane used that shortcut**,
   in the function `rr_h0`.
   (ii) *Enumeration*, independent of (i): `#{E >= 0 : E ~ D} = (q^{h^0(D)}-1)/(q-1)`, with the left side
   obtained by exhaustive enumeration and classification (D13). All Riemann--Roch statements of the
   brief are verified against this route as well as against (i), and the two are compared on every
   effective divisor of degree `<= 4` (D14) and on ~150 signed divisors (D15).
   (iii) *Linear algebra* over `F_{q^6}` for `n P_0`, `n = 0..4` (D10, as required): `L(nP_0)` is
   spanned by `{x^i y^j : j in {0,1}, 2i+3j <= n}` since `ord_{P_0} x = -2`, `ord_{P_0} y = -3` and
   every function regular off `P_0` lies in `R = F_q[x,y]/(curve)` -- this spanning inclusion is the one
   structural input taken from the standard description of the affine coordinate ring. Independence is
   then *proved* numerically: a nonzero element of the span has at most `n` zeros, so full column rank
   of its value matrix at more than `n` affine points is a proof of independence.
6. **Canonical divisor.** At genus one `K_C = 0` is used as a divisor (a representative of the
   canonical class, which is principal); `Pic^{g-1} = Pic^0` and the theta divisor is the principal
   class.
7. **Character extension.** A character `chi` of `Pic^0` is extended to `Pic` through the splitting
   `Pic = Pic^0 (x) Z` given by the rational point `P_0`, i.e. `chi([D]) := chi([D - (deg D) P_0])`.
8. **Measure.** `d^x x` is the multiplicative Haar measure `dx/x` on `R_+^x`; `xi(s) = pi^{-s/2}
   Gamma(s/2) zeta(s)`.
9. **Theta section.** mpmath at 40 working digits. `theta` and `psi` are summed directly (never via the
   functional equation) wherever the functional equation is itself under test (D22, D28, D31). In the
   Mellin integral the lower half `(0,1)` is mapped to `(1,oo)` by `x -> 1/x` using
   `theta(1/x) = sqrt x theta(x)` -- verified independently in D22 -- after which the theta-tails are
   quadratured on `(0,1)` (tanh-sinh, integrand vanishing to all orders at the endpoint) and the two
   *elementary* tails `int_1^oo u^{-s/2-1} du = 2/s` and `int_1^oo x^{(s-1)/2-1} dx = -2/(s-1)` are
   taken in closed form, their antiderivatives being verified symbolically in sympy and their limits
   numerically (D23, lines 1125, 1134). Inside `0 < Re s < 1` that expression *is* the integral;
   outside, it is its analytic continuation, and the ledger says which is being used.
10. **Tolerances.** Exact (integer arithmetic, or sympy over `Q`, `Q(i)`, `Q(sqrt 3)`) for everything in
    Sections 1--8: point counts, closed points, divisor counts, the group law, `Pic^0`, `h^0`, the zeta
    and `L` identities, the functional equation, the superdeterminant. Floating point occurs only in
    the theta section, where the assertion threshold is `1e-30` absolute for identities away from a
    zero of `xi` (measured deviations are `1e-40` to `1e-45`), `1e-10` for "numerically zero at a
    truncated zero of `xi`" (measured `3.9e-12` and `5.8e-14` against `|I| ~ 8` elsewhere in the strip),
    `1e-9` for a residue extracted by `eps`-scaling at `eps = 1e-12`, and `1e-6` for the `A -> oo` limit
    of an elementary antiderivative evaluated at `A = 1e200`. No threshold was relaxed to make a claim
    pass; the seven failing checks are the brief's own formulas asserted at the same thresholds at which
    their corrected forms pass.
11. **Naming.** Ledger rows are `D01, D02, ...`; the two curves keep the brief's names `D2` and `D3`.
12. **Determinism.** Seed `20260921` (numpy `default_rng`) for the random associativity triples and the
    random signed divisors; two consecutive runs of the script produce byte-identical output.

---

## Tally

```
CHECKS: 152 passed, 7 failed
```

All seven failures are deliberate: they are the brief's own formulas asserted exactly as written.
Three are `D23` (B4(b)'s `2 xi(s)/(s(s-1))` at `s = 1/2, 0.3, 0.7+0.2i`), two are `D25` (the same
constant at `s = 2, 3`), and two are `D28` (B4(a)'s `theta(x)` where the lattice sum gives
`theta(x^2)`). The corrected forms `2 xi(s)` and `theta(x^2)` pass at the same thresholds in the same
rows.
