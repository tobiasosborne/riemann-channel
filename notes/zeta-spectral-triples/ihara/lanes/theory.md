# The Connes-Consani-Moscovici chain over `Z`: the Ihara zeta of a finite regular graph

Lane: mathematics prover, `notes/zeta-spectral-triples/ihara/lanes/`. Session 2026-09-18.
Author `claude:opus-5`. Nothing here is a registered lab-book claim; the claims below are
numbered `IH-n` and carry their own status.

**Sources cited by line.**
`CCM` = `refs/src/2511.22755/mc2arXiv.tex` (Connes-Consani-Moscovici, *Zeta spectral triples*).
`CS` = `refs/src/2511.23257/Araki-final-oct25.tex` (Connes-van Suijlekom, *Quadratic forms, real
zeros and echoes of the spectral action*), the `[CS]` that CCM cite at `CCM:292` and `CCM:839`.
`plan` = `notes/zeta-spectral-triples/plan.md`. Notebook claim ids are looked up in `db/claims.tsv`.

**Status legend.** `PROVED` = complete proof given here or a precise citation to a complete proof.
`CLAIMED` = argument given, gap named. `OPEN` = no argument.

**Numerical verification.** Every computational claim below was checked in this lane against the
Petersen graph (`q = 2`, `|V| = 10`, `|E| = 15`, adjacency spectrum `3, 1^5, (-2)^4`) and the
non-Ramanujan prism `C_16 x K_2` (`q = 2`, `|V| = 32`), at double precision, before being written
down. Targets for the numerics lane are collected in section 9.

---

## 0. Standing notation

`X` a finite connected `(q+1)`-regular graph, `q >= 2`, `|V|` vertices, `|E| = (q+1)|V|/2`
undirected edges, `A` the adjacency matrix, `B` the Hashimoto (non-backtracking edge) operator on
`C^{2|E|}` (`def:hashimoto-operator`, `report/sections/02_definitions.tex:79`). `r = |E|-|V|+1` is
the first Betti number, so `|E|-|V| = r-1 = -chi(X)`.

- Ihara-Bass (`def:ihara-bass`, `02_definitions.tex:87`):
  `Z_G(u)^{-1} = det(1-uB) = (1-u^2)^{|E|-|V|} det(1 - Au + q u^2)`.
- `N_k = Tr B^k = sum over prime classes [C] with |C| dividing k of |C|` (the graph von Mangoldt),
  `N_0 := Tr B^0 = 2|E|`.
- Spectrum of `B`, with multiplicity: for each `lambda in spec(A)` the two roots of
  `mu^2 - lambda mu + q = 0`, together with `+1` and `-1` each with multiplicity `|E|-|V|`.
- **Trivial divisor** `S_triv`: `{q, 1}` (from `lambda = q+1`), plus `{-q, -1}` if `X` is bipartite
  (from `lambda = -(q+1)`), plus `+1` and `-1` each with multiplicity `|E|-|V|`.
  **Retained divisor** `A_ret` = the rest; `|A_ret| = 2|V|-2`, or `2|V|-4` if bipartite.
  This is `def:graded-transfer-channel`'s trivial/retained bookkeeping
  (`report/sections/02h_definitions_graded_ramanujan.tex:20`) specialised to `X = B`, `trivS`,
  critical radius `sqrt q`.
- **Rescaling** `w = mu / sqrt q`. `eps_bip = 1` if `X` is bipartite, else `0`.
- **Window.** `W = {0,1,...,K-1} subset Z`, `K = 2M+1`; `l^2(W) = C^K`. Because the form below is
  translation invariant, `{-M,...,M}` gives literally the same matrix, so the position of the window
  is irrelevant. This is already a difference from CCM, whose window `[lambda^{-1}, lambda]` is
  pinned at `1` by the inversion symmetry `iota` (`CCM:479`, Lemma `wsharp`).
- Inner products are antilinear in the first slot, as in `CCM:326`.
- `eta := delta_0` (the position delta at the cut point of the window), `Z` = cyclic shift on
  `Z_K`, `(Zf)_j = f_{j-1 mod K}`, `z_n = exp(2 pi i n / K)`, `theta_n = 2 pi n / K`,
  `e_n(j) = K^{-1/2} z_n^j` the DFT basis (so `Z e_n = z_n^{-1} e_n`, `Z^* e_n = z_n e_n`).

---

## 1. The explicit formula of the Ihara zeta in CCM's shape

### 1.1 The two-sided sequence

**IH-1 (PROVED). Reality and the two extensions.**
Set `t_k := sum_{mu in A_ret} (mu / sqrt q)^k` for `k >= 0`. Then

  (i) `A_ret` is closed under complex conjugation and under `mu -> q/mu` (equivalently `w -> 1/w`);
  (ii) `t_k` is real for every `k >= 0`;
  (iii) the **Hermitian** extension `t_{-k} := conj(t_k)` and the **inverse** extension
       `t^inv_{-k} := sum_{mu in A_ret} (q/mu)^k q^{-k/2}` coincide, and both equal `t_k`;
  (iv) the full spectrum of `B` is **not** closed under `mu -> q/mu`: the image of `+1` (multiplicity
       `|E|-|V|+1`) is `q`, which has multiplicity `1`; so (iii) is a statement about `A_ret` only,
       and it is false for the unrescaled trace sequence `Tr B^k`.

*Proof.* (i) `B` is a real matrix, so its characteristic polynomial is real and `spec(B)` is
conjugation closed with multiplicity; `S_triv` is a set of real numbers with conjugation-symmetric
multiplicities; hence `A_ret` is conjugation closed. Each retained `lambda != +-(q+1)` contributes
exactly the two roots of `mu^2 - lambda mu + q`, whose product is `q`, so the pair `{mu, q/mu}` lies
in `A_ret` with equal multiplicities. (ii) follows from (i) since `sqrt q` is real. (iii) `t^inv_{-k}
= sum (q/mu)^k q^{-k/2} = sum (sqrt q / mu)^k = sum (1/w)^k`, and `w -> 1/w` permutes `A_ret/sqrt q`
by (i). (iv) `1` occurs in `spec(B)` with multiplicity `|E|-|V|+1` (the `|E|-|V|` copies plus the one
from `lambda = q+1`), while `q` occurs once (`|V| > 1`); the Perron root of `B` is `q` with
multiplicity `1`. QED

**IH-2 (PROVED). Which extension is the right one for a Hermitian window form.**
The Hermitian one, `t_{-k} = conj(t_k)`. Reason: the window form is `QW_M(f,g) = Psi_G(f^* * g)`
with the `l^1(Z)` involution `f^*(k) = conj(f(-k))` (`CCM:318`, the discrete counterpart of
`\eqref{pinvolution}`); `QW_M` is sesquilinear, and it is Hermitian **iff** `t_{-k} = conj(t_k)`.
The inverse extension is not a definition but a *theorem about the divisor* (`IH-1`(iii)); it is a
form of the functional equation, is exactly the hypothesis of `thm:weil-duality-pairing`
(`08b_weil_positivity.tex:87`, status `proved`), and it fails for irregular graphs
(section 6). Using it as a definition would silently assume the functional equation.

### 1.2 The identity

**IH-3 (PROVED). Explicit formula for the Ihara zeta in CCM's shape.**
For `F: Z -> C` finitely supported set `F^(w) := sum_{k in Z} F(k) w^k` and

    Psi_G(F) := sum_{mu in A_ret} F^(mu / sqrt q)   ( = sum_{k in Z} F(k) t_k ).

Then

    Psi_G(F) = W_C(F) - W_{0,2}(F) - W_R(F),

with the three pieces

    W_C(F)   = sum_{k in Z} q^{-|k|/2} N_{|k|} F(k)
             = 2|E| F(0) + sum_{[C]} sum_{m>=1} |C| q^{-m|C|/2} ( F(m|C|) + F(-m|C|) ) ,
    W_{0,2}(F) = ( 1 + eps_bip (-1)^k )-weighted pole pair
             = sum_{k in Z} ( q^{|k|/2} + q^{-|k|/2} ) ( 1 + eps_bip (-1)^k ) F(k) ,
    W_R(F)   = (|E|-|V|) sum_{k in Z} ( (q^{-1/2})^{|k|} + (-q^{-1/2})^{|k|} ) F(k) .

Equivalently, lag by lag, for every `k >= 0`

    t_k = q^{-k/2} N_k  -  (1 + eps_bip (-1)^k)(q^{k/2} + q^{-k/2})  -  (|E|-|V|)(1+(-1)^k) q^{-k/2}.

*Proof.* `Tr B^k = sum_{mu in spec B} mu^k` (with multiplicity), valid for `k >= 1` and for `k = 0`
with `N_0 = 2|E|`. Split `spec B = S_triv + A_ret` using the multiplicities listed in section 0 and
Ihara-Bass; the trivial part contributes `q^k + 1` (from `lambda = q+1`), plus `(-q)^k + (-1)^k` if
bipartite, plus `(|E|-|V|)(1^k + (-1)^k)`. Multiply by `q^{-k/2}` and rearrange. The prime-cycle
form of `N_k` is `def:ihara-zeta` (`02_definitions.tex:73`) together with `u d/du log Z_G(u) =
sum_k N_k u^k`; expanding `-log prod_{[C]}(1-u^{|C|})` gives `N_k = sum_{|C| divides k} |C|`.
Finally `sum_k F(k) t_k = sum_{mu in A_ret} sum_k F(k) (mu/sqrt q)^k = Psi_G(F)`, all sums finite. QED

*Verified* on Petersen: `N_k = 30, 0, 0, 0, 0, 120, 120, 0` for `k = 0..7`, and
`t_k = 18, -2.121320, -7.5, -3.181981, -6.75, 15.379572, 5.625, -11.402097, ...` computed from the
identity agrees with `sum_{A_ret} w^k` to `1e-14`.

**IH-4 (PROVED). Dictionary of the three pieces.**

| CCM | line | graph |
|---|---|---|
| `W_p(F) = (log p) sum_m p^{-m/2}(F(p^m)+F(p^{-m}))` | `CCM:445` | `|C| sum_m q^{-m|C|/2}(F(m|C|)+F(-m|C|))` |
| `W_{0,2}(F) = F^(i/2) + F^(-i/2)`, rank two | `CCM:469`, Lemma `w02` `CCM:684` | `q^{|k|/2}+q^{-|k|/2}` (times `2` at even `k` if bipartite), rank two |
| `W_R`, kernel `rho(x) = e^{x/2}/(e^x-e^{-x}) = sum_{n>=0} e^{-(2n+1/2)x}` | `CCM:450`, `plan:67` | `(|E|-|V|)((q^{-1/2})^{|k|} + (-q^{-1/2})^{|k|})` |

