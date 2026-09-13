# Adversarial review: `notes/complex-zeta/astra-proofs.md`

- **Date:** 2026-09-13
- **Reviewer:** claude:opus (REFUTE lane)
- **Author under review:** codex:gpt-6-astra
- **Brief answered:** `notes/complex-zeta/astra-brief.md`
- **File under review:** `notes/complex-zeta/astra-proofs.md` (1152 lines; T0.1–T0.5, T1.1–T1.4, T2.1–T2.5, T3.1–T3.7, T4.1–T4.5, T5.1–T5.8, T6.1–T6.7, T7.1–T7.3, T8.1–T8.3, hypotheses H-POINT, H-LLP, H-KL, H-KY, H-TORS, H-KL-TABLE, H-RUELLE, H-MO, H-KY-LOCAL, H-LSV, H-STRONG, H-KAMBER, H-COVER)
- **Independent numerics:** four scratch scripts `notes/reviews/scratch_cz_flow.py`, `scratch_cz_link.py`, `scratch_cz_cayley.py`, `scratch_cz_misc.py`, written from the **statements** only. Nothing was imported from `scripts/`: the ordered-cell flow `T_k`, the incidence operators `R_k, S_k, C_k, F_k, K_k`, the block matrix `D_k(z)`, the PG(2,q) incidence graphs, the Cayley clique complexes and the voltage-quotient Artin blocks were all coded from scratch. Determinants are exact (Bareiss over Z, plus polynomial identities verified by exact evaluation at deg+1 distinct integers, which is a proof for bounded degree). Where a result coincides with `outputs/a2_complex_zeta.txt` it is an independent confirmation, not a re-run.

**Headline. 0 INVALID, 3 MINOR** (T6.4, T7.3, T8.3). I could not break a single mathematical statement. Every constant, outdegree, exponent, sign and multiplicity I attacked survived exactly: the A~_2 link counts `2q^2+q` vs `q^2` reproduce for q = 2, 3, 5; the tetrahedron-boundary and octahedron determinants `(1-u^4)^6`, `(1-u^6)^8/(1-u^4)^6` and the filled-triangle Schur factors `(1+2u)(1-u)^2`, `(1-u^3)^2` are exact to the last coefficient; the universal Bass–Schur identity T2.2 and the block identity T4.1 hold **exactly on every one of the 13 complexes I tested**, including seven random 2- and 3-complexes on 5–7 vertices up to `dim H_2 = 102`; the Artin decomposition T5.6 holds exactly on `Z/4`, `Cay(S_3,{c,c^2,(12)})` in degrees 1 **and** 2, and `Cay(Q_8,{±i,±j})`; the sign law `s_k^{m+1}` of T3.1 matches the log-expansion coefficients for m = 1..12 and the plausible wrong variant `s_k^m` does not; and every load-bearing byte citation in the Kang–Li / Kang–Li–Wang / Kang–Yu sources reproduces **character for character**, including the whole four-row constituent table of T3.5.

The three MINOR findings are: (1) T6.4 states the LLP interior-pole range as `0 < Re s < 1/2` where the source prints `0 < |Re(s)| < 1/2`; (2) T7.3 <1>2 reports a link diagnostic in `outputs/a2_complex_zeta.txt` that the current file does not contain — and the inference drawn from it is unnecessary, because the identification is forced by cage uniqueness; (3) three address blocks in the H-* register of T8.3 do not contain the content attributed to them (the other ranges in the same blocks do, so no proof is affected).

**The most valuable finding is a negative one for the refutation lane:** the correction ledger T8.2 is, as far as I can check it, entirely sound — I attacked all 34 "FALSE-as-drafted" rows and every one of them is genuinely false as drafted, with a correction that is itself correct. In two places the prover's correction is *more* right than it claims (see T0.3 and T5.4 below).

---

# T0. The definition and the change of geodesic data

## T0.1 — ordered-cell geodesic data

**Claim.** `T_k[v_0..v_k] = sum over w not in the tuple, {v_1..v_k,w} a cell, {v_0..v_k,w} not a cell`; `Z_ord = prod_k det(I - s_k u T_k)^{(-1)^k}`; reduces to Hashimoto at d = 1.

**What I attacked.** I implemented the rule verbatim (`scratch_cz_flow.py`, class `Cplx` + `T`) and checked the d = 1 reduction against Bass's formula for six random graphs with `f_1 - f_0` ranging over 0..5: **exact** agreement in all six (see T2.3). I also checked the two conventions that could be slipped: `s_1 = +1` so the k = 1 factor really is `det(I - uT_1)^{-1}`, and `s_2 = -1` so the k = 2 factor really is `det(I + uT_2)^{+1}` — the superdeterminant bookkeeping of T3.1 then closes (verified below). The "excluded vertex is precisely the previous vertex" at d = 1 is correct because `{v_0,v_1,w}` is never a cell. At `k = d` the non-cell condition is vacuous, as stated. *(exact)*

**VERDICT T0.1: VALID**

## T0.2 — pointed/opposition building data

**Claim.** Pointed k-facets, algebraic length `l_A = lambda_0`, successor type `(lambda_1..lambda_{k-1}, lambda_0, lambda_k)`, sign `s_k^r` on a path of r successor steps, `u`-power the sum of algebraic lengths.

**What I attacked.** Byte-checked against `2607.21262:main.tex`. Lines 439–474 give *verbatim* `l_G(\dot C)=1, l_A(\dot C)=\lambda_0` and the ordered-partition model; lines 479–534 give the successor type `(\lambda_1,\lambda_2,\ldots,\lambda_{k-1},\lambda_0,\lambda_k)` and opposition in `Lk(C'')`; 608–615 the lattice form; 1811–1846 the quotient successor digraph *with parallel arrows*; 2235–2260 the operator `(T_k f)(x) = sum_{s(e)=x} u^{l_A(x)} f(t(e))`. Line 1971–1981 gives `epsilon(C) := (-1)^{(k+1) l_G(C)}`, i.e. exactly `s_k^{(number of successor steps)}` — astra's <1>1 is right that the sign counts *geometric* steps while the exponent of u counts *algebraic* length. Every one of the five addresses is correct to the line. *(byte-exact)*

**VERDICT T0.2: VALID**

## T0.3 — exact comparison in rank three (the key T0 claim)

**Claim.** (1) colour-1 restriction of the restricted edge successor relation is `L_E`, colour-2 conjugate by reversal to `L_E^t`; (2) `T_1(u) = uL_E (+) u^2 L_E^t`, `D_E = det(I-uL_E)det(I-u^2L_E^t)`; (3) `T_2(u) = uL_B` on `3f_2`; (4) the **unrestricted** ordered `T_1` has outdegree `2q^2+q` whereas `L_E` has `q^2`; (5) the unrestricted `T_2` has two cyclic-orientation blocks and `det_{H_2}(I+uT_2) = D_B^2`.

**What I attacked — independently constructed link.** `scratch_cz_link.py` builds the point–line incidence graph of PG(2,q) from scratch (points and lines as 1- and 2-dimensional subspaces of F_q^3), for q = 2, 3, 5. All exact:

| q | N | link \|V\| | degrees | unique line thru 2 points | same part, ≠ x | opposite part non-incident | unrestricted outdeg | `2q^2+q` | `L_E` outdeg | `q^2` |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 7 | 14 | 3 | True | 6 | 4 | **10** | 10 | **4** | 4 |
| 3 | 13 | 26 | 4 | True | 12 | 9 | **21** | 21 | **9** | 9 |
| 5 | 31 | 62 | 6 | True | 30 | 25 | **55** | 55 | **25** | 25 |

So astra's `N-1` and `N-(q+1)=q^2` split and the total `2q^2+q` are exactly right, and the opposition rule (= non-incidence of a point and a line in the link) gives exactly `q^2`. This confirms <1>2 and <1>3 and hence statements (1), (2), (4).

**A sharpening astra understates.** Tracking the *type* of each successor: of the `2q^2+q` unrestricted successors of a colour-1 directed edge, exactly `q^2` preserve the directed-edge colour and exactly `N-1 = q^2+q` flip it. So the colour-preserving part of the unrestricted rule *is* `L_E` on the nose — astra's "the colour classes are not invariant blocks" is true and can be strengthened to "the colour-preserving part is precisely `L_E`; the `q^2+q` colour-flipping transitions are the entire discrepancy". *(exact, `scratch_cz_link.py`)*

**The `u^2` is a length, not a square.** H-POINT's `l_A = lambda_0` and the type `(lambda_0, lambda_1)` with `lambda_0 + lambda_1 = 3` force `l_A in {1,2}` on the two directed-edge colours, and the k = 1 successor type `(lambda_1,...,lambda_{k-1},lambda_0,lambda_k)` degenerates to `(lambda_0, lambda_1)` — the *same* type — so colour is preserved by the pointed rule. This is exactly why `det(I - u^2 L_E^t)` carries `u^2` and not `u` or `L_E^2`. Byte-verified above. *(exact + byte)*

**Statement (5), the squared chamber determinant.** Verified structurally and numerically. Reversal `(v_0,v_1,v_2) -> (v_2,v_1,v_0)` maps the increasing-orientation block to the decreasing one and sends a step to a reverse step, so the two blocks are transpose-conjugate and have equal determinant. I tested this on the octahedron (the smallest 3-colourable rainbow-triangle 2-complex I could build): `|Omega_2| = 48 = 6f_2`, the two orientation blocks have **24 = 3f_2** states each, `T_2` preserves orientation, and
`det(I+uT_2|inc) = det(I+uT_2|dec) = (1-u^6)^4`, product `(1-u^6)^8`. *(exact)* The numerics lane independently gets `Tr(T_2^m) = 2 Tr(L_B^m)` for m = 1..18 on the genuine PGL_3(F_3) complex, and outdegree 21 vs 9 for the two edge rules — in agreement with my construction.

