# Numerics lane: a finite graph with a cusp

Author: `claude:opus`. Date 2026-09-20. Run blind to the prover's file, from the brief
`notes/cusp-graph/astra-brief.md` alone.

Script `scripts/cusp_graph.py` (python3 + numpy/scipy, seed 20260920, ~10 s), captured output
`outputs/cusp_graph.txt`. **569 checks, all asserted with tolerances, all passing.** Every formula
below was re-derived from the brief's *definitions*; the brief's *displayed* formulas were treated
as conjectures and are corrected where wrong.

---

## 0. Conventions I fixed

* **Indexing.** Core vertices `0..n-1` with `v_0 = 0`; ray vertex `r_k` at ambient index `n+k-1`.
  `(T g)(r_1) = g(r_2) + c g(v_0)`, `(T g)(r_k) = g(r_{k+1}) + g(r_{k-1})` for `k >= 2`.
* **Polynomials.** `p(z) = det((1+z^2) I - z T_X - c^2 P_0)`,
  `ptilde(z) = det((1+z^2) I - z T_X - c^2 z^2 P_0)`, computed by evaluating the determinant at the
  `(2n+1)`-th roots of unity and inverting the DFT (exact to machine precision, well conditioned).
* **Krylov reduction (new, and load-bearing).** Let `Kry = Krylov(T_X, v_0)`. Its orthocomplement is
  the largest `T_X`-invariant subspace inside `v_0^perp`, i.e. *exactly* the cusp forms. Hence
  `p(z) = p_red(z) * prod_{cusp forms} (z^2 - lambda z + 1)` with `deg p_red = 2(n - mu)`,
  `mu` the total cusp multiplicity (checked at coefficient level on all 19 cores, dev `<= 1e-8`).
  All root finding is done on `p_red`, where no root is forced to be multiple; this is what makes
  Petersen (cusp multiplicity 7) numerically clean.
* **Counting symbols.** `t_nc` = number of `l^2` eigenvalues of `T` on `Y` outside `[-2,2]` whose
  eigenfunction does *not* vanish at `v_0`; `mu` = cusp multiplicity; `e` = cusp forms with
  `|lambda| < 2`; `beta` = band-edge common roots at `z = +-1`; `t = t_nc + (cusp forms outside the
  band)` = all `l^2` eigenvalues outside the band.
* **Energy form.** `E = [[I, -T/2], [-T/2, I]]`, `W = [[T, -I], [I, 0]]`. `W^T E W = E` exactly
  (dev `0.0`).
* **Model.** For the renewal sections `C` is the Sz.-Nagy--Foias model of a contraction with defect
  indices `(1,1)` and characteristic function the Blaschke product over the graph's resonances:
  `G_nm = 1/(1 - conj(z_n) z_m)`, `C = G^{1/2} diag(z) G^{-1/2}`, `j = G^{-1/2} 1`. This is used
  because the direct `D_+/D_-` construction does not produce `K` in `l^2` (see D10).

---

## 1. Correction ledger

The brief's drafted formulas that are **wrong, too strong, or need a hypothesis**. This is the part
worth reading.

