# Deninger's programme in the supertrace-cMPS language: the dictionary, the metric, and what it suggests

Author: `claude:fable-5.1`, 2026-09-23, working alone at TJO's request. Version 2, after the Opus REFUTE
review `notes/reviews/deninger-cmps-2026-09-23.md` (1 VALID / 6 MINOR / 1 INVALID, 278 independent checks,
30 corrections, all applied; ledger at the end). Sources, all local and byte-addressed: Deninger,
*Arithmetic geometry and analysis on foliated spaces* (`math/0505354:main.tex`, cited as `[D05:line]`),
*Analogies between analysis on foliated spaces and arithmetic geometry* (`0709.2801:main.tex`, `[D07:line]`),
*Dynamical systems for arithmetic schemes* (`1807.06400:main.tex`, `[D18:line]`), Leichtnam
(`1307.3851:main.tex`, `[L13:line]`). Notebook objects are cited by claim label. Standard theorems without a
local source are marked "not byte-cited". Scratch check: `notes/deninger-cmps/scratch_riesz.py` (author's
own); the reviewer's five independent scripts are `notes/reviews/scratch_den_*.py`.

**Question (TJO).** The metric is the missing datum of the current strategy. Cast Deninger's programme as
precisely as possible in the notebook's supertrace-cMPS language and see what it suggests: a candidate metric,
or the same shortcoming.

**Answer.** A reformulation with the same gap, and the gap is now stated more sharply. Deninger's programme,
translated term by term, is the notebook's forced graded picture (shard 04b) with three structures the
notebook does not have: a *product* on the bond (the cup product of leafwise cohomology, with the flow acting
by ring automorphisms so that its generator is a derivation), a *transverse geometry* (a Riemann-surface
lamination whose leaves carry the odd sector and whose totally disconnected transversal carries the
contraction), and a *metric mechanism* (the leafwise Hodge star). His RH argument is the manifest form (HP)
of `def:graded-rh-fe-ramanujan`: the cup product supplies the functional equation (`Theta^# = 1 - Theta`,
the transpose), and a star commuting with the flow supplies a positive form in which `Theta - 1/2` is skew,
after which nothing remains to be proved. The metric is therefore not new data in his formulation: it is a
flow-invariant polarisation of the symplectic odd bond, equivalent to RH plus semisimplicity, and a single
point when the spectrum is simple (or Krein-definite) and the symplectic form is canonical (Proposition R4).
Deninger writes that the conformal metric will not exist for number fields and must be replaced by "the
Kähler identities on cohomology" `[D05:674]`, Serre's Kähler analogue `[L13:423]`, which is the analogue of
Rosati positivity (`thm:rosati-ph-genus-two`); his only realised system is the CM lift of an ordinary elliptic
curve with its Frobenius `[D05:1205-1231]`, the notebook's Hodge ket bond (`def:lifted-frobenius-torus`,
`thm:hodge-doubling-tensor`, `thm:elliptic-ph-unitary`) with the same non-liftability caveat; and his 2018
spaces carry no Riemannian or leafwise metric and no analytic structure `[D18:559]`, sit over Connes's adele
space `[D18:2363]`, and get `H^0 = R` from an irreducible leaf space `[D18:3021-3023]`. What the translation
adds: (i) an exact Tate-twist identity between the two graded spectral data with the archimedean bookkeeping
(Proposition R1); (ii) the polarisation statement of the metric and what it needs to be a point (R4); (iii)
the local structure at a prime, a rotation angle that zeta does not see (R3); (iv) a proof that the notebook's
model space `K_S` is not Deninger's `H^1` with an equivalent inner product, even under RH (R7); (v) at genus
one, the notebook's doubled bond carries Deninger's product and his derivation argument verbatim, and no other
notebook bond is known to (R8); and (vi) the comparative table of Part III, the format TJO asked for.

Conventions. Deninger's time is `t_D`; the notebook's dilation time is `t = 2 t_D` (ring length `2 log n`,
`prop:ringnorm-trace`). `rho = sigma + i gamma` runs over the nontrivial zeros with multiplicity `m_rho`.
Notebook: `Tr_d Z(t) = sum_rho e^{-conj(rho) t/2}` (`def:distributional-trace`), `P_+(t) = sum_{n>=2}
(Lambda(n)/n) delta(t - 2 log n)`, graded bond `C_+ (+) (K_S (+) l^2(N_{>=1}))_-` with generator
`0 (+) B (+) diag(-(k+1/2))` (`def:riemann-graded-bond`). Deninger: `Theta` the generator of `phi^{t*}` on
reduced leafwise cohomology; `H(alpha)` is `H` with `Theta - alpha` `[D05:332]`; `alpha` the conformal
exponent; `W_x` the fixed-point term.

---

## Part I. Deninger's package, stated

**D1 (the data).** A triple `(X, F, phi^t)`: `X` compact, `F` a one-codimensional foliation whose leaves are
transversal to the flow `phi^t`, every `phi^t` mapping leaves to leaves `[D07:359-367]`. For a scheme over
`F_p` the model is the suspension `X = M x_{p^Z} R^*_+` of `(M, phi)`, `phi^t[m,u] = [m, e^t u]`, whose
closed orbits are the finite `phi`-orbits on `M` with `l(gamma) = |orbit| log p` `[D07:339-353]`; when `phi`
is a covering of degree `> 1` the manifold is replaced by the solenoid `M-bar = lim_<-(M, phi)` on which
`phi` becomes the shift `[D05:1131-1160]`, `[D07:373]`. For a flat scheme, `X_0 = X^hat_0(C) x_{Q^{>0}}
R^{>0}` with `Q^{>0}` acting on the leaf space through commuting Frobenii `F_p` `[D18:492-497, 505-509]`;
the leaves are the components of the leaf space and `Q^{>0}` is its group of Poincaré return maps
`[D18:494]`. Closed orbits `<->` finite places (`l = log Np`), fixed points `<->` infinite places
`[D05:883-889]`.

**D2 (the cohomology and the divisor).** `H^i_dyn = H^i-bar(X, R)`, the maximal Hausdorff quotient of
leafwise de Rham cohomology, with `Theta = lim (phi^{t*} - 1)/t` `[D07:445]`. Conjecture:
`zeta^hat_K(s) = prod_{i=0}^2 det_infty((s - Theta)/2pi | H^i_dyn)^{(-1)^{i+1}}` `[D05:308-312]`; if the
eigenvalues of `Theta` on `H^0, H^1, H^2` are distinct `[D05:317-319]`, this forces `H^0 = R` with
`Theta = 0`, `H^1` infinite-dimensional with spectrum the nontrivial zeros with multiplicity, `H^2 = R(-1)`,
i.e. `Theta = 1` `[D05:320-326, 334]`. Here `zeta^hat_K` is the Gamma-completed zeta with poles at `0, 1`,
not the notebook's entire `cxi`. The archimedean factors are themselves regularised determinants: for a real
place `R_infty = R[exp(-2y)]` with `Theta = d/dy`, eigenvalues `0, -2, -4, ...`, and
`zeta_infty(s) = det_infty((s-Theta)/2pi | R_infty)^{-1}`; for a complex place `R[exp(-y)]`, eigenvalues the
nonpositive integers (Proposition 2.1, `[D05:204-215, 286-296]`).

**D3 (the Lefschetz formula).** On `R^{>0}`, for `K = Q`:
`sum_i (-1)^i Tr(phi^* | H^i) = 1 - sum_rho e^{t rho} + e^t = sum_p log p sum_{k>=1} delta_{k log p} +
(1 - e^{-2t})^{-1}` `[D05:874-880]`, `[D07:432-436]`. On all of `R^*` the coefficient of
`delta_{k l(gamma)}` is uniformly `det(1 - T_x phi^{k l}|T_xF) / |det(1 - T_x phi^{|k| l}|T_xF)|`
`[D05:1028-1037]`, which under conformality with `alpha = 1` becomes `e^{k l(gamma)} = Np^k` for `k <= -1`
`[D05:1064-1080]`; the fixed-point term is `W_x = epsilon_x |1 - e^{kappa_x t}|^{-1}` on `R^{>0}`
`[D05:1020-1022]`, and on `R^{<0}` carries `det(-T_x phi^t|T_xF)`, which is `e^t` in the conformal case
`[D05:1066-1072]` and matches the number-field `W_p` `[D05:383-398]`; `kappa = -2` real place, `-1` complex
place. The fixed-point term is Deninger's conjecture, not a theorem `[D05:756, 1038-1041]`.

**D4 (Hodge theory of Riemannian foliations).** For a bundle-like metric `g` `[D05:555]`, Álvarez López and
Kordyukov: `ker Delta_F -> H-bar^n(X,R)` is a topological isomorphism `[D05:585-592]`; the leafwise star
gives `*_F: H-bar^n -> H-bar^{d-n}` `[D05:594-604]`; `tr(h) = int_X *_F H(h) vol` `[D05:606-608]`; the
scalar product `(h,h') = tr(h cup *_F h') = int_X <H h, H h'>_F vol` `[D05:622-626]`; the cup pairing
`H-bar^n x H-bar^{d-n} -> R` is nondegenerate `[D05:628-633]`; Künneth `[D05:635-643]`; for Kähler
foliations the Hodge decomposition, hard Lefschetz and polarisable `ind R`-Hodge structures on primitive
classes `[D05:646-672]`.

