# A2 complex zeta: the smallest Ramanujan complex, exactly

Worker log, 2026-09-13. Script `scripts/a2_complex_zeta.py`, captured stdout
`outputs/a2_complex_zeta.txt`. Deterministic, ~90 s from the repo root, no
randomness. Everything below is either **VERIFIED** (exact integer or exact
polynomial arithmetic, or a numerical computation whose residual is printed),
**INDICATED** (numerical evidence short of a proof), or **FAILED**.

Sources read in the TeX, not the PDF: LSV `math/0406217` (`sec:explicit`
algorithm, `:2586-2630`; `sec:finq` `:1673-1686`; `whatisr` `:2032-2038`),
Kang–Li `0804.2305:195-260`, Kang–Li–Wang `0809.1401v1:342-368`, `:1352-1370`,
`:1410-1418`, LLP `1702.05452:1009-1027`.

## 1. The complex (VERIFIED)

LSV algorithm with `q = 3, d = 3, e = 1, s = 1`:
`F_27 = F_3[v]/(v^3+2v+2)`, normal basis `zeta_i = phi^i(v^2)`, `beta = v^2`
(`tr = 2`), `x |-> alpha = 1` in `L = F_3`, `gamma = y(alpha) = N(1+alpha beta)-1 = 1`.
(`gamma = 1` is forced: `p(lam) = lam - gamma` must be prime to `lam` and `lam+1`,
and for `e = 1` that leaves only `gamma = 1`.)
`rho(z) = (1 + alpha rho(beta)) Phi`, `b = 1 - rho(z)^{-1}`, `b_u = rho(u) b rho(u)^{-1}`.

| quantity | value | expected |
|---|---|---|
| `|S_1|` | 13 | `[3,1]_3 = q^2+q+1` |
| `<S_1>` | **5616** | `PGL_3(F_3) = PSL_3(F_3)` |
| `S_1 ∩ S_1^{-1}` | empty | colour-1 and colour-2 disjoint |
| `|P| = #{b_u b_v b_w = 1}` | 52 | `(q^2+q+1)(q+1)` = complete flags |
| `S_2` | `= S_1^{-1}`, 13 elements | LSV step 5 |
| link of a vertex | 26 vertices, 4-regular, bipartite, girth 6, any 2 points on exactly 1 line | incidence graph of `PG(2,3)`, the unique (4,6)-cage |
| `V, E, F` | 5616, 73008, 97344 | 26 nbrs, 52 triangles per vertex |
| `chi = V-E+F` | **29952** | `= |G| * 16/3` |

Two structural facts that matter downstream and were **not** anticipated in the brief:

* **No 3-colouring.** LSV `whatisr`: `r = ord(y/(1+y))` in `L^*/(L^*)^d`; here
  `y/(1+y) = 2` and cubing is the identity on `F_3^*`, so `r = 1`. Directly
  confirmed: the BFS colouring of the Cayley graph is inconsistent (as it must
  be, `PGL_3(F_3)` is simple, so there is no epimorphism onto `Z/3`). Hence
  `Gamma(I)` is **not** contained in `Gamma_1`, and Kang–Li's hypothesis (I),
  `ord_pi det Gamma ⊂ 3Z`, **fails** for this quotient. For `q = 3` no `e`
  repairs this (`3 | q^e - 1` is impossible).
  Types of *directed* edges are still globally defined (via `S_1` vs `S_2`),
  which is all the combinatorics of `L_E`, `L_B` needs.
* **2-cell stabilisers.** All 13 generators have order 3 in `PGL_3(F_3)`, so the
  24336 triangles `{g, g b_u, g b_u^2}` carry a `Z/3` stabiliser. `G` acts freely
  on vertices and on edges but **not** on unpointed 2-cells. This is exactly the
  caveat in the prover's T5.7 and is why the per-block Euler factor is not
  `(1-u^3)^{chi·dim/|G|}` (see §5).