| # | Where | Brief says | What I find |
|---|---|---|---|
| **D1** | C1 | `R(z) = det(lam - T_X - c^2 z^-1 P_0)/det(lam - T_X - c^2 z P_0)`, and `R = p/ptilde` "up to a power of `z`" | Both are off by a **sign**, not a power of `z`. Exactly `R(z) = - p(z)/ptilde(z) = - det(...)/det(...)`; the power of `z` is **0**. The brief's own G-form `(1 - c^2 G/z)/(c^2 G z - 1)` is correct and already contains the minus. Sanity: `c -> 0` must give `R = -1` (Dirichlet), and it does. Verified against a direct solve of `T g = lam g` on the ray at 4 points of `|z| = 1` for 3 cores, dev `<= 1e-13`; the solve is exact (the ansatz solves the free recursion), `L = 40` and `L = 200` agree to `1e-13`. |
| **D2** | C1 | vertex measure `m(Lambda_n) ~ q^{-n}` | Not self-adjoint at the junction. Self-adjointness of `A` on `L^2(Y,m)` forces `m_0 : m_1 = q : (q+1)`, i.e. `m_0 = 1`, `m_n = (q+1) q^{-n}` for `n >= 1`. With the uncorrected `m_n = q^{-n}` for all `n`, `A - A^T` has max entry `q` (checked `q = 2,3,5`). With the correction, `g = m^{1/2} f` and division by `sqrt q` give the standard path adjacency and **`c^2 = q+1` exactly** — the brief's value is right. |
| **D3** | C1 | degree of `R` | `deg p = 2n` with leading coefficient `1` and `p(0) = 1 - c^2`; `deg ptilde = 2n` with leading coefficient `1 - c^2`. So **at `c = 1` the degree of `ptilde` drops** and `roots(ptilde) = 1/roots(p)` fails (`p(0) = 0`). The free half line `T_X = [0], c = 1` is exactly this case: `p = z^2`, `ptilde = 1`, `R = -z^2`. |
| **D4** | C2(i) | poles of `R` in `|z|<1` **are** the `l^2` eigenvalues of `T` outside `[-2,2]` | Too strong. A cusp form with `|lambda| > 2` *is* an `l^2` eigenvalue (its zero-extension is an exact eigenvector, dev `1e-12`) but is **cancelled** in `R`, so it is not a pole. Explicit core `cuspy w=-3`: cusp form at `lambda = +3.000000`, `2` `l^2` eigenvalues outside the band, only `1` pole of `R`. Corrected: poles of `R` inside the disc = the `l^2` eigenvalues outside `[-2,2]` **whose eigenfunction does not vanish at `v_0`** (count `t_nc`). |
| **D5** | C2(iii) | common factors of `p`, `ptilde` are **exactly** the cusp forms | Too strong. `p(+-1) = ptilde(+-1)` *identically* (because `ptilde(z) = z^{2n} p(1/z)`), so `z = +-1` is a common root whenever `p(+-1) = 0`, with no cusp form present. Explicit core: `T_X = [1]`, `c^2 = 3` shares the root `z = -1` (`lambda = -2`, the band edge) and has **no** cusp form. Corrected: common factors = cusp forms **plus** band-edge roots at `z = +-1`. Away from `z = +-1` the brief's statement is right, and after the Krylov reduction `p_red` and `ptilde_red` share *only* the band-edge roots (checked, all 19 cores). |
| **D6** | C2(iv) | "give the count of resonances" | The count is `#res = 2(n - mu) - t_nc - beta`, equivalently `2n - t - mu - e - beta`. Verified on all 19 cores (incl. K4, 3-cube, Petersen, `cuspy`, band-edge, free). The first form is the structural one: resonances live in the Krylov block. |
| **D7** | C3 | `R = (z^2-q)/(qz^2-1)`, no resonances, `1/R = q zeta_K(2s-1)/zeta_K(2s)` | **All correct**, no correction needed. At `q = 2,3,5,7`: `p = z^2 - q`, `ptilde = 1 - qz^2`, poles `+-q^{-1/2}`, zeros `+-q^{1/2}`, `0` resonances; at three complex `s` the ratio matches `1/R` to `1e-15` and differs from `R` by `O(1)`. So **`phi = 1/R`**: the poles of `phi` in `|z| < 1` are the *zeros* of `R`, i.e. the resonances, which is what makes shard 04's convention consistent with C2(iv). Everything downstream must use `1/R`. |
| **D8** | T1(a) | `D_+` = "data supported on the ray moving up" | Ambiguous, and the maximal reading is wrong. The *maximal* forward-invariant set of data whose solution vanishes on the core for all `m >= 0` is generated by `b_1 = (e_{r_1}, c e_{v_0})` and `b_j = (e_{r_j}, e_{r_{j-1}})`, `j >= 2`. But `<b_1, E f_1> = (1 - c^2)/2 != 0` unless `c = 1` (checked on 3 cores, and `<b_j, E f_k> = 0` for all `j >= 2, k >= 1` to `1e-12`). Lax--Phillips needs `D_+ perp_E D_-`, so **`D_+ = span{b_j : j >= 2}`**, i.e. the outgoing profile `B` must be supported on `k >= 2`, while `D_- = span{f_j : j >= 1}` (`F` supported on `k >= 1`). The asymmetry is real, not a slip. |
| **D9** | T1(b) | "prove `E > 0` there" | False as stated. `E` restricted to a `T`-eigenvector `psi` with eigenvalue `lambda` has signature `(1 - lambda/2, 1 + lambda/2)`: positive definite for `|lambda| < 2`, **indefinite** for `|lambda| > 2`, and *degenerate at `lambda = +-2`*. For every trivial mode both `W`-eigen-data `(psi, psi/z)` and `(psi, z psi)` are **`E`-null** (checked `<= 3e-16` on the pure cusp, `loop a=1 c^2=4`, K4): the trivial eigen-data plane is `E`-hyperbolic, not just indefinite. Separately, the two threshold profiles `u = v = 1` and `u = (-1)^k, v = -(-1)^k` on `r_P..r_Q` have `E = 2` **independent of the length** while `||.||^2` grows linearly: they are in the energy completion but **not in `l^2`**. |
| **D10** | T1(c) | `dim K` = number of resonances | **False in `l^2`.** With the corrected `D_+` and with `H_LP` the `E`-orthocomplement of *all* `l^2` eigen-data, the compactly supported part of `K` has `dim K_c = max(0, 2(n - mu - t_nc) - 2) = max(0, #res - t_nc + beta - 2)` — verified on all 19 cores at two ray cuts (`M = 8` and `M = 12`, identical). The deficit `t_nc + 2` is exactly: the **two threshold modes at `z = +-1`** (D9), plus **one `E`-isotropic direction per trivial mode** (removing the whole hyperbolic plane over-counts by one). Moral: the Lax--Phillips space is the energy completion, not `l^2`, and the trivial spectrum must be removed one isotropic direction at a time. I did not construct the completion, so `dim K = #res` there is *plausible arithmetic, not verified* (see §4). |
| **D11** | T1(c) | `spec Z` = resonances "or their reflections `1/conj z`" | It is the **resonances themselves**. `1/conj z` lies outside the closed disc and cannot be the spectrum of a contraction with `Z^m -> 0`. Checked on 4 models. |
| **D12** | T1(c) | Gram matrix "`1/(1 - z_n conj z_m)` up to normalisation" | The exact identity, which also *proves* no mode is dark, is `<k_n,k_m> (1 - conj(z_n) z_m) = conj(a_n) a_m` with `a_n = <j|k_n>` — an immediate consequence of `1 - C^*C = |j><j|` and `C k_n = z_n k_n`. If some `a_n = 0` then `<k_n,k_n> = 0`, absurd. So `a_n != 0` is not an extra fact to check, it is forced. Verified to `1e-14` on 4 models. |
| **D13** | T1(d) | "identify [the scattering matrix] with `R` or `1/R`" | **Neither.** `R(z) = - prod_i (z - z_i)/(1 - z_i z)` over the roots of `p`; the factors with `|z_i| > 1` are *inverse* Blaschke factors, so `R` has poles in the disc and is **not inner**. The product of `R` with the Blaschke product of the trivial modes is `+-` the Blaschke product over the roots of `p` inside the disc, i.e. (after the cusp factors cancel) over the **resonances** — and that is the characteristic function of `Z`. Checked two ways: the Blaschke product formula for `R` (dev `1e-8`), and `|Theta_Z| = |B_res|` for the model (dev `3e-16`). Note also the origin of the translation representation is only fixed up to a shift, so the scattering function is only defined up to a power of `z`: the free half line has `R = -z^2` with the "obstacle" a single site. |
| **D14** | T3(c) | asks whether aperiodicity is automatic when `Omega` sits on a **non-real** resonance | The relevant condition is `z != 0`, not non-reality: for `Omega = |k><k|`, `m(m) = |<j|k>|^2 |z|^{2m-2} > 0` for every `m >= 1`, so `gcd = 1` for **any** nonzero resonance, real or not (checked on 4 models). The periodic counterexample needs `z = 0`, which by `p(0) = 1 - c^2` happens **iff `c = 1`**: the free half line has `p = z^2`, a double resonance at `0`, and model `Z = [[0,1],[0,0]]`; with `Omega = |psi><psi|`, `psi perp j`, the holding law is supported on `{2}` and `E_Omega` has the eigenvalue `-1` exactly. |
| **D15** | T3(d) | "`rho_inf` is mixed iff `Omega` is not a pure state that is ..." (left blank) | `rho_inf` is **pure iff `Omega = |psi><psi|` with `psi` an eigenvector of `C`** (then `rho_inf = Omega`). Checked: eigenvector `Omega` gives purity `1.000000`; a generic pure `Omega` gives `0.34`--`0.87`. |
| **D16** | T4 / T7(b) | "with the arithmetic normalisation `r = q^{-1/4}`"; "is `r` forced, e.g. by `prod = 1 - c^2`" | Nothing pins `r`. The product identity, in its usable form, is `prod_{|z_i|<1} |z_i| = |1 - c^2| * prod_t |z_t|` over the trivial modes (verified exactly on all 19 cores). Under RH(Y) with `R` resonances this fixes `r^R`, but only in terms of the *trivial* spectrum and `c`. Sharp consequence: **if `c^2 = q+1` and the only trivial modes are the Perron pair `+-q^{-1/2}`, then `prod|res| = 1`, impossible for moduli `< 1`, so there are no resonances at all** — the pure cusp's emptiness is forced by the identity, and resonances at `c^2 = q+1` require extra (deeper) trivial modes. `r = q^{-1/4}` is not implied by anything in the toy. |
| **D17** | T7(b) | `prod` of all roots of `p` `= 1 - c^2` "up to sign" | Exactly `1 - c^2`, no sign ambiguity: `deg p = 2n` (even) with leading coefficient `1`, so `prod z_i = p(0) = det(I - c^2 P_0) = 1 - c^2`. Verified on all 19 cores to `1e-8`. |
| **D18** | T7(d) | "give the smallest core with at least one non-real resonance pair" | `n = 1`. For `T_X = [a]`, `p = z^2 - a z + (1 - c^2)`, so a non-real pair needs `a^2 < 4(1 - c^2)`, hence **`c^2 < 1`**, and then `|z| = sqrt(1 - c^2)` automatically, so RH(Y) holds. Example `a = 1, c^2 = 1/2`: `z = (1 +- i)/2`, `r = 0.707107`. Consequence for the arithmetic round: **with `c^2 = q + 1 > 1` a one-vertex core has only real resonances**; the smallest core with a non-real pair *and* `c > 1` is `n = 2` (89 of 400 random 2--3 vertex cores with `c > 1`). |
| **D19** | T7(a) | "show by examples ... that RAM and RH are independent" | True, and sharper: a one-vertex core already realises `RAM&RH`, `RAM&!RH`, `!RAM&RH`, but **can never realise `!RAM & !RH`**, because `#res + #trivial <= 2n = 2` while `!RAM` needs 2 trivial modes and `!RH` needs 2 resonances. `n = 2` suffices for the fourth (100 of 400 random 2--3 vertex cores). |

