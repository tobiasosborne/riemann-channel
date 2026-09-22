# The genus-two quotient graph and the H-CLASS test

Author: `codex:gpt-6-astra`

## Ledger

| Claim | Verdict | Result |
|---|---|---|
| Q1 | PROVED | Exact nucleus: 366 vertices, 915 edges, fifteen standard rays; all GL stabilisers and lattice representatives below. |
| Q2 | SHARPENED | H-CLASS proved for this quotient; exact L-ratios, reciprocal convention, 64 arithmetic resonances and 154 model modes. |
| Q3 | SHARPENED | Hyperelliptic pullback gives full weighted-graph inversion; the literal Riemann–Roch degree-reflection fold is refuted. |
| Q4 | SHARPENED | Complete numerical handoff; arithmetic H-CLASS settled here, while the graded-bond fold and metric comparison remain open. |

## Correction ledger

The numbered correction ledger appears under **Corrections to the brief** below; verdicts distinguish the proved graph and scattering from the refuted literal fold and the remaining comparison problem.

## Q1 — PROVED: the complete quotient graph

### Q1.1. The object and the centre

We use `Γ=GL₂(R)` and retain its ineffective centre `F₅×` in every stabiliser order. Thus `S(v)=|Aut(E_v)|`, not `|Aut(E_v)/F₅×|`. Dividing **every** vertex and edge order by four gives the effective projective convention and the identical weighted adjacency. This is the GL convention used by the D3 table (`S(O²)=48` at q=3), `report/sections/04k_elliptic_cavity_scattering.tex:32–43`.

The literal double coset is

`GL₂(R) \ GL₂(K_∞) / (GL₂(O_∞) K_∞×)`.

Its bundles trivialise off infinity and are identified by twists `O(n∞)`. It is not, without justification, the set of all rank-two bundles modulo every line bundle. In the present example the two descriptions **do** agree: the determinant of the restriction to R is a class in A=Z/15, and twisting by a line bundle changes it by twice that class. Multiplication by two on A is bijective, so there is a unique twist making the restriction free; residual twists are precisely `O(n∞)`. Rank-two projective modules over the Dedekind ring R are classified by their determinant. No nontrivial projective self-twist survives, since it would give a 2-torsion class. This proves equality of the quotient and the connected projective-bundle Hecke graph, including stabiliser indices. Lorscheid's exact statements are `refs/src/1012.3513/hecke.tex:384–417`; his explicit distinction from Serre is at `:576–580`: “Serre considers rank 2 bundles that trivialise outside a given place”.

The graph is bipartite by determinant degree modulo two (`1012.3513/hecke.tex:437–443`). Its cusps are the fifteen classes of A. In ratio coordinates write

`c(j,d)=[O ⊕ O(jG+d∞)]`, `j in Z/15`, `d>0`.

In the literal arithmetic cusp convention take a maximal subline of class `a` in a free R-module: its complement has class `−a`, so the ratio class is `j=2a`. We use this maximal-subline convention for the final Fourier labels. APW's displayed convention `L_c ⊕ (O(n∞)L_c⁻¹)` instead calls the *lower* summand c, hence j=−2c (`refs/src/2603.26443/final_draft.tex:884–892`). Either convention is legitimate; silently identifying j and a is not.

### Q1.2. The guaranteed boundary and nucleus

Let `δ(E)=max_L(2 deg L−deg E)` over saturated rational line subbundles. Here `−4≤δ`, and `δ>2` forces splitting. These are Serre, *Trees*, Chapter II, §2.2, Propositions 6 and 7 (**not byte-cited in Serre**), quoted explicitly in `1012.3513/hecke.tex:728–741`. Lorscheid's nucleus is exactly `δ≤3`; each cusp meets it at `c(j,3)` (`:936–970`). The source says “Each vertex ... is at distance ≤(2g_X+m_X+d_x)/d_x from some cusp” (`:965`): at most seven here.

For a positive-degree split ratio D,

`S(c_D)=(5−1)² 5^{h⁰(D)}`,

because every automorphism is upper triangular with two nonzero constant diagonal entries and upper-right entry in `H⁰(D)`. Thus the fifteen heads `c(j,3)` all have S=400; their first exterior vertices `c(j,4)` have S=2000. Every tail edge from d to d+1, d≥3, has S=16·5^{d−1}, and its two indices are `(1,5)`. The coupling at every head is exactly one.

| Family | Number | S(vertex) | Known outward edges |
|---|---:|---:|---|
| c(0,0)=O² | 1 | 480 | to c(0,1), edge S=80, indices (6,1) |
| c(j,0), 1≤j≤7, with j and −j identified | 7 | 16 | one to c(j,1), one to c(−j,1), each outward index 1 |
| c(j,1), j=0,±1 | 3 | 80 | one to c(j,2), outward index 1 |
| c(j,1), other j | 12 | 16 | one to c(j,2), outward index 1 |
| c(0,2) | 1 | 400 | one to c(0,3), outward index 1 |
| c(j,2), j≠0 | 14 | 80 | one to c(j,3), outward index 1 |
| c(j,3), all j | 15 | 400 | one to c(j,4), edge S=400 |
| c(j,d), d≥4 | 15 per d | 16·5^{d−1} | to d−1 and d+1, indices 5 and 1 |

There are therefore **53 decomposable nucleus vertices**, not merely fifteen ray heads. The remaining vertices are indecomposable. The first three h⁰ rows used here are binding E1 (`notes/genus-two-bond/astra-proofs.md:55–85`). The upward-index assertions are precisely Lorscheid `:910–920`; at d=3 the inward neighbours must still be computed, particularly j=0. Tail regularity is only guaranteed for d>3.

### Q1.3. Exact computational certificate

`checks/enumerate_graph.py` uses `t=x²/y`, a uniformiser at infinity, and lattices

`g(n,u) O_∞²`, `g(n,u)=[[t^n,u],[0,1]]`,

where u is a finite Laurent polynomial reduced modulo t^n. The six neighbours are `(n−1,u mod t^{n−1})` and `(n+1,u+a t^n)`, a∈F₅. Ring elements have the exact basis `1,x,x²,…; y,xy,x²y,…`, with distinct pole orders 0,2,4,5,6,7,… . The Laurent expansion is computed from `w=1/x`,

`w=t²(1+w²+w³−2w⁵)`, `y=x²/t`.

For two lattice representatives g,h, parity must agree and `l=(v(det g)−v(det h))/2`. Solve the finite F₅-linear conditions `h⁻¹ A g ∈ t^l Mat₂(O_∞)` for `A∈Mat₂(R)`. Entrywise valuation bounds are obtained from `A=t^l h B g⁻¹`, B integral; thus the search is exhaustive, not a pole-bound guess. Its determinant has valuation at least zero and belongs to R, so it is constant. The lattices are equivalent exactly when this solution space contains an A with nonzero determinant. A quadratic polynomial on an F₅-vector space is identically zero iff it vanishes on each basis vector and each pairwise sum; this makes the invertibility test finite without enumerating all matrices.

For g=h the units in the resulting endomorphism algebra give S(v). The action on the six lines of the fibre at infinity gives individual edge orbits, hence S(e); parallel edge orbits must be kept separately. Breadth-first enumeration starts at O², stops expanding at S=2000 (the δ=4 ray vertices), and verifies all inverse indices. Reduction theory ensures termination and completeness. Both enumeration runs closed with 381 vertices including the fifteen first exterior vertices, and the exact mass below. The orbit audit finds no parallel edges in this example. The observed representatives have −4≤n≤8 and −3≤exponents(u)≤7; neighbour tests use n≤9. The entry pole bound is at most 24, products in the integrality tests have no exponent below −31, and coefficients beyond exponent 32 cannot affect any tested inequality. The Laurent window [−48,48] therefore has a strict exactness margin. It is not a numerical series approximation. An indecomposable with positive δ has a unique maximal subline and automorphism order at most 4·5²=100; for δ≤0 an indecomposable has order at most 24. A split vertex with δ≤3 has order at most 480. Thus the first encountered order-2000 vertices are exactly δ=4, validating the stopping rule independently of a guessed graph size.


### Q1.4. Counts, mass and reproducible adjacency

The cut is **δ=3 at every cusp**. All tables retain the original breadth-first vertex identifiers; the fifteen omitted identifiers are exterior ray vertices, not gaps in the enumeration.

| S(v) | Number of nucleus vertices |
|---:|---:|
| 4 | 278 |
| 16 | 19 |
| 20 | 9 |
| 24 | 25 |
| 80 | 17 |
| 100 | 1 |
| 400 | 16 |
| 480 | 1 |
| **Total** | **366** |

There are **915 nucleus edges**, no loops or parallel edges, and fifteen attaching edges. The nucleus has first Betti number `915−366+1=550`. Of its vertices, 53 are split and 313 are indecomposable. The 25 trace vertices independently agree with `(P_C(−1)−1)/2=(51−1)/2`; the quadratic constant extension has Jacobian order `P_C(1)P_C(−1)=765`. The stabiliser-4 vertices are called scalar-automorphism vertices here; this alone does not assert geometric stability.

**Mass theorem used (external, original proof not byte-cited).** The rank-two Siegel–Weil mass formula for a smooth projective curve gives, for each fixed determinant line bundle Λ, `Σ_{det E≅Λ}1/|Aut(E)|=q^{3(g−1)} ζ_C(2)/(q−1)`. The determinant is fixed up to isomorphism, not equipped with a chosen determinant trivialisation. See André Weil, *Adeles and Algebraic Groups* (1982), Tamagawa-number-one theorem for SL₂; the fixed-determinant/automorphism convention and compact volume are explained in [Lin Weng, “Parabolic Reduction, Stability and the Mass, I. Special Linear Groups”, §2.1](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1826-16.pdf). In our odd-class-number quotient there are two determinant parities and a unique Pic⁰ twist to either fixed determinant. The zeta functional equation therefore gives

`mass_V = 2 ζ_C(−1)/(q−1) = 4637/64`,

`mass_E = (q+1) mass_V/2 = 13911/64`,

`χ_EP(Γ)=mass_V−mass_E=−ζ_C(−1)=−4637/32`.

