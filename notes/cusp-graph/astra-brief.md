# Brief for the prover: a finite graph with a cusp, its scattering, and the rebound channel

You are the prover in a mathematical research notebook (git repo, current directory). Author line
for everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/cusp-graph/astra-proofs.md`
(create it; overwrite if present). Do not edit anything else. Do not run git. You may run python3
(numpy, mpmath, sympy, scipy are installed) for checks, and you may read any file in the repo,
especially `report/sections/04h_rebound_state.tex` (the continuous-time rebound round you are now
discretising: one-exit no-event semigroup, renewal channel, admissible densities, invariant flags),
`report/sections/04_riemann_channel.tex` (the Lax--Phillips scattering symbol of the modular surface
and the compressed semigroup with one mode per zero), `report/sections/02h_definitions_graded_ramanujan.tex`
(the graded Ramanujan property on the divisor of a ring zeta) and `report/sections/08_quantum_ihara_general.tex`
(Ihara--Bass conventions). Be elementary and explicit; the reader will run numerics against every
formula. Do not pad.

## Why this problem

The notebook's Riemann channel (shard 04) is the Lax--Phillips semigroup of the modular surface with
the cusp forms removed: the surface has one cusp, only the angle-independent mode of a wave can escape
up the cusp, so the exit is one-dimensional, the reflection coefficient of that mode is the scattering
matrix `phi(s) = xi(2s-1)/xi(2s)`, its poles with `Re s < 1/2` are the zeros of zeta at `rho/2`, and
those poles are the eigenvalues of the compressed semigroup. Shard 04h then showed that ANY one-exit
no-event semigroup admits a conservative renewal completion (exit flux reinserted at a rebound density),
with the zeros protected as odd modes; the reviewer's verdict was that nothing about zeta is used and
the zeros are put in by hand. We want the simplest object where the arithmetic supplies the exit: a
finite graph with a cusp. The discrete model of a cusp is an infinite ray attached to a finite graph
with the weights of the quotient of the `(q+1)`-regular tree by a cusp stabiliser (Serre, "Trees",
II.1.6: the quotient of the tree by `GL_2(F_q[T])` is a ray `Lambda_0, Lambda_1, ...` in which `Lambda_0`
sends all `q+1` edges to `Lambda_1` and every `Lambda_n`, `n >= 1`, sends one edge up to `Lambda_{n+1}` and
`q` edges down to `Lambda_{n-1}`; vertex measure proportional to `1/|Stab|`). This round is the toy with
one cusp and a general finite core, NO arithmetic; the next round attaches the ray to the quotient graph
of a congruence subgroup `Gamma_0(N)` of `GL_2(F_q[T])`, where the scattering matrix is expected to be
built from Dirichlet `L`-functions over `F_q[T]`. Your job: set the toy up rigorously, prove the discrete
Lax--Phillips statements, transcribe the rebound round, and say exactly what is generic and what the
next round must supply.

## Conventions (Section 0 of your file must restate these and PROVE items C1 to C3)

- **The diagram `Y`.** A finite core: a real symmetric matrix `T_X` on `C^n` (a weighted graph, loops
  and multi-edges allowed), a distinguished vertex `v_0` with `P_0 = |v_0><v_0|`, a coupling `c > 0`, and
  a ray with vertices `r_1, r_2, ...`. The Hilbert space is `l^2(V_X) (+) l^2({1,2,...})` with counting
  measure, and the operator
  `T = T_X (+) T_ray + c(|v_0><r_1| + |r_1><v_0|)`,   `(T_ray g)(k) = g(k+1) + g(k-1)` for `k >= 2`, `(T_ray g)(1) = g(2)`.
  So `T` is bounded self-adjoint. This is the normalised form: in the tree-quotient picture the
  adjacency operator `A` on `L^2(Y, m)` with `m(Lambda_n) ~ q^{-n}` and `(A f)(Lambda_n) = f(Lambda_{n+1}) + q f(Lambda_{n-1})`
  becomes, after the unitary `g = m^{1/2} f` and division by `sqrt q`, exactly the standard path
  adjacency on the ray; state and prove this in C1, including the value of `c` for the pure tree
  quotient (`T_X = [0]` on the single vertex `Lambda_0`, `(Af)(Lambda_0) = (q+1) f(Lambda_1)`; I get
  `c^2 = q+1`, check it).
- **Spectral parameter.** `lambda = z + 1/z`. The map `z = q^{s - 1/2}` makes `|z| = 1` the critical line
  `Re s = 1/2`, `|z| < 1` the half plane `Re s < 1/2`, and the Eisenstein-type eigenfunctions of the tree
  `q^{-s h}` (with `h` the Busemann height up the cusp) into `q^{-h/2} z^{-h}`. Under this map the
  modular-surface conventions of shard 04 (poles of `phi` with `Re s < 1/2` are the eigenvalues of the
  compressed semigroup) become: eigenvalues of the compressed operator lie in `|z| < 1`.
- **Generalised eigenfunctions and the reflection coefficient.** For `|z| = 1`, `z != +-1`, seek
  `T g = lambda g` with `g(r_k) = z^{-k} + R(z) z^{k}` for `k >= 1` and `g_X` on the core. Let
  `G(lambda) = <v_0|(lambda - T_X)^{-1}|v_0>`. I get
  `c g(v_0) = 1 + R`,  `g_X = c (z^{-1} + R z)(lambda - T_X)^{-1}|v_0>`,  hence
  `R(z) = (1 - c^2 G(lambda) z^{-1}) / (c^2 G(lambda) z - 1)`.
  **C1.** Prove: `R` is a rational function of `z` with real coefficients, `|R(z)| = 1` on `|z| = 1`,
  `R(z) R(1/z) = 1` (the functional equation), `R(conj z) = conj R(z)`, and the determinant form
  `R(z) = det(lambda - T_X - c^2 z^{-1} P_0) / det(lambda - T_X - c^2 z P_0)`
  (use `det(lambda - T_X - a P_0) = det(lambda - T_X)(1 - a G(lambda))`), equivalently, with
  `p(z) := det(1 + z^2 - z T_X - c^2 P_0)` and `ptilde(z) := det(1 + z^2 - z T_X - c^2 z^2 P_0) = z^{2n} p(1/z)`,
  `R(z) = p(z)/ptilde(z)` up to a power of `z` you determine. State the degree of `R`.
- **C2 (classification of zeros and poles).** Prove: (i) the poles of `R` in `|z| < 1` are real and are
  exactly the `l^2` eigenvalues of `T` on `Y` outside the band `[-2, 2]` via `lambda = z + 1/z`, with
  eigenfunction decaying as `z^k` on the ray (the "trivial" spectrum; for the pure tree quotient these are
  `z = +-q^{-1/2}`, i.e. the constant function on the quotient and its bipartite twin); (ii) `R` has no
  non-real pole in `|z| < 1` (self-adjointness); (iii) the common factors of `p` and `ptilde` are exactly
  the eigenvalues of `T_X` whose eigenvectors vanish at `v_0` (the "cusp forms"; extended by zero they
  are `l^2` eigenfunctions of `T` on `Y`, embedded in the band when `|lambda| <= 2`), and `R` does not see
  them; (iv) define the **resonances** as the zeros of `R` (after cancellation) in `|z| < 1`, with
  multiplicity; show they are the roots in `|z| < 1` of `p` not shared with `ptilde`, that they are the
  self-consistent eigenvalues `lambda = z + 1/z` of the non-self-adjoint effective operator
  `T_X + (c^2/z) P_0` (the outgoing self-energy of the ray at `v_0`; the trivial ones use `c^2 z`,
  the incoming branch), that non-real resonances come in conjugate pairs, and give the count of
  resonances in terms of `n`, the number of trivial eigenvalues and the cusp-form multiplicities.
- **C3 (the pure cusp).** For the pure tree quotient (`n = 1`, `T_X = [0]`, `c^2 = q+1`) I get
  `R(z) = (z^2 - q)/(q z^2 - 1)`, poles `+-q^{-1/2}` (trivial), zeros `+-q^{1/2}` (outside), NO
  resonances, and `1/R(z) = q zeta_K(2s-1)/zeta_K(2s)` with `zeta_K(s) = 1/((1 - q^{-s})(1 - q^{1-s}))`
  the zeta function of `F_q(T)` (standard, no local source) and `z = q^{s-1/2}`: the exact analogue of
  `phi(s) = xi(2s-1)/xi(2s)`, with the pole at `s = 1` and the zero at `s = 0` and nothing else. Verify
  or correct, and say which of `R`, `1/R` plays the role of `phi` (incoming/outgoing convention), so that
  everything downstream is consistent.

## The objects to define (Section 1) and the statements to prove or correct (Sections 2 to 8)

- **T1 (discrete Lax--Phillips: the wave group and the one-exit contraction).** The discrete wave
  equation on `Y` is `u_{m+1} = T u_m - u_{m-1}`, first-order form `W(u, v) = (T u - v, u)` on
  `l^2(Y) (+) l^2(Y)`, with the conserved energy form `E(u, v) = ||u||^2 + ||v||^2 - Re <u, T v>`.
  (a) Prove `E` is `W`-invariant and that on the ray the equation has the exact d'Alembert solutions
  `u_m(k) = F(k + m) + B(k - m)` (finite propagation speed one), so `D_+` (outgoing: data supported on
  the ray moving up) and `D_-` (incoming) are `W`-invariant subspaces on which `W` acts as a unilateral
  shift of multiplicity ONE (this is the one-dimensional exit: only one function of one variable leaves
  through the cusp). (b) Let `H_LP` be the `E`-completion of the orthocomplement (in the sense you
  make precise) of the trivial eigen-data and the cusp-form data; prove `E > 0` there and `W` is unitary
  for `E`. (c) Define `K = H_LP (-) (D_+ (+) D_-)` and `Z = P_K W|_K`. Prove: `dim K` equals the number of
  resonances with multiplicity; `spec Z` = the resonances (or their reflection `1/conj z`: fix and state
  the convention, tied to C3); `Z^m -> 0`; and the defect identities `1 - Z^* Z = |j><j|`,
  `1 - Z Z^* = |j'><j'|` with `j, j'` explicit (the exit vectors; `j` is the compression of the first
  ray datum). Give `j` in the resonance eigenbasis and show `<k_i, j> != 0` for every resonance
  (no mode decoupled from the cusp), with the Gram matrix of the eigenvectors of `Z` in closed form if
  you can (the discrete analogue of `G_nm = i/(w_n - conj w_m)` of 04h: I expect `1/(1 - z_n conj z_m)`
  up to normalisation). (d) State the discrete Lax--Phillips theorem you use (scattering matrix =
  characteristic function of `Z`, Sz.-Nagy--Foias) as "standard (no local source)" and identify it
  with `R` or `1/R`.