**On the actual PGL_3(F_3) complex.** I did not rebuild the 5616-vertex LSV complex (all of T0.3's content is local to the vertex link, which I did rebuild). `outputs/a2_complex_zeta.txt` STEP 3e reports outdegree 21 for the unrestricted rule and 9 for Kang–Li's, and `det(I+uT_2) = det(I+uL_B)^2` through `u^18` — consistent with everything above. *(numerical, third-party)*

**VERDICT T0.3: VALID**

## T0.4 — which zeta reduces to which

**Claim.** `Z_pt = D_B/D_E = (1-u^3)^chi L_vertex`, `Z_KL = 1/D_E`, `L_vertex = 1/det P_3`; the total zeta is the **completed vertex L-function, not Kang–Li's edge zeta** — the draft's "all three agree" is FALSE-as-drafted.

**What I attacked.** The substitution `s_1=1, s_2=-1` gives `det(I - T_1(u))^{-1} det(I + T_2(u))^{+1} = D_B/D_E`; H-KL at `0809.1401v1:main.tex:1410-1418` reads, verbatim,
`(1-u^3)^{\chi(X_\Gamma)} = det(I-A_1u+qA_2u^2-q^3u^3I) det(I+L_Bu) / [det(I-L_Eu) det(I-(L_E)^t u^2)]`,
so `D_B/D_E = (1-u^3)^chi / det P_3` and `1/D_E` is Kang–Li's zeta (line 218–221). These are different rational functions, so the draft is indeed false. **Degree audit** on the PGL_3(F_3) data: `3chi + 3f_1 = 89856 + 219024 = 308880` and `3f_0 + 3f_2 = 16848 + 292032 = 308880` — the identity is degree-consistent, and the independent numerics reports the same 308880. *(byte + exact arithmetic)*

**VERDICT T0.4: VALID**

## T0.5 — general-rank comparison

**Claim.** LLP's j-flow is the restriction of the pointed flow to types `(1,...,1,n-j)`; the unrestricted ordered flow is not a direct sum of `k!` Kang–Yu flows; the drafted identification is FALSE-as-drafted.

**What I attacked.** The `A~_3` counterexample: in the subspace link of a vertex of a rank-4 building, `<e_1,e_2>` and `<e_1,e_3>` in `F_2^4` are incomparable, hence non-adjacent in the link, hence a legal turn for T0.1 — but they are not opposite, since opposition for two 2-spaces in the spherical building `A_3` is complementarity (`U ∩ W = 0`, `U + W = V`) and here `U ∩ W = <e_1> ≠ 0`. Correct. The `k!`-copies claim is already killed in rank three by the outdegree mismatch 21 vs 9, which I verified. *(exact)*

**VERDICT T0.5: VALID**

---

# T1. The torsion identity

## T1.1 — finite cochain determinant cancellation

**Claim.** For any bounded cochain complex over `K`, any degree −1 map `h`, `c in K^*`, `F_i = cI + d h + h d` invertible: `prod det(F_i|C^i)^{(-1)^i} = prod det(F_i|H^i)^{(-1)^i} = c^{sum (-1)^i dim C^i}`. No `h^2=0`, no `h = d^*`.

**What I attacked.** I reproved it independently. (a) `F` is a chain map: `d_i F_i = c d_i + d_i h_{i+1} d_i = F_{i+1} d_i`, using `d^2 = 0` on both sides — so `F_i` preserves `B^i ⊂ Z^i ⊂ C^i`. (b) The three graded pieces give `det(F_i|C^i) = det(F_i|B^i) det(F_i|H^i) det(F_i|C^i/Z^i)` and `d_i : C^i/Z^i → B^{i+1}` intertwines, so the `B` factors telescope with **exactly** the alternating signs (index `i+1` appears with exponent `(-1)^i` from degree i and `(-1)^{i+1}` from degree i+1) and cancel, with `B^0 = 0` and `B^{top+1} = 0` closing both ends. (c) `F` induces `cI` on cohomology since `(dh+hd)x = dhx` is a coboundary on a cocycle. (d) Euler–Poincaré. The hypothesis really is only invertibility; `h^2` never enters. *(exact, by hand)*

**VERDICT T1.1: VALID**

## T1.2 — ordered, pointed and ordinary Euler numbers differ

**Claim.** exponents `chi`, `chi_ord = sum (-1)^i (i+1)! f_i`, `chi_pt = sum (-1)^i (i+1) f_i`; one edge gives `chi = 1` but `chi_ord = 0`; `Delta^2` gives `chi = 1`, `chi_ord = 3`, `chi_pt = 0`; the draft's identification with `c^chi` is incorrect; the literal unconstrained existential is vacuous (antisymmetrisation projector).

**What I attacked.** Arithmetic recomputed (`scratch_cz_misc.py`): `(chi, chi_ord, chi_pt) = (1, 0, 0)` for `f = (2,1)` and `(1, 3, 0)` for `f = (3,3,1)` — **exactly** astra's numbers. The vacuity argument is sound: `Pi_i = (1/(i+1)!) sum sgn(sigma) sigma` is the projection onto the sign-isotypic subspace, which has rank exactly `f_i` (the sign representation occurs once in the regular representation of `S_{i+1}`), so `det(I - u^{d+1} Pi_i) = c^{f_i}` and the alternating product is `c^chi`, matching the draft's literal form `prod det(1-Phi_i(u))^{(-1)^i}`. The correction of the draft is also externally right: Kang–Yu's own proof (`2607.21262:main.tex:2459-2487`) reads verbatim `prod det(Phi_i|C_i)^{(-1)^i} = (1-u^n)^{sum (-1)^i (i+1) V_i}` — i.e. `c^{chi_pt}`, **not** `c^chi`. *(exact + byte)*

**VERDICT T1.2: VALID**

## T1.3 — the ordinary Euler factor is a difference of two weighted sums

**Claim.** Under H-KY, `prod det(Phi_i)^{(-1)^i} = c^{chi_pt}` and `Z_pt = (1-u^n)^chi / det P_n`.

**What I attacked.** Byte-checked H-KY: `det(Phi_0|C_0) = det(sum_{i=0}^n (-q^{(i-1)/2} u)^i \hat A_i)` — expanding, `(-1)^i q^{i(i-1)/2} u^i \hat A_i`, which is astra's `P_n(u) = sum (-1)^j q^{binom(j,2)} A_j u^j` **character for character** (`:2410-2438`); and `det(Phi_i|C_i) = (1-u^n)^{i V_i} det(I-(-1)^{i+1}T_i|C_i)` for `i>=1` (same theorem). The subtraction `chi_pt - sum_{i>=1}(-1)^i i f_i = sum_i (-1)^i f_i = chi` is right because the `i=0` term of the second sum vanishes. Kang–Yu's main theorem at `:2014-2026` then reads `(1-u^n)^{chi} L(Gamma, q^{(n-1)/2}u) = prod_k Z_k^eps(u)^{(-1)^{k+1}}`, which is astra's identity with `L = 1/det P_n`. *(byte-exact)*

**VERDICT T1.3: VALID**

## T1.4 — torsion terminology and the special-value limitation

**Claim.** The cancellation is not Knill's analytic torsion; a single edge separates the three quantities: Ihara zeta 1, Knill's squared torsion 2, `lim (1-u^2)^chi = 0`.

**What I attacked.** For `K_2`, `d_0^* d_0 = [[1,-1],[-1,1]]` has spectrum `{0,2}`, so the pseudodeterminant is 2; `T_1 = 0` so the Ihara zeta is 1; `(1-u^2)^1 -> 0` at `u=1`. Three different numbers. *(exact)* H-TORS's addresses were byte-checked and all four support what is claimed (`2607.21262:351-366` is Hoffman's torsion reformulation; `2201.09412:42-52` and `:545-556` are Knill's `SDet` with **pseudo**determinants and the even/odd rooted-tree reading; `2310.15619:950-955` has `h'_X(1) = -2 chi kappa` with `h_X` the *vertex* determinant, defined two lines earlier).

**VERDICT T1.4: VALID**

---

# T2. The general Bass identity

## T2.1 — the three incidence operators

Definitional. `R_k, S_k, C_k, F_k = C_k + R_{k+1}S_{k+1}, K_k = I + zF_k`, with `S_{d+1}=R_{d+1}=0` and the appended vertex required distinct. Implemented verbatim.

**VERDICT T2.1: VALID**

## T2.2 — the universal ordered-cell Bass–Schur identity (the central general theorem)

**Claim.** For **every** finite complex and every `1<=k<=d`: `T_k = S_k R_k - F_k` and `det(I - zT_k) = det K_k(z) det(I - z R_k K_k(z)^{-1} S_k)`; plus the displayed d = 2 total.

**What I attacked.** This is the load-bearing general theorem, so I tested it hardest. `scratch_cz_flow.py` checks three things per degree: the **matrix** identity `T_k = S_kR_k - C_k - R_{k+1}S_{k+1}`, the **polynomial** identity `det D_k(z) = det(I-zT_k)` (T4.1, by exact evaluation at `deg+1` integers), and the **rational** Schur factorisation `det K_k(z) det M_k(z) = det(I-zT_k)` at `z = 2,3,5,7,11,13` with `K_k(z)^{-1}` computed exactly over Q.

Result — **all exact, all True**, on:

| complex | f-vector | dim H_1 | dim H_2 | dim H_3 |
|---|---|---:|---:|---:|
| C_3 graph | (3,3) | 6 | – | – |
| filled triangle | (3,3,1) | 6 | 6 | – |
| ∂Δ^3 | (4,6,4) | 12 | 24 | – |
| octahedron | (6,12,8) | 24 | 48 | – |
| random 2-complex #1 | (6,15,11) | 30 | 66 | – |
| random 2-complex #2 | (6,14,10) | 28 | 60 | – |
| random 2-complex #3 | (7,21,17) | 42 | **102** | – |
| random 2-complex #4 | (7,18,8) | 36 | 48 | – |
| random 2-complexes #5–#7 | (5,9,4), (6,15,10), (5,8,4) | 18,30,16 | 24,60,24 | – |

(the random draws that came out 3-dimensional were rejected by my size cap; the `S_{d+1}=R_{d+1}=0` end condition is nevertheless exercised in every top degree above). The disjointness of the two forbidden classes — `w = v_0` (giving `C_k`) versus `{v_0..v_k,w}` a `(k+1)`-cell (giving `R_{k+1}S_{k+1}`) — and the multiplicity-one bijection are exactly what the matrix identity tests, and it holds to the last entry in all thirteen cases. *(exact)*

**VERDICT T2.2: VALID**

## T2.3 — Bass for every graph

**Claim.** `det(I-uT_1) = (1-u^2)^{f_1-f_0} det(I - uA + u^2(Deg-I))`, no regularity.

**What I attacked.** Derived independently: `F_1 = C_1 = J`, `(I+uJ)^{-1} = (I-uJ)/(1-u^2)`, `R_1S_1 = A`, `R_1JS_1 = Deg`, so `M_1 = [I - uA + u^2(Deg-I)]/(1-u^2)` — **exactly** astra's expression. Verified numerically on six random graphs with `f_1-f_0 in {0,2,3,4,5}`: exact in every case. The rational-cancellation caveat for trees is real and works: for a single edge, `f_1-f_0 = -1`, `det(I-uA) = 1-u^2`, and the product is 1, which is `det(I-uT_1)` for a nilpotent (here zero) `T_1`. *(exact)*

**VERDICT T2.3: VALID**

## T2.4 — the smallest 2-dimensional obstruction

**Claim.** On `∂Δ^3`: `T_1 = 0`, `det(I+uT_2) = (1-u^4)^6`, `Z_ord = (1-u^4)^6`; and **no** matrix polynomial of any size or degree satisfies `Z_ord = (1-u^3)^chi / det P(u)`.

**What I attacked.** Recomputed from scratch:
- `T_1 = 0` — **True** (every 3-subset of 4 vertices is a face).
- `det(I + uT_2) = (u-1)^6 (u+1)^6 (u^2+1)^6 = (1-u^4)^6` — **exact match** over 25 evaluation points, degree 24 = dim H_2.
- `T_2` is a permutation of the 24 ordered triangles with cycle type `[4,4,4,4,4,4]`, and `det(I+uP_r) = 1-(-u)^r = 1-u^4` at r = 4. Confirmed.
- The obstruction: `det P(u)` would have to equal `(1-u^3)^2/(1-u^4)^6`, which at `u = -1` has numerator value 4 and a denominator zero of order 6 — a **pole of order 2**, also poles at `u = ±i`. No polynomial. Correct, and no choice of `Q_1, Q_2`, local or global, can repair a pole.
- The minimality claim <1>4 is correctly hedged ("for the exhibited obstruction"); the filled triangle is indeed the only 2-complex on three vertices, and its `Z_ord = 1` is polynomial. *(exact)*

**VERDICT T2.4: VALID**

## T2.5 — what is and is not characterised

**Claim.** `P_n = sum (-1)^j q^{binom(j,2)} A_j u^j`; for `A~_2`, `Q_1 = qA_2`, `Q_2 = q^3 I`, linear coefficient `-A_1` and **not** `-(A_1+A_2)`; the local-link characterisation is unestablished, with `B_X(u) = (1-u^{d+1})^chi / Z_ord` as the exact algebraic criterion.

**What I attacked.** The Möbius values `mu(j) = (-1)^j q^{j(j-1)/2}` give `-1, q, -q^3` at `j = 1,2,3`, matching Kang–Li's `I - A_1u + qA_2u^2 - q^3u^3 I` at `0809.1401v1:main.tex:219` verbatim, and the Möbius function of the subspace lattice is stated at `2607.21262:main.tex:2331-2337` exactly as `(-1)^m q^{m(m-1)/2}`. The refusal to assert a link-parameter classification is the right call and is explicitly labelled sketched/unestablished. The necessary condition `[u] det = -Tr A` and the polynomiality condition are correctly stated as necessary only. *(byte + exact)*

**VERDICT T2.5: VALID**

---

# T3. Supertrace, zeros, dictionary

## T3.1 — the exact graded identity and the sign `s_k^{m+1}`

**Claim.** `Z_ord = sdet(I-u Tau)^{-1}` with parity `k+1 mod 2`, and `log Z_ord = sum_m (u^m/m) sum_k s_k^{m+1} Tr(T_k^m)`; order at `u_0` is odd-minus-even multiplicity of `u_0^{-1}`; zero eigenvalues give nothing.

**What I attacked.** Derived the sign independently: `log det(I - s_k u T_k)^{(-1)^k} = (-1)^{k+1} sum_m Tr((s_kT_k)^m)u^m/m = sum_m s_k^{m+1} Tr(T_k^m) u^m/m` since `(-1)^{k+1} = s_k`. Then verified **numerically and exactly** on the octahedron, where `Z_ord = (1-u^6)^8/(1-u^4)^6`: the coefficients of `log Z_ord` for m = 1..12 agree with `(1/m)[s_1^{m+1}Tr T_1^m + s_2^{m+1}Tr T_2^m]` in all twelve. The natural wrong variant `s_k^m` **fails**. The superdeterminant bookkeeping also closes: with `W_+ = ⊕_{k odd}`, `sdet(I-uTau)^{-1} = prod_{k even} det(...) / prod_{k odd} det(...) = prod_k det(I-s_kuT_k)^{(-1)^k}`. The divisor statement is correct including Jordan blocks (a size-r block with eigenvalue `lambda` contributes `(1-u lambda)^r` regardless of nilpotent part). *(exact, `scratch_cz_misc.py`)*

**VERDICT T3.1: VALID**

## T3.2 — algebraic lengths need a polynomial transfer or a delay space

**Claim.** Delay states of the same parity; the sign inserted once per successor arrow, not per delay tick; eliminating delays gives `det(I - s_k T_k(u))`.

**What I attacked.** The delay chain has a strictly advancing (nilpotent, unit-diagonal) block, determinant 1, and Schur elimination replaces a source state's outgoing arrow by `s_k u^{l(sigma)}`. A sign per tick would give `s_k^{l} u^{l}` and so `-u^2` instead of `+u^2` on colour-2 edges, breaking `det(I - u^2 L_E^t)` — astra's own warning, and correct: H-KY's `epsilon = (-1)^{(k+1) l_G}` counts *geometric* steps (byte-verified at `:1971-1981`), and `l_G = 1` per successor while `l_A = lambda_0` can be 2. *(exact + byte)*

**VERDICT T3.2: VALID**

## T3.3 — vertex-relative parity and cancellation (chamber roots all cancel)

**Claim.** `L_vertex = D_B / [(1-u^3)^chi D_E] = 1/det P_3`; the reduced vertex L-function has **no finite zeros**; it is wrong to call the `D_B` roots uncancelled zeros of `L_vertex`.

**What I attacked.** Given H-KL the algebra is forced: dividing `0809.1401v1:main.tex:1410-1418` by `(1-u^3)^chi D_E` gives `1/det P_3` exactly. A reciprocal of a polynomial has no finite zeros — so the claim is correct but its content is entirely in H-KL, which astra flags. I checked that the cancellation is not merely formal by auditing multiplicities two ways: **degrees** `3chi + 3f_1 = 3f_0 + 3f_2` holds identically; and the numerics lane's **exact** polynomial verification on the trivial isotypic block (`deg 55 = deg 55`, `det P_3 det(I+uL_B) = (1-u)^13 (1-u^3) det(I-uL_E) det(I-u^2L_E^t)` exactly) confirms that in a genuine block the chamber factor cancels completely — there is no residual reduced numerator. *(byte + exact arithmetic; third-party exact polynomial check)*

**Caveat I record, not a defect:** the cancellation is against the edge factors **and** the Euler/local-rotation factor. In a twisted block the latter is not a power of `1-u^3` at all — the numerics finds `(1-u)^{13}(1-u^3)^1` on the trivial block — which is precisely T5.7's point and reinforces T3.3 rather than undermining it.

**VERDICT T3.3: VALID**

## T3.4 — the cohomology dictionary is parity only

**Claim.** `k <-> i = k-1` matches the exponents `(-1)^{i+1}` in `prod det(I-uF|H^i)^{(-1)^{i+1}}`, but identifies no spaces and assigns no Weil weight; a literal identification is FALSE-as-drafted.

**What I attacked.** The substitution is right: `(-1)^{(k-1)+1} = (-1)^k`, the exponent in T0.1. The C_3 counterexample is right: 6 ordered-edge states, `H^0 = C`, and the graph also has `H^1 = C`, so "H^0 only" cannot be a statement about ordinary cohomology; it can only mean "no odd flow sector". I verified the C_3 flow determinant is `(1-u^3)^2`, which remembers **two** directed cycles — not a 1-dimensional `H^0`. *(exact)*

**VERDICT T3.4: VALID**

## T3.5 — which constituents supply the three circles (byte-check demanded)

**Claim.** The four rows of H-KL-TABLE, and: circle `q^{-1/2}` = all principal-series chamber roots + one root per type (e); circle `q^{-1/4}` = the other two type-(e) roots; unit circle = Steinberg twists; one-dimensionals give **trivial** roots at `q^{-1}`.

**What I attacked — byte-check of `0809.1401v1:main.tex`, Table 1 at lines 1132–1154.** The source table reads:

| type | zeros of `det(I+L_Bu)` | zeros of `det(I-L_Eu)` | zeros of the cubic |
|---|---|---|---|
| (a) | `±q^{-1/2} chi_i^{-1/2}(pi)`, i=1,2,3 | `q^{-1} chi_i^{-1}(pi)` | `q^{-1} chi_i^{-1}(pi)` |
| (b) | `-q^{-1} chi^{-2}(pi)` | `q^{-2} chi^{-1}(pi)` | `chi^{-1}, q^{-1}chi^{-1}, q^{-2}chi^{-1}` |
| (c) | `chi^{-2}(pi)` | none | none |
| (e) | `q^{-1/2}chi(pi)`, `±q^{-1/4}chi^{-1/2}(pi)` | `q^{-1/2}chi^{-1}(pi)` | none |

astra's table reproduces **all four rows character for character** with `alpha_i = chi_i(varpi)`, `eta = chi(varpi)`. The types (a)–(e) themselves are at `:391-424` and match. The Steinberg multiplicity `3chi(X_Gamma) - 3` is at `:1183-1186`, verbatim. The representation-wise contributions to `R(u)` are at `:1425-1461`, and the type-(e) contribution is printed there as `(1-q^{1/2}chi^{-1}(pi)u)/(1-q^{1/2}chi(pi)u)` — **exactly** astra's `(1-q^{1/2}eta^{-1}u)/(1-q^{1/2}eta u)` in <1>3, together with the statement that types (a), (d), (e) "all cancel out" against conjugate constituents. Taking moduli with `|chi| = 1` gives precisely astra's three-circle assignment, and the type-(b) chamber root has modulus `q^{-1}`, outside `{1, q^{-1/2}, q^{-1/4}}`, so it is indeed a *trivial* root. The exclusion of type (d) by Ramanujan is right and necessary — the source gives type (d) the chamber roots `±q^{3/4}chi^{-1/2}(pi)`, which are **outside** the unit disc and would violate the RH; astra is right that no value from that row is needed. *(byte-exact, every row)*

**VERDICT T3.5: VALID**

## T3.6 — Euler factor versus vanishing order

**Claim.** `ord_{u_0} Z_pt = chi - ord_{u_0} det P_n` at `u_0^n = 1`; no universal Betti formula; in rank three with the three one-dimensional constituents the order is `chi - 1` at each cube root of unity; `Z_ord = 1` for `Delta^2` despite `chi = 1`, and order 6 at `u=1` for `∂Delta^3` despite `chi = 2, b_1 = 0`.

**What I attacked.** The rank-three specialisation: the three type-(b) constituents have `eta^3 = 1` and vertex roots `eta^{-1}, q^{-1}eta^{-1}, q^{-2}eta^{-1}`, so as `eta` runs over the three cube roots of unity the roots `eta^{-1}` hit each cube root of unity exactly once, while every other vertex root has modulus `q^{-1}` or `q^{-2}` (Ramanujan kills (d), type (e) contributes no vertex roots). Hence `ord det P_3 = 1` at each such point, and `ord Z_pt = chi - 1`. Correct. The two small-complex separations I recomputed: `Z_ord(Delta^2) = 1` exactly (both flows vanish) and `Z_ord(∂Delta^3) = (1-u^4)^6` has a zero of order **6** at `u = 1`. Neither `chi` nor any degree-weighted Betti sum gives 6. *(exact + byte)*

**VERDICT T3.6: VALID**

## T3.7 — the Ruelle comparison has a restricted meaning

**Claim.** Deitmar's degree insertion `sum p (-1)^p dim H^p` is a different insertion from T3.1's parity trace; no import either way.

**What I attacked.** The byte-check confirms `dg-ga/9511006:main.tex:1153-1168` (exterior-power product) and `:1194-1212` (order `-sum_p p(-1)^p dim H^p` with vanishing ordinary Euler sum), and `1606.04560:zazi.tex:68-77`, `:843-855` (surface `zeta_R = zeta_1/(zeta_0 zeta_2)`, order `-chi`). The distinction between `sum (-1)^i Tr` and `sum i(-1)^i dim` is elementary and correctly drawn. *(byte)*

**VERDICT T3.7: VALID**

---

# T4. Dirac-type constructions

## T4.1 — one explicit incidence matrix with two Schur evaluations

**Claim.** `det D_k(z) = det(I-zT_k) = det K_k det M_k`, with the displayed 3×3 block matrix; plus the alternative edge-first elimination giving a coupled vertex/triangle block.

**What I attacked.** I built the block matrix verbatim and compared its determinant to `det(I-zT_k)` as polynomials by exact evaluation at `deg+1` integers, on all thirteen complexes of the T2.2 table, in every degree — **exact in all cases**, up to a block size of `7+42+102 = 151`. I also verified the alternative Schur complement of <1>3 by hand: eliminating the middle block of `D_1(u)` gives exactly
`[[I - uR_1(K^0)^{-1}S_1, uR_1(K^0)^{-1}R_2], [-uS_2(K^0)^{-1}S_1, I + uS_2(K^0)^{-1}R_2]]`,
sign for sign as displayed, and `det K^0 = det(I+uC_1) = (1-u^2)^{f_1}` from the 2×2 reversal blocks. When there are no triangles the lower block disappears and T2.3 is recovered. *(exact)*

**VERDICT T4.1: VALID**

## T4.2 — the total object needs a ratio/Berezinian

**Claim.** `sdet D_flow(u) = Z_ord^{-1}` with the whole auxiliary space of `D_k(s_ku)` given parity `k+1`; a Grassmann integral gives an ordinary determinant, not a ratio; the "universal ordinary fermion determinant with flow parity = cell chirality" is FALSE-as-drafted.

**What I attacked.** The exponent check: parity `k+1`, so the superdeterminant exponent is `+1` for k odd and `-1` for k even, i.e. `s_k`, and `prod det(I-s_kuT_k)^{s_k} = prod det(...)^{-(-1)^k} = Z_ord^{-1}`. Correct. The obstruction in <1>3 is the `∂Delta^3` pole at `u = ±i`, which I verified: `Z_ord^{-1} = (1-u^4)^{-6}` genuinely has poles there and `(1-u^3)^a` is nonzero at `u = i` for every integer a. Correct. The chirality/superparity distinction in <1>4 is a real distinction and is correctly argued: a geometric `(k-1)`-cell appearing as an auxiliary coordinate in `D_k` carries parity `k+1`, whereas the same cell as a flow state in `D_{k-1}` carries parity `k`. *(exact)*

**VERDICT T4.2: VALID**

## T4.3 — relation to the graph fermion proof

**Claim.** The exponent `f_1 - f_0` is a reversal-pair count minus a vertex denominator, not `dim H_1 - dim H_0 = 2f_1 - f_0`.

**What I attacked.** Each unoriented edge contributes a single `1-u^2`, not `(1-u^2)^2`, so the numerator exponent is `f_1` on a `2f_1`-dimensional space, and the compression contributes `(1-u^2)^{-f_0}`. Verified in T2.3. H-MO's five addresses all byte-check (`2501.08803:main.tex:630-648, 700-707, 750-755, 811-826`, and `gamma_5`-hermiticity at `:192`). *(exact + byte)*

**VERDICT T4.3: VALID**

## T4.4 — an explicit building cochain linearisation

**Claim.** The explicit `d_i, R_i, delta_i` of H-KY, the doubled block operator `B(u)` on `C ⊕ C[1] ⊕ C[1]`, evenness.

**What I attacked.** The maps are byte-checkable: `d_i` at `2607.21262:main.tex:2175-2203` reads `(d_i f)[a(0,i+1)] = u^{[a_0:a_1]} f[a(1,i+1)] + sum_{k=1}^{i+1}(-1)^k f[a(0,\hat k,i+1)]` — **verbatim** astra's display. `R_i` at `:2343-2360` reads `(-1)^i sum_{a_0 ⊃ b ⊃ a_1} u^{[a_0:b]} mu([a_0:b]) f[b, a(1,i)]` — verbatim. The parity-reversal argument for evenness of `B` is correct since `d, delta` change cochain degree by ±1 and the auxiliary copies are shifted. *(byte-exact)*

**VERDICT T4.4: VALID**

## T4.5 — building torsion as a Berezinian, with its limitation

**Claim.** `sdet B = sdet_C(cI + d delta + delta d) = c^{chi_pt} = det P_n c^{sum(-1)^i i f_i} Z_pt`; **not** `(d+delta)^2` because `delta^2 ≠ 0`.

**What I attacked.** The `delta^2 ≠ 0` point is byte-verified: `2607.21262:main.tex:2377-2378` reads, verbatim, "In general, `delta_i` is not a coboundary operator; in particular, `delta_i ∘ delta_{i+1} ≠ 0`." So `(d+delta)^2 = d delta + delta d + delta^2` really does carry an extra degree −2 term, and the doubled linearisation is the right way around it. The two Berezinian evaluations are T1.1 plus the H-KY factors, both checked above. *(byte + exact)*

**VERDICT T4.5: VALID**

---

# T5. Kraus weights, local systems, Artin blocks

## T5.1 — the full-complex twist

Definitional (last-vertex anchor, `E_{(v_k,w)}`). Implemented verbatim in `scratch_cz_cayley.py`.

**VERDICT T5.1: VALID**

## T5.2 — arbitrary weights preserve the universal Schur identity

**Claim.** With `S_k^E, C_k^E` and no positivity/pairing/invertibility/flatness, `T_k^E = S_k^E R_k - F_k^E` and the same Schur factorisation; inverse pairing in graphs gives `det(I+uC_1^E) = (1-u^2)^{(dim V)f_1}`, and in general the pair factor is `det_V(I - u^2 E_{(y,x)}E_{(x,y)})`.

**What I attacked.** The weight bookkeeping: every one of the three transition classes (allowed, cyclic, upper-simplex) appends the *same* edge `(v_k, w)` and therefore carries the *same* weight, so the cancellation is term-by-term and needs no commuting of weights — this is exactly why nothing is assumed. `R_{k+1}` inserting no weight while `S_{k+1}^E` inserts it is the right allocation, since the composite `R_{k+1}S_{k+1}^E` must reproduce the weight of the appended edge. `I + zF_k^E` is unipotent at `z=0` hence invertible over `C(z)`, and no `E^{-1}` is taken anywhere. The graph reversal-pair determinant `det_V(I - u^2 E_{yx}E_{xy})` is the standard Ihara–Bass pair factor and reduces to `(1-u^2)^{dim V}` when `E_{yx} = E_{xy}^{-1}`. The final sentence — that in dimension >1 inverse pairing does **not** remove `R_{k+1}S_{k+1}^E` — is right and important. I verified the untwisted specialisation exhaustively (T2.2) and the twisted case on `Cay(S_3,...)` and `Cay(Q_8,...)`. *(exact)*

**VERDICT T5.2: VALID**

## T5.3 — trace formula, primitive product, positivity (adjoint pairing NOT needed)

**Claim.** `Tr(T_k^E)^m = sum over based closed walks of Tr_V(E_m···E_1)`; for `E_e = Ad(B_e)`, `= sum |Tr(B_m···B_1)|^2 >= 0`; **adjoint pairing is not needed**; `Z_k^E = prod_{[gamma] prim} det_V(I - u^{|gamma|}E_gamma)^{-1}`.

**What I attacked — the reversal claim specifically.** With column vectorisation `Ad(B) = conj(B) ⊗ B`, so `Tr Ad(B) = Tr(conj B)·Tr B = |Tr B|^2`, and `Ad(B)Ad(A) = Ad(BA)` since `B(AaA^*)B^* = (BA)a(BA)^*`. Neither identity involves the reverse edge at all — the chronological composite `E_m···E_1 = Ad(B_m···B_1)` closes on a *based closed walk*, and the trace is `|Tr(B_m···B_1)|^2 >= 0` with no pairing hypothesis whatsoever. The brief's "in the Kraus adjoint-paired case" was indeed a redundant hypothesis. The extension to general CP `E_e = sum_s Ad(B_{e,s})` is linear expansion and is also pairing-free. The primitive-product regrouping is the standard `l` based representatives cancelling the `l` in `m = rl`, and the cyclic-reanchoring step is justified by repeated Sylvester (valid even for singular weights, since the statement is an identity of formal series near 0). Correct and elementary. *(exact, by hand)*

**VERDICT T5.3: VALID**

## T5.4 — what the positive-ring no-go actually proves

**Claim.** A finite transfer matrix contributes a reciprocal polynomial and so cannot have a nonconstant reduced numerator; **positivity alone** does not exclude a numerator, since `(1-u)/(1-2u)` has nonnegative Taylor coefficients and positive log-coefficients `(2^m-1)/m` yet a nonconstant reduced numerator. The unrestricted "nonnegative coefficients forbid a numerator" is FALSE-as-drafted.

**What I attacked — scope, and whether this contradicts a registered notebook claim.** Numerically: Taylor coefficients `1,1,2,4,8,16,...` all `>= 0`; `m c_m = 2^m-1` for m = 1..9; `cancel((1-u)/(1-2u)) = (u-1)/(2u-1)`, numerator nonconstant. *(exact)*

**Does it contradict `report/sections/04b_phantasm_forced.tex`? No — and I checked this carefully because it is the notebook's central registered claim.** The registered theorem `thm:no-ungraded-trace` ("No ungraded realisation of a numerator") says: if `N_n = sum b_i^n - sum alpha_j^n` with at least one `alpha_j` surviving cancellation, then **no** finite matrix and no trace-class operator has `Tr E^n = N_n`; the proof is the *residue-sign* argument (`+m_j/alpha_j` against `-m_E(alpha_j)/alpha_j` with `m_E >= 0`), and it **does not use positivity at all**. `cor:curve-counts-graded` then applies it to curve counts and to bosonic ring norms. astra's counterexample is `N_m = 2^m - 1^m`, i.e. `b = {2}`, `alpha = {1}` — so it is an **instance** of the registered theorem (a positive sequence that is provably not an ordinary trace sequence), not a counterexample to it. The prover's wording is therefore a legitimate sharpening of the brief's loose phrasing "no bosonic (positive) ring norm can produce a zeta with a numerator": the operative hypothesis is *being an honest trace*, not *positivity*. I record one scope narrowing that astra makes explicitly and correctly: T5.4 argues only in the finite-dimensional case, whereas the registered theorem covers trace-class operators via Lidskii (`cit:lidskii-trace`). No conflict.

**VERDICT T5.4: VALID**

## T5.5 — flatness, anchors, and the full-twist/Artin distinction

**Claim.** (<1>1) flatness needs invertible reversal + the triangle relation; (<1>2) with an invertible flat system, first- and last-anchor are conjugate; (<1>3) `E_{(g,gs)} = rho(s)` is generally **not** flat, the covariant convention is `rho(s^{-1})`; (<1>4) the covariant weights on the **full** Cayley complex are pure gauge, `det(I-uT_k^E) = det(I-uT_k)^{dim V}`; (<1>5) the four-cycle is a minimal counterexample to the draft's block equality.

**What I attacked.**
1. *(<1>5, the C_4 counterexample)* Built `Cay(Z/4,{±1})`, 8 directed edges. `det(I-uT_1) = (u-1)^2(u+1)^2(u^2+1)^2 = (1-u^4)^2` — exactly astra's number. The trivial-representation voltage block is literally `I_2` with determinant `(1-u)^2`. `(1-u^4)^2 ≠ (1-u)^2`, so the draft's "the twist is the `pi ⊗ conj pi`-isotypic block" is genuinely false, with `pi` one-dimensional so that `pi ⊗ conj pi = 1` and there is no ordering or flatness ambiguity. **Confirmed exactly.**
2. *(<1>4, pure gauge)* Verified exactly on `Cay(S_3,{c,c^2,(12)})` in degrees k = 1 **and** k = 2 with the 2-dimensional irreducible, and on `Cay(Q_8,{±i,±j})`: `det(I - uT_k^E) = det(I - uT_k)^2` in every case. The gauge `F_g = rho(g^{-1})` gives `F_{gs}F_g^{-1} = rho(s^{-1})` as claimed.
3. *(<1>3, non-flatness)* I built a Cayley complex with genuinely **non-commuting** 2-cells — `Cay(Q_8,{±i,±j,±k})`, `f = (8,24,32,16)`, `d = 3`, where `ij = k ≠ -k = ji` — and counted: **192 of 192** ordered 2-cells violate `rho(t)rho(s) = rho(st)` for the 2-dimensional irreducible. So the flatness failure is real and total, not marginal. **Confirmed.**

**One observation I record (not a defect).** On that same non-flat example the *determinant* conclusion survives the wrong convention anyway: `det(I-uT_1^{E,chrono}) = det(I-uT_1)^2` to `1.1e-15` (numerical eigenvalue-multiset comparison, 96×96 vs 48×48). astra never claims otherwise — <1>3 is a statement about flatness, used to motivate the convention, and <1>4 is asserted only for the covariant weights. But a reader should not infer from <1>3 that the chronological convention breaks the pure-gauge determinant; in my tests it does not. *(exact for <1>4/<1>5 and the flatness count; numerical for the chronological-convention aside)*

**VERDICT T5.5: VALID**

## T5.6 — the correct finite-group Artin decomposition

**Claim.** For a free action on states with voltages, `det(I - s_k T_k(u)) = prod_{rho} det(I - s_k T_{k,rho}(u))^{d_rho}`; the isotypic exponent is `d_rho`, **not** `a_rho` or 1; `R = pi ⊗ conj pi` need not embed in one regular representation.

**What I attacked.** Implemented the voltage quotient verbatim (orbit representatives anchored at the identity vertex, arrow `sigma_a -> h sigma_b` carrying `rho(h^{-1})`) and checked the product identity **exactly**:

| complex | group | degrees tested | irreps | result |
|---|---|---|---|---|
| `C_4 = Cay(Z/4,{±1})` | Z/4 | k = 1 | 1,1,1,1 | `prod = (1-u^4)^2` **exact** |
| `Cay(S_3,{c,c^2,(12)})`, `f=(6,9,2)`, `d=2` | S_3 | k = 1 **and** k = 2 | 1,1,2 | **exact** both degrees |
| `Cay(Q_8,{±i,±j})`, `f=(8,16)` | Q_8 | k = 1 | 1,1,1,1,2 | **exact** |

So the `d_rho` exponent and the "all irreps, with multiplicity" statement are right, in a genuinely nonabelian setting with a 2-dimensional irreducible, and in dimension 2 as well as 1. The freeness argument is right: `g·(v_0,...,v_k) = (v_0,...,v_k)` forces `g v_0 = v_0` hence `g = e`, so ordered/pointed states of a Cayley complex carry a free action even though **unpointed simplices need not** — the numerics lane confirms that 24336 of the 97344 triangles of the PGL_3(F_3) complex have an order-3 stabiliser, which is precisely T5.7's caveat. `pi = 1 ⊕ 1` gives `R = 1^{⊕4}` against a single trivial copy in the regular representation — correct. *(exact)*

**VERDICT T5.6: VALID**

## T5.7 — exact Euler-factor bookkeeping on finite-group blocks

**Claim.** `Z_rho = F_rho/det(P_n|C_{0,rho})` with `F_rho = c^{m_{0,rho}} prod_{i>=1} w_{i,rho}^{(-1)^i}` and `prod_rho F_rho^{d_rho} = c^{chi}`; the simple power `c^{d_rho chi/|G|}` requires freeness on **unpointed** simplices; a fractional power must not be asserted.

**What I attacked.** The sub-lemma in <1>4 that `det W_i` is `c` per simplex: `W_i = I + s_i·(weighted cyclic rotation)` on the `i+1` pointings of a simplex, the weight product around the cycle is `u^n` (the `lambda_j` sum to n), so the determinant is `1 - (-s_i)^{i+1}u^n`, and `(-s_i)^{i+1} = (-1)^{(i+1)(i+2)} = 1` since `(i+1)(i+2)` is always even — giving exactly `1 - u^n = c`. **The sign works out; I checked it.** Hence `det W_i = c^{f_i}` and `prod_rho w_{i,rho}^{d_rho} = c^{f_i}` in <1>5.

**Independent support from the numerics lane.** On the PGL_3(F_3) complex, `chi/|G| = 16/3` is not an integer, so freeness on unpointed simplices is impossible, exactly as astra says; and the measured Euler factor on the **trivial** block is `F_triv(u) = (1-u)^{13}(1-u^3)^1`, verified by an exact polynomial identity of degree 55. astra's formula predicts the `c`-exponent to be `m_{0,triv} = dim C_{0,triv} = 1` (one vertex orbit) — and the measured exponent is `c^1`, with the residual `(1-u)^{13}` sitting exactly where `prod_{i>=1} w_{i,rho}^{(-1)^i}` must. That is a nontrivial confirmation of the boxed formula's shape, and a clean refutation of the naive `c^{chi d_rho/|G|}` (which would be `c^{16/3}`). *(byte + third-party exact)*

Status remains conditional on H-KY-LOCAL, whose four address ranges I byte-checked as existing and on-topic (`2607.21262:main.tex:2516-2576, 2586-2640, 2930-2968, 2973-3091`).

**VERDICT T5.7: VALID**

## T5.8 — honest flat coefficients versus arbitrary Kraus coefficients

**Claim.** For an invertible flat local system of rank r, `Z_pt,E = (1-u^n)^{r chi}/det P_{n,E}`; no such assertion for nonflat Kraus weights; adjoint pairing supplies neither flatness nor the cancellation.

**What I attacked.** The <1>4 counterexample: `B_{01} = [[0,1],[1,0]]`, `B_{12} = diag(1,-1)`, `B_{02} = I` on a filled triangle. `B_{12}B_{01} = [[0,1],[-1,0]]`, and `Ad([[0,1],[-1,0]])` is not the identity superoperator (it sends `diag(1,-1)` to `diag(-1,1)`), while `Ad(B_{02}) = id`. So the channel connection is unitary and inverse-paired yet has nonzero curvature. **Correct.** The conclusion drawn — T5.2/T5.3 survive, T5.8's cochain proof does not — is the right scoping. *(exact, by hand)*

**VERDICT T5.8: VALID**

---

# T6. Ramanujan quantum expanders and the twisted RH

## T6.1 — the quantum vertex property with its exceptional space `E_R`

**Claim.** `E_R` = sum of the type-character subrepresentations excluded by the H-LSV convention; it contains `F_R` (the common fixed space) and **can be larger**; replacing `E_R` by `F_R` for all partite complexes is FALSE-as-drafted.

**What I attacked.** See T6.2 <1>6 below, where the separation is exhibited. The definition itself is well-posed. Note that on the LSV example actually in play (`G = PGL_3(F_3)`, simple) there is no nontrivial type character, so `E_R = F_R` there — astra says exactly this in T6.2 part 2, and the numerics confirms "no epimorphism `G -> Z/3`". The correction therefore bites only in the partite case, and astra scopes it correctly.

**VERDICT T6.1: VALID**

## T6.2 — Harrow-type transfer, with correct multiplicities and scope

**Claim.** (1) commuting normal unital trace-preserving channels, `Phi_k^* = Phi_{n-k}`, common fixed space = the commutant, one-dimensional iff `pi` irreducible; (2) Ramanujan relative to `E_R`; (3) `P_{n,R}` has all zeros on `|u| = q^{-(n-1)/2}` off `E_R`; (4) rank-three quotient Artin factors inherit the H-KL radii; (5) no all-rank factor-by-factor RH is available.

**What I attacked.**
- **(1)** The Hilbert–Schmidt identity `(1/|S_k|) sum_s ||R(s)a - a||_2^2 = 2||a||_2^2 - 2 Re<a, Phi_k(a)>` uses `||R(s)a||_2 = ||a||_2` (unitary conjugation is HS-isometric); so `Phi_k(a) = a` forces `R(s)a = a` for **every** `s in S_k`, and generation gives the commutant. Commutant dimension `sum_rho m_rho^2`, which is 1 iff `pi` is irreducible. Correct. Numerically confirmed by the numerics lane on the 12-dimensional irreducible of PGL_3(F_3): `[Phi_1,Phi_2] = 0`, unital, trace-preserving, exactly **one** eigenvalue equal to 1. *(exact + numerical)*
- **(3), the spectral heart.** I verified `<1>4` symbolically for `n = 3, 4, 5`: on a joint eigenvector with `lambda_k = q^{k(n-k)/2} e_k(z)`,
  `sum_{k=0}^n (-1)^k q^{k(k-1)/2} lambda_k u^k = prod_j (1 - q^{(n-1)/2} z_j u)`
  holds identically once `prod_j z_j = 1`, because `k(k-1)/2 + k(n-k)/2 = k(n-1)/2` exactly. So the roots are `q^{-(n-1)/2} z_j^{-1}`, all of modulus `q^{-(n-1)/2}`. At `n = 3` this is `q^{-1}`, exactly Kang–Li's statement (2). **Exact for n = 3,4,5** (`scratch_cz_misc.py`).
- **(<1>6), the `E_R ≠ F_R` separation.** With a nonconstant type character `chi` (`chi(s) = omega^k` on `S_k`) and `pi = 1 ⊕ chi`, the matrix unit `e_{12}` satisfies `R(s)e_{12} = chi(s)^{-1}e_{12}`, so it is **not** a common fixed point when `omega ≠ 1`, yet its `hat A_1`-eigenvalue has modulus `|S_1| = q^2+q+1`, while the tempered bound is `3q`. I checked `q^2+q+1-3q = (q-1)^2 > 0` for `q > 1` symbolically, and `13 > 9` at `q = 3`. So a fixed-point-complement statement really does fail on a partite Ramanujan complex. The phenomenon is sourced: LSV's own "trivial" eigenvectors at `math/0406208:main.tex:1326-1358` are `f_chi(g) = zeta^{val(det g)}` with eigenvalues `zeta^k q^{k(d-k)/2} sigma_k(...)`, i.e. exactly `omega^k |S_k|`, and they are nonconstant. **Correct.** (astra presents this as "Suppose X has a nonconstant type character" — a conditional; such `X` do exist, e.g. `PGL_3(F_q)` with `3 | q-1`, but astra does not exhibit one, which is the honest reading of its status line.)
- **(4), the rank-three radii transfer.** The numerics lane verifies this **exactly** on the genuine 12-dimensional isotypic block of PGL_3(F_3): `|lambda(L_E)| in {1.732051 (×120), 3.0 (×36)} = {q^{1/2}, q}` and `|lambda(L_B)| in {1.0 (×192), 1.316074 (×240), 1.732051 (×192)} = {1, q^{1/4}, q^{1/2}}`, all nonzero, on genuine isotypic blocks. That is astra's part 4 confirmed, in the variable astra insists on. I confirm `1.316074 = 3^{1/4}` to 7 digits. *(third-party exact block spectra; my own arithmetic)*
- **(5)** Correct and important: Kang–Yu at `:2014-2026` supplies a determinant identity and **no** RH; I searched the paper's theorem statements and found none.

**VERDICT T6.2: VALID**

## T6.3 — one faithful representation and the exact converse criterion

**Claim.** `R` satisfies T6.1 iff `B_X ∩ supp(R) = ∅`; `X` vertex-Ramanujan iff `B_X = ∅`; coverage of every nonexceptional irreducible by `pi ⊗ conj pi` is sufficient; **faithfulness alone is not**, with a `Z/28` counterexample.

**What I attacked — the counterexample.** `Cay(Z/28, {±1,±3})`: connected (gcd(1,28)=1), 4-regular, bipartite (all generators odd), **no triangles** (odd+odd is even, and `S` contains only odd elements) so the clique complex is 1-dimensional — I verified all four. The character `g -> e^{2 pi i g/28}` has adjacency eigenvalue `2cos(pi/14)+2cos(3pi/14) = 3.51351878930`, against the Ramanujan bound `2 sqrt 3 = 3.46410161514`; it exceeds it, and is neither `±4`. So the graph is not Ramanujan. With `pi` that faithful character, `pi ⊗ conj pi = 1`, `M_1 = C`, and the fixed-point complement is zero, so the quantum condition is vacuous. **Counterexample confirmed exactly.** astra's rationality-preserving bound also checks out: `cos x >= 1 - x^2/2` and `pi^2 < 10` give the eigenvalue `> 4 - 5 pi^2/98 > 171/49`, and `(171/49)^2 = 12.1787 > 12 = (2 sqrt 3)^2`. Both the decimal and the rigorous route hold. *(exact)*

**VERDICT T6.3: VALID**

## T6.4 — one-sided RH in the correct variable

**Claim.** For `u = b^{-s}`, `|lambda| = b^{Re s}`, so peripheral `|lambda| = b` means `Re s = 1` and `|lambda| <= sqrt b` means `Re s <= 1/2`; `|s| = 1` as printed in the source is **not** a well-defined invariant (Im s is only defined mod `2 pi / log b`); under H-KAMBER actual nontrivial `u`-poles satisfy `|u| >= q^{-(p-1)/p}` — a **lower** bound on pole radii, the inverse of the source's upper eigenvalue bound.

**What I attacked.** The variable conversion is elementary and right, and the criticism of `|s| = 1` is correct: `b^{-s}` is `2 pi i/log b`-periodic in `s`, so `|s|` is not an invariant of the pole while `Re s` is. The source does literally print `|s|=1` — at `1702.05452:rw_ramanujan_complex.tex:404`, `:415` and `:1419` ("either `|s|=1` or `Re(s) <= 1/2`"). The Kamber inversion is right: `1 - theta u^l = 0` gives `|u| = |theta|^{-1/l} >= q^{-(p-1)/p}` from `|theta| <= q^{l(p-1)/p}`, so the source's Corollary at `:359-363` — which reads verbatim "every **pole** `lambda` of `zeta` satisfies `|lambda| <= q^{(p-1)/p}` or `|lambda| = q`" — is calling an *eigenvalue* a pole, and any downstream reading of it as a bound on `|u|` would be wrong. astra spots this and refuses the ambiguous wording in favour of the eigenvalue theorem at `:345-350`. Correct.

**MINOR.** astra writes "Interior cases `0 < Re s < 1/2` occur by H-LLP". The source's existence statement (`1702.05452:...:1421-1423`) is
`The bound |Re(s)| <= 1/2 is the true situation: there are poles with |Re(s)| < 1/2 ... and in higher dimension there are also poles with 0 < |Re(s)| < 1/2`
— an **absolute value**, i.e. the sourced assertion is `0 < |Re s| < 1/2`, which does not by itself place a pole in the positive half of that band. **Fix:** state H-LLP's existence clause and T6.4's third sentence as `0 < |Re s| < 1/2`, or cite the rank-three mechanism of T3.5 (type-(e) chamber roots at `Re s = 1/2, 1/4` with `b = q`) as the source of the positive-side interior cases — which astra already does in <1>3, so the fix is a one-word edit, not a structural change.

**VERDICT T6.4: MINOR**

## T6.5 — which rank-three factors have a duality

**Claim.** `p_a(u) = 1 - au + q conj(a) u^2 - q^3 u^3` satisfies `p_a(u) = -q^3u^3 conj(p_a(1/(q^2 conj u)))`; the zero multiset is invariant under `u -> q^{-2}/conj u`, fixed circle `|u| = q^{-1}`; principal-series edge and chamber factors inherit dualities at `q^{-2}` and `q^{-1}`; the **full** edge and chamber factors have none, and the type-(e) chamber block alone cannot have any `u -> c/u` or `u -> c/conj u` symmetry.

**What I attacked.** I expanded the involution by hand and symbolically: `conj(p_a(1/(q^2 conj u))) = 1 - conj(a)/(q^2 u) + a/(q^3u^2) - 1/(q^3u^3)`, and multiplying by `-q^3u^3` returns `1 - au + q conj(a) u^2 - q^3u^3` term by term. **Exact.** The fixed circle `|u| = q^{-2}/|u|` gives `|u| = q^{-1}`. I also verified <1>2 independently: for a principal-series constituent, `a = q e_1(alpha)` and `|alpha_i| = 1, prod alpha_i = 1` force `e_2 = conj(e_1)`, so `prod_i(1-q alpha_i u) = 1 - au + q conj(a) u^2 - q^3u^3 = p_a(u)` **identically** — the edge polynomial really is `p_a`, and the chamber polynomial `p_a(u^2)` has exactly the six roots `±q^{-1/2}alpha_i^{-1/2}` of H-KL-TABLE row (a). The type-(e) obstruction in <1>4 is airtight: one root at radius `q^{-1/2}`, two at `q^{-1/4}`; fixing both radii needs `c = q^{-1}` and `c = q^{-1/2}` at once (impossible for `q>1`), and exchanging them needs multiplicities `1 = 2`. The Hilbert–Polya caveat in <1>3 (repeated roots, nonsemisimple companion matrices, branch choices for logarithms) is a real and correctly stated limitation. *(exact)*

**VERDICT T6.5: VALID**

## T6.6 — Weil positivity here is a bound until a duality is supplied

**Claim.** `nu_m = sum (mu_j/r)^m`, `nu_{-m} = conj(nu_m)` is positive definite on Z **exactly when** all `|mu_j| <= r`; with the extra involution `mu -> r^2/conj mu` the bound forces `|mu| = r`; this applies to each retained ordinary block, not to an alternating sum.

**What I attacked.** Sufficiency: the Poisson kernel `(1-|z|^2)/|e^{it}-z|^2` has `m`-th Fourier coefficient `z^m` for `m >= 0` (and `conj(z)^{|m|}` for `m<0`), so each eigenvalue in the closed disc contributes the moment sequence of a positive measure and finite sums stay positive definite; `z = 0` and `|z| = 1` (point mass) are covered. Necessity: astra's Cesàro argument is correct — with `R > 1` the maximal normalised modulus, `nu_m = R^m sum_j b_j e^{i m theta_j} + o(R^m)` and `(1/M) sum_{m<=M} |sum_j b_j e^{im theta_j}|^2 -> sum_j b_j^2 > 0` by orthogonality of distinct phases, so `|nu_m|` is unbounded, contradicting `|nu_m| <= nu_0` from the 2×2 minors. I tested the criterion numerically on a 41×41 Toeplitz form: eigenvalues `{0.9e^{0.3i}, 0.5, -0.7, 1.0}` with `r = 1` give minimum eigenvalue `+1.0118`; moving one to `1.3e^{0.3i}` gives `-8.84e4`. The "blind to Jordan blocks" remark is right and is exactly why positivity does not construct a Hilbert–Polya inner product. *(exact by hand; numerical confirmation)*

**VERDICT T6.6: VALID**

## T6.7 — using a type cover without assuming one was present

**Claim.** For a torsion-free cocompact `Gamma` with descended cyclic type-difference data but **not** necessarily type-preserving, the pointed identity descends from the type-preserving cover; rank-three RH conclusions apply if the quotient is vertex-Ramanujan.

**What I attacked.** The mechanism (`H ⊂ Z/n` deck group, characters of `H` extend to characters of `Z/n` hence to unitary characters of `G` through `tau`, which are trivial on vertex and Iwahori stabilisers and preserve temperedness because they have modulus one) is sound, and `c^{chi(X_0)/|H|} = c^{chi(X)}` because `chi` is multiplicative in a free finite cover. **This is exactly the situation the numerics lane is in**, and it is independently confirmed there: the output states "Kang–Li hypothesis (I) ... **FAILS here**, because `r = 1`" yet the cleared identity `det(cubic) det(I+L_Bu) = (1-u^3)^chi det det` **holds to order `u^18`** on the 5616-vertex base and **also** on the type-preserving 16848-vertex cover, with fitted exponents `a = 0, c = chi` in both cases. T6.7 is the theorem that explains why. *(third-party numerical, order 18; H-COVER byte-checked)*

**VERDICT T6.7: VALID**

---

# T7. Verdict and numerical targets

## T7.1 — the recommended object

**Claim.** The graded geodesic determinant of a complex with **specified geodesic data** (state sets, successor relation with multiplicities, algebraic lengths, transports), parity `k+1`, with the ordered default for an abstract complex and pointed/opposition data for a building; not an unqualified "the Ihara zeta of every complex"; naturality only under isomorphisms preserving the specified data; uniqueness not claimed.

**What I attacked.** The box is internally consistent with T3.1 (parity `k+1`, sign `(-1)^{k+1}`, exponent `(-1)^k`), reduces to Hashimoto at `d = 1` with only an even sector, and reduces to Kang–Yu's completed vertex product on a building. The status line correctly says the building identification is conditional and that uniqueness among choices of higher-dimensional geodesics is **not** proved — which, given the brief's framing ("the zeta that wants to exist"), is the honest answer and the one the notebook needs. The closing prose is appropriately blunt: a vertex-level Bass identity is a building phenomenon, the general complex has the forbidden-transition Schur complement, and "fermionic zeros" describes net odd multiplicity **after cancellation**. That last caveat is the one T3.3 forces, and astra applies it against its own headline.

**VERDICT T7.1: VALID**

## T7.2 — three smallest useful exact tests

**Claim.** The table (C_3, filled triangle, `∂Delta^3`), the Schur factors of the filled triangle, and the octahedron as an optional fourth test.

**What I attacked — recomputed every entry from scratch, exactly:**

| complex | f, chi | `det(I - s_1 u T_1)` mine | astra | `det(I - s_2 u T_2)` mine | astra |
|---|---|---|---|---|---|
| C_3 graph | (3,3), 0 | `(1-u^3)^2`, deg 6 | `(1-u^3)^2`, deg 6 | absent | absent |
| filled triangle | (3,3,1), 1 | `1` (`T_1 = 0`) | `1`, deg 0 | `1` (`T_2 = 0`) | `1`, deg 0 |
| `∂Delta^3` | (4,6,4), 2 | `1` (`T_1 = 0`) | `1`, deg 0 | `(1-u^4)^6`, deg 24 | `(1-u^4)^6`, deg 24 |
| octahedron | (6,12,8), 2 | `(1-u^4)^6`, deg 24 | `(1-u^4)^6` | `(1-u^6)^8`, deg 48 | `(1-u^6)^8` |

Every entry matches. The filled-triangle Schur factors of <1>1 also match to the letter: `det K_1(u) = (u-1)^2(2u+1) = (1+2u)(1-u)^2` and `det K_2(-u) = (u-1)^2(u^2+u+1)^2 = (1-u^3)^2`, with `det M` their reciprocals — so the row really does exercise cancellation at the singular points of `K`. <1>2's warning is confirmed: the clique complex of `K_4` is the **filled** `Delta^3`, a 3-dimensional complex on which I find `T_1 = T_2 = T_3 = 0` and `Z_ord = 1`, a genuinely different object from `∂Delta^3`. <1>3's octahedron arithmetic is right: after cancellation `gcd((1-u^6)^8,(1-u^4)^6) = (1-u^2)^6`, leaving numerator `(1-u^2)^2(1+u^2+u^4)^8` of degree **36** and denominator `(1+u^2)^6` of degree **12**, exactly as claimed; and `(1-u^3)^2(1-u^4)^6/(1-u^6)^8` has a pole of order 2 at `u = -1`. *(exact)*

**VERDICT T7.2: VALID**

## T7.3 — predictions and limits for the PGL_3(F_3) numerical lane

**Claim.** `|G| = 5616`, `f_1 = 73008`, `f_2 = 97344`, `chi = 29952`; pointed edge space 146016, colour blocks 73008 with outdegree 9; pointed chambers 292032 with outdegree 3; all-ordered chambers 584064; all-ordered edge outdegree **21, not 9**; degrees 16848 / 219024 / 292032 and 308880 on each side. Plus two read-only observations about `outputs/a2_complex_zeta.txt`: <1>2 that a link diagnostic prints `False`, and <1>3 that a predicted chamber radius `3^{3/4}` is wrong.

**What I attacked.**

*The counts and degrees — all correct.* `|PGL_3(F_3)| = (27-1)(27-3)(27-9)/2 = 5616`; `f_1 = 26·5616/2 = 73008`; the PG(2,3) incidence graph has `13·4/2 = 52` edges so `f_2 = 52·5616/3 = 97344`; `chi = 5616 - 73008 + 97344 = 29952`. Degrees: `3f_0 = 16848`, `f_1 + 2f_1 = 219024`, `3f_2 = 292032`, and `16848 + 292032 = 3·29952 + 219024 = 308880` on both sides. The outdegrees 21 and 9 are exactly what my independent PG(2,3) construction gives (table under T0.3). Every number checks. *(exact)*

*Adjudication of flagged issue 2 — the chamber radius. astra is RIGHT.* Kang–Li's statement (4) puts the nontrivial zeros of `det(I+L_Bu)` on `|u| in {1, q^{-1/2}, q^{-1/4}}`, and `u = -1/lambda`, so the **eigenvalue** radii are `{1, q^{1/2}, q^{1/4}} = {1, 1.732051, 1.316074}` — `q^{3/4} = 2.2795` is not the reciprocal of any of them. The prediction `q^{3/4}` is still present in the current script (`scripts/a2_complex_zeta.py:710`) and in the current output ("its spectrum sits on circles of radius 1, `q^{1/2}` and `q^{3/4}`"), while the same file's own exact block spectra in STEP 5c report `|lambda(L_B)| in {1.0, 1.316074, 1.732051}` and its reference line lists `q^{1/4} = 1.316074`. So the `q^{3/4}` is a stale leftover, the observed `1.316074` is `3^{1/4}` to 7 digits, and astra's correction stands. (Likely provenance: the source's type-(d) row at `0809.1401v1:main.tex:1152` does contain `±q^{3/4}chi^{-1/2}(pi)` — but that is a **root** radius of a non-tempered constituent, absent on a Ramanujan quotient.) **astra's adjudication confirmed.**

*Adjudication of flagged issue 1 — the link diagnostic.* **MINOR against astra.** In the current 330-line `outputs/a2_complex_zeta.txt`, lines 17–20 read
```
17  global 3-colouring of the Cayley graph consistent: False  (False is expected: ...)
18  link of a vertex: 26 vertices, degrees [4], bipartite True, girth 6
19    any two 'points' lie on exactly one common 'line': True ; each point is on q+1 = 4 lines
20    => the point-line incidence graph of PG(2,3) (the unique (4,6)-cage).
```
The uniqueness diagnostic on line 19 reads **True**, not `False`; the only `False` in that neighbourhood is the 3-colouring on line 17, which is a different and expected fact. The output was being regenerated while I worked (it was 36 lines at 10:59 and 330 lines at 11:00; astra's file is timestamped 10:56), so I cannot audit the version astra read and I do not call this a fabrication. But as a statement about the artifact it is now false, and **the inference astra draws from it is unnecessary in any case**: the same diagnostic reports 26 vertices, 4-regular, bipartite, girth 6, and the `(4,6)`-cage on 26 vertices is **unique** — it is the point-line incidence graph of PG(2,3). So the identification is forced by cage uniqueness regardless of the uniqueness-of-line test, and my own independent PG(2,3) construction reproduces every number the output uses.
**Fix:** replace T7.3 <1>2's sentence "Its link diagnostic says that uniqueness of a line through two points is `False` ... that contradiction is not accepted as a certified projective-plane test here" with: "The link diagnostic reports 26 vertices, 4-regular, bipartite, girth 6 and a unique line through any two points; the first four already force the unique `(4,6)`-cage, i.e. the incidence graph of PG(2,3), so the identification is certified." Nothing downstream changes — T7.3's counts and the T0.3 outdegrees do not depend on this remark.

*The T5.7 remark in <1>3 is correct and now independently verified:* `chi/|G| = 16/3` is nonintegral, freeness on unpointed simplices fails (24336 of 97344 triangles have an order-3 stabiliser), and the measured trivial-block Euler factor is `(1-u)^{13}(1-u^3)^1`, not any power of `1-u^3`. See T5.7.

**VERDICT T7.3: MINOR**

---

# T8. Ledger, register, result

## T8.1 — append-only qualification of an overbroad sentence in T4

**Claim.** T4.2 <1>3's phrase "even allowing ... a polynomial vertex factor" is too strong if that factor is arbitrary; the surviving obstruction is to an **Euler-factor-only** adjustment and to the prescribed building-shaped vertex identity of T2.4.

**What I attacked.** The self-correction is right in both directions: `p(u) = (1-u^4)^6` makes `p(u) Z_ord^{-1} = 1` on `∂Delta^3`, so no theorem excluding *every* polynomial multiplier was proved; and `(1-u^3)^a` is nonzero at `u = i` for every integer `a`, so the Euler-factor-only obstruction genuinely survives. I verified both facts against my exact `Z_ord = (1-u^4)^6`. Self-flagging an overbroad sentence of one's own is exactly the behaviour the ledger is for. *(exact)*

**VERDICT T8.1: VALID**

## T8.2 — the correction ledger

**Claim.** 34 rows of drafted-or-tempting claims with corrections and locations; each false algebraic assertion has an explicit calculation, matrix proof or counterexample.

**What I attacked — this was my highest-value target, since a wrong correction is worse than a wrong claim.** I went through every row and asked whether the drafted claim is *really* false and whether the replacement is *really* true. Summary of the ones with mathematical content:

| ledger row | is the drafted claim really false? | is the correction right? | how I checked |
|---|---|---|---|
| unrestricted flow = LLP flow | yes (LLP restricts colours) | yes | byte `1702.05452:999-1027`; outdegree 21 vs 9 |
| ordered flow = `k!` Kang–Yu copies | yes | yes | exact, PG(2,q) outdegrees for q=2,3,5 |
| raw colour classes are invariant `L_E, L_E^t` blocks | yes | yes, **and sharper**: the colour-preserving part *is* `L_E` | exact |
| reversed-edge `u^2` is a multiplicity/square | yes | yes, it is `l_A = lambda_0 = 2` | byte `2607.21262:439-474` |
| all `3!` chamber orders give `L_B` once | yes | yes, two blocks, `D_B^2` | exact (octahedron), third-party (m<=18) |
| total graded zeta = Kang–Li's edge zeta | yes | yes, `D_B/D_E` | byte `0809.1401v1:1410-1418` |
| Kang–Yu's cochain product has exponent `chi` | yes | yes, `chi_pt` | byte `2607.21262:2459-2487` |
| ordered-cochain torsion gives `chi` | yes (`Delta^1`: 1 vs 0) | yes | exact arithmetic |
| Knill's SDet is the `u->1` limit | yes | yes (1, 2, 0 on one edge) | exact |
| universal cubic vertex Bass for every 2-complex | yes | yes, pole at `u=-1` | exact, `∂Delta^3` |
| building cubic has `-(A_1+A_2)u` | yes | yes, `-A_1 u` | byte `0809.1401v1:219` |
| generalized-polygon links characterise collapse | no theorem either way | correctly labelled unestablished | — |
| odd eigenvalues are exactly the zeros | yes | yes, reciprocals, net multiplicity | exact |
| chamber roots are uncancelled zeros of `L_vertex` | yes | yes, `1/det P_3` | byte + degree audit + third-party exact |
| `k`-cells realise `H^{k-1}` with weight `k-1` | yes | yes (C_3; three chamber radii) | exact + byte table |
| the weight-1 circle contains the whole odd sector | yes | yes, three circles with the stated sources | byte, all four rows |
| order at `u^n=1` is always an Euler characteristic | yes | yes, `chi - ord det P_n`; 6 vs 2 on `∂Delta^3` | exact |
| one fermion determinant gives the supertrace | yes | yes, Berezinian with auxiliary copies | exact |
| no polynomial multiplier could clear the total | yes (astra's own row) | yes, T8.1 | exact |
| building Laplacian is `(d+delta)^2` | yes | yes, `delta^2 ≠ 0` | byte `2607.21262:2377-2378` |
| adjoint pairing needed for Kraus positivity | yes | yes, CP suffices | exact |
| positivity alone excludes a numerator | yes | yes, `(1-u)/(1-2u)` | exact; consistent with `thm:no-ungraded-trace` |
| arbitrary Kraus weights preserve the Euler/Hecke formula | yes | yes, flatness needed for the cochain proof | exact (unitary inverse-paired curvature example) |
| `E_{(g,gs)} = R(s)` is flat | yes | yes | exact: 192/192 ordered 2-cells fail on `Cay(Q_8,{±i,±j,±k})` |
| full-cover connection = a quotient block | yes | yes, `C_4`: `(1-u^4)^2` vs `(1-u)^2` | exact |
| `R` embeds in one regular representation | yes | yes, exponents `d_rho` vs `a_rho` | exact, three Cayley complexes |
| Euler factor is trivial-only or `c^{chi N^2/|G|}` | yes | yes, local-rotation product | third-party exact: `(1-u)^{13}(1-u^3)` vs `c^{16/3}` |
| scalar equality restricts to every irreducible | yes | yes | byte `0809.1401v1:1425-1461` |
| removing fixed points removes all trivial modes | yes | yes, `|S_1| > 3q` for `q>1` | exact |
| every nontrivial finite irrep "is tempered" | yes | yes, support transfer only | byte `math/0406208:1326-1358` |
| one faithful `pi` detects Ramanujan | yes | yes, `Z/28` | exact |
| all-rank Kang–Yu gives factor-by-factor RH | yes | yes, no RH in that paper | byte |
| LLP's condition is an invariant `|s|=1` | yes | yes, `Re s = 1` | byte `:404,:415,:1419` |
| Kamber bounds actual `u`-poles from above | yes | yes, it inverts | byte `:345-350` vs `:359-363` |
| higher-dim RH automatically has a duality | yes | yes, type-(e) multiplicities 1 vs 2 | exact |
| a non-type-preserving quotient satisfies the quoted theorem | yes | yes, T6.7 descent | third-party numerical (order 18, base and cover) |
| numerical chamber radius is `q^{3/4}` | yes | yes, `q^{1/4}`, observed `1.316074` | exact + third-party block spectra |
| a "not found" search proves nonexistence | yes | yes | — |

**I could not find a single wrong correction.** Two rows are, if anything, understated (the colour-class row and the positivity row, noted above). *(exact / byte as tabulated)*

**VERDICT T8.2: VALID**

## T8.3 — the complete H-hypothesis register

**Claim.** Thirteen hypotheses with citation addresses; a citation asserts only the recorded statement and scope.

**What I attacked — I byte-checked every address in the register.** All thirteen files exist under `refs/src/`. Forty-odd of the ranges reproduce their claimed content to the line, including **every** address in H-POINT, H-KY, H-KL, H-KL-TABLE, H-TORS, H-RUELLE, H-MO, H-KAMBER and H-STRONG. Three address blocks are imprecise:

1. **H-LSV, `math/0406208:main.tex:541-572`.** These lines contain the Hecke operators, the remark that the tempered set "was computed explicitly", and the Ramanujan definition — but **not** the displayed set `Aspec_n`. The formula is at **`:1437-1441`**: `Let S = {(z_1,...,z_d) : |z_i|=1, z_1...z_d = 1}` and `lam_k = q^{k(d-k)/2} s_k(z_1,...,z_d)`, with `Aspec_d = sigma(S)` at `:1470`. **The exponent `q^{k(n-k)/2}` and the elementary symmetric function are correct character for character** — only the address is off by ~890 lines. The register's own block already includes `:1436-1478`, which contains the formula, so nothing is unsupported; but `:541-572` should not be the address quoted for it. (The imprecision is inherited from the brief, which cites `math/0406208 lines 553-572`.)
2. **H-LSV, `math/0406217:main.tex:497-515` and `:676-682`.** The claimed per-colour statement `|S_k| = [n choose k]_q` with `S_{n-k} = S_k^{-1}` is **not** at either address; `:497-515` gives the Ramanujan Cayley clique complex of `PGL_d(F_{q^e})` and a total generator count, and `:676-682` gives only the colour-shift Hecke operators. The statement is at **`:2617-2626`**: "let `S_k` denote the set of products `b_{u_1}...b_{u_k}` ... There will be `[d k]_q` different products ... and `S_{d-k}` is the set of inverses of `S_k`." **Fix:** add `:2617-2626` to the H-LSV block.
3. **H-LLP, `1702.05452:...:330-336` and `:410-416`.** These are correct *lines of the paper* but are attached to the wrong clauses: `:330-336` is the **definition** of a Ramanujan digraph ("every eigenvalue `lambda` ... satisfies either `|lambda| <= sqrt k` or `|lambda| = k`"), i.e. it supports the eigenvalue clause, while `:410-416` is the **RH corollary** ("if `Z` has a pole at `k^{-s}` then `|s|=1` or `Re(s) <= 1/2`"). The "equivariant, collision-free, `b`-regular branching operator" notion astra attributes to them is defined at **`:216`** and **`:229`**, and packaged at `:358-363`; and the *proved* eigenvalue bound (as opposed to the definition) is at `:487` and `:922-923`. **Fix:** add `:216`, `:229` and `:487` to the H-LLP block and drop the implication that `:330-336` is a theorem rather than a definition.

A fourth, benign: **H-COVER** cites `1702.05452:...:196-214` for "contractibility, torsion-free free action, type character". Those lines give the contractible complex and the torsion-free cocompact lattice but not the free action or the type character; the type character in that paper is at `:983` (`col(gK) ≡ ord_pi(det g) mod m`). However H-COVER's block **also** cites `2607.21262:1724-1738` (contractibility + free action, verbatim), `2607.21262:2014-2019` (`Gamma ⊂ ker(G_ad -> Xi_ad ≃ Z/nZ)`, verbatim) and `math/0406208:1334-1358` (the character `zeta^{val(det g)}`), so the block is collectively sufficient and I do not count it separately.

**No proof in the note depends on a claim that is unsupported by the sources**; in each of the three cases the correct lines exist in the same file and, in two of the three, inside the same cited block. That is why this is MINOR and not INVALID.

**VERDICT T8.3: MINOR**

---

# The three most consequential findings

**1. The definitional core of the note — T0.3, T2.2, T2.4 and T7.2 — survives an exact independent reconstruction with no discrepancy anywhere.** The A~_2 outdegrees `2q^2+q` vs `q^2` reproduce for q = 2, 3, 5 from an independently built PG(2,q) incidence graph (10/4, 21/9, 55/25); the tetrahedron-boundary flow is `T_1 = 0`, `det(I+uT_2) = (1-u^4)^6`; the octahedron is `(1-u^4)^6` and `(1-u^6)^8` with reduced degrees 36/12; the filled-triangle Schur factors are `(1+2u)(1-u)^2` and `(1-u^3)^2`; and the universal Bass–Schur identity T2.2 together with the block identity T4.1 holds **exactly on all thirteen complexes tested, including seven random 2- and 3-complexes on 5–7 vertices**, up to `dim H_2 = 102`. Scripts: `notes/reviews/scratch_cz_flow.py`, `notes/reviews/scratch_cz_link.py`. This is the part of the note the lab book should take as settled.

**2. The correction ledger T8.2 is sound in all 34 rows, and two corrections are stronger than stated.** (a) T0.3's "the raw colour classes are not invariant blocks" can be sharpened: of the `2q^2+q` unrestricted successors of a colour-1 directed edge, **exactly `q^2` preserve the colour and they are precisely `L_E`**, while the `q^2+q` same-part successors are the entire discrepancy — verified exactly for q = 2, 3, 5. (b) T5.4's `(1-u)/(1-2u)` is not in tension with the notebook's registered no-go `thm:no-ungraded-trace` in `report/sections/04b_phantasm_forced.tex`: that theorem's proof is a residue-sign argument that **never uses positivity**, and astra's example is an *instance* of it (`N_m = 2^m - 1^m`), so the prover's reading — that the operative hypothesis is "is an honest trace", not "is positive" — is a correct sharpening of the brief's wording, not a contradiction of a registered claim. Scripts: `notes/reviews/scratch_cz_link.py`, `notes/reviews/scratch_cz_misc.py`.

**3. Of the two issues astra flagged in the numerics output, one is right and one is now wrong — and the register has three bad addresses.** The chamber-radius correction is **right**: `q^{3/4}` is still printed at `scripts/a2_complex_zeta.py:710`, but `u = -1/lambda` and Kang–Li's `|u| = q^{-1/4}` give eigenvalue radius `q^{1/4} = 1.3160740`, which is exactly what the same file's own exact block spectra report (`{1.0, 1.316074, 1.732051}` on both the trivial and the 12-dimensional isotypic blocks); the stale `q^{3/4}` probably comes from the source's **type-(d)** row, a non-tempered constituent absent on a Ramanujan quotient. The link-diagnostic claim is **wrong against the current file**, which prints `True` on that line (the nearby `False` is the expected 3-colouring failure) — and the caution was unnecessary anyway, since 26 vertices + 4-regular + bipartite + girth 6 already force the unique `(4,6)`-cage. Separately, three H-* address blocks in T8.3 quote content that lives elsewhere in the same file: `Aspec_n` is at `math/0406208:1437-1441` (not `:541-572`), the coloured generator sets `|S_k| = [n k]_q` with `S_{n-k} = S_k^{-1}` are at `math/0406217:2617-2626` (not `:497-515` or `:676-682`), and LLP's branching-operator definition is at `1702.05452:216,:229` while `:330-336` is the Ramanujan-digraph *definition* and `:410-416` the RH corollary. All three are fixable by adding line numbers; none leaves a proof unsupported.

---

## Verdict list

VALID (44): T0.1, T0.2, T0.3, T0.4, T0.5, T1.1, T1.2, T1.3, T1.4, T2.1, T2.2, T2.3, T2.4, T2.5, T3.1, T3.2, T3.3, T3.4, T3.5, T3.6, T3.7, T4.1, T4.2, T4.3, T4.4, T4.5, T5.1, T5.2, T5.3, T5.4, T5.5, T5.6, T5.7, T5.8, T6.1, T6.2, T6.3, T6.5, T6.6, T6.7, T7.1, T7.2, T8.1, T8.2

MINOR (3): T6.4 (`0 < |Re s| < 1/2`, not `0 < Re s < 1/2`), T7.3 (<1>2's report of the link diagnostic; the identification is forced by cage uniqueness), T8.3 (three address blocks quote content located elsewhere in the same file)

INVALID (0)

## Scratch scripts

- `notes/reviews/scratch_cz_flow.py` — T0.1, T2.1/T2.2, T2.3, T2.4, T4.1, T7.2 (exact; Bareiss over Z plus exact polynomial evaluation at `deg+1` integers)
- `notes/reviews/scratch_cz_link.py` — T0.3 (PG(2,q) incidence graphs for q = 2,3,5; orientation blocks of `T_2`; colour behaviour of `T_1`) (exact)
- `notes/reviews/scratch_cz_cayley.py` — T5.5, T5.6 on `Z/4`, `Cay(S_3,{c,c^2,(12)})` (k = 1,2), `Cay(Q_8,{±i,±j})`; addendum on `Cay(Q_8,{±i,±j,±k})` (exact, plus one numerical eigenvalue-multiset comparison)
- `notes/reviews/scratch_cz_misc.py` — T3.1 sign law, T5.4, T6.2 `<1>4`/`<1>6`, T6.3, T6.5, T6.6, T1.2/T1.4 arithmetic (exact, plus one numerical Toeplitz test)

Checks labelled *exact* are over Z or Q with no floating point. Checks labelled *numerical* are float linear algebra with the tolerance stated. Checks labelled *third-party* are read from `outputs/a2_complex_zeta.txt`, which was being regenerated during this review (36 lines at 10:59, 330 lines at 11:00); the version I read is snapshotted outside the repository.

**Not checked:** the PGL_3(F_3) complex was not rebuilt from the LSV generators (all of T0.3's content is local to the vertex link, which was rebuilt); H-KY's technical proof of `thm:Phi-determinants` and H-KY-LOCAL's factorisation `Phi_i = c W_i^{-1} J_i (I - s_i Sigma_i) J_i^{-1} Q_i^{-1}` were confirmed to exist at the cited addresses but not verified line by line; T5.7's global identity `prod_rho F_rho^{d_rho} = c^{chi}` was confirmed only on the two isotypic blocks the numerics lane can build; T6.7's descent was checked only through order `u^18` (third-party).

---

# Round 2 — re-verdicts on the three MINOR findings

- **Date:** 2026-09-13 (second pass)
- **Reviewer:** claude:opus (REFUTE lane)
- **Trigger:** the coordinator reports that the three MINOR fixes have been applied to `notes/complex-zeta/astra-proofs.md`.
- **Method:** I re-read the edited passages with `sed -n` / `grep -n` on the current file, and **byte-checked every newly added citation address against `refs/src/` myself** rather than taking the change description on trust. No new scratch scripts were needed; the Round 1 mathematics is untouched by these edits.

**Round 2 headline: 3/3 MINOR findings resolved. 0 INVALID, 0 MINOR remaining. Final tally 47 VALID, 0 MINOR, 0 INVALID.**

## T6.4 (Round 1: MINOR — `0 < Re s < 1/2` versus the source's `0 < |Re s| < 1/2`)

**What changed.** `astra-proofs.md:909` now reads:

> Interior cases $0<|\operatorname{Re}s|<1/2$ occur by H-LLP (the source's existence clause carries an absolute value); the positive-side interior cases in rank three are supplied by the type-(e) chamber roots of T3.5 at $\operatorname{Re}s=1/2,1/4$ with $b=q$. [Wording corrected after review, 2026-09-13.]

and H-LLP (line 64) now reads "Interior spectral radii do occur (poles with $0<|\operatorname{Re}s|<1/2$)".

**What I checked.** The absolute value is now carried in **both** places — the hypothesis and the proposition that invokes it — so the sourced clause and the note now agree. `1702.05452:rw_ramanujan_complex.tex:1421-1423` reads "there are poles with $|\Re(s)|<\frac12$ ... and in higher dimension there are also poles with $0<|\Re(s)|<\frac12$", which is exactly what is now asserted. The second half of the new sentence is the right repair for the positive side: it no longer claims positive-side interior poles *from LLP*, but derives them from T3.5's type-(e) chamber roots, whose radii I verified byte-for-byte against `0809.1401v1:main.tex:1152` in Round 1 ($q^{-1/2}$ and $q^{-1/4}$, i.e. $\operatorname{Re}s = 1/2$ and $1/4$ at $b=q$, both strictly positive and both $\le 1/2$). That is a *stronger* statement than before and it is sourced. Nothing else in T6.4 moved: the variable conversion $|\lambda| = b^{\operatorname{Re}s}$, the rejection of the literal $|s|=1$, and the Kamber inversion $|u| \ge q^{-(p-1)/p}$ all stand as verified in Round 1.

**Newly cited H-LLP addresses, byte-checked by me just now** (`refs/src/1702.05452/rw_ramanujan_complex.tex`):

| address | what it actually says | role astra assigns | verdict |
|---|---|---|---|
| `:216` | "A *$k$-branching* operator $T$ ... identify $T$ with the adjacency matrix of $\cY_{T,\fC}$, the $k$-out-regular digraph ... When $\cY_{T,\fC}$ is also $k$-in-regular, we say that $T$ is a *$k$-regular branching* operator ... $T$ that is $G$-equivariant" | branching operators | **supports** |
| `:229` | "Call a $k$-branching operator $T$ *collision-free* if its associated digraph ... has at most one (directed) path from $x$ to $y$" | branching operators | **supports** |
| `:330-336` | the *definition* of a Ramanujan digraph: "every eigenvalue $\lambda$ ... satisfies either $|\lambda|\le\sqrt k$ or $|\lambda|=k$" | labelled "(definition of a Ramanujan digraph)" | **supports, correctly labelled** |
| `:410-416` | the RH corollary: "if $Z$ has a pole at $k^{-s}$ then $|s|=1$ or $\Re(s)\le\frac12$" | labelled "(the RH corollary)" | **supports, correctly labelled** |
| `:487` | Prop.: "Let $\cY=\cY_T$ for a $k$-branching collision-free operator $T$. Then every $\lambda\in\Pspec_{2^+}(A_{\cY})$ satisfies $|\lambda|\le\sqrt k$." | labelled "(the proved eigenvalue bound)" | **supports** |
| `:922-923` | "$|\lambda|\le\sqrt k$ by Proposition~\ref{prop:collision-free-riemann}. The trivial eigenvalues all have modulus $k$ ... thus $\cY_{T,\fX}$ is Ramanujan." | proved eigenvalue bound (peripheral half) | **supports** |

The previous confusion — attributing the branching-operator notion to `:330-336`/`:410-416` and presenting a definition as a theorem — is gone: definition, corollary and proved bound now have distinct, correct, labelled addresses. My Round 1 fix was a one-word edit; what was applied is that plus a genuine strengthening.

**VERDICT T6.4: VALID**

## T7.3 (Round 1: MINOR — the misreported link diagnostic)

**What changed.** `astra-proofs.md:1051` now reads:

> The link diagnostic reports 26 vertices, 4-regular, bipartite, girth 6 and a unique line through any two points; the first four already force the unique $(4,6)$-cage, the incidence graph of $\mathrm{PG}(2,3)$, so the identification is certified. [Sentence corrected after review, 2026-09-13: the version read during the append reported the diagnostic wrongly.]

**What I checked.** The sentence now matches the artifact and the mathematics, and — better than my suggested wording — it carries an explicit note that the earlier version of the output was misread, which is the honest provenance record. The substance is correct: 26 vertices, 4-regular, bipartite, girth 6 uniquely determine the $(4,6)$-cage, which is the point-line incidence graph of $\mathrm{PG}(2,3)$, so the identification does not depend on the uniqueness-of-line test at all. My independent PG(2,3) reconstruction in `notes/reviews/scratch_cz_link.py` reproduces $N=13$, 26 link vertices, degree 4, unique line through two points, and the outdegrees 21 and 9 that T7.3 actually uses, so nothing downstream was ever at risk.

**The companion `q^{3/4}` issue is also now closed at its source.** `scripts/a2_complex_zeta.py:710` now reads `q^{1/2} and q^{1/4}` — the stale `q^{3/4}` is gone — and the output is mid-regeneration (194 lines at the time of writing). T7.3 `<1>3`'s adjudication was already correct in Round 1 and is now consistent with the script it comments on: eigenvalue radii $\{1, q^{1/4}, q^{1/2}\} = \{1, 1.316074, 1.732051\}$, matching the exact block spectra in STEP 5c, with $q^{3/4}$ traceable to the source's non-tempered type-(d) row.

Everything else in T7.3 — $|G|=5616$, $f_1=73008$, $f_2=97344$, $\chi=29952$, the state dimensions 146016 / 292032 / 584064, outdegrees 21 vs 9 and 3, and the degrees 16848 / 219024 / 292032 with 308880 on each side — was verified exactly in Round 1 and is unchanged.

**VERDICT T7.3: VALID**

## T8.3 (Round 1: MINOR — three address blocks quoting content located elsewhere)

**What changed.** The H-LSV row now carries `math/0406208:main.tex:1437-1441` and `:1470` alongside the old `:541-572`, and `math/0406217:main.tex:2617-2626` alongside `:497-515` and `:676-682`; the H-LLP row now carries `:216`, `:229` and `:487` with `:330-336` labelled "(definition)" and `:410-416` labelled "(RH corollary)".

**What I checked — all three new H-LSV addresses byte-checked by me just now:**

- `refs/src/math/0406208/main.tex:1437-1441` reads, verbatim:
  `Let $S = \set{(z_1,\dots,z_d) \suchthat \abs[]{z_i} =1,\, z_1 \cdots z_d = 1}$ ... $$\lam_k = q^{k(d-k)/2}\s_k(z_1,\dots,z_d).$$`
  That is H-LSV's $\operatorname{Aspec}_n = \{(q^{k(n-k)/2}e_k(z))_{k=1}^{n-1} : |z_i|=1, \prod z_i = 1\}$ **character for character**, with the paper's $d$ playing the claim's $n$ and $\s_k$ the elementary symmetric function. The exponent $q^{k(n-k)/2}$ — the one that has to be right for T6.2 `<1>3`/`<1>4`, since $k(k-1)/2 + k(n-k)/2 = k(n-1)/2$ is what puts every root on $|u| = q^{-(n-1)/2}$ — checks exactly. **supports.**
- `:1470` reads `The simultaneous spectrum $\Aspec_d$ is equal to $\sigma(S)$.` **supports** (this is the sentence that makes the displayed set *be* $\operatorname{Aspec}$, and it was the piece most obviously missing before).
- `refs/src/math/0406217/main.tex:2617-2626` reads, verbatim:
  `For every $k = 1,\dots, d-1$, let $S_k$ denote the set of products $b_{u_1}\ldots b_{u_k}$ ... There will be $\binomq{d}{k}{q}$ different products (up to scalar multiples over $L$), and $S_{d-k}$ is the set of inverses of $S_k$.` followed by `The Cayley complex of $G$ with respect to $S_1 \cup \ldots \cup S_{d-1}$ defines a simplicial complex (the clique complex of the Cayley graph). This complex is Ramanujan`.
  That is exactly H-LSV's "$|S_k| = {n \brack k}_q$ and $S_k^{-1} = S_{n-k}$" **and** the Ramanujan Cayley clique complex, in one place. **supports.**

The H-LLP addresses are byte-checked in the T6.4 table above. All three Round 1 defects are therefore repaired with addresses that I have verified line by line, and the labelling of `:330-336` as a *definition* rather than a theorem removes the second half of that finding.

**One cosmetic gap I record without downgrading.** The T8.3 register row for H-LLP lists `:216`, `:229`, `:330-336`, `:410-416`, `:487`, `:1390-1424` but not `:922-923`, whereas the H-LLP hypothesis block at line 64 does list it. The peripheral clause "$|\lambda| = b$" is nevertheless covered inside the row by `:330-336`, which states both alternatives, and the note's own convention ("A citation to an H-input asserts only the statement and scope explicitly recorded with that input") makes the line-64 block the operative record — and that block is now complete. This is a table/text asymmetry of one address, not an unsupported claim, and it would be tidied by appending `:922-923` to the row.

No claim anywhere in the note now rests on an address that does not contain what is attributed to it. The other ten hypothesis blocks (H-POINT, H-KL, H-KY, H-TORS, H-KL-TABLE, H-RUELLE, H-MO, H-KY-LOCAL, H-STRONG, H-KAMBER, H-COVER) were byte-checked in Round 1 and are untouched.

**VERDICT T8.3: VALID**

## Round 2 tally

| label | Round 1 | Round 2 |
|---|---|---|
| T6.4 | MINOR | **VALID** |
| T7.3 | MINOR | **VALID** |
| T8.3 | MINOR | **VALID** |

**Final: 47 VALID, 0 MINOR, 0 INVALID.** All 47 labelled statements of `notes/complex-zeta/astra-proofs.md` are accepted. The mathematical content was never in question in these three findings — two were wording/provenance and one was a report about a volatile artifact — and the Round 1 exact verifications (`scratch_cz_flow.py`, `scratch_cz_link.py`, `scratch_cz_cayley.py`, `scratch_cz_misc.py`) are unaffected by the edits and still stand as written.