Indeed `P_C(5)=13911` and `ζ_C(−1)=13911/96=4637/32`. Independently, the **enumerated** nucleus contributes vertex mass `11591/160` and edge mass `3477/16`; the fifteen exterior tails, including attaching edges, contribute respectively `15/1600` and `15/320`. These exact fractions recover the theorem. A mass is not an unweighted vertex count. The GL convention matters: effective PGL stabilisers multiply both masses and χ_EP by four. This also sharpens the convention in `report/sections/04m_elliptic_cavity_sources.tex:33–39`, which writes “−ζ_K(−1)”.

In the following drawing-free table, `u` is encoded as `exponent:coefficient` in F₅, so `−1:1,2:3` means `t⁻¹+3t²`. Empty u means zero. The last column lists **only neighbours with larger identifier**, in the form `neighbour/S(edge)`; every nucleus edge appears exactly once. Together with S(v), its two oriented indices are `S(v)/S(e)` and `S(w)/S(e)`. The lattice representatives are actual vertices of Γ\T, not abstract graph labels.

| Vertex | n | u | S(v) | Larger nucleus neighbours / S(e) |
|---:|---:|---|---:|---|
| 0 | 0 | 0 | 480 | 1/80 |
| 1 | -1 | 0 | 80 | 2/80, 3/20 |
| 2 | -2 | 0 | 400 | 4/400 |
| 3 | 0 | -1:1 | 20 | 5/4 |
| 4 | -3 | 0 | 400 | 7/100 |
| 5 | 1 | -1:1 | 4 | 8/4, 9/4, 10/4, 11/4, 12/4 |
| 7 | -2 | -3:1 | 100 | 13/20 |
| 8 | 2 | -1:1 | 4 | 14/4, 15/4, 16/4, 17/4, 18/4 |
| 9 | 2 | -1:1,1:1 | 4 | 19/4, 20/4, 21/4, 22/4, 23/4 |
| 10 | 2 | -1:1,1:2 | 4 | 24/4, 25/4, 26/4, 27/4, 28/4 |
| 11 | 2 | -1:1,1:3 | 4 | 29/4, 30/4, 31/4, 32/4, 33/4 |
| 12 | 2 | -1:1,1:4 | 4 | 34/4, 35/4, 36/4, 37/4, 38/4 |
| 13 | -1 | -3:1 | 20 | 39/20, 40/20, 41/20, 42/20, 43/20 |
| 14 | 3 | -1:1 | 4 | 44/4, 45/4, 46/4, 47/4, 48/4 |
| 15 | 3 | -1:1,2:1 | 4 | 49/4, 50/4, 51/4, 52/4, 53/4 |
| 16 | 3 | -1:1,2:2 | 4 | 54/4, 55/4, 56/4, 57/4, 58/4 |
| 17 | 3 | -1:1,2:3 | 4 | 54/4, 55/4, 56/4, 59/4, 58/4 |
| 18 | 3 | -1:1,2:4 | 4 | 49/4, 50/4, 51/4, 52/4, 53/4 |
| 19 | 3 | -1:1,1:1 | 4 | 60/4, 61/4, 62/4, 63/4, 64/4 |
| 20 | 3 | -1:1,1:1,2:1 | 4 | 65/4, 66/4, 67/4, 68/4, 69/4 |
| 21 | 3 | -1:1,1:1,2:2 | 4 | 70/4, 71/4, 72/4, 73/4, 74/4 |
| 22 | 3 | -1:1,1:1,2:3 | 4 | 75/4, 71/4, 72/4, 73/4, 74/4 |
| 23 | 3 | -1:1,1:1,2:4 | 4 | 65/4, 66/4, 67/4, 68/4, 69/4 |
| 24 | 3 | -1:1,1:2 | 4 | 76/4, 77/4, 78/4, 79/4, 80/4 |
| 25 | 3 | -1:1,1:2,2:1 | 4 | 81/4, 82/4, 83/4, 84/4, 85/4 |
| 26 | 3 | -1:1,1:2,2:2 | 4 | 86/4, 87/4, 88/4, 89/4, 90/4 |
| 27 | 3 | -1:1,1:2,2:3 | 4 | 91/4, 87/4, 88/4, 89/4, 90/4 |
| 28 | 3 | -1:1,1:2,2:4 | 4 | 81/4, 82/4, 83/4, 84/4, 85/4 |
| 29 | 3 | -1:1,1:3 | 4 | 92/4, 93/4, 94/4, 95/4, 96/4 |
| 30 | 3 | -1:1,1:3,2:1 | 4 | 97/4, 98/4, 99/4, 100/4, 101/4 |
| 31 | 3 | -1:1,1:3,2:2 | 4 | 102/4, 103/4, 104/4, 105/4, 106/4 |
| 32 | 3 | -1:1,1:3,2:3 | 4 | 102/4, 107/4, 104/4, 105/4, 106/4 |
| 33 | 3 | -1:1,1:3,2:4 | 4 | 108/4, 98/4, 99/4, 100/4, 101/4 |
| 34 | 3 | -1:1,1:4 | 4 | 109/4, 110/4, 111/4, 112/4, 113/4 |
| 35 | 3 | -1:1,1:4,2:1 | 4 | 114/4, 115/4, 116/4, 117/4, 118/4 |
| 36 | 3 | -1:1,1:4,2:2 | 4 | 119/4, 120/4, 121/4, 122/4, 123/4 |
| 37 | 3 | -1:1,1:4,2:3 | 4 | 119/4, 120/4, 121/4, 122/4, 123/4 |
| 38 | 3 | -1:1,1:4,2:4 | 4 | 114/4, 115/4, 116/4, 117/4, 118/4 |
| 39 | 0 | -3:1 | 20 | 124/4 |
| 40 | 0 | -3:1,-1:1 | 20 | 125/4 |
| 41 | 0 | -3:1,-1:2 | 20 | 126/4 |
| 42 | 0 | -3:1,-1:3 | 20 | 127/4 |
| 43 | 0 | -3:1,-1:4 | 20 | 128/4 |
| 44 | 4 | -1:1 | 24 | — |
| 45 | 4 | -1:1,3:1 | 4 | 129/4, 130/4, 131/4, 132/4, 133/4 |
| 46 | 4 | -1:1,3:2 | 4 | 134/4, 135/4, 136/4, 137/4, 138/4 |
| 47 | 4 | -1:1,3:3 | 4 | 139/4, 140/4, 141/4, 142/4, 143/4 |
| 48 | 4 | -1:1,3:4 | 24 | — |
| 49 | 4 | -1:1,2:1 | 4 | 144/4, 145/4, 146/4, 147/4 |
| 50 | 4 | -1:1,2:1,3:1 | 4 | 148/4, 149/4, 150/4, 151/4 |
| 51 | 4 | -1:1,2:1,3:2 | 4 | 152/4, 153/4, 154/4, 155/4 |
| 52 | 4 | -1:1,2:1,3:3 | 4 | 156/4, 157/4, 158/4, 159/4 |
| 53 | 4 | -1:1,2:1,3:4 | 4 | 160/4, 161/4, 162/4, 163/4 |
| 54 | 4 | -1:1,2:2 | 4 | 164/4, 165/4, 166/4, 167/4 |
| 55 | 4 | -1:1,2:2,3:1 | 4 | 168/4, 169/4, 170/4, 171/4 |
| 56 | 4 | -1:1,2:2,3:2 | 4 | 172/4, 173/4, 174/4, 175/4 |
| 57 | 4 | -1:1,2:2,3:3 | 4 | 176/4, 177/4, 178/4, 179/4, 180/4 |
| 58 | 4 | -1:1,2:2,3:4 | 4 | 181/4, 182/4, 183/4, 184/4 |
| 59 | 4 | -1:1,2:3,3:3 | 4 | 185/4, 186/4, 187/4, 188/4, 189/4 |
| 60 | 4 | -1:1,1:1 | 24 | — |
| 61 | 4 | -1:1,1:1,3:1 | 4 | 182/4, 190/4, 152/4, 153/4, 191/4 |
| 62 | 4 | -1:1,1:1,3:2 | 4 | 192/4, 135/4, 186/4, 180/4, 138/4 |
| 63 | 4 | -1:1,1:1,3:3 | 24 | — |
| 64 | 4 | -1:1,1:1,3:4 | 4 | 193/4, 194/4, 160/4, 161/4, 195/4 |
| 65 | 4 | -1:1,1:1,2:1 | 4 | 196/4, 197/4, 198/4, 169/4 |
| 66 | 4 | -1:1,1:1,2:1,3:1 | 4 | 199/4, 200/4, 201/4, 202/4 |
| 67 | 4 | -1:1,1:1,2:1,3:2 | 4 | 155/4, 203/4, 204/4, 139/4 |
| 68 | 4 | -1:1,1:1,2:1,3:3 | 4 | 205/4, 134/4, 206/4, 207/4 |
| 69 | 4 | -1:1,1:1,2:1,3:4 | 4 | 208/4, 174/4, 129/4, 209/4 |
| 70 | 4 | -1:1,1:1,2:2 | 4 | 210/4, 211/4, 142/4, 181/4, 212/4 |
| 71 | 4 | -1:1,1:1,2:2,3:1 | 4 | 185/4, 148/4, 176/4, 150/4 |
| 72 | 4 | -1:1,1:1,2:2,3:2 | 4 | 132/4, 146/4, 147/4, 131/4 |
| 73 | 4 | -1:1,1:1,2:2,3:3 | 4 | 213/4, 214/4, 215/4, 216/4 |
| 74 | 4 | -1:1,1:1,2:2,3:4 | 4 | 166/4, 167/4, 217/4, 218/4 |
| 75 | 4 | -1:1,1:1,2:3 | 4 | 219/4, 220/4, 184/4, 141/4, 221/4 |
| 76 | 4 | -1:1,1:2 | 4 | 222/4, 172/4, 214/4, 215/4, 175/4 |
| 77 | 4 | -1:1,1:2,3:1 | 4 | 169/4, 223/4, 146/4, 147/4, 224/4 |
| 78 | 4 | -1:1,1:2,3:2 | 24 | — |
| 79 | 4 | -1:1,1:2,3:3 | 16 | 225/16, 226/16 |
| 80 | 4 | -1:1,1:2,3:4 | 4 | 155/4, 189/4, 217/4, 218/4, 177/4 |
| 81 | 4 | -1:1,1:2,2:1 | 4 | 162/4, 163/4, 166/4, 167/4 |
| 82 | 4 | -1:1,1:2,2:1,3:1 | 4 | 213/4, 183/4, 192/4, 216/4 |
| 83 | 4 | -1:1,1:2,2:1,3:2 | 4 | 188/4, 152/4, 153/4, 178/4 |
| 84 | 4 | -1:1,1:2,2:1,3:3 | 4 | 150/4, 148/4, 174/4, 227/4 |
| 85 | 4 | -1:1,1:2,2:1,3:4 | 4 | 141/4, 142/4, 228/4, 229/4 |
| 86 | 4 | -1:1,1:2,2:2 | 4 | 196/4, 230/4, 132/4, 156/4, 231/4 |
| 87 | 4 | -1:1,1:2,2:2,3:1 | 4 | 209/4, 185/4, 208/4, 176/4 |
| 88 | 4 | -1:1,1:2,2:2,3:2 | 4 | 173/4, 212/4, 220/4, 193/4 |
| 89 | 4 | -1:1,1:2,2:2,3:3 | 4 | 139/4, 170/4, 171/4, 232/4 |
| 90 | 4 | -1:1,1:2,2:2,3:4 | 4 | 138/4, 233/4, 135/4, 234/4 |
| 91 | 4 | -1:1,1:2,2:3 | 4 | 197/4, 235/4, 158/4, 131/4, 236/4 |
| 92 | 4 | -1:1,1:3 | 4 | 168/4, 207/4, 152/4, 153/4, 206/4 |
| 93 | 4 | -1:1,1:3,3:1 | 4 | 139/4, 237/4, 216/4, 213/4, 238/4 |
| 94 | 4 | -1:1,1:3,3:2 | 4 | 193/4, 200/4, 146/4, 147/4, 202/4 |
| 95 | 4 | -1:1,1:3,3:3 | 4 | 222/4, 176/4, 228/4, 229/4, 185/4 |
| 96 | 4 | -1:1,1:3,3:4 | 4 | 174/4, 156/4, 210/4, 219/4, 158/4 |
| 97 | 4 | -1:1,1:3,2:1 | 4 | 239/4, 132/4, 199/4, 177/4, 160/4 |
| 98 | 4 | -1:1,1:3,2:1,3:1 | 4 | 157/4, 234/4, 159/4, 233/4 |
| 99 | 4 | -1:1,1:3,2:1,3:2 | 4 | 154/4, 170/4, 171/4, 192/4 |
| 100 | 4 | -1:1,1:3,2:1,3:3 | 4 | 240/4, 241/4, 166/4, 167/4 |
| 101 | 4 | -1:1,1:3,2:1,3:4 | 4 | 215/4, 136/4, 137/4, 214/4 |
| 102 | 4 | -1:1,1:3,2:2 | 4 | 242/4, 243/4, 198/4, 183/4 |
| 103 | 4 | -1:1,1:3,2:2,3:1 | 4 | 244/4, 163/4, 223/4, 212/4, 186/4 |
| 104 | 4 | -1:1,1:3,2:2,3:2 | 4 | 190/4, 172/4, 191/4, 175/4 |
| 105 | 4 | -1:1,1:3,2:2,3:3 | 4 | 245/4, 231/4, 235/4, 155/4 |
| 106 | 4 | -1:1,1:3,2:2,3:4 | 4 | 149/4, 195/4, 151/4, 194/4 |
| 107 | 4 | -1:1,1:3,2:3,3:1 | 4 | 246/4, 180/4, 220/4, 224/4, 162/4 |
| 108 | 4 | -1:1,1:3,2:4 | 4 | 247/4, 161/4, 189/4, 201/4, 131/4 |
| 109 | 4 | -1:1,1:4 | 4 | 205/4, 234/4, 146/4, 147/4, 233/4 |
| 110 | 4 | -1:1,1:4,3:1 | 4 | 139/4, 172/4, 160/4, 161/4, 175/4 |
| 111 | 4 | -1:1,1:4,3:2 | 4 | 168/4, 220/4, 136/4, 137/4, 212/4 |
| 112 | 4 | -1:1,1:4,3:3 | 4 | 198/4, 130/4, 166/4, 167/4, 133/4 |
| 113 | 4 | -1:1,1:4,3:4 | 4 | 182/4, 151/4, 228/4, 229/4, 149/4 |
| 114 | 4 | -1:1,1:4,2:1 | 4 | 192/4, 173/4, 217/4, 218/4 |
| 115 | 4 | -1:1,1:4,2:1,3:1 | 4 | 157/4, 209/4, 159/4, 208/4 |
| 116 | 4 | -1:1,1:4,2:1,3:2 | 4 | 131/4, 132/4, 248/4, 249/4 |
| 117 | 4 | -1:1,1:4,2:1,3:3 | 4 | 223/4, 150/4, 224/4, 148/4 |
| 118 | 4 | -1:1,1:4,2:1,3:4 | 4 | 219/4, 178/4, 188/4, 210/4 |
| 119 | 4 | -1:1,1:4,2:2 | 4 | 199/4, 184/4, 201/4, 181/4 |
| 120 | 4 | -1:1,1:4,2:2,3:1 | 4 | 197/4, 186/4, 180/4, 196/4 |
| 121 | 4 | -1:1,1:4,2:2,3:2 | 4 | 174/4, 250/4, 242/4, 243/4 |
| 122 | 4 | -1:1,1:4,2:2,3:3 | 4 | 170/4, 171/4, 134/4, 222/4 |
| 123 | 4 | -1:1,1:4,2:2,3:4 | 4 | 165/4, 155/4, 193/4, 164/4 |
| 124 | 1 | -3:1 | 4 | 251/4, 252/4, 253/4, 254/4, 255/4 |
| 125 | 1 | -3:1,-1:1 | 4 | 256/4, 257/4, 258/4, 259/4, 260/4 |
| 126 | 1 | -3:1,-1:2 | 4 | 261/4, 262/4, 263/4, 264/4, 265/4 |
| 127 | 1 | -3:1,-1:3 | 4 | 266/4, 267/4, 268/4, 269/4, 270/4 |
| 128 | 1 | -3:1,-1:4 | 4 | 271/4, 272/4, 273/4, 274/4, 275/4 |
| 129 | 5 | -1:1,3:1 | 4 | 266/4, 276/4, 277/4, 278/4 |
| 130 | 5 | -1:1,3:1,4:1 | 4 | 279/4, 280/4, 281/4, 282/4 |
| 131 | 5 | -1:1,3:1,4:2 | 4 | 251/4 |
| 132 | 5 | -1:1,3:1,4:3 | 4 | 251/4 |
| 133 | 5 | -1:1,3:1,4:4 | 4 | 283/4, 284/4, 281/4, 282/4 |
| 134 | 5 | -1:1,3:2 | 4 | 252/4, 285/4, 286/4 |
| 135 | 5 | -1:1,3:2,4:1 | 4 | 257/4, 287/4, 288/4 |
| 136 | 5 | -1:1,3:2,4:2 | 4 | 272/4, 289/4, 290/4 |
| 137 | 5 | -1:1,3:2,4:3 | 4 | 272/4, 289/4, 290/4 |
| 138 | 5 | -1:1,3:2,4:4 | 4 | 257/4, 287/4, 288/4 |
| 139 | 5 | -1:1,3:3 | 4 | 263/4 |
| 140 | 5 | -1:1,3:3,4:1 | 4 | 253/4, 291/4, 292/4, 293/4, 294/4 |
| 141 | 5 | -1:1,3:3,4:2 | 4 | 273/4, 295/4, 296/4 |
| 142 | 5 | -1:1,3:3,4:3 | 4 | 273/4, 295/4, 296/4 |
| 143 | 5 | -1:1,3:3,4:4 | 4 | 253/4, 291/4, 292/4, 293/4, 294/4 |
| 144 | 5 | -1:1,2:1,4:1 | 4 | 260/4, 285/4, 297/4, 298/4, 291/4 |
| 145 | 5 | -1:1,2:1,4:2 | 4 | 260/4, 298/4, 285/4, 291/4, 297/4 |
| 146 | 5 | -1:1,2:1,4:3 | 4 | 275/4 |
| 147 | 5 | -1:1,2:1,4:4 | 4 | 275/4 |
| 148 | 5 | -1:1,2:1,3:1 | 4 | 279/4, 294/4 |
| 149 | 5 | -1:1,2:1,3:1,4:2 | 4 | 261/4, 299/4, 300/4 |
| 150 | 5 | -1:1,2:1,3:1,4:3 | 4 | 283/4, 294/4 |
| 151 | 5 | -1:1,2:1,3:1,4:4 | 4 | 261/4, 300/4, 299/4 |
| 152 | 5 | -1:1,2:1,3:2 | 4 | 262/4, 277/4 |
| 153 | 5 | -1:1,2:1,3:2,4:1 | 4 | 262/4, 277/4 |
| 154 | 5 | -1:1,2:1,3:2,4:2 | 4 | 267/4, 301/4, 302/4, 303/4 |
| 155 | 5 | -1:1,2:1,3:2,4:4 | 4 | 257/4 |
| 156 | 5 | -1:1,2:1,3:3 | 4 | 258/4, 304/4, 305/4 |
| 157 | 5 | -1:1,2:1,3:3,4:2 | 4 | 263/4, 306/4, 284/4 |
| 158 | 5 | -1:1,2:1,3:3,4:3 | 4 | 258/4, 304/4, 305/4 |
| 159 | 5 | -1:1,2:1,3:3,4:4 | 4 | 263/4, 280/4, 306/4 |
| 160 | 5 | -1:1,2:1,3:4,4:1 | 4 | 259/4, 286/4 |
| 161 | 5 | -1:1,2:1,3:4,4:2 | 4 | 259/4, 286/4 |
| 162 | 5 | -1:1,2:1,3:4,4:3 | 4 | 274/4, 293/4, 307/4 |
| 163 | 5 | -1:1,2:1,3:4,4:4 | 4 | 274/4, 307/4, 293/4 |
| 164 | 5 | -1:1,2:2,4:1 | 4 | 270/4, 304/4, 296/4, 290/4 |
| 165 | 5 | -1:1,2:2,4:2 | 4 | 270/4, 290/4, 304/4, 296/4 |
| 166 | 5 | -1:1,2:2,4:3 | 4 | 265/4 |
| 167 | 5 | -1:1,2:2,4:4 | 4 | 265/4 |
| 168 | 5 | -1:1,2:2,3:1 | 4 | 251/4, 308/4, 309/4 |
| 169 | 5 | -1:1,2:2,3:1,4:1 | 4 | 261/4, 310/4, 288/4 |
| 170 | 5 | -1:1,2:2,3:1,4:2 | 4 | 283/4, 307/4 |
| 171 | 5 | -1:1,2:2,3:1,4:4 | 4 | 279/4, 307/4 |
| 172 | 5 | -1:1,2:2,3:2 | 4 | 267/4, 298/4 |
| 173 | 5 | -1:1,2:2,3:2,4:1 | 4 | 262/4, 281/4, 311/4 |
| 174 | 5 | -1:1,2:2,3:2,4:2 | 4 | 272/4 |
| 175 | 5 | -1:1,2:2,3:2,4:3 | 4 | 267/4, 298/4 |
| 176 | 5 | -1:1,2:2,3:3 | 4 | 268/4, 297/4 |
| 177 | 5 | -1:1,2:2,3:3,4:1 | 4 | 273/4, 312/4, 299/4 |
| 178 | 5 | -1:1,2:2,3:3,4:2 | 4 | 253/4, 282/4, 289/4 |
| 179 | 5 | -1:1,2:2,3:3,4:3 | 16 | 313/16, 314/16 |
| 180 | 5 | -1:1,2:2,3:3,4:4 | 4 | 263/4, 315/4 |
| 181 | 5 | -1:1,2:2,3:4,4:1 | 4 | 254/4, 287/4, 280/4 |
| 182 | 5 | -1:1,2:2,3:4,4:2 | 4 | 274/4, 316/4, 285/4 |
| 183 | 5 | -1:1,2:2,3:4,4:3 | 4 | 259/4, 317/4, 292/4 |
| 184 | 5 | -1:1,2:2,3:4,4:4 | 4 | 254/4, 284/4, 287/4 |
| 185 | 5 | -1:1,2:3,3:3 | 4 | 268/4, 297/4 |
| 186 | 5 | -1:1,2:3,3:3,4:1 | 4 | 263/4, 315/4 |
| 187 | 5 | -1:1,2:3,3:3,4:2 | 16 | 318/16, 314/16 |
| 188 | 5 | -1:1,2:3,3:3,4:3 | 4 | 253/4, 282/4, 289/4 |
| 189 | 5 | -1:1,2:3,3:3,4:4 | 4 | 273/4, 312/4, 299/4 |
| 190 | 5 | -1:1,1:1,3:1,4:1 | 4 | 290/4, 279/4, 312/4, 319/4 |
| 191 | 5 | -1:1,1:1,3:1,4:4 | 4 | 290/4, 283/4, 312/4, 319/4 |
| 192 | 5 | -1:1,1:1,3:2 | 4 | 320/4, 275/4 |
| 193 | 5 | -1:1,1:1,3:4 | 4 | 253/4, 321/4 |
| 194 | 5 | -1:1,1:1,3:4,4:1 | 4 | 297/4, 280/4, 272/4, 322/4 |
| 195 | 5 | -1:1,1:1,3:4,4:4 | 4 | 297/4, 284/4, 272/4, 322/4 |
| 196 | 5 | -1:1,1:1,2:1 | 4 | 267/4, 294/4, 322/4 |
| 197 | 5 | -1:1,1:1,2:1,4:1 | 4 | 267/4, 322/4, 294/4 |
| 198 | 5 | -1:1,1:1,2:1,4:2 | 4 | 273/4, 323/4, 321/4 |
| 199 | 5 | -1:1,1:1,2:1,3:1 | 4 | 291/4, 262/4, 324/4 |
| 200 | 5 | -1:1,1:1,2:1,3:1,4:1 | 4 | 325/4, 295/4, 279/4, 315/4 |
| 201 | 5 | -1:1,1:1,2:1,3:1,4:3 | 4 | 291/4, 262/4, 324/4 |
| 202 | 5 | -1:1,1:1,2:1,3:1,4:4 | 4 | 325/4, 283/4, 315/4, 295/4 |
| 203 | 5 | -1:1,1:1,2:1,3:2,4:1 | 4 | 282/4, 300/4, 326/4, 305/4, 275/4 |
| 204 | 5 | -1:1,1:1,2:1,3:2,4:3 | 4 | 305/4, 326/4, 300/4, 282/4, 275/4 |
| 205 | 5 | -1:1,1:1,2:1,3:3 | 4 | 314/4, 258/4, 301/4, 327/4 |
| 206 | 5 | -1:1,1:1,2:1,3:3,4:2 | 4 | 293/4, 270/4, 284/4, 320/4 |
| 207 | 5 | -1:1,1:1,2:1,3:3,4:4 | 4 | 270/4, 293/4, 320/4, 280/4 |
| 208 | 5 | -1:1,1:1,2:1,3:4,4:1 | 4 | 328/4, 296/4, 259/4 |
| 209 | 5 | -1:1,1:1,2:1,3:4,4:4 | 4 | 328/4, 259/4, 296/4 |
| 210 | 5 | -1:1,1:1,2:2 | 4 | 261/4, 319/4, 286/4 |
| 211 | 5 | -1:1,1:1,2:2,4:1 | 16 | 329/16, 302/16 |
| 212 | 5 | -1:1,1:1,2:2,4:4 | 4 | 260/4, 326/4 |
| 213 | 5 | -1:1,1:1,2:2,3:3 | 4 | 252/4, 322/4, 312/4 |
| 214 | 5 | -1:1,1:1,2:2,3:3,4:2 | 4 | 321/4, 258/4, 277/4 |
| 215 | 5 | -1:1,1:1,2:2,3:3,4:3 | 4 | 277/4, 258/4, 321/4 |
| 216 | 5 | -1:1,1:1,2:2,3:3,4:4 | 4 | 252/4, 312/4, 322/4 |
| 217 | 5 | -1:1,1:1,2:2,3:4,4:3 | 4 | 285/4, 325/4, 266/4 |
| 218 | 5 | -1:1,1:1,2:2,3:4,4:4 | 4 | 325/4, 266/4, 285/4 |
| 219 | 5 | -1:1,1:1,2:3 | 4 | 261/4, 319/4, 286/4 |
| 220 | 5 | -1:1,1:1,2:3,4:1 | 4 | 260/4, 326/4 |
| 221 | 5 | -1:1,1:1,2:3,4:4 | 16 | 330/16, 302/16 |
| 222 | 5 | -1:1,1:2 | 4 | 326/4, 292/4, 265/4 |
| 223 | 5 | -1:1,1:2,3:1,4:1 | 4 | 304/4, 324/4, 252/4 |
| 224 | 5 | -1:1,1:2,3:1,4:4 | 4 | 304/4, 324/4, 252/4 |
| 225 | 5 | -1:1,1:2,3:3,4:1 | 16 | 284/4, 331/16 |
| 226 | 5 | -1:1,1:2,3:3,4:4 | 16 | 280/4, 332/16 |
| 227 | 5 | -1:1,1:2,2:1,3:3,4:4 | 4 | 333/4, 270/4, 334/4, 288/4, 326/4 |
| 228 | 5 | -1:1,1:2,2:1,3:4,4:3 | 4 | 257/4, 324/4, 306/4 |
| 229 | 5 | -1:1,1:2,2:1,3:4,4:4 | 4 | 257/4, 324/4, 306/4 |
| 230 | 5 | -1:1,1:2,2:2,4:1 | 20 | 335/20 |
| 231 | 5 | -1:1,1:2,2:2,4:4 | 4 | 320/4, 289/4, 295/4, 265/4 |
| 232 | 5 | -1:1,1:2,2:2,3:3,4:4 | 4 | 336/4, 254/4, 277/4, 337/4, 299/4 |
| 233 | 5 | -1:1,1:2,2:2,3:4,4:2 | 4 | 266/4, 292/4, 319/4 |
| 234 | 5 | -1:1,1:2,2:2,3:4,4:4 | 4 | 266/4, 292/4, 319/4 |
| 235 | 5 | -1:1,1:2,2:3,4:1 | 4 | 320/4, 289/4, 295/4, 265/4 |
| 236 | 5 | -1:1,1:2,2:3,4:4 | 20 | 338/20 |
| 237 | 5 | -1:1,1:3,3:1,4:1 | 4 | 288/4, 328/4, 274/4, 281/4, 301/4 |
| 238 | 5 | -1:1,1:3,3:1,4:4 | 4 | 288/4, 328/4, 274/4, 281/4, 301/4 |
| 239 | 5 | -1:1,1:3,2:1 | 16 | 339/16, 333/16 |
| 240 | 5 | -1:1,1:3,2:1,3:3 | 4 | 315/4, 328/4, 298/4, 305/4, 254/4 |
| 241 | 5 | -1:1,1:3,2:1,3:3,4:1 | 4 | 328/4, 305/4, 315/4, 298/4, 254/4 |
| 242 | 5 | -1:1,1:3,2:2 | 4 | 251/4, 301/4, 325/4, 306/4 |
| 243 | 5 | -1:1,1:3,2:2,4:2 | 4 | 301/4, 251/4, 306/4, 325/4 |
| 244 | 5 | -1:1,1:3,2:2,3:1 | 16 | 278/16, 340/16 |
| 245 | 5 | -1:1,1:3,2:2,3:3 | 4 | 281/4, 286/4, 341/4, 342/4, 268/4 |
| 246 | 5 | -1:1,1:3,2:3,3:1 | 16 | 278/16, 343/16 |
| 247 | 5 | -1:1,1:3,2:4 | 16 | 344/16, 333/16 |
| 248 | 5 | -1:1,1:4,2:1,3:2,4:3 | 4 | 321/4, 268/4, 287/4, 307/4, 300/4 |
| 249 | 5 | -1:1,1:4,2:1,3:2,4:4 | 4 | 300/4, 268/4, 307/4, 321/4, 287/4 |
| 250 | 5 | -1:1,1:4,2:2,3:2,4:1 | 4 | 299/4, 260/4, 345/4, 346/4, 320/4 |
| 251 | 2 | -3:1 | 4 | — |
| 252 | 2 | -3:1,1:1 | 4 | — |
| 253 | 2 | -3:1,1:2 | 4 | — |
| 254 | 2 | -3:1,1:3 | 4 | — |
| 255 | 2 | -3:1,1:4 | 24 | — |
| 256 | 2 | -3:1,-1:1 | 16 | 347/16, 348/16 |
| 257 | 2 | -3:1,-1:1,1:1 | 4 | — |
| 258 | 2 | -3:1,-1:1,1:2 | 4 | — |
| 259 | 2 | -3:1,-1:1,1:3 | 4 | — |
| 260 | 2 | -3:1,-1:1,1:4 | 4 | — |
| 261 | 2 | -3:1,-1:2 | 4 | — |
| 262 | 2 | -3:1,-1:2,1:1 | 4 | — |
| 263 | 2 | -3:1,-1:2,1:2 | 4 | — |
| 264 | 2 | -3:1,-1:2,1:3 | 24 | — |
| 265 | 2 | -3:1,-1:2,1:4 | 4 | — |
| 266 | 2 | -3:1,-1:3 | 4 | — |
| 267 | 2 | -3:1,-1:3,1:1 | 4 | — |
| 268 | 2 | -3:1,-1:3,1:2 | 4 | — |
| 269 | 2 | -3:1,-1:3,1:3 | 24 | — |
| 270 | 2 | -3:1,-1:3,1:4 | 4 | — |
| 271 | 2 | -3:1,-1:4 | 24 | — |
| 272 | 2 | -3:1,-1:4,1:1 | 4 | — |
| 273 | 2 | -3:1,-1:4,1:2 | 4 | — |
| 274 | 2 | -3:1,-1:4,1:3 | 4 | — |
| 275 | 2 | -3:1,-1:4,1:4 | 4 | — |
| 276 | 6 | -1:1,3:1,5:1 | 24 | — |
| 277 | 6 | -1:1,3:1,5:3 | 4 | — |
| 278 | 6 | -1:1,3:1,5:4 | 16 | — |
| 279 | 6 | -1:1,3:1,4:1 | 4 | 347/4 |
| 280 | 6 | -1:1,3:1,4:1,5:1 | 4 | — |
| 281 | 6 | -1:1,3:1,4:1,5:2 | 4 | — |
| 282 | 6 | -1:1,3:1,4:1,5:4 | 4 | — |
| 283 | 6 | -1:1,3:1,4:4 | 4 | 348/4 |
| 284 | 6 | -1:1,3:1,4:4,5:1 | 4 | — |
| 285 | 6 | -1:1,3:2,5:2 | 4 | — |
| 286 | 6 | -1:1,3:2,5:3 | 4 | — |
| 287 | 6 | -1:1,3:2,4:1,5:2 | 4 | — |
| 288 | 6 | -1:1,3:2,4:1,5:4 | 4 | — |
| 289 | 6 | -1:1,3:2,4:2,5:1 | 4 | — |
| 290 | 6 | -1:1,3:2,4:2,5:3 | 4 | — |
| 291 | 6 | -1:1,3:3,4:1,5:1 | 4 | — |
| 292 | 6 | -1:1,3:3,4:1,5:2 | 4 | — |
| 293 | 6 | -1:1,3:3,4:1,5:3 | 4 | — |
| 294 | 6 | -1:1,3:3,4:1,5:4 | 4 | — |
| 295 | 6 | -1:1,3:3,4:2,5:3 | 4 | — |
| 296 | 6 | -1:1,3:3,4:2,5:4 | 4 | — |
| 297 | 6 | -1:1,2:1,4:1,5:2 | 4 | — |
| 298 | 6 | -1:1,2:1,4:1,5:3 | 4 | — |
| 299 | 6 | -1:1,2:1,3:1,4:2,5:3 | 4 | — |
| 300 | 6 | -1:1,2:1,3:1,4:2,5:4 | 4 | — |
| 301 | 6 | -1:1,2:1,3:2,4:2,5:1 | 4 | — |
| 302 | 6 | -1:1,2:1,3:2,4:2,5:2 | 16 | — |
| 303 | 6 | -1:1,2:1,3:2,4:2,5:3 | 24 | — |
| 304 | 6 | -1:1,2:1,3:3,5:2 | 4 | — |
| 305 | 6 | -1:1,2:1,3:3,5:3 | 4 | — |
| 306 | 6 | -1:1,2:1,3:3,4:2,5:3 | 4 | — |
| 307 | 6 | -1:1,2:1,3:4,4:3,5:4 | 4 | — |
| 308 | 6 | -1:1,2:2,3:1,5:1 | 24 | — |
| 309 | 6 | -1:1,2:2,3:1,5:2 | 24 | — |
| 310 | 6 | -1:1,2:2,3:1,4:1,5:1 | 24 | — |
| 311 | 6 | -1:1,2:2,3:2,4:1,5:4 | 24 | — |
| 312 | 6 | -1:1,2:2,3:3,4:1,5:2 | 4 | — |
| 313 | 6 | -1:1,2:2,3:3,4:3 | 80 | 349/80 |
| 314 | 6 | -1:1,2:2,3:3,4:3,5:1 | 16 | — |
| 315 | 6 | -1:1,2:2,3:3,4:4,5:3 | 4 | — |
| 316 | 6 | -1:1,2:2,3:4,4:2,5:1 | 16 | 350/16, 351/16 |
| 317 | 6 | -1:1,2:2,3:4,4:3,5:2 | 24 | — |
| 318 | 6 | -1:1,2:3,3:3,4:2 | 80 | 352/80 |
| 319 | 6 | -1:1,1:1,3:1,4:1,5:4 | 4 | — |
| 320 | 6 | -1:1,1:1,3:2,5:1 | 4 | — |
| 321 | 6 | -1:1,1:1,3:4,5:4 | 4 | — |
| 322 | 6 | -1:1,1:1,3:4,4:1,5:4 | 4 | — |
| 323 | 6 | -1:1,1:1,2:1,4:2,5:2 | 24 | — |
| 324 | 6 | -1:1,1:1,2:1,3:1,5:3 | 4 | — |
| 325 | 6 | -1:1,1:1,2:1,3:1,4:1 | 4 | — |
| 326 | 6 | -1:1,1:1,2:1,3:2,4:1,5:2 | 4 | — |
| 327 | 6 | -1:1,1:1,2:1,3:3,5:4 | 24 | — |
| 328 | 6 | -1:1,1:1,2:1,3:4,4:1 | 4 | — |
| 329 | 6 | -1:1,1:1,2:2,4:1 | 80 | 353/80 |
| 330 | 6 | -1:1,1:1,2:3,4:4 | 80 | 354/80 |
| 331 | 6 | -1:1,1:2,3:3,4:1,5:1 | 80 | 355/80 |
| 332 | 6 | -1:1,1:2,3:3,4:4,5:1 | 80 | 356/80 |
| 333 | 6 | -1:1,1:2,2:1,3:3,4:4 | 16 | — |
| 334 | 6 | -1:1,1:2,2:1,3:3,4:4,5:2 | 24 | — |
| 335 | 6 | -1:1,1:2,2:2,4:1,5:4 | 80 | 357/80, 351/80 |
| 336 | 6 | -1:1,1:2,2:2,3:3,4:4 | 24 | — |
| 337 | 6 | -1:1,1:2,2:2,3:3,4:4,5:3 | 24 | — |
| 338 | 6 | -1:1,1:2,2:3,4:4,5:4 | 80 | 350/80, 358/80 |
| 339 | 6 | -1:1,1:3,2:1,5:1 | 80 | 359/80 |
| 340 | 6 | -1:1,1:3,2:2,3:1,5:2 | 80 | 360/80 |
| 341 | 6 | -1:1,1:3,2:2,3:3,5:2 | 24 | — |
| 342 | 6 | -1:1,1:3,2:2,3:3,5:3 | 24 | — |
| 343 | 6 | -1:1,1:3,2:3,3:1,5:2 | 80 | 361/80 |
| 344 | 6 | -1:1,1:3,2:4,5:1 | 80 | 362/80 |
| 345 | 6 | -1:1,1:4,2:2,3:2,4:1,5:2 | 24 | — |
| 346 | 6 | -1:1,1:4,2:2,3:2,4:1,5:3 | 24 | — |
| 347 | 3 | -3:1,-1:1,2:1 | 16 | 363/16 |
| 348 | 3 | -3:1,-1:1,2:4 | 16 | 364/16 |
| 349 | 7 | -1:1,2:2,3:3,4:3,6:3 | 400 | — |
| 350 | 7 | -1:1,2:2,3:4,4:2,5:1 | 80 | — |
| 351 | 7 | -1:1,2:2,3:4,4:2,5:1,6:3 | 80 | — |
| 352 | 7 | -1:1,2:3,3:3,4:2,6:2 | 400 | — |
| 353 | 7 | -1:1,1:1,2:2,4:1,6:1 | 400 | — |
| 354 | 7 | -1:1,1:1,2:3,4:4,6:4 | 400 | — |
| 355 | 7 | -1:1,1:2,3:3,4:1,5:1,6:2 | 400 | — |
| 356 | 7 | -1:1,1:2,3:3,4:4,5:1,6:3 | 400 | — |
| 357 | 7 | -1:1,1:2,2:2,4:1,5:4,6:1 | 400 | — |
| 358 | 7 | -1:1,1:2,2:3,4:4,5:4,6:4 | 400 | — |
| 359 | 7 | -1:1,1:3,2:1,5:1,6:2 | 400 | — |
| 360 | 7 | -1:1,1:3,2:2,3:1,5:2,6:1 | 400 | — |
| 361 | 7 | -1:1,1:3,2:3,3:1,5:2,6:4 | 400 | — |
| 362 | 7 | -1:1,1:3,2:4,5:1,6:3 | 400 | — |
| 363 | 4 | -3:1,-1:1,2:1 | 80 | 377/80 |
| 364 | 4 | -3:1,-1:1,2:4 | 80 | 378/80 |
| 377 | 5 | -3:1,-1:1,2:1,4:1 | 400 | — |
| 378 | 5 | -3:1,-1:1,2:4,4:4 | 400 | — |


