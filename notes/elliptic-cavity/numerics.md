# Numerics lane: two arithmetic cavities with cusps (elliptic curves over F_2 and F_3)

Author: `claude:opus`. Date 2026-09-20. Run **blind to the prover's file**, from the brief
`notes/elliptic-cavity/astra-brief.md` and the sources alone.

Script `scripts/elliptic_cavity.py` (python3 + numpy/scipy/sympy, seed 20260920, ~50 s),
captured output `outputs/elliptic_cavity.txt`. **192 checks, all asserted with tolerances,
all passing.** Every displayed formula of the brief was treated as a conjecture and re-derived
from the definitions. Where exactness was possible it was used: every determinant, every
scattering matrix, every zeta identity is an **exact sympy identity of rational functions**,
not a sample-point agreement.

---

## 0. Transcription verdict

I re-read `refs/src/2603.26443/serre_example.png` and `takahashi_example.png` directly.

**Both diagrams in the brief are transcribed CORRECTLY, vertex for vertex and edge for edge.**

* **D2** (`serre_example.png`): top row `6 --2-- 2 --2(dashed)-- 4 --4-- 8 ...`, hanging from the
  second vertex `2 --2-- 2 --1-- 1 --1-- 3` and `--1-- 3`. That is exactly the brief's
  `A,B,C,D,E,F = 6,2,2,1,3,3`, edges `A-B(2), B-C(2), C-D(1), D-E(1), D-F(1)`, cusp at `B` by an
  edge of `S = 2` onto a ray `4, 8, 16, ...` with `S(c_k - c_{k+1}) = S(c_k)`.
* **D3** (`takahashi_example.png`): the figure shows `48` above the left `12`; the spine
  `12 --6-- 6 --2-- 2 --2-- 4`; `8` above the central `2`; below it `6 --6-- 12`, with `48` to the
  left of that `12`; and four dashed cusp edges — `12 --12-- 36 --36-- 108 ...` at each of the two
  `12`s, and `4 --4-- 12 --12-- 36 ...` twice at the `4`. That is exactly the brief's
  `L1p,L1,L2,X,Xp,Y,Z,Zp,Q = 48,12,6,2,8,6,12,48,4` with its eight core edges and four cusps.

**Degrees.** Every core vertex has `deg = sum_e S(v)/S(e) = q+1` (D2: all `3`; D3: all `4`), and
every ray vertex too: at `c_1` the condition reads `S(c_1)/S(e) + 1 = q+1`, i.e. `S(c_1) = q S(e)`,
which the transcribed rays satisfy (D2 `4 = 2*2`; D3 `36 = 3*12` and `12 = 3*4`); at `c_k`, `k >= 2`,
it is `q + 1` identically. Checks 1, 2, 6, 7.

Independent confirmation that the brief's `S_even` and mine are the *same* matrix: the brief quotes
the two eigenvalues of `S_even` at `z = 0.8 + 0.1i` as `-1.19997 + 0.27727i` and
`0.80005 + 0.10680i`; I get `-1.199967 + 0.277270i` and `+0.800046 + 0.106797i` (check 113).

---

## 1. Conventions I fixed

