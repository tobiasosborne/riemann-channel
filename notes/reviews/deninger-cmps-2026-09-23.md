# REFUTE review: Deninger's programme in the supertrace-cMPS language (R1–R8, S1–S6)

Reviewer: `claude:opus` (adversarial lane, REFUTE protocol).
Date: 2026-09-23. Author under review: `claude:fable-5.1`, `notes/deninger-cmps/reformulation.md` (600 lines,
written alone, no brief, no blind numerics lane). This review does not edit that file.

## Inputs read

| file | what it is |
|---|---|
| `notes/deninger-cmps/reformulation.md` | the note under review, in full: D1–D7, R1–R8, S1–S6, the comparative table, Part IV, the ledger |
| `notes/deninger-cmps/scratch_riesz.py` | the author's own check for R7 (read; not imported, not reused) |
| `refs/src/math/0505354/main.tex` (`[D05]`) | Deninger 2005, read in full lines 1–1240 (§§1–6); §7 (arithmetic topology) skimmed to 1638 |
| `refs/src/0709.2801/main.tex` (`[D07]`) | Deninger 2007, read in full (§§1–6, 741 lines) |
| `refs/src/1807.06400/main.tex` (`[D18]`) | Deninger 2018: introduction (484–578) and §§6–10 (1983–3074) in full; theorem statements of §5 |
| `refs/src/1307.3851/main.tex` | Leichtnam: 60–210 and 380–445 (the Hodge-star argument, the Γ-factor sentence) |
| `report/sections/02c, 02g, 02h, 03, 04, 04b, 04c, 04f, 04h, 04k, 04l, 04n, 04o, 04p, 06c, 06d, 06f, 08c, 10` | every notebook label the note cites (35 labels), read at its definition with enough context for its conventions |
| `HANDOFF.md:1141-1146`, `notes/ideation-ledger-2026-09-19/digests/G3-prover-campaigns.md:120-125` | "open step 2" and `G3-T3-3`, both quoted by the note |
| `notes/reviews/gl1-bond-2026-09-21.md` | house format and standard |

## Scripts written by this lane (independent; nothing imported from `scripts/` or from the author's script)

| script | checks | covers |
|---|---|---|
| `notes/reviews/scratch_den_r1.py` | **65** | Deninger's explicit formula on `R^{>0}` in Deninger time with Gaussian test functions and the 3000 zeros (4 test functions, `|lhs-rhs| <= 3.3e-15`), plus the wrong `kappa = -1` and the missing `H^0` term (both fail by `>1e-4`); **R1(b) in notebook time** and **`prop:ringnorm-trace`** (3 test functions each, `<= 1.4e-15`), with the weight `Lambda(n)/n` without the 2 (off by `1.2e-3 .. 1.4e-2`) and the support `t = log n` both failing; the pointwise identities of the proof; `zeta-hat` residues `-1` at 0 and `+1` at 1, finite at `-2,-4,-6`; `Gamma_R` simple poles; **`Gamma_C(s) = Gamma_R(s)Gamma_R(s+1)`** to `1e-25` and **one simple pole of `Gamma_C` per nonpositive integer**; **Deninger's Proposition 2.1** (`[D05:204-215, 286-296]`) by zeta-regularised determinants through the Hurwitz zeta, real and complex places, 3 points each, to `1e-20` |
| `notes/reviews/scratch_den_r2r3.py` | **90** | Poisson trace of a one-prime suspension (6 cases, `<= 4e-14`); the lifted `pi = 1+2i` on `C/Z[i]` has degree 5; Bost–Connes vectors `v_rho` are joint eigenvectors of every `mu_p^*` for **arbitrary** `rho` (truncation `N = 2*10^5`); the one-prime orthogonality loophole; Deninger's coefficient (34) against the superdeterminant form for rotations and reflections, `k = -6..6`; **Deuring by exhaustive enumeration** of all Weierstrass curves over `F_2, F_3, F_5, F_7` and short ones over `F_11, F_13`; a Honda–Tate counterexample; solenoid measure bookkeeping at `p = 5` |
| `notes/reviews/scratch_den_r4.py` | **52** | R4(i)–(ii) on random examples; **fixed sets of `g_1` in Siegel space by tangent-space dimension** for eight spectral configurations; invariant alternating forms against invariant metrics; the **eigen-model of `K_HW` of D2** (resonances of `2z^4-2z^2+1`), its unitarising cone, its invariant alternating forms, reality, parity, and the `B`-compatible polarisation; Deninger's Laplacian route and the dimension of its metric cone |
| `notes/reviews/scratch_den_r7.py` | **58** | pseudo-hyperbolic distances of the 3000 modes; the Gram matrix by quadrature in the note's lower-half-plane convention; the two-point identity `1 - |<k^_a,k^_b>|^2 = rho(a,b)^2`; `sigma_min` of the normalised Gram matrix for `N = 10 .. 1600`; the Carleson-measure test in unit boxes; truncated Carleson products; the S3 normalisation |
| `notes/reviews/scratch_den_r8.py` | **13** | multiplicativity of `c Ad(U)`, `X -> AXA^dag`, `X -> AXA^{-1}` (and its Choi matrix); **the doubled Hodge-ket transfer is a ring automorphism of the exterior (cup) product and is not multiplicative for composition in `End(V)`** |

**278 checks, 0 failures.** Every number below is from these scripts unless attributed to the author.

---

## Citations byte-checked

**Deninger addresses.** The note uses **59 distinct** `[D05:…]`, `[D07:…]`, `[D18:…]` addresses. I opened
every one. **52 are exact or within four lines of the content.** The seven that are not:

| address in the note | what it is used for | verdict |
|---|---|---|
| `[D05:676]` (R6 Reading) | "one will need the Kähler identities on cohomology" | **wrong line**: the sentence is `:674`; `:676` is `\begin{theorem}` |
| `[D05:1040-1046]` (R3 proof) | "agrees with" the `k <= -1` coefficient | **wrong lines**: the uniform coefficient is eq. (34)–(35), `[D05:1028-1037]`; `:1038-1041` is the *conjectured* fixed-point term and `:1042-1046` Remark 3 (manifold case) |
| `[D05:1213-1224]` (R6(d)) | "its trace formula is the explicit formula of `zeta_E`" | **off**: `:1213-1224` is the suspension and the Tate module; the sentence is `[D05:1225]` |
| `[D05:383-395, 1020-1027]` (D3) | `W_x = eps_x e^t |1-e^{kappa|t|}|^{-1}` on `R^{<0}` | **partly off**: `:1020-1022` has `det(-T_x phi^t | T_xF)`, not `e^t`; the `e^t` form is `[D05:1066-1072]` (conformal case) and `[D05:395-398]` (number fields) |
| `[D07:370-378]` (R5(a)) | the form `omega_phi` | **off by six**: Construction 2.3 is `[D07:376-387]` |
| `[D05:785-789]` (S6) | "McKean–Singer: `sum (-1)^i Tr(phi^{t*}|H^i) = str(phi^{t*} e^{-s Delta_F})` for every `s > 0`" | **overreach**: the source says only that via harmonic forms the left side "becomes the `D'(R)`-valued transverse index of the leafwise de Rham complex", and that the relation to Connes–Moscovici transverse index theory "still needs to be clarified" (`:785-787`). No heat-kernel identity is stated, and the trace of Theorem 7 is defined on the Hilbert completion `H^^n` (`:767-775`), not on forms |
| `[D05:316-326]` (D2) | "forcing `H^0 = R` …" | **softened paraphrase**: Deninger's inference is conditional, "If we assume that the eigenvalues of `Theta` on `H^i_dyn` are distinct for `i = 0,1,2`" (`:317-319`). This assumption matters for R1(c) (below) |

Two paraphrases stretch without a wrong address: `[D18:559]` ("no metric and no complex structure") — the
line says "we have yet to define analytical structures on our spaces"; D18 *does* construct a metric in the
metric-space sense (`[D18:2203-2205]`, Proposition t86), so "no Riemannian or leafwise metric" is the correct
reading. And `[D05:674-676]` is quoted exactly but glossed as "which is Rosati positivity" (dictionary; see S2).