### Q1.5. Every ray attachment and its class

| Cusp a | Ratio class j=2a mod 15 | Head c(j,3), S=400 | First exterior vertex, S=2000 | Edge S |
|---:|---:|---:|---:|---:|
| 0 | 0 | 4 | 6 | 400 |
| 1 | 2 | 378 | 380 | 400 |
| 2 | 4 | 356 | 370 | 400 |
| 3 | 6 | 354 | 368 | 400 |
| 4 | 8 | 360 | 374 | 400 |
| 5 | 10 | 349 | 365 | 400 |
| 6 | 12 | 362 | 376 | 400 |
| 7 | 14 | 357 | 371 | 400 |
| 8 | 1 | 358 | 372 | 400 |
| 9 | 3 | 359 | 373 | 400 |
| 10 | 5 | 352 | 366 | 400 |
| 11 | 7 | 361 | 375 | 400 |
| 12 | 9 | 353 | 367 | 400 |
| 13 | 11 | 355 | 369 | 400 |
| 14 | 13 | 377 | 379 | 400 |

From each first exterior vertex append one infinite ray: subsequent vertex orders are `2000·5^r`, r=0,1,…; the edge from r to r+1 has the smaller endpoint's order. Thus every ray vertex has degree indices 5+1=6, and every core head has c²=1.