Hypotheses the statements need, which the brief does not declare: **H-SIMPLE** (distinct resonances)
for the Gram model, the flag construction and the eigen-operator statements — it fails exactly for the
free half line; **H-NOEDGE** (`p(+-1) != 0`), without which D5 bites and `E` degenerates on a genuine
threshold state; **H-APERIODIC**, which by D14 is just `0` not a resonance, i.e. `c != 1`.

---

## 2. Tables

### 2.1 Per core: counts and the `l^2` Lax--Phillips dimension

`dimK_c` is the compactly supported `E`-orthocomplement of `D_+ (+) D_-` inside `H_LP`; the last
column is the formula of D10. Identical at ray cuts `M = 8` and `M = 12`.

```
 core                            n  #res  mu  t_nc  beta | dimK_c  2(n-mu-t_nc)-2
 pure cusp q=2                   1     0   0     2     0 |      0               0
 pure cusp q=5                   1     0   0     2     0 |      0               0
 free half line (c=1)            1     2   0     0     0 |      0               0
 loop a=1.0 c^2=0.5              1     2   0     0     0 |      0               0
 loop a=0.0 c^2=1.5              1     2   0     0     0 |      0               0
 loop a=0.5 c^2=1.2              1     2   0     0     0 |      0               0
 loop a=1.0 c^2=3 (band edge)    1     0   0     1     1 |      0               0
 loop a=1.0 c^2=4                1     0   0     2     0 |      0               0
 cuspy w=-3 (cusp lam=3)         3     3   1     1     0 |      0               0
 cuspy w=1  (cusp lam=-1)        3     3   1     1     0 |      0               0
 K4, q=2, c^2=3                  4     2   2     2     0 |      0               0
 3-cube, q=2, c^2=3              8     6   4     2     0 |      2               2
 Petersen, q=2, c^2=3           10     4   7     2     0 |      0               0
 random 3-vertex core #1         3     6   0     0     0 |      4               4
 random 3-vertex core #2         3     5   0     1     0 |      2               2
 random 4-vertex core #1         4     7   0     1     0 |      4               4
 random 4-vertex core #2         4     6   0     2     0 |      2               2
 random 5-vertex core #1         5    10   0     0     0 |      8               8
 random 5-vertex core #2         5     8   0     2     0 |      4               4
```

