# Brief for the prover: H-ARITH over F_q[T]. The scattering matrix of Gamma_1(N) < GL_2(F_q[T]) on the Bruhat--Tits tree for a prime-level N (linear, quadratic, cubic), its diamond/character blocks, the completed Dirichlet L-functions of F_q[T] with the infinity factor, and the exact finite-cavity structure of the local factors

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/h-arith-fqt/astra-proofs.md` (create it;
overwrite if present) and, if you want scratch computations, python files under `notes/h-arith-fqt/checks/`.
Do not edit anything else. Do not run git. python3 with numpy, mpmath, sympy is installed; finite-field
polynomial arithmetic in python is expected (small `q = 2, 3, 5`). Read first:

1. `notes/deninger-cusp/astra-proofs.md` (this morning's lane over `Q`; binding conventions): D3.1 the cusps of
   `Gamma_1(N)` over `Q`; D3.3–D3.5 the prime-level scattering matrices with all constants, `Phi_psi(s) = [[0, A_psi],[A_{bar psi}, 0]]`,
   `A_psi(s) = q^{1/2-s} Lambda_psi(2s-1)/Lambda_psi(2s)`, the trivial block `Phi_1(s) = phi(s)/(q^{2s}-1) [[q-1, q^s - q^{1-s}],[q^s - q^{1-s}, q-1]]`,
   the determinant (D3.16), the residue; D4 twisted theta edges; D5 the model decomposition with local factors and
   delays; **D6: "SHARPENED over F_q[T]: the double-coset correspondence, inducing-character bookkeeping, constant-term
   intertwining, finite Fourier transform, and finite-dimensional defect algebra have analogues. The real Gaussian,
   gamma factor, logarithmic continuous clock and T log T argument do not transfer verbatim to a tree quotient. A
   cubic-level calculation must specify the subgroup including determinant and scalar-center conditions, singular
   cusps, cusp heights, local new/old bases, and the infinity representation."** and the Rosen degree facts (even
   `chi`: `L(u, chi)` of degree `d - 1` with the factor `1 - u` removed by the infinity Euler factor; odd `chi`: degree
   `d - 1`, infinity ramified).
2. `report/sections/04o_graded_toys_exits.tex` (`obs:level-tower-correction`, `asm:h-arith-gamma1`: the assumption
   this lane must settle — "for Gamma_1(N) < GL_2(F_q[T]) the scattering matrix is diagonalised by the Dirichlet
   characters chi of (F_q[T]/N)^x, the chi-channel being a monomial in z times L(2s-1, chi)/L(2s, chi) with L the
   completed L-function (Euler factor at infinity included), and the diamond operators act on the chi-channel by chi";
   `prop:character-channel-graded-bond`, `conj:galois-graded-bond`, `obs:graded-toys-next`),
   `report/sections/04i_cusp_graph_scattering.tex`, `04j_cusp_graph_renewal.tex` (a finite graph with a cusp:
   scattering on trees, `z = q^{s-1/2}`-type variable), `04k_elliptic_cavity_scattering.tex` (`thm:multi-exit-scattering`:
   `S(z) = -Q(z)^{-1} Q(1/z)`, `det S = (-1)^h p/ptilde`), `04p_gl1_bond.tex` (`prop:cusps-are-class-group-bond`, H-CLASS:
   the scattering matrix at equal depth is a Pic-group matrix block-diagonalised by the Fourier transform in 2x2
   blocks on inverse pairs of characters), `02d_definitions_complexes.tex` (trees, buildings), `03f_selberg_letters_finite.tex`.
3. Sources in `refs/src`: search for `lorscheid` (Lorscheid, "Graphs of Hecke operators", "Automorphic forms for
   elliptic function fields": the quotient graphs `GL_2(R) \ T` and the constant terms), `gekeler`, `nonnenmacher`,
   `kondo`, `kaneko` (the level constant term over `F_q[T]` at one cusp: `cit:kk-level-constant-term` if present in
   the shards), `weil` (Weil's "Dirichlet series and automorphic forms" / adeles and algebraic groups for the function
   field Eisenstein series); quote by file and line; everything else marked "not byte-cited" with author and year.

Be explicit and computational: every matrix below is finite and exact (rational functions of `u = q^{-s}`).
A numerics lane will rebuild the quotient graph and the constant terms for `q = 2, 3` and small `N` and test every
displayed matrix; a hostile reviewer will try to refute every claim. Label PROVED, REFUTED, SHARPENED or OPEN.
Keep a correction ledger. Do not pad.

## 0. Why this round

Over `Q` the prime-level scattering matrix of `Gamma_1(q)` is now explicit: a `2 x 2` block per even nebentypus with
entries `q^{1/2-s} Lambda_psi(2s-1)/Lambda_psi(2s)` and a rational trivial block, and `asm:h-arith-gamma1`'s "one diagonal
monomial-times-`L` channel per character" was refuted as a `Q` statement (two cusp coordinates per even nebentypus;
local rational factors; odd characters excluded in weight zero). The function-field version is the one the notebook
actually wants (the cusps of `GL_2(F_q[T])`-type quotients are the class-group bond, the tree quotient is a finite
diagram, all `L`-functions are polynomials): settle `asm:h-arith-gamma1` over `F_q[T]`, exactly.

## 1. Claims

**H1 (the quotient graph and the cusps).** For `A = F_q[T]`, `K = F_q(T)`, the place `infinity`, and `N in A` monic
of degree `d`, define `Gamma_0(N), Gamma_1(N) < GL_2(A)` (say precisely: with or without the scalar centre; the
determinant condition; the notebook uses `GL_2(R)` for a coordinate ring `R`, `prop:cusps-are-class-group-bond`).
Prove: the quotient `Gamma_1(N) \ T` of the Bruhat--Tits tree `T` of `PGL_2(K_infinity)` (degree `q + 1`) is a finite
graph with finitely many cusps (rays), the cusps of `Gamma_0(N)` in bijection with `{(d_1, class): d_1 | N, ...}` and those of
`Gamma_1(N)` with the analogue of D3.1 (give the exact parametrisation and count `h_1(N)` for `N` prime of degree 1, 2, 3;
for `N = T` or a degree-one prime, `Gamma_0(N) \ T` is the classical two-cusp picture of Serre/Gekeler; state the
structure of the finite part: how many vertices and edges, and which vertices carry nontrivial stabilisers, for
`q = 2, 3` and `deg N = 1, 2, 3`). Cite Gekeler / Serre (Trees, II.2) / Nonnenmacher for the shape of `GL_2(A) \ T`
(a ray) and the level `N` covers; not byte-cited unless present.

**H2 (Eisenstein series and the constant terms).** Define the Eisenstein series at each cusp of `Gamma_1(N)` with a
Dirichlet character `psi` of `(A/N)^x` (weight zero, i.e. functions on vertices of `T`; say what "even" means here:
`psi` trivial on `F_q^x`, the scalar centre) and prove the constant-term formula at every cusp: incoming term
`u^{-deg}`-type times the cusp height and outgoing term with coefficient a ratio of **completed** Dirichlet
`L`-functions of `A` (`L(u, chi) = sum_{f monic} chi(f) u^{deg f}`, a polynomial of degree `d - 1` for primitive `chi != 1`
of conductor degree `d`; the infinity factor `(1 - u)^{-1}` for even `chi`, none (or a different one) for odd `chi`:
fix it from Rosen/Weil and state the completed `Lambda(u, chi)` with its functional equation
`Lambda(u, chi) = epsilon(chi) (sqrt q u)^{d - 2 or d - 1} Lambda(1/(qu), bar chi)`, with the Gauss sum). The result to
prove or refute: the scattering matrix `Phi_N(u)` in the class-character basis is block-diagonal with, for each even
`psi`, a `2 x 2` block `[[0, A_psi(u)],[A_{bar psi}(u), 0]]` with `A_psi(u) = (monomial in u, from the cusp heights and the
conductor) times Lambda_psi(q^{-1} u^2...)`-type ratio `Lambda(2s-1, psi)/Lambda(2s, psi)` in the variable `u = q^{-s}`,
plus a rational trivial block with the `xi`-analogue `zeta_A`-ratio (`zeta_A(s) = 1/(1 - q^{1-s})`, completed
`(1 - q^{-s})^{-1}(1 - q^{1-s})^{-1}`: so the trivial block's "`xi`-ratio" is an explicit rational function: compute
it). If odd `psi` are excluded in weight zero exactly as over `Q` (the scalar centre acts on vertex functions
trivially), say so and give the odd analogue (functions on edges? the sign character on the tree's bipartition?).

**H3 (the theorem for prime level, all three degrees).** For `N` a monic prime of degree `d = 1, 2, 3` over `F_q`, give
`Phi_N(u)` completely: the trivial block (a rational `2 x 2` matrix in `u` — the function-field twin of D3.11, with
`q^s -> u^{-1}`), and the character blocks with all constants (Gauss sums `tau(psi)` of `A/N`, `epsilon(psi)`), the
functional equation `Phi_N(u) Phi_N(1/(qu)) = I` (check), the determinant, the "residue" (the pole at `u = q^{-1}`,
the constant function; its rank), and the count: `h_1(N)` cusp coordinates `=` (number of even characters) `x 2`
`+` (trivial) — check against H1. This settles `asm:h-arith-gamma1`: state exactly which parts survive (the
`L`-ratio per character with the completed `L`) and which are refuted (diagonal vs `2 x 2` blocks; "monomial in
`z`" vs the finite rational factors of the trivial block; the diamond action `psi` on the whole block vs the two
`L`-labels `psi, bar psi`).

**H4 (the local factors are a finite cavity; the model space).** The trivial block's rational matrix is, in the
notebook's language, the scattering matrix of a finite diagram with two cusps (`thm:multi-exit-scattering`): identify
its core (`n`, `T_X`, couplings), `p(z)`, `ptilde(z)`, its resonances and bound states, exactly as the sibling lane
`notes/level-local-cavity/` is doing over `Q` (read its `astra-proofs.md` if it exists by the time you get here; do not
wait for it). Here everything is a polynomial: the "arithmetic" part is `Lambda(u, psi)` of degree `d - 2` (even) and the
"local" part is the rational cavity factor; so the level-`N` model space of `def:h-exit-renewal-channel`/`thm:h-exit-model`
is finite-dimensional: compute its dimension `deg det Theta` for `q = 2, 3`, `d = 1, 2, 3`, split into arithmetic modes
(the zeros of the `L`-polynomials: `(d - 2)` per even nontrivial character, all of modulus `q^{-1/2}` by Weil) and
local modes (the cavity's resonances), and the number of exits. Then H-CLASS: is the character-block structure the
Fourier transform on the "class group" of cusps (`(A/N)^x/F_q^x` at prime level, two torsors), matching
`prop:cusps-are-class-group-bond`(a)'s `2 x 2` blocks on inverse pairs of characters? State the exact correspondence
between the `Q`-side D3 structure and this one.

**H5 (what this changes).** One structured page: `asm:h-arith-gamma1` settled (corrected statement); the level-`N`
function-field cavity as the first fully finite instance of "arithmetic modes + local cavity + one exit per cusp
coordinate"; what `conj:galois-graded-bond` and `prop:character-channel-graded-bond` (odd-only graded bond of a
character channel) become; the elliptic-function-field case (`R` the coordinate ring of an affine elliptic curve,
the notebook's D2/D3 diagrams of 04k) as the next target: does the same theorem hold with `Pic^0` characters replacing
`(A/N)^x`, i.e. is H-CLASS the level-one case of this theorem for a curve of genus one? Two paragraphs; mark speculation.

## 2. Output format

`notes/h-arith-fqt/astra-proofs.md`: ledger table (H1–H5, verdicts); full proofs with hierarchical steps; external
theorems stated precisely, marked "not byte-cited"; repo sources quoted by file and line; a section "Numerical checks
for the blind lane" (explicit: the quotient graph of `Gamma_0(N)` and `Gamma_1(N)` for `q = 2`, `N = T`, `N = T^2 + T + 1`,
and one cubic; the constant terms by direct summation over a truncated orbit; the `2 x 2` blocks at two values of
`u`; the functional equation; the determinant; the dimension of the model space); a section "Corrections to the
brief"; and a closing "What this changes in the notebook" with statuses and one-sentence statements.

## 3. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts `PENDING`)
before you start, and after finishing each claim rewrite the file with that claim's section and its updated ledger
row. If you are resumed after an interruption, read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/h-arith-fqt/progress.txt` with the
claim you are working on.