The class labels are computed independently of scattering. A nonzero nilpotent in `End(E)` at a split tail vertex has image the unique maximal line. If its nonzero column is `(a,b)∈R²`, the saturated line module is `(a,b)⁻¹·(a,b)^t`; its Pic(R) class is the effective common-zero divisor class of a and b. Hermite reduction of the ideal `(a,b)` as an F₅[x]-module gives its Mumford pair, then Cantor reduction identifies it with one of the fifteen binding E1 classes. `checks/analyse_graph.py` implements this and obtains every class exactly once. It uses the generator `(x−1,1)`, so the table is not a fitted permutation of Fourier channels.

The machine-readable table is `checks/graph_data.py` (381 lattice representatives, stabilisers, individual edges and aggregated oriented adjacency); exclude `TAILS` for the 366-vertex nucleus. The source algorithm and this printed table are two routes to rebuilding the same graph. In the notebook's `scripts/elliptic_cavity.py:141–161`, supply the core stabiliser dictionary, the 915 edge triples and the fifteen `(head,400,2000)` cusp triples. No changes to that script are needed for these data; its assignment-style edge builder is safe here because there are no parallel edges.

## Q2 — SHARPENED: H-CLASS holds, with the reciprocal and cusp-label conventions fixed

### Q2.1. The exact fifteen-by-fifteen answer