**Leichtnam `1307.3851`** is cited only for "ramified leafwise flat bundles" (true, `:73-76`). The note misses
two byte-citable lines it needs: `:420-421` ("This argument comes from an idea of Serre … formalized in the
foliation case in [D-S]"), which is the only source-level support for the note's "Kähler identities = Rosati"
analogy; and `:427-440` ("the transpose of `e^{tTheta}` is `e^t e^{-tTheta}`"), which is the correct form of
R4(i) (see R4).

**Notebook labels.** 35 labels cited; I located each with `grep 'label{…}'`. **Two do not exist:**
`prop:mode-diagonal-rebounds` (it is `prop:mode-diagonal-rebound-rh`, `04h:161`; the Gram formula the note
quotes is printed at `prop:rebound-persistence-secular`, `04h:155`, and `thm:rebound-renewal`(iii), `04h:90`)
and `sec:artin-schreier-mps` (it is `sec:artin-schreier`, `06:10`). The others exist and are used with their
printed statements except where a verdict below says otherwise (`obs:kraus-dichotomy` (d),
`prop:d2-spectrum-frobenius`, `cor:forced-net-spectrum`, `obs:prime-by-prime-blind`).

**Standard theorems marked "not byte-cited".**

| theorem | as used | verdict |
|---|---|---|
| Shapiro–Shields (1961), Nikolski (*Treatise*) | normalised kernels of `K_B`, `B` Blaschke with simple zeros, are a Riesz basis iff the zeros are Carleson; Riesz ⇒ uniformly separated | **correctly stated as used** |
| Levinson (1974), Conrey (1989) | a positive proportion of zeros on the line | **correct**; Selberg (1942) is the original positive-proportion theorem and suffices |
| Skolem–Noether | automorphisms of `End(V)` are inner | **correct theorem, misapplied**: the step "multiplicative ⇒ automorphism" needs nonzero ⇒ injective ⇒ bijective ⇒ **unital**, which forces `c = 1`; see R8 |
| Deuring | every `|a| <= 2 sqrt p` is a trace of Frobenius over `F_p` | **correct**; verified by enumeration for `p = 2,3,5,7,11,13` |
| Atiyah–Bott | "the trace of the flow on the jets of the normal line at the archimedean fixed point" | **misattributed**: the fixed-point term of a foliated flow is Deninger's *conjecture* (`[D05:1038-1041]`; "The conjecture is not known … if `phi` has fixed points", `[D05:756]`), and the leafwise complex at a fixed point is not transversally elliptic (`:756`). The bosonic ladder itself is byte-citable as Deninger's **Proposition 2.1** (`[D05:204-215, 286-296]`), which the note does not cite |

---

## Verdicts

### R1. The Tate-twist identity of graded spectral data

**VERDICT R1: MINOR.** Statements (a)–(d) and the proof are correct, every sign and factor 2 included; the
defects are in the Reading, one citation, and the framing.

*What holds, recomputed.* Deninger's formula on `R^{>0}` (`[D05:878-880]`, `[D07:433]`) paired with
`phi(t) = exp(-(t-t0)^2/2s^2)`, `Phi(rho)` in closed form, 3000 zeros and both signs of `gamma`:
`Phi(0) + Phi(1) - sum_rho Phi(rho) = sum log p phi(k log p) + int phi/(1-e^{-2t})` at
`(t0,s) = (1.2,.05), (2.0,.03), (2.9,.02), (0.8,.06)` with residuals `3.3e-16 .. 3.3e-15`. With `kappa = -1`
or without the `H^0` term the identity fails by more than `1e-4`. In notebook time `t = 2t_D`,
`1 + e^{-t/2} - Tr_d Z(t) = 2P_+(t) + sum_{k>=0} e^{-(k+1/2)t}` holds at `(t0,s) = (2.4,.06), (4.0,.04),
(5.5,.03)` to `<= 1.4e-15`, and `prop:ringnorm-trace` holds in its printed form to the same precision; the
weight `Lambda(n)/n` without the 2 misses by `1.2e-3, 7.2e-3, 1.4e-2`, and the support `t = log n` misses
too. So the Jacobian `delta(t_D - a) = 2 delta(t - 2a)` is right and `t = 2t_D` is used consistently in R1.
(d): `zeta-hat = pi^{-s/2}Gamma(s/2)zeta(s)` has residue `-1` at 0 and `+1` at 1 and is finite and nonzero at
`-2,-4,-6` (`0.19131, 0.07880, 0.06098`), so the trivial zeros cancel the `Gamma_R` poles, and
`nu(zeta) + nu(Gamma_R) = D` exactly as the proof says.

**Defect 1 (Reading, false).** "Complex places give `kappa = -1`, jets at `-k`, the poles of
`Gamma_C(s) = 2(2pi)^{-s}Gamma(s)`: the two incoming orbits of `[D18:2036-2052]` are the two poles' worth
of jets per integer." `Gamma_C` has **one** simple pole at each `s = -k` (residues `2, -4pi, 4pi^2, ...` =
`2(-2pi)^k/k!`, checked `k = 0..4`), and Deninger's own spectrum for a complex place is `{-nu : nu >= 0}`
with multiplicity one (`[D05:294-296]`). What is true, and checked to `1e-25`, is the duplication identity
`Gamma_C(s) = Gamma_R(s)Gamma_R(s+1)`, i.e. `(1-e^{-t})^{-1} = (1-e^{-2t})^{-1} + e^{-t}(1-e^{-2t})^{-1}`:
one `kappa = -1` ladder is two interleaved `kappa = -2` ladders. *Corrected sentence:* "A complex place has
`kappa = -1` and one simple pole of `Gamma_C` at every nonpositive integer; since `Gamma_C(s) =
Gamma_R(s)Gamma_R(s+1)`, its ladder is the union of two real ladders (even and odd integers). Deninger's two
incoming orbits at a complex point (`[D18:2052]`), which he says he deduced from `Gamma`-factors, match the
two `Gamma_R` factors, not two poles per integer."

**Defect 2 (misattribution).** R1(d) and the ledger call the jet ladder "Atiyah–Bott, not byte-cited" and
file it under "theorem (elementary)". The identity `sum e^{-2kt} = (1-e^{-2t})^{-1}` is elementary; its
reading as "the Lefschetz contribution of a fixed point" is Deninger's conjecture (`[D05:756, 1038-1041]`).
The ladder as a *cohomology* is Deninger's Proposition 2.1: `R_inf = R[exp(-2y)]` with `Theta = d/dy`, so the
eigenvalues `0,-2,-4,…` are the poles of `Gamma_R` and `zeta_inf(s) = det_inf((s-Theta)/2pi | R_inf)^{-1}`
(`[D05:204-215, 286-289]`). I verified that regularised determinant, `sqrt2 pi^{s/2}/Gamma(s/2)`, and the
complex one, `(2pi)^s/Gamma(s)`, to `1e-20` at `s = 0.7, 3.2, 1.5+2i`. *Correction:* cite
`[D05:204-215, 286-296]` and drop Atiyah–Bott; move "the jets of the normal line at the archimedean fixed
point" to the dictionary column.

**Defect 3 (naming).** "Tate twist by −1": in Deninger's convention `H(alpha)` carries `Theta - alpha`
(`[D05:332]`) and `H^2 = R(-1)` (`[D05:334]`); `lambda -> lambda - 1` is the twist **(1)**, which sends `R(-1)`
to `R`.

**Defect 4 (framing).** The Answer's item (iii) and Part IV (3) say R1 "fixes"/"settles" the ladder parity.
R1 shows the parity is bookkeeping (which side of the trace formula the fixed point sits on);
`prop:ladder-parity-free` had already settled it for the notebook's target ("Exact equality to `2P_+` forces
the net spectrum"). R1(a)'s transport `lambda -> (lambda-1)/2` with `rho -> 1-rho` is printed verbatim
under `cor:forced-net-spectrum` (`04b:114-116`); R1's new content is (d). Also, R1(c)'s "net multiplicities"
cancellation (the `k = 0` rung against the image of `H^0`) is exactly what Deninger's distinct-eigenvalue
hypothesis (`[D05:317-319]`) excludes; the note should say that `N` is a net datum in the sense of
`thm:supertrace-rigidity` and not a Deninger-type graded datum.

### R2. Suspension = ring; joint eigenvectors; the Bost–Connes vectors

**VERDICT R2: MINOR.** (a) is correct as a statement about diffeomorphisms of a compact manifold, but its
final application is outside its own hypotheses; (b) and (c) contain one imprecision each; the Reading's
"shape of the prime letters" is a tautology.

*What holds.* Poisson: `sum_k Phi(lambda_k)` with `lambda_k = (log mu + 2pi i k)/log q`, `q = 5`, equals
`log q sum_m mu^m phi(m log q)` for `mu = 1+2i, 3, sqrt5 e^{0.7i}` at two test functions each, residuals
`<= 4.2e-14`. (b)'s uniqueness of `u^rho v` is the density argument, correctly labelled "formal". (c)'s
algebra `mu_p^* v_rho = p^{-rho} v_rho` holds exactly on truncations, and `||v_rho||^2 = zeta(2 Re rho)` (the
truncation tail matches `N^{1-2sigma}/(2sigma-1)` to 1%).

