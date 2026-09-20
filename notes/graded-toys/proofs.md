# Proofs: a graded tensor-network realisation of the cusp toys

Author: `claude:fable-5.1`. Brief: `notes/graded-toys/brief.md` (claims G1--G7). Numerics lane
(blind): `notes/graded-toys/numerics.md`, `scripts/graded_toys.py`. Review: `notes/reviews/graded-toys-2026-09-20.md`.
Conventions are those of Section 0 of the brief; labels `def:`, `thm:`, `prop:` refer to
`db/claims.tsv` and the shards named there. Every statement below is either proved here from the
registered results it names, or marked as conditional on a named hypothesis. A correction ledger
against the brief is at the end.

## G1. The diagram's own transfer matrix

**Theorem G1.** Let `M = [[T_X, -(I - C)], [I, 0]]` on `C^n (+) C^n`.

(a) `det(z - M) = p(z)` and `det(1 - z M) = ptilde(z)`. For `h = 1`,
`R(z) = - prod_{mu in spec M} (z - mu)/(1 - z mu)` with algebraic multiplicities; a unimodular
conjugate pair contributes `1`, an interior eigenvalue contributes a zero of `R` at `mu`, and an
exterior eigenvalue `mu = 1/vartheta` contributes the bound-state pole at `vartheta`.

(b) `Tr M^m = sum_{p(mu) = 0} mu^m` for all `m >= 1`.

(c) `ker M = 0 (+) ker(I - C)`. If the Schur bracket of `prop:multi-exit-spectrum`(iii) is invertible,
`M` has exactly `dim ker(I - C)` Jordan blocks at `0`, each of size two.

(d) If `C = 0` and `T_X = A_X/sqrt q` with `A_X` the adjacency matrix of a `(q+1)`-regular graph, then
`det(1 - z M_0) = det(I - u A_X + q u^2)`, `u = z/sqrt q`, hence by Ihara--Bass
`spec(sqrt q M_0) cup {+-1}^{|E| - |V|} = spec(B)` (multisets), `B` the Hashimoto operator. In general
`M = M_0 + [[0, C], [0, 0]]`.

*Proof.* (a) Block elimination with the invertible lower-right block `z`, valid for `z != 0` and then
for all `z` by polynomial identity:
`det(z - M) = det [[z - T_X, I - C], [-I, z]] = det(z) det((z - T_X) + (I - C) z^{-1}) = det(z^2 - z T_X + I - C) = p(z)`,
and `det(1 - z M) = det [[I - z T_X, z(I - C)], [-z I, I]] = det(I - z T_X + z^2 (I - C)) = ptilde(z)`,
which is `z^{2n} p(1/z)` by inspection. `R = -p/ptilde` (`prop:cusp-reflection`) gives the product; `M`
is real so `spec M` is closed under conjugation; for `|mu| = 1`,
`(z - mu)(z - conj mu)/((1 - z mu)(1 - z conj mu)) = (z^2 - 2 Re(mu) z + 1)/(1 - 2 Re(mu) z + z^2) = 1`;
for `mu = 1/vartheta`, `(z - 1/vartheta)/(1 - z/vartheta) = -(1 - vartheta z)/(vartheta - z)` has its
pole at `vartheta`; an interior `mu` gives the factor `(z - mu)/(1 - z mu)` with pole at `1/mu` outside.
(b) Newton's identities for the characteristic polynomial `p`. (c) `M(x, y) = (T_X x - (I - C) y, x) = 0`
forces `x = 0` and `(I - C) y = 0`. The algebraic multiplicity of `0` is `ord_0 p = 2 dim ker(I - C)`
under the invertibility hypothesis (`prop:multi-exit-spectrum`(iii)) and the geometric multiplicity is
`dim ker(I - C)`; a nilpotent part with `k` blocks of total size `2k` and every block of size at least
one has all blocks of size exactly two only if no block has size one, i.e. if `ker M cap ran M` has
dimension `k`; for `(0, y) in ker M`, `(0, y) = M(x', y')` needs `x' = y` and `T_X y = (I - C) y'`, and
the invertible Schur bracket is exactly the solvability of this equation for every `y in ker(I - C)`
(it is the statement that `T_{UV} A_V^{-1} T_{VU} - I_U` is invertible on `U = ker(I - C)`, with
`A_V = I - C` on `V = U^perp`; the two conditions coincide, cf. the Schur elimination in
`prop:multi-exit-spectrum`). (d) `det(I - z T_X + z^2) = det(I - u A_X + q u^2)` by substitution;
`det(1 - u B) = (1 - u^2)^{|E| - |V|} det(I - u A_X + q u^2)` is Bass's theorem (the scalar case of
`thm:qihara-general`); comparing linear factors gives the multiset identity. The decomposition of `M`
is `-(I - C) = -I + C`. QED.

*Remark (G1(e)).* `M` is real, so the resonances enter `Tr M^m` with a plus sign; `R` is the ratio of the
characteristic polynomial of `M` to its reversal. There is no grading of `M` in one variable whose
superdeterminant is `R`: `det(z - M)` and `det(1 - z M)` are evaluated at reciprocal arguments. The
grading of the resonances is a fact about the arithmetic side (G2) and is imposed on the model side (G3).

## G2. The scattering matrix as a superdeterminant of Frobenius

Notation: `H = H^0_+ (+) H^1_- (+) H^2_+`, `Fr` with eigenvalues `1; alpha_1..alpha_{2g}; q`,
`P(T) = prod_i (1 - alpha_i T)`, `zeta_K(s) = P(q^{-s})/((1 - q^{-s})(1 - q^{1-s}))`. `Fr(-1) = q Fr` on
the same graded space; `Pi X` is `X` with the parities reversed. `E_S := Fr (+) Pi Fr(-1)` on `H (+) H`.