Put `P(T)=1−3T+7T²−15T³+25T⁴`, `Z(T)=P(T)/((1−T)(1−5T))`, `ζ=exp(2πi/15)`, and

`L_k(T)=1+(1+ζ^k+ζ^(−k))T+5T²`, `1≤k≤14`.

These are binding E1–E2, `notes/genus-two-bond/astra-proofs.md:33–37,93–132`; in particular `L_k=L_(15−k)`. Index the exits by the maximal-subline ideal classes **a** in Q1.5, and put

\[
 m_0(z)=\frac{z^6}{5}\frac{Z(z^2)}{Z(z^2/5)}
       =\frac{z^6}{5}\frac{P(z^2)}{P(z^2/5)}\frac{1-z^2/5}{1-5z^2},
 \qquad
 m_k(z)=\frac{z^6}{5}\frac{L_k(z^2)}{L_k(z^2/5)}\quad(k\ne0).
\]

Define `f(j)=15⁻¹ Σ_(k=0)^14 m_k ζ^{kj}`. Since `m_k=m_(−k)`, f is even. The **actual graph scattering matrix** is

\[
 \boxed{\quad S_{ab}(z)=f(a+b),\qquad S=M P_{\rm inv},\quad
 M_{ab}=f(b-a),\quad (P_{\rm inv}u)_a=u_{-a}.\quad}
\]