The `l^2` eigenvalues outside `[-2,2]` were computed independently by diagonalising `T` on a ray
truncated at `L = 400` and keeping the eigenvectors with tail norm `< 1e-6` on the last 40 sites;
they agree with `{z + 1/z : ptilde(z) = 0, |z| < 1}` to `<= 1e-7` on every core.

### 2.2 The three regular cores (`T_X = A/sqrt q`, `q = 2`, `c^2 = 3`)

| core | resonances | moduli | RH(Y)? | RAM(Y)? |
|---|---|---|---|---|
| K4 | `0.442513 +- 0.608338i` | `0.752259` (both) | **yes** (a single conjugate pair is automatically RH) | no |
| 3-cube | `+-0.759676 +- 0.449397i`, `+-0.900780 i` | `0.882647` (x4), `0.900780` (x2) | no | yes (bipartite: trivial `lam = +-2.245...`) |
| Petersen | `-0.187467 +- 0.807269i`, `0.812880 +- 0.387093i` | `0.828751` (x2), `0.900342` (x2) | no | no |

For reference `q^{-1/4} = 0.840896` and `q^{-1/2} = 0.707107` at `q = 2`. The moduli straddle
`q^{-1/4}` but no core hits it; nothing in the toy pushes them there (D16).

### 2.3 T7(a): RAM and RH over the one-vertex loop core