A type-preserving companion is also built: `Gamma~ = Gamma(I) ∩ Gamma_1`, with
`Gamma/Gamma~ = PGL_3(F_3) x Z/3` (Goursat, using `delta(Gamma(I)) = Z/3`), i.e.
the 3-fold cover with `V = 16848`, `chi = 89856`. Its closed-walk counts are
`3 x` the base counts restricted to total colour shift `0`.

## 2. Vertex level (VERIFIED)

`A_2 = A_1^T` exactly; `A_1` is normal and `[A_1,A_2] = 0` (exact sparse check).
Hence on every simultaneous eigenvector `(lambda_1, lambda_2) = (lambda, conj lambda)`.
Full dense `eigvals` of the 5616x5616 `A_1` (38 s).

* exactly **one** trivial eigenvalue, `lambda = 13 = q^2+q+1`;
* temperedness tested by **Cohn's theorem** (the cubic `z^3 - (l/q)z^2 + (l̄/q)z - 1`
  is self-inversive, so all its roots are unimodular iff both roots of
  `3z^2 - 2sz + s̄` lie in the closed disc; this is stable, unlike `np.roots` on the
  near-degenerate cubic, which gave spurious 1e-7 defects);
* **all 5615 nontrivial eigenvalues are tempered**, max defect `2.0e-14`;
* `max |lambda|` over nontrivial eigenvalues `= 7.126860684 < 3q = 9`.

So `X_Gamma` is a Ramanujan complex, and KLW statement (2) — RH for the vertex
cubic — is verified outright.

## 3. Edge and chamber operators, exact traces (VERIFIED)

* `L_E` on the 73008 directed colour-1 edges, successor `(x,y)->(y,z)` with `z` a
  **colour-1** neighbour of `y` and `{x,y,z}` not a 2-cell: out-degree exactly
  `q^2 = 9` for every edge (LLP `:1009-1027`, Kang–Li `:210`).
* `L_B` on the `3F = 292032` cyclically-increasing pointed chambers,
  successor as Kang–Li `:212`: out-degree exactly `q = 3`.
* Traces computed **exactly as integers** by the free `G`-action
  (`Tr = |G| x` sum of diagonal return counts from the identity vertex), sparse
  int64 matvecs only, no eigendecomposition. `Tr((L_E^t)^m) = Tr(L_E^m)` confirmed.

```
 m        Tr(L_E^m)              Tr(L_B^m)
 1..5              0                      0
 6           657072                      0
 7          1533168                      0
 8         36796032                      0
 9        359418384                      0
10       3531762000                      0
11      31686640128                      0
12     282029757984                      0
13    2542424897376                      0
14   22890084785568                      0
15  205914931747200               16426800
16 1853110568391264               22778496
17 16677363472645824             145212912
18 150094642133807280            342991584
```
`Tr(A_1^a A_2^b) = |G| n(a,b)` also exact (Python-integer matvecs);
`n(1,1) = 13`, `n(3,0) = n(0,3) = 52`, `n(2,2) = 325`.

### Prover cross-checks (all VERIFIED)

* the **unrestricted** ordered edge rule has out-degree `2q^2+q = 21`, not 9: it
  is not Kang–Li's operator;
* on all **6** orderings of a chamber, `Tr(T_2^m) = 2 Tr(L_B^m)` for `m = 1..18`,
  i.e. `det(I + u T_2) = det(I + u L_B)^2`;
* on `∂Δ^3`: `T_1 = 0` (every triple is a 2-cell) and `T_2` is a permutation of
  cycle type `4^6`, so `det(I + u T_2) = (1-u^4)^6`, matching T2.4.

## 4. Which form of the identity holds

**Holds (VERIFIED to `u^18`, exactly, on both the 5616-vertex complex and the
16848-vertex type-preserving cover):**

```
det(I - A_1 u + q A_2 u^2 - q^3 u^3 I) · det(I + L_B u)
      = (1-u^3)^chi · det(I - L_E u) · det(I - (L_E)^t u^2)
```