This specifies every entry, with no undetermined scalar, local factor or cusp permutation. The Fourier matrix `F_(ka)=ζ^(−ka)/√15` gives one scalar block m₀ and the seven blocks, ordered `(k,15−k)`, k=1,…,7,

\[
 \begin{pmatrix}0&m_k\\m_k&0\end{pmatrix}.
\]

Their eigenvalues are `+m_k,−m_k`. Here a further constant change to symmetric and antisymmetric inverse-character vectors diagonalises the blocks because the fourteen L-functions occur in equal inverse pairs. In ratio-class coordinates **j**, rather than ideal-class coordinates a, the character k carries `L_(2k)`. Doubling permutes all fourteen nontrivial factors, but it is essential for identifying a particular channel with the binding morning-lane label.

For `z=5^{s−1/2}` the same formula is

\[
 m_k(z)=5z^6\frac{L(2s,\chi_k)}{L(2s-1,\chi_k)},
\]

with ζ_C in place of L for k=0. Thus the **group-matrix assertion is PROVED for this curve**; the literal ratio direction in `report/sections/04k_elliptic_cavity_scattering.tex:299–301` is **REFUTED in its own incoming/outgoing convention**. It describes the inverse scattering convention. This agrees with the explicit reciprocal already present at `04k:162–167` and `04i_cusp_graph_scattering.tex:103–110`.

### Q2.2. Proof from constant terms, including every normalising factor

1. **External analytic input, precisely stated.** For GL₂ over a global function field, the spherical Eisenstein series induced from the unramified ratio character `ν |·|^{s−1/2}` is meromorphic in s, is an eigenfunction of the degree-one adjacency with eigenvalue `5^s+5^{1−s}`, and has constant term `f_s+M(s)f_s`; the second term belongs to the inverse inducing character. The difference between the Eisenstein series and its constant term is compactly supported in the cusp direction. These statements are byte-supported in `refs/src/1012.3223/main.tex:213–219,349–370,563–568,1023`; the original Langlands/Mœglin–Waldspurger constant-term and continuation theorems are **not byte-cited**. The source's words at `:219` are “the function f−f_N has compact support”. We use the unnormalised sum rather than Lorscheid's additional `L(χ²,1)` normalisation; multiplying an Eisenstein eigenfunction by a scalar does not change its ratio of outgoing to incoming coefficients.

2. **Compute the local intertwiner.** At a place of residue size Q, give O additive volume one, put `b=ν(π)^2 Q^{1−2s}`, and decompose the integral over `|u|≤1` and the shells `|u|=Q^n`. Its value at the spherical vector is

   `1+(1−Q⁻¹) Σ_(n≥1)b^n = (1−ν(π)^2 Q^(−2s))/(1−ν(π)^2 Q^(1−2s))`.

   This is the local `L(2s−1,ν²)/L(2s,ν²)` factor. The square on the inducing character is forced by the root of GL₂; it is not a speculative change of labels.

3. **Compute the global constant.** With local additive O-volumes one, the additive adelic quotient has volume `q^{g−1}`. Equivalently, the Haar measure giving `K\A` volume one gives the product of integral adeles volume `q^{1−g}`. This is the additive adelic Riemann–Roch volume identity (**external standard theorem, original proof not byte-cited**). Multiplying the local integrals therefore gives

   `c_ν(s)=5^(1−g) L(2s−1,ν²)/L(2s,ν²) = (1/5) L(2s−1,ν²)/L(2s,ν²)`.

   The same calculation for the trivial character uses the full zeta function, including its two poles. No infinity factor is omitted: infinity has ν(∞)=1 and appears in the product.

4. **Pass to the graph and fix the cut.** At `c(j,d)`, d sufficiently large, the two terms are

   `ν(j) 5^{sd} + c_ν(s) ν(j)⁻¹ 5^{(1−s)d}`.

   Division by `√S(c(j,d))=4·5^{(d−1)/2}` changes these into a common constant times

   `ν(j) z^d + c_ν(s) ν(j)⁻¹ z^(−d)`.

   The cusp recurrence `(Af)(d)=f(d+1)+5f(d−1)` extends this exact expression down to d=3. With ray coordinate r=d−3, outgoing/incoming coefficients have ratio `z⁶/c_ν(s)`. The fifteen incoming vectors span all exit data for generic s; the finite-core scattering problem has a unique solution there. Meromorphic continuation proves the resulting matrix identity everywhere. Core cusp eigenfunctions cannot alter the ray coefficients.

5. **Identify the character seen by the physical cusp.** Its ratio is j=2a, so `ν(j)=ν²(a)`. Because A has odd order, every class character χ is uniquely ν². The coefficient in channel χ is consequently `5z⁶ L(2s,χ)/L(2s−1,χ)`, rather than an unlabelled `L(χ²)` substitute. In the alternate APW lower-summand convention the label is inverted, which makes no difference to this curve's equal inverse-pair factors.

6. **Convert to the tree variable.** E2 proves `L(T,χ)=5T² L(1/(5T),χ⁻¹)`; Z satisfies the identical genus-two functional equation. Substituting `T=z⁻²` and `T=z⁻²/5` gives the formula in Q2.1. In particular `m_k(z)m_k(1/z)=1`, the nontrivial m_k have modulus one on the unit circle, and the trivial block has precisely the Perron poles `z=±1/√5`. This also independently calibrates the scalar: at genus zero the same calculation is the Nagao answer `(z²−q)/(qz²−1)`, and at genus one/d=1 it is the notebook's factor z².

No transitive geometric action of Pic⁰ on the graph was assumed in this proof. The group matrix comes from the character dependence of the constant term. This resolves exactly the transfer gap noted at `04k:293–300` for the present odd-class-number example.

### Q2.3. Core formula, determinant, and the full unreduced p

Build the 366×366 oriented integer adjacency A from Q1 and set

`T_X = 5^(−1/2) diag(S)^(−1/2) A diag(S)^(1/2)`,

`W_(v,a)=1` at the head of cusp a and zero elsewhere, `C=WW*`,

`Γ(z)=W* ((z+z⁻¹)I−T_X)⁻¹ W`.

Then, exactly in `thm:multi-exit-scattering`, `report/sections/04k_elliptic_cavity_scattering.tex:88–107`,

`S=(zΓ−I)⁻¹(I−z⁻¹Γ)`,

`p=det((1+z²)I−zT_X−C)`, `ptilde=z^732 p(1/z)`,

\[
 \boxed{\det S=-\frac{p}{\widetilde p}
 =-\frac{z^{90}}{5^{15}}\frac{P_Y(z^2)}{P_Y(z^2/5)}
                 \frac{1-z^2/5}{1-5z^2}.}
\]

Here the determinant of inversion is `(−1)^7=−1`, and

`P_Y(T)=P(T)(1+5T²)²(1+T+9T²+5T³+25T⁴)²`

`          ×(1+5T+25T²+70T³+195T⁴+350T⁵+625T⁶+625T⁷+625T⁸)²`.