Units: CCM's atoms sit at `y = log p^m` with weight `Lambda(p^m) p^{-m/2}`; the graph's sit at
`y = m|C| log q` with weight `|C| log q * q^{-m|C|/2}` if one keeps the same units. Working in the
length variable `k = y / log q` divides the whole distribution by `log q`, which is an overall
positive scalar: it rescales `tau` and `eps_M` but changes neither `xi` nor the returned divisor.
All formulas below use the length variable.

**IH-5 (CLAIMED). `W_R` is the graph's gamma factor.** Four reasons, of which the first is an
identity and the other three are interpretation:

1. (PROVED) `W_R` is exactly the log-derivative contribution of the factor `(1-u^2)^{|E|-|V|}` of
   Ihara-Bass, and that factor is exactly the completion that produces a clean functional equation:
   writing `P(u) := prod_{lambda nontrivial} (1 - lambda u + q u^2)` one has
   `(1-u^2)^{r-1}(1-u)(1-qu) Z_G(u) = 1/P(u)` and `P(1/(qu)) = (q u^2)^{-(|V|-1)} P(u)`, while
   neither `Z_G` nor `det(1-uB)` satisfies such an equation. So `(1-u^2)^{r-1}` is the "gamma
   factor" and `(1-u)(1-qu)` the "pole pair", exactly the split `W_R` / `W_{0,2}`.
2. Its atoms are a geometric series in the length variable, `c * s^{|k|}` with `s = q^{-1/2} =
   exp(-(1/2) log q)`: the discrete counterpart of `rho(x) = sum_{n>=0} e^{-(2n+1/2)x}`, with the
   same leading exponent `1/2` and the ladder truncated to a single rung (plus its sign-twisted
   partner `(-q^{-1/2})^{|k|}`, which is the ladder of the "period 2" / bipartite double cover).
3. Its multiplicity `|E|-|V| = -chi(X)` is topological, as the archimedean factor of a number field
   is determined by the data at infinity and not by the primes.
4. It sits strictly inside the critical circle (`|w| = q^{-1/2} < 1`), like the trivial zeros of
   `zeta` which sit off the critical line; it therefore contributes an *unboundedly positive* rank-`2`
   piece to the window form (the Poisson-kernel term of `thm:weil-positivity-finite`), never a
   negative one.

*What is missing:* a statement identifying `(1-u^2)^{r-1}` with an archimedean local factor in a
motivic sense. The notebook's own treatment (`07_deligne_via_graphs.tex:28`) records the term as
part of `N_k` without naming it a gamma factor.

### 1.3 The sign flip

**IH-6 (PROVED). The sign flip relative to CCM.** CCM's functional is
`Psi = W_{0,2} - W_R - sum_p W_p` and equals `sum over the nontrivial ZEROS` (`CCM:465`,
`\eqref{bombtest}`). The graph's is `Psi_G = W_C - W_{0,2} - W_R` and equals
`sum over the nontrivial POLES`. Every term changes sign: for `zeta` the trivial data (the pole pair,
the gamma factor) is on the left and the atoms on the right; for the graph the atoms are on the left
and the trivial data on the right.

*Reason.* For an ungraded object every side-B eigenvalue is a pole of the zeta function
(`prop:no-ungraded-zeros`(i), `03c_graded_ramanujan.tex:73`, status `sketched`; and
`07_deligne_via_graphs.tex:70`: "for the graph `Z_X` is the reciprocal of a polynomial and every
eigenvalue is a pole; for the curve the trivial eigenvalues `1` and `q` are poles and the interesting
ones are zeros"). In `def:graded-transfer-channel` language
(`02h_definitions_graded_ramanujan.tex:26`) the graded divisor is `nu = m_0 - m_1` and `nu > 0` are
poles; with `P = 1` there is no odd sector, so `nu = m_0 >= 0` everywhere and the retained divisor is
purely even. The Weil form on a retained divisor of graded multiplicity `nu_ret` is
`sum (-nu_ret(lambda)) |f^(lambda/sqrt q)|^2` (`plan:426`, line 448); it is positive semidefinite
exactly when `nu_ret <= 0`, i.e. when the retained points are **zeros**. For a graph they are poles,
so one must take `+nu_ret`, i.e. flip the global sign, which is what `Psi_G` above does.

*Practical warning for the implementation.* Feeding a graph's `(atoms, poles)` into a `zeta`-shaped
`zst_weil_t` (`plan:213`) with CCM's signs produces `-QW_M`, hence a **negative** semidefinite form,
hence "min eigenvalue" is the wrong extremum: the correct object for a graph is the eigenvector of
the **largest** eigenvalue of the zeta-signed matrix, or equivalently the smallest of the flipped
one. Makhoul's theorem (`IH-22`) covers both extremes, so the construction still works, but `eps_M`
changes sign and every inequality in the chain reverses.

---

## 2. The window Weil form, the displacement structure, and the discrete key lemma

### 2.1 The form is Toeplitz

**IH-7 (PROVED).** For `f, g` supported in `W = {0,...,K-1}`,

    QW_M(f,g) := Psi_G(f^* * g) = sum_{j,k in W} conj(f(j)) t_{k-j} g(k),

so the matrix of `QW_M` in the position basis is the Hermitian Toeplitz matrix `T_{jk} = t_{j-k}`,
which by `IH-1` is **real symmetric** (`t_d = t_{-d} real`). It involves lags `|d| <= K-1 = 2M`, i.e.
exactly the cycle counts `N_1, ..., N_{2M}`. This is the counterpart of CCM's "primes up to
`lambda^2 = e^L`" (`CCM:693`, `\eqref{bomp}` sums over `1 < k <= exp(L)`): the window of length
`L` needs atoms up to `L`, the window of `K` integers needs atoms up to `K-1`.

*Proof.* `(f^* * g)(y) = sum_x conj(f(x-y)) g(x)`, so
`Psi_G(f^**g) = sum_y t_y sum_x conj(f(x-y)) g(x) = sum_{x,x'} t_{x-x'} conj(f(x')) g(x)`. QED

**IH-8 (PROVED). Positivity.** `QW_M(f,f) = sum_{mu in A_ret} f^(mu/sqrt q) conj(f^(sqrt q/ conj(mu)))`,
which for a Ramanujan graph is `sum_{mu in A_ret} |f^(mu/sqrt q)|^2 >= 0`; a retained real pair
`{rho, 1/rho}`, `rho > 1`, contributes `2 m Re( f^(rho) conj(f^(1/rho)) )`, which takes both signs.
`QW_M >= 0` for every `M` iff `X` is Ramanujan. This is `thm:weil-positivity-finite`
(`08b_weil_positivity.tex:60`, status `proved`) plus `thm:weil-duality-pairing`
(`:87`, `proved`, whose hypothesis is `IH-1`(i)) plus `prop:weil-orbit-negative` (`:105`, `proved`),
applied to `X = B`, `trivS = S_triv`, `critr = sqrt q`.

*Cost of the atoms.* Unlike `zeta`, where `lambda^2` primes must be enumerated, `N_k = Tr B^k` is a
trace of a matrix power: `O(|E|^3 log k)` by repeated squaring, or `O(|V|^3)` once from
`spec(A)`. The atom side of the graph problem is free.

### 2.2 The displacement structure: which `D`?

**IH-9 (PROVED). The DFT of a Toeplitz matrix is a Loewner matrix on the circle.**
Let `That_{nm} = <e_n, T e_m>`. Put

    Bn := sum_{0 < |d| <= K-1} sign(d) t_d z_n^{-d} ,   b_n := -i Bn .

Then `Bn` is purely imaginary (so `b_n` is real), `b_{-n} = -b_n`, and

    That_{nm} = z_n (Bn - Bm) / ( K (z_n - z_m) )    for n != m,
    That_{nn} = a_n := sum_{|d| <= K-1} (1 - |d|/K) t_d z_n^{-d}   (a real Fejer mean, a_{-n} = a_n).

Conjugating by the diagonal unitary `S = diag(exp(i theta_n / 2))` makes it manifestly real
symmetric:

    (S^* That S)_{nm} = (b_n - b_m) / ( 2 K sin( (theta_n - theta_m)/2 ) ),  n != m;  diagonal a_n.

*Proof.* `That_{nm} = K^{-1} sum_{j,k=0}^{K-1} z_n^{-j} t_{j-k} z_m^k`. Substituting `d = j-k` and
summing the geometric series over the admissible `k` gives, with `w = z_m/z_n`,
`sum_{k in I_d} w^k = sign(d)(1 - w^{-d})/(1-w)` for `d != 0` (and `0` for `d = 0` when `n != m`);
since `z_n^{-d} w^{-d} = z_m^{-d}`, this is `K^{-1}(Bn - Bm)/(1 - z_m/z_n)`, which is the stated
formula. For `n = m`, `|I_d| = K - |d|`. `conj(Bn) = sum sign(d) t_{-d} z_n^{d} = -Bn` after `d ->
-d` and `t_{-d} = t_d`; `b_{-n} = -b_n` because `z_{-n} = conj(z_n)` and `t_d` is real. The
symmetrised form follows from `z_n^{1/2} z_m^{1/2} / (z_n - z_m) = 1/(2i sin((theta_n-theta_m)/2))`.
QED

*Verified* on Petersen at `K = 7` to `1e-14`, including `a_{-n} = a_n`, `b_{-n} = -b_n`.

This is the exact counterpart of CCM's `tau_{nm} = (b_n - b_m)/(n-m)`, `tau_{nn} = a_n` (Lemma
`basicexpli`, `CCM:817`; `CS` `\eqref{form}` at `CS:1153`), with the nodes moved from the integers
`n` on the **line** to the roots of unity `z_n` on the **circle**, and with the same Fejer weight
`1 - |d|/K` on the diagonal as CCM's `2(1 - y/L)` (`CCM:387`, `plan:57`).

**IH-10 (PROVED). The right `D` is the cyclic shift; the angle operator fails.**
Of the three candidates:

(a) **cyclic shift `Z`** (unitary, eigenvalues `z_n^{-1}`, eigenvectors the DFT modes).
    `Z T Z^* - T` has rank `<= 2`, is supported on row `0` and column `0` of the position basis, and
    in the DFT basis has entries `-(Bn - Bm)/K`. Explicitly

        T - Z T Z^* = |eta><g| + |g><eta| ,   eta = delta_0,  g_0 = 0,  g_k = t_k - t_{k-K} (k>0),
        Z T Z^* - T = -(i/K) ( |b><E| - |E><b| ) ,  b = sum_n b_n e_n,  E = sum_n e_n = K^{1/2} delta_0.

    The second display is *verbatim* CCM's `\eqref{QD}` (`CCM:839`, `CS:1166`):
    `D T - T D = |beta><eta| - |eta><beta|`, with `beta -> b`, `eta -> E`.
    Note `E = K^{1/2} delta_0` **exactly**: the discrete Dirichlet kernel *is* a Dirac delta, so
    CCM's whole subsection "The Dirichlet Kernel `delta_N` as an approximation of the Dirac Delta"
    (`CCM:937`) is vacuous over `Z`.

