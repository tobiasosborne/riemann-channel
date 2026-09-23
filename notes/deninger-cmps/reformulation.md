# Deninger's programme in the supertrace-cMPS language: the dictionary, the metric, and what it suggests

Author: `claude:fable-5.1`, 2026-09-23, working alone at TJO's request; an Opus REFUTE review follows
(`notes/reviews/deninger-cmps-2026-09-23.md`). Sources, all local and byte-addressed: Deninger,
*Arithmetic geometry and analysis on foliated spaces* (`math/0505354:main.tex`, cited below as `[D05:line]`),
*Analogies between analysis on foliated spaces and arithmetic geometry* (`0709.2801:main.tex`, `[D07:line]`),
*Dynamical systems for arithmetic schemes* (`1807.06400:main.tex`, `[D18:line]`), Leichtnam `1307.3851`.
Notebook objects are cited by their claim labels. Standard theorems named without a local source are marked
"not byte-cited". Scratch check: `notes/deninger-cmps/scratch_riesz.py` (author's own, not a blind lane).

**Question (TJO).** The metric is the missing datum of the current strategy. Cast Deninger's programme as
precisely as possible in the notebook's supertrace-cMPS language and see what it suggests: a candidate metric,
or the same shortcoming.

**Answer in one paragraph.** Deninger's programme, translated term by term, is the notebook's forced graded
picture (shard 04b) with three additions the notebook does not have: a *product* on the bond (the cup
product of leafwise cohomology, with the flow acting by ring automorphisms, so its generator is a
derivation), a *transverse geometry* (a Riemann-surface lamination whose leaves carry the odd sector and whose
totally disconnected transversal carries the dissipation), and a *metric mechanism* (the leafwise Hodge star).
His RH argument is exactly the notebook's Kraus dichotomy case (d): the cup product is the inverse pairing
(functional equation), the Hodge star intertwines it with an adjoint pairing (reality), and a star commuting
with the flow gives both. The metric is therefore not new data in his formulation: it is a flow-invariant
polarisation of the symplectic odd bond, equivalent to RH plus semisimplicity, and *unique* when it exists
(Proposition R4). Deninger says himself that the mechanism will not exist as stated for number fields and
must be replaced by "the Kähler identities on cohomology" `[D05:674-676]`, which is Rosati positivity in the
notebook's words (`thm:rosati-ph-genus-two`); the one case where his system exists is the CM lift of an
ordinary elliptic curve with its Frobenius `[D05:1210-1231]`, which is the notebook's Hodge ket bond
(`def:lifted-frobenius-torus`, `thm:hodge-doubling-tensor`) with the same non-liftability caveat; and his
2018 spaces carry no metric and no complex structure `[D18:559]`. So: a reformulation with the same gap.
What the translation adds is (i) a sharper statement of the gap (a unique invariant polarisation, determined
by Poincaré duality; a product on the bond for which the transfer is multiplicative), (ii) a proof that the
notebook's model space `K_S` is *not* Deninger's `H^1` with a different inner product on the same space,
even under RH (Proposition R7: the zero modes are not a Riesz basis), (iii) an exact Tate-twist identity
between the two graded spectral data that fixes the archimedean bookkeeping and the ladder parity
(Proposition R1), (iv) the shape of the prime letters: commuting, functions `p^Theta` of one operator,
with a rotation angle per prime that zeta does not see (Propositions R2, R3), and (v) the dictionary entries
of the comparative table in Part III, which is the format TJO asked for.

Conventions. Deninger's time is `t_D`; the notebook's dilation time is `t = 2 t_D` (ring length `2 log n`,
`prop:ringnorm-trace`). `rho = sigma + i gamma` runs over the nontrivial zeros with multiplicity `m_rho`.
Notebook: `Tr_d Z(t) = sum_rho e^{-conj(rho) t/2}` (`def:distributional-trace`), `P_+(t) = sum_{n>=2}
(Lambda(n)/n) delta(t - 2 log n)`, graded bond `C_+ (+) (K_S (+) l^2(N_{>=1}))_-` with generator
`0 (+) B (+) diag(-(k+1/2))` (`def:riemann-graded-bond`). Deninger: `Theta` the generator of `phi^{t*}` on
reduced leafwise cohomology; `alpha` the conformal exponent; `W_x` the fixed-point term.

---

## Part I. Deninger's package, stated

**D1 (the data).** A triple `(X, F, phi^t)`: `X` compact, `F` a one-codimensional foliation whose leaves are
transversal to the flow `phi^t`, every `phi^t` mapping leaves to leaves `[D07:359-367]`. For a scheme over
`F_p` the model is the suspension `X = M x_{p^Z} R^*_+` of `(M, phi)`, `phi^t[m,u] = [m, e^t u]`, whose
closed orbits are the finite `phi`-orbits on `M` with `l(gamma) = |orbit| log p` `[D07:339-353]`. For a flat
scheme, `X_0 = X^hat_0(C) x_{Q^{>0}} R^{>0}` with `Q^{>0}` acting on the leaf space through commuting
Frobenii `F_p` `[D18:492-497, 505-509]`; the leaves are the components of the leaf space and `Q^{>0}` is
its group of Poincaré return maps `[D18:494]`. Closed orbits `<->` finite places (`l = log Np`), fixed
points `<->` infinite places `[D05:883-889]`.

**D2 (the cohomology and the divisor).** `H^i_dyn = H^i-bar(X, R)`, the maximal Hausdorff quotient of
leafwise de Rham cohomology, with `Theta = lim (phi^{t*} - 1)/t` `[D07:445]`. Conjecture:
`zeta^hat_K(s) = prod_{i=0}^2 det_infty((s - Theta)/2pi | H^i_dyn)^{(-1)^{i+1}}` `[D05:308-312]`, forcing
`H^0 = R` with `Theta = 0`, `H^1` infinite-dimensional with spectrum the nontrivial zeros with multiplicity,
`H^2 = R` with `Theta = 1` `[D05:316-326]`. Here `zeta^hat_K` is the Gamma-completed zeta with poles at
`0, 1` (not the notebook's entire `cxi`).

**D3 (the Lefschetz formula).** On `R^{>0}`, for `K = Q`:
`sum_i (-1)^i Tr(phi^* | H^i) = 1 - sum_rho e^{t rho} + e^t = sum_p log p sum_{k>=1} delta_{k log p} +
(1 - e^{-2t})^{-1}` `[D05:874-880]`, `[D07:432-436]`. On all of `R^*` the coefficient of
`delta_{k l(gamma)}` for `k <= -1` is `epsilon_gamma(|k|) det(-T_x phi^{k l} | T_x F)`, uniformly
`det(1 - T_x phi^{k l}|T_xF) / |det(1 - T_x phi^{|k| l}|T_xF)|` `[D05:1006-1058]`, which under
conformality with `alpha = 1` becomes `e^{k l(gamma)} = Np^k` `[D05:1064-1080]`; the fixed-point term is
`W_x = epsilon_x |1 - e^{kappa_x t}|^{-1}` on `R^{>0}` and `epsilon_x e^t |1 - e^{kappa_x |t|}|^{-1}` on
`R^{<0}`, `kappa = -2` real place, `-1` complex place `[D05:383-395, 1020-1027]`.

**D4 (Hodge theory of Riemannian foliations).** For a bundle-like metric `g` `[D05:555]`, Álvarez López and
Kordyukov: `ker Delta_F -> H-bar^n(X,R)` is a topological isomorphism `[D05:585-592]`; the leafwise star
gives `*_F: H-bar^n -> H-bar^{d-n}` `[D05:594-604]`; `tr(h) = int_X *_F H(h) vol` `[D05:606-608]`; the
scalar product `(h,h') = tr(h cup *_F h') = int_X <H h, H h'>_F vol` `[D05:622-626]`; the cup pairing
`H-bar^n x H-bar^{d-n} -> R` is nondegenerate `[D05:628-633]`; Künneth `[D05:635-643]`; for Kähler
foliations the Hodge decomposition, hard Lefschetz and polarisable `ind R`-Hodge structures on primitive
classes `[D05:646-672]`.

**D5 (the RH mechanism).** Theorem 4 `[D05:676-691]`: `X` compact 3-manifold, `F` Riemannian by surfaces with
a dense leaf, `phi^t` `F`-compatible and conformal on `TF` with factor `e^{alpha t}` (eq. 18). Then `Theta = 0`
on `H-bar^0 = R`, `Theta = alpha` on `H-bar^2 ~ R`, and on `H-bar^1`, `Theta = alpha/2 + S` with `S` skew
for `( , )`. Proof `[D05:697-719]`: `Theta` is a derivation for the cup product (`phi^{t*}` is a ring
automorphism), `Theta = alpha` on `H^2`, and conformality makes `phi^{t*}` commute with `*_F` on 1-forms;
hence `alpha (h,h') = (Theta h, h') + (h, Theta h')`. Corollary 9 `[D05:804-822]` adds transversality,
non-degenerate orbits, and gets pure point spectrum on the completion `H^hat^1`, all `Re rho = alpha/2`,
and the trace formula (eq. 22). For the arithmetic case the same argument is stated at `[D05:349-365]`: if a
star with `(f,f') = tr(f cup *f')` positive exists and commutes with `Theta`, then `Theta = 1/2 + A`, `A`
skew, "hence the Riemann conjecture would follow"; in higher dimension the condition is
`Theta *= *(d - i + Theta)`, "the flow changes the metric defining the star by the conformal factor `e^t`",
and "equation (11n) for forms is a much stronger condition than for cohomology classes" `[D05:474-479]`.

**D6 (the obstructions, in Deninger's words).** (a) On a compact manifold the conditions of Corollary 9
force `alpha = 0`, an isometric flow `[D05:825]`, `[D07:480]`; number theory needs `alpha = 1` `[D05:935]`,
so the phase space must be a solenoid `[D05:940-945]`. (b) "The existence of a conformal metric for the
flow simplifies the analysis. However, I do not think that such a metric will exist for dynamical systems
relevant to number fields. In order to verify equation (11n) for them one will need the Kähler identities
on cohomology" `[D05:674-676]`. (c) The one realised case: an ordinary elliptic curve `E/F_p` with
Frobenius `pi` lifted to `C/Gamma` with CM, `X = (C x_Gamma T_pi Gamma) x_{p^Z} R^*_+`, whose Lefschetz
formula is the explicit formula of `zeta_E` and whose leaf metric `g_{[z,y,t]}(xi,eta) = e^t Re(xi
conj(eta))` is conformal with `alpha = 1` `[D05:1210-1229]`; "misleading however, since it almost never
happens that a variety in characteristic `p` can be lifted to characteristic zero together with its
Frobenius endomorphism" `[D05:1230-1231]`. (d) "Our present dream: to an algebraic scheme over `Z` one
should first attach an infinite dimensional dissipative dynamical system ... the desired dynamical system
should then be obtained by passing to the finite dimensional compact global attractor" `[D05:1232-1234]`.
(e) With conformality and `epsilon_gamma(k) = +1` for all `k`, the linearised return map on the leaf plane at
a prime orbit is `e^{k l/2} O_k` with `O_k in SO(T_xF)`; "are the eigenvalues Weil numbers (of weight 1)?
If yes there would be some elliptic curve over `o_K/p` involved by Tate–Honda theory" `[D05:1095-1106]`.
(f) `chi_Co(F, mu) = -log|d_K|` `[D05:918-933, 1110-1118]`; for `Q` this is `0`, and by Candel's theorem an
`F`-leaf is then a plane, a torus or a cylinder, while a ramified field forces hyperbolic leaves
`[D05:1118-1126]`.

**D7 (the 2018 spaces).** `W_rat(X)(C)` with commuting injective Frobenii `F_p` `[D18:505]`; the closed
points of `X_0` correspond to compact packets `Gamma_x` of periodic orbits of length `log N x`, fibred over
`Aut(F-bar_p^x)/Aut(F-bar_p) = Z^hat^x_{(p)} / p^{Z^hat}` `[D18:505-510]`; no fixed points `[D18:510]`;
`X_0` connected and the zeroth foliation cohomology one-dimensional `[D18:512]`; the closure of the union
of the periodic orbits is `X^hat_0(S^1) x_{Q^{>0}} R^{>0}`, the points with *unitary* characters
`[D18:2416-2441]`; the system is infinite-dimensional where `3` is wanted `[D18:2416]`; "we have yet to
define analytical structures on our spaces" `[D18:559]`; the archimedean fixed points are expected on a
compactification from `X_0(C)/F_infty`, with two incoming orbits at a complex point and one at a real point
`[D18:2036-2052]`. Leichtnam's axioms `1307.3851` add ramified leafwise flat bundles for Artin
`L`-functions.

---

## Part II. The dictionary, as propositions

### R1. The Tate-twist identity of graded spectral data

**Proposition R1.** Let `D` be Deninger's graded spectral datum for `K = Q` in Deninger time,
`D = {(0,+1), (1,+1)} u {(rho, -m_rho)}`, and `W_infty(t_D) = (1 - e^{-2 t_D})^{-1}` the archimedean
fixed-point term (D3). Let `N` be the notebook's datum in notebook time (`def:riemann-graded-bond`,
`prop:riemann-graded-generator`), `N = {(0,+1)} u {(-conj(rho)/2, -m_rho)} u {(-(k+1/2), -1) : k >= 1}`,
with `str = 2 P_+(t)`.
(a) The map `lambda -> (lambda - 1)/2` (Tate twist by `-1`, then `t = 2 t_D`) sends `D` to
`D' = {(-1/2,+1), (0,+1)} u {(-conj(rho)/2, -m_rho)}`.
(b) `e^{-t_D} x` (Deninger's identity D3) is the identity `1 + e^{-t/2} - Tr_d Z(t) = 2 P_+(t) +
sum_{k>=0} e^{-(k+1/2)t}`, and this is `prop:ringnorm-trace` rearranged. Deninger's Lefschetz formula for
`Q` on `R^{>0}` and the notebook's distributional trace identity are the same statement.
(c) As net multiplicities, `D' (+) {(-(k+1/2), -1) : k >= 0} = N`: the notebook's datum is Deninger's
twisted datum with the archimedean fixed-point term moved from the geometric side to the operator side and
counted odd.
(d) Untwisted: `D` is the divisor of `zeta^hat = zeta Gamma_R`, `Gamma_R(s) = pi^{-s/2} Gamma(s/2)`; the
comb datum of `cor:forced-net-spectrum` is the divisor of `zeta`; their difference is the divisor of
`Gamma_R`, poles at `s = -2k`, `k >= 0`, even, and equals `W_infty = sum_{k>=0} e^{-2k t_D} = Tr(e^{-2 t_D
N} | Sym(R))`, the trace of the flow on the jets of the normal line at the archimedean fixed point
(Atiyah–Bott, not byte-cited): a bosonic Fock ladder, even. The notebook's odd ladder `diag(-(k+1/2))`,
`k >= 1`, is the trivial zeros `s = -2k` of `zeta`, odd because they are zeros.

*Proof.* (a) `(0,+) -> (-1/2,+)`, `(1,+) -> (0,+)`. For the zeros, `rho - 1 = -(1 - rho)`; the multiset of
zeros is stable under `rho -> 1 - rho` (functional equation) and `rho -> conj(rho)` (real coefficients), so
`{1 - rho} = {conj(rho)}` as multisets and `{(rho-1)/2} = {-conj(rho)/2}`. (b) Multiply D3 by `e^{-t_D}`.
Left side: `e^{-t_D}(1 + e^{t_D}) - sum_rho e^{t_D(rho - 1)} = e^{-t/2} + 1 - sum_rho e^{-conj(rho) t/2}`
by (a), i.e. `1 + e^{-t/2} - Tr_d Z(t)`. Right side, primes: `e^{-t_D} log p delta(t_D - k log p)` at
`t_D = k log p` equals `p^{-k} log p delta(t/2 - log p^k) = 2 (Lambda(n)/n) delta(t - 2 log n)` with
`n = p^k`, summing to `2 P_+(t)`; archimedean: `e^{-t_D} (1 - e^{-2 t_D})^{-1} = sum_{k>=0} e^{-(2k+1) t_D}
= sum_{k>=0} e^{-(k+1/2) t} = 1/(2 sinh(t/2))`. Rearranging, `Tr_d Z(t) = 1 - 2P_+(t) - sum_{k>=1}
e^{-(k+1/2)t}`, and `sum_{k>=1} e^{-(k+1/2)t} = e^{-t/2}/(e^t - 1)`, which is `prop:ringnorm-trace`.
(c) In `D'` the net multiplicity at `-1/2` is `+1`; adding the odd rung `k = 0` makes it `0`, as in `N`
(`cor:forced-net-spectrum`: `netmult(-(k+1/2)) = -1` only for `k >= 1`); the rungs `k >= 1` and the zeros
and the fixed line agree. (d) `zeta` has `nu = +1` at `1`, `-m_rho` at `rho`, `-1` at `-2k` (`k >= 1`);
`Gamma_R` has `nu = +1` at `-2k` (`k >= 0`); the sum is `+1` at `0` and `1`, `-m_rho` at `rho`, `0` at
`-2k`, which is `D` (D2). The jet trace: `T_x phi^t` acts on the normal line by `e^{kappa t}`, `kappa =
-2`, so on the `k`-th symmetric power by `e^{-2kt}`, and `sum_{k>=0} e^{-2kt} = (1 - e^{-2t})^{-1}`. QED.

*Reading.* The notebook's `prop:ladder-parity-free` found that positivity does not fix the parity of the
ladder. Deninger's structure says why: the rungs are not cohomology at all but the Lefschetz contribution of
the archimedean fixed point, whose parity in a graded operator is the choice of which side of the trace
formula it sits on. Named as the trivial zeros of `zeta` they are odd (the notebook's choice); named as the
poles of the Gamma factor they are the even bosonic Fock ladder of the normal line at infinity, and the two
cancel in `zeta^hat`. The notebook's even fixed line is Deninger's `H^2` (the pole at `1`), not `H^0`; his
`H^0` (the pole of `zeta^hat` at `0`) is the `k = 0` rung, invisible in `N` because it cancels against the
leading term of `W_infty`. Complex places give `kappa = -1`, jets at `-k`, the poles of `Gamma_C(s) =
2(2pi)^{-s}Gamma(s)`: the two incoming orbits of `[D18:2036-2052]` are the two poles' worth of jets per
integer.

### R2. Suspension = ring; the zeros as joint eigenvalues of commuting Frobenii

**Proposition R2.** Let `Q <= R^{>0}` be a subgroup acting on a space `M`, `X = M x_Q R^{>0}` with the flow
`[m,u] -> [m, e^t u]`.
(a) (One prime, rigorous.) `Q = q^Z`, `M` a compact manifold, `q` acting by a diffeomorphism `f^{-1}`.
Then `X` fibres over the circle `R^{>0}/q^Z` with fibre `M`, the reduced leafwise cohomology is the space
of smooth sections `c: R^{>0} -> H^i(M)` with `c(qu) = f^* c(u)`, `Theta = u d/du`, the spectrum of
`Theta` on `H-bar^i` is `{(log mu + 2 pi i k)/log q : mu in spec(f^*|H^i(M)), k in Z}` with the
multiplicities of `mu`, and
`sum_{lambda} e^{t lambda} = log q sum_{m in Z} Tr(f^{*m} | H^i(M)) delta(t - m log q)` in `D'(R)`.
Alternating over `i`, the right side is `log q sum_m L(f^m) delta(t - m log q)`, the Lefschetz numbers at the
orbit lengths. For `M = E(C)` with `f = pi` a lifted Frobenius, the `Theta`-spectrum on `H-bar^1` is the
zero set of `zeta_E(s)` in `s`, `p^s in {pi, conj(pi)}`, with its vertical towers.
(b) (All primes, formal.) For `Q = Q^{>0}` and a vector `v in H^i(M)` with `F_q^* v = q^rho v` for all
`q in Q^{>0}`, `c(u) = u^rho v` is a `Theta`-eigenvector with eigenvalue `rho`, and it is the only
equivariant section built on `v`: because `Q^{>0}` is dense in `R^{>0}`, a continuous function invariant
under it is constant, so the towers of (a) collapse to single points. Conversely, on a suspension the
`Theta`-eigenvectors are the equivariant sections `u^rho v` with `v` a joint eigenvector of the commuting
`F_p^*` with eigenvalues `p^rho`. The zeros, in Deninger's picture, are the characters `n -> n^rho` of
`Q^{>0}` that occur as joint eigencharacters of the Frobenii on the leaf-space cohomology; a product leaf
space `prod_p M_p` with `F_p` acting on the `p`-th factor has only product characters, the poles of the
Euler factors, which is `obs:prime-by-prime-blind` in this language.
(c) (The Bost–Connes shadow.) On `l^2(N)` with the isometries `mu_p e_n = e_{pn}`, the vector
`v_rho = sum_n n^{-rho} e_n` satisfies `mu_p^* v_rho = p^{-rho} v_rho` for all `p`, and `||v_rho||^2 =
zeta(2 Re rho)`: it lies in `l^2` iff `Re rho > 1/2`. A metric in which the joint eigenvectors of the
`mu_p^*` at the zeros are normalisable and the normalised flow is unitary must be inequivalent to the
`l^2(N)` metric, and under RH it makes `v_rho, v_rho'` orthogonal for `rho' != rho`: from
`<F_p^* v, F_p^* w> = p <v, w>` and eigenvalues `p^rho, p^rho'` one gets `(p^{rho + conj(rho')} - p)
<v_rho, v_rho'> = 0`, so `<v_rho, v_rho'> = 0` unless `rho + conj(rho') = 1`.

*Proof.* (a) Fibrewise Hodge theory with a fibre metric depending smoothly on the base point gives the
smooth family of harmonic projections, so the leafwise complex is quasi-isomorphic to the complex of smooth
sections of the flat bundle `H^i(M)` over the circle, the image of `d_F` is closed, reduced equals
unreduced, and the equivariant description follows by unwinding the quotient. On sections `c(u) = u^lambda
v`, `Theta c = lambda c` iff `q^lambda v = f^* v`; Jordan blocks of `f^*` give `u^lambda (log u)^j v`
and do not change the spectrum or the algebraic multiplicities. The trace of translation by `t` on the
`mu`-isotypic sections `span{u^{(log mu + 2 pi i k)/log q}}` is `mu^{t/log q} sum_k e^{2 pi i k t/log q}
= mu^{t/log q} log q sum_m delta(t - m log q)` by Poisson summation, and `mu^{m} = mu^{m log q/log q}`.
(b) is a computation; the last sentence is the definition of a product action. (c) `mu_p^* e_{pn} = e_n`,
`mu_p^* e_n = 0` for `p` not dividing `n`, so `mu_p^* v_rho = sum_n (pn)^{-rho} e_n`. The orthogonality is
the standard argument for eigenvectors of a normal operator, written for the similarity `p^{-1/2} F_p^*`.
QED.

*Reading.* Deninger's Frobenius on the leaf space is the notebook's transfer matrix (`sec:what-rh`), his
suspension is the periodic MPS ring of length `log p`, and his `Q^{>0}`-space is one ring with every prime
period at once. HANDOFF's open step 2 asks for "a generator of Holevo jump form with jumps at `k log p`";
in Deninger's structure the jump at `log p` on the odd sector is `F_p^* = p^Theta = p^{1/2} p^{i H}`, a
dilation by `log p` in a common self-adjoint `H` with spectrum `{gamma}`, and the primes are coupled not
non-abelianly but by sharing one joint eigenbasis; commuting Frobenii are all Deninger uses. (c) is
`obs:kraus-dichotomy` (c) once more: the `l^2(N)` metric makes `mu_p` isometries but puts the zeros exactly
where the joint eigenvectors cease to be normalisable, Connes's "spectrum from its negative"
(`cit:connes-absorption`).

### R3. The local Lefschetz coefficient is a superdeterminant; the rotation angle per prime

**Proposition R3.** Let `gamma` be a closed orbit transversal to `F`, `x in gamma`, `A = T_x phi^{l(gamma)}
|_{T_xF} in GL(2,R)` the linearised Poincaré return map on the leaf plane.
(a) Deninger's coefficient of `delta_{k l}` (D3) is `c_k = str(Lambda^* A^k) / |det(1 - A^k)|` for `k >= 1`
and `c_k = det(A^k) str(Lambda^* A^{-k}) / |det(1 - A^{-k})|` for `k <= -1`, where `str(Lambda^* B) =
sum_i (-1)^i Tr(Lambda^i B) = det(1 - B)`: fermions along the leaf in the numerator, the bosonic jet
normalisation in the denominator, the sign `epsilon_gamma(k)` being the sign of this superdeterminant.
(b) If `A = e^{l/2} O` with `O in O(2)`, then `c_k = 1` for all `k >= 1` and `c_k = e^{k l}` for all
`k <= -1` iff `O in SO(2)`; if `det O = -1` then `c_k = -1` for `k >= 1`. (Deninger's Fact
`[D05:1095-1101]`.)
(c) For `O` the rotation by `theta`, the spectrum of `Lambda^* A` on `Lambda^0 (+) Lambda^1 (+) Lambda^2`
is `{1, e^{l/2} e^{+-i theta}, e^l}`: with `e^l = p`, the Frobenius spectrum on `H^0, H^1, H^2` of an
elliptic curve `E_p/F_p` with `a_p = 2 sqrt(p) cos theta`, whenever that is an integer (Deuring: every
`a` with `|a| <= 2 sqrt(p)` occurs for `p` prime; not byte-cited). The Ruelle zeta uses only `c_k`, so
`theta` is invisible to `zeta`; the leafwise structure sees it.

*Proof.* (a) `det(1 - B) = sum_i (-1)^i Tr Lambda^i B` for a `2 x 2` matrix. For `k <= -1`,
`det(1 - A^k) = det(A^k) det(A^{-k} - 1) = det(A^k) det(1 - A^{-k})` (even dimension), giving the stated
form, which agrees with `[D05:1040-1046]`. (b) `det(1 - u O^k)` with `u = e^{kl/2}`: for a rotation by
`k theta`, `1 - 2u cos(k theta) + u^2 = (u - cos k theta)^2 + sin^2(k theta) > 0` since `u != 1`; for a
reflection, `O^k` is a reflection or `1` and `det(1 - u O^k) = 1 - u^2 < 0` for `k` odd, `u > 1`. Then
`c_k = sgn det(1 - A^k) = 1` and `c_{-k} = det(A^{-k}) = e^{-kl}` for `k >= 1`. (c) Direct. QED.

*Reading.* The notebook's `def:graded-lattice-tensor` has the ring zeta as `1/sdet(1 - z E)`; Deninger's
formula is the same superdeterminant orbit by orbit, with the odd letters the leaf 1-forms and the even
sector the leaf 0- and 2-forms, exactly as `thm:hodge-doubling-tensor` reads the torus. The angle `theta_p`
is the notebook's `G3-T3-3` ("zeta data do not determine the physical state") made concrete: the
conformal-metric hypothesis carries one rotation per prime that the explicit formula never sees, and by
Honda–Tate an algebraic angle is an elliptic curve over `F_p`. The hedgehog picture (04k) of a Hasse–Weil
quartet per cusp is Deninger's local structure at a prime knot.

### R4. The metric is a flow-invariant polarisation of the symplectic odd bond, unique when it exists

**Proposition R4.** Let `V` be a real vector space (the odd bond: `H-bar^1`, or a finite-dimensional
model), `B: V x V -> R` a nondegenerate alternating form (the cup product `H^1 x H^1 -> H^2 ~ R` followed
by `tr`), and `Theta` an endomorphism that is a derivation for `B` in the sense `B(Theta h, h') + B(h,
Theta h') = alpha B(h,h')`.
(i) `g_t := e^{-alpha t/2} e^{t Theta}` lies in `Sp(V,B)`. Hence the spectrum of `Theta` is symmetric
under `lambda -> alpha - lambda`, and with `J` the `B`-transpose, `J e^{t Theta} J^{-1} = e^{alpha t}
e^{-t Theta}`: the operator form (FE) of `def:graded-rh-fe-ramanujan` with `q = e^{alpha t}`. Deninger's
Poincaré duality on `H^1` is the notebook's inverse pairing.
(ii) A *polarisation* is `*` with `*^2 = -1`, `B(*h, *h') = B(h,h')`, and `(h,h') := B(h, *h')`
symmetric positive definite. Deninger's `( , )` is of this form with `*` the leafwise Hodge star on 1-forms
(D4). If `[Theta, *] = 0` then `(Theta h, h') + (h, Theta h') = alpha (h,h')`, so `Theta = alpha/2 + S`
with `S` skew: the manifest form (HP). Conversely, if `g_t` is `B`-symplectic and `( , )`-orthogonal with
`( , ) = B(., *.)`, then `[g_t, *] = 0`. So, given `B`, (HP) with a `B`-compatible form is exactly a
flow-invariant polarisation. In the Kraus dichotomy (`obs:kraus-dichotomy`), `B` is the inverse pairing,
`( , )` the adjoint pairing, and `*` the operator that identifies them; a star commuting with the flow is
case (d), both pairings, and the Hastings-type bound alone remains.
(iii) In leaf dimension two, `*` on 1-forms depends only on the conformal class of the leaf metric, so
Deninger's hypothesis is: the flow preserves the leafwise complex structure (the leaves are Riemann
surfaces and `phi^t` is leafwise holomorphic) and scales leaf area by `e^{alpha t}`; positivity of
`int h wedge *h` for a real 1-form is then automatic. The metric is not extra data beyond the complex
structure.
(iv) (Uniqueness.) Let `dim V = 2g`, and let the return map `g_1 = e^{-alpha/2} e^{Theta}` (or any `g_t`,
`t != 0`) be semisimple with eigenvalues `e^{+-i theta_j}`, `theta_j in (0, pi)` pairwise distinct. Then
there is exactly one polarisation commuting with `g_1`. If some `theta_j in {0, pi}` or some `theta_j`
repeats, the set of invariant polarisations is a positive-dimensional totally geodesic subspace of the
Siegel space `Sp(V,B)/U(g)`. If `g_1` has an eigenvalue off the unit circle, there is none.
(v) (Comparison.) `thm:arithmetic-metric` imposes only `Z^* H Z = r^2 H` and finds, for `K_HW` of D2, a
cone of real dimension four (three modulo scale), cut to one ray by parity and reality. Deninger's
formulation imposes `B` instead and, by (iv), leaves a point. Whether the notebook's symmetric ray is the
`B`-compatible point is a computation not yet done: it needs the cup form on `K_HW`, which is
`H^1 (x) C^2` under `asm:h-diag` (`prop:d2-spectrum-frobenius`), so `B` must be written on the doubling.

*Proof.* (i) `d/dt B(g_t h, g_t h') = B((Theta - alpha/2) g_t h, g_t h') + B(g_t h, (Theta - alpha/2)
g_t h') = 0`. Symplectic maps have `lambda -> 1/lambda` symmetric spectrum; for `e^{t Theta}` this is
`lambda -> alpha - lambda`. The `B`-transpose of a symplectic `g` is `g^{-1}`, so `J g_t J^{-1} =
g_t^{-1}`, i.e. `J e^{t Theta} J^{-1} = e^{alpha t} e^{-t Theta}`. (ii) `(Theta h, h') + (h, Theta h')
= B(Theta h, *h') + B(h, *Theta h') = B(Theta h, *h') + B(h, Theta *h') = alpha B(h, *h')`. Conversely
`B(gh, *gh') = (gh, gh') = (h,h') = B(h, *h') = B(gh, g*h')` for all `h`, so `*g = g*` by
nondegeneracy. (iii) On a surface `*` on 1-forms is `J^T` up to sign for the complex structure `J` and is
unchanged by `g -> e^{2f} g`; `h wedge *h = |h|^2 vol >= 0`. (iv) `B(V_lambda, V_mu) = 0` unless
`lambda mu = 1` by invariance, so `V = (+)_j E_j`, `B`-orthogonally, with `E_j` the real 2-plane of the
pair `e^{+-i theta_j}`; a polarisation commuting with `g_1` preserves each `E_j` (distinct eigenvalues); on
`E_j`, `g_1` is an elliptic element of `Sp(E_j, B) = SL(2,R)`, conjugate to the rotation by `theta_j`,
whose centraliser in `SL(2,R)` for `theta_j not in {0, pi}` is that `SO(2)`; a complex structure in
`SO(2)` is `+-` the rotation by `pi/2`, and `B(h, *h) > 0` picks one sign. The degenerate cases: the
centraliser is larger (`SL(2,R)` for `+-1`, `Sp(4)` etc. for repeats) and its fixed set in Siegel space is
the Siegel space of the centraliser, of positive dimension. A non-unimodular eigenvalue has no invariant
positive form. (v) is a statement of what was computed. QED.

*Reading.* This is the precise form of "the metric": not a free positive form on the zero sector but a
complex structure on the symplectic odd bond, invariant under the transfer, unique when it exists,
determined by Poincaré duality and the spectrum. Existence is equivalent to (RH and semisimplicity); so it is
not a candidate metric in the sense of new data, it is RH in different words, as `prop:hp-inner-product-
discrete` already says for the sesquilinear version. What is new relative to the notebook is the role of
`B`: Poincaré duality removes the cone's freedom that the notebook removed by symmetries.

### R5. Why compact manifolds force `alpha = 0`, and what a solenoid changes

**Proposition R5.** (a) If `X` is a compact oriented manifold, `phi^t` a flow transversal to `F` with the
invariant closed 1-form `omega_phi` (`omega|_{TF} = 0`, `omega(Y_phi) = 1`, `[D07:370-378]`), and `phi^t`
conformal on `TF` with factor `e^{alpha t}`, then `alpha = 0`.
(b) On Deninger's elliptic solenoid `X = (C x_Gamma T_pi Gamma) x_{p^Z} R^*_+` with `g = e^t Re(xi
conj(eta))`, the flow scales leaf area by `e^t` and the holonomy `(z, y, t) ~ (pi^{-1} z, pi^{-1} y, t + log
p)` scales leaf area by `p^{-1}` and the Haar measure of the transversal `T_pi Gamma ~ Z_p` by `p^{+1}`
under the inverse identification, so the product measure `vol_F (x) mu_transverse` is invariant while
leaf area alone is not: expanding leaves, contracting transversal, neutral flow direction.

*Proof.* (a) `Omega = vol_F wedge omega_phi` is a volume form on `X`, `phi^{t*} Omega = e^{alpha t}
Omega` (the leaf area form scales by `e^{alpha t}` in leaf dimension two, `omega_phi` is invariant), and
`int_X phi^{t*} Omega = int_X Omega` for a diffeomorphism isotopic to the identity, so `e^{alpha t} = 1`.
(b) `g` is well defined on the quotient: `e^{t + log p} Re(pi^{-1} xi conj(pi^{-1} eta)) = e^t p |pi|^{-2}
Re(xi conj(eta)) = e^t Re(xi conj(eta))` since `|pi|^2 = p` `[D05:1225-1229]`; `T phi^s` is the identity
on leaf tangents while the base point moves from `t` to `t + s`, so `g` scales by `e^s`. The transversal
statement is `|pi|_p = p^{-1}`. QED.

*Reading.* In the notebook's normalisations (`def:graded-transfer-channel`) this is the counting
normalisation (Perron root `q`, growth) against the channel normalisation (trace preservation, growth `1`):
on a compact manifold an invariant finite volume forces the trivial divisor's `q` and `1` to coincide, and
the solenoid separates them by paying for the leaf growth with contraction on the totally disconnected
transversal. Deninger's "dissipative system with a compact attractor" `[D05:1232-1234]` is that
contraction; the notebook calls it the Lindbladian. The units-invariant GL_1 bond of shard 04p, `R_+^x
x Z^hat^x` inside `A^x/Q^x`, and the adele class group `A/Q = R x_Z Z^hat`, are solenoids of exactly this
type: an archimedean flow line with a profinite transversal. The closure of the periodic orbits in the 2018
system is the space of *unitary* characters `[D18:2441]`, the Pontryagin-dual side of that transversal.

### R6. The elliptic example is the notebook's Hodge ket bond

**Proposition R6.** For an ordinary `E/F_p` with Frobenius `pi` and CM lift `C/Gamma`
(`asm:deuring-lift`, `def:lifted-frobenius-torus`):
(a) Deninger's leaf-space data `(H^*(C/Gamma, C), pi^*, (-1)^{deg})` is the notebook's doubled bond
`(V (x) V-bar, E-double = diag(1, conj(pi), pi, p), G-double = diag(1,-1,-1,1))` of
`thm:hodge-doubling-tensor`, with `V = Lambda^*(H^{1,0}) = C (+) C dz`; Deninger's `H^1` is the odd
sector `H^{1,0} (+) H^{0,1} = V_- (x) V-bar_+ (+) V_+ (x) V-bar_-`, and his `H^0 (+) H^2` the even sector.
(b) Deninger's Hodge inner product on `H^1`, `(h,h') = int h wedge *conj(h')`, is the inner product
induced on the doubled bond by the Hodge inner product on the ket bond `V` (`||dz||^2 = int dz wedge
*conj(dz)`), restricted to the odd sector.
(c) Conformality with factor `e^t` per period `log p` on `H^1` is the statement `||pi^* dz||^2 = |pi|^2
||dz||^2 = p ||dz||^2`, i.e. the ket-bond letter `A = diag(1, pi) = 1 (+) sqrt(p) U` with `U` unitary on
`V_-`. Deninger's metric hypothesis on the doubled bond is exactly: the prime letter is a similarity with
ratio `sqrt(p)` on the odd ket line for the ket-bond inner product.
(d) The `Theta`-spectrum of the suspension (R2(a)) on `H-bar^1` is `{s : p^s in {pi, conj(pi)}}`, the
zeros of `zeta_E`, and its trace formula is the explicit formula of `zeta_E` `[D05:1213-1224]`.

*Proof.* (a) `V (x) V-bar = Lambda^*(C dz (+) C dz-bar) = H^*(T^2, C)` graded by total degree
(`thm:hodge-doubling-tensor`); `pi^* dz = pi dz`, `pi^* dz-bar = conj(pi) dz-bar`, `pi^*(dz wedge dz-bar)
= p dz wedge dz-bar`. (b) The Hodge inner product on forms is multiplicative on wedge products of
orthogonal factors; `H^{1,0} = V_- (x) 1-bar`. (c) is (b) applied to `pi^*`. (d) is R2(a) with `f = pi`,
`spec(pi^* | H^1) = {pi, conj(pi)}`. QED.

*Reading.* At genus one everything is forced by Hasse and the test of "which metric" is vacuous
(`obs:gl1-bond-no-metric`, numerics D29–D30); Deninger's own verdict on his example is the same
`[D05:1230-1231]`. For higher genus the notebook's `thm:rosati-ph-genus-two` says the Hodge inner product
on `H^{1,0}` of the canonical lift is singled out by Rosati positivity, not by the count equations; Deninger's
"one will need the Kähler identities on cohomology" `[D05:676]` is the same sentence. Both programmes reduce
RH to a positivity that must be supplied; neither derives it from the dynamics or the channel.

### R7. The model space `K_S` is not Deninger's `H^1` with another inner product

**Proposition R7.** (a) In Deninger's picture, with `( , )` positive and `Theta = 1/2 + A`, `A`
skew-adjoint on the completion `H^hat^1`, the eigenvectors of `Theta` at distinct zeros are orthogonal,
and under pure point spectrum (Corollary 9 `[D05:808-822]`) `H^hat^1 ~ l^2(zeros)` with `Theta` diagonal.
(b) Let `w_n = -gamma_n/2 - i(1 - sigma_n)/2` be the notebook's modes in `K_S = H^2 (-) S H^2`
(`prop:functional-model-modes`, `obs:model-modes-sign`), `k_n` the reproducing kernels. The normalised
kernels `k_n/||k_n||` are not a Riesz basis of their closed span. Consequently there is no bounded
invertible operator `T: H^hat^1 -> K_S` sending an orthonormal eigenbasis of Deninger's `Theta` to
multiples of the `k_n`, and no inner product on `K_S` equivalent to the Hardy inner product in which
`Z(t)` is normal with the `k_n` as eigenvectors. This holds unconditionally, and under RH the failure is
explicit: `rho(w_n, w_{n+1})^2 = (d_n/2)^2 / ((d_n/2)^2 + 1/4) <= d_n^2` for a gap `d_n = gamma_{n+1} -
gamma_n`, and `liminf d_n = 0`.

*Proof.* (a) `(Theta h, h') = (h, (1 - Theta) h')` gives, for eigenvectors at `rho, rho'`,
`(rho - (1 - conj(rho'))) (h,h') = 0`, and `1 - conj(rho') = rho'` on the line, so distinct zeros are
orthogonal. (b) The normalised reproducing kernels of a model space `K_B`, `B` a Blaschke product with
simple zeros `(w_n)`, form a Riesz basis iff `(w_n)` is a Carleson sequence, `inf_n prod_{m != n} rho(w_n,
w_m) > 0` (Shapiro–Shields 1961, Nikolski, *Treatise on the shift operator*, not byte-cited), and this
requires uniform separation `inf_{n != m} rho(w_n, w_m) > 0`. Under RH `Im w_n = -1/4` and the displayed
formula holds; `N(T) ~ (T/2pi) log T` gives `liminf d_n = 0`. Unconditionally, a positive proportion of
zeros lies on the critical line (Levinson 1974, Conrey 1989, not byte-cited), so among the zeros on the
line below `T` the mean consecutive gap is `O(1/log T)`, and consecutive on-line zeros with `Im w = -1/4`
and gap `d -> 0` have `rho <= d`. The scalar `S` may carry a singular inner factor beside its Blaschke
part; the kernels `k_n` still lie in `K_S` (`prop:functional-model-modes`) and the Riesz-basis criterion
for the sequence `(k_n)` is the same Carleson condition. A bounded invertible `T` maps an orthonormal
sequence to a Riesz sequence, contradiction; an equivalent inner product making `Z(t)` normal with
eigenvectors `k_n` would make `(k_n/||k_n||')` orthogonal, hence a Riesz basis for the Hardy norm.
Numerics (`scratch_riesz.py`, first 3000 zeros): the nearest-neighbour `rho` has minimum `0.097`, and
the smallest singular value of the Gram matrix of the normalised kernels decreases monotonically,
`0.40, 0.23, 0.13, 0.075, 0.040, 0.016` for `N = 10, 25, 50, 100, 200, 400`. QED.

*Reading.* `thm:arithmetic-metric` found, for the finite cavities, that the Lax–Phillips energy metric lies
outside the cone of `Z`-unitarising metrics on the same space. For `zeta` the statement is stronger: the
cone's metrics are not equivalent to the energy metric at all. `K_S` carries data Deninger's `H^1` discards,
the Gram matrix `G_{nm} = i/(w_n - conj(w_m))` of `prop:mode-diagonal-rebounds` (04h), which encodes the
cusp coupling and the rank-one defect; Deninger's metric is the one in which that Gram matrix is the
identity. A Deninger completion of the notebook's odd bond would be the space of mode coefficients with an
unbounded change of norm, not a second inner product on `K_S`. This is not an obstruction to RH; it is an
obstruction to identifying the two odd bonds, and it says the conjecture H-THETA (`conj:h-theta`), if it
holds, identifies `K_S` with something that is not Deninger's `H^1`.

### R8. The bond is an algebra and the flow is multiplicative; the channel is not

**Proposition R8.** (a) Deninger's `phi^{t*}` is a ring automorphism of the graded-commutative algebra
`H-bar^*(X, R)`, so `Theta` is a derivation, and the Leibniz rule on `H^1 cup H^1 -> H^2` with `Theta =
alpha` on `H^2` is the whole of the functional-equation half of R4(i). (b) The notebook's doubled bond
`V (x) V-bar = End(V)` is an algebra with `odd . odd subset even`, but a graded transfer channel `E(X) =
sum_s A_s X A_s^dagger` is multiplicative, `E(XY) = E(X)E(Y)`, iff it has a single Kraus operator up to
scalar and that operator is invertible, i.e. `E = c Ad(A)`; for a trace-preserving channel this forces
`A` unitary up to scalar. (c) Hence the class of notebook objects on which Deninger's derivation mechanism
can act is exactly the "scalar times automorphism" transfers: the Artin–Schreier transfer with `E E^dagger
= q` (`sec:artin-schreier-mps`), the Frobenius channel of `thm:frobenius-channel-expander` without its
reset term, and the odd sector of any Ramanujan channel in its manifest form (HP). Mixed-unitary expanders
(Weil–LPS, `sec:weil-lps`) and the renewal channels with resets (04h, 04l) are not multiplicative, and for
them Poincaré duality in Deninger's form is not available.

*Proof.* (a) is D5. (b) If `E = sum_s Ad(A_s)` is multiplicative then it is a homomorphism of `End(V)`,
hence (Skolem–Noether, not byte-cited) `E = Ad(A)` for an invertible `A`, and `sum_s A_s X A_s^dagger =
A X A^{-1}` for all `X` forces each `A_s` proportional to `A` and `A^dagger` proportional to `A^{-1}`.
(c) collects the notebook's instances. QED.

*Reading.* The notebook's bond is a vector space with a channel on it; Deninger's is an algebra with an
automorphism group. The functional equation is, for him, the Leibniz rule; the metric is a complex structure
compatible with the product. This is where the two frameworks differ most, and it locates the metric in the
multiplicative structure, which the notebook's channels have only when they are already Ramanujan in the
manifest form. The Bost–Connes system is, in this respect, on Deninger's side: `sigma_t` is an automorphism
group of an algebra, not a Lindbladian, and the KMS states are its equilibria; what it lacks is the grading
and the cohomology.

---

## Part III. What it suggests, and the comparative table

### S1. The gap, sharpened, and one computation for the next round

The missing datum is a transfer-invariant polarisation of the symplectic odd bond (R4). It is unique when
it exists and is determined by Poincaré duality `B` and the spectrum. For the D2 cavity the notebook has the
spectrum and, from `thm:scattering-superdeterminant`, the duality `Fr ~ q Fr^{-1}` on `H^1`; what it has
not written is `B` on `K_HW = H^1 (x) C^2` (under `asm:h-diag`). The computation: write `B` on the
doubling (the natural candidates are `B_{H^1} (x) (symmetric or alternating form on C^2)`), find the
`B`-compatible polarisation fixed by `q^{1/4} Z`, and compare with the symmetric ray of
`thm:arithmetic-metric` and with the Lax–Phillips energy form. Three outcomes: the ray is the
`B`-point (Poincaré duality and the two symmetries agree), the ray is not (then the symmetries are the wrong
selection principle), or no `B` on the doubling is invariant (then `K_HW` is not a symplectic bond and
the doubling is not the `H^1 (x) C^2` of a Deninger structure).

### S2. Same shortcoming, three ways

(a) Deninger reduces RH to the existence of a star commuting with the flow, which he says requires "the
Kähler identities on cohomology" for number fields `[D05:674-676]`; the notebook reduces RH to (HP), which
`thm:rosati-ph-genus-two` says is Rosati positivity. Same reduction. (b) The one realised Deninger system
is the lifted ordinary elliptic curve (R6), where the metric is the Hodge inner product of the lift and RH
is Hasse; the notebook has the same object with the same caveat. (c) The 2018 spaces have no analytic
structure `[D18:559]`, are infinite-dimensional `[D18:2416]`, and their `H^1` is not computed; they
supply the Frobenius packets and connectedness (`H^0 = R`, the notebook's simple even fixed line,
`def:graded-transfer-channel` "graded primitive") and nothing about the odd sector's metric. Added by
this note: (d) the notebook's `K_S` cannot be Deninger's `H^1` up to equivalent norm (R7).

### S3. The prime letters: commuting dilations in one operator

R2 says Deninger's jump at `log p` on the odd sector is `p^Theta = p^{1/2} p^{iH}`, all primes sharing one
self-adjoint `H`; the coupling of the primes is a shared joint eigenbasis, not a non-abelian structure.
For HANDOFF's step 2 (the Stinespring form with jumps at `k log p`) this predicts the answer's shape: a
positive result would exhibit `K_S`-modes as joint eigenvectors of commuting jump operators `J_p` with
`J_p k_rho = p^{-conj(rho)/2} k_rho` (notebook normalisation), and R7 says the `J_p` cannot be normal for
the Hardy inner product. A cheap test: define `J_p` on the span of the first `N` modes by these
eigenvalues and measure its departure from normality in the Gram metric as `N` grows; by R7 it must diverge.

### S4. One angle per prime is the missing data

R3: with a conformal metric, the return map at the prime `p` is `sqrt(p)` times a rotation by an angle
`theta_p` that `zeta` does not see, and the leaf-linearisation at `p` has the cohomology of an elliptic
curve over `F_p` with `a_p = 2 sqrt(p) cos theta_p`. This is the notebook's finding that three tensors
share the ring norms of one curve (`G3-T3-3`) and that the metric selects among presentations, now with the
selection data named: `{theta_p}`. For the cavities of 04k the analogous local question is whether the
return map of the cusp orbit of D2 or D3, linearised on the odd sector, is `q^{1/2}` times a rotation, and
what the angle is (for the curves themselves it is `arg alpha`); for `zeta` there is no candidate for
`theta_p`, which is a precise way of saying there is no candidate for the metric.

### S5. Solenoid, dissipation, and the adelic bond

R5: `alpha = 1` needs expanding leaves paid for by a contracting profinite transversal. The notebook's
adelic GL_1 bond (04p) has this shape, `R_+^x` as the flow line and `Z^hat^x` as the transversal, and
`A/Q` is the connected solenoid on which the theta functional lives. Deninger's packets over
`Z^hat^x_{(p)}/p^{Z^hat}` `[D18:505-510]` are the Bost–Connes symmetry `Z^hat^x = Gal(Q^ab/Q)` modulo the
Frobenius at `p`, which is the structure `conj:galois-graded-bond` asks the bond to carry. The closure of
the periodic orbits being the unitary characters `[D18:2441]` says the geometric core of the 2018 system
is a Pontryagin-dual object, the Fourier side of shard 04p's bond. Candel's dichotomy `[D05:1118-1126]`
adds a discriminator the notebook did not have: for `Q` the leaves are parabolic (plane, torus, cylinder),
not hyperbolic; the modular surface's hyperbolic leaves belong to a ramified field or to `GL_2`, which
bears on the promotion of the modular surface to the Phantasm.

### S6. The supertrace is a transverse index

D3 read through D4 is McKean–Singer: `sum (-1)^i Tr(phi^{t*} | H-bar^i) = str(phi^{t*} e^{-s Delta_F})`
for every `s > 0` `[D05:785-789]`, a `D'(R)`-valued index of the leafwise Dirac operator `d_F + d_F^*`,
transversally elliptic for the `R`-action. In the notebook's language the physical fermions of the graded
cMPS are the leafwise forms, the "ring norm = supertrace" identity is a Witten index, and the dissipative
generator whose kernel is the bond is the leafwise Laplacian. Deninger's explicit-formula line of the
dictionary, "transversal index theorem for the `R`-action and Laplacian along the leaves" `[D07:425]`,
is the notebook's `thm:cmps-twisted-supertrace` in this reading. Two generators, not one: `Delta_F`
(dissipative, kernel = the bond) and `Theta` (the flow on the kernel); in the isometric case `-Theta^2 =
Delta^1` on the kernel `[D05:852-856]`, a wave equation, which is Cramér's function `[D07:681-700]` and
the Lax–Phillips wave picture, not a relaxation spectrum. With `alpha = 1` the "Lindbladian" content of
Deninger's odd sector is the scalar `e^{-t/2}`: the notebook's "one correlation length iff RH" is his
"`Theta - 1/2` is skew".

### The comparative table

One row per attack, the columns the cMPS ingredients; entries are what the notebook has recorded, with
this note's additions in the Deninger row. "Product" means a multiplication on the bond for which the
transfer is multiplicative (R8).

| attack | bond | transfer / flow | grading and sign | pairing (FE) | metric: where positivity comes from | product | what it lacks |
|---|---|---|---|---|---|---|---|
| Artin–Schreier (06, 06b) | `C^q` additive characters | `E`, `E E^dagger = q` | super-transfer: even = trivial character, odd = nontrivial | `S_n` sign law; Weil representation of `M_g` | Parseval, given in advance | yes: `E` is one operator | only quadratic `g`; nothing to choose |
| Weil, curves (06f) | `H^1(J)`, `H^{1,0}` of the lift | Frobenius `pi` | cohomological degree; `H^1` odd | Poincaré duality `pi ~ q pi^{-1}` | Rosati positivity = Hodge index on `C x C`; supplied, not derived | yes: cup product, Frobenius a ring map | liftability (`asm:deuring-lift`); moduli not in the counts |
| Deligne (07) | tensor powers of `H^1` | Frobenius | odd numerator | Poincaré duality | none: positivity of even tensor powers + a base curve | yes | no inner product; needs `X x X` |
| LPS / Weil–LPS channels (05) | `l^2(F_p)` | mixed-unitary `sum Ad(U_i)/D` | ungraded; Hastings bound | adjoint pairing only | Hilbert–Schmidt; one-sided bound only (`thm:kraus-weil-criterion`) | no | duality; assembly over `p` |
| quantum Ihara (08, 08b, 08c) | edge space | Hashimoto `H`, `Sigma` | graded by the Kraus dichotomy | inverse pairing buys FE, adjoint buys reality | both pairings iff unitary | no in general | a family with both pairings that is not already unitary |
| Lax–Phillips / Riemann channel (04, 04h) | `K_S = H^2 (-) S H^2` | compressed dilation `Z(t)`, c.n.u. | `C_+ (+) K_S (+) ladder`, str `= 2P_+` (04b) | `S(-tau) = 1/S(tau)` on the boundary; no operator `J` on `K_S` (semigroup) | energy metric; modes not orthogonal, not a Riesz basis (R7) | no: `Z` not invertible | the metric; the rebound (04h) |
| Bost–Connes (04c, 04d) | `l^2(N)`, product over primes | `sigma_t = Ad(N^{it})`, automorphisms | none | none | KMS, `beta > 1` only (`prop:normal-kms-gibbs`) | yes: an algebra with automorphisms | grading, cohomology, the zeros (`obs:prime-by-prime-blind`) |
| Connes adele class space (cit.) | `L^2(A/Q^x)` modulo | scaling | absorption spectrum: zeros as `(-) H` | Poisson = FE | Weil positivity as the criterion, not a metric | no | the positivity |
| Deninger (this note) | leafwise cohomology of a lamination; odd = leaf 1-forms | flow `phi^{t*}`, ring automorphisms; `Theta = p^{-Theta}`-jumps per prime (R2) | `(-1)^i`; the twist of 04b (R1); archimedean = bosonic jets at a fixed point (R1d) | cup product, `Theta` a derivation (R4, R8) | leafwise Hodge star commuting with the flow = invariant polarisation, unique (R4); needs "Kähler identities on cohomology" | yes: cup product and Künneth | the space (2018: infinite-dimensional, no analytic structure); the star; a rotation angle per prime (R3) |

What the table shows for TJO's programme of assembling clues: the attacks that have a metric (Artin–Schreier,
Weil, Deninger-on-elliptic-curves) all have a product on the bond and a multiplicative transfer; the attacks
without a product (channels, Lax–Phillips, Connes) have only one-sided bounds or criteria. Deninger's
column is the one that supplies, conjecturally, the product for `Spec Z` (Künneth for `X x X`, the
ingredient the README says `zeta` lacks for a Deligne-type argument), and the notebook's column is the one
that supplies the concrete odd bond with its Gram data and the exit structure. The two do not meet on the
same space (R7).

---

## Part IV. Verdict on the metric, and next steps

No candidate metric emerges from Deninger's programme beyond the one the notebook already has: the diagonal
form in the mode basis, which is RH. His mechanism (a Hodge star on the odd bond commuting with the transfer)
is the Kraus dichotomy's "both pairings", and his own assessment is that it will not exist as a metric on
forms for number fields and must be replaced by the Kähler identities, which is Rosati positivity, which is
Weil's proof. The programme is a reformulation with the same gap.

What is gained is the shape of the gap: (1) the metric is a flow-invariant polarisation of the symplectic
odd bond, unique, fixed by Poincaré duality, so the search is for `B`, not for `H`; (2) the bond must be an
algebra on which the transfer is multiplicative, which the notebook's channels are only in the manifest
Ramanujan form; (3) the archimedean bookkeeping and the ladder parity are settled by the fixed-point
reading; (4) the prime letters are commuting dilations `p^Theta` sharing one eigenbasis, with one
rotation angle per prime as the data `zeta` does not fix; (5) `K_S` is not Deninger's `H^1` under any
equivalent norm.

Next, in order. (i) S1: `B` on `K_HW` of D2 and the `B`-compatible polarisation against the symmetric ray
(finite, the cavity scripts exist). (ii) S3: the joint-eigenvector jump operators on the first `N` modes
of `K_S` and their departure from normality (finite, `data/zeros3000.npy`). (iii) S4: the linearised
return map of the cusp orbit of D2 and D3 on the odd sector: is it `q^{1/2}` times a rotation? (iv) Read
Deninger 2018 sections 6–10 for the `Q^{>0}`-orbit structure at a prime and match the packets with the
Bost–Connes symmetry action of shard 04d; (v) register: R1 (proved), R2(a) (proved), R3 (proved), R4
(proved), R5 (proved), R6 (proved-conditional on `asm:deuring-lift`), R7 (proved; the Riesz-basis theorem
and the positive-proportion theorem not byte-cited), R8 (proved), with `cit:` rows for D5–D7.

## What is theorem and what is dictionary

| statement | status |
|---|---|
| R1 (a)–(d): twist identity, equivalence with `prop:ringnorm-trace`, divisor of `Gamma_R` as the jet ladder | theorem (elementary) |
| R2(a): suspension spectrum and Poisson trace for one prime | theorem, standard |
| R2(b): joint eigenvectors for `Q^{>0}` | formal (depends on a leafwise cohomology of the 2018 space that is not computed) |
| R2(c): Bost–Connes joint eigenvectors and orthogonality | theorem (elementary) |
| R3: local superdeterminant, `SO(2)` iff `epsilon = 1`, the angle invisible to `zeta` | theorem (elementary), the Deuring sentence not byte-cited |
| R4(i)–(iv): FE from the derivation, HP from the star, uniqueness of the polarisation | theorem (linear algebra) |
| R4(v), S1: the `B`-point against the symmetric ray | not computed |
| R5: `alpha = 0` on compact manifolds, the solenoid evasion | theorem (elementary) |
| R6: elliptic example = Hodge ket bond | theorem, conditional on `asm:deuring-lift` |
| R7: no Riesz basis, no equivalent normalising metric on `K_S` | theorem, two standard results not byte-cited; numerics support |
| R8: multiplicative channels are `c Ad(A)` | theorem (Skolem–Noether, not byte-cited) |
| "the metric is the missing datum in Deninger too" | Deninger's own words `[D05:674-676, 1230-1231]`, `[D18:559]`; dictionary beyond that |
| S3–S6 | suggestions, not claims |