**Defect 1 (R2(a), last sentence; inherited by R6(d)).** "For `M = E(C)` with `f = pi` a lifted Frobenius,
the `Theta`-spectrum on `H^1` is the zero set of `zeta_E`." Multiplication by `pi` on `C/Gamma` is a covering
of degree `[Gamma : pi Gamma] = |pi|^2 = p` (determinant 5 for `pi = 1+2i` on `Z[i]`), not a diffeomorphism;
a diffeomorphism of a compact oriented surface cannot act by `p != +-1` on `H^2`. R5(a) itself shows no
compact-manifold suspension carries the `alpha = 1` structure. Deninger replaces `M` by the solenoid
`M-bar = lim_<-(M, f)` on which `f` becomes the shift automorphism (`[D05:1131-1160]`; "a more accurate
analogy", `[D07:373]`) and proves the trace formula there (Theorem, `[D05:1186-1201]`, example `:1205-1225`).
*Correction:* "(a) … For the lifted Frobenius, which is a degree-`p` covering and not a diffeomorphism, replace
`M` by `M-bar = C x_Gamma T_pi Gamma` with the shift; Deninger's Theorem `[D05:1186-1201]` then gives the
trace formula with `l = log p`, and by `thm:supertrace-rigidity` the net `Theta`-spectrum on the odd part is
`{s : p^s in {pi, conj pi}} + 2pi i Z/log p`."

**Defect 2 (R2(b)).** "A product leaf space `prod_p M_p` … has only product characters." Every character of
the free abelian group `Q^{>0}` is a product of its values at the primes. What a product structure prevents is
a single exponent `rho` with `p^rho` in the local spectrum *for every `p` at once*; for Euler-factor spectra
(`p^rho = 1`) linear independence of the `log p` forces `rho = 0`. Rephrase accordingly.

**Defect 3 (R2(c)).** `v_rho` is a joint eigenvector of every `mu_p^*` for **every** `rho` with
`Re rho > 1/2` (checked at `rho = 0.8+3.3i` and `0.75-i`, neither a zero); nothing in `l^2(N)` selects the
zeros. So the Reading's "puts the zeros exactly where the joint eigenvectors cease to be normalisable" is true
of every point of the critical line and carries no information about zeros. And the orthogonality step
"`(p^{rho+conj rho'} - p)<v,w> = 0`, so `<v,w> = 0` unless `rho + conj rho' = 1`" is wrong for one prime:
it only gives `(gamma - gamma') log p in 2 pi Z`. With `gamma' = gamma + 2pi/log 2`, `2^{rho + conj rho'} = 2`
exactly (checked), and `p = 3` separates them. *Correction:* "for all primes `p`; two primes with
`log p/log q` irrational already force `gamma = gamma'`."

**Defect 4 (Reading).** "`F_p^* = p^Theta = p^{1/2}p^{iH}`, … the primes are coupled … by sharing one joint
eigenbasis" is the flow of `Theta` sampled at `t_D = log p`; any one-parameter group has that property, so
this is not a prediction about the Stinespring question (see S3). In the 2018 construction the primes are
**not** coupled by a joint eigenbasis: Deninger's structure theorem gives a continuous `R^{>0}`-equivariant
bijection from `X_0(C)_{Q,in} x R^{>0} ⊔ ⨆_p X_0(C)_{p,in} x_{p^Z} R^{>0}` onto `X_0` (`[D18:2292-2301]`),
"not homeomorphisms in general" (`[D18:2318]`): set-theoretically one suspension per prime plus a free part,
coupled only through the adèle topology (`[D18:2380, 2411, 3021-3068]`). The note's "one ring with every
prime period at once" misses the construction's actual mechanism.

### R3. The local coefficient; the angle per prime

**VERDICT R3: MINOR.** (a) and (c) are correct; (b) is false as printed for even `k`; the Reading's
Honda–Tate sentence is false; the "superdeterminant" reading conflates two different objects.

*What holds.* `str Lambda^* B = det(1 - B)` for `2x2` `B` (3 random checks); Deninger's uniform coefficient
(34) equals the note's superdeterminant form for `k = ±1..±6`, for a rotation and a reflection
(`l = log 7`, `theta = 1.1`). For a rotation `c_k = 1` (`k >= 1`) and `c_k = e^{kl}` (`k <= -1`). Deuring:
the trace sets over `F_2, F_3, F_5, F_7, F_11, F_13` are exactly `{|a| <= 2 sqrt p}` (exhaustive enumeration).

**Defect 1 (R3(b)).** "If `det O = -1` then `c_k = -1` for `k >= 1`." For a reflection `O^2 = 1`, so
`det(1 - uO^k) = (1-u)^2 > 0` for even `k`: **`c_k = (-1)^k`** (`c_2 = +1.000000` computed). And for
`k <= -1` a reflection gives `c_k = e^{kl}` exactly as a rotation does (checked `k = -1..-6`), so only the odd
positive `k` detect orientation. The proof restricts to odd `k`; the statement does not. The "iff" survives
through `k = 1`, which is Deninger's Fact (`[D05:1095-1101]`). *Corrected (b):* "…iff `O in SO(2)`; if
`det O = -1` then `c_k = (-1)^k` for `k >= 1` and `c_k = e^{kl}` for `k <= -1`."

**Defect 2 (Reading, false).** "By Honda–Tate an algebraic angle is an elliptic curve over `F_p`." False twice.
(i) `e^{i theta}` algebraic does not make `sqrt p e^{i theta}` an algebraic integer: `cos theta = 1/3`, `p = 2`
gives minimal polynomial `9x^4 + 28x^2 + 36`. (ii) A `p`-Weil number of degree 4 gives a simple abelian
**surface**: `x^4 + x^2 + 4` is irreducible over `Q`, all four roots have modulus `sqrt 2`, the middle
coefficient is odd (ordinary), and the pair on `T_xF` has trace `2 sqrt2 cos theta = ±sqrt3`, not an integer.
Only `2 sqrt p cos theta in Z` gives an elliptic curve, as R3(c) itself says. Deninger's own sentence
(`[D05:1104]`, "Are the eigenvalues Weil numbers (of weight 1)? If yes there would be some elliptic curve …")
has the same gap; the note inherits and strengthens it.

**Defect 3 (Reading).** "Deninger's formula is the same superdeterminant orbit by orbit, with the odd letters
the leaf 1-forms … exactly as `thm:hodge-doubling-tensor` reads the torus." The graded trace of `Lambda^*A^k`
is `det(1 - A^k) = |1 - (sqrt p e^{i theta})^k|^2`, whose ring zeta is the Hasse–Weil zeta of the curve with
`a_p = 2 sqrt p cos theta`. Deninger's coefficient is that number **divided by its own absolute value**; the
orbit's Ruelle factor is the Euler factor `(1-p^{-s})^{-1}`. The note's two readings differ precisely by the
`theta`-dependence it says `zeta` does not see; `c_k` is a sign, not a superdeterminant.

**Address.** `[D05:1040-1046]` → `[D05:1028-1037]`.

### R4. The metric as a flow-invariant polarisation, "unique when it exists"

**VERDICT R4: MINOR — with one false clause in (iv), a type error in (i), and a false dictionary entry in (ii)
that the Answer paragraph promotes to a headline.** The linear algebra of the generic case is right.

*What holds.* (i): for `Theta = alpha/2 + X`, `X in sp(B)`, `g_t` is symplectic and the spectrum is symmetric
under `lambda -> alpha - lambda`; and a generic derivation has eigenvalues **off** the line
(`max|Re - 1/2| = 1.6 .. 3.2` in three random `g = 3` examples): the functional equation without RH, as the note
says. (ii): a star commuting with `Theta` gives `(Theta h,h)+(h,Theta h) = alpha(h,h)` and spectrum on
`Re = alpha/2`; the converse holds. (iii) is right; the pairing `tr` is unique up to a scalar because
`H^2 ~ R` with a dense leaf (`[D05:611]`). (iv), generic case: for angles `(0.4, 1.1, 2.3)` the fixed set in
Siegel space has dimension **0**.

**Defect 1 ((iv), false clause).** "If some `theta_j in {0, pi}` or some `theta_j` repeats, the set of
invariant polarisations is a positive-dimensional totally geodesic subspace." Tangent-space dimension of the
fixed set at an invariant `J_0`:

| `g_1` | dim of invariant polarisations |
|---|---|
| `R_{0.4} ⊕ R_{1.1} ⊕ R_{2.3}` (distinct) | 0 |
| `R_0`; `R_0 ⊕ R_{1.1}`; `R_pi ⊕ R_{0.9}` | 2, 2, 2 |
| **`R_theta ⊕ R_theta`** (repeated, one Krein sign) | **0** |
| **`R_theta ⊕ R_theta ⊕ R_theta`** | **0** |
| `R_theta ⊕ R_{-theta}` (repeated, opposite signs) | 2 |
| `R_theta ⊕ R_theta ⊕ R_{-theta}` | 4 |

The centraliser of `R_theta ⊕ R_theta` in `Sp(4,R)` is `U(2)`, compact, and its fixed set in Siegel space is a
point; the proof's "`Sp(4)` etc. for repeats" is wrong. *Corrected (iv):* "…If an eigenvalue `e^{i theta}`,
`theta in (0,pi)`, is repeated, let `(p,q)` be the signature of `iB(v, conj v)` on its eigenspace; the
invariant polarisations there form `U(p,q)/(U(p) x U(q))`, positive-dimensional iff `pq > 0`, and a point when
the Krein signature is definite. At `theta in {0, pi}` they form the Siegel space of the eigenspace."

**Defect 2 (headline).** Hence "unique when it exists" (title of R4, the Answer, Part IV (1)) needs "and the
spectrum of `g_1` is simple (more generally, Krein-definite)". For `zeta` with the whole flow this is simplicity
of the zeros up to Krein type — an unproved hypothesis the note does not state.

**Defect 3 ((i), type error).** "With `J` the `B`-transpose, `J e^{tTheta} J^{-1} = e^{alpha t}e^{-tTheta}`."
The `B`-transpose is an anti-automorphism `g -> g^#`, `B(gh,h') = B(h, g^# h')`; it is not conjugation by an
operator. `B` gives `Theta^# = alpha - Theta` — Leichtnam's "the transpose of `e^{tTheta}` is
`e^t e^{-tTheta}`" (`1307.3851:427-440`). The operator form (FE) of `def:graded-rh-fe-ramanujan` asks for an
even **similarity** `J`; one exists in finite dimension because `Theta^#` is similar to `Theta^T` and hence to
`Theta`, but it is neither `B` nor canonical, and in infinite dimension it needs an argument.

**Defect 4 (Reading: the freedom moves into `B`).** For `g_1` with distinct angles the `g_1`-invariant
alternating forms and the `g_1`-invariant metrics have the **same dimension `g`** (3 and 3 checked), and
`B = ⊕ b_j omega_j` has compatible metric `⊕ |b_j| I`. "Poincaré duality removes the cone's freedom" is
therefore true only when `B` is canonically given, as Deninger's cup product into `H^2 ~ R` would be. On any
notebook object where `B` has to be chosen, choosing `B` *is* choosing a point of the cone (see S1).

**Defect 5 ((ii) and the Answer: the Kraus dictionary entry is wrong where it matters).** "A star commuting
with the flow is case (d), both pairings, and the Hastings-type bound alone remains"; the Answer: "His RH
argument is exactly the notebook's Kraus dichotomy case (d)". `obs:kraus-dichotomy`(d) concerns a Kraus
family with both pairings, which is unitary, and there "all retained modes on the circle" **reduces to
Hastings' bound**, a genuine inequality that unitary families can violate (two violating Haar-unitary families in `num:weil-positivity`, `08c`). Deninger's star commuting with the
flow gives RH outright (`[D05:357-365]`, `[D05:709-720]`); nothing remains. The notebook analogue of
Deninger's mechanism is (HP) of `def:graded-rh-fe-ramanujan` together with
`prop:hp-inner-product-continuous`, not the Kraus dichotomy.

**Defect 6 ((v)).** "`K_HW`, which is `H^1 (x) C^2` under `asm:h-diag` (`prop:d2-spectrum-frobenius`)":
that proposition says "a spectral similarity, not a canonical identification with cohomology (ledger 14)".
There is no cup form on `K_HW` to "write"; see S1.

### R5. Compact manifolds force `alpha = 0`; the solenoid

**VERDICT R5: MINOR.** (a) is a correct proof of what Deninger asserts without proof (`[D05:825]`,
`[D07:480]`). (b)'s computation is right and its words are not; the Reading's identifications are false.

*(b), what is and is not scaled.* At `p = 5`, `pi = 1+2i`, `|pi|_5 = 1/5` under `i -> 2` (checked by Hensel
lifting): the gluing `(z,y,t) ~ (pi^{-1}z, pi^{-1}y, t + log p)` preserves flat area × Haar; it multiplies
`g`-area × Haar by `p` (so R5(a)'s `Omega` does not exist on the solenoid); `g`-area ×
`e^{-t}Haar dt` is invariant under both the gluing and the flow. So "the holonomy … scales leaf area by
`p^{-1}`" is the **flat** area (in `g` the gluing is an isometry, as the proof itself shows), and the flow does
**not** contract the transversal: `phi^s` fixes `y`. What contracts is the Poincaré return map
`(z,y) -> (pi z, pi y)` (`[D05:1225]`: "`p^nu` acts … by diagonal multiplication with `pi^nu`"), or
equivalently the transverse measure `e^{-t}Haar dt`, which the flow scales by `e^{-s}` while it scales
`g`-area by `e^{s}`. *Corrected last clause:* "…the flat area × Haar measure is gluing-invariant; the flow
scales `g`-area by `e^{s}` and the transverse measure `e^{-t}Haar dt` by `e^{-s}`: expanding leaves, a
contracting transverse measure, and a return map `(z,y) -> (pi z, pi y)` that expands `z` and contracts `y`."

*Reading.* "The units-invariant GL_1 bond `R_+^x x Z^hat^x` … and `A/Q = R x_Z Z^hat` are solenoids of exactly
this type." `A/Q` is a solenoid (`[D05:963-967]`) but its `R`-action is additive translation, with dense
orbits and **no** closed orbits; `R_+^x x Z^hat^x` in the idèle topology is a product with profinite factor,
no dense leaves, no closed orbits; in the adèle topology Deninger proves the quotient
`Q^{>0}Z^hat^x x_{Q^{>0}} R^{>0}` **irreducible** — every continuous function is constant (`[D18:3021-3023]`,
`:3068`). None is "exactly this type" (suspension of an expanding covering with conformal leaves and periodic
orbits). "The notebook calls it the Lindbladian" exhibits no operator: dictionary.

### R6. The elliptic example is the Hodge ket bond

**VERDICT R6: MINOR.** (a)–(c) are right; (d)'s proof inherits R2's defect.

*What holds.* `A (x) conj A = diag(1, conj pi, pi, p)` with `A = diag(1, pi)`, in the basis
`(1, dz-bar, dz, dz ∧ dz-bar)` of `thm:hodge-doubling-tensor` (checked). (c) is `thm:elliptic-ph-unitary`.
*Defects.* (d) "is R2(a) with `f = pi`": replace by Deninger's Theorem and example (`[D05:1186-1201,
1205-1225]`), as in R2 Defect 1. Deninger's example assumes CM by the **maximal** order `o_K`
(`[D05:1206]`); `asm:deuring-lift` allows any order, so R6 covers Deninger's case as a special case. Addresses:
`[D05:1213-1224]` → `:1225`; `[D05:676]` → `:674`. The Reading's "is the same sentence" (Deninger's Kähler
identities = `thm:rosati-ph-genus-two`) is dictionary; Leichtnam's attribution of the star argument to Serre
(`1307.3851:420-421`) is the citable support for it.

### R7. `K_S` is not Deninger's `H^1` up to equivalent norm

**VERDICT R7: VALID.** The proposition and both proofs are correct; I reproduced the numerics independently.
Four one-line fixes, none affecting the conclusion.

*What holds, recomputed.* `rho(w_n,w_{n+1})^2 = (d_n/2)^2/((d_n/2)^2 + 1/4)` and `rho <= d` on all 2999
neighbours; minimum `rho = 0.09700` between zeros 1496 and 1497 (`gamma = 1977.1739`, gap `0.0975`). The Gram
matrix by quadrature on the real line (`(2pi)^{-1}dx`) is `<k_n,k_m> = i/(conj w_n - w_m)` with
`||k_n||^2 = 2` under RH. The normalised Gram minimum eigenvalue is `0.3996, 0.2331, 0.1340, 0.0753, 0.0395,
0.0159` at `N = 10, 25, 50, 100, 200, 400` — the author's list to three digits — and `0.0059`, `0.0013` at
`N = 800, 1600`.

*Fixes.* (1) "Decreases monotonically" is automatic: `G_N` is a leading principal block of `G_{N+1}`, so by
interlacing `sigma_min` cannot increase. The evidence is the two-point identity
`1 - |<k^_a, k^_b>|^2 = rho(a,b)^2` (checked on five pairs including the closest), which gives
`sigma_min(G_N) <= 1 - sqrt(1 - rho_min(N)^2)` (checked `N = 10..1600`): the Riesz failure is already a
`2x2` statement, and it *is* the proof. (2) The Reading's `G_nm = i/(w_n - conj w_m)` is 04h's
upper-half-plane formula (`04h:26`, `w = gamma/2 + i(1-sigma)/2`); with the note's lower-half-plane `w_n` it has
diagonal `1/(2 Im w_n) = -2`; write `i/(conj w_n - w_m)`. (3) The label is `prop:mode-diagonal-rebound-rh`.
(4) A sharper unconditional route: `sum |Im w_n| delta_{w_n}` is not a Carleson measure, since unit boxes carry
mass growing like `(1/4pi) log T` from on-line zeros alone (0.25 at `Re w = -10` to 0.50 at `-1700`, against the
prediction 0.09 → 0.50); truncated Carleson products fall `0.416, 0.074, 0.050` at `N = 100, 1000, 3000`.

*Scope.* R7(a) quotes Corollary 9 for pure point spectrum, but Corollary 9's hypotheses force `alpha = 0`
(`[D05:825]`), and for general `alpha` Deninger explicitly allows continuous spectrum (Remark b,
`[D05:865-869]`); "under pure point spectrum" is an assumption, as R7(a) in fact states it. In the Answer,
"not Deninger's `H^1` with a different inner product on the same space" must read "with an **equivalent** inner
product": an inequivalent one on the span of the `k_n` exists trivially, as R7's own Reading says.

### R8. "The bond is an algebra and the flow is multiplicative; the channel is not"

**VERDICT R8: INVALID.** (b) is false as stated, and (c) — the substantive claim — is false because it uses
the wrong product; the note's own R6 is a counterexample.

**Defect 1 ((b)).** "`E` is multiplicative, `E(XY) = E(X)E(Y)`, iff … `E = c Ad(A)`; for a trace-preserving
channel this forces `A` unitary up to scalar." A nonzero multiplicative map on `End(V)` is injective
(simplicity), hence bijective, hence unital, so `c Ad(U)` with `c != 1` is **not** multiplicative:
`E(XY) = c^{-1}E(X)E(Y)` (checked `c = 2, 5`). With complete positivity the Choi matrix of `X -> AXA^{-1}` is
positive iff `A` is a scalar times a unitary (checked indefinite for `A = diag(1, 1+2i, 0.3)`), so
multiplicative + CP ⇔ `E = Ad(U)`; trace preservation plays no role. And a single Kraus operator `A`,
invertible and not unitary, gives `X -> AXA^dag`, which is not multiplicative (checked). *Corrected (b):* "A
CP map on `End(V)` is multiplicative iff `E = Ad(U)`, `U` unitary; it is multiplicative up to a scalar,
`E(XY) = c^{-1}E(X)E(Y)`, iff `E = c Ad(U)`."

**Defect 2 ((c), false).** Deninger's derivation mechanism uses the **cup product**. R6(a), following
`thm:hodge-doubling-tensor`, identifies the doubled Hodge-ket bond with
`Lambda^*(C dz ⊕ C dz-bar) = H^*(T^2, C)`, whose product is the wedge. For that product the doubled transfer
`diag(1, conj pi, pi, p) = A (x) conj A` is a ring automorphism (checked on 20 random pairs), although
`A = diag(1, pi)` has singular values `1` and `sqrt 5` and is not a scalar times a unitary; read on `End(V)`
with composition, the same map is not multiplicative (checked). So "the class of notebook objects on which
Deninger's derivation mechanism can act is exactly the scalar-times-automorphism transfers" excludes
Deninger's own realised example, which R6 identifies with a notebook object. "The odd sector of any Ramanujan
channel in its manifest form" is a statement about a sector restriction (`q^{-1/2}E_1` unitary, true for the
Hodge ket transfer), not about `E = c Ad(U)` (false for it).

**Consequences.** The Reading ("locates the metric in the multiplicative structure, which the notebook's
channels have only when they are already Ramanujan in the manifest form"), Part IV (2), the table's "product"
column and its closing paragraph all rest on composition in `End(V)`. *Replacement for (b)–(c) and the
Reading:* "At genus one the doubled bond carries the exterior product of `H^*(T^2)` (R6(a)); for it `A (x)
conj A` is multiplicative for every even letter `A = 1 ⊕ a`, and Deninger's derivation argument applies
verbatim with `B` the `(-,-)` coefficient of the wedge of two odd vectors; this is
`thm:elliptic-ph-unitary`. At genus two the doubled bond `C^{1|2} (x) C^{1|2}` has a four-dimensional
`(-,-)` block and is not a cohomology ring (`06f:215-221`: the curve's `H^*` sits in `Lambda^*H^1(J)` behind a
rank-six non-product projector). Whether any other notebook bond (`K_S`, `K_HW`) carries a graded-commutative
product for which its transfer is multiplicative is open."

---

## Part III and the Answer paragraph

**S1 (the proposed computation is decided up to the choice it leaves open).** In the eigen-model of `K_HW`
of D2 (resonances of `2z^4 - 2z^2 + 1`, `|z| = 2^{-1/4}`, `arg z = ±pi/8, ±7pi/8`): the unitarising cone has
real dimension 4 (reproducing `thm:arithmetic-metric`); the `Z`-invariant alternating forms
`Z^T B Z = r^2 B` have complex dimension **2**, real dimension 2 after reality, so **the third outcome ("no `B`
on the doubling is invariant") cannot occur**; by R4(ii)'s converse the `B`-compatible polarisation is always
`Z`-invariant, i.e. **always inside the cone**; and it lies on the symmetric ray **iff `B` is parity-invariant
or anti-invariant** (checked: `B_1 ± B_2` on the ray, `B_1 + 0.37 B_2` off it). "`B_{H^1} (x)` (alternating form
on `C^2`)" is symmetric, not alternating, so only the symmetric factor is a candidate. With
`prop:d2-spectrum-frobenius` giving only a spectral similarity, the cup form on `K_HW` is not defined by the
notebook; choosing `B` is choosing a point of the two-dimensional real cone. S1 should be restated as: "is
there a canonical `B` on `K_HW`, and is it parity-(anti)invariant?"

**S2.** (a) "Same reduction" is dictionary, and the roles are reversed: in Deninger's Theorem 4 positivity of
`( , )` is free (leafwise Hodge theory, `[D05:622-626]`) and the missing input is flow–star compatibility (11n)
(`[D05:474-479, 674]`); in `thm:rosati-ph-genus-two` the compatibility `pi pi^dag = q` is free and positivity
of the trace form is the input. Cite Leichtnam `:420-421` (Serre's Kähler analogue) and call it analogy.
(c) "`H^0 = R`, the notebook's simple even fixed line" contradicts R1's Reading ("the notebook's even fixed
line is Deninger's `H^2`, not `H^0`"); D18's `H^0 = R` (`[D18:512, 3002-3005]`) is Deninger's `H^0`.

**S3 (factor 2, and nothing to test).** "`J_p k_rho = p^{-conj rho/2} k_rho` (notebook normalisation)": that
eigenvalue has modulus `p^{-1/4}` and is `Z(log p)`; the ring length of `p` in notebook time is `2 log p`
(`prop:ringnorm-trace`), where `Z(2 log p)` has eigenvalues `p^{conj rho - 1}` of modulus `p^{-1/2}` (checked
`p = 2,3,5`). Since `J_p := Z(2 log p)` commute and share the modes by construction, "measure its departure from
normality in the Gram metric as `N` grows" re-tests R7 (non-similarity of `Z(t)` to a normal operator) and
nothing else. `obs:prime-by-prime-blind` already lists "commuting dilations" among the blind ansätze; S3 should
say that `p^Theta` escapes it only because it is one flow sampled at `log p`, and therefore carries no
information beyond `Theta`.

**S4.** Drops R3(c)'s integrality condition ("has the cohomology of an elliptic curve … with
`a_p = 2 sqrt p cos theta_p`", true only when that is an integer), and "no candidate for `theta_p` … is a
precise way of saying there is no candidate for the metric" is a non sequitur: `theta_p` is local data at a
closed orbit, invisible to the trace formula; the metric is a polarisation on `H^1`; no proposition relates
them.

**S5.** (i) Candel: for `|d_K| = 1` Deninger concludes "there is an `F`-leaf which is either a plane, a torus
or a cylinder" (`[D05:1124]`) — existence of one parabolic leaf, not that the leaves are parabolic; "the
modular surface's hyperbolic leaves belong to a ramified field or to `GL_2`" does not follow. (ii)
`Z^hat^x_{(p)} = prod_{l != p} Z_l^x` (`[D18:1733]`), so the packet base `Z^hat^x_{(p)}/p^{Z^hat}` is
`Z^hat^x` modulo the **decomposition group** at `p` (inertia `Z_p^x` and the closure of Frobenius) — the set of
primes of `Q^ab` above `p` — not "modulo the Frobenius at `p`". (iii) The solenoid identifications: see R5.

**S6.** The McKean–Singer sentence is the note's gloss, not `[D05:785-789]` (see citations). "Two generators,
not one" and "the 'Lindbladian' content … is the scalar `e^{-t/2}`" are dictionary.

**The table.** The Deninger row's "`Theta = p^{-Theta}`-jumps per prime (R2)" is garbled: `F_p^* = p^Theta`.
The "product" column follows R8 and must be redone. The closing paragraph's "the two do not meet on the same
space" should note that D18 maps Deninger's system `Q^{>0}`-equivariantly into Connes's adèle space
(`[D18:2363-2411]`, next section).

**The Answer and Part IV.** Five sentences overreach: "exactly the notebook's Kraus dichotomy case (d)" (R4
Defect 5); "which is Rosati positivity in the notebook's words" and "which is Weil's proof" (dictionary, S2);
"unique" without the simplicity/Krein hypothesis (R4 Defects 1–2); "(2) the bond must be an algebra … which
the notebook's channels are only in the manifest Ramanujan form" (R8); "(3) … settled" (R1 Defect 4).
"No candidate metric … beyond the one the notebook already has: the diagonal form in the mode basis": by R7
that form is not a metric on `K_S` at all; say "beyond the inequivalent diagonal form on mode coefficients,
which is RH". The registration list in Part IV (v) must drop R8 and carry the R2, R3, R4 fixes.

---

## The central question: does anything in Deninger change the verdict?

TJO asked whether Deninger in supertrace-cMPS language gives a candidate metric or the same shortcoming. The
note answers "reformulation with the same gap, plus a sharper statement of the gap". I read the sources for
anything that would move that verdict in either direction.

**The verdict survives, and what the note missed pushes the same way.**

1. **The Laplacian route (`[D05:852-869]`), missed as a mechanism.** Deninger's proof of Corollary 9 gives, for
   general `alpha`, `-(Theta - alpha/2)^2 = Delta^1|_{ker Delta^1_F}` (`:857-858`), and Remark a asks whether the
   `gamma^2` of the zeros lie in the spectrum of a Laplace–Beltrami operator on 1-forms (`:864`). This is a second
   positivity mechanism: RH plus semisimplicity follows if `-(Theta - 1/2)^2` is a nonnegative self-adjoint
   operator. It gives no candidate metric (it needs a Laplacian whose restriction is `-(Theta-1/2)^2`, which needs
   the flow isometric up to scale — the same equivariance gap). But it refutes "unique" as a feature of the
   programme: the metrics making `-(Theta-1/2)^2` self-adjoint are all metrics in which the eigenplanes are
   orthogonal, a cone of dimension `3g` against `g` for the invariant polarisations (9 against 3 checked at
   `g = 3`). Uniqueness belongs to the polarisation mechanism, not to Deninger. The note mentions `-Theta^2 =
   Delta^1` only as "a wave equation" (S6). It is also where Deninger meets the notebook's Selberg shards:
   `s(1-s) - 1/4 = gamma^2` as a Laplace eigenvalue.
2. **D18 lands on Connes's space (`[D18:2329-2411]`), missed.** Deninger maps `X~ = X(C) x R^{>0}`
   `Q^{>0}`-equivariantly into `A^{>0} ⊔ ⨆_p A^{>0}_{(p)} ⊂ A`, with `A^{>0}_{(p)}` the adèles whose
   `p`-component vanishes (Connes's periodic orbits), and writes: "One may wonder if it is possible to study the
   `Q^{>0}`-action on `X~` from their non-commutative point of view" (`:2363`). The 2018 route therefore sits
   over the table's Connes row, whose missing datum is Weil positivity: the same shortcoming again, now
   byte-cited. The comparative table treats the two as independent attacks; in D18 one is fibred over the
   other.
3. **D18's cohomological geometry is hostile to a metric (`[D18:3002-3068]`, `2292-2322`).** `H^0_F = R` is
   proved through the **irreducibility** of `Q^{>0}Z^hat^x x_{Q^{>0}} R^{>0}` in the adèle topology — all
   continuous functions are constant, "reminiscent of … a dense leaf" (`:3068`) — and the system is
   set-theoretically one suspension per prime plus a free part, coupled only by that topology. There is no
   invariant measure or Hilbert structure in sight on this leaf space. This strengthens S2(c) ("nothing about
   the odd sector's metric") beyond "`H^1` not computed".
4. **D07 §4 (Lichtenbaum, analytic torsion, `[D07:569-679]`), missed.** There Deninger uses a Hodge metric as
   auxiliary data and the output, `zeta_R^*(0)`, is metric-independent (Cheeger–Müller). It is the opposite
   situation to RH, where the metric must be special; no candidate.
5. **Leichtnam (`1307.3851:392-422`).** The star is anti-linear and pairs the `chi`- and `chi-bar`-sectors,
   `*: H^1_chi -> H^1_{chi-bar}`, `*^2 = Id`, and the argument is attributed to Serre's Kähler analogue. This
   supports the note's dictionary (and bears on `conj:galois-graded-bond`: the metric on a character sector
   would be defined through the conjugate sector) but supplies no metric.
6. Nothing in D05 §3 beyond what the note has: Poincaré duality into `R(-1)` on generalised eigenspaces
   `Theta ~ alpha` × `Theta ~ 1-alpha` (`[D05:336-348]`) is R4(i); the star argument (`:349-365`) and (11n)
   (`:470-479`) are R4(ii).

**What the verdict loses.** Of the five sharpenings in Part IV: (1) "unique, fixed by Poincaré duality" is
conditional (simple or Krein-definite spectrum) and only relabels the cone's freedom unless `B` is canonical
(R4 Defects 1, 2, 4; S1); (2) "the bond must be an algebra … only in the manifest Ramanujan form" is false
(R8); (3) "settled" is bookkeeping already in `cor:forced-net-spectrum` (R1 Defect 4); (4) "commuting dilations
sharing one eigenbasis" is a tautology of any flow, and the 2018 construction couples primes differently (R2
Defect 4, S3); (5) "`K_S` is not Deninger's `H^1` under any equivalent norm" stands (R7). **So the honest
summary is: same gap; one sharpening survives (R7); a second survives in corrected form ("the metric is a
flow-invariant polarisation, a point when the spectrum is simple and `B` is canonical; the notebook has no
canonical `B` on any of its bonds except the genus-one Hodge ket, where it is the cup product").**

---

## What is theorem and what is dictionary

| statement | status |
|---|---|
| R1(a)–(d): transport, equivalence with `prop:ringnorm-trace`, `div zeta-hat = div zeta + div Gamma_R` | **theorem** (elementary; re-verified to `1e-15` with 3000 zeros); (a) already in `cor:forced-net-spectrum` |
| "the `Gamma_R` ladder is the jet trace at the archimedean fixed point" | **dictionary** resting on Deninger's conjecture `[D05:756, 1038-1041]`; the ladder *as a cohomology* is Deninger's Proposition 2.1 `[D05:204-215]` (theorem, byte-cited) |
| "two incoming orbits = two poles' worth of jets per integer" | **false**; the two `Gamma_R` factors of `Gamma_C` is the correct dictionary |
| R2(a) for a diffeomorphism of a compact manifold | **theorem** |
| R2(a) for the lifted Frobenius on `E(C)` | **outside its hypotheses**; true on the solenoid by Deninger's Theorem `[D05:1186-1201]` |
| R2(b) | **formal**, correctly labelled |
| R2(c) algebra; orthogonality | **theorem** with "all primes"; the reading "zeros where eigenvectors cease to be normalisable" selects nothing |
| R3(a), (c), the iff in (b) | **theorem** |
| R3(b) "`c_k = -1` for `k >= 1`" | **false** at even `k` |
| "by Honda–Tate an algebraic angle is an elliptic curve"; "Deninger's formula is the same superdeterminant" | **false** / **conflation** |
| R4(i)–(iii), R4(iv) generic | **theorem** (linear algebra) |
| R4(iv) degenerate clause | **false** for Krein-definite repeats |
| "Deninger's RH argument is Kraus-dichotomy case (d)" | **false as dictionary** (case (d) leaves Hastings' bound; Deninger leaves nothing); the entry is (HP) |
| R5(a) | **theorem** |
| R5(b) | **theorem** after the wording fix |
| "`A/Q`, `R_+^x x Z^hat^x` are solenoids of exactly this type" | **false** |
| R6(a)–(c) | **theorem**, conditional on `asm:deuring-lift` (Deninger: maximal order) |
| R6(d) | **theorem** via Deninger's Theorem, not via R2(a) |
| R7 | **theorem** (two standard results, correctly stated); numerics reproduced |
| R8(b) as printed; R8(c) | **false**; corrected (b) is Skolem–Noether + Choi; the cup-product statement at genus one is `thm:elliptic-ph-unitary` |
| S1 outcome 3; "`B_{H^1} (x)` alternating" | **impossible**; **not alternating** |
| S3 `J_p` eigenvalue | **off by the factor 2** of the note's own conventions |
| S5 Candel; `Z^hat^x_{(p)}` | **overreach**; **mislabelled** |
| S6 McKean–Singer for all `s` | **not in the source**; the note's gloss |
| "the metric is the missing datum in Deninger too" | Deninger's own words for the conformal metric (`[D05:674]`) and the 2018 spaces (`[D18:559]`); **reinforced** by `[D18:2363-2411, 3021-3068]` |

## Summary table

| proposition | verdict | defect in one line |
|---|---|---|
| **R1** Tate-twist identity | **MINOR** | math exact to `1e-15`; Reading's "two poles' worth of jets per integer" is false (`Gamma_C` has one pole per integer; two `Gamma_R` factors); "Atiyah–Bott" misattributes a Deninger conjecture while Deninger's Prop. 2.1 byte-cites the ladder; twist sign; "fixes the parity" overclaims |
| **R2** suspension, joint eigenvectors, `v_rho` | **MINOR** | (a) applied to `pi` on `E(C)`, a degree-`p` covering, not a diffeomorphism (needs Deninger's solenoid); one-prime orthogonality loophole; `v_rho` exists for every `rho`, so nothing selects zeros; "joint eigenbasis" is not how D18 couples primes |
| **R3** local coefficient, angle per prime | **MINOR** | "`c_k = -1` for `k >= 1`" false at even `k` (`c_k = (-1)^k`); Honda–Tate sentence false (degree-4 Weil numbers give surfaces); "superdeterminant" conflates `zeta_{E_p}` with its sign; wrong address |
| **R4** invariant polarisation, uniqueness | **MINOR** | degenerate clause of (iv) false (Krein-definite repeats give a point); "unique" needs simple spectrum; `B`-transpose is not a similarity; `B` carries the cone's freedom; "Kraus case (d)" is the wrong dictionary entry |
| **R5** `alpha = 0`, solenoid | **MINOR** | (a) correct; (b) conflates flat and `g`-area and says the flow contracts the transversal (it is the return map); `A/Q` and `R_+^x x Z^hat^x` are not "exactly this type" |
| **R6** elliptic example = Hodge ket bond | **MINOR** | (d) proved through the misapplied R2(a); two addresses off; Deninger needs the maximal order |
| **R7** `K_S` modes not a Riesz basis | **VALID** | reproduced; nits: monotonicity is interlacing, Gram sign convention, wrong label, "equivalent" missing in the Answer |
| **R8** multiplicative CP maps | **INVALID** | `c Ad(U)` with `c != 1` is not multiplicative; the relevant product is the cup product, for which the note's own R6 example (`A = diag(1,pi)`, not scalar × unitary) is multiplicative, contradicting (c) |

**1 VALID / 6 MINOR / 1 INVALID.** Central question: **the verdict "same gap" stands and is reinforced**
(`[D05:852-869]`, `[D18:2363-2411, 3021-3068]`); of the note's five claimed sharpenings, one survives intact
(R7) and one in corrected form (R4).

## Corrections (concrete)

1. **R1 Reading, complex places.** Replace the `Gamma_C` sentence by: "A complex place has `kappa = -1` and one
   simple pole of `Gamma_C` at every nonpositive integer; `Gamma_C(s) = Gamma_R(s)Gamma_R(s+1)`, so its ladder is
   two real ladders (even and odd integers), which is what the two incoming orbits of `[D18:2052]` match."
2. **R1(d) and ledger.** Replace "(Atiyah–Bott, not byte-cited)" by "Deninger's Proposition 2.1,
   `[D05:204-215, 286-296]`: `R_inf = R[exp(-2y)]`, `Theta = d/dy`"; file "jets at the archimedean fixed point"
   as dictionary resting on `[D05:756, 1038-1041]`.
3. **R1(a).** "Tate twist by −1" → "the twist (1) in Deninger's notation `H(alpha)`: `Theta - alpha`
   (`[D05:332-334]`)"; add "this transport is printed under `cor:forced-net-spectrum`".
4. **Answer (iii), Part IV (3).** "fixes/settles the ladder parity" → "explains the ladder parity as bookkeeping
   (which side of the trace formula carries the fixed point); `prop:ladder-parity-free` fixes it by exact
   equality".
5. **D2.** "forcing" → "if the eigenvalues on `H^0, H^1, H^2` are distinct (`[D05:317-319]`), forcing"; add to
   R1(c) that `N` is a net datum in the sense of `thm:supertrace-rigidity`, with a cancellation Deninger's
   hypothesis excludes.
6. **R2(a), last sentence, and R6(d).** Replace `M = E(C)`, `f = pi` by the solenoid
   `M-bar = C x_Gamma T_pi Gamma` with the shift, citing `[D05:1131-1160, 1186-1201, 1205-1225]` and
   `[D07:373]`; state the spectrum up to cancelling pairs via `thm:supertrace-rigidity`.
7. **R2(b).** "has only product characters, the poles of the Euler factors" → "admits a common exponent `rho`
   only where every local spectrum contains `p^rho`; for Euler-factor spectra that is `rho = 0`".
8. **R2(c).** "for all `p`" in the orthogonality step, with "two primes with `log p/log q` irrational
   suffice"; add "`v_rho` is a joint eigenvector for every `rho`; nothing in `l^2(N)` selects the zeros" and
   delete "puts the zeros exactly where …".
9. **R2 Reading, S3.** Add D18's structure theorem (`[D18:2292-2322]`): the 2018 primes are coupled by the adèle
   topology, not by a joint eigenbasis.
10. **R3(b).** "`c_k = -1` for `k >= 1`" → "`c_k = (-1)^k` for `k >= 1` and `c_k = e^{kl}` for `k <= -1`".
11. **R3 proof.** `[D05:1040-1046]` → `[D05:1028-1037]`.
12. **R3 Reading and S4.** Delete "by Honda–Tate an algebraic angle is an elliptic curve"; write "when
    `2 sqrt p cos theta_p` is an integer, Deuring gives an elliptic curve over `F_p`; a Weil number of higher
    degree gives a higher-dimensional abelian variety (e.g. `x^4 + x^2 + 4` over `F_2`)". Replace "the same
    superdeterminant orbit by orbit" by "the numerator is the graded trace of `Lambda^*A^k`, whose ring zeta is
    `zeta_{E_p}`; Deninger's coefficient keeps only its sign".
13. **R4(i).** Replace "with `J` the `B`-transpose, `J e^{tTheta}J^{-1} = …`" by "`B` gives
    `Theta^# = alpha - Theta` (transpose, `1307.3851:427-440`); in finite dimension this implies a
    non-canonical similarity `J` with `J Theta J^{-1} = alpha - Theta`, the operator form of (FE)".
14. **R4(iv).** Replace the degenerate clause by the Krein-signature statement (R4 Defect 1) and fix the proof's
    "`Sp(4)` etc. for repeats" (the centraliser is `U(p,q)`).
15. **R4 title, Answer, Part IV (1).** "unique when it exists" → "unique when it exists and the spectrum is
    simple (or Krein-definite), given `B`"; add "invariant `B` and invariant metrics have the same dimension, so
    the gain requires a canonical `B`".
16. **R4(ii) and the Answer.** Delete "exactly the notebook's Kraus dichotomy case (d) … the Hastings-type
    bound alone remains"; write "Deninger's mechanism is (HP) of `def:graded-rh-fe-ramanujan`
    (`prop:hp-inner-product-continuous`) with `G = ( , )`, and (FE) from `B`; unlike Kraus case (d), nothing
    remains to be proved".
17. **R4(v), S1.** Replace "which is `H^1 (x) C^2` under `asm:h-diag`" by "which is similar to `H^1 (x) C^2`
    as a spectrum only (ledger 14)"; restate S1 as "is there a canonical `B` on `K_HW`, and is it
    parity-(anti)invariant?", delete outcome 3, and drop "or alternating" from the candidates.
18. **R5(b).** Use the corrected last clause in R5 above (flat vs `g`-area; the return map contracts `y`, not
    the flow).
19. **R5 Reading, S5.** Delete "solenoids of exactly this type" for `A/Q` and `R_+^x x Z^hat^x`, citing
    `[D18:3021-3023]` for the irreducibility of the latter in the adèle topology.
20. **R6 Reading.** `[D05:676]` → `[D05:674]`; cite `1307.3851:420-421` for the Serre analogy; note the maximal
    order in Deninger's example.
21. **R7.** Write the LHP Gram as `i/(conj w_n - w_m)`; label → `prop:mode-diagonal-rebound-rh`; replace
    "decreases monotonically" by the two-point bound `sigma_min <= 1 - sqrt(1 - rho_min^2)`; in the Answer insert
    "equivalent".
22. **R8.** Replace (b) by the corrected statement (R8 Defect 1) and (c) and the Reading by the cup-product
    replacement (R8 Defect 2); redo Part IV (2) and the table's "product" column; do not register R8 as printed.
23. **S2(c).** "`H^0 = R`, the notebook's simple even fixed line" → "`H^0 = R` (`[D18:3002-3005]`), Deninger's
    `H^0`; the notebook's even line is his `H^2` (R1)".
24. **S3.** `p^{-conj rho/2}` → `p^{conj rho - 1}` (that is, `Z(2 log p)`); delete the "cheap test" or say it
    re-tests R7.
25. **S5.** Candel: "there is a parabolic leaf" (`[D05:1124]`); `Z^hat^x_{(p)}/p^{Z^hat}` = `Z^hat^x` modulo the
    decomposition group at `p` (`[D18:1733]`).
26. **S6.** Mark the heat-kernel identity as the note's gloss; quote `[D05:785-787]` exactly.
27. **Table.** "`Theta = p^{-Theta}`-jumps" → "`F_p^* = p^Theta`"; add to the closing paragraph that D18 maps
    Deninger's system into Connes's adèle space (`[D18:2363-2411]`).
28. **Part IV verdict.** "the diagonal form in the mode basis" → "the (inequivalent) diagonal form on mode
    coefficients"; "his 2018 spaces carry no metric" → "no Riemannian or leafwise metric and no analytic
    structure (`[D18:559]`; D18 does construct a metric-space metric, `:2205`)".
29. **Central question, add.** A paragraph on Deninger's Laplacian route `[D05:852-869]` (a second positivity
    mechanism with a `3g`-dimensional metric cone and the same equivariance gap) and on D18's map to the adèles.