(b) **the self-adjoint angle operator** `A e_n = (2 pi n / K) e_n` (the literal transcription of
    `D V_n = n V_n`). `[A,T]_{nm} = (n-m) That_{nm} = (n-m) z_n (Bn-Bm)/(K(z_n-z_m))`, which is
    **not** of the form `c_n - c_m`: the factor `(n-m)/(z_n-z_m)` is not constant. **FAILS.**
    (Repaired in `IH-13` by a Cayley transform plus a non-unitary congruence.)

(c) **the nilpotent truncated shift** `S`. `S T S^* - T` also has rank `<= 2` (classical
    Gohberg-Semencul displacement), but `S` is not invertible and `spec(S) = {0}`, so the perturbed
    operator has no circle to put a spectrum on and the `T`-isometry argument of `IH-11` fails
    (`S^* T S != T` in general). **FAILS** as a substitute for `D`.

*Proof of (a).* In the position basis `(Z T Z^*)_{jk} = t_{(j-1 mod K)-(k-1 mod K)}`, which equals
`t_{j-k}` unless `j = 0` or `k = 0`; the displayed `g` reads off the exceptional row and column, and
Hermiticity fixes the rest. In the DFT basis `Z^* e_m = z_m e_m` gives
`(Z T Z^*)^_{nm} = (z_m/z_n) That_{nm} = -(z_n-z_m)/z_n * That_{nm}`, and substituting `IH-9` gives
`-(Bn - Bm)/K`. The vector identity follows from `(|b><E| - |E><b|)_{nm} = b_n - b_m` (`E` and `b`
real in the DFT basis). QED

*Verified*: rank exactly `2`, support on row/column `0`, DFT entries matching, on Petersen `K = 7`.

**Reading.** In CCM `D` is the generator of the scaling flow and `tau` is a convolution restricted to
the window, so `[D, tau]` is a pure boundary term, supported at the two ends of `[0,L]` which the
periodic boundary conditions glue into one point. Over `Z` the same thing happens: `Z` generates the
translations of the window `Z_K`, `T` is a convolution, and the displacement is supported at the
single point where the circle `Z_K` is cut. The rank-two structure is *the boundary of the window*,
in both cases.

### 2.3 The discrete key lemma

**IH-11 (PROVED, new; not in CS). The unitary key lemma.**
Let `T` be a Hermitian positive semidefinite Toeplitz matrix on `C^K` with `ker T = C xi`,
one dimensional. Then `xi_0 != 0`; normalise `<eta|xi> = xi_0 = 1`. Define

    U := Z^* ( 1 - |xi><eta| )  =  Z^* - |Z^* xi><eta|            (rank-one perturbation of Z^*)

