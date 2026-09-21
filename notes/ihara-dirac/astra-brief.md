# Brief for the prover: square roots of the Ihara--Bass formula (chiral linearisation, the oriented half, odd letters)

Role: you are `codex:gpt-6-astra`, the prover of this round. Orchestrator and author of the drafted
statements: `claude:fable-5.1`. Date 2026-09-21. Repository: `riemann-channel` (a lab book on zeta
functions as transfer matrices of quantum channels). Write your proofs to the file
`notes/ihara-dirac/astra-proofs.md` (create it; do not write anywhere else except scratch files under
`notes/ihara-dirac/scratch/`). Do not modify any other file in the repository.

Your task: prove or correct each of the statements T1--T4 below, in Lamport structure (numbered steps
`<1>1, <1>2, ...`, each a claim followed by its proof). Statements are drafted deliberately slightly too
strong; where a statement is false as drafted, state the corrected version, prove it, and record the
correction in a **correction ledger** at the end (one row per correction: label, what was drafted, what is
true, why). Declare every hypothesis you need as `H-<NAME>` in a hypothesis register. Give explicit
counterexamples where you refute something. Small explicit checks (e.g. the classical bouquet with two
loops) are welcome; you may run python3 (numpy available) for sanity checks but proofs must be complete
arguments, not numerics. Length: as long as needed; precision over prose.

## 0. Conventions (fixed; from `report/sections/08_quantum_ihara_general.tex` and `02h`, `03c`)

* `V` a finite-dimensional complex vector space, `N = dim V`. `D = 2m` letters, `iota` a fixed-point-free
  involution ("reversal") on `[D] = {1..D}`, `bar i = iota(i)`.
* `E_1..E_D in End(V)` arbitrary linear maps ("letters"). Edge space `W = V (x) C^D`, elements
  `x = sum_i x_i (x) |i>`.
* Quantum Hashimoto operator `H` on `W`: `H(v (x) |i>) = sum_{j != bar i} E_i v (x) |j>`;
  `zeta_H(u) = det_W(1 - uH)^{-1}`.
* Auxiliary maps: `R : W -> V`, `R(v (x) |i>) = E_i v` (propagate); `S : V -> W`, `S v = sum_j v (x) |j>`
  (start); `J : W -> W`, `J(v (x) |i>) = E_i v (x) |bar i>` (backtrack). Then `H = S R - J` (shard 08,
  step <1>1), and `det_W(1 + uJ) = prod_{pairs {i, bar i}} det_V(1 - u^2 E_{bar i} E_i)` (shard 08, <1>2).
* Deformed adjacency and degree: `A(u) = u sum_i E_i (1 - u^2 E_{bar i} E_i)^{-1}`,
  `D(u) = u^2 sum_i E_{bar i} E_i (1 - u^2 E_{bar i} E_i)^{-1}`.
* **Theorem (thm:qihara-general, proved, may be used):** for `u` with all `1 - u^2 E_{bar i} E_i`
  invertible, `det_W(1 - uH) = prod_{pairs} det_V(1 - u^2 E_{bar i} E_i) * det_V(1 + D(u) - A(u))`.
  Its proof shows `det_V(1 - u R (1 + uJ)^{-1} S) = det_V(1 + D(u) - A(u))`.
* **Unitary / inverse-paired case (cor:qihara-unitary, proved, may be used):** if `E_{bar i} = E_i^{-1}`
  then `det_W(1 - uH) = (1 - u^2)^{N(D-2)/2} det_V(1 - u Sigma + (D-1) u^2)`, `Sigma = sum_i E_i`.
* **Kraus case:** `V = M_n` (n x n matrices, Hilbert--Schmidt inner product), `E_i = Ad(A_i)`,
  `Ad(A) X = A X A^*`, `A_{bar i} = A_i^*`; then `E_{bar i} = E_i^*` (HS adjoint). Unitary Kraus case:
  `A_i = U_i` unitary, `E_{bar i} = E_i^{-1} = E_i^*`.
* Euler product (proved in shard 08, may be used): `zeta_H(u) = prod_{[w]} det_V(1 - u^{l(w)} E_w)^{-1}`
  over primitive cyclically non-backtracking classes `[w]` (cyclic words `w = (i_1..i_l)` with
  `i_{k+1} != bar i_k` cyclically, up to cyclic shift, not a proper power), `E_w = E_{i_l} ... E_{i_1}`.
  The **reverse** of `w` is `bar w := (bar i_l, ..., bar i_1)`; then `E_{bar w} = E_{bar i_1} ... E_{bar i_l}`.