`a` in `{-3,-2,-1,-0.5,0,0.5,1,1.5,2,3}` x `c^2` in `{0.25,0.5,0.75,1.25,1.5,2,3,4,6}`, 90 cores.

```
 RAM=True  RH=True    72/90   e.g. a=-3.0 c^2=0.25: 1 resonance |z| = 0.275255, 1 trivial
 RAM=True  RH=False    2/90   e.g. a=-0.5 c^2=1.25: |z| = {0.309017, 0.809017},   0 trivial
 RAM=False RH=True    16/90   e.g. a=-3.0 c^2=6.00: 0 resonances,                 2 trivial
 RAM=False RH=False    0/90   impossible for n = 1 (D19)
```

Non-vacuous versions (both `>= 2` resonances and `>= 2` trivial modes), from 1200 random cores:

```
 RAM=True  RH=True   bipartite n=3 c=2.195  |z_res| = {0.952369 x2}                        trivial lam = +-2.539101
 RAM=True  RH=False  bipartite n=4 c=1.424  |z_res| = {0.811331 x4, 0.948932 x2}           trivial lam = +-2.239142
 RAM=False RH=True   generic   n=2 c=2.204  |z_res| = {0.977579 x2}                        trivial lam = {-2.614249, 2.410808}
 RAM=False RH=False  generic   n=4 c=0.526  |z_res| = {0.352038, 0.515975, 0.949642 x2, 0.999904 x2}  trivial lam = {-2.412621, 2.773871}
```