(the exact transcription of CCM's `D' = D - |D xi><eta|`, `CCM:863`, `CS:1176`). Then

  (i)  `U xi = 0`, so `U` descends to `E/C xi`;
  (ii) `U^* T U = T` **exactly**, so `U` is an isometry for the `T`-inner product; consequently the
       induced operator `U''` on the Hilbert space `H = E / ker T = E / C xi` is **unitary**;
  (iii) `det(U'' - w) = det(Z^* - w) * K^{-1/2} * sum_n xihat_n / (z_n - w)`, where `xihat_n =
       <e_n, xi>`, `det(Z^* - w) = (-1)^K (w^K - 1)`; equivalently

           det(U'' - w) = (-1)^{K+1} * Ptilde(w),   Ptilde(w) := sum_{k=0}^{K-1} xi_k w^{K-1-k};

  (iv) `spec(U'')` = the zero set of `Ptilde`, `K-1` points, all on the unit circle `|w| = 1`.

*Proof.* `xi_0 != 0` is `IH-15` below (or `CS:871`, citing Hallouin-Perret Lemma 33).
(i) `U xi = Z^* xi - Z^* xi <eta|xi> = 0`.
(ii) Write `P = |xi><eta|`. Since `T xi = 0` we have `T P = 0` and `P^* T = 0`, hence
`(1-P^*) T (1-P) = T`. By `IH-10`(a), `Z T Z^* = T - |eta><g| - |g><eta|`, so

    U^* T U = (1-P^*) Z T Z^* (1-P) = T - (1-P^*)( |eta><g| + |g><eta| )(1-P).

Now `(1-P^*) eta = eta - |eta><xi|eta> = eta - <xi|eta> eta = 0` because `<xi|eta> = conj(xi_0) = 1`,
and `<eta|(1-P) = <eta| - <eta|xi><eta| = 0` for the same reason. Both correction terms vanish, so
`U^* T U = T`. Since `T >= 0` with radical `C xi` and `U (C xi) = 0 subset C xi`, `U` descends to
`H = E/C xi`, which carries the positive definite form `<.,.>_T`, and
`<U''[f], U''[g]>_T = <Uf, Ug>_T = <f,g>_T`. An isometry of a finite dimensional Hilbert space is
unitary.
(iii) `det(U - w) = det(Z^*-w) det(1 + (Z^*-w)^{-1} R)` with `R = -|Z^*xi><eta|` of rank one, so by
`det(1+A) = sum_k Tr(wedge^k A)` only `k <= 1` survives (CCM's computation at `CCM:925`):
`det(1 + (Z^*-w)^{-1}R) = 1 - <eta|(Z^*-w)^{-1} Z^* xi>`. In the DFT basis
`(Z^*-w)^{-1} Z^* xi = sum_n z_n xihat_n/(z_n-w) e_n` and `<eta| = K^{-1/2} sum_n <e_n|`, and
`<eta|xi> = K^{-1/2} sum_n xihat_n = 1`, so the bracket equals
`-w K^{-1/2} sum_n xihat_n/(z_n-w)`. Since `U` is triangular in a basis `(xi, lifts of the v_j)`
with a `0` on the diagonal, `det(U-w) = -w det(U''-w)`, giving the first display. For the second,
`xi_k = K^{-1/2} sum_n xihat_n z_n^k` gives
`sum_k xi_k w^{-k} = K^{-1/2}(1-w^{-K}) w sum_n xihat_n/(w-z_n)`, and substituting together with
`det(Z^*-w) = (-1)^K(w^K-1)` collapses everything to `(-1)^{K+1} w^{K-1} sum_k xi_k w^{-k}`.
(iv) The characteristic polynomial of a unitary has all roots on the circle. QED

*Verified*: for Petersen, `K = 4, 5, 6, 9`, `||U^* T U - T|| < 3e-12`, `U xi = 0`, and
`spec(U) \ {0}` equals `roots(Ptilde)` to `1e-12` in every case.

**Remark (what `IH-11` costs and what it does not need).** It needs neither the evenness of `xi`
(CCM's `gamma xi = xi`, `CCM:850` Definition `even-simple`) nor simplicity of the spectrum of `D`
(`CS:1356`). It needs only `T >= 0` Toeplitz with a one-dimensional kernel. The evenness enters
elsewhere: see `IH-17`.

**IH-12 (PROVED). Correspondence of the determinant identities.**

| CCM | graph |
|---|---|
| `det_reg(D_log - z) = 1 - exp(-izL)` (`CCM:1120`) | `det(1 - w Z) = 1 - w^K` |
| `xi^(z) = 2 L^{-1/2} sin(zL/2) sum_j xi_j/(z - 2 pi j/L)` (`CCM:1069`) | `Xi(w) := sum_k xi_k w^{-k} = K^{-1/2}(1-w^{-K}) w sum_n xihat_n/(w - z_n)` |
| `Det(D''-s) = Det(D-s) sum_j xi_j/(j-s)` (`CCM:869`, `\eqref{eq:detDp}`) | `det(U''-w) = det(Z^*-w) K^{-1/2} sum_n xihat_n/(z_n-w)` |
| `det_reg(D_log^{(lambda,N)} - z) = -i lambda^{-iz} xi^(z)` (`CCM:1085`) | `det(U''-w) = (-1)^{K+1} w^{K-1} Xi(w)` |

There is no *regularised* determinant on the graph side: the window space is finite dimensional and
`E_N^perp` (CCM's orthogonal complement carrying the spurious spectrum `{2 pi j/L : |j| > N}`,
`CCM:1133`) is empty.

**Index conventions.** CCM's `xi_j` are the components of `xi` in the eigenbasis of `D`; over `Z`
these are the DFT components `xihat_n`. The *position* components `xi_k` are what enter the
polynomial. `CS`'s `P(z) = sum_k xi_k z^k` (`CS:792`) is the reverse of `Ptilde`; the two root sets
are reciprocal, hence equal whenever all roots are on the circle and `xi` is real
(conjugation-closed root set). The divisor is recovered directly as `roots(Ptilde)`.

### 2.4 The Cayley route to `CS` Proposition `prop:finmain`

**IH-13 (PROVED). The Cayley transform brings the graph case *exactly* under `CS:1356`.**
Let `K = 2M+1` be **odd**, index `n in {-M,...,M}`, `theta_n = 2 pi n / K in (-pi, pi)`, and put

    lambda_n := tan(theta_n / 2)   (real, simple, lambda_{-n} = -lambda_n),
    C := diag( sqrt(2K) cos(theta_n / 2) )   (real, invertible since theta_n != pi),
    Q := C ( S^* That S ) C ,   S = diag(exp(i theta_n / 2)).

Then `Q` is real symmetric, `Q >= 0` iff `T >= 0`, `ker Q = C^{-1} ker That`, and

    Q_{nm} = (b_n - b_m)/(lambda_n - lambda_m)  for n != m,   Q_{nn} = a_n ,

with the *same* `b_n, a_n` as in `IH-9`, `b_{-n} = -b_n`, `a_{-n} = a_n`. That is literally `CS`'s
`\eqref{form2}` (`CS:1128`), with the parity hypotheses of Lemma `basics-general` (`CS:1324`)
satisfied. Hence `CS` Lemma `key-general` (`CS:1335`), `main-odd` (`CS:1344`) and Proposition
`prop:finmain` (`CS:1356`) apply verbatim and give: all roots of
`P(s) = sum_k xi_k prod_{j != k} (lambda_j - s)` are real, and they are the Cayley images
`tan(arg(w)/2)` of the returned divisor points.

*Proof.* `tan(a) - tan(b) = sin(a-b)/(cos a cos b)` gives
`lambda_n - lambda_m = sin((theta_n-theta_m)/2) / (cos(theta_n/2) cos(theta_m/2))`; substitute into
the symmetrised Loewner form of `IH-9` and clear the cosines with `C`. QED

*Verified* on Petersen at `K = 5` and `K = 7`: `Q` matches `\eqref{form2}` to `1e-13`, `Q >= 0`,
the roots of `P(s)` at `K = 5` are `-2.414214, -0.691080, 0.691080, 2.414214`, which are exactly
`tan(arg w / 2)` for the four true retained points.

**IH-14 (PROVED). The cost of the Cayley route, and which backbone MVP-2 should use.**
Costs: (a) `K` must be odd, otherwise `z = -1` is a node and `lambda = infinity`; (b) `C` is a
**non-unitary** congruence, so it preserves positivity, rank, kernel and the `gamma`-parity, but
**not** the spectrum: `min spec Q != min spec T`. Therefore the `eps`-shift must be performed in the
Toeplitz (position) picture *first* — `T_eps := T - eps I` is again Toeplitz, which is the whole
reason the CCM shift is legitimate — and only then transformed. (c) The Cayley picture destroys the
natural unitarity: it converts a unitary `U''` with spectrum on the circle into a self-adjoint `D''`
with real spectrum, at the price of an artificial diagonal congruence.

**Recommendation.** The MVP-2 backbone should be **`CS` Corollary `corcar` (`CS:792`) in the position
basis**, i.e. the Toeplitz/Caratheodory-Fejer route, for four reasons:

1. `corcar` has a complete published proof (`CS:898`), needs only "PSD Toeplitz of rank `K-1`", and
   no evenness, no simple `D`, no rank-two commutator.
2. The perturbed operator adds **nothing** to the zero set: `IH-11`(iv) shows
   `spec(U'') = roots(Ptilde)` exactly. In the graph case the truth is known, so the zero set is the
   entire deliverable.
3. The Caratheodory-Fejer decomposition gives more than the operator route: the *weights*, hence the
   multiplicities (`IH-20`), and the exact description of the over-resolved failure
   (`CS`'s remark at `CS:908`: with a non-simple kernel only the *intersection* of the zero sets of
   the kernel vectors is on the circle — which is precisely the over-resolved window, `IH-19`).
4. It is `O(K^2)` (Levinson / Prony) rather than `O(K^3)`.

The perturbed operator should nevertheless be implemented as a **certified cross-check**
(`spec(U'') == roots(Ptilde)`, `||U^* T U - T|| ~ 0`), because it, not `corcar`, is what has to be
carried to the graded case (section 7) and to the Selberg case (`plan:434`), where the object of
interest is an operator and not a polynomial. Between the two operator versions, use the **unitary**
one (`IH-11`): it is the honest analogue over `Z`, it needs no parity hypothesis and no odd `K`, and
it keeps the divisor on the circle where the functional equation lives. The Cayley/`CS` version
(`IH-13`) is worth computing once, as a certification that the graph case really is an instance of
`CS:1356` and not merely an analogue.

---

## 3. Grading, rank, and the three resolution regimes

### 3.1 The grading

**IH-15 (PROVED). Caratheodory-Toeplitz description of everything.**
Let `T` be a `K x K` Hermitian PSD Toeplitz matrix, `T_{jk} = t_{j-k}`. By the
Caratheodory-Fejer/Toeplitz structure theorem (`CS:772`, quoted with the Vandermonde factorisation
`T = V D V^*`; original `CF11`, `CS:2065`) there are `R = rank T` distinct points
`w_1,...,w_R` on the unit circle and weights `alpha_1,...,alpha_R > 0` with
`t_d = sum_j alpha_j w_j^d`. Setting `F_f(w) = sum_{k=0}^{K-1} f_k w^{-k}`,

    <f, T f> = integral |F_f|^2 d sigma ,   sigma = sum_j alpha_j delta_{w_j} ,
    ker T = { f : F_f vanishes on supp sigma },   dim ker T = max(0, K - R).

Consequences: `dim ker T = 1` iff `R = K-1`; in that case the kernel polynomial
`Ptilde(w) = w^{K-1} F_xi(w) = sum_k xi_k w^{K-1-k}` has degree exactly `K-1` with `Ptilde(0) != 0`,
so `xi_0 != 0` and `xi_{K-1} != 0`, and its `K-1` roots are exactly `supp sigma`.

*Proof.* `<f,Tf> = sum_{j,k} conj(f_j) t_{j-k} f_k = sum_j alpha_j |sum_k f_k w_j^{-k}|^2`. The
evaluation map `f -> (F_f(w_1),...,F_f(w_R))` has a Vandermonde matrix in the distinct nonzero nodes
`w_j`, hence rank `min(K,R)`. If `R = K-1`, `Ptilde` is a polynomial of degree `<= K-1` with `K-1`
distinct nonzero roots, so it has degree exactly `K-1` and nonzero constant term. QED

This is simultaneously: the classical theorem of `IH-22`, the proof that the CCM normalisation
`<eta|xi> = 1` is legitimate (CCM prove this at `CCM:852` using evenness; here it is free), and
the complete analysis of the over-resolved case.

**IH-16 (PROVED). The grading `gamma`.** `T` is real symmetric Toeplitz, hence *persymmetric*:
`J T J = T` with `(Jf)_k = f_{K-1-k}`. By Cantoni-Butler (1976, *Eigenvalues and eigenvectors of
symmetric centrosymmetric matrices*, Linear Algebra Appl. 13, 275-288) the eigenvectors of a
symmetric centrosymmetric matrix may be chosen symmetric (`J v = v`) or skew (`J v = -v`), and `T`
block-diagonalises into blocks of sizes `ceil(K/2)` and `floor(K/2)`. This is CCM's `gamma`
(`CCM:837`, Lemma `basics`(i)) and the even/odd block split of `plan:111`: the even block replaces
the full `K x K` eigenproblem, a factor-four saving, exactly as in `plan:111`. In the DFT basis
`J` acts as `e_n -> e_{-n}` up to a phase, which is CCM's `gamma(V_j) = V_{-j}` verbatim.

**IH-17 (PROVED). What evenness means on the graph side.**
`J xi = xi` iff `Ptilde` is self-reciprocal (palindromic), `J xi = -xi` iff anti-palindromic. A
self-reciprocal polynomial has a root set invariant under `w -> 1/w`. Hence:

  **evenness of `xi` = the functional equation of the returned divisor.**

`CS:865` proves that when `dim ker T = 1` the kernel vector is automatically palindromic *or*
anti-palindromic, so the `gamma`-parity is never in doubt; what CCM's Definition `even-simple`
(`CCM:850`) adds is that the sign is `+`, and that the eigenvalue is simple. Over `Z`, `IH-11` shows
the `+` sign is **not needed** for the reality/circle conclusion. It is needed for the returned
divisor to obey `w -> 1/w`, which for a graph is true anyway (`IH-1`), and it is needed for
`CS:1356` via `CS:1335`. Net: **half of "even-simple" evaporates over `Z`; the surviving half is
simplicity, and it can fail (`IH-19`).**

### 3.2 The three regimes

Let `R` = the number of **distinct** points of the retained divisor `A_ret/sqrt q` on the circle
(Ramanujan case). By `IH-8` and `IH-15` the sequence `t_k` is the moment sequence of
`sigma = sum_{distinct w} m(w) delta_w`, `m(w)` the multiplicity.

**IH-18 (PROVED). The three regimes.** With `K = 2M+1`:

| regime | condition | `rank T` | `eps_M = min spec T` | `dim ker(T - eps_M)` | what `roots(Ptilde)` is |
|---|---|---|---|---|---|
| under-resolved | `K <= R` | `K` | `> 0` | `1` if simple | `K-1` points on the circle, **not** the divisor; a Pisarenko/`K-1`-atom approximation |
| critical | `K = R+1` | `R = K-1` | `= 0` | `1` | **exactly** the `R` divisor points |
| over-resolved | `K > R+1` | `R` | `= 0` | `K - R >= 2` | not determined; only the intersection over `ker T` is the divisor (`CS:908`) |

*Proof.* Rank and kernel dimension are `IH-15`. In the under-resolved regime `T` is nonsingular so
`eps_M > 0`; `T - eps_M I` is again Toeplitz and PSD with a kernel, so `IH-15` applies to it and its
own Caratheodory measure `sigma_eps` has exactly `K-1` atoms, which are the roots of `Ptilde`. In
the critical and over-resolved regimes `eps_M = 0` and `T` itself is the object. QED

*Verified* on Petersen (`R = 4`): `eps_M` for `K = 2,3,4,5,6,7,8` equals
`15.8787, 9.4477, 5.7124, 0, 0, 0, 0` and `dim ker(T - eps)` equals `1,1,1,1,2,3,4`. At `K = 5` the
roots of `Ptilde` are `exp(+-3 pi i /4)` and `(1 +- i sqrt 7)/(2 sqrt 2)` to `1e-15`, i.e. exactly
the four retained points. At `K = 4` they are `-1` and `0.026801 +- 0.999641 i`: on the circle, but
not the divisor.

**IH-19 (PROVED). Even-simplicity fails in the over-resolved regime, and the conclusion fails with
it.** For `K > R+1`, `dim ker T = K-R >= 2`, so the smallest eigenvalue of `T` is not simple and
CCM's hypothesis `even-simple` (`CCM:850`) is violated. Moreover the conclusion is false for a
general kernel vector: `ker T = { q_0 * s : deg s <= K-1-R }` where `q_0` is the minimal-degree
kernel polynomial (monic of degree `R`, roots exactly the divisor), so a kernel vector's polynomial
has the `R` true roots plus `K-1-R` **arbitrary** roots anywhere in `C`. The correct statement is
`CS`'s: the *intersection* of the zero sets over `ker T` is on the circle (`CS:908`).

*Verified*: Petersen at `K = 6`, the eigenvector returned by a standard symmetric eigensolver gives
roots `{four true points} union {-0.314767}` — the last one strictly inside the disc — and is
neither palindromic nor anti-palindromic. At `K = 9` the extra roots are `-2.8759`, `0.9660`,
`0.7968 +- 2.1352 i`: three of the five outside the disc.

**IH-20 (PROVED). Multiplicities are recovered, but only at the critical window and only by a second
step.** The construction returns the *support* of the divisor, never its multiplicities: `Ptilde`
depends on `sigma` only through `supp sigma`. At `K = R+1` the multiplicities are recovered by the
Prony step: the weights solve the `(R+1) x R` Vandermonde system `t_d = sum_j alpha_j w_j^d`,
`d = 0..R`, which has full column rank since the `w_j` are distinct, so `alpha_j = m(w_j)` is the
unique solution and is the true multiplicity. Equivalently, the Caratheodory-Fejer decomposition of
a PSD Toeplitz matrix of rank `R` and size `R+1` is unique.

*Petersen, concretely.* `A_ret` has `18` points (`2|V|-2`) but only `R = 4` distinct ones:
`(1 +- i sqrt 7)/(2 sqrt 2)` with multiplicity `5` (from `lambda = 1`) and
`(-1 +- i)/sqrt 2` with multiplicity `4` (from `lambda = -2`). The `5 x 5` construction returns the
four points; the Prony step returns `(5,5,4,4)`.

*Comparison with CCM.* The zeros of `zeta` are believed simple, so for CCM support and divisor
coincide and the distinction is invisible. It is not invisible for a graph, and it is a structural
limitation of the method, of a piece with `prop:weil-blind-jordan`
(`08c_weil_positivity_continuous.tex`, status `proved`): Weil positivity sees the divisor as a set of
moduli, not as a module.

**IH-21 (CLAIMED). Canonical choices in the over-resolved regime.**
Write `d = K-1-R >= 1`.

  (a) **A family that keeps the circle exists:** take `Ptilde = q_0(w) * (w^d - beta)` with
      `|beta| = 1`. These are exactly the *paraorthogonal* completions (Jones-Njastad-Thron 1989;
      Simon, *OPUC*, Section 2.2), a one-parameter family, none canonical. All roots lie on the
      circle, so the conclusion of `IH-11` holds for each member even though its hypothesis does not.
  (b) **The minimal-degree choice** `Ptilde = q_0(w) * w^d` puts the `d` extra roots at `w = 0`:
      `U''` then has eigenvalue `0` with multiplicity `d`, is a `T`-isometry but not unitary. It is
      canonical and computable (it is the vector in `ker T` with `xi_k = 0` for `k > R`) but it
      breaks the circle conclusion.
  (c) **The minimum-norm choice** (minimise `||xi||` subject to `xi_0 = 1`) is the classical
      minimum-phase / Levinson prediction filter; its extra roots lie strictly inside the disc.
      Breaks the circle conclusion.
  (d) **The right fix is not a choice of `xi` but a choice of window:** run at `K = R+1`. `R` is
      observable without knowing the answer, as the rank of `T` stabilises (`rank T = R` for all
      `K > R`), so the algorithm can find the critical window by increasing `K` until the rank stops
      growing, then step back one.

  *What is missing:* whether any canonical choice in (a) is selected by a natural perturbation of the
  construction (e.g. adding `delta * (rank-one at the window boundary)` and letting `delta -> 0`).
  Not settled; see section 10.

---

## 4. Classical identifications, and the "does not generalise" list

**IH-22 (PROVED, classical). The minimal-eigenvector theorem.**
*Statement.* Let `T` be a `K x K` Hermitian Toeplitz matrix whose smallest eigenvalue `eps` is
simple, with eigenvector `xi`. Then all `K-1` zeros of `Ptilde(w) = sum_k xi_k w^{K-1-k}` lie on
`|w| = 1`.

*Proof.* `T - eps I` is Hermitian PSD (by minimality) and Toeplitz (a diagonal shift preserves
Toeplitz structure) with one-dimensional kernel `C xi` (by simplicity). Apply `IH-15`: its
Caratheodory measure `sigma_eps` has `K-1` atoms on the circle, `Ptilde` has degree exactly `K-1`,
and its roots are exactly those atoms. QED

*Attribution.* This is `CS` Corollary `corcar` (`CS:792`), proved there `C^*`-algebraically at
`CS:898`, and it is exactly the classical result of J. Makhoul, *On the eigenvectors of symmetric
Toeplitz matrices*, IEEE Trans. ASSP 29 (1981) 868-872 ("the eigenfilters corresponding to the
maximum and minimum eigenvalues, if distinct, have their zeros on the unit circle"); see also
Delsarte-Genin-Kamp and the survey literature on the split Levinson algorithm. The maximum-eigenvalue
half of Makhoul's statement is the one relevant to the graph, by the sign flip `IH-6`. The
number-theoretic use of the same corollary is Hallouin-Perret, *A unified viewpoint for upper bounds
for the number of points of curves over finite fields via Euclidean geometry and semi-definite
symmetric Toeplitz matrices*, Trans. AMS 372 (2019) 5409-5451 (`CS:2103`), which `CS:800` cites as
"a striking number-theoretic flavor"; `CS:871` uses its Lemma 33 for `xi_0 != 0`.

**IH-23 (PROVED). CCM's Theorem `finmain` restricted to a finite divisor is `IH-22`.**
`CCM` Theorem `finmain` (`CCM:1085`) says: `eps_N` simple with even eigenvector implies
`D_log^{(lambda,N)}` self-adjoint, `det_reg = -i lambda^{-iz} xi^(z)`, and all zeros of `xi^` real and
equal to the spectrum. Over `Z` with a finite divisor, `IH-11` + `IH-15` gives exactly this
statement, and `IH-15` shows it is `IH-22`, i.e. Caratheodory-Fejer 1911 plus one line. The content
CCM adds over the classical theorem is *not* in the finite-dimensional linear algebra.

**IH-24 (PROVED). Pisarenko.** Pisarenko harmonic decomposition (V. F. Pisarenko, *The retrieval of
harmonics from a covariance function*, Geophys. J. R. Astron. Soc. 33 (1973) 347-366) is: given a
covariance sequence `c_k = sum_j alpha_j exp(i k theta_j) + sigma^2 delta_{k,0}` (`R` harmonics plus
white noise), the minimal eigenvector of the `(R+1)x(R+1)` covariance Toeplitz matrix has its
polynomial roots at the `R` frequencies, and the minimal eigenvalue is the noise floor `sigma^2`.
This is exactly the construction of `IH-18` with the identification

    eps_M  <-->  the noise floor sigma^2 ,
    the divisor  <-->  the harmonic frequencies ,
    the critical window K = R+1  <-->  Pisarenko's exact-order case .

So: **CCM's `eps_N` is a noise floor, and the CCM chain on a finite divisor is Pisarenko.** The
`(lambda, N)`-dependence of the accuracy studied in `plan:456` is, in the graph case, the classical
under-resolved (order-underestimated) Pisarenko problem.

**IH-25 (PROVED). OPUC / paraorthogonal / CMV.** `U''` of `IH-11` is a rank-one perturbation of the
shift which is unitary for the `T`-inner product, and its characteristic polynomial `Ptilde` is
self-reciprocal when `xi` is even (`IH-17`). That is the definition of a *paraorthogonal polynomial*
for the measure `sigma_eps`; the corresponding unitary matrices are the truncated GGT / CMV matrices
(Cantero-Moral-Velazquez 2003; Simon, *OPUC*, Chapters 2 and 4). The statement "a rank-one
perturbation of a unitary shift has spectrum on the circle, at the roots of a paraorthogonal
polynomial" is the standard OPUC picture and `IH-11` is its `T`-inner-product form. Note that
`IH-21`(a)'s free unimodular parameter `beta` is precisely the paraorthogonal parameter.

### 4.1 What in CCM is NOT covered by the classical theory (main deliverable)

Numbered `NG-n` (**n**ot **g**eneralising). Each entry says what CCM has, what the graph has, and why
the difference matters.

**NG-1. The continuous group, hence the second truncation `N`.**
CCM's window space `L^2([0,L])` is infinite dimensional, so a *second* truncation to `2N+1` Fourier
modes is needed (`CCM:812`), the full operator lives on `E'_N (+) E_N^perp` (`CCM:1086`), and the
spectrum of `D_log^{(lambda,N)}` contains the spurious set `{2 pi j/L : |j| > N}` on top of the zeros
of `xi^` (`CCM:1133`). Over `Z` the window space `l^2(W)` is *already* finite: there is no `N`, no
`E_N^perp`, no spurious spectrum, and the `(lambda, N)` two-parameter accuracy map of `plan:456`
collapses to a one-parameter family in `M`. Half of the `zst` library's parameter management
(`plan:306`) has nothing to manage.

**NG-2. The Dirichlet kernel as an approximate delta.**
CCM must approximate the boundary evaluation `f -> f(lambda)` by the Dirichlet kernel `delta_N`
(`CCM:937-960`), and carry the discrepancy `delta_N = L^{-1/2} eta` through the normalisation
(`CCM:1104`). Over `Z`, `E = sum_n e_n = K^{1/2} delta_0` **exactly**: the "approximate delta" is a
delta. This subsection of CCM is vacuous on `Z`.

**NG-3. The infinite divisor, hence the permanent under-resolution.**
`zeta` has infinitely many zeros: `R = infinity`, every window is under-resolved, `eps_N > 0` always,
and the entire content of the method is the *rate* at which `eps_N -> 0` (`plan:172`, the empirical
law `eps_N ~ 10(1 - chi_4(lambda))`). A graph has `R < infinity`, so there is a critical window at
which the answer is *exact* and beyond which the hypothesis *fails*. The graph therefore cannot
exhibit, even qualitatively, the phenomenon that CCM's missing proof must control. This is the single
most important entry in this list.

**NG-4. The archimedean term.**
CCM's `W_R` is a transcendental kernel requiring digamma, trigamma and Hurwitz-Lerch evaluations
(`plan:82-104`), and the generic archimedean regularisation is explicitly the one place in the `zst`
plan where "a derivation, not a transcription, is required" (`plan:473`). The graph's `W_R` is two
geometric terms with rational data. **MVP-2 therefore does not exercise the hardest existing code
path in `zst/`**; it exercises `loewner.c`, `eigmin.c` and `secular.c` only.

**NG-5. Conditional convergence and analytic continuation.**
CCM must restrict to test functions of the form `f^* * g` to make the sum over zeros absolutely
convergent (`CCM:428`), and the explicit formula itself is Weil's theorem. The graph identity `IH-3`
is a finite rearrangement of `Tr B^k`, provable by inspection; there is no analysis in it at all.

**NG-6. The cost and the arithmetic of the atoms.**
`zeta` needs every prime power up to `lambda^2 = e^L`; the graph needs `Tr B^k` for `k <= 2M`,
a matrix power. The number-theoretic input disappears.

**NG-7. The Hermite/prolate convergence strategy — the only missing step, and it has no graph
counterpart.** CCM's route to a proof (`CCM:1216-1400`) rests on: `Xi` being the Fourier transform of
`E(h)` with `h` the unique combination of the Hermite functions `h_0, h_4` with vanishing integral
(Lemma `hermfact`, `CCM:1246`); Poisson summation `k(u) = k(1/u)`; the prolate deformation
`PW_lambda` of the harmonic oscillator (`CCM:1262`); the Meixner-Schafke estimate (`CCM:1271`); and
Fuchs' asymptotics for `1 - chi_4(lambda)` (`CCM:1325`). **None of this has a counterpart over `Z`.**
There is no theta function on `Z`, no Gaussian fixed by the Fourier transform of `(Z, T)` adapted to
a window, no self-dual prolate deformation, and the "`Xi` function" of a graph is the polynomial
`P(u) = prod_{nontrivial}(1 - lambda u + q u^2)` of degree `2(|V|-1)` whose roots are already known
in closed form. The step whose absence blocks CCM's proof of RH is exactly the step the graph MVP
**cannot test at all**. Any claim that MVP-2 "tests the CCM programme" must be qualified by this.

**NG-8. Weil's criterion as a limit.**
CCM's Corollary `strange` (`CCM:668`): `mu_lambda` is decreasing in `lambda` and `mu_lambda -> 0`
implies RH. The discrete analogue holds (`eps_M` is non-increasing in `M` by restriction/Cauchy
interlacing, verified: Petersen `15.88, 9.45, 5.71, 0, ...`; prism `43.0, 38.2, 23.4, 6.0, -32.8,
...`), but it is not a limit statement: `eps_M >= 0` for all `M` **iff** Ramanujan
(`thm:weil-positivity-finite`), and in the Ramanujan case `eps_M = 0` *exactly* for `M >= (R-1)/2`.
Weil's criterion becomes a finite computation, which is a loss of content, not a gain.

**NG-9. Spectral-triple content.**
`D_log` is an unbounded self-adjoint operator with a regularised determinant, a zeta function and a
dimension spectrum; the "infrared" character of the construction is that the window is a neighbourhood
of `1` in `R_+^*` (`CCM:806`). Over `Z` the analogue `U''` is a finite unitary on a `(K-1)`-dimensional
space: the triple is finite, the regularised determinant is an ordinary determinant, and `Z` has no
small-scale structure for an "infrared" limit to see. The graph case is a *finite spectral triple*,
which is linear algebra.

**NG-10. The evenness hypothesis.**
See `IH-17`. In CCM, `gamma xi = xi` is needed both for `<eta|xi> != 0` (`CCM:852`) and for Lemma
`key` (`CCM:863`). Over `Z`, `<eta|xi> != 0` is automatic (`IH-15`) and `IH-11` needs no parity at
all. So a hypothesis that CCM lists among its two missing steps (`CCM:1385`, "the missing steps")
is, in the discrete case, half free and half a genuinely different question (simplicity, `IH-19`).

**NG-11. Multiplicity.**
`IH-20`: the method recovers the support of the divisor and not its multiplicities. The `zeta` zeros
are believed simple so CCM never meets this; a graph always does.

**NG-12. Where RH enters.**
For CCM the reality of the spectrum is unconditional and RH is the *convergence*. The same is true
over `Z`, and there one can *watch it fail*: section 5. CCM cannot. This is the one thing MVP-2
genuinely adds.

---

## 5. Non-Ramanujan graphs: where RH enters the chain

Setting: `X` non-Ramanujan, so `A_ret` contains a real pair `{rho, 1/rho}` with `rho = mu/sqrt q > 1`
(coming from an adjacency eigenvalue `|lambda| > 2 sqrt q`), of multiplicity `m`, and possibly
several such pairs; let `rho` be the largest. By `thm:weil-positivity-finite` the window form is
indefinite once `M` is large.

**IH-26 (PROVED). The construction never breaks.** For every `M`, `T - eps_M I >= 0` is Toeplitz
(with `eps_M < 0` once the form is indefinite, so the shift *adds* to the diagonal), so `IH-15`
applies and `IH-11`/`IH-22` return `K-1` points on the unit circle. Reality of the spectrum is
unconditional. **RH is nowhere in the reality half of the CCM chain**; it enters only through
whether the returned points converge to the divisor.

*Verified*: prism `C_16 x K_2`, `M = 1..21`, `max | |root| - 1 | < 4e-15` throughout, including
deep in the indefinite regime.

**IH-27 (PROVED). The sign of `eps_M` and its rate.**
Write `T = T_circ + m(|u><v| + |v><u|) + ...`, `u_j = rho^j`, `v_j = rho^{-j}`, the second term being
the contribution of the pair `{rho, 1/rho}`. Then `<u,v> = K`, `||u||^2 = (rho^{2K}-1)/(rho^2-1)`,
`||v||^2 = (1-rho^{-2K})/(1-rho^{-2})`, and the rank-two term has smallest eigenvalue
`m(K - ||u|| ||v||)`, while `||T_circ|| = O(K)`. Hence

    eps_M  =  - m rho^{K+1}/(rho^2 - 1) * (1 + o(1))  =  - C rho^{2M} (1+o(1)) ,   K = 2M+1,
    d log(-eps_M) / dM  ->  2 log rho .

In particular `eps_M > 0` for small `M`, crosses zero once, and then diverges to `-infinity` at the
exponential rate set by the *largest off-circle radius* — so **the failure of RH is readable off the
growth rate of the noise floor, and that rate recovers the offending eigenvalue**.

*Verified*: prism (`|V| = 32`, bipartite, so `{-q,-1}` is also trivial), `rho = 1.123952` from
`lambda = 2 cos(pi/8) + 1 = 2.847759 > 2 sqrt 2`, multiplicity `m = 2`. `eps_M` is
`39.000, 37.057, 30.084, 24.099, 14.133, 1.212` for `M = 1..6`, crosses zero between `M = 6` and
`M = 7` (`eps_7 = -13.384`), and at `M = 21` equals `-1351.24` against the closed-form prediction
`-m rho^{K+1}/(rho^2-1) = -2 * 1.123952^44 / 0.263268 = -1299`. Successive ratios `eps_{M+1}/eps_M`
are `1.2826` at `M = 20..21` against `rho^2 = 1.263268`, converging from above (the `O(K)` positive
part is the finite-`M` correction). Failing to remove the bipartite trivial pair `{-q,-1}` puts
`rho = sqrt q` in `A_ret` and the same law then reports `2 log sqrt q` instead: the trivial-divisor
bookkeeping of `def:graded-transfer-channel` is load-bearing here.

**IH-28 (CLAIMED). What the returned points do: equidistribution.**
In the same regime the minimal eigenvector is asymptotically the most-negative direction of the
rank-two term, `xi ~ u/||u|| - v/||v||`, i.e. two geometric profiles of ratio `1/rho` anchored at the
two ends of the window. Then

    Ptilde(w) ~ 1/(1 - w/rho)  -  w^{K-1}   on |w| = 1,

so `|w|^{K-1} = O(1)` forces `|w| -> 1` and the roots are the `(K-1)`-st roots of a slowly varying
unimodular-ish function: **the returned spectrum becomes asymptotically equidistributed on the
circle, with an `O(1/K)` phase modulation, and retains no information about the divisor** except
through `eps_M`. The circle points contribute `O(K)` against `rho^{2M}` and are asymptotically
invisible.

*Gap:* the argument is a leading-order estimate; the error term and the exact weak-* limit are not
proved here. *Verified partially*: prism at `M = 21` (`K-1 = 42` roots), the `41` consecutive gaps
between sorted root angles have mean `0.148627` against `2 pi/(K-1) = 0.149600`, with standard
deviation `0.012038` (8% of the mean) — approaching equidistribution with a visible modulation, as
predicted, but not yet converged at `M = 21`.

**IH-29 (CLAIMED). Where RH enters the CCM chain.** Three places, of which only the third is real:

1. *Not* in the reality of the spectrum (`IH-26`).
2. *Not* in the existence of `eps_M` and of `xi` (`IH-15`, unconditional).
3. **In the identification of the limit.** The returned measure is `sigma_{eps_M}`, the
   Caratheodory measure of `T - eps_M I`. It converges to the true divisor measure `sigma` if and
   only if `eps_M -> 0`, which by `thm:weil-positivity-finite` + `thm:weil-duality-pairing` is
   equivalent to RH for the object. In CCM, "`mu_lambda -> 0`" (`CCM:668`, Cor. `strange`) is exactly
   this, and the prolate strategy `NG-7` is an attempt to prove it. So: **the CCM chain proves
   reality unconditionally and reduces RH to the vanishing of the noise floor, which is Weil's
   criterion restored verbatim.** It is not a new route to RH; it is a spectral realisation of the
   old one. The graph case makes this visible because there one can exhibit an object where the noise
   floor does not vanish and watch the construction produce a meaningless circle spectrum.

---

## 6. Irregular graphs

For an irregular finite graph, Ihara-Bass reads `det(1-uB) = (1-u^2)^{|E|-|V|} det(1 - Au + (D-I)u^2)`
with `D` the degree matrix. `R_G` is the radius of convergence of `Z_G(u)`, `1/R_G = specrad(B)`.
Stark-Terras graph RH: `Z_G(u)` has no poles in the annulus `R_G < |u| < sqrt(R_G)`; equivalently,
with `u = R_G^s`, `Z_G` has no poles in the open strip `1/2 < Re(s) < 1` (Terras, *Zeta functions of
graphs: a stroll through the garden*, Chapter 8, "Irregular graphs: what is the Riemann hypothesis?";
for `(q+1)`-regular this is "no poles in `1/q < |u| < 1` except on `|u| = 1/sqrt q`").

**IH-30 (PROVED). What survives verbatim.** Everything in sections 2-4 that uses only "`T` Hermitian
Toeplitz": `IH-7` (Toeplitz structure), `IH-9` (Loewner/displacement), `IH-10`(a) (rank-two
displacement), `IH-11` (unitary key lemma), `IH-15`, `IH-16`, `IH-18`, `IH-22`. The construction runs
and returns a circle spectrum. Reason: none of these uses `q`, the functional equation, or the shape
of the trivial divisor.