30. **Labels.** `sec:artin-schreier-mps` → `sec:artin-schreier`.

## What a further reviewer should attack next

1. **A canonical `B` on `K_HW`.** S1, restated: does the D2 or D3 diagram, or the Hecke structure, supply an
   alternating form on `K_HW` that is not a choice? If not, the "search is for `B`" slogan has no content on the
   notebook's finite cavities.
2. **Krein signature of the zeta flow.** R4's uniqueness needs a statement about multiple zeros of mixed Krein
   type; whether the notebook's graded bond even defines a Krein form on `K_S` is untested.
3. **A cup product beyond genus one.** R8's corrected content says the only notebook bond with Deninger's
   algebra structure is the genus-one Hodge ket. Is there a graded-commutative product on `K_HW` for which `Z`
   is multiplicative up to scale?
4. **The Laplacian route on the modular surface.** `[D05:864]` asks whether `gamma^2` lies in the spectrum of a
   Laplacian on 1-forms. The notebook's Lax–Phillips shards have a Laplacian and the zeros as resonances, not
   eigenvalues; stating precisely why this fails there would close Deninger's second mechanism in the
   notebook's language.
5. **D18 over Connes.** `[D18:2363]` suggests studying `X~ -> A` from the Bost–Connes side; shard 04d already has
   the Bost–Connes MPOs. Writing the fibre of `X~` over `A^{>0}_{(p)}` in that language is a finite, concrete test.