**D5 (the RH mechanism).** Theorem 4 `[D05:676-691]`: `X` compact 3-manifold, `F` Riemannian by surfaces with
a dense leaf, `phi^t` `F`-compatible and conformal on `TF` with factor `e^{alpha t}`. Then `Theta = 0` on
`H-bar^0 = R`, `Theta = alpha` on `H-bar^2 ~ R`, and on `H-bar^1`, `Theta = alpha/2 + S` with `S` skew for
`( , )`. Proof `[D05:697-719]`: `Theta` is a derivation for the cup product (`phi^{t*}` is a ring
automorphism), `Theta = alpha` on `H^2`, and conformality makes `phi^{t*}` commute with `*_F` on 1-forms;
hence `alpha (h,h') = (Theta h, h') + (h, Theta h')`. Corollary 9 `[D05:804-822]` adds transversality and
non-degenerate orbits and gets pure point spectrum on the completion `H^hat^1`, all `Re rho = alpha/2`, and
the trace formula; its proof also gives `-(Theta - alpha/2)^2 = Delta^1|_{ker Delta^1_F}` `[D05:852-858]`,
and Remark a asks whether the squares of the zeros' imaginary parts lie in the spectrum of a Laplacian on
1-forms `[D05:864]`; Remark b allows continuous spectrum in general `[D05:865-869]`. For the arithmetic case
the star argument is `[D05:349-365]`: a star with `(f,f') = tr(f cup *f')` positive and commuting with
`Theta` gives `Theta = 1/2 + A`, `A` skew, "hence the Riemann conjecture would follow"; in higher dimension
the condition is `Theta *= *(d - i + Theta)`, and "equation (11n) for forms is a much stronger condition than
for cohomology classes" `[D05:474-479]`. Leichtnam attributes the argument to Serre's Kähler analogue
`[L13:423]` and writes the functional-equation half as "the transpose of `e^{t Theta}` is `e^t e^{-t
Theta}`" `[L13:427-440]`.

**D6 (the obstructions, in Deninger's words).** (a) On a compact manifold the conditions of Corollary 9
force `alpha = 0`, an isometric flow `[D05:825]`, `[D07:480]`; number theory needs `alpha = 1` `[D05:935]`,
so the phase space must be a solenoid `[D05:940-945]`. (b) "The existence of a conformal metric for the
flow simplifies the analysis. However, I do not think that such a metric will exist for dynamical systems
relevant to number fields. In order to verify equation (11n) for them one will need the Kähler identities
on cohomology" `[D05:674]`. (c) The one realised case: an ordinary elliptic curve `E/F_p` with Frobenius
`pi`, lifted to `C/Gamma` with CM by the maximal order `[D05:1206]`, `X = (C x_Gamma T_pi Gamma) x_{p^Z}
R^*_+`, whose Lefschetz formula (Theorem `[D05:1186-1201]`) is the explicit formula of `zeta_E`
`[D05:1225]` and whose leaf metric `g_{[z,y,t]}(xi,eta) = e^t Re(xi conj(eta))` is conformal with `alpha =
1` `[D05:1226-1230]`; "misleading however, since it almost never happens that a variety in characteristic
`p` can be lifted to characteristic zero together with its Frobenius endomorphism" `[D05:1230]`. (d) "Our
present dream: to an algebraic scheme over `Z` one should first attach an infinite dimensional dissipative
dynamical system ... the desired dynamical system should then be obtained by passing to the finite
dimensional compact global attractor" `[D05:1232-1234]`. (e) With conformality and `epsilon_gamma(k) = +1`
for all `k`, the linearised return map on the leaf plane at a prime orbit is `e^{k l/2} O_k` with `O_k in
SO(T_xF)`; "are the eigenvalues Weil numbers (of weight 1)? If yes there would be some elliptic curve over
`o_K/p` involved by Tate–Honda theory" `[D05:1095-1106]`. (f) `chi_Co(F, mu) = -log|d_K|` `[D05:918-933,
1110-1118]`; for `Q` this is `0`, and by Candel's theorem there is then an `F`-leaf that is a plane, a torus
or a cylinder `[D05:1124]`, while a ramified field forces every leaf hyperbolic `[D05:1118-1122]`.

**D7 (the 2018 spaces).** `W_rat(X)(C)` with commuting injective Frobenii `F_p` `[D18:505]`; the closed
points of `X_0` correspond to compact packets `Gamma_x` of periodic orbits of length `log N x`, fibred over
`Aut(F-bar_p^x)/Aut(F-bar_p) = Z^hat^x_{(p)} / p^{Z^hat}` with `Z^hat^x_{(p)} = prod_{l != p} Z_l^x`
`[D18:505-510, 1733]`; no fixed points `[D18:510]`; `X_0` connected and the zeroth foliation cohomology
one-dimensional `[D18:512]`, proved through the irreducibility of `Q^{>0} Z^hat^x x_{Q^{>0}} R^{>0}` in the
adele topology, where every continuous function is constant `[D18:3021-3023, 3068]`; the structure theorem
gives continuous `R^{>0}`-equivariant bijections from `X^dot(C)_{Q,in} x R^{>0} ⊔ ⨆_p X^dot(C)_{p,in}
x_{p^Z} R^{>0}` onto `X` and `X_0`, "not homeomorphisms in general" `[D18:2292-2322]`; `X~ = X^hat(C) x
R^{>0}` maps `Q^{>0}`-equivariantly to `A^{>0} = A_f x R^{>0} subset A`, and Deninger asks whether the
`Q^{>0}`-action can be studied from the Bost–Connes–Connes point of view `[D18:2363-2411]`; the closure of
the union of the periodic orbits is `X^hat_0(S^1) x_{Q^{>0}} R^{>0}`, the points with *unitary* characters
`[D18:2416-2441]`; the system is infinite-dimensional where `3` is wanted `[D18:2416]`; it carries a
`G`-invariant metric in the metric-space sense `[D18:2205]` but "we have yet to define analytical structures
on our spaces" `[D18:559]`; the archimedean fixed points are expected on a compactification from
`X_0(C)/F_infty`, with two incoming orbits at a complex point and one at a real point `[D18:2036-2052]`.
Leichtnam's axioms `[L13:73-76]` add ramified leafwise flat bundles for Artin `L`-functions, with an
antilinear star pairing the `chi`- and `chi-bar`-sectors `[L13:392-422]`.

---

## Part II. The dictionary, as propositions

### R1. The Tate-twist identity of graded spectral data

**Proposition R1.** Let `D` be Deninger's graded spectral datum for `K = Q` in Deninger time,
`D = {(0,+1), (1,+1)} u {(rho, -m_rho)}`, and `W_infty(t_D) = (1 - e^{-2 t_D})^{-1}` the archimedean term
(D3). Let `N` be the notebook's datum in notebook time (`def:riemann-graded-bond`,
`prop:riemann-graded-generator`), `N = {(0,+1)} u {(-conj(rho)/2, -m_rho)} u {(-(k+1/2), -1) : k >= 1}`,
with `str = 2 P_+(t)`.
(a) The map `lambda -> (lambda - 1)/2`, the twist `H(1)` of `[D05:332]` followed by `t = 2 t_D`, sends `D`
to `D' = {(-1/2,+1), (0,+1)} u {(-conj(rho)/2, -m_rho)}`. This transport, with `rho -> 1 - rho`, is the one
printed under `cor:forced-net-spectrum`.
(b) `e^{-t_D} x` (Deninger's identity D3) is the identity `1 + e^{-t/2} - Tr_d Z(t) = 2 P_+(t) +
sum_{k>=0} e^{-(k+1/2)t}`, which is `prop:ringnorm-trace` rearranged. Deninger's Lefschetz formula for `Q`
on `R^{>0}` and the notebook's distributional trace identity are the same statement.
(c) As net multiplicities in the sense of `thm:supertrace-rigidity`, `D' (+) {(-(k+1/2), -1) : k >= 0} =
N`: the notebook's datum is Deninger's twisted datum with the archimedean term moved from the geometric side
to the operator side and counted odd. `N` is a net datum; the cancellation at `-1/2` (the image of `H^0`
against the `k = 0` rung) is exactly what Deninger's distinct-eigenvalue hypothesis `[D05:317-319]`
excludes, so `N` is not a Deninger-type graded datum.
(d) Untwisted: `D` is the divisor of `zeta^hat = zeta Gamma_R`, `Gamma_R(s) = pi^{-s/2} Gamma(s/2)`; the
comb datum of `cor:forced-net-spectrum` is the divisor of `zeta`; their difference is the divisor of
`Gamma_R`, poles at `s = -2k`, `k >= 0`, even, and equals `W_infty = sum_{k>=0} e^{-2k t_D}`, the trace of
`e^{t_D Theta}` on Deninger's `R_infty = R[exp(-2y)]`, `Theta = d/dy` (Proposition 2.1, `[D05:204-215,
286-296]`). The notebook's odd ladder `diag(-(k+1/2))`, `k >= 1`, is the trivial zeros `s = -2k` of `zeta`,
odd because they are zeros.

*Proof.* (a) `(0,+) -> (-1/2,+)`, `(1,+) -> (0,+)`. For the zeros, `rho - 1 = -(1 - rho)`; the multiset of
zeros is stable under `rho -> 1 - rho` (functional equation) and `rho -> conj(rho)` (real coefficients), so
`{1 - rho} = {conj(rho)}` as multisets and `{(rho-1)/2} = {-conj(rho)/2}`. (b) Multiply D3 by `e^{-t_D}`.
Left side: `e^{-t_D}(1 + e^{t_D}) - sum_rho e^{t_D(rho - 1)} = e^{-t/2} + 1 - sum_rho e^{-conj(rho) t/2}`
by (a), i.e. `1 + e^{-t/2} - Tr_d Z(t)`. Right side, primes: `e^{-t_D} log p delta(t_D - k log p)` at
`t_D = k log p` equals `p^{-k} log p delta(t/2 - log p^k) = 2 (Lambda(n)/n) delta(t - 2 log n)` with
`n = p^k`, summing to `2 P_+(t)`; archimedean: `e^{-t_D} (1 - e^{-2 t_D})^{-1} = sum_{k>=0} e^{-(2k+1) t_D}
= sum_{k>=0} e^{-(k+1/2) t} = 1/(2 sinh(t/2))`. Rearranging, `Tr_d Z(t) = 1 - 2P_+(t) - sum_{k>=1}
e^{-(k+1/2)t}`, and `sum_{k>=1} e^{-(k+1/2)t} = e^{-t/2}/(e^t - 1)`, which is `prop:ringnorm-trace`. (The
reviewer verified both identities with Gaussian test functions and 3000 zeros to `1.4e-15`, and that
dropping the factor 2 or placing the primes at `t = log n` fails.) (c) In `D'` the net multiplicity at
`-1/2` is `+1`; adding the odd rung `k = 0` makes it `0`, as in `N` (`cor:forced-net-spectrum`:
`netmult(-(k+1/2)) = -1` only for `k >= 1`); the rungs `k >= 1`, the zeros and the fixed line agree. (d)
`zeta` has `nu = +1` at `1`, `-m_rho` at `rho`, `-1` at `-2k` (`k >= 1`); `Gamma_R` has `nu = +1` at `-2k`
(`k >= 0`); the sum is `+1` at `0` and `1`, `-m_rho` at `rho`, `0` at `-2k`, which is `D` (D2). On `R_infty`
the eigenvalues of `Theta` are `-2k`, so `Tr e^{t_D Theta} = sum_k e^{-2k t_D}`. QED.

*Reading.* `prop:ladder-parity-free` found that positivity does not fix the parity of the ladder and that
exact equality to `2P_+` does. R1 explains the freedom: the rungs are not cohomology but the contribution of
the archimedean place, whose parity in a graded operator is the choice of which side of the trace formula it
sits on; named as the trivial zeros of `zeta` they are odd (the notebook's choice), named as the poles of
`Gamma_R` they are even (Deninger's `R_infty`), and the two cancel in `zeta^hat`. Deninger's reading of
`R_infty` as the jets of the normal line at a fixed point of the flow is his conjecture `[D05:756,
1038-1041]` and is dictionary here. The notebook's even fixed line is Deninger's `H^2` (the pole at `1`),
not `H^0`; his `H^0` (the pole of `zeta^hat` at `0`) is the `k = 0` rung, invisible in `N` because it
cancels against the leading term of `W_infty`. A complex place has `kappa = -1` and one simple pole of
`Gamma_C(s) = 2(2pi)^{-s}Gamma(s)` at every nonpositive integer; since `Gamma_C(s) = Gamma_R(s)
Gamma_R(s+1)`, its ladder is two real ladders (even and odd integers), which is what the two incoming orbits
at a complex point `[D18:2052]` match.

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
orbit lengths. The lifted Frobenius `pi` on `C/Gamma` is a covering of degree `[Gamma : pi Gamma] = |pi|^2
= p`, not a diffeomorphism, so (a) does not apply to it; Deninger replaces `M` by the solenoid `M-bar = C
x_Gamma T_pi Gamma` with the shift `[D05:1131-1160]` and proves the trace formula there (Theorem
`[D05:1186-1201]`, example `[D05:1205-1225]`); by `thm:supertrace-rigidity` the net `Theta`-spectrum on the
odd part is then `{s : p^s in {pi, conj pi}}`, the zeros of `zeta_E` with their vertical towers.
(b) (All primes, formal.) For `Q = Q^{>0}` and a vector `v in H^i(M)` with `F_q^* v = q^rho v` for all
`q in Q^{>0}`, `c(u) = u^rho v` is a `Theta`-eigenvector with eigenvalue `rho`, and it is the only
equivariant section built on `v`: because `Q^{>0}` is dense in `R^{>0}`, a continuous function invariant
under it is constant, so the towers of (a) collapse to single points. Conversely, on a suspension the
`Theta`-eigenvectors are the equivariant sections `u^rho v` with `v` a joint eigenvector of the commuting
`F_p^*` with eigenvalues `p^rho`. A product leaf space `prod_p M_p` with `F_p` acting on the `p`-th factor
admits a common exponent `rho` only where every local spectrum contains `p^rho`; for Euler-factor spectra
(`p^rho = 1`) the linear independence of the `log p` forces `rho = 0`: `obs:prime-by-prime-blind` in this
language. In the 2018 construction the primes are coupled otherwise: set-theoretically the system is one
suspension per prime plus a free part, coupled only through the adele topology `[D18:2292-2322]`.
(c) (The Bost–Connes shadow.) On `l^2(N)` with the isometries `mu_p e_n = e_{pn}`, the vector
`v_rho = sum_n n^{-rho} e_n` satisfies `mu_p^* v_rho = p^{-rho} v_rho` for all `p` and every `rho` with
`Re rho > 1/2`, where `||v_rho||^2 = zeta(2 Re rho)`; nothing in `l^2(N)` selects the zeros. A metric in
which such joint eigenvectors at the zeros are normalisable and the normalised flow is unitary is
inequivalent to the `l^2(N)` metric, and under RH it makes `v_rho, v_rho'` orthogonal for `rho' != rho`:
from `<F_p^* v, F_p^* w> = p <v, w>` for all `p` and eigenvalues `p^rho, p^rho'`, `(p^{rho + conj(rho')} -
p) <v_rho, v_rho'> = 0` for all `p`; one prime only gives `(gamma - gamma') log p in 2 pi Z`, and two
primes with `log p/log q` irrational force `gamma = gamma'`.

*Proof.* (a) Fibrewise Hodge theory with a fibre metric depending smoothly on the base point gives the
smooth family of harmonic projections, so the leafwise complex is quasi-isomorphic to the complex of smooth
sections of the flat bundle `H^i(M)` over the circle, the image of `d_F` is closed, reduced equals
unreduced, and the equivariant description follows by unwinding the quotient. On sections `c(u) = u^lambda
v`, `Theta c = lambda c` iff `q^lambda v = f^* v`; Jordan blocks of `f^*` give `u^lambda (log u)^j v`
and do not change the spectrum or the algebraic multiplicities. The trace of translation by `t` on the
`mu`-isotypic sections `span{u^{(log mu + 2 pi i k)/log q}}` is `mu^{t/log q} sum_k e^{2 pi i k t/log q}
= mu^{t/log q} log q sum_m delta(t - m log q)` by Poisson summation, and `mu^{m} = mu^{m log q/log q}`. A
diffeomorphism of a compact oriented surface acts by `+-1` on `H^2`, so the covering `pi` is excluded; the
solenoid statement is Deninger's theorem. (b) is a computation; the product statement is the definition of a
product action. (c) `mu_p^* e_{pn} = e_n`, `mu_p^* e_n = 0` for `p` not dividing `n`, so `mu_p^* v_rho =
sum_n (pn)^{-rho} e_n`. The orthogonality is the argument for eigenvectors of a normal operator, written for
the similarities `p^{-1/2} F_p^*`; `p^{rho + conj rho'} = p` iff `sigma + sigma' = 1` and `(gamma -
gamma') log p in 2 pi Z`. QED.

*Reading.* Deninger's Frobenius on the leaf space is the notebook's transfer matrix (`sec:what-rh`), his
suspension is the periodic MPS ring of length `log p`, and his `Q^{>0}`-space carries every prime period at
once. On the odd sector the jump at `log p` is `F_p^* = p^Theta = p^{1/2} p^{iH}`, the flow of `Theta`
sampled at `t_D = log p`; any one-parameter group has this property, so it carries no information beyond
`Theta`, and it is the "commuting dilations" that `obs:prime-by-prime-blind` lists among the blind ansätze.
What distinguishes Deninger's picture from that ansatz is only that the leaf space is not a product over
primes, which the 2018 construction realises through the adele topology and not through a joint
eigenbasis. (c) is `obs:kraus-dichotomy` (c) once more: the `l^2(N)` metric makes the `mu_p` isometries at the
price of leaving no joint eigenvector normalisable on the critical line.

### R3. The local Lefschetz coefficient; the rotation angle per prime

**Proposition R3.** Let `gamma` be a closed orbit transversal to `F`, `x in gamma`, `A = T_x phi^{l(gamma)}
|_{T_xF} in GL(2,R)` the linearised Poincaré return map on the leaf plane.
(a) Deninger's coefficient of `delta_{k l}` (D3) is `c_k = det(1 - A^k) / |det(1 - A^k)|` for `k >= 1` and
`c_k = det(A^k) det(1 - A^{-k}) / |det(1 - A^{-k})|` for `k <= -1`, where `det(1 - B) = sum_i (-1)^i
Tr(Lambda^i B)` is the graded trace of `Lambda^* B`: the numerator is the graded trace of the exterior
algebra of the leaf plane, and `c_k` keeps only its sign (times `det A^k` for negative `k`).
(b) If `A = e^{l/2} O` with `O in O(2)`, then `c_k = 1` for all `k >= 1` iff `O in SO(2)`; if `det O = -1`
then `c_k = (-1)^k` for `k >= 1`. In both cases `c_k = e^{k l}` for `k <= -1`. (Deninger's Fact
`[D05:1095-1101]`, which uses `k = 1`.)
(c) For `O` the rotation by `theta`, the spectrum of `Lambda^* A` on `Lambda^0 (+) Lambda^1 (+) Lambda^2`
is `{1, e^{l/2} e^{+-i theta}, e^l}`: with `e^l = p`, the Frobenius spectrum on `H^0, H^1, H^2` of an
elliptic curve `E_p/F_p` with `a_p = 2 sqrt(p) cos theta` whenever that is an integer (Deuring: every `a`
with `|a| <= 2 sqrt(p)` occurs for `p` prime; not byte-cited; the reviewer verified it by enumeration for
`p <= 13`). A Weil number of higher degree gives a higher-dimensional abelian variety instead (the
reviewer's example `x^4 + x^2 + 4` over `F_2`, a simple surface). The Ruelle zeta uses only `c_k`, so
`theta` is invisible to `zeta`; the leafwise structure sees it.

*Proof.* (a) `det(1 - B) = 1 - Tr B + det B` for a `2 x 2` matrix. For `k <= -1`, `det(1 - A^k) =
det(A^k) det(A^{-k} - 1) = det(A^k) det(1 - A^{-k})` (even dimension), which is `[D05:1028-1037]`. (b)
`det(1 - u O^k)` with `u = e^{kl/2} > 1`: for a rotation by `k theta`, `1 - 2u cos(k theta) + u^2 = (u -
cos k theta)^2 + sin^2(k theta) > 0`; for a reflection, `O^k` is `O` for odd `k` and `1` for even `k`, so
`det(1 - u O^k) = 1 - u^2 < 0` for odd `k` and `(1 - u)^2 > 0` for even `k`. Then `c_k = sgn det(1 - A^k)`
for `k >= 1` and `c_{-k} = det(A^{-k}) sgn det(1 - A^k)`, with `det A^{-k} = e^{-kl}` and the sign
`+1` for a rotation; for a reflection and odd `k` the sign `-1` is compensated by `det(A^{-k}) =
e^{-kl} det(O)^{-k} = -e^{-kl}`, so `c_{-k} = e^{-kl}` in both cases. (c) Direct. QED.

*Reading.* The graded trace `det(1 - A^k) = |1 - (sqrt p e^{i theta})^k|^2` has ring zeta `zeta_{E_p}`;
Deninger's coefficient is that number divided by its absolute value, and the orbit's Ruelle factor is the
Euler factor `(1 - p^{-s})^{-1}`. So the notebook's superdeterminant reading of a ring zeta and Deninger's
Ruelle coefficient differ precisely by the `theta`-dependence that `zeta` does not see. The angle `theta_p`
is the notebook's `G3-T3-3` ("zeta data do not determine the physical state") made concrete: the
conformal-metric hypothesis carries one rotation per prime that the explicit formula never sees.

### R4. The metric is a flow-invariant polarisation of the symplectic odd bond

**Proposition R4.** Let `V` be a real vector space (the odd bond: `H-bar^1`, or a finite-dimensional
model), `B: V x V -> R` a nondegenerate alternating form (the cup product `H^1 x H^1 -> H^2 ~ R` followed
by `tr`, unique up to scale when there is a dense leaf `[D05:611]`), and `Theta` an endomorphism with
`B(Theta h, h') + B(h, Theta h') = alpha B(h,h')`.
(i) `g_t := e^{-alpha t/2} e^{t Theta}` lies in `Sp(V,B)`; the `B`-transpose satisfies `Theta^# = alpha -
Theta`, Leichtnam's "the transpose of `e^{t Theta}` is `e^t e^{-t Theta}`" `[L13:427-440]`, and the
spectrum of `Theta` is symmetric under `lambda -> alpha - lambda`. In finite dimension `Theta^#` is similar
to `Theta`, so there is a similarity `J` with `J Theta J^{-1} = alpha - Theta`, the operator form (FE) of
`def:graded-rh-fe-ramanujan`; `J` is not `B` and not canonical. Deninger's Poincaré duality on `H^1` is the
notebook's inverse pairing; a generic derivation has eigenvalues off the line (the reviewer's random
examples), so this is the functional equation without RH.
(ii) A *polarisation* is `*` with `*^2 = -1`, `B(*h, *h') = B(h,h')`, and `(h,h') := B(h, *h')`
symmetric positive definite. Deninger's `( , )` is of this form with `*` the leafwise Hodge star on 1-forms
(D4). If `[Theta, *] = 0` then `(Theta h, h') + (h, Theta h') = alpha (h,h')`, so `Theta = alpha/2 + S`
with `S` skew: the manifest form (HP) of `def:graded-rh-fe-ramanujan` with `G = ( , )`
(`prop:hp-inner-product-continuous`). Conversely, if `g_t` is `B`-symplectic and `( , )`-orthogonal with
`( , ) = B(., *.)`, then `[g_t, *] = 0`. So, given `B`, (HP) with a `B`-compatible form is exactly a
flow-invariant polarisation, and once it holds nothing remains to be proved; this is not the Kraus
dichotomy's case (d), where a unitary family still has Hastings' bound to satisfy (`obs:kraus-dichotomy`,
`num:weil-positivity`).
(iii) In leaf dimension two, `*` on 1-forms depends only on the conformal class of the leaf metric, so
Deninger's hypothesis is: the flow preserves the leafwise complex structure (the leaves are Riemann
surfaces and `phi^t` is leafwise holomorphic) and scales leaf area by `e^{alpha t}`; positivity of
`int h wedge *h` for a real 1-form is then automatic. The metric is not extra data beyond the complex
structure.
(iv) (Uniqueness.) Let `dim V = 2g` and let the return map `g_1 = e^{-alpha/2} e^{Theta}` be semisimple
with eigenvalues `e^{+-i theta_j}`, `theta_j in [0, pi]`. If the `theta_j` are pairwise distinct and in `(0, pi)` there is
exactly one polarisation commuting with `g_1`. If an eigenvalue `e^{i theta}`, `theta in (0,pi)`, is
repeated, let `(p,q)` be the signature of the Hermitian form `i B(v, conj w)` on its eigenspace (the Krein
signature); the invariant polarisations there form `U(p,q)/(U(p) x U(q))`, positive-dimensional iff
`pq > 0` and a point when the signature is definite. At `theta in {0, pi}` they form the Siegel space of
that eigenspace. If `g_1` has an eigenvalue off the unit circle, there is none. So "unique when it exists"
needs simple, or Krein-definite, spectrum.
(v) (What `B` buys.) For `g_1` with distinct angles the `g_1`-invariant alternating forms and the
`g_1`-invariant metrics have the same dimension `g` (`B = (+)_j b_j omega_j`, compatible metric `(+)_j |b_j|
1`; the reviewer's count), so imposing `B` removes the cone's freedom only when `B` is canonical, as the cup
product into `H^2 ~ R` is. `thm:arithmetic-metric` imposes only `Z^* H Z = r^2 H` and finds, for `K_HW` of
D2, a cone of real dimension four cut to one ray by parity and reality; `prop:d2-spectrum-frobenius` gives
`K_HW ~ H^1 (x) C^2` as a spectral similarity only (its ledger 14), so no cup form on `K_HW` is defined by
the notebook, and choosing one is choosing a point of the cone (S1).

*Proof.* (i) `d/dt B(g_t h, g_t h') = B((Theta - alpha/2) g_t h, g_t h') + B(g_t h, (Theta - alpha/2)
g_t h') = 0`. `B(Theta h, h') = B(h, (alpha - Theta) h')` is the definition of `Theta^#`. Symplectic maps
have `lambda -> 1/lambda` symmetric spectrum; a real matrix is similar to its transpose and `Theta^#` is
conjugate to `Theta^T` by the matrix of `B`. (ii) `(Theta h, h') + (h, Theta h') = B(Theta h, *h') + B(h,
*Theta h') = B(Theta h, *h') + B(h, Theta *h') = alpha B(h, *h')`. Conversely `B(gh, *gh') = (gh, gh') =
(h,h') = B(h, *h') = B(gh, g*h')` for all `h`, so `*g = g*` by nondegeneracy. (iii) On a surface `*` on
1-forms is the complex structure up to sign and is unchanged by `g -> e^{2f} g`; `h wedge *h = |h|^2 vol
>= 0`. (iv) `B(V_lambda, V_mu) = 0` unless `lambda mu = 1` by invariance, so `V = (+) E_j`,
`B`-orthogonally, with `E_j` the real subspace of the pair `e^{+-i theta_j}`; a polarisation commuting with
`g_1` preserves each `E_j` (distinct angles). On a two-dimensional `E_j`, `g_1` is an elliptic element of
`Sp(E_j, B) = SL(2,R)` conjugate to the rotation by `theta_j`, whose centraliser for `theta_j not in {0, pi}`
is that `SO(2)`; a complex structure in `SO(2)` is `+-` the rotation by `pi/2`, and `B(h, *h) > 0` picks
one sign. For a repeated angle the eigenspace `E` of `e^{i theta}` in `V (x) C` carries the Hermitian form
`i B(v, conj w)` of signature `(p,q)`, the centraliser of `g_1` on `E (+) conj E` is `U(p,q)`, and the
invariant polarisations are its fixed points in Siegel space, the symmetric space `U(p,q)/(U(p) x U(q))`
(the reviewer's tangent-space count: dimension `0` for `R_theta (+) R_theta`, `2` for `R_theta (+)
R_{-theta}`, `4` for `R_theta (+) R_theta (+) R_{-theta}`). At `theta in {0, pi}` the centraliser is
`Sp(E)` and the fixed set is its Siegel space. A non-unimodular eigenvalue has no invariant positive form.
(v) is the reviewer's dimension count and a restatement of what the notebook has. QED.

*Reading.* This is the precise form of "the metric": not a free positive form on the zero sector but a
complex structure on the symplectic odd bond, invariant under the transfer, and a point when the spectrum is
simple (or Krein-definite) and `B` is canonical. Existence is equivalent to (RH and semisimplicity); so it
is not a candidate metric in the sense of new data, it is RH in different words, as
`prop:hp-inner-product-discrete` already says for the sesquilinear version. What is new relative to the
notebook is the role of a canonical `B`: on Deninger's `H^1` the cup product is canonical and does the work
that the notebook did by symmetries; on the notebook's bonds no canonical `B` is known except at genus one
(R8). Deninger's Corollary 9 also gives a second positivity mechanism, `-(Theta - alpha/2)^2 =
Delta^1|_{ker Delta^1_F}` `[D05:852-858, 864]`: RH plus semisimplicity follows if `-(Theta - 1/2)^2` is a
nonnegative self-adjoint operator. It needs a Laplacian whose restriction is that operator, i.e. the flow
isometric up to scale, the same equivariance gap; and the metrics making the eigenplanes orthogonal form a
cone of dimension `3g` (the reviewer's count), so uniqueness belongs to the polarisation mechanism, not to
the programme.

### R5. Why compact manifolds force `alpha = 0`, and what a solenoid changes

**Proposition R5.** (a) If `X` is a compact oriented manifold, `phi^t` a flow transversal to `F` with the
invariant closed 1-form `omega_phi` (`omega|_{TF} = 0`, `omega(Y_phi) = 1`, `[D07:376-387]`), and `phi^t`
conformal on `TF` with factor `e^{alpha t}`, then `alpha = 0`.
(b) On Deninger's elliptic solenoid `X = (C x_Gamma T_pi Gamma) x_{p^Z} R^*_+` with `g = e^t Re(xi
conj(eta))`, the gluing `(z, y, t) ~ (pi^{-1} z, pi^{-1} y, t + log p)` is a `g`-isometry on leaves and
preserves flat area times the Haar measure of the transversal; the flow scales `g`-area by `e^s` and the
transverse measure `e^{-t} Haar dt` by `e^{-s}`; the return map `(z, y) -> (pi z, pi y)` expands `z` and
contracts `y` (`|pi|_p = p^{-1}`). Expanding leaves, a contracting transverse measure, and the invariant
`Omega` of (a) does not exist.

*Proof.* (a) `Omega = vol_F wedge omega_phi` is a volume form on `X`, `phi^{t*} Omega = e^{alpha t}
Omega` (the leaf area form scales by `e^{alpha t}` in leaf dimension two, `omega_phi` is invariant), and
`int_X phi^{t*} Omega = int_X Omega` for a diffeomorphism isotopic to the identity, so `e^{alpha t} = 1`.
(b) `g` is well defined on the quotient: `e^{t + log p} Re(pi^{-1} xi conj(pi^{-1} eta)) = e^t p |pi|^{-2}
Re(xi conj(eta)) = e^t Re(xi conj(eta))` since `|pi|^2 = p` `[D05:1226-1230]`, which says the gluing is a
`g`-isometry; the flat area scales by `|pi|^{-2} = p^{-1}` and the Haar measure of `pi^{-1}` times a
transversal by `p`; `T phi^s` is the identity on leaf tangents while the base point moves from `t` to
`t + s`, so `g` scales by `e^s`, and `e^{-t}` by `e^{-s}`. The return map is `[D05:1225]`. QED.

*Reading.* In the notebook's normalisations (`def:graded-transfer-channel`) this is the counting
normalisation (Perron root `q`, growth) against the channel normalisation (trace preservation, growth `1`):
on a compact manifold an invariant finite volume forces the trivial divisor's `q` and `1` to coincide, and
the solenoid separates them by paying for the leaf growth with a contracting transverse measure. Deninger's
"dissipative system with a compact attractor" `[D05:1232-1234]` is that contraction; no operator is
exhibited here, and the identification with the notebook's Lindbladian is dictionary. The adelic objects of
shard 04p are not solenoids of this type: `A/Q` is a solenoid `[D05:963-967]` but its `R`-action is
translation with no closed orbits, and `Q^{>0} Z^hat^x x_{Q^{>0}} R^{>0}` in the adele topology is
irreducible `[D18:3021-3023]`.

### R6. The elliptic example is the notebook's Hodge ket bond

**Proposition R6.** For an ordinary `E/F_p` with Frobenius `pi` and CM lift `C/Gamma`
(`asm:deuring-lift`, `def:lifted-frobenius-torus`; Deninger takes the maximal order `[D05:1206]`, a special
case):
(a) Deninger's leaf-space data `(H^*(C/Gamma, C), pi^*, (-1)^{deg})` is the notebook's doubled bond
`(V (x) V-bar, E-double = diag(1, conj(pi), pi, p), G-double = diag(1,-1,-1,1))` of
`thm:hodge-doubling-tensor`, with `V = Lambda^*(H^{1,0}) = C (+) C dz`; Deninger's `H^1` is the odd
sector `H^{1,0} (+) H^{0,1} = V_- (x) V-bar_+ (+) V_+ (x) V-bar_-`, and his `H^0 (+) H^2` the even sector.
(b) Deninger's Hodge inner product on `H^1`, `(h,h') = int h wedge *conj(h')`, is the inner product
induced on the doubled bond by the Hodge inner product on the ket bond `V` (`||dz||^2 = int dz wedge
*conj(dz)`), restricted to the odd sector.
(c) Conformality with factor `e^t` per period `log p` on `H^1` is the statement `||pi^* dz||^2 = |pi|^2
||dz||^2 = p ||dz||^2`, i.e. the ket-bond letter `A = diag(1, pi) = 1 (+) sqrt(p) U` with `U` unitary on
`V_-`: `thm:elliptic-ph-unitary`, where `|pi|^2 = p` is derived from the covering degree.
(d) The net `Theta`-spectrum of Deninger's solenoid on `H-bar^1` is `{s : p^s in {pi, conj(pi)}} + 2 pi i
Z/log p`, the zeros of `zeta_E`, and its trace formula is the explicit formula of `zeta_E` (Theorem
`[D05:1186-1201]`, `[D05:1225]`, with `thm:supertrace-rigidity`).

*Proof.* (a) `V (x) V-bar = Lambda^*(C dz (+) C dz-bar) = H^*(T^2, C)` graded by total degree
(`thm:hodge-doubling-tensor`); `pi^* dz = pi dz`, `pi^* dz-bar = conj(pi) dz-bar`, `pi^*(dz wedge dz-bar)
= p dz wedge dz-bar`. (b) The Hodge inner product on forms is multiplicative on wedge products of
orthogonal factors; `H^{1,0} = V_- (x) 1-bar`. (c) is (b) applied to `pi^*`. (d) is Deninger's theorem
read through R2(a)'s Poisson identity applied to the solenoid's Lefschetz data. QED.

*Reading.* At genus one everything is forced by Hasse and the test of "which metric" is vacuous
(`obs:gl1-bond-no-metric`, numerics D29–D30); Deninger's own verdict on his example is the same
`[D05:1230]`. For higher genus `thm:rosati-ph-genus-two` singles out the Hodge inner product on `H^{1,0}`
of the canonical lift by Rosati positivity, with `pi pi^dagger = q` free; in Deninger's Theorem 4 the
positivity of `( , )` is free (leafwise Hodge theory) and the missing input is the compatibility (11n). The
two reductions have their free and missing inputs exchanged; that they are "the same" is dictionary, with
Leichtnam's attribution of the star argument to Serre's Kähler analogue `[L13:423]` as its citable
support.

### R7. The model space `K_S` is not Deninger's `H^1` with an equivalent inner product

**Proposition R7.** (a) In Deninger's picture, with `( , )` positive and `Theta = 1/2 + A`, `A`
skew-adjoint on the completion `H^hat^1`, the eigenvectors of `Theta` at distinct zeros are orthogonal;
under pure point spectrum (an assumption: Corollary 9's hypotheses force `alpha = 0` `[D05:825]`, and
Remark b allows continuous spectrum `[D05:865-869]`) `H^hat^1 ~ l^2(zeros)` with `Theta` diagonal.
(b) Let `w_n = -gamma_n/2 - i(1 - sigma_n)/2` be the notebook's modes in `K_S = H^2 (-) S H^2`
(`prop:functional-model-modes`, `obs:model-modes-sign`), `k_n` the reproducing kernels. The normalised
kernels `k_n/||k_n||` are not a Riesz basis of their closed span. Consequently there is no bounded
invertible operator `T: H^hat^1 -> K_S` sending an orthonormal eigenbasis of Deninger's `Theta` to
multiples of the `k_n`, and no inner product on `K_S` equivalent to the Hardy inner product in which
`Z(t)` is normal with the `k_n` as eigenvectors. This holds unconditionally, and under RH the failure is
explicit: `rho(w_n, w_{n+1})^2 = (d_n/2)^2 / ((d_n/2)^2 + 1/4) <= d_n^2` for a gap `d_n = gamma_{n+1} -
gamma_n`, `liminf d_n = 0`, and already for two modes `sigma_min(G) <= 1 - sqrt(1 - rho^2)` by the
two-point identity `1 - |<k^_a, k^_b>|^2 = rho(a,b)^2`.

*Proof.* (a) `(Theta h, h') = (h, (1 - Theta) h')` gives, for eigenvectors at `rho, rho'`, `(conj(rho) -
1 + rho') (h,h') = 0` in the convention linear in the second slot, so `(h,h') = 0` unless `rho' = 1 -
conj(rho)`, which on the line is `rho' = rho`. (b) The normalised reproducing kernels of a model space
`K_B`, `B` a Blaschke product with simple zeros `(w_n)`, form a Riesz basis iff `(w_n)` is a Carleson
sequence, `inf_n prod_{m != n} rho(w_n, w_m) > 0` (Shapiro–Shields 1961, Nikolski, *Treatise on the shift
operator*, not byte-cited), and this requires uniform separation `inf_{n != m} rho(w_n, w_m) > 0`. Under RH
`Im w_n = -1/4` and the displayed formula holds; `N(T) ~ (T/2pi) log T` gives `liminf d_n = 0`.
Unconditionally, a positive proportion of zeros lies on the critical line (Selberg 1942, Levinson 1974,
Conrey 1989, not byte-cited), so among the zeros on the line below `T` the mean consecutive gap is
`O(1/log T)`, and consecutive on-line zeros with `Im w = -1/4` and gap `d -> 0` have `rho <= d`. The scalar
`S` may carry a singular inner factor beside its Blaschke part; the kernels `k_n` still lie in `K_S`
(`prop:functional-model-modes`) and the Riesz-basis criterion for the sequence `(k_n)` is the same Carleson
condition. A bounded invertible `T` maps an orthonormal sequence to a Riesz sequence, contradiction; an
equivalent inner product making `Z(t)` normal with eigenvectors `k_n` would make `(k_n/||k_n||')`
orthogonal, hence a Riesz basis for the Hardy norm. For two normalised kernels the Gram determinant is
`1 - |<k^_a,k^_b>|^2 = rho(a,b)^2`, which bounds `sigma_min` of any Gram matrix containing them by
interlacing. Numerics (`scratch_riesz.py`, first 3000 zeros): the nearest-neighbour `rho` has minimum
`0.097` (zeros 1496, 1497), and the smallest singular value of the Gram matrix of the normalised kernels is
`0.40, 0.23, 0.13, 0.075, 0.040, 0.016` for `N = 10, 25, 50, 100, 200, 400`, reproduced by the reviewer to
three digits and continued to `0.0059, 0.0013` at `N = 800, 1600`. QED.

*Reading.* `thm:arithmetic-metric` found, for the finite cavities, that the Lax–Phillips energy metric lies
outside the cone of `Z`-unitarising metrics on the same space. For `zeta` the statement is stronger: the
cone's metrics are not equivalent to the energy metric at all. `K_S` carries data Deninger's `H^1` discards,
the Gram matrix `<k_n, k_m> = i/(conj(w_n) - w_m)` of `prop:rebound-persistence-secular` and
`prop:mode-diagonal-rebound-rh` (04h, there written in the upper half plane), which encodes the cusp
coupling and the rank-one defect; Deninger's metric is the one in which that Gram matrix is the identity. A
Deninger completion of the notebook's odd bond is the space of mode coefficients with an inequivalent norm,
not a second inner product on `K_S`. This is not an obstruction to RH; it is an obstruction to identifying
the two odd bonds, and it says that H-THETA (`conj:h-theta`), if it holds, identifies `K_S` with something
that is not Deninger's `H^1`. The reviewer adds an unconditional route: `sum |Im w_n| delta_{w_n}` is not a
Carleson measure, unit boxes carrying mass `~ (1/4pi) log T` from on-line zeros alone.

### R8. The bond as an algebra: where the derivation mechanism can act

**Proposition R8.** (a) Deninger's `phi^{t*}` is a ring automorphism of the graded-commutative algebra
`H-bar^*(X, R)`, so `Theta` is a derivation, and the Leibniz rule on `H^1 cup H^1 -> H^2` with `Theta =
alpha` on `H^2` is the whole of the functional-equation half of R4(i).
(b) A completely positive map `E` on `End(V)` is multiplicative, `E(XY) = E(X)E(Y)`, iff `E = Ad(U)` with
`U` unitary; it is multiplicative up to a scalar, `E(XY) = c^{-1} E(X) E(Y)`, iff `E = c Ad(U)`. Composition
in `End(V)` is not the product Deninger's argument uses.
(c) At genus one the notebook's doubled bond is `H^*(T^2, C) = Lambda^*(C dz (+) C dz-bar)` with the
exterior product (R6(a)), and for that product the doubled transfer `A (x) conj(A)` is a ring endomorphism
for every even letter `A = 1 (+) a`, and an automorphism when `a != 0`, although `A = diag(1, pi)` is not a
scalar times a unitary; Deninger's derivation argument applies verbatim with `B` the `(-,-)` coefficient of
the wedge of two odd vectors, and its conclusion is `thm:elliptic-ph-unitary`. At genus two the doubled bond
`C^{1|2} (x) conj(C^{1|2})` has a four-dimensional `(-,-)` block and is not the cohomology ring of the curve
(`06f:215-221`: the curve's `H^*` sits inside `Lambda^* H^1(J)` behind a rank-six non-product projector). Whether any other notebook bond (`K_S`,
`K_HW`) carries a graded-commutative product for which its transfer is multiplicative up to scale is open.

*Proof.* (a) is D5. (b) A nonzero multiplicative map on the simple algebra `End(V)` is injective, hence
bijective, hence unital, so `E = Ad(A)` for an invertible `A` (Skolem–Noether, not byte-cited) and `c = 1`;
`X -> A X A^{-1}` is completely positive iff its Choi matrix is positive iff `A^{-1}` is a positive multiple
of `A^dagger`, i.e. `A` is a scalar times a unitary (the reviewer checked an indefinite Choi matrix for a
non-unitary `A`). Scaling by `c` gives the second statement. (c) `A (x) conj(A)` acts on `Lambda^*(C dz (+)
C dz-bar)` as the exterior algebra of the linear map `a (+) conj(a)` on the degree-one part, and exterior
powers of a linear map are multiplicative; the reviewer checked this on random pairs and checked that the
same map is not multiplicative for composition. The genus-two statement is `06f`. QED.

*Reading.* The notebook's bond is a vector space with a channel on it; Deninger's is an algebra with an
automorphism group, the functional equation is the Leibniz rule, and the metric is a complex structure
compatible with the product. The version-1 claim that the derivation mechanism acts only on
scalar-times-automorphism channels was false: the relevant product is the exterior product of the doubled
bond, not composition, and the genus-one Hodge ket bond has it. The open question is whether any bond of the
notebook beyond genus one carries such a product. The Bost–Connes system is, in this respect, on Deninger's
side: `sigma_t` is an automorphism group of an algebra, not a Lindbladian, and the KMS states are its
equilibria; what it lacks is the grading and the cohomology.

---

## Part III. What it suggests, and the comparative table

### S1. Is there a canonical `B` on `K_HW`?

The missing datum is a transfer-invariant polarisation of the symplectic odd bond (R4). Given a canonical
`B` and simple spectrum it is a point. On `K_HW` of D2 the reviewer computed, in the eigen-model of the
resonances of `2z^4 - 2z^2 + 1`: the unitarising cone has real dimension four (reproducing
`thm:arithmetic-metric`); the `Z`-invariant alternating forms `Z^T B Z = r^2 B` have real dimension two
after reality; every `B`-compatible polarisation is `Z`-invariant, hence inside the cone; and it lies on the
symmetric ray iff `B` is parity-invariant or parity-anti-invariant (`B_1 +- B_2` on the ray, `B_1 + 0.37
B_2` off it). So the computation proposed in version 1 is decided up to the choice it leaves open, and the
question for the next round is: does the D2 or D3 diagram, or a Hecke structure on it, supply an
alternating form on `K_HW` that is not a choice, and is it parity-(anti)invariant? If not, "the search is
for `B`" has no content on the finite cavities.

### S2. Same shortcoming, three ways

(a) Deninger reduces RH to a star commuting with the flow, which he says requires "the Kähler identities on
cohomology" for number fields `[D05:674]`, Serre's Kähler analogue `[L13:423]`; the notebook reduces RH to
(HP), which `thm:rosati-ph-genus-two` obtains from Rosati positivity. The two reductions exchange their free
and missing inputs (R6 Reading); that they are the same reduction is analogy. (b) The one realised Deninger
system is the lifted ordinary elliptic curve (R6), where the metric is the Hodge inner product of the lift
and RH is Hasse; the notebook has the same object with the same caveat. (c) The 2018 spaces have no analytic
structure `[D18:559]`, are infinite-dimensional `[D18:2416]`, get their `H^0 = R` (Deninger's `H^0`, the
notebook's even line being his `H^2` by R1) from an irreducible leaf space on which every continuous
function is constant `[D18:3021-3023, 3068]`, and map `Q^{>0}`-equivariantly into Connes's adele space
`[D18:2363-2411]`, so the 2018 route inherits the Connes row's missing datum, Weil positivity. Added by this
note: (d) the notebook's `K_S` cannot be Deninger's `H^1` up to equivalent norm (R7).

### S3. The prime letters carry nothing beyond `Theta`

R2 says Deninger's jump at `log p` on the odd sector is `F_p^* = p^Theta`, one flow sampled at `log p`; in
notebook normalisation `Z(2 log p)` with eigenvalues `p^{conj(rho) - 1}` of modulus `p^{-1/2}`. These commute
and share the modes by construction, so no test of them says more than R7 already says about `Z(t)`. For
HANDOFF's step 2 (the Stinespring form with jumps at `k log p`) the lesson is negative: commuting jump
operators that are functions of the compressed dilation are the blind ansatz of `obs:prime-by-prime-blind`,
and Deninger's construction escapes it only by the topology of its leaf space, not by the operators.

### S4. One angle per prime is data zeta does not see

R3: with a conformal metric, the return map at the prime `p` is `sqrt(p)` times a rotation by an angle
`theta_p` that `zeta` does not see; when `2 sqrt(p) cos theta_p` is an integer, Deuring gives an elliptic
curve over `F_p` with that trace, and otherwise a Weil number of higher degree gives a higher-dimensional
abelian variety. This is the notebook's finding that three tensors share the ring norms of one curve
(`G3-T3-3`) with part of the selection data named: `{theta_p}`. The angles are local data at closed orbits
and the metric is a polarisation on `H^1`; no proposition here relates the two, so the absence of a candidate
`theta_p` for `zeta` is a separate statement from the absence of a candidate metric. For the cavities of 04k
the local question is whether the return map of the cusp orbit of D2 or D3, linearised on the odd sector, is
`q^{1/2}` times a rotation, and what the angle is.

### S5. Solenoid, contraction, and the adelic bond

R5: `alpha = 1` needs expanding leaves paid for by a contracting transverse measure. The adelic objects of
shard 04p are not such suspensions (R5 Reading). What D18 does supply is the packet structure: the periodic
orbits of the prime `p` form a compact family over `Z^hat^x_{(p)}/p^{Z^hat}`, which is `Z^hat^x =
Gal(Q^ab/Q)` modulo the decomposition group at `p` (inertia `Z_p^x` and the closure of Frobenius), the set
of primes of `Q^ab` above `p`; this is the Galois structure `conj:galois-graded-bond` asks the bond to carry,
attached here to the orbits rather than to the modes. The closure of the periodic orbits being the unitary
characters `[D18:2441]` says the geometric core of the 2018 system is a Pontryagin-dual object. Candel's
theorem gives, for `Q`, one parabolic leaf `[D05:1124]`, not a statement about all leaves.

### S6. The supertrace as a transverse index

Deninger reads the left side of the Lefschetz formula, through harmonic forms, as "the `D'(R)`-valued
transverse index of the leafwise de Rham complex", transversally elliptic for the `R`-action, and says the
relation to Connes–Moscovici transverse index theory "still needs to be clarified" `[D05:785-787]`; the
McKean–Singer form `str(phi^{t*} e^{-s Delta_F})`, independent of `s`, is this note's gloss, not the
source. In the notebook's language the physical fermions of the graded cMPS are the leafwise forms, the
"ring norm = supertrace" identity is index-like, and the dissipative generator whose kernel is the bond
would be the leafwise Laplacian, Deninger's dictionary line "transversal index theorem for the `R`-action
and Laplacian along the leaves" `[D07:425]`. Two generators rather than one (`Delta_F` with kernel the
bond, `Theta` the flow on the kernel), the wave equation `-(Theta - alpha/2)^2 = Delta^1` of R4's Reading,
Cramér's function `[D07:681-700]`, and the reading that with `alpha = 1` the dissipative content of the odd
sector is the scalar `e^{-t/2}` are dictionary.

### The comparative table

One row per attack, the columns the cMPS ingredients; entries are what the notebook has recorded, with
this note's additions in the Deninger row. "Product" means a graded-commutative multiplication on the bond
for which the transfer is multiplicative up to scale (R8(c)).

| attack | bond | transfer / flow | grading and sign | pairing (FE) | metric: where positivity comes from | product | what it lacks |
|---|---|---|---|---|---|---|---|
| Artin–Schreier (06, 06b) | `C^q` additive characters | `E`, `E E^dagger = q` | super-transfer: even = trivial character, odd = nontrivial | `S_n` sign law; Weil representation of `M_g` | Parseval, given in advance | not recorded | only quadratic `g`; nothing to choose |
| Weil, curves (06f) | `H^1(J)`, `H^{1,0}` of the lift | Frobenius `pi` | cohomological degree; `H^1` odd | Poincaré duality `pi ~ q pi^{-1}` | Rosati positivity = Hodge index on `C x C`; supplied, not derived | yes: cup product, Frobenius a ring map | liftability (`asm:deuring-lift`); moduli not in the counts |
| Deligne (07) | tensor powers of `H^1` | Frobenius | odd numerator | Poincaré duality | none: positivity of even tensor powers + a base curve | yes: Künneth on `X x X` | no inner product |
| LPS / Weil–LPS channels (05) | `l^2(F_p)` | mixed-unitary `sum Ad(U_i)/D` | ungraded; Hastings bound | adjoint pairing only | Hilbert–Schmidt; one-sided bound only (`thm:kraus-weil-criterion`) | no | duality; assembly over `p` |
| quantum Ihara (08, 08b, 08c) | edge space | Hashimoto `H`, `Sigma` | graded by the Kraus dichotomy | inverse pairing buys FE, adjoint buys reality | both pairings iff unitary, and then Hastings' bound remains | no | a family with both pairings that is not already unitary |
| Lax–Phillips / Riemann channel (04, 04h) | `K_S = H^2 (-) S H^2` | compressed dilation `Z(t)`, c.n.u. | `C_+ (+) K_S (+) ladder`, str `= 2P_+` (04b) | `S(-tau) = 1/S(tau)` on the boundary; no operator `J` on `K_S` (semigroup) | energy metric; modes not orthogonal, not a Riesz basis (R7) | none known | the metric; the rebound (04h) |
| Bost–Connes (04c, 04d) | `l^2(N)`, product over primes | `sigma_t = Ad(N^{it})`, automorphisms | none | none | KMS, `beta > 1` only (`prop:normal-kms-gibbs`) | yes: an algebra with automorphisms | grading, cohomology, the zeros (`obs:prime-by-prime-blind`) |
| Connes adele class space (cit.) | `L^2(A/Q^x)` modulo | scaling | absorption spectrum: zeros as `(-) H` | Poisson = FE | Weil positivity as the criterion, not a metric | no | the positivity |
| Deninger (this note) | leafwise cohomology of a lamination; odd = leaf 1-forms | flow `phi^{t*}`, ring automorphisms; `F_p^* = p^Theta` per prime (R2) | `(-1)^i`; the twist of 04b (R1); archimedean = `R_infty` ladder (R1d) | cup product, `Theta` a derivation, `Theta^# = 1 - Theta` (R4, R8) | leafwise Hodge star commuting with the flow = invariant polarisation, a point for simple spectrum and canonical `B` (R4); or a Laplacian with `-(Theta-1/2)^2` (R4 Reading); needs "Kähler identities on cohomology" | yes: cup product and Künneth; realised in the notebook only on the genus-one Hodge ket (R8) | the space (2018: infinite-dimensional, no analytic structure, over Connes's adele space); the star; a rotation angle per prime (R3) |

What the table shows for TJO's programme of assembling clues: the attacks that have a metric (Artin–Schreier,
Weil, Deninger on elliptic curves) either have it given in advance (Parseval) or have a product on the bond
with a multiplicative transfer and a positivity supplied from outside (Hodge index); the attacks without a
product (channels, Lax–Phillips, Connes) have only one-sided bounds or criteria. Deninger's column is the
one that supplies, conjecturally, the product for `Spec Z` (Künneth for `X x X`, the ingredient the README
says `zeta` lacks for a Deligne-type argument), and the notebook's column is the one that supplies the
concrete odd bond with its Gram data and the exit structure. The two do not meet on the same space (R7), and
the 2018 realisation of Deninger's column is fibred over the Connes row `[D18:2363]`.

---

## Part IV. Verdict on the metric, and next steps

No candidate metric emerges from Deninger's programme beyond the inequivalent diagonal form on mode
coefficients, which is RH. His mechanism (a Hodge star on the odd bond commuting with the transfer) is the
notebook's manifest form (HP) with the functional equation supplied by the cup product, and his own
assessment is that it will not exist as a metric on forms for number fields and must be replaced by the
Kähler identities on cohomology; his second mechanism, a Laplacian with `-(Theta - 1/2)^2` as its
restriction, has the same equivariance gap. The programme is a reformulation with the same gap, reinforced
by the 2018 construction, which lands on Connes's adele space and derives its one cohomological fact from an
irreducible leaf space.

What is gained is the shape of the gap: (1) the metric is a flow-invariant polarisation of the symplectic
odd bond, a point when the spectrum is simple (or Krein-definite) and the symplectic form is canonical; the
notebook has no canonical `B` on any bond except the genus-one Hodge ket, where it is the cup product; (2)
at genus one the doubled bond carries Deninger's product and his argument verbatim, and whether any other
notebook bond carries a product for which the transfer is multiplicative up to scale is the open structural
question; (3) the archimedean ladder is Deninger's `R_infty`, its parity in a graded operator a matter of
which side of the trace formula it sits on, with the notebook's exact-equality choice fixing it; (4) the
prime letters are one flow sampled at `log p`, which is the blind ansatz unless the leaf space is
non-product, and the conformal hypothesis adds one rotation angle per prime as data `zeta` does not fix;
(5) `K_S` is not Deninger's `H^1` under any equivalent norm.

Next, in order. (i) S1: a canonical alternating form on `K_HW` from the diagram or a Hecke structure, and its
parity behaviour (finite, the cavity scripts and the reviewer's eigen-model exist). (ii) A graded-commutative
product on `K_HW` or on a finite model of `K_S` for which `Z` is multiplicative up to scale (R8(c), open).
(iii) S4: the linearised return map of the cusp orbit of D2 and D3 on the odd sector. (iv) The Laplacian
route on the modular surface: the Lax–Phillips shards have a Laplacian and the zeros as resonances, not
eigenvalues; state precisely why `[D05:864]` fails there. (v) D18 over Connes: write the fibre of `X~` over
`A^{>0}_{(p)}` in the language of shard 04d's Bost–Connes MPOs. (vi) Register: R1 (proved), R2(a) and (c)
(proved), R3 (proved), R4 (proved), R5 (proved), R6 (proved-conditional on `asm:deuring-lift`), R7 (proved;
the Riesz-basis theorem and the positive-proportion theorem not byte-cited), R8(b)–(c) (proved), with `cit:`
rows for D5–D7.

## What is theorem and what is dictionary

| statement | status |
|---|---|
| R1 (a)–(d): transport, equivalence with `prop:ringnorm-trace`, `div zeta-hat = div zeta + div Gamma_R`, the `R_infty` ladder | theorem (elementary; (a) is printed under `cor:forced-net-spectrum`; the reviewer re-verified to `1e-15`) |
| "the `Gamma_R` ladder is the jet trace at the archimedean fixed point" | dictionary, resting on Deninger's conjecture `[D05:756, 1038-1041]` |
| R2(a) for a diffeomorphism of a compact manifold; the solenoid case via Deninger's theorem | theorem |
| R2(b): joint eigenvectors for `Q^{>0}` | formal (depends on a leafwise cohomology of the 2018 space that is not computed) |
| R2(c): Bost–Connes joint eigenvectors and orthogonality with all primes | theorem (elementary) |
| R3(a)–(c) | theorem (elementary); the Deuring sentence not byte-cited |
| R4(i)–(v) | theorem (linear algebra); the Krein statement in (iv) from the reviewer's count |
| R5(a), (b) | theorem (elementary) |
| R6(a)–(d) | theorem, conditional on `asm:deuring-lift` (Deninger: maximal order) |
| R7 | theorem, two standard results not byte-cited; numerics reproduced by the reviewer |
| R8(b): multiplicative CP maps are `Ad(U)` | theorem (Skolem–Noether and Choi, not byte-cited) |
| R8(c): the genus-one doubled bond is a cohomology ring with a multiplicative transfer | theorem (`thm:hodge-doubling-tensor`, `thm:elliptic-ph-unitary`) |
| S1's outcome: the `B`-point is in the cone, on the ray iff `B` is parity-(anti)invariant | the reviewer's computation, not registered here |
| "the metric is the missing datum in Deninger too" | Deninger's own words `[D05:674, 1230]`, `[D18:559]`, reinforced by `[D18:2363-2411, 3021-3068]`; dictionary beyond that |
| "Deninger's reduction = Rosati positivity"; the Lindbladian reading of the contraction; S3–S6 | dictionary and suggestions, not claims |

## Correction ledger (review of 2026-09-23, 30 items, all applied)

| # | where | change |
|---|---|---|
| 1 | R1 Reading | `Gamma_C` has one simple pole per nonpositive integer; `Gamma_C = Gamma_R(s)Gamma_R(s+1)`; two incoming orbits match the two `Gamma_R` factors |
| 2 | R1(d), ledger | Atiyah–Bott dropped; the ladder is Deninger's Proposition 2.1 `[D05:204-215, 286-296]`; the jet reading is dictionary on his conjecture |
| 3 | R1(a) | "twist by −1" renamed the twist `H(1)`; the transport is printed under `cor:forced-net-spectrum` |
| 4 | Answer, Part IV (3) | "fixes/settles the parity" replaced by "explains it as bookkeeping; `prop:ladder-parity-free` fixes it by exact equality" |
| 5 | D2, R1(c) | the forced shape is conditional on distinct eigenvalues `[D05:317-319]`; `N` is a net datum with a cancellation that hypothesis excludes |
| 6 | R2(a), R6(d) | `pi` on `E(C)` is a degree-`p` covering, not a diffeomorphism; the solenoid and Deninger's Theorem `[D05:1131-1160, 1186-1201, 1205-1225]` used instead |
| 7 | R2(b) | product leaf spaces: a common exponent needs `p^rho` in every local spectrum; Euler factors force `rho = 0` |
| 8 | R2(c) | orthogonality with all primes (two with `log p/log q` irrational suffice); `v_rho` exists for every `rho`, nothing selects the zeros |
| 9 | R2 Reading, S3 | D18 couples the primes by the adele topology `[D18:2292-2322]`, not by a joint eigenbasis |
| 10 | R3(b) | `c_k = (-1)^k` for a reflection, `k >= 1`; `c_k = e^{kl}` for `k <= -1` in both cases |
| 11 | R3 proof | address `[D05:1028-1037]` |
| 12 | R3 Reading, S4 | the Honda–Tate sentence deleted; Deuring with the integrality condition; a higher-degree Weil number gives a surface; the graded trace versus its sign |
| 13 | R4(i) | `B` gives the transpose `Theta^# = alpha - Theta` `[L13:427-440]`; the similarity `J` is non-canonical |
| 14 | R4(iv), proof | Krein-signature statement for repeated angles; `U(p,q)/(U(p) x U(q))`; the false "`Sp(4)` for repeats" removed |
| 15 | R4 title, Answer, Part IV (1) | "unique when it exists" conditioned on simple or Krein-definite spectrum and a canonical `B`; invariant `B` and invariant metrics have the same dimension |
| 16 | R4(ii), Answer | "Kraus dichotomy case (d)" replaced by (HP) with `prop:hp-inner-product-continuous`; nothing remains, unlike case (d) |
| 17 | R4(v), S1 | `K_HW ~ H^1 (x) C^2` is a spectral similarity only; S1 restated as "a canonical `B`, parity-(anti)invariant?"; outcome 3 deleted; "alternating on `C^2`" dropped |
| 18 | R5(b) | flat area versus `g`-area; the return map, not the flow, contracts the transversal; the invariant `Omega` does not exist |
| 19 | R5 Reading, S5 | `A/Q` and `R_+^x x Z^hat^x` are not solenoids of this type; `[D18:3021-3023]` |
| 20 | R6 | `[D05:674]`; Serre via `[L13:423]`; Deninger's maximal order |
| 21 | R7 | Gram matrix `i/(conj w_n - w_m)`; labels `prop:mode-diagonal-rebound-rh`, `prop:rebound-persistence-secular`; two-point bound in place of "monotone"; "equivalent" inserted; pure point spectrum as an assumption |
| 22 | R8 | (b) corrected to `Ad(U)`; (c) and the Reading replaced by the cup-product statement; Part IV (2) and the table's product column redone; re-verdict: endomorphism, automorphism iff `a != 0`; "not the cohomology ring of the curve" |
| 23 | S2(c) | `H^0 = R` is Deninger's `H^0`; the notebook's even line is his `H^2` |
| 24 | S3 | `Z(2 log p)`, eigenvalues `p^{conj(rho)-1}`; the "cheap test" dropped as re-testing R7 |
| 25 | S5 | Candel gives one parabolic leaf; `Z^hat^x_{(p)}/p^{Z^hat}` is modulo the decomposition group |
| 26 | S6 | the heat-kernel identity marked as this note's gloss; `[D05:785-787]` quoted |
| 27 | table | `F_p^* = p^Theta`; D18 over Connes added to the closing paragraph |
| 28 | Part IV | "inequivalent diagonal form on mode coefficients"; D18 has a metric-space metric `[D18:2205]` but no Riemannian or leafwise metric |
| 29 | R4 Reading, S2, Part IV | the Laplacian route `[D05:852-869]` and the map into Connes's adele space `[D18:2363-2411]` added |
| 30 | labels | `sec:artin-schreier`; addresses `[D07:376-387]`, `[D05:1225]`, `[D05:1020-1022, 1066-1072, 383-398]` |