**Theorem G2.** (a) With `w = q^{-2s}`,
`zeta_K(2s - 1)/zeta_K(2s) = sdet(1 - w E_S) = (1 - w) P(q w)/((1 - q^2 w) P(w))`.
(b) The eigenvalues `e` of `E_S` with `|e| < q` are `1` (even) and `alpha_1, ..., alpha_{2g}` (odd); the
two eigenvalues equal to `q` (one even, from `Fr` on `H^2`; one odd, from `Fr(-1)` on `H^0`) cancel;
all others (`q alpha_i` even, `q^2` odd) have `|e| > q`.
(d) `sdet(1 - w E_S) . sdet(1 - E_S/(q^2 w)) = q^{2g - 2}`.

*Proof.* (a) The even part of `E_S` is `Fr|_{H^0 (+) H^2}` together with the odd part of `Fr(-1)`, i.e.
`Fr(-1)|_{H^1}`: eigenvalues `1, q, q alpha_1, ..., q alpha_{2g}`. The odd part is `Fr|_{H^1}` together
with `Fr(-1)|_{H^0 (+) H^2}`: eigenvalues `alpha_1, ..., alpha_{2g}, q, q^2`. Hence
`sdet(1 - w E_S) = (1 - w)(1 - q w) P(q w) / (P(w)(1 - q w)(1 - q^2 w)) = (1 - w) P(q w)/((1 - q^2 w) P(w))`.
On the other side `zeta_K(2s) = P(w)/((1 - w)(1 - q w))` and
`zeta_K(2s - 1) = P(q w)/((1 - q w)(1 - q^2 w))` since `q^{-(2s-1)} = q w`; the ratio is the same
expression. (b) `|alpha_i| = sqrt q < q` for `q >= 2`; `|q alpha_i| = q^{3/2} > q`; `|q^2| > q`; and the
eigenvalue `1`. (d) Write `F(w) = (1 - w) P(q w)/((1 - q^2 w) P(w))`. The functional equation of the
Weil polynomial, `P(T) = q^g T^{2g} P(1/(q T))` (from `alpha_i -> q/alpha_i`), gives
`P(1/(q w)) = P(w)/(q^g w^{2g})` and `P(1/(q^2 w)) = P(q w)/(q^g (q w)^{2g})`. Then
`F(1/(q^2 w)) = [(q^2 w - 1)/(q^2 w)] [P(w)/(q^g w^{2g})] [w/(w - 1)] [q^g (q w)^{2g}/P(q w)]
= q^{2g - 2} (1 - q^2 w) P(w) / ((1 - w) P(q w)) = q^{2g - 2}/F(w)`. QED.

**Proposition G2(c).** Under `asm:h-diag`, for D2 (`thm:d2-zeta`) and for the zeta channel of D3
(`thm:d3-channels`), `1/R(z) = z^{-2} sdet(1 - E_S/(q z^2))`; the visible bound states are the even
disc eigenvalue `e = 1` (`z^2 = e/q = 1/q`) and the resonances are the odd disc eigenvalues
`e = alpha_i` (`z^2 = alpha_i/q`).

*Proof.* `z = q^{s - 1/2}` gives `w = q^{-2s} = 1/(q z^2)`. `thm:d2-zeta` states
`1/R_2 = z^{-2} zeta_K(2s-1)/zeta_K(2s)`; `thm:d3-channels` states `R_3 = det S_e = z^2 zeta_K(2s)/zeta_K(2s-1)`;
apply G2(a). The zeros of `1/R` in the disc are the poles of `R`, the visible bound states
(`prop:multi-exit-spectrum`(i)), and come from the even factor `(1 - w)`, i.e. `z^2 = 1/q`; the poles
of `1/R` in the disc are the resonances and come from the odd factor `P(w)`, i.e. `w = 1/alpha_i`,
`z^2 = alpha_i/q`. The prefactor `z^{-2}` carries the two delay modes (`prop:multi-exit-spectrum`(iii)).
QED.

**Proposition G2(e) (genus `g`, one cusp).** Let a one-cusp diagram have a single junction with
`c = 1`, cut at the junction, and suppose: the visible bound states are exactly the Perron pair
`vartheta = +- q^{-1/2}`; the resonances are exactly the `4g` numbers with `z^2 in {alpha_i/q}`, each
simple; every other root of `p` lies on the unit circle. Let `D(z)` be the monic product of the
unimodular root factors and `s_D = D(0) = (-1)^{m_{+1}}`, `m_{+1}` the multiplicity of the root
`z = +1`. Then
`1/R(z) = s_D z^{-2} q^{1 - g} zeta_K(2s - 1)/zeta_K(2s)` and `[z^2] p = -s_D q^{1 - g}`.
In particular the prefactor `q^{1 - 2gs} = z^{-2g} q^{1-g}` considered in `thm:d2-zeta` is excluded for
`g >= 2`.