---

## Re-verdicts (version 2)

I re-read `notes/deninger-cmps/reformulation.md` version 2 in full (722 lines: D1–D7, R1–R8 with proofs
and Readings, S1–S6, the table, Part IV, the theorem/dictionary table and the 30-row correction ledger), and
checked each of the 30 ledger rows against the text it points to. All 30 are applied. The five scratch scripts
still stand at 65 / 90 / 52 / 58 / 13 = **278 checks, 0 failures** (re-run today). For the statements that
version 2 rewords or adds, I wrote **`notes/reviews/scratch_den_v2.py`, 17 checks, 0 failures**:
- R4(i): `Theta^# = Omega^{-1} Theta^T Omega = alpha - Theta`, and `alpha - Theta` has the same spectrum.
- R4(iv): `dim U(p,q)/(U(p) x U(q)) = 2pq` agrees with the tangent-space counts 0, 2, 4, 0.
- R8(c): `A (x) conj A` is multiplicative for the wedge product for three values of `a`, and bijective iff `a != 0`.
- R3(b): the proof's negative-`k` step for a reflection, `k = 1..4`.

In total **295 checks, 0 failures**.

**R1.** Every correction is in. The complex-place sentence now reads "one simple pole of `Gamma_C` at every
nonpositive integer … two real ladders"; the ladder is cited to Deninger's Proposition 2.1; the jet reading is
filed as dictionary on `[D05:756, 1038-1041]`; the twist is named `H(1)`; the transport is credited to
`cor:forced-net-spectrum`; and the net-datum caveat is stated against `[D05:317-319]`. The statement and proof
are what I verified to `1.4e-15`.

