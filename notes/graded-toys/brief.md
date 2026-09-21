# Brief: a graded tensor-network realisation of the cusp toys

Author of the brief and of the proofs (`proofs.md`): `claude:fable-5.1`. Numerics lane: `claude:opus`,
blind from this brief. Review lane: `claude:opus`, REFUTE protocol. Date 2026-09-20 (night).

This round works through the four "next" items of `HANDOFF.md` (2026-09-20 evening) and
`obs:elliptic-cavity-next` in `report/sections/04l_elliptic_cavity_channel.tex`:
(i) the cusp-plus-funnel toy by hand, (ii) the genus-two coefficient, (iii) the level tower, (iv) the
arithmetic-metric completion with one exit per zero mode; and it does so through one construction, a
graded tensor network (graded transfer channel in the sense of `def:graded-transfer-channel`,
`report/sections/02h_definitions_graded_ramanujan.tex`) whose bond is the model space of a diagram.
Everything below is stated for the reader who will run numerics against it. Claims are labelled
G1--G7; the numerics lane should test every displayed formula, and the reviewer should try to break
every claim. Where a claim is conditional the hypothesis is named.

## 0. Setting and conventions (fixed; not up for re-derivation)

**Diagram** (`def:elliptic-cavity`, shard 04k). A finite real symmetric core `T_X` (`n x n`), `h`
standard rays attached at vertices `v_a` with couplings `c_a > 0`, `W = (c_a delta_{v, v_a})_{v,a}`,
`C = W W^* = sum_a c_a^2 P_{v_a}`. Spectral parameter `lambda = z + 1/z`, `z = q^{s - 1/2}`, so
`|z| < 1` is `Re s < 1/2`. Resonance polynomial `p(z) = det((1 + z^2) I - z T_X - C)` (monic, degree
`2n`), reversed `ptilde(z) = z^{2n} p(1/z) = det(I - z T_X + z^2 (I - C))`, `ptilde(0) = 1`.
Scattering matrix `S(z) = -Q(z)^{-1} Q(1/z)`, `Q(z) = I - z Gam(z)`, `Gam(z) = W^* (lambda - T_X)^{-1} W`
(`thm:multi-exit-scattering`), `det S = (-1)^h p/ptilde`. For `h = 1`, `R = -p/ptilde` and the modular
convention is `phi = 1/R` (`prop:pure-cusp-scattering`). Resonances: zeros of the reduced `det S`
in `|z| < 1`; visible bound states: its poles there, real, `z = vartheta`.

**Model** (`def:h-exit-renewal-channel`, `thm:h-exit-model`, shard 04l). `Theta = eta S B_bd` inner,
`K = H^2(C^h) ominus Theta H^2(C^h)`, `Z = P_K M_w|_K`, exit map `J : K -> C^h` with
`I - Z^* Z = J^* J`, `Z^m -> 0`, `dim K = deg det Theta = N` (delay modes at `z = 0` included).
Eigenvectors `Z k_n = z_n k_n`, exit amplitudes `a_n = J k_n`, Gram identity
`(1 - conj(z_n) z_m) <k_n, k_m> = a_n^* a_m`. Exit vectors `j_a = J^* e_a in K`.
**Renewal channel with a fixed reset** `Omega` (a density on `K`):
`E_Omega(rho) = Z rho Z^* + Tr(J rho J^*) Omega = Z rho Z^* + sum_a <j_a| rho |j_a> Omega`.
Holding law, mean `tbar`, stationary density `rho_inf = tbar^{-1} sum_{m >= 0} Z^m Omega Z^{*m}`
(`thm:h-exit-renewal`(d)).