*Proof.* By hypothesis and `prop:multi-exit-spectrum`(iii) (`ord_0 p = 2`),
`p(z) = z^2 . prod_{i=1}^{2g} (z^2 - alpha_i/q) . (z^2 - q) . D(z)`, monic, degree `2n = 4g + 4 + deg D`.
Since `D` is real with unimodular roots closed under conjugation, `z^{deg D} D(1/z) = D(0) D(z)` with
`D(0) = prod(-mu) = (-1)^{m_{+1}}` (conjugate pairs contribute `1`, `mu = -1` contributes `1`, `mu = 1`
contributes `-1`). Hence
`ptilde(z) = z^{2n} p(1/z) = prod_i (1 - alpha_i z^2/q) (1 - q z^2) s_D D(z)`, and indeed
`ptilde(0) = s_D^2 = 1`. The common factor `D` cancels in `R = -p/ptilde`. Substitute
`z^2 = 1/(q w)`: `z^2 - alpha_i/q = (1 - alpha_i w)/(q w)`, so `prod_i = P(w)/(q w)^{2g}`;
`z^2 - q = (1 - q^2 w)/(q w)`; `1 - alpha_i z^2/q = (q^2 w - alpha_i)/(q^2 w)`, so
`prod_i = prod_i(-alpha_i) prod_i (1 - q^2 w/alpha_i)/(q^2 w)^{2g} = q^g P(q w)/(q^2 w)^{2g}` using
`prod alpha_i = q^g` and `q/alpha_i = conj alpha_i`, a permutation of the roots; `1 - q z^2 = (w - 1)/w`.
Collecting,
`R = -(1/(q w)) [P(w)/(q w)^{2g}] [(1 - q^2 w)/(q w)] (q^2 w)^{2g} w / (s_D q^g P(q w)(w - 1))
= s_D q^{g - 2} w^{-1} (1 - q^2 w) P(w)/((1 - w) P(q w)) = s_D q^{g - 1} z^2 / F(1/(q z^2))`,
with `F` as in G2(d). So `1/R = s_D q^{1 - g} z^{-2} F(1/(q z^2))`, which is the claim by G2(a).
The coefficient: `[z^2] p = prod_i (-alpha_i/q) . (-q) . D(0) = -s_D q^{1 - g}`. Finally, a prefactor
`z^{-2g}` would give `ord_0 R = 2g`, but `ord_0 R = ord_0 p = 2 dim ker(I - C) = 2` for one `c = 1`
junction cut at the junction (`prop:multi-exit-spectrum`(iii)); this is independent of `g`. QED.

*Remarks.* (1) For D2 and D3 (`g = 1`, `s_D = 1`) this is `thm:d2-zeta` and `thm:d3-channels`. The
brief omitted `s_D`; it is `+1` unless the threshold `z = +1` occurs with odd multiplicity. (2) The
reviewer's formula `|[z^m] p| = q^{1 - g - (h-1)(g-1)}` in `prop:nonzero-root-product` reduces at
`h = 1` to `q^{1 - g}`, which is the product identity under the structural hypothesis; the content of a
genus-two computation is whether the hypothesis holds (no visible bound states beyond the Perron pair
and no resonances off the circle), not the formula. (3) Nothing here constructs a genus-two diagram.

## G3. The graded MPS of the renewal channel

**Theorem G3.** Let `(Z, J)` be a finite `h`-exit contraction with `Z^m -> 0`, `I - Z^* Z = J^* J`, let
`Omega = sum_k p_k |omega_k><omega_k|` (`p_k > 0`) be a density on `K`, `H = C vac (+) K`,
`P = 1 (+) (-1)`, and let the letters be `A_0 = 1 (+) Z`, `A_{(a,k)} = sqrt(p_k) |omega_k><j_a|`,
`j_a = J^* e_a`.

(a) `sum_i A_i^* A_i = 1`; `E(rho) = sum_i A_i rho A_i^* = (1 (+) Z) rho (1 (+) Z)^* + sum_a <j_a|rho|j_a> Omega`
is the graded renewal channel of `thm:h-exit-renewal`(e) with the fixed reset `Omega`; every letter is
even and `E` commutes with `Ad(P)`.

(b) On the even sector (block-diagonal `rho = rho_vv |vac><vac| (+) rho_K`), `E` acts as
`rho_vv (+) E_Omega(rho_K)`. On the odd sector, `E(|k><vac|) = |Z k><vac|` and
`E(|vac><k|) = |vac><Z k|`; hence the odd eigenvalues are the `z_n` and `conj z_n` with the Jordan
structure of `Z`, and the reset does not act on the odd sector.

(c) `Tr EE^L = <psi_L|psi_L> = 1 + Tr E_Omega^L + 2 Re Tr Z^L` and
`str EE^L = <psi_L^P|psi_L^P> = 1 + Tr E_Omega^L - 2 Re Tr Z^L`, where `EE = sum_i A_i (x) conj A_i`.
For D2, `Tr Z^L = 0` for odd `L` and `Tr Z^{2k} = 2 q^{-k}(alpha_+^k + alpha_-^k) = 2 q^{-k}(1 + q^k - N_k)`.

(d) The graded divisor of `EE`: `nu(1) = 2` (both even: `|vac><vac|` and `rho_inf`), `nu(z_n) = nu(conj z_n) = -m_n`
(odd), and `nu(lambda) = m_0(lambda)` at the remaining even eigenvalues, which are the eigenvalues of
`E_Omega` other than `1`; `1/sdet(1 - u EE) = prod_n (1 - u z_n)^{m_n}(1 - u conj z_n)^{m_n} / ((1 - u) det(1 - u E_Omega))`.

(e) `RH(Y)` with radius `r` holds iff every odd eigenvalue of `EE` has modulus `r`. `EE` has two even
fixed points, so it is not a mixing graded quantum expander in the sense of `def:graded-quantum-expander`.