VERDICT prop:deninger-twist-identity: VALID

**R2.** (a) now excludes the covering `pi` in the proposition itself, gives the reason (a diffeomorphism acts by
`+-1` on `H^2`), and routes the solenoid case through Deninger's Theorem `[D05:1186-1201]` and
`thm:supertrace-rigidity`. The "`+ 2 pi i Z/log p`" after `{s : p^s in {pi, conj pi}}` is redundant, since that
set already contains the towers, but it is not false. (c) now says `v_rho` exists for every `rho` with
`Re rho > 1/2`, and states the orthogonality with all primes, the one-prime loophole and the two-prime closure,
all correctly. (b) is labelled formal and now carries D18's topological coupling; it is not claimed.

VERDICT prop:deninger-suspension-ring: VALID

**R3.** (b) reads "`c_k = (-1)^k` for `k >= 1`; in both cases `c_k = e^{kl}` for `k <= -1`", and its proof covers
odd and even `k` (re-checked `k = 1..4`). (c) carries the integrality condition and the higher-degree
alternative. The Reading replaces "the same superdeterminant" by the graded-trace-versus-sign statement. Two
nits, not defects:
- The proof contains a stray "`...`" after "`sgn det(1 - A^k)`".
- The Reading's "has ring zeta `zeta_{E_p}`" is literal only when `2 sqrt p cos theta` is an integer; otherwise
  it is the formal ratio `(1-alpha z)(1-conj(alpha) z)/((1-z)(1-pz))`. That wording is mine, from correction 12.