This is precisely the genus-16 numerator of binding E2 (`notes/genus-two-bond/astra-proofs.md:145–157`).

There is also a complete specification of the **unreduced**, degree-732 polynomial, including all invisible modes:

\[
 \boxed{p(z)=5^{-16}z^{90}(z^2-5)(z^2-1)^7 P_Y(z^2)D_c(z),\qquad
 D_c(z)=\prod_{\lambda\in\operatorname{spec}(T_X|X_c)}(1-\lambda z+z^2).}
\]

`dim X_c=281`, so `deg D_c=562`, `D_c(0)=1`, and D_c is monic reciprocal. To make D_c reproducible without a 156-degree coefficient dump, the following finite-polynomial specification uses only the printed adjacency matrix. Let X denote the **unnormalised** adjacency eigenvalue, put r=X²/5−2 and

`B_0(X)=X⁸−63X⁶+1157X⁴−6870X²+7650`,

`B_+(X,a)=25(5r³+a r²−14r−2a)`,

`B_−(X,a)=5X(5r²+a r−4)`,

`H(a)=a(a²−a−1)(a⁴−5a³+5a²+5a−5)`.

Then

`χ_b(X)=B_0(X) Res_a(H(a), B_+(X,a) B_−(X,a))`,

`χ_c(X)=det(XI−A)/χ_b(X)`,

`D_c(z)=z^281 5^(−281/2) χ_c(√5(z+z⁻¹))`.

The quotient is exact in Z[X]; the apparently radical last expression is an even polynomial in Q[z]. `checks/spectral_data.py` additionally contains every coefficient in factored form. Exact computation gives

`χ_c(X)=X^123 (X²−20) H_156(X)`,

where H_156 is the monic degree-156 factor specified by that quotient and the coefficient list. In particular D_c contains `(1+z²)^123 (z²−1)²`: **there are two compactly supported threshold eigenfunctions**, in addition to the visible half-bound states. They must not be counted as half-bound states or resonances of S.

**Proof/certificate of the multiplicities.** The script selects a Krylov basis of `span{A^j e_head}` using modular pivots, then verifies `A K=K B` over Q, with K of exact rank 85. This proves both minimal visibility and `dim X_c=366−85=281`; it is not a rank decision made only in floating point. The exact characteristic polynomial of B agrees with χ_b above. The factors B_± follow directly by writing the scalar boundary resolvent as `z(1±m_k)/(1±z²m_k)` and replacing `z²+z⁻²` by r; B_0 follows in the same way from m₀. For each nontrivial inverse pair the visible core dimensions are 6 and 5, and the trivial block has dimension 8: `8+7(6+5)=85`. There are seven visible half-bound states at each threshold because S(±1) has +1 multiplicity seven; its −1 multiplicity is eight. Thus the visible p has degree 170, consisting of delay degree 90, arithmetic degree 64, bound reciprocal degree 2 and threshold degree 14. These account for all 170 degrees and fix the displayed monic factorisation. The exact graph determinants at `z=√5/10` and `z=√5/3` independently verify both p itself and p/ptilde.

### Q2.4. Zeros, exits, modes and cut dependence

| Object | Count at the δ=3 cut |
|---|---:|
| Geometric exits | 15 |
| Trivial-channel arithmetic zeros in T | 4 |
| Nontrivial-character arithmetic zeros in T, with multiplicity | 28 |
| Arithmetic resonances in z, with multiplicity | 64 |
| Delay modes, six per Fourier coordinate | 90 |
| Visible bound poles | 2 |
| Visible half-bound states, both thresholds together | 14 |
| Invisible core eigenvectors | 281 |
| Visible core dimension | 85 |
| `deg det Θ = dim K_Θ` | **154** |
| `wind det S` | **152** |

All 64 nonzero arithmetic resonances satisfy `|z|=5^(−1/4)`. The bound poles are removed only in the constant character direction. Multiplying m₀ by `(z²−1/5)/(1−z²/5)` gives `−z⁶ P(z²)/(25P(z²/5))`, a degree-14 inner function; every other scalar eigenchannel has degree ten. Hence `14+14·10=154`, also `2·85−2−14=154`, exactly as in the notebook's model theorem (`04l_elliptic_cavity_channel.tex:38–57`). The exit defect rank is fifteen (S(0)=0, and hence Θ(0)=0); it is not 32, 64 or 154.

Moving all cuts out r steps multiplies S by z^(2r), and adds 30r delay modes. Moving cuts separately gives `S→D S D`, `D_aa=z^{r_a}`. Thus **equal height means equal degree gap δ**, here three. Counting steps from each cusp's first individually regular edge is not a canonical equal-height convention and can destroy the displayed group matrix. Both delay count and total model dimension depend on the cut; the 64 nonzero arithmetic resonances do not.

## Q3 — SHARPENED: a geometric inversion exists, but it is not the Riemann–Roch height reflection

### Q3.1. The actual automorphism of the entire weighted diagram

The hyperelliptic involution `σ(x,y)=(x,−y)` is defined over F₅ and fixes infinity. It acts on R, on `K_∞`, and on the lattice tree, normalising GL₂(R). Consequently it descends to a graph automorphism preserving every vertex and edge stabiliser. This proves existence on the **whole core**, not merely a guessed permutation of exits.

Since `P+σP~2∞`, its action on Pic⁰ is −1. Thus

`σ c(j,d)=c(−j,d)`, and `σ(a,r)=(−a,r)` on the fifteen rays.

In the explicit representatives of Q1, `t=x²/y` changes to −t, so its action is

`[g(n,u(t))] ↦ [g(n,u(−t))]`.

The factor (−1)^n on the first column is a unit and disappears from the lattice. This formula determines the permutation of every printed vertex, via the exact equivalence test in Q1.3. `checks/labelled_data.py` gives the complete 381-entry permutation, including the exterior vertices; `checks/analyse_graph.py` verifies its square is the identity and that it preserves the **multiset of all weighted edges**. It fixes 198 of the 366 nucleus vertices, exchanges the other 168 in 84 pairs, fixes the a=0 ray, and exchanges seven pairs of rays. In particular the head transpositions are

`(378,377), (356,355), (354,353), (360,361), (349,352), (362,359), (357,358)`.

The pointed curve automorphism group over F₅ is exactly this C₂: every automorphism fixes the unique hyperelliptic pencil and hence has `x↦ax+b`, `y↦cy`, with a,c nonzero. The exact test of `f(ax+b)=c² f(x)` over the 80 triples gives only `(a,b,c)=(1,0,1),(1,0,4)`. This statement is about automorphisms arising from the pointed curve, not a claim to have classified every accidental automorphism of the weighted core.

It follows geometrically that `P_inv S P_inv=S`. In Fourier coordinates it exchanges χ_k and χ_(−k), agreeing with the seven blocks of Q2. In this curve, equality of the inverse L-factors gives the additional constant ± eigenbasis.

### Q3.2. Why the stated Riemann–Roch map is not itself that graph automorphism

Binding E6 correctly gives `(j,n)↦(−j,2−n)` on the **graded divisor bond** (`notes/genus-two-bond/astra-proofs.md:460–466`). It changes degree and does not define the same operation as pullback by σ, which preserves degree.

There are two precise obstructions to identifying it with a graph fold:

1. A rank-two bundle has the canonical isomorphism `E^∨≅E⊗(det E)⁻¹`. Therefore duality, and also `E↦E^∨⊗K_C`, acts **trivially** on projective-bundle vertices. In the literal arithmetic quotient det E is trivial away infinity, so the requisite twist is also allowed there. Duality cannot exchange the nontrivial cusp pairs.
2. Defining a map on split vertices by `c_D↦c_(K−D)` is not well-defined, since `c_D=c_(−D)`. For example `c_(4∞)=c_(−4∞)` would have the two different images `c_(2∞)` and `c_(6∞)`. Their stabiliser orders are different. Hence the affine Riemann–Roch reflection cannot be extended by this prescription to a diagram automorphism.

**Verdict:** the desired cusp inversion is geometrically realised by the hyperelliptic involution, and its full core action is proved. The literal assertion that the Riemann–Roch degree reflection is that automorphism is **REFUTED**. This supplies the geometric permutation part left open in E6, but does not construct a quotient of the GL₁ degree bond whose dynamics is the GL₂ cavity. Such a bond-to-cavity construction remains **OPEN**. Passing to the separate quotient graph by σ would identify the fifteen rays into eight; the original quotient still has fifteen exits.

### Q3.3. Which part of Pic acts geometrically?

Tensoring a bundle by a line bundle acts trivially after projectivisation. On the literal free-away-infinity model, a tensor twist preserves that component only if its class satisfies 2a=0. Here `A[2]=0`, so this mechanism supplies no nontrivial translations of the cusps. Inversion is supplied by σ instead.

There is also a scattering obstruction to *any* weighted diagram automorphism inducing a nonzero translation a↦a+b. Such an automorphism preserves the equal-δ cut (the order-2000 tail vertices and their order-400 predecessors identify it). It would force S to commute with the translation T_b. But the proved group-matrix formula gives

`S T_b = T_(−b) S`.

Since S is invertible generically, commuting would require `T_b=T_(−b)`, or 2b=0. For A=Z/15 this forces b=0. Thus no transitive Pic action on this weighted graph exists, although H-CLASS holds. A class-group matrix times inversion is an **intertwiner** for opposite translations, not a graph translation symmetry.

## Numerical checks for the blind lane

### Rebuild instructions and certificates

Use the Q1.4 vertex/edge table and Q1.5 attachments, or import `checks/graph_data.py` and `checks/labelled_data.py`. Core identifiers are all identifiers not in `TAILS`; the head order must be a=0,…,14, **not** breadth-first identifier order. For each core edge insert `A_vw=S(v)/S(e)` and its reverse. After conjugation/division by √5, insert fifteen unit couplings at the listed heads. Every weighted degree, including the ray degrees, must equal six. The data are already in the stabiliser format described by `scripts/elliptic_cavity.py:118–161`; `scripts/cusp_graph.py:11–53` fixes the incoming/outgoing and p/ptilde conventions.

Run, from the repository root, with `PYTHONDONTWRITEBYTECODE=1`:

```sh
python3 notes/genus-two-quotient-graph/checks/enumerate_graph.py
python3 notes/genus-two-quotient-graph/checks/analyse_graph.py
python3 notes/genus-two-quotient-graph/checks/spectral_certificate.py
```

