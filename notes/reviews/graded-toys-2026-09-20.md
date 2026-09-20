# REFUTE review: a graded tensor network for the cusp toys (transfer matrix, Frobenius superdeterminant, graded MPS, the even exit, the glued toy, the Frobenius channel, the level tower)

Reviewer: `claude:opus` (adversarial lane, REFUTE protocol).
Date: 2026-09-20 (night). Prover: `claude:fable-5.1`. Numerics lane: `claude:opus` (blind).

## Inputs read (in full)

| file | what it is |
|---|---|
| `notes/graded-toys/brief.md` | the orchestrator's brief (357 lines; G1–G7, deliberately slightly too strong) |
| `notes/graded-toys/proofs.md` | prover output (489 lines; G1–G6 with proofs, a 15-row correction ledger against the brief) |
| `notes/graded-toys/numerics.md`, `scripts/graded_toys.py`, `outputs/graded_toys.txt` | the blind numerics lane (ledger D1–D51, 512 checks, 498 pass / 14 fail, findings F1–F15) |
| `report/sections/04n_graded_toys_network.tex`, `04o_graded_toys_exits.tex` | the two new shards: the registered statements graded below |
| `report/sections/04h_rebound_state.tex`, `04i_cusp_graph_scattering.tex`, `04j_cusp_graph_renewal.tex`, `04k_elliptic_cavity_scattering.tex`, `04l_elliptic_cavity_channel.tex`, `02h_definitions_graded_ramanujan.tex`, `02f_definitions_graded_cmps.tex` | the shards they build on |
| `report/sections/04m_elliptic_cavity_sources.tex` | for the `cit:` rows the proofs lean on |
| `notes/reviews/elliptic-cavity-2026-09-20.md` | the previous review (format and standard) |
| `refs/src/2603.26443/final_draft.tex`, `refs/src/2303.09327/main.tex` | the two sources with byte addresses in the chain |

`hejhal1983selberg2`, `huxley1984scattering`, `rosen2002function` are **not in the repository**
(`report/references.bib` carries all three with `note = {no local source}`, and `refs/src/` has no
copy). Every claim that rests on them is judged **not byte-cited** below.

## Scripts written by this lane (independent; nothing imported from `scripts/graded_toys.py` or `scripts/elliptic_cavity.py`)

| script | checks | covers |
|---|---|---|
| `notes/reviews/scratch_gt_lin.py` | **128** | D2/D3 rebuilt from `def:elliptic-cavity`; degrees, couplings, `p`, `ptilde` exactly; `det(z-M)=p`, `det(1-zM)=\tilde p` symbolically for generic `n=2,3` cores and coefficientwise on D2/D3; `Tr M^m` power sums (D2, D3, five random rational cores); `ker M`, `ord_0 p`, Jordan sizes, the loop counterexample; Bass on `K4`, the 3-cube, `K_{3,3}`, Petersen, `C_5` and the spectral form `spec(√q M_0) ∪ {±1}^{|E|-|V|} = spec(B)`; **three non-regular graphs where the shard's Bass identity fails for every `q`** (new); `M-M_0` and its rank; `det S = (-1)^h p/\tilde p` from a direct `Γ` build |
| `notes/reviews/scratch_gt_sdet.py` | **154** | `sdet(1-wE_S)` exactly for D2, D3 and a synthetic genus-two Weil polynomial; the disc classification with **exhaustiveness** and the two `|e|=q` lines; graded divisor; functional equation both as a rational identity and as the graded multiset similarity `E_S ≃ Π(q^2E_S^{-1})`; `1/R = z^{-2}sdet(1-E_S/(qz^2))` symbolically and at 8 points on D2 and D3; `prop:genus-prefactor-forced` in **seven** instances (`g=1,2`; `s_D=±1`); the D3 even block worked out in the proposition's own terms; the `w`-reciprocal produced by flipping the other copy |
| `notes/reviews/scratch_gt_net.py` | **409** | the D2 model space built from scratch (`Θ = Pc/qq`, basis `{Θ/w^2, Θ/w, Θ/(w-a)}`, Gram **exact by residues** and cross-checked by Taylor coefficients); `I-Z^*Z=J^*J`, `Z^m→0`, `χ_Z = Pc`, the size-two delay block, the Gram identity, `a_n=1`; the graded MPS with a modal and a random reset: normalisation, parities, sector split, `E_0 = [1] ⊕ E_Ω`, odd spectrum, both closures `L=1..8`, **explicit ring vectors to `L=4`**, ring-zeta product formula, `ν(1)=2`, `ν(z_n)=-2`, `ν(0)=+16/+14`; point counts `N_k` by enumeration in `F_{2^k}`; the glued toy in full (parities, uniqueness, evenness, mixedness, rank, `ρ_∞ ≥ t̄^{-1}Ω`, aperiodicity, odd eigenvalues, twisted ring norm); the sector-preserving segment; random even-letter channels; **the homogeneous-Kraus existence step verified from the Choi matrix**; the shared-exit residue on a random three-vertex core; **an explicit degenerate rank-one perturbation refuting the persistence "iff"** |
| `notes/reviews/scratch_gt_funnel.py` | **185** | the one-vertex cusp+funnel formula symbolically in `(a,q)` and the corrected ranges at `q=2,3,5`; the constant-mode identity and both "iff" clauses on three regular diagrams; `p_f = p - (f/q)p^{(v)}` symbolically at all six D2 vertices; `d|z_i|/df` at `f=0`; **continuation-tracked** quartets at `f=1/5`, `1`, `2`, `5`; the Perron parameter; **a non-bipartite triangle core where the roots of `p_f` are not closed under `z↦-z`** (new); the Klein-orbit criterion |
| `notes/reviews/scratch_gt_char.py` | **679** | the arithmetic-metric channel in full (CPTP, Kraus set, `ρ_∞`, `ρ_∞=Ω` iff `[U,Ω]=0`, relaxation moduli); the Sz.-Nagy–Foias characteristic function of `Z'` **and of `Z'^*`, showing they differ** and that `Θ` belongs to `Z`; `U^2` against `Fr|_{H^1}/√q ⊗ 1_2` **and the dimension mismatch with the full `Frob`**; `Γ(1/z)=Γ(z)`, `Q(z)Q(1/z)=Q(1/z)Q(z)`, `S(\bar z)=S(z)^*` and the scalar consequence for D2 with a second cusp at each of `A,C,D,E,F`; the Klein group; `Γ_0(N)` cusp counts, the newform-conductor obstruction and the `Γ_1(N)` Eisenstein count for `N ≤ 40`; all 26 characters mod `T^3-T-1` and all 16 mod `T(T^2+1)` over `F_3[T]` (CRT construction, primitivity, even/odd, `(1-u)`, Weil moduli, Euler product, the superdeterminant identity, the disc divisor) |

**1555 checks, 0 failures.** Every number below is from these scripts unless labelled as the
prover's or the numerics lane's.

## Citations byte-checked