*Proof.* (a) `A_0^* A_0 = 1 (+) Z^* Z` and `sum_{a,k} A_{(a,k)}^* A_{(a,k)} = sum_a |j_a><j_a| sum_k p_k = J^* J`
(`J^* J = sum_a J^* e_a e_a^* J`), so the sum is `1 (+) (Z^* Z + J^* J) = 1`. The channel is
`(1 (+) Z) rho (1 (+) Z)^* + sum_{a,k} p_k |omega_k><j_a| rho |j_a><omega_k|`, which is the displayed form;
this is the definition in `thm:h-exit-renewal` with `R(X) = Tr(X) Omega` and `tilde Z = 1 (+) Z`,
`tilde J = 0 (+) J`. `P A_i P = A_i` since `vac` and `K` are each preserved, so
`Ad(P) E Ad(P) = E`. (b) `(1 (+) Z)(rho_vv (+) rho_K)(1 (+) Z^*) = rho_vv (+) Z rho_K Z^*`, and
`<j_a| rho |j_a>` only sees `rho_K`. For `X = |k><vac|`: `(1 (+) Z) X (1 (+) Z)^* = |Z k><vac|` because
`<vac|(1 (+) Z^*) = <vac|`, and `<j_a|X|j_a> = <j_a|k><vac|j_a> = 0` since `j_a in K`. The map
`|vac><k| -> |vac><Z k|` is `X -> X (1 (+) Z)^*`, whose eigen-operators are `|vac><k_n|` with
eigenvalue `conj z_n` (`<Z k_n| = conj(z_n) <k_n|`). (c) `<psi_L|psi_L> = sum_i |Tr(A_{i_1}...A_{i_L})|^2
= sum_i Tr[(A_{i_1} (x) conj A_{i_1}) ... (A_{i_L} (x) conj A_{i_L})] = Tr EE^L`, and with `P` inserted
`= Tr[(P (x) conj P) EE^L] = Tr E_0^L - Tr E_1^L` because `P (x) conj P` is `+1` on the even and `-1`
on the odd sector (`def:cmps-transfer-generators`) and commutes with `EE`. By (b), `Tr E_0^L = 1 + Tr E_Omega^L`
and `Tr E_1^L = Tr Z^L + conj(Tr Z^L)` (the map `X -> Z^L X` on `{|k><vac|}` has trace `Tr Z^L`; the map
`X -> X Z^{*L}` on `{|vac><k|}` has trace `conj Tr Z^L`). For D2, `Z` has the four Hasse--Weil
eigenvalues `+-(alpha_+/q)^{1/2}, +-(alpha_-/q)^{1/2}` and a nilpotent block (`prop:d2-spectrum-frobenius`,
`prop:d2-canonical-rebound`); odd powers cancel in `+-` pairs; `Tr Z^{2k} = 2[(alpha_+/q)^k + (alpha_-/q)^k]`;
`N_k = 1 + q^k - alpha_+^k - alpha_-^k` is the point count of the curve (`str Fr^k`). (d) Read off (b):
the even spectrum is `{1} cup spec E_Omega`, and `1` is a simple eigenvalue of `E_Omega`
(`thm:cusp-renewal-discrete`(c), `thm:h-exit-renewal`(d)); the odd spectrum is `spec Z cup conj spec Z`.
(e) Immediate from (b); the two even fixed points are `prop:graded-stationary-segment`. QED.

## G4. The even exit

**Proposition G4(a).** Let a diagram with core `T_X`, cusp rays and funnel rays be `(q+1)`-regular at
every vertex in the stabiliser normalisation (`def:elliptic-cavity`; a funnel ray has `S(f_{k+1}) = S(f_k)/q`
and `S(f_k f_{k+1}) = S(f_{k+1})`). Let `C_c = sum_{cusp junctions} (S(v)/S(e)) P_v` and
`C_f = sum_{funnel junctions} (S(v)/S(e)) P_v`. Then the restriction `x` of the constant function
(`g = 1/sqrt S`) to the core satisfies
`[(1 + z^2) I - z T_X - z^2 C_c - q^{-1} C_f] x = 0` at `z = q^{-1/2}`,
with all entries of `x` nonzero. `x` is a null vector of the outgoing matrix
`(1 + z^2) - z T_X - C_c - q^{-1} C_f` at `z = q^{-1/2}` iff `C_c = 0`, and of the bound matrix
`(1 + z^2) - z T_X - z^2 C_c - z^2 q^{-1} C_f` iff `C_f = 0`.

*Proof.* Regularity gives `A 1 = (q + 1) 1`, so `g = 1/sqrt S` satisfies `T g = lambda g` with
`lambda = (q+1)/sqrt q = z + 1/z` at `z = q^{-1/2}`, where `T` is the symmetrised, `sqrt q`-normalised
adjacency (`prop:stabiliser-normalisation`). On a cusp ray, `S(c_1) = q S(e)` (degree condition at
`c_1`) and `S(c_k) = q^{k-1} S(c_1)`, so `g(c_k) = q^{-(k-1)/2} g(c_1) proportional z^k`; the junction
term at `v` is `sqrt(S(v) S(c_1))/(sqrt q S(e)) g(c_1) = c g(c_1)` with `c^2 = S(v)/S(e)`, and
`g(c_1)/g(v) = sqrt(S(v)/S(c_1)) = sqrt(S(v)/(q S(e))) = c z`; so the ray contributes `c^2 z g(v)` (bound
sheet). On a funnel ray the degree condition at `f_1` reads `S(f_1)/S(e) + S(f_1)/S(f_2) = q + 1` with
`S(f_1)/S(f_2) = q`, so `S(f_1) = S(e)`; the normalised ray entries are
`sqrt(S(f_k) S(f_{k+1}))/(sqrt q S(f_{k+1})) = 1` (standard ray), `g(f_k) = q^{(k-1)/2} g(f_1) proportional z^{-k}`
(outgoing), the junction coupling is `c_f^2 = S(v) S(f_1)/(q S(e)^2) = S(v)/(q S(e))`, and
`g(f_1)/g(v) = sqrt(S(v)/S(f_1)) = sqrt(S(v)/S(e)) = sqrt q c_f = c_f/z`; so the ray contributes
`(c_f^2/z) g(v)` (outgoing sheet), in agreement with `prop:funnel-self-energy`. The core rows of
`T g = lambda g` are therefore `T_X x + z C_c x + z^{-1} q^{-1} C_f x = (z + 1/z) x`; multiply by `z`.
The entries of `x` are `1/sqrt S(v) != 0`. The outgoing matrix differs from the mixed one by
`(z^2 - 1) C_c`, and `(z^2 - 1) C_c x = 0` with `z^2 = 1/q != 1` and all `x_v != 0` iff `C_c = 0`; the bound
matrix differs by `q^{-1}(1 - z^2) C_f`, likewise. QED.

*Remark.* The proposition says the constant vector is neither outgoing nor bound on a diagram with
both kinds of ray; `z = q^{-1/2}` may still be a root of `p_funnel` through a different null vector.
Under the wave group the constant mode is then not a resonance eigen-datum of the model and not an
`L^2` eigen-datum; it is a half-outgoing state, not represented in `K`.