Observation worth stating: **RAM(Y) non-vacuously (two trivial modes) essentially forces a bipartite
core**, because the two trivial eigenvalues must be exactly `+-lambda_top`; no generic symmetric core
in 600 tries had it, every bipartite one did. So in this toy "Ramanujan" is a *bipartiteness plus
gap* condition, and it constrains the even sector, while RH constrains the odd one.

### 2.4 T7(c): a checkable criterion

Let `p_res(z) = prod (z - z_i)` over the resonances (real coefficients), `d = #res`, `r` the common
modulus candidate, `b_k = c_k r^{k-d}`. Then

> **RH(Y) holds iff `b_k = b_0 b_{d-k}` for all `k`** (`r`-self-reciprocality), and then `|b_0| = 1`.

Verified as an *iff* on all 15 cores with `>= 2` resonances: deviation `<= 5e-16` for every RH core
(`loop a=1 c^2=0.5`, `loop a=0 c^2=1.5`, K4, `|b_0| = 1.000000`), and `0.08`--`0.91` for every
non-RH core (`|b_0|` ranging `0.38`--`0.9997`). This is the brief's T7(c) guess, made precise.

### 2.5 Renewal channel (T3--T6), four models

`Omega` random density unless stated. Every model: CPTP (Choi min eigenvalue `> -5e-16`), holding law
non-negative and telescoping exactly (`sum_1^M m(m) = 1 - Tr(C^M Omega C^{*M})`, remainder
`< 1e-280`), mean `= Tr X` with `X - C X C^* = Omega` (agreement `< 1e-6` relative), `rho_inf`
stationary (`< 1e-10`), agreeing with the null vector of `1 - E_Omega` (`< 1e-8`) and with 4000
iterations from a random density (`< 2e-12`), spectral gap of `E_Omega` strictly `< 1`, and
`det(1 - u E_Omega) = det(1 - u E_0)(1 - mhat(u))` at four complex `u` (`<= 1.3e-14`).

| model | `#res` | moduli | `mu_Omega` (mode-diag) | `rho_inf = Omega`? |
|---|---|---|---|---|
| `loop a=1 c^2=0.5` | 2 | `0.707107` (x2) | `2.000000 = 1/(1-r^2)` | **yes** (`3e-16`) |
| `loop a=0.5 c^2=1.2` | 2 | `0.262348, 0.762348` | `1.134007` | no (`4.3e-2`) |
| K4 | 2 | `0.752259` (x2) | `2.303579 = 1/(1-r^2)` | **yes** (`2e-16`) |
| random 3-vertex #2 | 5 | `0.138, 0.898 (x2), 0.922 (x2)` | `4.911815` | no (`1.3e-1`) |

So T4's "`rho_inf = Omega` for every mode-diagonal `Omega` iff all `|z_i|` coincide" holds as an
**iff** on the four models, and under uniform modulus `mu = 1/(1-r^2)` independently of the mixture.
The 04h reviewer's point is confirmed: the spectrum of `rho_inf` is a **Gram spectrum**, not the
weight list — e.g. `loop a=1 c^2=0.5` with weights `{0.188121, 0.811879}` gives
`{0.142488, 0.857512}` (mode overlap `0.4472`).