VERDICT prop:deninger-local-coefficient: VALID

**R4.** Everything checks:
- (i) now has the transpose `Theta^# = alpha - Theta`, byte-cited to `[L13:427-440]`, and a non-canonical
  similarity `J` with a correct proof (`Theta^#` is conjugate to `Theta^T` by the matrix of `B`).
- (ii) names (HP) and `prop:hp-inner-product-continuous`, and states the contrast with Kraus case (d) correctly.
- (iv) carries the Krein-signature statement `U(p,q)/(U(p) x U(q))`, which matches my tangent-space table, and the
  conditioned "unique when it exists".
- (v) states that `B` carries the cone's freedom and that `K_HW ~ H^1 (x) C^2` is a spectral similarity only.
- The Reading adds the Laplacian route with the correct `3g` count.

One presentational nit: (iv)'s hypothesis says `theta_j in (0, pi)` and then treats `theta in {0, pi}`. Reading
"`theta_j in [0, pi]`" in the hypothesis would make it consistent. This does not affect any conclusion.

VERDICT thm:deninger-invariant-polarisation: VALID

**R5.** (b) is now exactly the corrected statement:
- The gluing is a `g`-isometry and preserves flat area × Haar.
- The flow scales `g`-area by `e^s` and `e^{-t} Haar dt` by `e^{-s}`.
- The return map expands `z` and contracts `y`, and the `Omega` of (a) does not exist.