**Proposition G4(b).** One-vertex regular diagram, core `[0]`, one cusp of weight `a` and one funnel of
weight `b = q + 1 - a`: `p(z) = z^2 - (1 + a(q - 1))/q`. The Perron root is a resonance at `z^2 = 1/q`
iff `a = 0`, a threshold iff `a = 1`, and a visible bound state with `vartheta^2 = q/(1 + a(q-1)) in (1/q, 1)`
for `1 < a <= q + 1`, with `vartheta^2 = 1/q` iff `a = q + 1`.

*Proof.* `p = z^2 + 1 - a - (q + 1 - a)/q = z^2 - (a(q-1) + 1)/q`. The root `z^2 = (1 + a(q-1))/q` is `1/q`
at `a = 0`, `1` at `a = 1`, `q` at `a = q + 1`, and increases in `a`; a root outside the disc is the
reciprocal of a visible bound parameter (`thm:cusp-resonance-count`). QED.

**Lemma G4(c) (first-order root motion under an added funnel).** For a diagram with resonance
polynomial `p(z) = det(N(z))`, `N(z) = (1 + z^2) - z T_X - C`, adding a funnel of weight `f` at vertex
`v` gives `p_f(z) = p(z) - (f/q) p^{(v)}(z)` exactly, where `p^{(v)} = det N(z)` with row and column `v`
deleted (the resonance polynomial of the core with `v` removed, Dirichlet condition). A simple root
`z_i` of `p` moves with `dz_i/df = (1/q) p^{(v)}(z_i)/p'(z_i)` and
`d|z_i|/df = Re(conj(z_i) dz_i/df)/|z_i|`. The Hasse--Weil quartet of D2 stays on a common circle to
first order iff `Re(conj(z_i) p^{(v)}(z_i)/p'(z_i))` is the same for all four `i`; it stays on the Weil
circle iff this quantity vanishes for all four.