T5: `Tr Q_sigma = <j|sigma|j>` exactly (`1e-11`); a *random* density fails `Q_sigma >= 0` on all four
models (min eigenvalue `-0.04` to `-0.38`), so admissibility is a genuine restriction; the
`C`-invariant flag of resonance eigenvectors gives `Q_k >= 0` and a `sigma` with the **prescribed**
spectrum (`1e-9`) which is stationary for its own `Omega` (`1e-10`); and in the resonance basis
`Q_sigma` has coefficient matrix `sigma_nm (1 - z_n conj z_m)` — an entrywise Schur factor (`1e-9`).

T6: on `C vac (+) K` with `C vac = vac` the defect identity survives, and for three random rebound
densities on the *graded* space each `|k_i><vac|` is an eigen-operator with eigenvalue **`z_i`**, not
`conj z_i` (dev `<= 7e-16`), because the exit functional annihilates odd operators.

---

## 3. Two positive structural findings the brief did not ask for

1. **`p` factorises through the Krylov space.** `p = p_red * prod_{cusp}(z^2 - lambda z + 1)` with
   `deg p_red = 2 dim Krylov(T_X, v_0)`. The resonances and the non-cusp trivial modes are entirely a
   property of the Krylov compression `(T_X|_Kry, v_0, c)`; the cusp forms contribute only unimodular
   or reciprocal-pair factors. Equivalently: **the cusp sees only the cyclic part of the core.** This
   also gives the cleanest form of C2(iii): after the reduction, `p_red` and `ptilde_red` share only
   the band-edge roots.
2. **The product identity is the whole obstruction to resonances at `c^2 = q+1`.**
   `prod_{|z|<1, p(z)=0} |z| = |1 - c^2| prod_{trivial} |z_t|`. With `c^2 = q+1` and the Perron pair
   `+-q^{-1/2}` as the only trivial modes, the right side is `q * q^{-1} = 1`, so there is no room for
   a single resonance. Any arithmetic quotient with resonances must therefore have `l^2` spectrum
   outside the band beyond the Perron pair — this is a concrete, checkable demand on the next round.

---

## 4. What I could not test

* **T2** (the cusp trace formula, walk expansions of `log p`, `-d/dz log R`) — outside my remit here;
  nothing in this report bears on it.
* **T8 / H-ARITH** — no arithmetic input at all; no `Gamma_0(N)` quotient, no Dirichlet `L`-function
  over `F_q[T]`, no `h > 1` matrix scattering. Everything above is one cusp.
* **`dim K = #res` in the energy completion.** I verified the `l^2` deficit is exactly `t_nc + 2` and
  identified both sources (D9, D10), but I did not build the energy-space completion (the threshold
  tails are `E`-isotropic and a truncated ray adds a spurious seam term, so the `E`-Gram of the
  completed space is not directly computable on a finite cut). Consequently `Z` was built from the
  functional model of the resonance Blaschke product, not by compressing `W` to a graph-side `K`. The
  link between the two is the Sz.-Nagy--Foias theorem plus my check that `R * B_trivial = +- B_res`
  and `|Theta_Z| = |B_res|`; the *operator* unitary equivalence is asserted, not verified.
* **Degenerate resonances.** Everything with a repeated resonance other than `z = 0` is untested
  (H-SIMPLE); the Gram model does not exist there and a Jordan model is needed. The only degenerate
  case I did handle is the free half line (`z = 0` double).
* **Cores with `beta >= 1` and resonances simultaneously.** My only band-edge example
  (`T_X = [1], c^2 = 3`) has `#res = 0`, so the threshold Jordan-block phenomenon is not exercised.
* **Infinite-mean holding times**: impossible in finite dimension, so 04h's infinite-mean rebound has
  no discrete analogue here; nothing to test, but also nothing to transfer.
* **Whether `r = q^{-1/4}` is achievable at all** for a core with `c^2 = q+1`: I showed it is not
  forced and showed the Perron-pair-only case is empty, but did not search for a core whose deeper
  trivial spectrum makes `r = q^{-1/4}` exactly.