| address | verdict |
|---|---|
| `2603.26443:final_draft.tex:854` (`cit:apw-cusps-pic-no-funnels`, Lubotzky Thm 6.1) | **exact** |
| `2603.26443:final_draft.tex:892` (same row, cusps = `Pic(R)`) | **exact** |
| `2603.26443:final_draft.tex:2092` (`cit:apw-elliptic-numerator`, the `q^{-1/4}` circle) | **exact** |
| `2603.26443:final_draft.tex:1915` (`prop:funnel-self-energy`'s outgoing ratios) | **present**: the line does contain `\sqrt{q}}{\mu_0} f(v)$` and `\sqrt{q} \mu_0} f(v)$`, the cusp and funnel constant-type conditions |
| `2303.09327:main.tex:390` (`cit:kk-level-constant-term`) | **exact** |
| `huxley1984scattering`, `hejhal1983selberg2` (in `obs:level-tower-correction`) | **NOT byte-cited** — no local source; the shard says so |
| `rosen2002function` (in `prop:character-channel-graded-bond`) | **NOT byte-cited** — no local source; the shard does **not** say so (see the finding) |

Every `\cref` in both new shards resolves to an existing `\label` (19 in 04n, 15 in 04o), every
`\cite` key is in `references.bib`, and no undefined control sequence appears.

## Verdicts

**VERDICT thm:diagram-linearisation: MINOR.** Every clause of (a)–(c) and the first identity of (d)
is exactly right, and I verified all of them independently: `det(z-M)=p` and `det(1-zM)=\tilde p`
symbolically for generic symmetric cores with `n=2` (5 symbols) and `n=3` (9 symbols), and
coefficientwise on D2 and D3 (max deviation `9.5e-14` and `1.4e-13`); `Tr M^m = Σ_{p(μ)=0}μ^m` for
`m=1..8` on both diagrams and for `m=1..6` on five random rational cores; `ker M = 0 ⊕ ker(I-C)`
with nullities `(1,2,2)` on D2 and `(2,4,4)` on D3 against `ord_0 p = 2` and `4`, so every delay
block has size two; the loop counterexample `T = [[1/2,1],[1,-1/3]]`, `C = diag(1,0)` gives
`p = z(6z^3-z^2-z-3)/6` exactly, `ord_0 p = 1` and a **single** Jordan block of size one;
`M-M_0 = [[0,C],[0,0]]` exactly with rank `= #{distinct junction vertices}` (1 on D2, **3** on D3
against `h = 4`); `det S = (-1)^h p/\tilde p` from a direct `Γ`-build at three complex points on
both diagrams (`< 3e-9`). The Bass statement in the shard's **corrected** normalisation,
`spec(√q M_0) ∪ {±1}^{|E|-|V|} = spec(B)`, holds to `< 2e-7` on `K_4`, the 3-cube, `K_{3,3}`,
Petersen and `C_5`, and the brief's uncorrected `spec(M_0) ∪ {±1} = spec(B)/√q` fails by
`1-1/√2 = 0.2929` (and `0.765` on Petersen) exactly as F3 says.

*Defect.* Part (d) is printed as "For `C = 0` and `T_X = A_X/√q`, `det(1-zM_0) = det(I-uA_X+qu^2)`
… so by Bass's theorem `spec(√q M_0) ∪ {±1}^{|E|-|V|} = spec(B)`". The **regularity hypothesis is
missing**. `proofs.md` G1(d) has it ("with `A_X` the adjacency matrix of a `(q+1)`-regular graph")
and the brief labels it H-REG; the shard dropped it. Bass's theorem reads
`det(1-uB) = (1-u^2)^{|E|-|V|} det(I - uA + u^2(D-I))`, and `D-I = qI` only for a `(q+1)`-regular
graph. I checked three non-regular graphs (the path `P_4`, a triangle with a pendant, `K_4` minus an
edge): the general `(D-I)` form holds every time, and the shard's `det(I-uA_X+qu^2)` form **fails
for every `q ∈ {1,2,3}`** on all three. (The first identity, `det(1-zM_0) = det(I-uA_X+qu^2)`, is a
pure substitution and is true for any `A_X`; it is only the Bass step that breaks.) The last
sentence of (d) shows the author is aware — but as printed the displayed spectral identity is
false without the hypothesis.
*Corrected statement.* "(d) For `C = 0` and `T_X = A_X/√q` **with `A_X` the adjacency matrix of a
`(q+1)`-regular graph** `X`, …".

**VERDICT thm:scattering-superdeterminant: VALID.** Verified exactly (sympy over `Q`) for D2
(`q=2`, `P = 1-2T+2T^2`), D3 (`q=3`, `P = 1+3T^2`) and a synthetic genus two
(`q=3`, `P = (1+3T^2)(1-2T+3T^2)`): `dim E_S = 4g+4 = 8,8,12`; the even list `1, q, qα_i` and the
odd list `α_i, q, q^2`; `sdet(1-wE_S) = (1-w)P(qw)/((1-q^2w)P(w)) = ζ_K(2s-1)/ζ_K(2s)` as an
identity of rational functions in `w`; the two lines at `e = q` cancel, and after cancellation the
reduced function has numerator and denominator of degree `2g+1` with **no** factor `(1-qw)`. The
disc classification is exhaustive as printed: I checked that `#{|e|<q} + #{|e|=q} + #{|e|>q}` equals
`4g+4` in each case, that the only even disc point is `e=1` (`z = ±q^{-1/2}`), that the odd disc
points are exactly the `2g` numbers `α_i` (`|z| = q^{-1/4}` to `1e-12`), that the two `e=q` lines
sit on `|z| = 1`, and that `ν(1) = +1`, `ν(α_i) = -1`. The functional equation holds exactly
(`q^{2g-2} = 1, 1, 9`), and I also verified the *operator* form the shard asserts: as graded
multisets `E_S` and `Π(q^2E_S^{-1})` agree sector by sector to `1e-9` on all three curves. The
shard has absorbed F5 (the `|e|=q` omission) correctly.

**VERDICT prop:cavity-superdeterminant: MINOR.** The mathematics is exactly right:
`1/R_2 = z^{-2}sdet(1-E_S/(qz^2))` and `1/R_3 = z^{-2}sdet(1-E_S/(qz^2))` for the D3 zeta channel
hold **symbolically** (`sp.simplify` of the difference is identically `0`) and numerically at eight
points each (max deviation `< 1e-13`); the even disc eigenvalue `e=1` sits at `z^2 = 1/q`, the
Perron pair, and the odd disc eigenvalues at `z^2 = α_i/q`, the resonances. The `z^{-2}` prefactor
is `ord_0 p = 2`, `prop:multi-exit-spectrum`(iii), and is a cut artefact.

*Defect (framing, and load-bearing).* "The parities are the cohomological degrees mod 2, with the
Tate-twisted copy flipped; **no choice is made**." The first clause is contradicted by its own
subordinate clause: on the twisted copy the parity is the cohomological degree **plus one**, so it
is not "the cohomological degree mod 2" there. And a choice *is* made: I computed the alternative
`E_S' = Π Fr ⊕ Fr(-1)` (flip the untwisted copy instead) and its superdeterminant is
`sdet(1-wE_S')·sdet(1-wE_S) = 1` identically — the **reciprocal** ratio `ζ_K(2s)/ζ_K(2s-1)`, a
different function. What is genuinely choice-free is one level down and is worth saying instead:
the graded **divisor** `ν = m_0 - m_1` is read off the rational function `ζ_K(2s-1)/ζ_K(2s)` itself,
so *any* graded operator whose superdeterminant is that ratio has `ν(1) = +1` and `ν(α_i) = -1`.
*Corrected statement.* Replace the two clauses by: "the graded divisor is determined by the rational
function alone — any graded `E` with `sdet(1-wE) = ζ_K(2s-1)/ζ_K(2s)` has `ν(1)=+1` and
`ν(α_i)=-1` — and it is realised by `E_S`, on whose untwisted copy the parity is the cohomological
degree and on whose Tate-twisted copy it is the degree plus one."

**VERDICT prop:genus-prefactor-forced: MINOR.** The two displayed formulas are correct and I proved
them independently in seven instances, building `p = z^2 ∏_i(z^2-α_i/q)(z^2-q)D(z)` from the
hypotheses and computing `R = -p/\tilde p` symbolically: `g=1, q=2, D=(z^2+1)^2` (D2, `s_D=+1`);
`g=1, q=3, D=(z^2+1)^2`; `g=2, q=3` with `D=z^2+1` and with `D=1`; and three `s_D=-1` instances
(`D=(z-1)(z+1)`, `D=z^4-1`, `D=(z-1)(z^2+1)(z+1)^3`). In every case `\tilde p(0)=1`, `ord_0 p = 2`,
`1/R = s_D z^{-2}q^{1-g}ζ_K(2s-1)/ζ_K(2s)` and `[z^2]p = -s_D q^{1-g}`; `s_D = D(0) = (-1)^{m_{+1}}`
is right (conjugate pairs and the root `-1` contribute `+1`, the root `+1` contributes `-1`). The
exclusion argument is also sound: with `z = q^{s-1/2}`, `q^{1-2gs} = z^{-2g}q^{1-g}` (exponent
identity verified), so that prefactor would force `ord_0 R = ord_0 p = 2g`, which contradicts
`ord_0 p = 2`. **Three defects, all in the hypotheses and the instance list.**

1. *The `g=1` instance list is wrong for D3.* "For `g = 1`, `s_D = 1`, this is
`thm:d2-zeta,thm:d3-channels`." D3 is a **four-cusp** diagram with two `c=1` kernel vertices and
`ord_0 p_3 = 4`, so it does not satisfy the proposition's hypotheses at all; what does satisfy them
is D3's **even 2×2 block**, `p_e = (z^2/3)(z^2-1)(z^2-3)(z^2+1)(3z^4+1)`. For that block I computed
`D = (z^2-1)(z^2+1) = z^4-1`, so `s_D = D(0) = **-1**` (the threshold root `z=+1` is simple in
`p_e`: `p_e(1) = 0`, `p_e'(1) ≠ 0`), and `[z^2]p_e = **+1** = -s_D q^{1-g}`, not `-1`. The final
formula `1/R_3 = z^{-2}ζ_K(2s-1)/ζ_K(2s)` nevertheless holds because the even block has `h = 2`, so
`det S_e = +p_e/\tilde p_e` (verified symbolically) while the proposition is written for `h = 1`
where `R = -p/\tilde p`; the two minus signs cancel. As printed, "`s_D = 1`" is false for D3.
2. *The hypothesis list is not satisfiable as printed.* It asks for "the `4g` numbers
`z^2 ∈ {α_i/q}` as its **resonances**, all simple, and **every other** root of `p` on the unit
circle". By `def:cusp-diagram` and `thm:cusp-resonance-count` the zero root is a resonance, and the
reduced `R_2` has a **double zero at `z=0`** (verified: the numerator of the cancelled `-p_2/\tilde p_2`
has `ord_0 = 2`), so D2 has **six** resonances, not four. Taken literally the hypotheses force
`ord_0 p = 0`, contradicting the `ord_0 p = 2` the proof itself uses.
3. *The hypotheses of `prop:multi-exit-spectrum`(iii) are dropped.* `ord_0 p = 2 dim ker(I-C) = 2`
needs "no loop at the `c=1` junction" **and** an invertible Schur bracket — exactly the hypotheses
that `thm:diagram-linearisation`(c) in the *same shard* is careful to state, and exactly what
numerics F1 found missing. With a loop, `ord_0 p = 1` (my counterexample above) and the whole
factorisation changes.
*Corrected statement.* "Let a one-cusp diagram with one junction of coupling `c = 1` and **no loop
at that junction**, cut at the junction, with the Schur bracket of `prop:multi-exit-spectrum`(iii)
invertible, have the Perron pair as its only visible bound states, the `4g` numbers
`z^2 ∈ {α_i/q}` as its **nonzero** resonances, all simple, and every root of `p` other than these,
the exterior pair `±q^{1/2}` and the double root at `0` on the unit circle …. For D2 (`g=1`,
`s_D=+1`) this is `thm:d2-zeta`; for D3's even channel (`h=2`, `s_D=-1`, `[z^2]p_e = +1`) the same
computation gives `thm:d3-channels` after the `(-1)^h` of `thm:multi-exit-scattering`."

**VERDICT thm:renewal-graded-mps: VALID.** Every clause, on a model space I rebuilt from scratch.
`Θ_2 = Pc/qq` with `Pc` monic over the six resonances and `qq(w) = ∏(1-\bar z_j w) = (w^4-2w^2+2)/2`
reproduces `thm:h-exit-model`'s `Θ_2` at three points and is inner on 17 circle points; in the basis
`{Θ/w^2, Θ/w, Θ/(w-a)}` the Gram is **exact** (`⟨Θ/w^2,Θ/w⟩=0`, `⟨Θ/w^2,Θ/(w-b)⟩=b`,
`⟨Θ/w,Θ/(w-b)⟩=1`, `⟨Θ/(w-a),Θ/(w-b)⟩=1/(1-\bar ab)`) and agrees with an independent
Taylor-coefficient computation to `2e-10`; after Cholesky, `I-Z^*Z = J^*J` to `4e-15`, `rank J = 1`,
`χ_Z = Pc` to `3e-15`, `‖Z^{200}‖ = 0`, one Jordan block of size two at `0`, `Jk_a = 1` and
`‖k_a‖^2 = (1-|a|^2)^{-1}`, and the Gram identity holds for all 16 pairs. Then, for a modal
Hasse–Weil reset and a random reset: (a) `ΣA_i^*A_i = 1` to `7e-16`, every letter even, `EE`
commutes with `P⊗\bar P`; (b) even/odd dimensions `37/12`, `EE` block diagonal in the sectors,
`spec E_0 = {1} ∪ spec E_Ω` and `spec E_1 = spec Z ∪ \overline{spec Z}` to `1e-8`; (c) both closures
for `L=1..8` to `1e-7`, **and** the explicit ring vectors `⟨ψ_L|ψ_L⟩ = Tr EE^L`,
`⟨ψ_L^P|ψ_L^P⟩ = str EE^L` for `L=1..4` over all `5^L` words; (d) the ring-zeta product formula at
three values of `u` (`< 1e-13`), `ν(1)=2`, `ν(λ) = -2m_λ` at all four Hasse–Weil values, and
`ν(0) = +16` (modal) / `+14` (random) — the shard's restriction of the divisor to **nonzero**
eigenvalues (F7, F8) is exactly what is needed; (e) every **nonzero** odd eigenvalue has modulus
`q^{-1/4} = 0.8408964` while the full odd spectrum has the two moduli `{0, 0.8408964}` (F9), and
`1` has even multiplicity two. The point-count identity is right: by direct enumeration of
`y^2+y = x^3+x+1` in `F_{2^k}` (built as `F_2[x]/(f)`, point at infinity included) `N_k = 1, 5, 13,
25, 41`, and `Tr Z^{2k} = 2q^{-k}(α_+^k+α_-^k) = 2q^{-k}(1+q^k-N_k)` to `1e-8` for `k=1..5`, with
`Tr Z^L = 0` for `L = 1,3,5,7`. *Note (not a defect).* "`ν = m_0` at the **remaining** nonzero
eigenvalues of `E_Ω`" tacitly assumes `spec E_Ω ∩ spec Z = ∅` off `0`; on D2 this holds because
`|z_a z̄_b| = r^2 ≠ r`, and under RH(Y) it always does.

**VERDICT prop:constant-mode-mixed-sheets: VALID.** Both halves. The constant-mode identity
`[(1+z^2)I - zT_X - z^2C_c - q^{-1}C_f]x = 0` at `z = q^{-1/2}` holds **exactly** (symbolic residual
`0`, not a tolerance) on three `(q+1)`-regular cusp-plus-funnel diagrams: D2 with the cusp at `B`
replaced by a funnel, D2 as it stands, and a hand-built two-vertex 3-regular cusp(2)+funnel(2)
diagram; all entries of `x = (1/√S(v))` are nonzero; the degree condition at `f_1` does force
`S(f_1) = S(e)` (verified), which is where the extra `1/q` on the funnel coupling comes from. Both
"iff" clauses are exactly right: the outgoing matrix differs by `(z^2-1)C_c` and the bound matrix
by `q^{-1}(1-z^2)C_f`, and with `z^2 = 1/q ≠ 1` and `x` nowhere zero each vanishes iff the
corresponding weight matrix does — verified in all three configurations, in both directions. The
one-vertex formula `p = z^2-(1+a(q-1))/q` is exact symbolically in `(a,q)`, and the corrected ranges
(F10) check out at `q = 2, 3, 5` and nine values of `a`: for `0 ≤ a < 1` the root lies in
`[1/q,1)`, a **resonance**, equal to `q^{-1/2}` iff `a = 0`, while `ϑ^2 = q/(1+a(q-1)) > 1` there
(e.g. `8/5, 4/3, 8/7` at `q=2` for `a = 1/4, 1/2, 3/4`); `a=1` gives `1`, the threshold; for
`1 < a ≤ q+1` one has `ϑ^2 ∈ [1/q,1)`, equal to `1/q` iff `a = q+1`. The concluding sentence "A
light cusp leaves the Perron-type mode outgoing, but at a radius other than `q^{-1/2}`" is correct.

**VERDICT lem:funnel-first-order: MINOR.** The quantitative content is all verified. The cofactor
identity `p_f = p - (f/q)p^{(v)}` holds **symbolically and exactly** at all six D2 vertices; the
first-order formulas are right; and with continuation-tracked roots I reproduce the numerics lane
number for number: `d|z_i|/df` at `f=0` is `+0.0630672` (A), `+0.1261345` (B), `-0.0210224` (C),
`-0.1681793` (D), `-0.0630672` (E, F), identical for all four quartet roots at each vertex
(spread `0.00e+00`, my own computation, to `2e-6` of the lane's values); at `f = 1/5` the four
moduli are still equal (spread `< 1e-8`) at radii `0.853128, 0.864176, 0.836761, 0.807041,
0.827557, 0.827557`, and the quartet is still closed under `z↦-z` and `z↦\bar z`; the orbit splits
into moduli `0.618034, 0.707107` at `f=1` for `D` (and I add: the split quartet is **real**,
`max|Im z| < 1e-7` — two size-two Klein orbits, exactly as the lemma's criterion predicts), at
`f=2` for `E, F`, at `f=5` for `A`, and not up to `f=5` at `B, C`. The Klein criterion itself is
correct and I verified it abstractly: any orbit `{z,-z,\bar z,-\bar z}` is automatically
equimodular, a set of four distinct **non-real, non-imaginary** elements closed under the group is
a single orbit, and an orbit of size `≤2` forces a real, imaginary or zero element — so
equimodularity can only be lost at a split, which is what happens. The Perron statement is right
too: the exterior real pair survives for every `f` tried and `ϑ` decreases strictly,
`0.706576, 0.679776, 0.598405, 0.382576, 0.138712` at `f = 0.01, 0.5, 2, 10, 100` (reproduced).

*Defect.* "Since `P_v` is real and diagonal, the roots of `p_f` stay closed under `z↦-z` and
`z↦\bar z` for every `f`". The conjugation closure follows from reality, but **`z↦-z` closure does
not follow from `P_v` being real and diagonal** — it needs the core to be bipartite, i.e. a diagonal
sign `ε` with `εT_Xε = -T_X` (which then commutes with the diagonal `C` and `P_v`), making `p_f`
even in `z`. `proofs.md`'s Corollary G4(c′) does say "`P_v` … commutes with the **bipartite sign**
`ε`"; the shard dropped the sign. Counterexample: the triangle core `T_X = A(K_3)`, `C = diag(1,0,0)`,
one funnel of weight `f=1` at vertex 1, `q=2` — `p_f` has nonzero odd coefficients and its root set
is **not** closed under `z↦-z` (already at `f=0`), while remaining conjugation closed. The lemma is
stated for a general diagram, and the whole equimodularity conclusion collapses without
bipartiteness. D2 is bipartite, so everything claimed about D2 stands.
*Corrected statement.* "Since the core is **bipartite** (`εT_Xε = -T_X` with `ε` diagonal) and `P_v`
is real and diagonal, hence commutes with `ε`, the roots of `p_f` stay closed under `z↦-z` and
`z↦\bar z` for every `f` …".

**VERDICT lem:even-letters-two-fixed-points: VALID.** The lemma is right and — this is the point the
brief got muddled — the "Hence" clause is the **contrapositive of the first sentence** and needs
nothing else: if every homogeneous letter were even, the first part gives two stationary densities,
contradicting uniqueness. `P A P = A` forces `A` block diagonal (so `A` and `A^*` preserve each
sector), `Tr E(ρ) = Tr(ρ ΣA_i^*A_i) = Tr ρ`, and `E` restricts to a trace-preserving CP map on each
`B(H_±)`, which has a fixed density. Verified on six random even-letter channels with
`dim H_± ∈ {1,2,3}`: eigenvalue `1` of the doubled transfer always has multiplicity `≥ 2`. Verified
too on the sector-preserving reset of the glued toy: 13 even letters, eigenvalue `1` of multiplicity
exactly `2`. I also checked the auxiliary claim `proofs.md` adds but the shard wisely does not need —
"a channel commuting with `Ad(P)` has a Kraus representation by homogeneous letters". It is **true**:
the Choi matrix `J = Σ_{ij}|i⟩⟨j|⊗E(|i⟩⟨j|)` satisfies `(P⊗P)J(P⊗P) = J`, so diagonalising `J`
inside the `±1` eigenspaces of `P⊗P` yields Kraus operators `A` with `PAP = ±A`. Verified on five
channels built from deliberately **non**-homogeneous letters: the Choi matrix commutes with `P⊗P`
(`< 1e-8`), the reconstruction reproduces the channel (`< 1e-7`), and every reconstructed letter is
homogeneous (`< 1e-7`). *Note.* The lemma as printed carries no finite-dimensionality hypothesis;
the fixed-density step needs one (or compactness). In this shard the bond is always finite.

**VERDICT thm:glued-graded-toy: VALID.** All five parts, on the instance (v) built from scratch.
(i) The glued `(Z,J) = (Z_+⊕Z_-, J_+⊕J_-)` satisfies `I-Z^*Z = J^*J` (`4e-15`) and `Z^m→0`, so it is
an `(h_++h_-)`-exit contraction in the sense of H-CONTRACTION; `ΣA_i^*A_i = 1` (`3e-15`); all 13
letters are homogeneous with parity `ε(ω_k)ε(j_a)` (`< 1e-9`) and **6 of them are odd**, the cross
letters. (ii) The uniqueness step is legitimate, and I checked the doubt the brief invites: because
the reset is **fixed**, the flux really is the scalar functional `ρ ↦ Tr(JρJ^*)`, and
`thm:h-exit-renewal`(d) — a registered `proved` row — states in terms that apply verbatim that "for
a fixed reset the scalar proof of `thm:cusp-renewal-discrete` applies **for any exit rank**". I
verified it three ways: analytically on a two-mode diagonal example (the stationary equation has a
unique solution, off-diagonals forced to zero); numerically, eigenvalue `1` of the `64×64` doubled
channel is **simple**; and the only peripheral eigenvalue is `1`, with the holding law summing to
`1` and its support having gcd `1`, so the instance is aperiodic and `ρ_∞` attracts. `ρ_∞` is even
(`< 1e-9`), mixed (both sector traces bounded away from `0`), satisfies `ρ_∞ ≥ t̄^{-1}Ω` (minimum
eigenvalue of the difference `> -1e-9`) and therefore has **rank ≥ 2** — the argument is sound:
`Ω = Ω_+⊕Ω_-` with both traces positive already has rank `≥ 2`. (iii) For odd `X`, `JXJ^*` is
block-off-diagonal in `C^{h_+}⊕C^{h_-}`, so its trace vanishes and `E X = ZXZ^*`; I verified
`⟨a_m,a_n⟩ = 0` **exactly** across blocks and that all eight coherences `|k_n⟩⟨k_m|` are
eigen-operators with eigenvalue `z_n\bar z_m` (`< 1e-9`) of modulus `q^{-3/4}`. The full odd
spectrum is `{z_n\bar z_m} ∪ {z_m\bar z_n}` to `1e-8`, with moduli `{0, 0.5946036 = q^{-3/4}}` —
the delay exception is stated in (v), so there is no clash with (iii). (iv) The twisted ring-norm
identity `str EE^L - Tr E_0^L = -2Re[(Tr Z_-^L)\overline{Tr Z_+^L}]` holds for `L=1..8` (`< 1e-7`).
(v) `p_+ = z^2-1/q` exactly, `R_+` is inner of degree two, `dim K_+ = 2`, `spec Z_+ = {±q^{-1/2}}`,
`I-Z_+^*Z_+ = J_+^*J_+`, and `Tr Z_+^L = q^{-L/2}(1+(-1)^L)` for `L=1..8`.

**VERDICT prop:shared-exit-tradeoff: MINOR.** The exact content is right and I verified all of it on
a random three-vertex core with one shared unit cusp and six distinct interior resonances:
`a_n = Jk_n = 1` for every mode, `Tr(JXJ^*) = ⟨a_m,a_n⟩ = (1-\bar z_m z_n)⟨k_m,k_n⟩` for all 36
pairs (`< 1e-8`), and the residue is **exactly** `⟨a_m,a_n⟩Ω`
(`E X - z_n\bar z_m X - ⟨a_m,a_n⟩Ω < 1e-8`), so `X` is not an eigen-operator whenever
`⟨a_m,a_n⟩ ≠ 0`. The last clause of the proposition is what fails.

*Defect.* "the copy of the eigenvalue it carried persists iff `⟨l_n|ρ̄|l_m⟩ = 0` for the dual
eigenvectors (`prop:rebound-persistence-secular`); on a real core the value is degenerate in `Ad(Z)`
and keeps its other copies." `prop:rebound-persistence-secular`'s criterion is stated for a
**simple** eigenvalue of `E_0`, and the sentence itself concedes that the value is **degenerate**.
For a rank-one perturbation `E = E_0 + |Ω⟩⟩⟨⟨fl|` and a value `λ` of `E_0`-multiplicity `μ`, the
correct statement is `det(u-E) = det(u-E_0) - ⟨⟨fl|adj(u-E_0)|Ω⟩⟩`, whose order of vanishing at `λ`
is `μ-1` iff `Σ_j fl(X_j)·dual_j(Ω) ≠ 0` — a **sum over all eigen-operators at `λ`**, not one term.
I built an explicit counterexample: `Z = diag(0.6, 0.5e^{0.7i}, 0.75, 0.4e^{0.7i})`, for which
`z_1\bar z_2 = z_3\bar z_4` with `Ad(Z)`-multiplicity exactly two, flux `fl(X) = ⟨f|X|f⟩` with
`f = (1,1,1,1)/2`, and a density `Ω` with `Ω_{12} = +t`, `Ω_{34} = -t`. Each individual
`fl(X_j)dual_j(Ω)` is nonzero, yet the two cancel and the multiplicity of `λ` **does not drop**
(`2 → 2`), whereas charging either pair alone drops it (`2 → 1`). This degeneracy is not exotic: on
D2's quartet `{a,-a,\bar a,-\bar a}` the value `z_1\bar z_2 = a\overline{(-a)} = -|a|^2 = -q^{-1/2}`
is carried by **two** distinct odd coherences (verified), which is exactly the situation the
sentence describes.
*Corrected statement.* "… and the multiplicity of `z_n\bar z_m` in `E_{\reb}` drops by exactly one
iff `Σ_j ⟨a_{m_j},a_{n_j}⟩⟨l_{n_j}|\reb|l_{m_j}⟩ ≠ 0`, the sum over the eigen-operators of `Ad(Z)`
at that value (`prop:rebound-persistence-secular`, whose one-term criterion is the simple case); on
a real core the value is degenerate, and cancellation in the sum can keep every copy."

**VERDICT thm:frobenius-channel-expander: MINOR.** All the channel statements are exactly right and
verified for a modal and a random `Ω`: the Kraus set `{rU} ∪ {√(1-r^2)√p_k|ω_k⟩⟨e_a|}` sums to `1`
and reproduces `E'` (`< 1e-9`); `ρ_∞ = (1-r^2)Σ r^{2m}U^mΩU^{*m}` is stationary of trace one and
eigenvalue `1` is simple; `ρ_∞ = Ω` **iff** `[U,Ω] = 0` (true for the modal `Ω`, false for the
random one, both directions checked); on traceless operators `E' = r^2Ad(U)`, so all 15 relaxation
eigenvalues have modulus **exactly** `r^2 = q^{-1/2}` and equal `r^2e^{i(θ_a-θ_b)}` (`< 1e-8`). The
characteristic-function clause is right, and I checked the brief's `Z'` versus `Z'^*` confusion
directly: the Sz.-Nagy–Foias function of the contraction `A = rU`,
`Θ_A(z) = -A + zD_{A^*}(1-zA^*)^{-1}D_A`, equals `(1-zrU^*)^{-1}(z-rU) = diag(b_{z_a}(z))` at four
points (`< 1e-9`), whereas `Θ_{A^*} = diag(b_{\bar z_a})` is a genuinely different function for
non-real `z_a`. The scalar model-space cross-check confirms the convention: for `Θ = b_a` the
compressed shift is the scalar `a` and **its** characteristic function is `b_a`, so it is `Z`, not
`Z^*`, whose characteristic function is `Θ`. The shard is right and the brief was wrong.

*Defect (notation, but a genuine dimension mismatch).* "`U^2 ≃ (Frob/√q)⊗1_2` as multisets." In the
convention fixed two pages earlier in `04n` — "`Frob` with eigenvalues `1; α_1,…,α_{2g}; q`" —
`Frob` is the **full** graded module, of dimension `2g+2 = 4` for D2, so `(Frob/√q)⊗1_2` is
**eight**-dimensional while `U^2` is `4×4`. What is true, and what I verified, is
`U^2 ≃ (Frob|_{H^1}/√q)⊗1_2`: `spec U^2 = {α_+/√q, α_+/√q, α_-/√q, α_-/√q}` to `1e-12`. (The
`(Frob|_{H^1}/√q)^{-1}` version of `prop:d2-spectrum-frobenius` and the brief is the same multiset,
since `√q/α = \barα/√q` and the `α` multiset is conjugation closed — also verified.)
*Corrected statement.* "… `U^2 ≃ (\Frob|_{H^1}/\sqrt{\qs})\otimes1_2` as multisets", and the same
substitution in `prop:d2-spectrum-frobenius` if that shard is touched.

**VERDICT prop:no-selfadjoint-one-mode-exits: MINOR.** The core argument is correct and I verified
every step of it on D2 with a second unit cusp at each of `A, C, D, E, F`: `Γ(\bar z) = Γ(z)^*`
(`< 1e-8`), `Γ(1/z) = Γ(z)` (so `Q(z)` and `Q(1/z)` are polynomials in one matrix and **commute**,
`< 1e-9` — the step `proofs.md` needs and the shard leaves implicit), `S = S^T` and
`S(\bar z) = S(z)^*` (`< 1e-7`), and `e^*S(\bar z)e = \overline{e^*S(z)e}` for five constant
directions including complex ones. Hence a constant diagonalising unitary gives channels with
`s_a(\bar z) = \overline{s_a(z)}` and conjugation-closed zero sets, which a single Blaschke factor
`b_{z_a}` with `z_a` non-real is not: the negative conclusion stands. The Klein clause is right
too — `ε` and conjugation act on `{a,-a,\bar a,-\bar a}` as a Klein four-group, the four elements
are distinct (`a` non-real and non-imaginary), and the action is simply transitive. **Two defects.**

1. "the symmetric arithmetic metric is **the unique** diagonal metric it fixes". The registered
source `thm:arithmetic-metric` says "a **single ray**, all weights equal", i.e. unique **up to
scale**; every positive multiple of an invariant metric is invariant. One-word fix: "the unique
diagonal metric it fixes **up to scale**".
2. "the finest constant-basis splitting of the quartet **is** into two conjugation-closed pairs"
asserts **attainment**, which nothing in the shard, the proofs or the numerics establishes. What is
proved is the **obstruction**: no constant exit direction of a Hermitian core can see a
non-conjugation-closed set, so `{a,\bar a}` and `{-a,-\bar a}` are the only conjugation-closed pairs
into which the quartet could split. The numerics lane's D46 tested D2 with a second cusp and
reported conjugation-closed disc zero sets, but those diagrams carry different resonances, not D2's
Hasse–Weil quartet. A disconnected self-adjoint two-cusp diagram (two one-vertex cores with
`c^2 < 1`, each with a non-real conjugate pair — verified) does realise a `2+2` splitting of *some*
four non-real modes, but nothing shows it for D2's quartet on a connected core.
*Corrected statement.* "…; no self-adjoint diagram in the sense of `def:elliptic-cavity` (Hermitian
core, standard rays, constant couplings, constant exit directions) can separate a single non-real
mode, so the finest splitting **not excluded by this argument** is into two conjugation-closed
pairs; whether that splitting is attained on a connected core carrying the quartet is open."

**VERDICT obs:level-tower-correction: VALID.** (Declared not byte-cited, and it says so.) I could not
byte-check Huxley or Hejhal — neither is in the repository, and the shard states this explicitly,
which is the honest thing to do. What I could test, I tested, and every piece of the internal logic
holds. (i) For squarefree `N ≤ 40`, `#cusps(Γ_0(N)) = Σ_{d|N}φ(gcd(d,N/d)) = 2^{ω(N)} = #divisors`,
so the `2^{ω(N)}` functions `E(dz,s)` are exactly as many as the cusps. (ii) They are
`Γ_0(N)`-invariant: for `γ = (a,b;cN,d')` and `σ_d = diag(d,1)`, `σ_dγσ_d^{-1} = (a, bd; cN/d, d')`
lies in `SL_2(Z)` because `d | N` — the shard's own one-line reason, and it is correct. (iii) "No
Eisenstein newforms with trivial character at squarefree level": a newform pair needs
`χ_1χ_2 = 1` with `cond(χ_1)cond(χ_2) = N`, hence `N = cond(χ_1)^2`, impossible for squarefree
`N > 1`. I verified computationally for every squarefree `N ≤ 40` that no divisor `u > 1` has
`u^2 = N`, and that the trivial-nebentypus Eisenstein count `Σ_{u^2t|N}φ^*(u)d(N/(u^2))` equals
`2^{ω(N)}`, while for non-squarefree `N` it strictly exceeds `d(N)` — the dichotomy the observation
rests on. (iv) The general count is consistent: `Σ_{uvt|N}φ^*(u)φ^*(v) = Σ_{d|N}φ(d)φ(N/d)` for
every `N ≤ 30`, and for `N ≥ 5` half of it is `#cusps(Γ_1(N))` — so the `Γ_1(N)` Eisenstein space
really is where the nontrivial character pairs live, which is the observation's point. (v) The
determinant consequence is sound: the constant terms give `Φ(s) = φ(s)M(s)` with `M` rational in
the `p^{-s}`, so `det Φ = φ(s)^{h} det M` with `h = 2^{ω(N)}` (symbolically verified, and on the
classical `Γ_0(p)` shape `det Φ/φ^2` is free of `φ`). No Dirichlet `L`-function can appear.
*Note.* "there are no Eisenstein newforms with trivial character at squarefree level" needs `N > 1`
(at `N = 1` the single series is a newform); the statement is vacuous there and nothing depends on it.

**VERDICT prop:character-channel-graded-bond: VALID.** Verified over `F_3[T]` for
`N_1 = T^3-T-1` (irreducible; I re-derived the irreducible counts `3,3,8,18,48` in degrees `1..5`)
and `N_2 = T(T^2+1)`, with the character tables built from scratch by CRT and discrete logarithms
in `F_{27}^×` and `F_3^× × F_9^×`. `|(A/N_1)^×| = 26`, `|(A/N_2)^×| = 16`, one trivial character
each. For every one of the 40 nontrivial characters `deg L = deg N - 1`. All 25 nontrivial
characters mod `N_1` are primitive (my primitivity test: every CRT component nontrivial, valid
since both `N` are squarefree) and **12 of them are even**; exactly **7 of the 15** mod `N_2` are
primitive. For every primitive `χ`: `(1-u) | L` **iff** `χ` is even; after dividing out that factor,
every root `β` of the completed `L` has `|β| = √3` (`< 1e-7`); `sdet(1-wE_χ) = L_c(qw)/L_c(w)` at
three values of `w`; and the disc part is odd only — `|β| = √q < q` and `|qβ| = q^{3/2} > q`, so
there is no even disc eigenvalue in any channel. The Euler product agrees with `L(u,χ)` to order
`u^5` for the primitive characters I sampled. The imprimitive characters mod `N_2` each carry a root
of modulus one from the re-inserted Euler factor, and a modulus-one `β` does sit at
`|z| = |β/q|^{1/2} = q^{-1/2}`, the Perron radius, exactly as the last sentence says. The trivial
channel is the `g=0` line `(1-w)/(1-q^2w)` with the single even disc point. The shard has absorbed
F13 (primitivity, the trivial zeros split off) and F14 correctly, and the
completed-versus-incomplete caveat is carried both in `asm:h-arith-gamma1` and in the closing
sentence. *Two notes, neither a defect in the mathematics.* (a) `\cite{rosen2002function}` is
**not byte-cited** and, unlike `obs:level-tower-correction`, this proposition does not say so; the
Weil bound `|β| = √q` for a nontrivial primitive character is standard, but the shard should carry
the same "not byte-cited" flag. (b) "the completed `L`-function (Euler factor at `∞` **included**)"
in `asm:h-arith-gamma1` is easy to read backwards: including the `∞`-Euler factor `(1-u)^{-1}`
**lowers** the degree from `deg N - 1` to `deg N - 2` for an even `χ`, by cancelling the `(1-u)`
that the proposition displays. The two statements are consistent, but a reader will want it spelt
out once.

**VERDICT obs:graded-toys-next: VALID.** It is a to-do list, and every factual assertion in it
checks out. (i) `asm:h-arith-gamma1` is indeed the open point and the completed-versus-incomplete
question is indeed part of it (my F13/F14 re-derivation confirms which modes each choice adds);
Gekeler–Nonnengardt is named in plain text, not `\cite`d, so nothing is claimed of the bibliography.
(ii) is well posed given `def:cmps-ring-vector`'s fermionic species and `def:cmps-transfer-generators`'s
sign-twisted generators, and the glued toy does have odd letters (6 of 13, verified). (iii) is
accurate: the Frobenius channel's letters really are `rU` and the reset, and its relaxation spectrum
really is `r^2spec(Ad U)` — verified, all 15 relaxation eigenvalues of modulus exactly `r^2`.
(iv) is exactly the gap that `prop:no-selfadjoint-one-mode-exits` leaves open. No overclaim.

## Findings: what must be fixed in the shards before promotion

1. **`thm:diagram-linearisation`(d)** — insert the regularity hypothesis: "with `A_X` the adjacency
matrix of a `(q+1)`-regular graph". Without it the displayed Bass identity is false (three
counterexamples).
2. **`prop:cavity-superdeterminant`** — replace "The parities are the cohomological degrees mod 2,
with the Tate-twisted copy flipped; no choice is made" by the divisor statement given above. As
printed, the first clause contradicts the second, and flipping the other copy gives the reciprocal
function.
3. **`prop:genus-prefactor-forced`** — (a) the sentence "For `g = 1`, `s_D = 1`, this is
`thm:d2-zeta,thm:d3-channels`" is **false for D3**: its even channel has `D = z^4-1`, `s_D = -1`,
`[z^2]p_e = +1`, and `h = 2`, so the `(-1)^h` of `thm:multi-exit-scattering` is what rescues the
prefactor. (b) The hypothesis list must say "**nonzero** resonances" and must admit the double root
at `0`, or it excludes D2. (c) Restore the "no loop at the `c=1` junction, Schur bracket
invertible" hypotheses that the same shard states in `thm:diagram-linearisation`(c).
4. **`lem:funnel-first-order`** — the `z↦-z` closure needs bipartiteness, not just that `P_v` is
real and diagonal (non-bipartite counterexample above). Restore `proofs.md`'s bipartite sign.
5. **`prop:shared-exit-tradeoff`** — the persistence "iff" is a simple-eigenvalue criterion and the
sentence itself says the value is degenerate; replace by the sum criterion (explicit counterexample
above).
6. **`thm:frobenius-channel-expander`** — `U^2 ≃ (\Frob|_{H^1}/\sqrt q)\otimes 1_2`, not `\Frob`
(dimension `4` against `8`).
7. **`prop:no-selfadjoint-one-mode-exits`** — "unique diagonal metric" → "unique **up to scale**";
and "the finest splitting **is** into two conjugation-closed pairs" asserts an attainment that is
not established — state it as the obstruction.
8. **`prop:character-channel-graded-bond`** — add the "not byte-cited" flag for
`\cite{rosen2002function}` (no local source), as `obs:level-tower-correction` does for Huxley and
Hejhal; and spell out once that "Euler factor at `∞` included" **cancels** the `(1-u)`.
9. **`num:graded-toys-network`** (numerical environment, bookkeeping) — "the odd multiplicities
`-2` and the **even multiplicity** of `0` (`16`, `14`)" mislabels the numbers: `16` and `14` are
`ν(0)`; the even multiplicities are `20` and `18` (I recomputed both, and the odd multiplicity is
`4` in each case).
10. **`num:funnel-on-d2`** and **`num:character-channels`** (numerical environments, bookkeeping) —
the ledger ranges are off: the constant-mode and one-vertex rows are D33–D37, not D32–D37; the
character rows are D47–D51, and D44–D46 are the Frobenius channel and the Hermitian-core test, not
part of "D38–D45".

## Summary table

| claim | verdict | one line |
|---|---|---|
| `thm:diagram-linearisation` | MINOR | all identities verified; part (d)'s Bass step is missing the `(q+1)`-regularity hypothesis and is false without it |
| `thm:scattering-superdeterminant` | VALID | `sdet`, the exhaustive disc classification, the divisor and the functional equation exact for `g = 1, 1, 2` |
| `prop:cavity-superdeterminant` | MINOR | `1/R = z^{-2}sdet` exact; "the parities are the cohomological degrees mod 2 … no choice is made" is self-contradictory and overclaims the operator (the divisor is what is forced) |
| `prop:genus-prefactor-forced` | MINOR | formulas right in 7 instances; "for `g=1`, `s_D=1`, this is `thm:d3-channels`" is false (`s_D = -1`, `h = 2`), the hypothesis list excludes the delay root, and the loop/Schur hypotheses are dropped |
| `thm:renewal-graded-mps` | VALID | every clause verified on a from-scratch model space, including the ring vectors to `L=4` and `N_k = 1,5,13,25,41` by enumeration |
| `prop:constant-mode-mixed-sheets` | VALID | constant-mode identity exact on three regular diagrams, both "iff" clauses, the corrected `a`-ranges at `q = 2,3,5` |
| `lem:funnel-first-order` | MINOR | cofactor identity, derivatives and the split all reproduced; the `z↦-z` closure needs bipartiteness, not just a real diagonal `P_v` |
| `lem:even-letters-two-fixed-points` | VALID | the consequence is the contrapositive of the first part; the homogeneous-Kraus step is also true (Choi commutes with `P⊗P`) |
| `thm:glued-graded-toy` | VALID | the fixed reset makes the flux scalar, so `thm:h-exit-renewal`(d) applies verbatim; uniqueness, mixedness, rank `≥2`, aperiodicity and the odd spectrum all verified |
| `prop:shared-exit-tradeoff` | MINOR | Gram identity and residue exact; the persistence "iff" fails in the degenerate case the sentence itself invokes (counterexample built) |
| `thm:frobenius-channel-expander` | MINOR | channel, gap and characteristic function of `Z'` (not `Z'^*`) all right; `U^2 ≃ (\Frob/\sqrt q)\otimes1_2` is a dimension mismatch, should be `\Frob|_{H^1}` |
| `prop:no-selfadjoint-one-mode-exits` | MINOR | the obstruction is proved and verified; "unique diagonal metric" needs "up to scale" and the `2+2` splitting is asserted, not attained |
| `obs:level-tower-correction` | VALID | not byte-cited and says so; every testable piece of the internal logic (cusp counts, newform obstruction, `Γ_1(N)` count, `det Φ = φ^h·` rational) checks out |
| `prop:character-channel-graded-bond` | VALID | all 40 nontrivial characters over `F_3[T]` verified; add the "not byte-cited" flag for Rosen |
| `obs:graded-toys-next` | VALID | a to-do list whose embedded facts all check out |

**8 VALID / 7 MINOR / 0 INVALID.**

## Scratch scripts

| script | checks |
|---|---|
| `notes/reviews/scratch_gt_lin.py` | 128 |
| `notes/reviews/scratch_gt_sdet.py` | 154 |
| `notes/reviews/scratch_gt_net.py` | 409 |
| `notes/reviews/scratch_gt_funnel.py` | 185 |
| `notes/reviews/scratch_gt_char.py` | 679 |
| **total** | **1555, 0 failures** |

All five run with `python3` + `numpy`/`sympy` only, from the repository root, in under four minutes
combined, and import nothing from `scripts/`.

## What a further reviewer should attack next

1. **The genus-two hypothesis, not the formula.** `prop:genus-prefactor-forced` is a conditional
whose hypotheses no diagram in the repository satisfies at `g ≥ 2`. The sharp question is whether a
one-cusp genus-two diagram exists at all with `ord_0 p = 2` and the Perron pair as its only visible
bound state; `prop:nonzero-root-product`'s `|[z^m]p| = q^{1-g-(h-1)(g-1)}` and this proposition's
`-s_D q^{1-g}` agree only at `h=1`, and `s_D` is the untested quantity. Someone should build the
Lorscheid `Z/2×Z/2` quotient and compute `D`, `m_{+1}` and `s_D`.
2. **H-LP, still.** The previous review flagged that H-LP has been inherited unexamined through
three shards; it is now inherited through five. Everything in `thm:renewal-graded-mps`,
`thm:glued-graded-toy` and `thm:frobenius-channel-expander` is a theorem about `(Z,J)`; the
identification of `K` with a geometric wave compression is still an assumption.
3. **The glued toy is not a diagram.** `thm:glued-graded-toy` is a theorem about two abstract exit
contractions. `cit:apw-cusps-pic-no-funnels` says the cusp-plus-funnel diagram is not a lattice
quotient; nobody has checked whether the glued *bond* is the model space of **any** self-adjoint
diagram, or whether the parity `P = 1_{K_+} ⊕ (-1)_{K_-}` has any meaning beyond being declared.
Attack: is there a diagram whose model space carries a `Z`-invariant `Z_2`-grading with `J` block
diagonal? The shard's own `prop:no-selfadjoint-one-mode-exits` is the template for a negative answer.
4. **Aperiodicity in general.** `thm:glued-graded-toy`(ii) says "attracts iff aperiodic" and the
instance is aperiodic; but with `Z_+` carrying only `±q^{-1/2}` and `Z_-` a bipartite spectrum, both
holding laws are supported on even times in isolation. Whether the *glued* law is aperiodic for
every `Ω_+ ⊕ Ω_-` (my instance is one point in that cone) is untested.
5. **The degenerate persistence criterion, properly.** `prop:rebound-persistence-secular` is
registered `proved` for simple eigenvalues only, and both `prop:shared-exit-tradeoff` and
`thm:cusp-renewal-discrete`(e) invoke it where the value is degenerate. The sum criterion I give
above should be promoted to `04h` and the two callers rewritten against it; the Connes–Consani–Moscovici
reading of the secular equation in `04h` depends on the same bookkeeping.
6. **Attainment of the `2+2` exit splitting.** Search self-adjoint two-cusp cores for one whose
`S(z)` is diagonalised by a constant unitary into two channels each carrying one conjugate pair of
the same Klein orbit. A negative answer would strengthen `prop:no-selfadjoint-one-mode-exits`
considerably; a positive one would make the "finest splitting" sentence a theorem.
7. **`asm:h-arith-gamma1` over `F_q[T]`.** This is the only assumption in `04o` doing real work, and
nothing in the repository bears on it — `cit:kk-level-constant-term` is the trivial character at one
cusp. The completed-versus-incomplete branch changes the bond by one odd mode per even character at
the Perron radius, which is exactly the kind of thing that would break "the disc part is odd only".
8. **Get Huxley and Hejhal into `refs/src/`.** `obs:level-tower-correction` is the round's cleanest
correction of an earlier target and it rests on two books that are not in the repository. Until they
are, the `Γ_0(N)`-versus-`Γ_1(N)` dichotomy is a well-argued belief, not a cited fact — and
`conj:galois-graded-bond` is about to be rewritten on the strength of it.