* **Indexing / normalisation (C1).** `T_X = D^{-1/2} A_X D^{-1/2}/sqrt q` with `D = diag S` and
  `(A_X)_{vw} = S(v)/S(e)` the integer non-symmetric adjacency. On a cusp ray this is the free path
  adjacency; the junction coupling is `c^2 = S(v)S(c_1)/(q S(e)^2) = S(v)/S(e)`, the two forms
  agreeing *because* `S(c_1) = q S(e)`. For D2 and D3 **every** junction has `c^2 = 1`
  (D3's `Q` carries two cusps, so `C_QQ = 2`).
* **The exact-arithmetic trick (new, load-bearing).** `T_X` carries square roots, but
  `p(sqrt q * t) = det((1 + q t^2) I - t A_X - C)` has **integer** coefficients. Every determinant
  is computed in `t` and pushed back by `z = sqrt q * t`. Likewise with
  `Mt = (1+qt^2)I - t A_X` and `W_ab = c_a c_b sqrt(S(v_b)/S(v_a)) [Mt^{-1}]_{ab}` one has
  `Gamma = sqrt q t W`, `z Gamma = q t^2 W`, `Gamma/z = W`, so
  **`S(z) = (q t^2 W - 1)^{-1}(1 - W)` is a rational function of `t` over `Q(sqrt(S-ratios))`**.
  This is what makes exact 9x9 work fast.
* **Klein reduction (D3).** The even/odd reduced diagrams are built *programmatically* from the
  involution `sigma`, not transcribed: orbits of `sigma`, `A_even[o1][o2] = sum_{w in o2} A[v][w]`,
  `S_eff(o) = S(v)/|o|`, and the odd version with the sign. The reduced diagrams again have degree
  `q+1` everywhere. Even: 6 vertices `S_eff = 24,6,3,2,8,4`, two channels with `c = 1` at the
  `L1`-orbit and `c = sqrt 2` at `Q`. Odd: 3 vertices `S_eff = 24,6,3`, one channel `c = 1`.
* **Model space.** For a scalar inner `Theta` (finite Blaschke over the resonances, `z = 0`
  included) `K_Theta = {P/qq : deg P < N}`, `qq(w) = prod (1 - conj(z_j) w)`; in the basis
  `f_k = w^k/qq` the compressed shift `Z = P_K M_w|_K` is **exactly the companion matrix** of
  `prod (w - z_j)`. Companion matrices are non-derogatory, so each distinct resonance carries a
  single Jordan block. `spec Z =` the resonances (04i's convention). `Z` is pushed to an
  orthonormal frame by `G^{1/2}` where `G` is the Gram of `{f_k}` computed from the Taylor
  coefficients of `1/qq`.
* **Not built here.** The Lax--Phillips energy space of *these* diagrams (H-LP is inherited from
  04i, reviewer MINOR T1c); the generic `h`-dimensional-exit renewal machinery of T3(b) (04j did
  the scalar-exit case; here `h = 1` for D2 and the D3 blocks are scalar or handled by counting).

---

## 2. Correction ledger

The brief's drafted statements, each confirmed / corrected / untested, with the numbers.

| # | Where | Brief says | What I find |
|---|---|---|---|
| **D1** | Sec 0 | H-DIAG-2, the D2 data | **CONFIRMED** against the PNG, exactly. Degrees all `3`, core and ray. |
| **D2** | Sec 0 | H-DIAG-3, the D3 data | **CONFIRMED** against the PNG, exactly. Degrees all `4`, core and ray. |
| **D3** | C1 | `c^2 = S(v)S(c_1)/(q S(e)^2) = S(v)/S(e)`, `= 1` for D2, D3, `C_QQ = 2` | **CORRECT**, all of it, and the two forms agree *because* the degree condition at `c_1` forces `S(c_1) = q S(e)`. The ray really becomes the free path adjacency after `g = f/sqrt S` and `/sqrt q` (dev `1e-16`). `T_X(D2)` has entries `sqrt(6)/2 = sqrt(3/2)`, `sqrt2/2`, `1`; `T_X(D3)` has `2 sqrt3/3`, `sqrt6/3`, `1`. |
| **D4** | T1(a) | `p(z) = (z^2/2)(z^2-2)(z^2+1)^2(2z^4-2z^2+1)`, `ptilde = -(1/2)(z^2+1)^2(2z^2-1)(z^4-2z^2+2)`, `R = z^2(z^2-2)(2z^4-2z^2+1)/((2z^2-1)(z^4-2z^2+2))` | **ALL THREE EXACTLY CORRECT** (zero polynomial difference). `deg p = 12`, monic, even. `R = -p/ptilde` with 04i's sign. |
| **D5** | T2(a) | `p(z) = (z^4/3)(z-1)^2(z+1)^2(z^2-3)(z^2+1)^2(3z^4+1)`, `ptilde = -(1/3)(z-1)^2(z+1)^2(z^2+1)^2(3z^2-1)(z^4+3)` | **EXACTLY CORRECT.** `deg p = 18`, monic, even. |
| **D6** | C2 | `det H(mu) = (-1)^n (2 mu)^{-n} det((1+mu^2) - mu T_X - C)`, so APW's `mu` IS the notebook's `z`, and APW's displayed polynomial is `det H` "up to a monomial and a constant" | The identity is **EXACT** (verified symbolically for both diagrams), so `mu = z`: **confirmed**. But the monomial and the constant are now pinned: APW's *displayed* polynomial is `(-1)^n 2^n q z^{n-m} det H(mu)`, i.e. `128 z^4 det H` (D2) and `-1536 z^5 det H` (D3), equivalently **`p(z) = z^m (APW display)/q`** with `m = ord_0 p`. The constant is exactly `q`, the monomial exactly `z^{n-m}`. APW silently drop the `z = 0` root. |
| **D7** | C3 | `p(0) = det(1-C) = prod(1 - C_vv)` vanishes; order of vanishing 2 (D2), 4 (D3); "relate it to `rank(1-C)`" | Orders **2 and 4 confirmed**, but the relation is a **factor two**: `ord_0 p = 2 dim ker(1-C)` (`2*1` and `2*2`), not `dim ker(1-C)`. The first-order term vanishes because `T_X` has **no loop at any attachment vertex** and the attachment vertices are **pairwise non-adjacent** — both verified exactly. Without those two geometric facts the order would be `dim ker(1-C)`. |
| **D8** | C2 | `S(z) = (z Gamma - 1)^{-1}(1 - z^{-1} Gamma)`, symmetric, unitary on the circle, `S(z)S(1/z) = 1`, `S(conj z) = conj S(z)`, `det S = (-1)^h p/ptilde` | **ALL CORRECT.** Checked against a *direct* generalised-eigenfunction solve on core + `h` rays (the ansatz solves the free recursion, so the solve is exact: `L = 14` and `L = 30` agree to `4e-15`), at four points of `|z| = 1`, dev `<= 4e-15`. `det S` checked at three points off the circle, dev `<= 2e-14`. |
| **D9** | C2 | "Reconcile with Childs--Gosset's `S = -Q(z)^{-1}Q(1/z)`" | The answer is a **factor `z^2`**: `S_notebook(z) = z^2 S_ChildsGosset(z)`, exactly, in every channel (dev `5e-16` on D2, `1e-15` on a random 6-vertex core with three tails). It is an **origin shift** of the tail coordinate: CG put the incoming wave `z^{-(j+1)}` at tail site `j` with `j = 0` the *attachment vertex* (`1203.6557:levinson2.tex:340-346`), the notebook puts `z^{-k}` at ray site `k >= 1` with the attachment vertex outside the ray. Consistent with 04i numerics D13 (a scattering function is only defined up to a power of `z`). **Caveat:** CG attach at most one tail per vertex, so D3 (two cusps at `Q`) is outside their setup as written; the `Gamma`-form still applies, and there `Gamma` is **singular** (rank 3 < h = 4). |
| **D10** | C3 | `N(D2) = 6 = 4 + 2`, `N(D3) = 8 = 4 + 4`; poles of `det S` in the disc are the `l^2` eigenvalues outside `[-2,2]`; thresholds cancel | **ALL CORRECT.** `gcd(p, ptilde) = (z^2+1)^2` for D2 (cusp forms only, **no** threshold factor) and `(z^2+1)^2(z^2-1)^2` for D3 (cusp forms **and** thresholds). Poles in the disc: `+-q^{-1/2}` only. Levinson (`1203.6557:levinson2.tex:511`) closes the loop: the winding of `det S` round the circle is `4 = 2(6-2-2-0)` (D2) and `6 = 2(9-2-2-4/2)` (D3), `= N - n_b` in both cases. |
| **D11** | T1(c) | "determine `dim ker T_X` and whether both [cusp forms] vanish at `B`" | D2: `dim ker T_X = 2` and **both** vanish at `B`, so both are cusp forms and the factor is `(z^2+1)^2`. D3: `dim ker T_X = 3` but only **2** vanish at all of `L1, Z, Q`; the third is **not** an `l^2` eigenfunction of `T` on `Y`. So `dim ker T_X` is *not* the cusp-form count in general. On the truncated diagram the third appears as a bipartite-imbalance zero mode with a non-decaying tail, and the genuine cusp forms are found as the subspace of `ker T` vanishing identically on the rays (`L = 120` and `L = 200`, same answer). |
| **D12** | T1(c) | `l^2` spectrum: Perron pair `+-3/sqrt2` (D2), cusp forms at `lambda = 0` | **CORRECT.** D2: `lambda = +-2.121320 = +-(q^{1/2}+q^{-1/2})`, nothing else outside `[-2,2]`; `lambda = 0` with multiplicity 2. D3: `lambda = +-2.309401`, `lambda = 0` multiplicity 2. So `RAM(Y)` holds on both diagrams. Eigenvectors decay to `1e-14` on the last 30 ray sites. |
| **D13** | T1(c) | resonances are the roots of `2z^4-2z^2+1`, `z^2 = 1/alpha`, `|z| = 2^{-1/4}` | **CORRECT.** D2: `z = 2^{-1/4} e^{i theta}`, `theta = +-22.5, +-157.5` degrees, `|z| = 0.840896415`, spread `4e-16`; `z^2` takes each root of `P(T)` twice. D3: `3^{-1/4} = 0.759835686`, angles `+-45, +-135`. |
| **D14** | T1(c) | "`Z` is a square root of the inverse Frobenius on `H^1(E)` tensored with the bipartite sign. State exactly in what sense." | Made precise and verified: `sigma^2 = 1`, `sigma Z sigma = -Z`, `[sigma, Z^2] = 0`; each `sigma`-eigenspace of `K_HW` is 2-dimensional and `Z^2` on it has spectrum exactly `{1/alpha, 1/conj alpha}`. **So `K_HW = H^1(E) (x) C^2` with `Z^2 = Frob^{-1} (x) 1` and `sigma = 1 (x) diag(+1,-1)`, and `Z` is a square root of `Frob^{-1} (x) 1` that ANTI-commutes with the bipartite sign.** |
| **D15** | T1(b) | `1/R(z) = z^{-2} zeta_K(2s-1)/zeta_K(2s)` exactly | **EXACTLY CORRECT**, as a rational-function identity (not just at sample points), and it is `1/R`, not `R`. Also checked numerically at `s = 0.31+0.22i, 0.77-0.4i, 1.3+0.9i, 0.5+14.13i` against `S` computed from `Gamma`, dev `9e-16`. |
| **D16** | T1(b) | H-EIS: the prefactor pattern `q^{1-2gs}` | **Cannot be separated** by these data. Genus 0 gives `q = q^{1-2gs}|_{g=0}`; genus 1 gives `z^{-2} = q^{1-2s}`, which is *both* `q^{1-2gs}|_{g=1}` and `q^{1-2s}`. D3's even block gives the same `q^{1-2s}` attached to `zeta(2s-1)/zeta(2s)`. Two genus-1 points and one genus-0 point cannot distinguish `q^{1-2gs}` from `q^{1-2s}`. **H-EIS stays unasserted.** |
| **D17** | T1(e) | finding 7; `prod_{nonzero} = (-2)(1)(1/2) = -1`; "derive it as a determinant or coefficient statement" | **CORRECT, and sharpened.** The coefficient statement: `prod (nonzero roots of p) = (-1)^{2n-m} [z^m]p / lc(p)` where `m = ord_0 p`; equivalently `[z^m]p = lead(ptilde)`. For **both** diagrams `[z^m]p = -1`, so the product is `-1`. Consequence (new): `prod|nonzero resonances| = prod|l^2 parameters| = 1/q` exactly (`0.5` and `0.3333`), and since the only `l^2` modes outside the band are the Perron pair `+-q^{-1/2}` and the `4 = 4g` Hasse--Weil resonances share one modulus, **`r^4 = q^{-1}` forces `r = q^{-1/4}`**: the Weil radius is *pinned by the Perron pair alone*. This answers 04j's flag "nothing pins `r` to `q^{-1/4}`". |
| **D18** | T2(b) | `(Q_1-Q_2)/sqrt2` has `S = -1`; `R = -1` because it vanishes at `Q` | **CORRECT**, with a cleaner reason: `Gamma` has rank 3 < h = 4 and annihilates `f_-`, so `S f_- = (0-1)^{-1}(1-0) f_- = -f_-` identically. |
| **D19** | T2(b) | `(L1-Z)/sqrt2` has `S = +z^2` (found numerically at three points); "prove it: ... find the reason, e.g. a hidden transparency" | **EXACTLY TRUE** as a rational-function identity. There is **no hidden transparency**. `p_odd = z^2(z^4-1)`, `ptilde_odd = 1-z^4`, `p_odd = -z^2 ptilde_odd`. The general criterion, proved symbolically: for **any** 3-path core with a `c = 1` cusp in the middle and couplings `a_1, a_2`, `p + z^2 ptilde = -z^2(z^2+1)^2(a_1^2+a_2^2-2)`, which vanishes identically **iff `a_1^2 + a_2^2 = 2`**. Here `a_1^2 = 4/3`, `a_2^2 = 2/3`. That one numerical identity is the whole reason. |
| **D20** | T2(b) | `det S_even = z^2 zeta_K(2s)/zeta_K(2s-1)` | **EXACTLY CORRECT.** Explicitly, with `Delta = (3z^2-1)(z^4+3)`, `S_even = Delta^{-1} [[z^2(z^2-1)(3z^4-2z^2+3), -4z^3(z^2+1)], [-4z^3(z^2+1), (z^2-1)(3z^4-2z^2+3)]]`. Note the exact internal relation `(S_even)_{11} = z^2 (S_even)_{22}`. |
| **D21** | T2(d) | H-CLASS: "the even 2x2 block does NOT have `z`-independent eigenvectors ... Decide: is there `D(z) = diag(z^a,z^b)` such that `D S_even D` has `z`-independent eigenvectors, with eigenvalues `{monomial x zeta ratio, monomial}`? Prove or refute." | The raw block indeed has `z`-dependent eigenvectors (`||[S(z_1),S(z_2)]||` up to `1.75`). **But the renormalisation EXISTS: H-CLASS is CONFIRMED, not refuted.** Scanning `a-b` over the half-integers in `[-4,4]`, the ratio `(z^{a-b}S_{11} - z^{b-a}S_{22})/S_{12}` is constant for **exactly one** value, `a-b = -1`. With `D = diag(1,z)` the block has equal diagonal entries, eigenvectors `(1,+-1)/sqrt2` (`z`-independent) and eigenvalues **exactly `z^2` and `z^2 zeta_K(2s)/zeta_K(2s-1)`**. Only the difference `a-b` matters. The brief's own physical guess — "the two `Q`-cusps start one step deeper (`12,36,...`) than the `L1,Z` cusps (`36,108,...`)" — is exactly right: `a-b = -1` is one ray step. With `D = diag(1,1,z,z)` on the four channels the spectrum of `S` becomes `z^2 * {1, 1, -1, zeta_K(2s)/zeta_K(2s-1)}`: **one zeta block and three monomial blocks**, the g = 1 prediction (`L(s,chi) = 1` for the three nontrivial unramified characters). |
| **D22** | T2(c) | "decide whether the MATRIX `S(z)` is regular at `+-1` for D3: I expect a nontrivial limit" | **REGULAR, with a nontrivial limit**, though `p` and `ptilde` both vanish to order 2 there. `S_even(+-1) = -(+-1) sigma_x` exactly (checked at `1 - eps` for `eps = 1e-5, 1e-7`); `det S_even(+-1) = -1`; the full `S(+-1)` has eigenvalues `{+1,-1}` (even) `+ {+1}` (e-) `+ {-1}` (f-), so `tr S(+-1) = 0`. Observation (2 data points, **not asserted**): `(h + tr S(+-1))/2` gives `2` for D3 and `0` for D2, matching APW's threshold multiplicities. |
| **D23** | T3(a) | `dim K = deg det Theta` = resonances with multiplicity incl. `z = 0`; "D2: a nilpotent block of size 2? decide" | **CORRECT**, `dim K(D2) = 6`. `char poly(Z) = prod(w - z_j)` to `3e-15`; `Z` is a contraction; `1 - Z^*Z = |j><j|` rank one (second singular value `8e-15`); `Z^m -> 0`; `dim ker Z = 1`, so the double resonance at `0` is a **single Jordan block of size 2** — the brief's guess is right. Also `sigma Z sigma = -Z` on `K`, with `sigma = diag((-1)^k)` an isometry because `p` and the Blaschke denominator are even. |
| **D24** | T4(a) | "the canonical cusp rebound `Omega_J = J^*J/Tr(J^*J)`; compute `rho_inf`, its spectrum, the holding law, aperiodicity, and whether `rho_inf` is supported on `K_HW`" | **A NEW NEGATIVE.** On the full `K(D2)`, `Theta(0) = prod z_j = 0` (because `c = 1` gives the double root at `z = 0`), and `||j||^2 = 1 - |Theta(0)|^2 = 1`. Hence `Z^*Z` is a **projection**, `Z` is a partial isometry, `Z j = 0`, the holding law is `m(1) = 1` and `m(m) = 0` for `m >= 2` (**deterministic holding time 1**, mean 1, `mhat(u) = u`), `rho_inf = Omega_J = |j><j|` is stationary and **pure**, and the Riesz projector gives `P_HW j = 0` to `1e-15`: **`rho_inf` lives entirely in the 2-dimensional delay sector and has zero overlap with the Hasse--Weil sector.** "Flux returns where it left" is the one rebound that never charges the arithmetic. This obstruction is not in the brief. |
| **D25** | T4(a) | same, but on APW's convention `mu in C^x` | Dropping the `z = 0` resonances gives the 4-dimensional Hasse--Weil model, `||j||^2 = 1 - q^{-2} = 3/4`. There `Omega_J` is non-degenerate: holding law `m = (3/4, 0, 1/12, 0, 1/48, 0, 1/12, ...)`, **supported on ODD times only** (because `sigma Z sigma = -Z` with `sigma j = +-j` kills `<j|Z^{m-1}|j>` for even `m`), gcd `= 1` so **aperiodic**; mean `= 7/3` exactly; `spec rho_inf = {1/7, 1/7, 1/7, 4/7}` exactly; `1` is a simple eigenvalue of `E_Omega`, the rest `<= 0.7827`, so `rho_inf` is unique and attracting. 04j's periodicity worry needs a *modal* rebound on a `z = 0` mode; `Omega_J` is not modal. |
| **D26** | T4(a) | "`Theta(u) = [-Z + u D_{Z^*}(1-uZ^*)^{-1}D_Z]` gives the exit-to-exit transfer function; derive `mhat` from it" | **The suggested derivation does not work.** `|Theta_Z| = |Blaschke over the resonances|` (dev `6e-16`), and its Taylor coefficients are `theta_{m+1} = <j'|Z^{*m}|j>` with `j'` the **second** defect vector (`1 - ZZ^* = |j'><j'|`), *not* `<j|Z^{*m}|j>` (the naive reading is off by `0.75` here; the two coincide only when `dim K = 1`). So `Theta` generates the **cross** amplitudes. `mhat` for `Omega_J` is the Hadamard square of the **diagonal** amplitudes: rational of degree `<= (dim K)^2`, and computed here from the superoperator, with `det(1 - u E_Omega) = det(1 - u E_0)(1 - mhat(u))` verified at `u = 0.3, -0.45, 0.6i`. |
| **D27** | T4(b) | mode-diagonal rebounds on `K_HW`: all stationary, mean `1/(1-2^{-1/2}) = 2+sqrt2` | **CORRECT.** Stationary for every weight vector (dev `6e-16`), mean `3.414213562 = 2+sqrt2` independent of the weights. Extra: the **exit rate is `<j|Omega|j> = 1 - q^{-1/2} = 0.292893` for every mode-diagonal `Omega`**, forced by the Gram identity `|<j|k_i>|^2/||k_i||^2 = 1 - |z_i|^2`. `spec rho_inf` is the Gram spectrum, not the weight list (04h reviewer M1 confirmed). |
| **D28** | T4(b) | a mode-diagonal rebound charging a `z = 0` mode is never stationary with the Hasse--Weil modes | **CORRECT.** `||E(Omega) - Omega|| = 0.0854`; the renewal sum still converges to a unique `rho_inf != Omega`, mean `2.207107 = (1/2)(1) + (1/2)/(1-q^{-1/2})`. |
| **D29** | T4(b)(c) | "the Lax--Phillips Gram matrix in closed form in `alpha`", "the angles between modes, in closed form" | In the normalisation `a_n = 1`, `G_nm = 1/(1 - conj(z_n) z_m)` with `conj(z_n) z_m` in `{+-q^{-1/2}, +-1/alpha, +-1/conj alpha}`; the four distinct `|G_nm|` are `1/(1-q^{-1/2}) = 2+sqrt2 = 3.414214` (diagonal), `1/(1+q^{-1/2}) = 2-sqrt2 = 0.585786` (`z` vs `-z`), `|q/(q-alpha)| = |alpha| = sqrt2` (`z` vs `conj z`) and `|q/(q+alpha)| = 2/sqrt10 = 0.632456` (`z` vs `-conj z`). The three off-diagonal cosines are exactly `(sqrt q - 1)/(sqrt q + 1) = 3 - 2sqrt2 = 0.171573`, `sqrt2 - 1 = 0.414214` and `(2-sqrt2)/sqrt10 = 0.185242`. |
| **D30** | T4(c) | `q^{1/4}Z` unitary for a cone of inner products of dimension 4 modulo scale; the `sigma`- and real-symmetric ones "form a smaller cone: describe it" | The cone is 4-parameter, i.e. **3-dimensional modulo scale** (the brief's "dimension 4 ... modulo scale" reads either way; the weights are 4, the projective cone is 3): `H_w = V^{-*} diag(w) V^{-1}`, `w > 0`, verified `U^* H_w U = H_w` to `3e-15` on three random `w`. The Lax--Phillips inner product is **not** in it (`||U^*U-1|| = 0.511`, `||[U,U^*]|| = 0.926`). **New:** the group generated by `z -> -z` (bipartite) and `z -> conj z` (real structure) acts **transitively** on the four Hasse--Weil modes, so an invariant weight vector must be constant: the symmetric sub-cone is a **single ray**. **The arithmetic inner product is unique up to scale**, namely `H = V^{-*}V^{-1}` (eigenvectors declared orthonormal). Read in it, a mode-diagonal `rho_inf` has spectrum exactly the rebound weights (dev `2e-16`); in the Lax--Phillips one it has the Gram spectrum. |
| **D31** | T3(c) | D3: `K = K_even (+) K_odd`, Hasse--Weil + 2 delay modes in `K_even`, 2 delay in `K_odd`, nothing from the `-1` channel | **CORRECT.** `6 + 2 + 0 = 8 = dim K`. `Theta_odd = z^2` gives `Z_odd = [[0,1],[0,0]]`, the free half line of 04i. A Dirichlet end has no model space. For genus one the hedgehog adds only trivial channels. |
| **D32** | T5 | the constant function is an `l^2` eigenfunction on a finite-volume diagram, invisible to every rebound | **CORRECT.** Volumes `sum_v 1/S(v)` are `10/3` (D2) and `7/4` (D3), finite; `f = 1` is an exact eigenvector of `A` with eigenvalue `q+1`, i.e. `lambda = (q+1)/sqrt q` (residual `1e-16`), parameter `z = q^{-1/2}` — a **pole** of `det S` in the disc, never a zero, hence removed by the Blaschke factor and **absent from `K`**. No rebound can give it an exit; the hedgehog does not help. |
| **D33** | T5 | `p_funnel(z) = det((1+z^2) - z T_X - C_cusp - q^{-1} C_funnel)`? | **CONFIRMED** on APW's own two worked examples, `q = 2,3,5`: the tree (one vertex, `q+1` funnels) gives `p = 1 + z^2 - (q+1)/q` with roots `+-q^{-1/2}`, matching APW's `H(mu) = -(mu - q^{-1}mu^{-1})/2` (`2603.26443:final_draft.tex:2000`); the modular curve (`q+1` cusps) gives `p = z^2 - q` with roots `+-q^{1/2}`. The pair fixes the relative factor `q^{-1}` on `C_funnel`. Still **H-FUNNEL**: no funnel diagram with a nontrivial core was built. |
| **D34** | T6 | `4g = 4` resonances for D2, D3 | **CORRECT** (4 each). The genus extrapolation is where it gets dangerous: see "what a refuter should attack", item 2. |
| **D35** | T4(d), T3(b) | Hecke / Bost--Connes; the generic `h`-exit renewal machinery | **NOT TESTED.** No Hecke data exists in H-DIAG. T3(b)'s `h`-dimensional-exit CPTP statements were not re-verified here (04j did the scalar-exit case; every renewal computation here has a scalar exit). |

---

## 3. The headline numbers

```
D2 (q=2)  p(z)      = (z^2/2)(z^2-2)(z^2+1)^2(2z^4-2z^2+1)          [exact]
          ptilde(z) = -(1/2)(z^2+1)^2(2z^2-1)(z^4-2z^2+2)           [exact]
          R = -p/ptilde ,  1/R = z^{-2} zeta_K(2s-1)/zeta_K(2s)     [exact]
          resonances  2^{-1/4} e^{i theta},  theta = +-22.5, +-157.5 deg   (|z| = 0.840896415)
                      + a double 0  ->  N = 6,  dim K = 6, Jordan block of size 2 at 0
          l^2 spectrum  lambda = +-2.121320 (Perron) and 0 (mult 2, cusp forms)
          Gram (a_n = 1)  diag 2+sqrt2 = 3.414214; off 2-sqrt2, sqrt2, 2/sqrt10
          cosines         0.171573 = 3-2sqrt2 ;  0.414214 = sqrt2-1 ;  0.185242 = (2-sqrt2)/sqrt10
          Omega_J on K    holding time == 1, rho_inf = |j><j| in the DELAY sector, P_HW j = 0
          Omega_J on K_HW holding law (3/4, 0, 1/12, 0, 1/48, ...), mean 7/3, spec {1/7,1/7,1/7,4/7}
          mode-diagonal   stationary, mean 2+sqrt2 = 3.414214, exit rate 1-q^{-1/2} = 0.292893

D3 (q=3)  p(z)      = (z^4/3)(z^2-1)^2(z^2-3)(z^2+1)^2(3z^4+1)      [exact]
          S in the fixed Klein basis  =  -1  (+)  z^2  (+)  S_even
          S_even    = [[z^2(z^2-1)(3z^4-2z^2+3), -4z^3(z^2+1)],
                       [-4z^3(z^2+1), (z^2-1)(3z^4-2z^2+3)]] / ((3z^2-1)(z^4+3))
          det S_even = z^2 zeta_K(2s)/zeta_K(2s-1)                  [exact]
          D = diag(1,z):  eigenvalues  z^2  and  z^2 zeta_K(2s)/zeta_K(2s-1),
                          eigenvectors (1,+-1)/sqrt2, z-INDEPENDENT
          resonances  3^{-1/4} e^{i theta}, theta = +-45, +-135 deg + 0 of order 4 -> N = 8
          thresholds  S_even(+-1) = -(+-1) sigma_x, regular; tr S(+-1) = 0
          dim K = 6 (even) + 2 (odd) + 0 = 8
```

---

## 4. What a refuter should attack first

1. **The `z = 0` sector is doing too much work.** `dim K`, the Jordan block, `||j||^2 = 1`, the
   collapse of `Omega_J` to a deterministic one-step channel, and the "delay sector" all come from
   `p(0) = det(1-C) = 0`, i.e. from `c^2 = 1`. Is `z = 0` a resonance *of the diagram* at all, or an
   artefact of putting the attachment vertex outside the ray? Childs--Gosset's origin (D9) shifts it
   by `z^2`. If the right convention kills the `z = 0` roots, D24 evaporates and D25 is the truth.
2. **The `r = q^{-1/4}` "pinning" (D17) proves too much.** The same argument at genus `g` gives
   `r^{4g} = q^{-1}`, i.e. `r = q^{-1/(4g)}`, which contradicts Weil for `g >= 2`. Either
   `[z^m]p = -1` fails for `g >= 2`, or arithmetic diagrams of higher genus carry extra `l^2`
   spectrum outside the band. Build a genus-2 diagram and find out; this is the sharpest testable
   consequence in the whole round.
3. **H-CLASS for D3 (D21) rests on one numerical coincidence.** `(S_even)_{11} = z^2 (S_even)_{22}`
   is what makes `a-b = -1` work. Is that relation forced by the ray depths (`S(c_1) = 12` versus
   `36`), or is it special to this curve? A second four-cusp example with different cusp depths
   would settle it. Likewise `a_1^2 + a_2^2 = 2` in D19.
4. **The "unique arithmetic inner product" (D30)** uses transitivity of `{z -> -z, z -> conj z}` on
   the four modes. That fails as soon as `P(T)` has a real root (`a = 0` gives `alpha = +-i sqrt q`,
   and indeed for D3 the four resonances are `3^{-1/4}e^{+-i pi/4}, 3^{-1/4}e^{+-3i pi/4}` — still
   one orbit, but check it), and it will fail for higher genus where `2g > 2` eigenvalue pairs give
   several orbits. The claim is "unique for D2", not "unique in general".
5. **Everything downstream of H-LP is inherited, not re-proved here.** I never built the energy
   completion for these diagrams; `K`, `Z` and `j` are the *model-theoretic* objects attached to the
   inner part of `S`, exactly as 04i's numerics D10 flagged. If the geometric `K` differs from the
   model `K` (04i found it does, in `l^2`), Sections 6--8 describe the model, not the diagram.


---

**Erratum (orchestrator, after review).** Section 1 states `T_X = D^{-1/2} A_X D^{-1/2}/sqrt q` with `A_X` the coordinate adjacency `S(v)/S(e)`; that matrix is not symmetric. The correct similarity is `T_X = q^{-1/2} D^{-1/2} A_X D^{1/2}` (equivalently `D^{-1/2}` (measure kernel) `D^{-1/2}`); the script builds `sqrt(S(u)S(v))/(S(e) sqrt q)` directly, so no computation is affected (review finding 10).