* **Graded bond** (shard 02h/03c): `V_bond = V_+ (+) V_-`, parity `P = 1 (+) (-1)`, `dim V_+- = D_+-`.
  A letter `U` is homogeneous of parity `eps in {+1,-1}` if `P U P = eps U` (even = block diagonal,
  odd = block off-diagonal). `B(V_bond) = End(V_bond)` is graded by `Gamma_b := Ad(P)`, `X -> P X P`:
  even sector `= Hom(V_+,V_+) (+) Hom(V_-,V_-)` (dimension `n_0 = D_+^2 + D_-^2`), odd sector
  `= Hom(V_+,V_-) (+) Hom(V_-,V_+)` (`n_1 = 2 D_+ D_-`). For homogeneous unitary letters with
  `U_{bar i} = U_i^*`, `E_i = Ad(U_i)` commutes with `Gamma_b`, so `H` and `Sigma` commute with
  `Gamma_b (x) 1` and restrict to sectors `H_k`, `Sigma_k`, `k = 0, 1`. Supertrace `str X = Tr(Gamma_b X)`,
  superdeterminant `sdet(1 - uX) = det(1 - uX_0)/det(1 - uX_1)` for `X` commuting with the grading.
  **Graded quantum Ihara zeta** `:= 1/sdet(1 - uH) = det(1 - uH_1)/det(1 - uH_0)`; its zeros come from the
  odd sector. **Graded Ihara--Bass (thm:graded-qihara-bass, proved, may be used):** for the unitary
  homogeneous case `det(1 - uH_k) = (1 - u^2)^{n_k (D-2)/2} det(1 - u Sigma_k + (D-1) u^2)`, `k = 0, 1`.
  `q := D - 1`. **Ramanujan band** for a sector: every eigenvalue `lambda` of `Sigma_k` other than the
  trivial ones satisfies `|lambda| <= 2 sqrt q`; then both roots `mu` of `1 - lambda u + q u^2 = 0`
  (as `u = 1/mu`) have `|mu| = sqrt q`.
* **Left multiplication** `L_P : X -> P X` on `B(V_bond)`; in column-stacking `vec(PX) = (1 (x) P) vec X`.
* A **super vector space** `E = E_0 (+) E_1`; for an *even* operator `X = diag(X_0, X_1)`,
  `Ber(X) = det X_0 / det X_1`. For a block matrix `[[A, B],[C, D]]` with `A` on `E_0`, `D` on `E_1`
  and **c-number** off-diagonal blocks, the two "Schur" expressions `det(A - B D^{-1} C)/det D` and
  `det A / det(D - C A^{-1} B)` are both meaningful numbers; part of T1 is to show they differ.

## T1. Chiral linearisation; the Euler exponent as the Berezinian of the mass; no super coupling