**IH-31 (PROVED). What is modified.**
  (a) The critical radius `sqrt q` is replaced by `R_G^{-1/2} = specrad(B)^{1/2}` and `t_k :=
      sum_{A_ret} (mu R_G^{1/2})^k`.
  (b) `t_{-k} = conj(t_k) = t_k` still holds (`B` real), so the Hermitian extension survives.
  (c) The `W_R` term survives unchanged in shape: `(|E|-|V|)((R_G^{1/2})^{|k|} + (-R_G^{1/2})^{|k|})`;
      the `+-1` eigenvalues of `B` with multiplicity `|E|-|V|` are a purely topological fact,
      independent of regularity.
  (d) `W_{0,2}` degenerates. The Perron pole `mu = 1/R_G` survives, but its designated partner `1`
      does not: `1` is generally **not** an eigenvalue of `B` for an irregular graph. So `W_{0,2}`
      becomes a rank-one term `(R_G^{-1/2})^{|k|}`, and the designation of the trivial divisor
      (`def:graded-transfer-channel`'s `trivS`, `02h:32`) loses its "`H^0` partner of `q`".

**IH-32 (PROVED). What fails.**
  (a) `IH-1`(i) fails: `A_ret` is **not** invariant under `mu -> R_G^{-1}/mu`. There is no functional
      equation, the Hermitian and inverse extensions genuinely differ, and only the Hermitian one is
      available (`IH-2`).
  (b) Consequently `thm:weil-duality-pairing` (`08b:87`) does not apply, and
      `thm:weil-positivity-finite` (`08b:60`) gives only the **one-sided** bound: `QW_M >= 0` for all
      `M` iff `|mu| <= R_G^{-1/2}` for every retained `mu`. That one-sided bound is *exactly* the
      Stark-Terras RH in its correct (one-sided) form. The two-sided "poles on the circle
      `|u| = R_G^{1/2}`" is a theorem only in the regular case.
  (c) Therefore the *interpretation* of the output fails even when the output exists: `sigma_{eps_M}`
      lives on the circle, but the true divisor does not, so even at `eps_M = 0` the returned points
      are not the divisor. The right statement for an irregular graph is the Hallouin-Perret one:
      the construction yields **bounds**, not a divisor.
  (d) The even/odd grading `IH-16` survives (persymmetry is automatic), but `IH-17`'s reading of
      evenness as the functional equation is empty.

**Practical consequence.** The `zst_weil_discrete` data model of `plan:426` should carry `critr` as a
free parameter, not `q`, and should mark whether the functional equation is asserted. An irregular
graph is the cheapest available example inside the notebook of an object with Weil positivity but no
duality — the exact situation of `prop:kraus-no-duality-example` (`08b:174`, status `proved`).

---

## 7. The graded case: zeros, and CCM's sign restored

**IH-33 (PROVED). The curve / graded form.**
For a smooth projective curve `C/F_q` of genus `g`, `N_n = 1 + q^n - sum_{i=1}^{2g} alpha_i^n`
(`07_deligne_via_graphs.tex:55`). Put `t_k := - sum_i (alpha_i / sqrt q)^k` (the fermionic sign,
`def:graded-transfer-channel`: `nu < 0` are zeros, `02h:28`). Then for `k >= 1`

    t_k = q^{-k/2} N_k - (q^{k/2} + q^{-k/2}) ,

i.e.

    Psi_C(F) = sum_i F^(alpha_i/sqrt q) = W_{0,2}(F) - W_pts(F),
    W_{0,2}(F) = sum_k (q^{|k|/2}+q^{-|k|/2}) F(k),   W_pts(F) = sum_k q^{-|k|/2} N_{|k|} F(k).

This is **CCM's sign exactly** (`CCM:465`): poles minus atoms equals the sum over the nontrivial
divisor. There is no `W_R`: a curve's zeta has no gamma factor beyond `(1-u)(1-qu)`, which is the
`W_{0,2}` term.

**IH-34 (PROVED). Nothing in the linear algebra changes.** `IH-7` through `IH-22` use only that `T`
is Hermitian Toeplitz and PSD after the `eps`-shift. Weil's theorem for curves gives `|alpha_i| =
sqrt q` and `{alpha_i}` invariant under `alpha -> q/alpha` and under conjugation, so `t_k` is real,
`t_{-k} = t_k`, the form is PSD, and the critical window `K = R+1` returns the zeros exactly.
Everything downstream is the same code. **The only thing that changes is the sign bookkeeping of
`def:graded-transfer-channel`** (`02h:20-47`): which multiplicities count with which sign in
`nu_ret = m_0 - m_1`, and hence whether the form is `sum (-nu_ret)|f^|^2` (zeros) or
`sum (+nu_ret)|f^|^2` (poles). One global sign, chosen once per object, exactly as in `IH-6`.

**IH-35 (PROVED, prior art). This case is already in the literature.** Hallouin-Perret (TAMS 372
(2019) 5409-5451, `CS:2103`) derive upper bounds for `#C(F_q)` from precisely the semidefinite
symmetric Toeplitz matrix of the rescaled point-count sequence, and `CS:800` points at it as the
number-theoretic home of `corcar`. So **the graded (curve) instance of MVP-2 is not new
mathematics**; it is a re-derivation. Its value in this notebook is as a certified anchor and as the
bridge to `def:graded-transfer-channel`, not as a result.

**IH-36 (CLAIMED). Mixed divisors break the chain.** For a general graded transfer channel
(`def:graded-transfer-channel`) the retained divisor may contain both poles (`nu > 0`) and zeros
(`nu < 0`). Then no global sign makes the form semidefinite: `QW_M(f,f) = sum_lambda
nu_ret(lambda)|f^|^2` is indefinite *by construction*, independently of RH, so `eps_M` is not a noise
floor and the returned circle spectrum has no interpretation at all. **The CCM chain requires the
retained divisor to be of a single parity.** `zeta` (all zeros, `NG` none), an ungraded graph (all
poles), a curve (all zeros) each satisfy this; `prop:qubit-graded-zeta`'s graded quantum Ihara zeta
(`03c:221`, status `sketched`) has a numerator and a denominator both nontrivial and therefore does
not, unless one of the two sectors is put into `trivS`. *Gap:* whether a two-sided (Krein-space)
version of `IH-11` says anything useful for a mixed divisor. Not settled.

---

## 8. Table: CCM step -> discrete analogue

`V` = verbatim, `M` = modified, `F` = fails / vacuous.

| # | CCM step (line) | discrete analogue over `Z` | V/M/F | why |
|---|---|---|---|---|
| 1 | group `R_+^*`, `x = log u` (`CCM:431`) | `Z`, length `k`; dual `T` | M | discrete group, compact dual |
| 2 | window `[lambda^{-1},lambda]`, `L = 2 log lambda` (`CCM:496`) | `W = {-M..M}`, `K = 2M+1` | V | but translation invariance makes the window's position irrelevant; CCM's is pinned by `iota` |
| 3 | `Psi = W_{0,2} - W_R - sum_p W_p` (`CCM:465`) | `Psi_G = W_C - W_{0,2} - W_R` | M | global sign flip: poles, not zeros (`IH-6`, `prop:no-ungraded-zeros`) |
| 4 | inversion symmetry, Lemma `wsharp` (`CCM:479`) | `t_{-k} = conj(t_k) = t_k` | V | `IH-1`, `IH-2` |
| 5 | `W_p`: `Lambda(n) n^{-1/2}` at `y = log n` (`CCM:445`) | `|C| q^{-m|C|/2}` at `k = m|C|` | V | `log p <-> |C| log q`; and the atoms are a matrix trace, not a prime enumeration (`NG-6`) |
| 6 | `W_{0,2}`, rank two (`CCM:684`) | `q^{|k|/2}+q^{-|k|/2}` (twice if bipartite), rank two | V | `IH-4` |
| 7 | `W_R`, kernel `rho = sum e^{-(2n+1/2)x}` (`CCM:450`) | `(|E|-|V|)((q^{-1/2})^{|k|}+(-q^{-1/2})^{|k|})` | M | ladder truncated to one rung; rational; = the `(1-u^2)^{r-1}` gamma factor (`IH-5`) |
| 8 | second truncation `N`, `E_N`, `E_N^perp` (`CCM:812`, `1103`) | none | F | window space already finite (`NG-1`) |
| 9 | Dirichlet kernel `delta_N ~ delta` (`CCM:937`) | `E = K^{1/2} delta_0` exactly | F | vacuous (`NG-2`) |
| 10 | `tau_{nm} = (b_n-b_m)/(n-m)`, `a_n` Fejer (`CCM:817`) | `That_{nm} = z_n(B_n-B_m)/(K(z_n-z_m))`, `a_n` Fejer mean | M | nodes on the circle, not the line (`IH-9`); recovered verbatim by Cayley + congruence (`IH-13`) |
| 11 | `[D,tau] = |beta><eta| - |eta><beta|` (`CCM:839`) | `Z T Z^* - T = -(i/K)(|b><E| - |E><b|)`, rank 2 | M | multiplicative displacement; the **additive angle operator fails** (`IH-10`(b)) |
| 12 | `gamma: V_j -> V_{-j}` (`CCM:837`) | flip `J`, persymmetry, Cantoni-Butler | V | `IH-16` |
| 13 | `even-simple` (`CCM:850`) | simplicity only; evenness free | M | `IH-17`, `NG-10`; and simplicity **fails** when `K > R+1` (`IH-19`) |
| 14 | `<eta|xi> != 0` from oddness of `beta` (`CCM:852`) | automatic (`CS:871`, Hallouin-Perret Lemma 33) | M | `IH-15` |
| 15 | `T = QW - eps >= 0`, Toeplitz preserved | same | V | diagonal shift preserves Toeplitz |
| 16 | `D' = D - |D xi><eta|`, self-adjoint for `T` (`CCM:863`) | `U = Z^* - |Z^* xi><eta|`, **unitary** for `T` | M | `IH-11`, new; or self-adjoint via Cayley (`IH-13`) |
| 17 | `Det(D''-s) = Det(D-s) sum xi_j/(j-s)` (`CCM:869`) | `det(U''-w) = det(Z^*-w) K^{-1/2} sum xihat_n/(z_n-w)` | V | `IH-11`(iii) |
| 18 | `det_reg(D_log - z) = 1 - e^{-izL}` (`CCM:1120`) | `det(1-wZ) = 1-w^K` | V | no regularisation needed |
| 19 | `xi^` entire, zeros real = spectrum (`CCM:1085`) | `Ptilde` polynomial, zeros on `|w|=1` = `spec(U'')` | V | `IH-11`(iv) = `CS:792` = Makhoul 1981 |
| 20 | `mu_lambda` decreasing, `-> 0 => RH` (`CCM:668`) | `eps_M` non-increasing; `eps_M >= 0` forall M **iff** Ramanujan | M | becomes a finite equivalence, not a limit (`NG-8`) |
| 21 | convergence of the spectrum to the divisor | exact at `K = R+1` | F | trivialised; no approximation problem to study in the limit (`NG-3`) |
| 22 | Hermite/prolate strategy (`CCM:1216-1400`) | none | F | no theta, no Gaussian, no prolate; `Xi` is a polynomial (`NG-7`) |
| 23 | spectral triple, regularised determinant, infrared | finite unitary, ordinary determinant | M | `NG-9` |
| 24 | multiplicities | support only; Prony recovers weights | M | `IH-20`, `NG-11` |

---

## 9. Numerical checks for the numerics lane

Each check names the claim it tests and, where possible, an exact target. `ihara_proto.py` is the
lane; nothing below depends on its current state.

**A. The explicit formula (`IH-1`, `IH-3`).**
1. For Petersen, Heawood, `K_4`, `K_{3,3}`, the prism `C_16 x K_2` and one LPS graph: check
   `det(1-uB) = (1-u^2)^{|E|-|V|} det(1-Au+qu^2)` at random `u` (target `< 1e-12` relative).
2. Check `t_k` from `IH-3` against `sum_{A_ret} (mu/sqrt q)^k` for `k = 0..40`. Petersen targets:
   `t_0..t_7 = 18, -2.121320, -7.5, -3.181981, -6.75, 15.379572, 5.625, -11.402097`;
   `N_0..N_7 = 30, 0, 0, 0, 0, 120, 120, 0`.
3. Check `t_k` real and `t_{-k} = t_k` (`IH-1`), and that the *full* spectrum sequence
   `q^{-k/2} Tr B^k` is **not** invariant under the inverse pairing (`IH-1`(iv)) — a deliberate
   negative control.
4. Bipartite control: `K_{3,3}` or `C_16 x K_2`, check the `eps_bip` term is needed (omitting it
   leaves a residue of exactly `(-1)^k(q^{k/2}+q^{-k/2})`).

**B. Toeplitz, Loewner, displacement (`IH-7`, `IH-9`, `IH-10`).**
5. `That = F^* T F` matches `z_n(B_n-B_m)/(K(z_n-z_m))` off-diagonal and the Fejer mean
   `sum_d (1-|d|/K) t_d z_n^{-d}` on the diagonal (target `< 1e-12`). Check `a_{-n} = a_n`,
   `b_{-n} = -b_n`, `B_n` purely imaginary.
6. `rank(Z T Z^* - T) == 2` exactly, and the difference is supported on row `0` and column `0`.
7. **Negative control:** `rank([A, T])` for the angle operator `A = diag(2 pi n/K)` is *not* `2`
   (it should be full or near-full). This is `IH-10`(b) and it is the check that decides the
   candidate question.

**C. The key lemma (`IH-11`).**
8. `||U^* T U - T||` and `||U xi||` at machine zero for `K = 3..15`; `U` built as
   `Z^* - |Z^* xi><eta|` after normalising `xi_0 = 1`.
9. `spec(U) \ {0} == roots(sum_k xi_k w^{K-1-k})` to `1e-10`, and all moduli `= 1` when
   `dim ker(T - eps) = 1`.
10. `det(U''-w) == det(Z^*-w) K^{-1/2} sum_n xihat_n/(z_n-w)` on a grid of `w`.

**D. Cayley / `CS:1356` (`IH-13`).**
11. For odd `K`, build `Q = C S^* That S C` with `lambda_n = tan(pi n/K)`, `C = diag(sqrt(2K)
    cos(pi n/K))`; check `Q` real symmetric, `Q >= 0`, and `Q_{nm} = (b_n-b_m)/(lambda_n-lambda_m)`
    off-diagonal (target `< 1e-12`), with the **same** `b_n` as in check 5.
12. Roots of `P(s) = sum_k xi_k prod_{j!=k}(lambda_j - s)` are real and equal `tan(arg(w)/2)` for the
    returned `w`. Petersen `K = 5` target: `-2.414214, -0.691080, 0.691080, 2.414214`.
13. Check that `min spec Q != min spec T` (the cost of the congruence, `IH-14`(b)) — a control that
    the `eps`-shift must precede the transform.

**E. The three regimes (`IH-18`, `IH-19`, `IH-20`).**
14. Window scan `K = 2..3R` on Petersen. Targets: `eps_M = 15.878680, 9.447657, 5.712424, 0, 0, 0, 0`
    for `K = 2..8`; `dim ker(T - eps) = 1,1,1,1,2,3,4`; `rank T = 2,3,4,4,4,4,4`.
15. At `K = R+1 = 5`: roots `= exp(+- 3 pi i/4)` and `(1 +- i sqrt 7)/(2 sqrt 2)`, error `< 1e-13`.
    Prony weights `= (5,5,4,4)` to `1e-10` (`IH-20`).
16. At `K = 4` (under-resolved): roots `-1`, `0.026801 +- 0.999641 i`, all on the circle, none equal
    to a divisor point. This is the CCM regime on an object where the truth is known, and the natural
    place to measure "accuracy vs window".
17. At `K = 6,9` (over-resolved): the eigensolver's kernel vector has roots off the circle
    (`K = 6`: `-0.314767`; `K = 9`: `-2.875853`, `0.965951`, `0.796760 +- 2.135222 i`) and is
    neither palindromic nor anti-palindromic. Then check `CS:908`: the **intersection** of the zero
    sets over a basis of `ker T` is exactly the four divisor points.
18. Detect the critical window blind: increase `K` until `rank T` stabilises, step back one
    (`IH-21`(d)).

**F. Non-Ramanujan (`IH-26`, `IH-27`, `IH-28`).**
19. Prism `C_16 x K_2`: `eps_M` for `M = 1..25`. Targets: positive for `M <= 4`
    (`43.026, 38.158, 23.442, 6.008`), negative from `M = 5` (`-32.837`), and
    `eps_21 = -1351.2`. Closed-form prediction `-m rho^{K+1}/(rho^2-1)` with `rho = 1.124123`,
    `m = 2`: `-1297`.
20. Fit `d log(-eps_M)/dM`; target `2 log rho = 0.233702`. Report the successive-ratio estimate
    `eps_{M+1}/eps_M -> rho^2 = 1.263268` as well — it converges faster (`1.2826` at `M = 21`).
21. `max | |root| - 1 |` stays `< 1e-13` for all `M` (the construction never breaks, `IH-26`).
22. Root-angle gaps at large `M`: mean `-> 2 pi/(K-1)`, standard deviation decreasing. At `M = 21`:
    mean `0.148627` vs `0.149600`, sd `0.012038`. Push to `M = 40` in extended precision and report
    whether the sd decays (this is the open part of `IH-28`).
23. **Inverse problem:** from the slope of `log(-eps_M)` alone, recover the largest adjacency
    eigenvalue `lambda = sqrt q (rho + 1/rho)` and compare with the true `2 cos(pi/8) + 1 =
    2.847759`. If this works it is a genuinely new diagnostic.

**G. Graded / curve (`IH-33`, `IH-34`).**
24. An Artin-Schreier curve from `shard 06b` (`N_n = 1 + q^n - sum alpha_i^n`): build `t_k` with the
    fermionic sign, run the same code, recover the `alpha_i/sqrt q` at `K = R+1`. Cross-check
    against Hallouin-Perret's bound (`IH-35`).
25. A mixed-parity graded divisor (`prop:qubit-graded-zeta`, `03c:221`): confirm `eps_M` is
    indefinite for reasons unrelated to RH (`IH-36`) and that the returned circle spectrum is
    meaningless.

**H. Irregular (`IH-30`-`IH-32`).**
26. Any irregular graph: check the construction runs, `t_{-k} = t_k` holds, but `A_ret` is **not**
    invariant under `mu -> R_G^{-1}/mu`, so at `eps_M = 0` (if reached) the returned points are not
    the divisor.

**I. Precision.** The condition number of `T` at the critical window is moderate (Petersen `K = 5`:
`spec(T) = 0, 13.9576, 24, 25.7924, 26.25`), so double precision suffices for the checks above. The
non-Ramanujan runs at `M > 25` need extended precision because `eps_M` grows like `rho^{2M}` while
`||T||` grows like `K`; use the same `prec`-doubling driver as `plan:306`.

---

## 10. Questions I could not settle

**Q1 (`IH-21`).** Is there a canonical `xi` in the over-resolved regime that keeps the circle
conclusion, selected by the construction rather than by hand? A paraorthogonal family
`q_0(w)(w^d - beta)`, `|beta| = 1`, exists, but nothing in the CCM/CS chain picks a `beta`. Candidate
mechanism not tested: perturb `T -> T + delta * (|eta><eta| or the boundary rank-two term)` and let
`delta -> 0+`; does the kernel vector converge to a paraorthogonal one, and with which `beta`?

**Q2 (`NG-3`).** What is the discrete counterpart of CCM's accuracy law `eps_N ~ 10(1 -
chi_4(lambda))` (`plan:172`)? In the under-resolved regime `eps_M > 0` is the Pisarenko noise floor
of an *exact* `R`-atom measure observed with too few lags. I expect it to be governed by the minimal
angular separation of the `R` divisor points against the Fejer resolution `2 pi/K`, i.e.
`eps_M ~ c * (K * delta_min)^{2(R-K+1)}`-ish, but I have neither derived nor tested this. It is the
one quantitative question where the graph can genuinely inform the `zeta` case, because both sides
are computable.

**Q3 (`IH-17`).** Can the minimal eigenvector of a *graph's* `T` be anti-palindromic
(`J xi = -xi`)? `CS:865` allows both signs; CCM's `even-simple` asserts the `+` sign and lists it
among the missing steps (`CCM:1385`). Petersen gives `+` at `K = 4,5`. A search over small regular
graphs and window sizes for a `-` case would settle whether "even" is a theorem or a hypothesis over
`Z`, and would be cheap.

**Q4 (`IH-28`).** The exact weak-* limit of the returned measure for a non-Ramanujan graph. I predict
normalised Lebesgue on the circle with an `O(1/K)` modulation; proved only at leading order.

**Q5 (`IH-31`(d)).** For an irregular graph, is there a principled trivial divisor replacing
`{q, 1}`? The Perron pole survives; its "`H^0` partner" does not. Without it the `W_{0,2}` term is
rank one and the retained set is not FE-invariant even in principle. Related to
`obs:divisor-regular-data` cited at `02h:154`.

**Q6 (`IH-36`).** Is there a Krein-space version of `IH-11` for a mixed-parity retained divisor,
and does it say anything? The form is indefinite with a known signature `(p,n)` = (number of retained
poles, number of retained zeros), so a `J`-unitary version of `U''` exists formally; whether its
spectrum localises anywhere useful is open.

**Q7 (NG-7, the real one).** Is there *any* structure over `Z` playing the role of the Hermite/prolate
tower — i.e. a family of window-adapted test functions, self-dual under the `(Z, T)` Fourier
transform, whose transform is the completed zeta? For a finite graph the answer is no (the completed
zeta is a polynomial). For an *infinite* regular tree quotient, or for the Selberg zeta of
`plan:434`, the question is open and is the only place where a discrete model could touch CCM's
missing step. I did not investigate it.