The Reading withdraws "solenoids of exactly this type" and cites `[D18:3021-3023]`. The address for `omega_phi`
is `[D07:376-387]`.

VERDICT prop:deninger-alpha-zero-solenoid: VALID

**R6.** (d) now rests on Deninger's Theorem and `[D05:1225]`, not on R2(a). The maximal order is stated. The
Reading's Rosati comparison is now "free and missing inputs exchanged … dictionary", with `[L13:423]`. I checked
that address: line 423 is "This argument comes from an idea of Serre", so it is more exact than my own `:420-421`.

VERDICT prop:deninger-elliptic-hodge-ket: VALID

**R7.** The fixes are in:
- (a) states pure point spectrum as an assumption.
- (b) adds the two-point bound; its proof uses interlacing in place of "monotone".
- The Reading uses the lower-half-plane Gram matrix `i/(conj w_n - w_m)`, the correct labels, "equivalent", and
  Selberg 1942.

(a)'s orthogonality is written in the convention linear in the second slot and is correct there:
`(conj rho - 1 + rho')(h,h') = 0`. The Reading's Gram matrix is written in the convention linear in the first
slot. Both are right in their own convention; a reader should not mix them.

VERDICT thm:ks-not-deninger-h1: VALID

**R8.** (b) is now correct: multiplicative + CP ⇔ `Ad(U)`, and up to a scalar ⇔ `c Ad(U)`, with a correct
Skolem–Noether + Choi proof. (c) has the right product and the right conclusion. Two words in (c) are still false
as printed:
- "for **every** even letter `A = 1 (+) a`": for `a = 0` the map `A (x) conj A = diag(1,0,0,0)` is a ring
  **endomorphism**, not an automorphism (checked).
- "the doubled bond `C^{1|2} (x) C^{1|2}` … **is not a cohomology ring**": 06f shows only that it is not the
  curve's cohomology ring (the curve's `H^*` sits behind a rank-six non-product projector). Whether it carries some
  graded-commutative product is part of the question the same paragraph calls open. The bar is also missing on the
  second factor.

(superseded below) VERDICT-v2a prop:deninger-product-genus-one: MINOR — (c) overstates in two places. Exact fix, two replacements in
R8(c):
- "is a ring automorphism for every even letter `A = 1 (+) a`" → "is a ring endomorphism for every even letter
  `A = 1 (+) a`, and an automorphism when `a != 0`".
- "the doubled bond `C^{1|2} (x) C^{1|2}` has a four-dimensional `(-,-)` block and is not a cohomology ring" →
  "the doubled bond `C^{1|2} (x) conj(C^{1|2})` has a four-dimensional `(-,-)` block and is not the cohomology
  ring of the curve".

(The proof of (c) needs no change: "exterior powers of a linear map are multiplicative" is true for `a = 0`, and
the genus-two sentence is already attributed to 06f.)

**Parts I, III, IV and the tables.** No new defects:
- The Answer now says (HP), not Kraus (d).
- The "unique" claims are conditioned.
- S1 is restated as the canonical-`B` question.
- S2(c) uses `H^0`/`H^2` consistently.
- S3 uses `Z(2 log p)`, eigenvalues `p^{conj rho - 1}`.
- S5 has Candel, the decomposition group and `[D18:1733]` right.
- S6 marks the heat-kernel form as a gloss.
- The table's Deninger row reads `F_p^* = p^Theta`.
- Part IV's registration list matches the verdicts above once R8's two replacements are made.

### The six facts to be registered: verbatim check

| address | text found at the address | verdict |
|---|---|---|
| `[D05:674]` | "The existence of a conformal metric for the flow simplifies the analysis. However, I do not think that such a metric will exist for dynamical systems relevant to number fields. In order to verify equation (\ref{eq:11n}) for them one will need the K\"ahler identities on cohomology." | **exact**, one line |
| `[D05:825]` | "2) Actually the conditions of the corollary force $\alpha = 0$ i.e. the flow must be isometric with respect to $g$." | **exact** |
| `[D05:1230]` | "The construction of $(X , \phi^t)$ that we made for ordinary elliptic curves is misleading however, since it almost never happens that a variety in characteristic $p$ can be lifted to characteristic zero {\it together with its Frobenius endomorphism}." | **exact** (the line begins with the end of the conformality sentence) |
| `[D18:512]` | "… the space $X_0$ is connected as well. … We also show the somewhat stronger statement that the zeroth ``foliation cohomology'' of $(X_0 , \Fh)$ is one dimensional." | **exact**, both sentences on the one line |
| `[D18:559]` | "We should stress though that we have yet to define analytical structures on our spaces and in the $p$-adic case even a topology." | **exact** |
| `[D18:2363]` | "Thus $\tX = \ceX (\C) \times \R^{> 0}$ maps naturally and $\Q^{> 0}$-equivariantly to $\A^{> 0} = \A_f \times \R^{> 0} \subset \A$ with its $\Q^{> 0}$-action. … One may wonder if it is possible to study the $\Q^{> 0}$-action on $\tX$ from their non-commutative point of view …" | **exact**. At this line the source writes `A^{>0} = A_f x R^{>0}`; at `:2411` it redefines `A^{>0} = A^x_f x R^{>0}`. Register the `:2363` form verbatim, as the note does in D7 |

All six reproduce their sources verbatim at the stated line.

**R8, re-read after the two replacements.** R8(c) now reads "a ring endomorphism for every even letter
`A = 1 (+) a`, and an automorphism when `a != 0`" and "`C^{1|2} (x) conj(C^{1|2})` … is not the cohomology
ring of the curve", word for word the two replacements; (a), (b), the proof and the Reading are unchanged and
were already correct.

VERDICT prop:deninger-product-genus-one: VALID
(Justification: both overstatements are gone. What (c) now claims is what the genus-one wedge computation in
`scratch_den_r8.py`/`scratch_den_v2.py` and 06f support: endomorphism always, automorphism iff `a != 0`, and at
genus two not the curve's cohomology ring.)

**Tally (version 2, final): 8 VALID / 0 MINOR / 0 INVALID.** The earlier MINOR line for
`prop:deninger-product-genus-one` above is superseded by the VALID line directly above.