This is literally KLW Theorem 3 (`0809.1401v1:1410-1418`) cleared of denominators,
and the only form that passes the degree count: `3|G| + 3F = 308880` on both sides.
Fitting the residual as `a log(1-u) + c log(1-u^3)` returns `a = 0, c = chi`
exactly — `29952` on the base, `89856` on the cover — consistently at every order.

**Fails:**
* `det(I - L_B u)` in place of `det(I + L_B u)`: first failure at `u^15`
  (residual `-2190240`; on the cover `-6570720`).
* the form written in the brief, `(1-u^3)^chi det(cubic) det(I+L_Bu) = det(I-L_Eu)det(I-L_E^t u^2)`:
  fails at `u^3` already (residual `-59904`) and fails the degree count
  (`398736` vs `219024`). The coordinator's own "equivalently" clause
  (`D_B/D_E = (1-u^3)^chi / det P_3`) rearranges to the form that holds.

**Notable:** the identity holds on the base complex *even though Kang–Li's
hypothesis (I) fails there* (no 3-colouring). Type preservation is apparently not
needed for the identity itself; the colour only controls where the traces vanish
(on the cover `Tr(L_E^m) = Tr(L_B^m) = 0` unless `3 | m`).

## 5. RH by factor

Predicted (KLW Theorem 2): nontrivial `|lambda(L_E)| ∈ {q, q^{1/2}} = {3, 1.7320508}`,
nontrivial `|lambda(L_B)| ∈ {1, q^{1/4}, q^{1/2}} = {1, 1.3160740, 1.7320508}`
(note `|u| = q^{-1/4}` means `|lambda| = q^{1/4}`; the brief's `q^{3/4}` is wrong).

* **VERIFIED, full space, `L_E`:** ARPACK's 40 largest moduli are `9.0` once and
  then `3.0` forty times over — one trivial eigenvalue of modulus `q^2`, nothing
  strictly between `q` and `q^2`.
* **VERIFIED, exactly, on two isotypic blocks** (see §6 for the construction):
  * trivial block: `|lambda(L_E)| = {9 (x1), √3 (x12)}`;
    `|lambda(L_B)| = {3 (x1), √3 (x12), 3^{1/4} (x24), 1 (x15)}`.
  * 12-dimensional block: `|lambda(L_E)| = {3 (x36), √3 (x120)}`;
    `|lambda(L_B)| = {√3 (x192), 3^{1/4} (x240), 1 (x192)}`.
  Exactly the three predicted radii, with nothing else.
* **INDICATED, full space:** `|Tr L_E^m|^{1/m} -> 9.000000` monotonically by `m = 18`;
  `(Tr L_E^m - q^{2m})/q^m` stays `O(10^3)` and oscillates in sign, consistent with
  `q` as the sub-leading modulus. ARPACK does **not** converge on `L_B` (its
  spectrum sits on three circles with huge degeneracies), so `L_B` is handled
  block by block instead.

## 6. The twisted ("quantum") version

`pi` = the 12-dimensional irrep, the permutation action on the 13 points of
`P^2(F_3)` minus the constant. (The line action gives the same character, so
`pi' ≅ pi`.)

**Channels (VERIFIED).** `Phi_k(rho) = (1/13) Σ_{s∈S_k} pi(s) rho pi(s)†` on 12x12:
unital, trace-preserving, `[Phi_1, Phi_2] = 0`. Exactly one eigenvalue `1`;
largest nontrivial `|mu| = 0.498594095`, i.e. `|13 mu| = 6.481723` — below the
classical deltoid radius `3q = 9` **and** below the Hastings quantum-Ramanujan
bound `2√(D-1) = 6.928203` for `D = 13`. All 143 nontrivial joint eigenvalues
`(13 mu, 13 conj mu)` are inside the tempered deltoid (max Cohn defect `2.2e-15`).
So this is a **Ramanujan quantum expander of type Ã_2**.

*Reason it cannot fail:* `Phi_1 = (1/13) Σ_s pi(s) ⊗ conj(pi(s))` is literally
`A_1^{(pi ⊗ π̄)}/13`, so `13·spec(Phi_1)` is a sub-multiset of `spec(A_1)` on `C[G]`
(checked numerically, max distance `< 1e-6`). Ramanujan complex ⇒ Ramanujan
quantum expander, automatically. The channel adds no new spectral values.

**Twist bookkeeping (prover T5.5/T5.6, folded in and VERIFIED).**
* The full-complex weights `E_{(g,gs)} = pi(s)` are **not flat**: 39 of the 52
  chambers have `pi(t)pi(s) ≠ pi(st)`.
* The covariant weights `pi(s^{-1})` on the full complex are **pure gauge**
  (`F_g = pi(g^{-1})`), so `det(I - u T_E^pi) = det(I - u L_E)^{12}`: every closed
  straight walk of the full complex returns to its own directed edge, hence has
  holonomy `e`.
* The genuine Artin object is the **voltage quotient**: 13 states (the colour-1
  edges at the identity vertex), 9 successors each with its group voltage.
  Verified directly: `Tr(T_nu^m) = Σ_{closed quotient walks} chi_nu(holonomy)`
  agrees with the block trace for `m = 1..8` (edges) and `m = 1..9` (chambers),
  and both differ from the gauge-trivial full twist, as they must.
  With the path-order matrix layout the fibre weight of a voltage-`h` arrow must be
  `rho(h)` (then the closed-walk trace is the class function `chi_rho(holonomy)`);
  T5.6's `rho(h^{-1})` is the same block for the opposite composition order, and
  `nu` has a real character so the determinants coincide.
* For `rho` = the regular representation the construction returns `L_E` itself, so
  `Tr(L_E^m) = Σ_rho dim(rho) Tr(L_E^{(rho)m})`.

**Blockwise identity (VERIFIED).** Writing the residual as
`F_rho(u) = (1-u)^a (1-u^3)^c`, consistently at every order up to `u^18`:

| block | `a` | `c` | naive `(chi/|G|)·dim` |
|---|---|---|---|
| trivial (dim 1) | 13 | 1 | `16/3` |
| `nu = 1 ⊕ pi` (dim 13) | 13 | 65 | `208/3` |
| `pi` (dim 12) | **0** | **64** | `64` |

So for the 12-dimensional irrep the naive hypothesis is exactly right,
`F_pi = (1-u^3)^{64} = (1-u^3)^{chi·dim pi/|G|}`, with **no** `(1-u)` factor;
the whole anomaly sits in the trivial block, where the fractional exponent `16/3`
is replaced by `(1-u)^{13}(1-u^3)^1`. This is exactly T5.7's warning: the deck
group does not act freely on the 2-cells (24336 triangles with `Z/3` stabilisers),
so the fractional power must not be asserted, and "the factor does not live only
in the trivial block" — here it lives only in the trivial block plus a `(1-u)^{13}`
that the other blocks must cancel (`Σ_rho d_rho a_rho = 0` forces the remaining
irreps to contribute `-13`; only the two blocks above were built, so that sum is
not checked here).

For the trivial block this is upgraded to an **exact polynomial identity** (sympy
characteristic polynomials, no truncation; both sides degree 55):

```
det(P_3) det(I + u L_B) = (1-u)^13 (1-u^3)^1 det(I - u L_E) det(I - u^2 L_E^t)
```

## 7. What was not done

* `pi ⊗ conj(pi)` (144-dim) as a separate block: unnecessary, since
  `Phi_1 = A_1^{(pi⊗π̄)}/13` was computed directly and its spectrum shown to be a
  sub-multiset of `spec(A_1)`; the `L_B` block for a 144-dimensional twist is
  7488x7488 and was judged not worth the time.
* Full-space spectra of `L_E` (beyond the top 40) and of `L_B`: would need the
  whole character table of `PGL_3(F_3)`.
* The identity is checked as a power series to `u^18` on the full complexes
  (degrees are 308880), not as a polynomial identity; only the trivial block is
  checked exactly as polynomials.