**Grading** (`def:cmps-transfer-generators`, `def:graded-transfer-channel`). A bond `H = H_+ (+) H_-`
with parity `P = 1 (+) (-1)`. An operator `A` on `H` is homogeneous of parity `eps` if `P A P = eps A`.
`B(H)` is graded by `Ad(P)`: even = block-diagonal, odd = block-off-diagonal. A channel
`E(rho) = sum_i A_i rho A_i^*` with homogeneous letters commutes with `Ad(P)`; its sector restrictions
are `E_0 = E|_even`, `E_1 = E|_odd`. The doubled transfer matrix is `EE = sum_i A_i (x) conj(A_i)` on
`H (x) H`; `str EE^L = Tr E_0^L - Tr E_1^L = Tr[(P (x) conj P) EE^L]`. Ring vectors of length `L`:
`psi_L = sum_i Tr[A_{i_1} ... A_{i_L}] |i_1 ... i_L>` (untwisted, "antiperiodic" in the vocabulary of
02h) and `psi_L^P = sum_i Tr[P A_{i_1} ... A_{i_L}] |i>` (twisted, "periodic");
`<psi_L|psi_L> = Tr EE^L`, `<psi_L^P|psi_L^P> = str EE^L`. Graded divisor `nu(lambda) = m_0 - m_1`
(algebraic multiplicities in the even minus the odd sector); ring zeta `1/sdet(1 - u EE) =
det(1 - u E_1)/det(1 - u E_0)`.

**Frobenius module.** For a smooth projective curve of genus `g` over `F_q` with function field `K`,
`H = H^0_+ (+) H^1_- (+) H^2_+` of dimensions `1, 2g, 1`, `Fr` with eigenvalues `1; alpha_1, ...,
alpha_{2g}; q`, `|alpha_i| = sqrt q` (Weil), and `alpha -> q/alpha = conj(alpha)` an involution of the
multiset. `P(T) = prod (1 - alpha_i T)`, `zeta_K(s) = P(q^{-s})/((1 - q^{-s})(1 - q^{1-s})) =
1/sdet(1 - q^{-s} Fr)`. Point counts `N_k = 1 + q^k - sum_i alpha_i^k = str Fr^k`. Tate twist
`Fr(-1) := q Fr` (same space, eigenvalues multiplied by `q`, same parities). `Pi` = parity flip
(the same operator with `P` replaced by `-P`). D2: `q = 2`, `P = 1 - 2T + 2T^2`, `alpha = 1 -+ i`;
D3: `q = 3`, `P = 1 + 3T^2`, `alpha = +- i sqrt 3`.

## G1. The diagram's own transfer matrix (linearisation)

Put `M = [[T_X, -(I - C)], [I, 0]]` on `C^n (+) C^n`.

(a) `det(z - M) = p(z)` and `det(1 - z M) = ptilde(z)`. Hence, with multiplicity over `spec M`,
`det S(z) = (-1)^h det(z - M)/det(1 - z M)` and for `h = 1`
`R(z) = - prod_{mu in spec M} (z - mu)/(1 - z mu)`: each unimodular conjugate pair `mu, conj mu`
(cusp forms, thresholds) cancels, each interior `mu` is a zero of `R` (a resonance) and each exterior
`mu = 1/vartheta` gives the bound-state pole at `vartheta`.

(b) `Tr M^m = sum_{roots of p} mu^m` for every `m >= 1`, so the resonance power sums of
`prop:cusp-walk-power-sums` are `Tr M^m` minus the cusp-form, threshold and exterior contributions.

(c) `ker M = 0 (+) ker(I - C)`; for `c = 1` junctions `M` is singular with Jordan blocks of size two at
`0` (one per junction with `c = 1`, when the Schur bracket of `prop:multi-exit-spectrum`(iii) is
invertible): this is the delay sector, `ord_0 p = 2 dim ker(I - C)`, seen on the core.