All three completed with `ALL ASSERTIONS PASSED`. `checks/audit_document.py` additionally parses the printed Markdown vertex/edge and cusp tables and verifies exact agreement with the executable data. Enumeration takes several minutes, writes only the Python data module in checks, and uses exact F₅ arithmetic. Analysis labels the ideals with exact F₅[x] arithmetic, checks the entire involution and all weighted degrees/masses, and uses floating point only for displayed scattering values. The spectral certificate uses the installed `python-flint` backend for exact integer/rational linear algebra; it saves the exact factor coefficients as another Python module. No network input enters any computation. The analytic constant-term proof is independent of the numerical comparisons.

### Two complete scattering matrices in compact form

For either column below, extend `f(15−j)=f(j)` and set `S_ab=f((a+b) mod 15)`. Thus the eight entries in each column specify the entire 15×15 matrix, not just a selected submatrix. Values are rounded from the **core-resolvent computation**.

| j | f(j), z=0.3 | f(j), z=0.6 |
|---:|---:|---:|
| 0 | 0.000163463233889814 | 0.0149573124954992 |
| 1 | 0.0000121870392343906 | 0.000115071019585756 |
| 2 | 0.00000198493317143858 | −0.00198027932807337 |
| 3 | 0.00000216509359958237 | −0.00184227321741203 |
| 4 | 0.00000216191212120244 | −0.00185136271721545 |
| 5 | 0.00000216196830337733 | −0.00185076405531855 |
| 6 | 0.00000216196731124849 | −0.00185080348426284 |
| 7 | 0.00000216196732876317 | −0.00185080089856988 |

The corresponding Fourier factors have m_(15−k)=m_k:

| k | m_k, z=0.3 | m_k, z=0.6 |
|---:|---:|---:|
| 0 | 0.000213432996029921 | −0.00726511286703403 |
| 1 | 0.000179383009155804 | 0.0202320193456247 |
| 2 | 0.000174749490268385 | 0.0194532944576961 |
| 3 | 0.000167778458428024 | 0.0182185163442436 |
| 4 | 0.000159553617238853 | 0.0166546435267732 |
| 5 | 0.000151459535552405 | 0.0149892950717405 |
| 6 | 0.000144972969798691 | 0.0135535010514272 |
| 7 | 0.000141360675717243 | 0.0127111303522515 |

| Check | z=0.3 | z=0.6 |
|---|---:|---:|
| det S, direct 15×15 matrix | −1.44799229925431·10⁻⁵⁷ | 6.90935642577700·10⁻²⁸ |
| −p/ptilde, direct 366×366 determinants | −1.44799229925398·10⁻⁵⁷ | 6.90935642577661·10⁻²⁸ |
| `−m₀ Π_(k=1)^7 m_k²` | −1.44799229925514·10⁻⁵⁷ | 6.90935642577684·10⁻²⁸ |
| max entry error against the L-ratio matrix | 2.92·10⁻¹⁶ | 5.64·10⁻¹⁶ |

The determinant test uses **relative** error, since these determinants are small. Additional checks at `z=0.8+0.2i` and `z=exp(0.7i)` have maximum matrix errors respectively `1.27·10⁻¹⁵` and `2.82·10⁻¹⁵`. The latter tests the unit-circle regime. Separate exact rational checks at `z=√5/10` and `z=√5/3` compare the complete p, the complete p/ptilde ratio, and the factorisation in Q2.3; no rounding tolerance is used there.

### Independent targets, including common-factor traps

1. Recover `(366 vertices, 915 edges, 15 exits)` and the eight-row stabiliser histogram; test both endpoint indices on every edge and the full mass `4637/64`.
2. Recover the head-to-class table from the nilpotent image ideals. Testing H-CLASS after optimising a permutation against the L-values would not check the arithmetic labels.
3. Compute `F S F*` and check its single scalar plus seven inverse-character blocks against Q2.1, using ideal-class labels. In ratio labels j, test `L_(2k)` instead.
4. Recover exact visible rank 85 and invisible rank 281. The core adjacency characteristic polynomial has zero multiplicity 130; seven zero modes are visible and 123 are invisible. The invisible factor `X²−20` gives two **compact threshold eigenfunctions**. Consequently the full p has order nine at each of z=±1: seven visible half-bound orders and two orders from the cusp eigenfunction at that sign.
5. Test `ord_0 p=90`, `deg p=732`, `deg D_c=562`, arithmetic degree 64 in z, two bound poles, and inner-model degree 154. Taking just `gcd(p,ptilde)` without tracking directions or threshold types loses the relevant bookkeeping (`04k:113–138`).

## Corrections to the brief

| # | Verdict | Correction |
|---:|---|---|
| 1 | SHARPENED | The arithmetic double coset initially parametrises bundles trivial away infinity modulo O(n∞); all bundles modulo Pic agree here because A has odd order and no 2-torsion. |
| 2 | SHARPENED | GL stabilisers include the centre of order four; effective PGL orders are all divided by four. The weighted adjacency and S are unchanged, but masses change by four. |
| 3 | PROVED | The finite nucleus has 366 vertices and 915 edges; it has many cycles, so the tree-matching determinant shortcut from the elliptic examples does not apply. |
| 4 | SHARPENED | The fifteen standard tails attach at δ=3, with head order 400, first exterior order 2000 and coupling one. Some classes have irregular behaviour before that cut. |
| 5 | SHARPENED | A cusp ideal class a and a positive-degree splitting-ratio class j satisfy j=2a, or j=−2a in APW's lower-summand labelling. |
| 6 | PROVED | H-CLASS's group-matrix-times-inversion structure holds for this actual genus-two quotient at the specified cut. |
| 7 | REFUTED | With the notebook's S convention, the s-variable factors are `5z⁶ L(2s,χ)/L(2s−1,χ)`, the reciprocal of the ratio written in literal H-CLASS. |
| 8 | SHARPENED | The 32 zeros of P_Y in T become 64 zeros in z because T=z²; inverse-character pairs have repeated factors but retain multiplicity. |
| 9 | SHARPENED | At this cut there are 90 delay modes, 281 invisible core eigenvectors, fourteen half-bound states and two visible bound poles; the inner model has 154 modes and fifteen exits. |
| 10 | SHARPENED | The full p has additional cusp and threshold factors; the two compact threshold eigenfunctions are different from the fourteen half-bound states. |
| 11 | REFUTED | Riemann–Roch's degree reflection is not a well-defined split-vertex map; rank-two duality acts trivially after projectivisation. |
| 12 | PROVED | Hyperelliptic pullback does give the full weighted-graph involution a↦−a, preserving height and every edge index. |
| 13 | REFUTED | The full Pic⁰ translation group does not act by weighted diagram automorphisms on these cusps; the scattering matrix intertwines opposite translations instead. |
| 14 | OPEN | A geometric construction from the entire graded GL₁ bond to this cavity, and a transport of its metric to cohomology, are not supplied by H-CLASS or by the involution. |
| 15 | SHARPENED | The instruction to write only the proof file conflicts literally with the separately mandatory progress.txt; that one-line author-tagged marker is the sole additional non-Python output. No other project files were edited and no git command was run. |

## Q4 — What this changes in the notebook

**H-CLASS is settled for this curve**, with the explicit equal-δ cut and the ratio direction corrected. This is an actual arithmetic cavity, reconstructed from local lattices over the given function field, whose fourteen nontrivial class characters carry nonconstant quadratic L-functions. Its graph needs no genus-two analogue of an unverified Takahashi picture: Q1 supplies all vertices, all weighted edges, all ray attachments, and an exact mass check. Takahashi's elliptic theorem remains background only: Shuzo Takahashi, *The fundamental domain of the tree of GL(2) over the function field of an elliptic curve*, Duke Math. J. **72** (1993), 85–97, Figure 5 (**original not byte-cited**; bibliography in `refs/src/2603.26443/Literatur.bib:3430–3444`). Serre's finite-core theorem is *Trees*, Chapter II, §2.3, Theorem 9 (**original not byte-cited**), with the explicit reduction/nucleus version byte-cited in Q1. No elliptic classification theorem was extrapolated to genus two.

The separation of exits and modes is now concrete: fifteen geometric rays, eight Fourier blocks, 32 arithmetic zeros in T, 64 arithmetic resonances in z, and a 154-dimensional minimal inner model at this cut. The extra 90 dimensions are delays. Neither 32 nor 64 is an exit count, and grouping characters into inverse pairs does not remove geometric rays. A change of cut changes delays and model dimension while retaining the nonzero arithmetic divisor.

The involution has also acquired a precise boundary. Hyperelliptic pullback extends the inversion permutation through the entire weighted core. Riemann–Roch's reflection of the graded divisor bond does not give that graph map. The symmetry proves the inverse-pair organisation; it does not identify the graph's metric with a Frobenius-normal or Hodge metric. Binding E4 and the metric caveats of E5 therefore remain untouched.

The numerics lane should rebuild the **366-vertex, 915-edge** nucleus with fifteen unit-coupled standard rays, in the class order of Q1.5. Its primary outputs should be the two scattering checks above, the exact Krylov split 85+281, and the degree-732 p with the full factorisation of Q2.3. The supplied Python data avoid a second transcription, while the printed table permits an independent rebuild.

| Notebook statement | Status | One-sentence result |
|---|---|---|
| Genus-two arithmetic diagram | PROVED | The quotient is the explicit 366-vertex weighted nucleus with fifteen rays and GL vertex mass 4637/64. |
| Genus-two H-CLASS | PROVED with conventions fixed | At δ=3, S_ab=f(a+b), and its Fourier factors are the exact z⁶/5 ratios in Q2.1. |
| Literal L-ratio direction of 04k | REFUTED | Its stated ratio belongs to inverse scattering in the notebook's wave convention. |
| Genus-two divisor and model count | PROVED | The arithmetic factor is P_Y(z²), giving 64 nonzero resonances and 154 total inner-model modes at this cut. |
| Geometric cusp inversion | PROVED | The hyperelliptic involution preserves the entire weighted graph and sends a to −a. |
| Riemann–Roch as the diagram fold | REFUTED / OPEN replacement | The literal map fails; constructing a graded-bond-to-cavity functor remains open. |
| General H-CLASS and cohomological metric comparison | OPEN beyond this result | This proof handles the specified odd-class-number quotient and supplies no universal even-class-number or metric theorem. |