*Proof.* `det(N - eps P_v) = det N - eps det N^{(v)}` (expansion along row `v`; exact since the
perturbation is rank one on the diagonal), with `eps = f/q` by `prop:funnel-self-energy`. Implicit
differentiation of `p_f(z_i(f)) = 0`. QED. (The values are computed by the numerics lane; the lemma
supplies the criterion. The brief's "for every `v` and every `f > 0`" is a numerical statement.)

**Lemma G4(d)(iii) (even letters, two stationary states).** Let `H = H_+ (+) H_-` with both summands
nonzero and let `E(rho) = sum_i A_i rho A_i^*` be trace preserving with every `A_i` even. Then `E` has
at least two linearly independent stationary densities, one supported on each sector. Consequently, if
a parity-preserving channel has a unique stationary density, every Kraus representation of it by
homogeneous letters contains an odd letter.

*Proof.* `P A_i P = A_i` implies `A_i H_+- subset H_+-` and, taking adjoints, `A_i^* H_+- subset H_+-`.
Hence for a density `rho` supported on `H_+`, `E(rho)` is supported on `H_+`, and
`Tr E(rho) = Tr(rho sum_i A_i^* A_i) = Tr rho`. So `E` restricts to a trace-preserving CP map on
`B(H_+)`, which has a stationary density (Brouwer, or the Markov--Kakutani argument); likewise on
`B(H_-)`. The two are linearly independent. For the consequence: a channel commuting with `Ad(P)` has
a Kraus representation by homogeneous letters (split each Kraus operator into its even and odd parts
and use the Choi matrix, which commutes with `P (x) conj P`); if all of them were even the first part
applies. QED.

**Theorem G4(d) (the glued toy).** Let `(Z_+-, J_+-)` be `h_+-`-exit contractions on `K_+-`,
`K = K_+ (+) K_-`, `P = 1 (+) (-1)`, `Z = Z_+ (+) Z_-`, `J = J_+ (+) J_-` into `C^{h_+} (+) C^{h_-}`, and
`Omega = Omega_+ (+) Omega_-` an even density with `Tr Omega_+ > 0` and `Tr Omega_- > 0`. Then:

(i) the letters `A_0 = Z` and `A_{(a,k)} = sqrt(p_k) |omega_k><j_a|` (`Omega = sum p_k |omega_k><omega_k|`)
are homogeneous of parity `eps(omega_k) eps(j_a)`; the cross letters are odd; `E` is a trace-preserving
graded transfer channel.

(ii) `E` has a unique stationary density, `rho_inf = tbar^{-1} sum_{m >= 0} Z^m Omega Z^{*m}`, which is
even, has rank at least two, and satisfies `rho_inf|_{K_+-} >= tbar^{-1} Omega_+- != 0`; it attracts every
density iff the holding law is aperiodic.

(iv) For eigenvectors `Z k_n = z_n k_n`, `k_n in K_-`, and `Z k_m = z_m k_m`, `k_m in K_+`:
`E(|k_n><k_m|) = z_n conj(z_m) |k_n><k_m|` and `E(|k_m><k_n|) = z_m conj(z_n) |k_m><k_n|`. More generally
`E` coincides with `X -> Z X Z^*` on the whole odd sector. If all `|z_n| = r_-` and all `|z_m| = r_+`,
every odd eigenvalue has modulus `r_+ r_-`.

(v) The odd part of the twisted ring norm is `str EE^L - Tr E_0^L = -2 Re[(Tr Z_-^L) conj(Tr Z_+^L)]`.

*Proof.* (i) `P |omega_k><j_a| P = eps(omega_k) eps(j_a) |omega_k><j_a|` since both vectors are homogeneous
(`j_a in K_+` for `a <= h_+`, in `K_-` otherwise; `omega_k` are eigenvectors of the even `Omega`, which can
be chosen homogeneous). `sum A_i^* A_i = Z^* Z + J^* J = 1`. (ii) The reset is fixed, so the flux is the
scalar functional `rho -> Tr(J rho J^*)` and the scalar renewal argument of `thm:cusp-renewal-discrete`(b,c)
applies verbatim (`thm:h-exit-renewal`(d)): `rho_inf` is the unique stationary density and attracts iff
aperiodic. `rho_inf` is even because `Z` and `Omega` are even; the `m = 0` term gives the lower bound on
each sector; rank at least two follows. (iv) For odd `X` (block-off-diagonal), `J X J^*` is
block-off-diagonal in `C^{h_+} (+) C^{h_-}`, so `Tr(J X J^*) = 0` and `E X = Z X Z^*`. On `|k_n><k_m|`
this is `z_n conj(z_m)`. (v) The odd sector is `B(K_+, K_-) (+) B(K_-, K_+)`; on the first summand `EE`
acts as `X -> Z_- X Z_+^*`, a map of trace `Tr Z_- . conj(Tr Z_+)`, and its `L`-th power has trace
`Tr Z_-^L . conj(Tr Z_+^L)`; the second summand is the conjugate. QED.

*Instance G4(d)(v).* `K_+`: one vertex, one funnel of weight `q + 1`: `c_+^2 = (q + 1)/q`,
`p_+ = z^2 + 1 - (q+1)/q = z^2 - 1/q`, `ptilde_+ = 1 - z^2/q`, `R_+ = -(z^2 - 1/q)/(1 - z^2/q)`, which is a
Blaschke product of degree two (zeros `+- q^{-1/2}`, poles `+- q^{1/2}`), so `B_bd = 1`, `Theta_+ = eta R_+`,
`dim K_+ = 2`, `spec Z_+ = {+- q^{-1/2}}`, `Tr Z_+^L = q^{-L/2}(1 + (-1)^L)`. `K_-`: the six-dimensional
model of D2 (`thm:h-exit-model`). Then the odd eigenvalues are `+- q^{-1/2} conj(z_n)` and their
conjugates: modulus `q^{-3/4}` on the Hasse--Weil part, `0` on the delay part.

**Proposition G4(d)(vi) (shared exit).** In the setting of `thm:h-exit-renewal` with a fixed reset,
let `k_n, k_m` be eigenvectors of `Z` with simple eigenvalues and `X = |k_n><k_m|`. Then
`Tr(J X J^*) = <a_m, a_n> = (1 - conj(z_m) z_n) <k_m, k_n>`. If this vanishes, `X` is an eigen-operator
of `E` with eigenvalue `z_n conj z_m`. If it does not vanish, `X` is not an eigen-operator, and the
eigenvalue `z_n conj z_m` of `Ad(Z)` (assumed simple) persists in `E` iff `<l_n| Omega |l_m> = 0`, where
`l_n, l_m` are the dual (left) eigenvectors of `Z`.

*Proof.* `J X J^* = |a_n><a_m|` has trace `<a_m, a_n>`; the Gram identity (`thm:h-exit-model`) gives the
second form. `E X = Z X Z^* + Tr(J X J^*) Omega`. `E = E_0 + |Omega>><<fl|` is a rank-one perturbation
of `E_0 = Ad(Z)`, and `prop:rebound-persistence-secular` says a simple eigenvalue of `E_0` with
eigen-operator `X` and dual functional `dual_X` persists iff `fl(X) dual_X(Omega) = 0`; here
`dual_X(Y) = <l_n| Y |l_m>` (the left eigen-operator of `Ad(Z)` at `z_n conj z_m` is `|l_n><l_m|`). QED.

*Remark (the trade-off).* Protection of the odd coherence between an even and an odd mode is
equivalent, by the Gram identity, to their energy-orthogonality; on a connected core with a shared
exit the modes of a diagram are never orthogonal in general (`prop:d2-modal-gram` for the
Hasse--Weil modes among themselves), so the zeros are not protected once the even mode leaks
through the same ray. The glued toy avoids this by construction: its sectors are orthogonal because
they exit through different blocks.

## G5. The arithmetic metric is the Frobenius channel

**Theorem G5(a).** Let `U` be unitary on a finite-dimensional `K`, `0 < r < 1`, `Z' = r U`,
`J' = sqrt(1 - r^2) 1_K` (so `I - Z'^* Z' = J'^* J'`), and `Omega` a density. The renewal channel
`E'(rho) = r^2 U rho U^* + (1 - r^2) Tr(rho) Omega` is CPTP; its unique stationary density is
`rho_inf = (1 - r^2) sum_{m >= 0} r^{2m} U^m Omega U^{*m}`; `rho_inf = Omega` iff `[U, Omega] = 0`; on
traceless operators `E' = r^2 Ad(U)`, so the spectrum of `E'` is `{1} cup r^2 spec(Ad U)`, every
relaxation eigenvalue having modulus exactly `r^2`. For `K = K_HW` of D2 in the symmetric arithmetic
metric, `r = q^{-1/4}`, `U = diag(e^{i theta_a})` with `e^{2 i theta_a} = z_a^2 q^{1/2} = alpha_a/sqrt q`
(each `alpha` twice), i.e. `U^2 ~ (Fr/sqrt q) (x) 1_2` as multisets, and the relaxation moduli are all
`q^{-1/2}`.

*Proof.* Kraus operators `r U` and `sqrt(1 - r^2) sqrt(p_k) |omega_k><e_a|` (`a` over an orthonormal
basis) sum to `r^2 + (1 - r^2) = 1`. Stationarity: `E' rho_inf = (1 - r^2) sum_{m >= 1} r^{2m} U^m Omega U^{*m}
+ (1 - r^2) Omega = rho_inf`; `Tr rho_inf = 1`. Uniqueness: if `E' X = X` then `Y = X - Tr(X) rho_inf`
is traceless and fixed, so `Y = r^2 U Y U^*`, so `|Y| = r^2 |Y|` in any unitarily invariant norm,
so `Y = 0`. If `[U, Omega] = 0` every term equals `Omega` and the geometric series sums to `1`;
conversely `rho_inf = Omega` in the stationarity equation gives `Omega = r^2 U Omega U^* + (1 - r^2) Omega`.
On traceless `X`, `Tr(X) = 0` kills the reset. `spec(Ad U) = {e^{i(theta_a - theta_b)}}` with
`|u_a><u_b|` as eigen-operators; the traceless ones are those with `a != b` together with the
diagonal differences, all with eigenvalue of modulus one. For D2, `Z = r U` in the arithmetic metric
is `thm:arithmetic-metric`; `z_a^2 = alpha/q` (`prop:d2-spectrum-frobenius`) gives `e^{2 i theta_a} = z_a^2/r^2 = alpha q^{-1/2}`. QED.

**Proposition G5(b).** The Sz.-Nagy--Foias characteristic function of the contraction `A = r U`
(`D_A = D_{A^*} = sqrt(1 - r^2) 1`) is
`Theta_A(z) = -A + z D_{A^*}(1 - z A^*)^{-1} D_A = (1 - z r U^*)^{-1}(z - r U)`,
which in the eigenbasis of `U` is `diag(b_{z_a}(z))`, `z_a = r e^{i theta_a}`, `b_a(z) = (z - z_a)/(1 - conj(z_a) z)`.

*Proof.* `(1 - z r U^*)^{-1}[-r U (1 - z r U^*) + z(1 - r^2)] = (1 - z r U^*)^{-1}[-r U + z r^2 + z - z r^2]`
using `U U^* = 1`. Diagonalise `U`. QED.

**Proposition G5(c).** Let the core `T_X` be Hermitian (in particular real symmetric) with standard
rays and constant couplings. Then `Gam(conj z) = Gam(z)^*`, `S(conj z) = S(z)^*`, and for every constant
`e in C^h`, `e^* S(conj z) e = conj(e^* S(z) e)`. Consequently, if `S(z) = V diag(s_1(z), ..., s_h(z)) V^*`
with a constant unitary `V`, each `s_a` has a conjugation-closed zero set. No such diagram has
`S ~ diag(b_{z_a}(z)) . (unitary constant) . (factors with real zeros and poles)` with the four
non-real Hasse--Weil modes of D2 in four distinct diagonal entries; the finest constant-basis
splitting of the quartet is into two conjugation-closed pairs.

*Proof.* With `T_X = sum_i t_i |x_i><x_i|`, `t_i` real, `Gam(z)_{ab} = sum_i c_a c_b x_i(v_a) conj(x_i(v_b))/(lambda(z) - t_i)`,
so `Gam(z) = sum_i (lambda(z) - t_i)^{-1} G_i` with Hermitian constant `G_i`, and `lambda(conj z) = conj lambda(z)`
gives `Gam(conj z) = Gam(z)^*`. `Gam` depends on `z` through `lambda` only, so `Gam(1/z) = Gam(z)`, and
`Q(z) = I - z Gam(z)`, `Q(1/z) = I - z^{-1} Gam(z)` commute; `Q(conj z) = Q(z)^*` and
`S(conj z) = -Q(conj z)^{-1} Q(1/conj z) = -(Q(z)^*)^{-1} Q(1/z)^* = (-Q(1/z) Q(z)^{-1})^* = S(z)^*`. The scalar
statement follows, and `s_a(conj z) = conj(s_a(z))` for `e = V e_a`. A diagonal entry `b_{z_a}` times
factors with real zeros has the single non-real zero `z_a` in the disc, contradicting
conjugation-closure. QED.

**Proposition G5(d).** On `K_HW` of D2 the bipartite sign `eps` (`eps Z eps = -Z`) and complex
conjugation (with respect to the real structure in which `Z` is real, `prop:d2-canonical-rebound`)
generate a Klein four-group acting simply transitively on the four modes `{a, -a, conj a, -conj a}`;
the symmetric arithmetic metric of `thm:arithmetic-metric` is the unique diagonal metric (up to
scale) invariant under this group, and in it the four one-mode exits of G5(b) are permuted by the
group.

*Proof.* `eps k_a` is an eigenvector with eigenvalue `-z_a`; `conj(k_a)` (entrywise, `Z` real) is an
eigenvector with eigenvalue `conj z_a`; the two commute and generate `{1, eps, conj, eps conj}`,
which maps `a` to `-a, conj a, -conj a`. A diagonal metric `diag(h_a)` is invariant iff
`h_a = h_{-a} = h_{conj a}`, i.e. all equal. The exits `e_a = u_a` (the metric-orthonormal modes) are
permuted accordingly. QED.

*Remark (what answers item (iv)).* The object that "has four cusps seeing the four Hasse--Weil modes
separately" is the channel `E'` with the four exits `e_a`, whose characteristic function is
`diag(b_{z_a})`; by G5(c) it is not the wave equation of any self-adjoint diagram. It is the Frobenius
module of G2 restricted to its odd disc part (`alpha_1, ..., alpha_{2g}`, one line per eigenvalue,
square-rooted by the bipartite sign), completed to a channel by the fixed reset. Its uniform gap is
the metric's doing, not a theorem about D2.

## G6. The level tower

**Observation G6(a) (not byte-cited; a correction of the target).** For `Gamma_0(N) < SL_2(Z)` with
trivial nebentypus and `N` squarefree, the `2^{omega(N)}` functions `E(dz, s)`, `d | N`, with `E` the
level-one Eisenstein series, are `Gamma_0(N)`-invariant (for `gamma = (a, b; cN, d')`,
`(d, 0; 0, 1) gamma (d, 0; 0, 1)^{-1} = (a, bd; cN/d, d') in SL_2(Z)`), linearly independent, and their
number equals the number of cusps `sum_{d|N} phi(gcd(d, N/d)) = 2^{omega(N)}`; there are no
Eisenstein newforms of level `N` with trivial character (they would need `chi psi = 1` with
`cond(chi) cond(psi) = N`, impossible for squarefree `N > 1`). The constant term of `E(dz, s)` at any
cusp is `a y^s + b y^{1-s}` with `a, b` rational functions of `p^{-s}`, `p | N`, times
`xi(2s-1)/xi(2s)` in `b`; hence the scattering matrix of `Gamma_0(N)` with trivial character involves
only `xi(2s-1)/xi(2s)` and finite Euler factors, and its determinant is `(xi(2s-1)/xi(2s))^{2^{omega(N)}}`
times a rational function of the `p^{-s}`. Dirichlet `L`-functions `L(2s-1, psi)/L(2s, psi)` enter the
scattering matrix for `Gamma_1(N)`, equivalently for `Gamma_0(N)` with a nontrivial nebentypus,
through the Eisenstein series `E(z, s; chi_1, chi_2)` (Huxley, Hejhal; not in the repository). The
same dichotomy is expected over `F_q[T]` (`cit:kk-level-constant-term` is the trivial-character
instance at one cusp). So `conj:galois-graded-bond` and item (iii) of `obs:elliptic-cavity-next`
should name `Gamma_1(N)` (or the nebentypus tower), not `Gamma_0(N)`.

**Proposition G6(b) (conditional on H-ARITH-1: the `psi`-channel of the `Gamma_1(N)` scattering
matrix over `F_q[T]` is a monomial times `L(2s-1, psi)/L(2s, psi)`, with `L` the completed
`L`-function).** Let `psi` be a nontrivial primitive Dirichlet character mod `N` over `F_q[T]`, and
`L(u, psi) = sum_{f monic} psi(f) u^{deg f}`, a polynomial of degree `deg N - 1`. If `psi` is odd
(`psi|_{F_q^x} != 1`), `L(u, psi) = det(1 - u Fr_psi)` with `Fr_psi` of size `deg N - 1` and all
eigenvalues of modulus `sqrt q`; if `psi` is even, `L(u, psi) = (1 - u) det(1 - u Fr_psi)` with `Fr_psi`
of size `deg N - 2` and the same property (the factor `1 - u` is the Euler factor of the place at
infinity, at which an even `psi` is unramified; the completed `L`-function is `det(1 - u Fr_psi)`).
Put `E_psi = (Fr_psi)_- (+) Pi Fr_psi(-1) = (Fr_psi)_- (+) (q Fr_psi)_+`. Then, with `w = q^{-2s}`,
`L(2s-1, psi)/L(2s, psi) = det(1 - q w Fr_psi)/det(1 - w Fr_psi) = sdet(1 - w E_psi)` (completed
`L`), and the disc part (`|e| < q`) of its graded divisor is `nu(beta_i) = -1` for each eigenvalue
`beta_i` of `Fr_psi`, with no even entry. For the trivial character the channel is
`zeta_{F_q(T)}(2s-1)/zeta_{F_q(T)}(2s) = sdet(1 - w E_S)` with `g = 0`, whose disc part is the single
even entry `nu(1) = +1`. Hence, under H-ARITH-1, the disc part of the level-`N` graded bond is
`(1)_+ (+) (+)_{psi != 1} (beta_{psi,1}, ..., beta_{psi, d_psi})_-`, with the diamond operator `<a>` acting
on the `psi`-block by `psi(a)`.

*Proof.* Orthogonality of characters gives `sum_{deg f = d, f monic} psi(f) = 0` for `d >= deg N`, so
`L(u, psi)` is a polynomial of degree at most `deg N - 1`; the Euler product
`L(u, psi) = prod_{P not | N} (1 - psi(P) u^{deg P})^{-1}` identifies it with the `L`-function of the
corresponding ray class character of `F_q(T)` with the Euler factor at infinity removed; that factor is
`(1 - psi(infinity) u)^{-1}` with `psi(infinity) = 1` when `psi` is trivial on `F_q^x` and absent
otherwise (standard; Rosen, *Number theory in function fields*, ch. 4, not in the repository). The
Riemann hypothesis for the completed `L`-function of a nontrivial character (Weil) gives
`|beta_i| = sqrt q`. With `w = q^{-2s}`, `L(2s, psi) = det(1 - w Fr_psi)` and `L(2s-1, psi) = det(1 - q w Fr_psi)`;
the ratio is `det(1 - w (q Fr_psi))/det(1 - w Fr_psi) = sdet(1 - w E_psi)` with `q Fr_psi` even and `Fr_psi`
odd. `|beta_i| = sqrt q < q` and `|q beta_i| = q^{3/2} > q`. The `g = 0` case of G2 gives the trivial
channel. QED.

*Remark.* If instead the incomplete `L(u, psi)` appears in the channel (as the incomplete
`zeta_{F_q[T]}` does in the one-cusp constant term of `cit:kk-level-constant-term`), each even
`psi` contributes one more odd disc eigenvalue, `e = 1`, at the Perron position `z = +- q^{-1/2}`: a
trivial zero appearing as a resonance. Which of the two occurs is part of H-ARITH-1 and is decided by
the Eisenstein computation, not here.

## Correction ledger against the brief

| # | claim | correction |
|---|---|---|
| 1 | G2(e) | a sign `s_D = (-1)^{m_{+1}}` (multiplicity of the threshold root `z = +1`) multiplies the prefactor and `[z^2] p`; it is `+1` for D2 and D3 |
| 2 | G1(c) | the "size exactly two" statement is proved under the same invertible-Schur-bracket hypothesis as `prop:multi-exit-spectrum`(iii), not unconditionally |
| 3 | G4(a) | "root of `p_funnel` iff `C_c = 0`" is stated for the constant vector as a null vector; `z = q^{-1/2}` can be a root through another vector |
| 4 | G4(c) | "for every `v` and every `f > 0`" is not proved; the lemma gives the first-order criterion, the numerics lane the values |
| 5 | G4(d)(iii) | strengthened to a general lemma: even letters on a graded bond give at least two stationary densities |
| 6 | G6(b) | the completed versus incomplete `L`-function (the place at infinity) is part of the hypothesis; the incomplete choice adds an odd mode at `z = +- q^{-1/2}` per even character |