(d) With `C = 0` and `T_X = A_X/sqrt q` (H-REG), `det(1 - z M_0) = det(I - u A_X + q u^2)`, `u = z/sqrt q`,
so by Ihara--Bass (`cit:ihara-bass-bass` or the notebook's `thm:qihara-general` in the scalar case)
`spec(M_0) cup {+-1 with multiplicity |E| - |V|} = spec(B)/sqrt q` for the Hashimoto operator `B` of the
core. Thus `M = M_0 + [[0, C], [0, 0]]`: the diagram's transfer matrix is the core's non-backtracking
operator plus a rank-`h` correction supported on the junctions, and the two branches of the ray
self-energy are the two determinants: bound sheet `det(1 - z M)`, outgoing sheet `det(z - M)`.

(e) What `M` is not: `M` is real, so `Tr M^m` carries the resonances with a plus sign, and `R` is the
ratio of the characteristic polynomial of `M` to its reversal, not a superdeterminant of `M` in one
variable. The grading of the resonances is not visible on the core; it is visible on the arithmetic
side (G2), and it is imposed on the model side (G3).

## G2. The scattering matrix is a superdeterminant of Frobenius

(a) For every curve of genus `g` over `F_q`, with `w = q^{-2s}`,

    zeta_K(2s - 1)/zeta_K(2s) = sdet(1 - w E_S),      E_S := Fr (+) Pi Fr(-1)   on   H (+) H,

`dim = 4g + 4`; explicitly `sdet(1 - w E_S) = (1 - w) P(q w) / ((1 - q^2 w) P(w))`. Even eigenvalues of
`E_S`: `1, q` (from `Fr` on `H^0, H^2`) and `q alpha_i` (from `Fr(-1)` on `H^1`, flipped to even); odd:
`alpha_i` (from `Fr` on `H^1`) and `q, q^2` (from `Fr(-1)` on `H^0, H^2`, flipped to odd). The two lines
with eigenvalue `q` cancel in the superdeterminant.

(b) Under `w = 1/(q z^2)` (i.e. `z^2 = e/q` for an eigenvalue `e`), the eigenvalues with `|e| < q` are
exactly those whose `z`-images lie inside the unit disc: even `e = 1` (`z = +- q^{-1/2}`) and odd
`e = alpha_i` (`z^2 = alpha_i/q`, `|z| = q^{-1/4}`); every other eigenvalue (`q alpha_i`, `q^2`) has
`|e| > q`. So the disc part of the graded divisor of `E_S` is `nu(1) = +1` and `nu(alpha_i) = -1`:
the pole is even and the zeros are odd, with the parities being cohomological degrees mod 2 and the
Tate-twisted copy carrying the flipped parity. No choice is made.

(c) For D2 (`thm:d2-zeta`, conditional on `asm:h-diag`) and for the zeta channel of D3
(`thm:d3-channels`): `1/R(z) = z^{-2} sdet(1 - E_S/(q z^2))`. Hence on these diagrams the visible bound
states (the Perron pair, the pole) are the even disc eigenvalue and the resonances are the odd disc
eigenvalues of `E_S`; the resonances are on `|z| = q^{-1/4}` iff the odd disc eigenvalues of `E_S` are on
`|e| = sqrt q` (Weil). The delay modes are the prefactor `z^{-2}`, which is a cut artefact
(`prop:multi-exit-spectrum`(iii)), not part of the divisor of `E_S`.

(d) Functional equation. Poincare duality is a graded similarity `Fr ~ q Fr^{-1}` (exchanging `H^0` and
`H^2`, preserving `H^1`); it gives `E_S ~ Pi (q^2 E_S^{-1})` and

    sdet(1 - w E_S) . sdet(1 - E_S/(q^2 w)) = q^{2g - 2},

which under `w -> 1/(q^2 w)`, i.e. `z -> 1/z`, is `R(z) R(1/z) = 1` once the prefactor of (e) is included.

(e) Genus `g`, one cusp (item (ii) of the handoff; H-EIS resolved under a structural hypothesis).
Suppose a one-cusp diagram with a single `c = 1` junction, cut at the junction, has: the Perron pair
`+- q^{-1/2}` as its only visible bound states, resonances exactly the `4g` square roots
`z^2 = alpha_i/q`, and every other root of `p` self-reciprocal (cusp forms, thresholds). Then
necessarily

    1/R(z) = z^{-2} q^{1-g} zeta_K(2s - 1)/zeta_K(2s),       [z^2] p = -q^{1-g},

and the reviewer's formula `|[z^m] p| = q^{1 - g - (h-1)(g-1)}` of `prop:nonzero-root-product` at `h = 1`
is a consequence of `ord_0 p = 2` (one `c = 1` junction) and the product identity. The alternative
prefactor `q^{1 - 2gs} = z^{-2g} q^{1-g}` of `thm:d2-zeta` would force `ord_0 p = 2g`, contradicting
`ord_0 p = 2 dim ker(I - C) = 2` for every genus; so H-EIS is `q^{1-g} z^{-2}` at the junction cut.
Contrapositive, the testable statement for a genus-two diagram: `[z^2] p != -q^{-1}` implies extra
non-self-reciprocal roots (visible bound states beyond the Perron pair, or resonances off the Weil
circle). Nothing here builds a genus-two diagram; the quotient graph is not in the repository.

## G3. The graded MPS of the renewal channel; ring norms; the odd sector is the resonances

Let `(Z, J)` be any finite `h`-exit contraction (H-CONTRACTION: `Z^m -> 0`, `I - Z^*Z = J^*J`) and
`Omega = sum_k p_k |omega_k><omega_k|` a density on `K` (spectral decomposition, `p_k > 0`). Bond
`H = C vac (+) K`, `P = 1 (+) (-1)`. Letters:

    A_0 = 1 (+) Z,        A_{(a,k)} = sqrt(p_k) |omega_k><j_a|,   a = 1..h,

all even (`vac` is never touched; `omega_k, j_a in K`).

(a) `sum_i A_i^* A_i = 1` (the MPS is normalised; equivalently the channel is trace preserving), and
`EE = sum_i A_i (x) conj(A_i)` is the graded renewal channel of `def:cusp-renewal-channel` /
`thm:h-exit-renewal`(e) on `B(H)`, `EE` commutes with `P (x) conj P`.

(b) `E_0` (block-diagonal operators) is the direct sum of the vacuum line (eigenvalue `1`, fixed vector
`|vac><vac|`) and `E_Omega` on `B(K)` (eigenvalue `1` on `rho_inf`, the secular roots of
`det(1 - u E_Omega) = det(1 - u E_0^K)(1 - mhat_Omega(u))` otherwise). `E_1` (block-off-diagonal) is
`span{|k><vac|, |vac><k| : k in K}` and `EE` acts there as `Z (x) 1` and `1 (x) conj Z`: its
eigenvalues are `z_n` and `conj z_n` with the Jordan structure of `Z` (this is
`prop:cusp-odd-protected` in the tensor-network picture; the exit functional vanishes on odd operators).

(c) Ring norms. `Tr EE^L = 1 + Tr E_Omega^L + 2 Re Tr Z^L` and `str EE^L = 1 + Tr E_Omega^L - 2 Re Tr Z^L`,
so `<psi_L|psi_L> - <psi_L^P|psi_L^P> = 4 Re Tr Z^L = 4 Re sum_n z_n^L` (with multiplicity; Jordan
blocks contribute their power sums). The resonance power sums of `prop:cusp-walk-power-sums` are the
difference of the two closures of the tensor network. For D2 (six-dimensional `K`, delay block
nilpotent): `Tr Z^L = 0` for odd `L`, and for `L = 2k`

    Tr Z^{2k} = 2 q^{-k} (alpha_+^k + alpha_-^k) = 2 q^{-k} (1 + q^k - N_k(E)),

the odd half of the point count of the curve, exactly (`N_1 = 1, N_2 = 5, N_3 = 13, N_4 = 25, ...`
for `y^2 + y = x^3 + x + 1` over `F_2`; the numerics lane should compute `N_k` by counting points
and compare).

(d) Graded divisor and ring zeta of the toy: `nu(1) = 2` (the vacuum and `rho_inf`, both even),
`nu(z_n) = nu(conj z_n) = -m_n` (odd, `m_n` the multiplicity), `nu(lambda) = +1` at each secular root;
`1/sdet(1 - u EE) = prod_n (1 - u z_n)^{m_n} (1 - u conj z_n)^{m_n} / ((1 - u)^2 prod_sec (1 - u lambda))`.
The zeros of the toy's ring zeta are the resonances and their conjugates; the poles are the two
fixed points and the secular roots.

(e) `RH(Y)` with radius `r` holds iff every odd eigenvalue of `EE` has modulus `r`: the odd sector is
"Ramanujan" (in the sense of `def:graded-quantum-expander`, odd bound `lambda_1 = r` attained by every
odd mode) iff `RH(Y)`. The even sector has the fixed-point segment of `prop:graded-stationary-segment`
(two even fixed points, the vacuum has no exit), so `EE` is not a mixing graded expander: exactly the
"even exit is missing" statement of `obs:cusp-no-graph-vacuum`, now as a property of the tensor network.

## G4. The even exit: what a funnel does, and what the graded network needs instead (item (i))

(a) Constant mode on a diagram with cusps and funnels. Let the diagram (core, cusp rays with
`S(c_{k+1}) = q S(c_k)`, funnel rays with `S(f_{k+1}) = S(f_k)/q`, junction edges) be `(q+1)`-regular at
every vertex, `C_c = sum_{cusps} (S(v)/S(e)) P_v`, `C_f = sum_{funnels} (S(v)/S(e)) P_v`
(`prop:funnel-self-energy`: `p_funnel = det((1 + z^2) - z T_X - C_c - q^{-1} C_f)`). The constant function
`f = 1`, `g = 1/sqrt S`, restricted to the core solves

    [(1 + z^2) I - z T_X - z^2 C_c - q^{-1} C_f] x = 0     at  z = q^{-1/2},

bound-sheet self-energy `c^2 z` on every cusp, outgoing-sheet self-energy `c_f^2/z = (S(v)/S(e))/(q z)`
on every funnel (ray tails `q^{-k/2} = z^k` on cusps and `q^{k/2} = z^{-k}` on funnels). It is a root of
`p_funnel` (outgoing everywhere) iff `C_c = 0` and a root of `ptilde_funnel` (bound everywhere) iff
`C_f = 0`. With both kinds of ray present, `z = q^{-1/2}` is in general neither a resonance nor a
visible bound state and the constant function is neither in `L^2` nor in the model space `K`.

(b) One-vertex regular cusp-plus-funnel diagram: core `[0]`, cusp weight `a = S(v)/S(e_c)`, funnel weight
`b = S(v)/S(e_f)`, `a + b = q + 1`. Then `p = z^2 - (1 + a(q-1))/q`: the Perron root is at `z^2 = 1/q`
(a resonance at `q^{-1/2}`) iff `a = 0` (pure funnel, APW's tree), at `z^2 = q` (bound state at
`q^{-1/2}`) iff `a = q + 1` (pure cusp), and a bound state at `vartheta^2 = q/(1 + a(q-1)) in (1/q, 1)`
for `0 < a < q + 1` except the threshold `a = 1`. A cusp of any weight keeps the constant mode bound.

(c) Bolting a funnel onto D2. Attach a funnel of weight `f > 0` at a core vertex `v` of D2 ("by hand":
regularity is dropped): `p_f = det((1 + z^2) - z T_2 - P_B - (f/q) P_v)`. For every `v` and every
`f > 0` the Hasse--Weil quartet leaves the circle `|z| = 2^{-1/4}` (a rank-one perturbation of a
matrix polynomial with simple roots moves every root at first order unless the residue vanishes; the
numerics lane should compute `d|z_i|/df` at `f = 0` for all six `v` and report whether any vanishes),
and the Perron pair moves inward without reaching `q^{-1/2}` for finite `f`. The arithmetic is not
robust under an extra funnel: "zeros from the cusp, vacuum leak from the funnel" cannot be had on one
connected regular core by adding a funnel to an arithmetic diagram, consistent with
`cit:apw-cusps-pic-no-funnels`.

(d) The glued toy (theorem). Let `(Z_+, J_+)` on `K_+` and `(Z_-, J_-)` on `K_-` be `h_+`- and
`h_-`-exit contractions, `K = K_+ (+) K_-` with `P = 1 (+) (-1)`, `Z = Z_+ (+) Z_-`,
`J = J_+ (+) J_- : K -> C^{h_+} (+) C^{h_-}` (one exit block per sector), and `Omega = Omega_+ (+) Omega_-`
an even density with `Tr Omega_+ > 0`, `Tr Omega_- > 0`. Then:
  (i) the letters `A_0 = Z` and `A_{(a,k)} = sqrt(p_k) |omega_k><j_a|` are homogeneous, of parity
  `eps(omega_k) eps(j_a)`; the cross letters (an exit of one sector reset into the other sector) are
  odd. `EE` is a trace-preserving graded transfer channel.
  (ii) `EE` has a unique stationary density, `rho_inf = tbar^{-1} sum_m Z^m Omega Z^{*m}`, which is even
  and populates both sectors (mixed); it attracts every density iff the holding law is aperiodic.
  (iii) If instead the reset is sector-preserving (`R(X) = Tr(X_{++}) Omega'_+ + Tr(X_{--}) Omega'_-`,
  all letters even), each sector carries its own stationary density and the stationary densities form
  a segment: a unique mixed stationary state on the graded bond requires an odd letter.
  (iv) For eigenvectors `k_n in K_-`, `k_m in K_+`, the odd coherences `|k_n><k_m|` and `|k_m><k_n|` are
  eigen-operators of `EE` with eigenvalues `z_n conj(z_m)` and `z_m conj(z_n)` for every fixed reset,
  because `Tr(J |k_n><k_m| J^*) = <a_m, a_n> = 0` (different exit blocks). Under `RH(Y_+)` with radius
  `r_+` and `RH(Y_-)` with radius `r_-` every odd eigenvalue has modulus `r_+ r_-`: rates add.
  (v) Instance ("funnel-glued D2"): `K_+` = the model space of APW's tree, the one-vertex core `[0]`
  with one funnel of weight `q + 1` (as a one-exit diagram: `c_+^2 = (q+1)/q`, `p_+ = z^2 - 1/q`,
  `R_+ = -(z^2 - q^{-1})/(1 - z^2/q)`, no bound states, `Theta_+ = -R_+`, `dim K_+ = 2`, eigenvalues
  `+- q^{-1/2}`); `K_-` = the six-dimensional model space of D2 (`thm:h-exit-model`). With `Omega_+` any
  density on `K_+` and `Omega_-` a modal Hasse--Weil density, the odd eigenvalues of `EE` are
  `+- q^{-1/2} conj(z_n)` and conjugates, all of modulus `q^{-3/4}` on the Hasse--Weil part and `0` on
  the delay part; the twisted ring norm's odd part is `-2 Re[(Tr Z_-^L) conj(Tr Z_+^L)]` with
  `Tr Z_+^L = q^{-L/2}(1 + (-1)^L)`.
  (vi) Shared exit (the trade-off). If the two sectors exit through a common ray, so that some
  `<a_m, a_n> != 0`, then `|k_n><k_m|` is not an eigen-operator of `EE_Omega`; by the rank-one
  persistence criterion (`prop:rebound-persistence-secular`) the eigenvalue `z_n conj z_m` of `EE_0`
  survives in `EE_Omega` iff `<a_m, a_n> . dual_{nm}(Omega) = 0`. By the Gram identity
  `<a_m, a_n> = (1 - conj(z_m) z_n) <k_m, k_n>`, so protection of the odd coherences is equivalent to
  energy-orthogonality of the two sectors' modes: on a connected core with a shared exit the zeros are
  not protected once the even mode leaks. The numerics lane should exhibit the shift on a random
  three-vertex core with one cusp, six resonances, graded by fiat (two modes even, four odd).

Conclusion for item (i): the answer is negative on one connected regular diagram (a--c) and positive
for a tensor network with two exit blocks and a parity-crossing (odd-letter) rebound (d); the object
with "pole even, zeros odd, unique mixed stationary state" is not a graph of groups but a graded
bond gluing an even funnel diagram to an odd cusp diagram through the rebound.

## G5. The arithmetic metric is the Frobenius channel; no self-adjoint diagram realises it (item (iv))

On `K_HW` of D2 with the symmetric arithmetic metric of `thm:arithmetic-metric`, `Z = r U`,
`r = q^{-1/4}`, `U` unitary, and `U^2 ~ (Fr/sqrt q)^{-1} (x) 1_2` (from `Z^2 ~ Fr^{-1} (x) 1_2`).

(a) With one exit per mode, `J' = sqrt(1 - r^2) 1_{K_HW}` (`h = 4`, `I - Z^{*'} Z = J'^* J'` holds in the
arithmetic metric), the renewal channel with a fixed reset `Omega` is

    EE'(rho) = r^2 U rho U^* + (1 - r^2) Tr(rho) Omega .

It is CPTP, its unique stationary density is `rho_inf = (1 - r^2) sum_m r^{2m} U^m Omega U^{*m}`, and
`rho_inf = Omega` iff `[Omega, U] = 0` (every modal reset is stationary: the arithmetic-metric form of
`prop:cusp-modal-rh`). On traceless operators `EE' = r^2 Ad(U)`, so the relaxation spectrum is
`{r^2 e^{i(theta_a - theta_b)}}` (`U = diag(e^{i theta_a})`), every relaxation mode of modulus exactly
`r^2 = q^{-1/2}`: a mixing quantum expander with a single gap, `lambda_0 = q^{-1/2}` (and, with the
vacuum adjoined as in G3, `lambda_1 = r = q^{-1/4}`). This is "RH = the compressed operator is
`q^{-1/4}` times a unitary" made into a channel; the uniform gap is built in by the metric, it is
not derived.

(b) The characteristic function of `Z'^* = r U^*` with this defect is diagonal in the mode basis:
`Theta'(z) = (1 - z r U^*)^{-1}(z - r U) = diag(b_{z_a}(z))`, `b_a(z) = (z - z_a)/(1 - conj(z_a) z)`:
the `a`-th exit sees the single mode `z_a`.

(c) No self-adjoint diagram has a diagonal `Theta` with non-real entries: for a real symmetric (or even
complex Hermitian) core with standard rays, `Gam(z)_{ab} = sum_i c_a c_b x_i(v_a) conj(x_i(v_b))/(lambda - t_i)`
has Hermitian coefficient matrices and real poles, so for every constant exit direction `e in C^h`,
`e^* S(conj z) e = conj(e^* S(z) e)`: the resonances visible in one exit direction are closed under
conjugation. The finest exit splitting of D2's quartet by a self-adjoint diagram is into conjugate
pairs `{a, conj a}`, `{-a, -conj a}` (two exits). The object that sees the four modes separately is not
a wave equation on a graph; it is the Frobenius module itself (`E_S` of G2, one line per eigenvalue),
or a non-self-adjoint core.

(d) The bipartite sign `eps` (`eps Z eps = -Z`) and complex conjugation act on the four modes as a
Klein four-group, transitively; the symmetric ray of `thm:arithmetic-metric` is the unique metric
invariant under both, and in it the four one-mode exits are permuted by this group: the odd-sector
analogue of D3's Klein-symmetric four-cusp hedgehog (`thm:d3-channels`).

## G6. The level tower (item (iii)): a correction, and the graded bond of a character channel

(a) Correction to the target. For `Gamma_0(N)` with trivial nebentypus and `N` squarefree (number field
case), every Eisenstein series is old: the `2^{omega(N)}` series `E(dz, s)`, `d | N`, span the
Eisenstein space, so every entry of the scattering matrix is a rational function of `p^{-s}`, `p | N`,
times `xi(2s-1)/xi(2s)`; the scattering determinant is `(xi(2s-1)/xi(2s))^{#cusps}` times a rational
function and contains no Dirichlet `L`-function. `cit:kk-level-constant-term` is the function-field
instance at one cusp. Dirichlet `L`-functions enter the scattering matrix of `Gamma_1(N)`, or of
`Gamma_0(N)` with a nontrivial nebentypus `chi mod N`, where the Eisenstein series `E(z, s; chi_1, chi_2)`
with `chi_1 chi_2 = chi` have constant terms with ratios `L(2s-1, psi)/L(2s, psi)` for characters `psi`
built from `(chi_1, chi_2)`. The honest "cusp per prime with `L`-functions" is therefore the
`Gamma_1(N)` tower (equivalently `Gamma_0(N)` with all nebentypus characters), whose diamond
operators carry `(Z/N)^x`; `conj:galois-graded-bond` should be read there. Over `F_q[T]` the same
applies with Dirichlet characters of `(F_q[T]/N)^x`. No source in the repository states the
function-field `Gamma_1(N)` scattering matrix (H-ARITH stays open); this item is a conditional analysis,
flagged as such.

(b) Character channel (conditional on H-ARITH in the form: the `psi`-channel of the scattering matrix is
a monomial times `L(2s-1, psi)/L(2s, psi)`). For a nontrivial primitive Dirichlet character `psi` mod `N`
over `F_q[T]`, `L(u, psi) = sum_{f monic} psi(f) u^{deg f} = det(1 - u Fr_psi)` is a polynomial of degree
`deg N - 1`, with the factor `(1 - u)` split off when `psi` is even (trivial on `F_q^x`); its nontrivial
roots have `|beta| = sqrt q` (Weil). Put `E_psi = (Fr_psi)_- (+) Pi (Fr_psi(-1)) = (Fr_psi)_- (+) (q Fr_psi)_+`.
Then `L(2s-1, psi)/L(2s, psi) = sdet(1 - w E_psi)`, `w = q^{-2s}`, and the disc part of its graded
divisor is odd only: `nu(beta_i) = -1`, no even disc eigenvalue. The trivial character carries
`zeta_{F_q(T)}(2s-1)/zeta_{F_q(T)}(2s) = sdet(1 - w E_S)` with `g = 0`: only the even `1`. So the level-`N`
graded bond (disc part) is

    (1)_+  (+)  (+)_{psi != 1} (beta_{psi, 1}, ..., beta_{psi, d_psi})_- ,

one even vacuum line from the trivial character and only odd modes, the `L`-zeros, from the others,
with the diamond operators `<a>` acting on the `psi`-block by `psi(a)`: over `F_q(T)` (genus zero) all
zeros live in the level tower. The numerics lane should compute `L(u, psi)` for every character `psi`
mod `N` for `q = 3`, `N = T^3 - T - 1` (irreducible, `(F_27)^x` cyclic of order 26) and `N = T(T^2 + 1)`
(composite, `(F_3)^x x (F_9)^x`), verify the degrees and `|beta| = sqrt 3`, list the graded bond, and
verify `L(2s-1, psi)/L(2s, psi) = sdet(1 - w E_psi)` symbolically.

## G7. Summary of the four items

(i) G4: negative on one connected regular diagram, positive as a glued graded network with odd letters.
(ii) G2(e): the coefficient `-q^{1-g}` and the prefactor `q^{1-g} z^{-2}` are forced by the structural
hypothesis; a genus-two diagram tests the hypothesis, not the formula; no diagram is built.
(iii) G6: `Gamma_0(N)` with trivial character sees only `zeta`; the `L`-zeros live on `Gamma_1(N)`; the
graded bond per character is odd-only, the vacuum is in the trivial channel alone.
(iv) G5: the arithmetic-metric completion is the Frobenius channel `r^2 Ad(U) + (1 - r^2) Omega Tr`, a
one-gap quantum expander with diagonal characteristic function; no self-adjoint diagram realises it;
its "four cusps" are the Frobenius eigenlines permuted by the Klein group of parity and conjugation.

## What the numerics lane must do (blind; do not read `proofs.md`)

Write `scripts/graded_toys.py` (deterministic, seed `20260920`, every claim an assertion with a stated
tolerance, tally printed at the end, runtime under `60 s`, stdlib + numpy + mpmath + sympy only) and
`notes/graded-toys/numerics.md` (a ledger, one row per finding, with the file and line of the assertion).
Build D2 from `def:elliptic-cavity` and `prop:stabiliser-normalisation` (shard 04k), the model space by
the companion construction (the header of `scripts/elliptic_cavity.py` documents the conventions; you
may read it, but re-implement), and do not import anything from `scripts/elliptic_cavity.py`.
Checks, in order: G1(a--d) on D2, D3 and five random cores with one to three cusps (exact rational
arithmetic where possible); G2(a,b,d) symbolically for genus `1` (D2, D3 data) and for a synthetic
genus-two Weil polynomial (`q = 3`, `P = (1 + 3T^2)(1 - 2T + 3T^2)`), and G2(c) on D2 and D3 numerically
at eight points; G2(e): the prefactor and `[z^2] p` on D2 and D3 against the formula; G3(a--e) on D2
with a modal Hasse--Weil reset and with a random reset, including the point counts `N_k` of
`y^2 + y = x^3 + x + 1` over `F_{2^k}` by direct enumeration for `k = 1..5`; G4(a) on D2 with its cusp
replaced by a funnel and with a funnel added at each vertex (report the root motions), G4(b) exactly,
G4(c) the derivatives `d|z_i|/df` at `f = 0` for all six vertices, G4(d)(i--v) on the funnel-glued D2
(uniqueness by the eigenvalue count at `1`, mixedness, parity of the letters, the odd eigenvalues,
the twisted ring norm identity), G4(d)(iii) the segment for a sector-preserving reset, G4(d)(vi) the
shift on a random three-vertex core; G5(a--b) on `K_HW` of D2 in the symmetric arithmetic metric
(`prop:d2-modal-gram`, `thm:arithmetic-metric`), G5(c) numerically: for D2 with two exits (cusp at `B`
and a second cusp at each other vertex in turn) check that no constant exit direction sees a
non-conjugation-closed set of resonances; G6(b) as specified. Report every discrepancy as a finding,
not as a silent tolerance change.