- **T2 (the cusp trace formula, or what the cusp adds to the Ihara zeta).** With `u = z/sqrt q` the
  Bass determinant of a `(q+1)`-regular core is `det(1 - u A_X + q u^2) = det(1 + z^2 - z T_X)`, so `p`
  and `ptilde` are rank-one perturbations of the Bass determinant. (a) Give the closed-walk expansion
  of `log p(z)` and of `log ptilde(z)` on the core (walks with rank-one insertions at `v_0`), and hence
  the power sums of the resonances `sum_i z_i^m` as core walk counts corrected by the trivial and
  cusp-form roots. (b) Give `-(d/dz) log R(z)` as the difference of the two expansions: this is the
  toy's version of the cusp term of the trace formula (shard 09c: the prime comb sits in the
  logarithmic derivative of the scattering determinant). (c) Say precisely which closed walks on the
  infinite graph `Y` (walks that go up the ray and return) the ray self-energy `c^2 z` and `c^2/z`
  resum, so that in the arithmetic round one knows where a comb over irreducible polynomials would have
  to come from.
- **T3 (the renewal channel in discrete time).** Let `C` be a contraction on a finite-dimensional `K`
  with `1 - C^* C = |j><j|` and `C^m -> 0` (take `C = Z` or `Z^*`, whichever has the exit `j` of T1(c);
  say which). For a density `Omega` on `K` define `E_Omega(rho) = C rho C^* + <j|rho|j> Omega`. Prove:
  (a) `E_Omega` is CPTP with Kraus operators `C` and `sqrt(p_i) |omega_i><j|` (spectral decomposition
  of `Omega`); (b) the holding-time law `m_Omega(m) = <j|C^{m-1} Omega C^{*(m-1)}|j>`, `m >= 1`, is a
  probability law with mean `mu_Omega = sum_{m >= 0} Tr(C^m Omega C^{*m}) < infinity` (finite
  dimension: the infinite-mean phenomenon of 04h cannot occur here; say so); (c) `rho_inf =
  mu_Omega^{-1} sum_{m >= 0} C^m Omega C^{*m}` is stationary, and it is the UNIQUE stationary density
  and attracts every density iff the holding law is aperiodic (`gcd{m : m_Omega(m) > 0} = 1`); give
  the periodic counterexample and say whether aperiodicity is automatic when `Omega` has support on a
  non-real resonance; (d) `rho_inf` is mixed iff `Omega` is not a pure state that is ... (decide: when
  is `rho_inf` pure?); (e) the rank-one identity `det(1 - u E_Omega) = det(1 - u E_0)(1 - mhat_Omega(u))`
  with `E_0(rho) = C rho C^*` and `mhat_Omega(u) = sum_m m_Omega(m) u^m`, and the eigenvalue-persistence
  criterion for the products `z_a conj z_b` (transcribe `prop:rebound-persistence-secular` of 04h).