On `E := W (+) V` define the block operators (blocks ordered `W` first)
```
  N(u) = [[ 1_W + uJ ,  S ],
          [   u R    , 1_V ]]  =  M(u) + Dslash(u),
  M(u) = diag(1_W + uJ, 1_V)  (even),   Dslash(u) = [[0, S],[uR, 0]]  (odd for the W/V grading).
```
(a) `det_E N(u) = det_W(1 - uH)`, by the Schur complement on the `V` block; and by the Schur complement on
the `W` block, `det_E N(u) = det_W(1 + uJ) det_V(1 - u R (1 + uJ)^{-1} S)`. Hence Theorem
`thm:qihara-general` is the statement that one determinant of the first-order pencil `N(u)` has two Schur
evaluations (this is the mechanism of Matsuura--Ohta, arXiv:2501.08803, for a graph, with the bouquet
and matrix weights here).
(b) **SUSY pairing.** Put `X := u R (1 + uJ)^{-1} : W -> V` and `Y := S : V -> W`. The nonzero spectra of
`X Y` on `V` and `Y X` on `W` coincide with algebraic multiplicities (Jacobson's lemma / Sylvester);
`Y X = u S R (1 + uJ)^{-1} = u (H + J)(1 + uJ)^{-1}`. On the super space `W_even (+) V_odd`, the even operator
`Lambda(u) := diag(Y X, X Y)` has `str Lambda(u)^k = 0` for all `k >= 1` and `sdet(1 - Lambda(u)) = 1`;
the index `dim W - dim V = N (D - 1)` counts the excess kernel of `Y X`. Ihara--Bass is the statement
`det_W(1 - uH) = det_W(1 + uJ) det_W(1 - Y X) = det_W(1 + uJ) det_V(1 - X Y)`.
(c) **Euler exponent as a Berezinian.** In the inverse-paired case `E_{bar i} = E_i^{-1}`:
`(1 - u^2)^{N(D-2)/2} = Ber_{W_even (+) V_odd}( diag(1_W + uJ, (1 - u^2) 1_V) )`, i.e. the Euler exponent
`N D/2 - N` ("edges minus vertices", `= -chi` for a graph) is the Berezinian of the *diagonal* mass term,
with the edge block even and the vertex block odd. (This is the parity convention `k + 1` for `k`-cells in
`def:graded-geodesic-determinant`.) State precisely what `Ber` means here and check the sign convention.
(d) **No Berezinian of the coupling.** For the block matrix `N(u)` with its c-number off-diagonal blocks,
the two Schur expressions for a would-be Berezinian on `W_even (+) V_odd` are
`det(1 + uJ - S u R)/det(1_V) = det_W(1 - uH)` and `det_W(1 + uJ)/det_V(1 - uR(1+uJ)^{-1}S) =
det_W(1 + uJ)^2 / det_W(1 - uH)`; they agree iff `det_W(1 - uH)^2 = det_W(1 + uJ)^2`, which fails in
general (give the smallest classical counterexample: the bouquet with two loops, `V = C`, `E_i = 1`, `D = 4`,
where `det(1 - uH) = (1 - u)^2 (1 + u)(1 - 3u)` and `det(1 + uJ) = (1 - u^2)^2`). Conclude: a Gaussian
Berezin integral with bosonic fields on `V` and fermionic fields on `W` coupled by the c-number Dirac blocks
is not defined (the exponent is not an even element of the Grassmann algebra), so the only super-object in
Ihara--Bass is the diagonal mass term of (c); the coupling must be evaluated as an ordinary determinant, as
Matsuura--Ohta do with fermions on both blocks. (You may state this as a proposition about the two Schur
expressions plus a remark about the integral; do not overclaim about "all possible" super formulations.)

## T2. The oriented half is a square root of the zeta on the real axis

Assume `E_{bar i} = E_i^*` for a fixed inner product on `V` (the Kraus case with HS adjoint, unitary or not).
(a) No primitive cyclically non-backtracking class is its own reverse: `[w] != [bar w]` for every `w`.
(Proof sketch: if `bar w` were a cyclic shift of `w`, the shift composed with reversal is an involution of
`Z/l` with, for `l` odd, a fixed point `i_0 = bar i_0` (impossible, `iota` fixed-point-free), and for `l`
even either a fixed point or an adjacent pair `i_{k+1} = bar i_k` (a backtrack). Check the `l` even case
carefully.)
(b) `det_V(1 - u^l E_{bar w}) = conj( det_V(1 - conj(u)^l E_w) )`.
(c) Hence, for real `u` with `|u|` small enough that the Euler product converges absolutely,
`det_W(1 - uH) = |F(u)|^2`, `F(u) := prod_{[w] in Pi} det_V(1 - u^{l(w)} E_w)`, where `Pi` contains exactly one
of `[w], [bar w]` for each pair. In particular `det_W(1 - uH) > 0` on the real interval of convergence.
State the radius: absolute convergence for `|u| < r` with `r` = ... (give a sufficient bound in terms of
`max_i ||E_i||` and `D`).
(d) Graded version: for homogeneous unitary letters with `U_{bar i} = U_i^*`, the same holds sector by
sector and for `sdet`: `sdet_W(1 - uH) = |F_gr(u)|^2` with `F_gr(u) = prod_{[w] in Pi} sdet_V(1 - u^{l(w)} E_w)`.
(e) `F` is in general **not** a polynomial (so it is not the determinant or Pfaffian of any finite matrix
pencil): in the classical bouquet with two loops, `det(1 - uH) = (1 - u)^2 (1 + u)(1 - 3u)` has simple real
roots at `-1` and `1/3`. Compare with Aizenman--Warzel (arXiv:1709.06052, Lemma "sq"): for a non-backtracking
flow matrix that is loopwise time-reversal invariant **and twist anti-symmetric**, `det(1 - uKW)` *is* the
square of a polynomial. Show that the Ad-weighted Hashimoto operator (and the classical one) is loopwise
time-reversal invariant in the trace sense (`Tr_V E_{bar w} = conj Tr_V E_w`) but twist **symmetric**
(the weight of a path `(e, e_1..e_{n-1}, bar e)` and of its twist `(e, bar e_{n-1}..bar e_1, bar e)` have
equal, not opposite, traces), so the Kac--Ward/Kasteleyn square root (a Pfaffian of a Dirac-type matrix,
Loebl--Somberg arXiv:0912.3200, Cimasoni arXiv:1307.2494) does not apply: the notebook's square root is the
modulus-squared one, the amplitude structure of a matrix-product state on prime cycles.

## T3. Odd letters make the Hashimoto operator chiral; the graded zeta is a square root

Graded bond, homogeneous unitary letters, `U_{bar i} = U_i^*`, parities `eps_i` (so `eps_{bar i} = eps_i`).
Let `Gamma := L_P (x) 1_{C^D}` on `W = B(V_bond) (x) C^D`.
(a) `Gamma^2 = 1`; `Gamma` commutes with `Gamma_b (x) 1` (so it preserves both sectors), and
`Gamma E_i Gamma = eps_i E_i` for each letter. Consequently `Gamma H Gamma = H^eps`, `Gamma J Gamma = J^eps`,
`Gamma Sigma Gamma = Sigma^eps`, where `X^eps` denotes the same construction with letters `eps_i E_i`
(the sign-character twist). Hence for every graded channel the sector determinants are invariant under
negating the odd letters: `det(1 - uH_k) = det(1 - uH_k^eps)`, `k = 0, 1`.
(b) **All letters odd** (`eps_i = -1` for all `i`; the index-two graded representation channels of
`def:index-two-grading`, e.g. Weil--LPS with all generators in the odd coset). Then `Gamma` anticommutes
with `H`, `J`, `Sigma` and with each `H_k`, `Sigma_k`: the spectra of `H_k` and `Sigma_k` are symmetric
under `lambda -> -lambda` with multiplicities, `det(1 - uH_k)` and `det(1 - u Sigma_k + q u^2)` are even
functions of `u`, and, writing `W_k = W_k^+ (+) W_k^-` for the `Gamma = +-1` eigenspaces inside sector `k`
and `H_k = [[0, h_k],[h_k', 0]]`,
```
   det(1 - uH_k) = det_{W_k^+}(1 - u^2 h_k h_k') = det_{W_k^+}(1 - u^2 H_k^2|_{W_k^+}),
```
so `1/sdet(1 - uH)` is the square root (normalised to `1` at `u = 0`) of `1/sdet(1 - u^2 H^2)` where
`H^2` is the two-step operator (letters `Ad(U_i U_j)`, `j != bar i`, all even). Give the analogous factorisation
of the Bass side: `Sigma_k = [[0, alpha_k],[beta_k, 0]]` with `beta_k = alpha_k^*` (HS self-adjointness of
`Sigma_k`, letters closed under adjoint), and
`det(1 - u Sigma_k + q u^2) = det_{+}((1 + q u^2)^2 - u^2 alpha_k alpha_k^*)`. Hence the Ramanujan band for
sector `k` (`|lambda| <= 2 sqrt q` for nontrivial `lambda`) is equivalent to
`spec(alpha_k alpha_k^*) subset [0, 4q]` off the trivial part: the graded Ramanujan property of an odd-letter
channel is a spectral bound on the *even two-step block* `Sigma_k^2|_{+}`.
(c) **Which block carries the zeros.** In the odd sector, `W_1^+ = Hom(V_-, V_+) (x) C^D` and
`W_1^- = Hom(V_+, V_-) (x) C^D` (or the reverse; fix the sign convention of `L_P` and state it), and
`H_1^2|_{W_1^+}` is the two-step Hashimoto-type operator with even letters `Ad(U_i U_j)` acting on the
mixed block `Hom(V_-, V_+)`; its eigenvalues are the squares `mu^2` of the odd edge eigenvalues, and the
zeros of the graded zeta are the `u` with `u^2 = 1/mu^2`. **RH for the graded channel** (every nontrivial odd
edge eigenvalue has `|mu| = sqrt q`) holds iff every nontrivial eigenvalue of the two-step odd block
`H_1^2|_{W_1^+}` has modulus `q`, iff (manifest Hilbert--Polya form) `q^{-1} H_1^2|_{W_1^+}` is
diagonalisable with unimodular nontrivial spectrum. Identify precisely which eigenvalues are "trivial"
here (from `+-1` factors of `(1 - u^2)` and from the `P`-mode; see (d)).
(d) **Perron pair and P-mode.** `Sigma_0 1 = D 1` and `Sigma_0 P = -D P` (`prop:p-mode` with all letters odd:
`P`-mode `= -D`); `Gamma` exchanges `1` and `P`, so `1 +- P` are the `Gamma`-eigenvectors and on
`span{1, P}` the operator `Sigma_0` is the chiral pair `diag(D, -D)`. The trivial edge eigenvalues are
`{q, 1, -q, -1}` (from `lambda = +-D`) plus the `+-1` from `(1 - u^2)^{n_k (D-2)/2}`.
(e) **Mixed parities.** Chirality fails as soon as one letter is even: the Pauli example of shard 03c
(`V = C^{1|1}`, letters `X, X, Y, Y, Z, Z`, `P = Z`) has even spectrum `{6, -2}` of `Sigma_0`, not symmetric.
State (a) as the general fact and (b)--(d) under the all-odd hypothesis `H-ODD`.
(f) **Continuum remark (no proof needed, one paragraph):** the symmetry `u -> -u` has no continuum analogue
as a symmetry of a Lindblad generator with odd jump operators (the jump term anticommutes with `Gamma`, the
anticommutator term `{L_i^* L_i, .}` commutes), so chirality is a lattice property.

## T4. The single layer: odd letters give an odd Hashimoto operator whose supertrace zeta is trivial

Same graded bond, all letters odd. Let `h` on `V_bond (x) C^D` be the single-layer Hashimoto operator with the
letters `U_i` themselves: `h(v (x) |i>) = sum_{j != bar i} U_i v (x) |j>`, graded by `P (x) 1`.
(a) `h` is odd: `(P (x) 1) h (P (x) 1) = -h`. Hence `det(1 - uh) = det_{+}(1 - u^2 h^2|_{+})` and
`str(h^k) = 0` for all `k >= 1`, so `sdet(1 - uh) = 1` identically: there is no single-layer graded zeta
for odd letters; the zeros of `1/sdet(1 - uH)` on the doubled bond are not squares of anything on the single bond.
(b) Representation-theoretic reading (index-two graded representation `pi = Ind_{G_0}^G pi_+`, all letters
in the odd coset): `det(1 - uh)^{-1}` is the Artin--Ihara `L`-function `L(u, pi)` of the bouquet, and by
induction `L(u, pi) = L(u, pi_+; Y) = L(u, pi_-; Y)` for the two-vertex quotient `Y = Cay(G,S)/G_0`, which
is why the supertrace `Tr(P U_w) = chi_+(w) - chi_-(w)` (for `w in G_0`) sums to zero over words of each
length. Prove (a) fully; for (b) give a proof or a precise citation-level argument (the Artin formalism for
graph coverings, Stark--Terras) and mark it `H-ARTIN` if you rely on it.
(c) Contrast: `str H^n = sum_w |Tr(P U_w)|^2 >= 0` on the doubled bond (`def:graded-hashimoto`) is a sum of
squared moduli of the single-layer supertraces, which is why the doubled bond can have zeros while the single
layer cannot: the square root of the doubled ring norm is the single-layer amplitude *per word*, not a
single operator.

## Output format

`notes/ihara-dirac/astra-proofs.md` with: a hypothesis register (`H-ODD`, `H-ARTIN`, ...); for each of
T1(a)--(d), T2(a)--(e), T3(a)--(f), T4(a)--(c) a statement (corrected if necessary) with status
`PROVED` / `PROVED-CORRECTED` / `REFUTED` / `CONDITIONAL-ON H-...`, and a Lamport-structured proof; a
correction ledger table; and a short list of what you consider the two or three most useful statements for
a lab book whose theme is "zeros of zeta functions as the odd spectrum of graded transfer channels".