- **T4 (mode-diagonal rebounds and the uniform-modulus criterion).** With `C k_i = z_i k_i` (or the
  reflected convention), for `Omega` a mixture of normalised eigenvectors, compute `mu_Omega =
  sum_i p_i/(1 - |z_i|^2)`, and prove `rho_inf = Omega` for every finitely supported mode-diagonal
  `Omega` on a family of distinct resonances iff all `|z_i|` in the family coincide (the discrete
  `prop:mode-diagonal-rebound-rh`). Under uniform modulus `r` the mean holding time is `1/(1 - r^2)`,
  independent of the mixture; with the arithmetic normalisation `r = q^{-1/4}` this is
  `1/(1 - q^{-1/2})`; compare with `mu = 2` of 04h (continuous rate `1/4`). Note the Gram matrix makes
  the spectrum of `rho_inf` a Gram spectrum, not the weight list (04h reviewer's point); state it.
- **T5 (admissibility and flags, transcribed).** A density `sigma` on `K` is stationary for some
  `E_Omega` iff `Q_sigma := sigma - C sigma C^* >= 0`; then `Omega = Q_sigma/Tr Q_sigma` is unique and
  `Tr Q_sigma = <j|sigma|j>`. For any `C`-invariant flag `V_1 c ... c V_N` with projections `P_k`,
  `Q_k = P_k - C P_k C^* >= 0`, and `sigma = sum_k (p_k - p_{k+1}) P_k` is admissible with the
  prescribed spectrum (the discrete `thm:flag-spectrum-attainable`; it holds for EVERY contraction
  with `C^m -> 0`, so say explicitly that nothing about the graph is used here either). Give the Schur
  (entrywise) form of `Q_sigma >= 0` in the resonance basis with the Gram matrix of T1(c).
- **T6 (the graded space and the trivial spectrum as a candidate even sector).** On `C vac (+) K`
  with `vac` even and `K` odd, transcribe `prop:odd-modes-protected`: for every rebound density on the
  graded space the odd operators `|k_i><vac|` are eigen-operators with eigenvalue `z_i` (or its
  conjugate), because the exit functional vanishes on odd operators. Then address the graph-specific
  question: the trivial `l^2` eigenfunctions of `T` on `Y` (C2(i)) are the discrete analogue of the
  constant function of the modular surface, i.e. of the pole at `s = 1`, which in the notebook is the
  even sector carrying the stationary state. Is there a natural way to let the vacuum BE the trivial
  eigen-data, so that the even sector is supplied by the graph rather than adjoined by hand? Under the
  wave group the trivial eigen-data are stationary and do not leak, so the answer may be no; say what
  the obstacle is (04h's "the vacuum needs an exit"), and whether the indefiniteness of `E` on the
  trivial data (the Lax--Phillips modified energy form) offers anything.
- **T7 (what "Ramanujan" and "RH" mean for the diagram, and whether they are independent).** Define
  RAM(Y): every `l^2` eigenvalue of `T` on `Y` other than the Perron eigenvalue and its bipartite twin
  lies in `[-2, 2]` (Morgenstern's Ramanujan diagram, in normalised form; for the pure tree quotient
  the two trivial eigenvalues are exactly the Perron pair). Define RH(Y): all resonances share one
  modulus `r`. (a) Show by examples (a one-vertex core with a loop of weight `a`, then small cores) that
  RAM and RH are independent conditions, or prove an implication if there is one. (b) Is `r` forced,
  e.g. by the product of all roots of `p` (I get `prod = 1 - c^2` up to sign), or by a symmetry? For the
  modular surface `r = q^{-1/4}` corresponds to `Re rho = 1/2`; what would force `q^{-1/4}` here? (c)
  Give a necessary and a sufficient condition on `(T_X, v_0, c)` for RH(Y) that is checkable, if one
  exists (e.g. in terms of `p` being, after removing the trivial and cusp factors, a scaled
  self-reciprocal polynomial). (d) Give the smallest core (fewest vertices) with at least one
  non-real resonance pair, and the smallest with RH(Y) and a non-real pair.
- **T8 (what the arithmetic round must supply).** One paragraph. For `Gamma_0(N) < GL_2(F_q[T])`,
  the quotient graph is a finite core with `h` cusps (rays of the above type, with the junction weights
  from the stabilisers). List exactly which of T1--T7 are generic (hold for every finite core and
  every `h`, after the obvious matrix generalisation to `h` exits) and which the arithmetic must supply:
  the identification of the `h x h` scattering matrix with Dirichlet `L`-functions over `F_q[T]`, the
  resonances as `L`-zeros at `|z| = q^{-1/4}`, the diamond (Galois) action as the level-`N` grading, and
  the cusp comb over monic irreducibles. Do NOT assert the `L`-function identification; state it as
  the hypothesis H-ARITH the next round must verify from sources.

Declare every hypothesis you need as `H-*` (e.g. H-SIMPLE: simple resonances; H-APERIODIC).

## Output format

`notes/cusp-graph/astra-proofs.md`, in Markdown with `$...$` math (or plain ASCII math), with:
0. Author line, list of hypotheses `H-*`, and Section 0 (conventions, C1 to C3 with proofs).
1. Sections 1 to 8 for the definitions and T1 to T8, each statement labelled `T<n>` (and `T<n>(a)`
   etc.), each with STATUS one of PROVED / PROVED-CONDITIONAL (on which H-*) / CORRECTED (state the
   corrected version, then prove it) / OPEN (say exactly what is missing).
2. A **correction ledger**: a numbered table of every place where my draft was wrong, too strong, or
   needed a hypothesis, with the fix.
3. Numerical checks: any python you ran, with the numbers; keep it short. Include at least: the
   one-vertex-loop core for several `(a, c)`, one random 4-vertex core, and the pure cusp.
4. A closing list "What a refuter should attack first", 3 to 5 lines.

Standard facts (Sz.-Nagy--Foias model theory, discrete Lax--Phillips, the renewal theorem, GKLS,
Serre's description of `GL_2(F_q[T])\T`) may be cited as "standard (no local source)" per the
notebook's convention; anything from the notebook cite by claim id and `report/sections/<file>:<line>`.
